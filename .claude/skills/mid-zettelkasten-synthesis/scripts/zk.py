"""제텔카스텐 저장소를 읽고 쓰는 공통 유틸.

이 파일은 단독 실행하지 않는다. index_notes.py 와 check_links.py 가 import 한다.
Python 3 표준 라이브러리만 사용한다.
"""

import os
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote

# 스키마 허용 값 — references/note-schema.md 와 일치시킨다.
ALLOWED_TYPES = {"concept", "claim", "practice", "question", "tension", "example"}
ALLOWED_STATUS = {"seed", "growing", "evergreen"}

FENCE_RE = re.compile(r"^\s*(```|~~~)")
LINK_RE = re.compile(r"\[([^\]\n]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
H1_RE = re.compile(r"^#\s+(.*)$")


def find_root(explicit=None):
    """제텔카스텐 루트를 찾는다. 못 찾으면 종료한다."""
    candidates = []
    if explicit:
        candidates.append(Path(explicit))
    else:
        project = os.environ.get("CLAUDE_PROJECT_DIR")
        if project:
            candidates.append(Path(project) / "zettelkasten")
        candidates.append(Path.cwd() / "zettelkasten")
        candidates.append(Path.cwd())

    for c in candidates:
        if (c / "notes").is_dir():
            return c.resolve()

    tried = ", ".join(str(c) for c in candidates)
    sys.exit(f"[오류] notes/ 를 가진 제텔카스텐 루트를 찾지 못했다. 시도: {tried}\n"
             f"       --root <경로> 로 직접 지정하라.")


def parse_scalar(raw):
    """YAML 스칼라 한 줄을 파싱한다. 문자열 또는 문자열 리스트만 지원한다."""
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip("\"'") for item in inner.split(",") if item.strip()]
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    return raw


def parse_frontmatter(text):
    """(frontmatter dict, 본문 시작 줄번호) 를 돌려준다. frontmatter 가 없으면 (None, 0)."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, 0

    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, 0

    fm = {}
    for line in lines[1:end]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, _, value = stripped.partition(":")
        fm[key.strip()] = parse_scalar(value)
    return fm, end + 1


def strip_code_blocks(text):
    """펜스 코드블록을 같은 줄 수의 빈 줄로 치환한다. 줄번호는 보존된다."""
    out = []
    fence = None
    for line in text.split("\n"):
        m = FENCE_RE.match(line)
        if fence is None and m:
            fence = m.group(1)
            out.append("")
            continue
        if fence is not None:
            out.append("")
            if line.strip().startswith(fence):
                fence = None
            continue
        out.append(line)
    return "\n".join(out)


class Doc:
    """제텔카스텐 문서 하나."""

    def __init__(self, path, root):
        self.path = path
        self.root = root
        self.rel = path.relative_to(root).as_posix()
        self.slug = path.stem
        self.kind = self.rel.split("/")[0] if "/" in self.rel else "root"
        self.raw = path.read_text(encoding="utf-8")
        self.frontmatter, self.body_start = parse_frontmatter(self.raw)
        self.text = strip_code_blocks(self.raw)

    @property
    def fm(self):
        return self.frontmatter or {}

    @property
    def title(self):
        value = self.fm.get("title")
        if isinstance(value, str) and value.strip():
            return value.strip()
        return self.h1 or self.slug

    @property
    def h1(self):
        for line in self.text.split("\n")[self.body_start:]:
            m = H1_RE.match(line)
            if m:
                return m.group(1).strip()
        return None

    @property
    def tags(self):
        value = self.fm.get("tags")
        if isinstance(value, list):
            return [str(t) for t in value]
        if isinstance(value, str) and value.strip():
            return [value.strip()]
        return []

    @property
    def note_type(self):
        return self.fm.get("type") if isinstance(self.fm.get("type"), str) else None

    @property
    def status(self):
        return self.fm.get("status") if isinstance(self.fm.get("status"), str) else None

    def summary_line(self):
        """제목 바로 다음의 첫 문단 한 줄. 없으면 빈 문자열."""
        seen_h1 = False
        for line in self.text.split("\n")[self.body_start:]:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#"):
                seen_h1 = True
                continue
            if seen_h1:
                return stripped
        return ""

    def links(self):
        """(줄번호, 링크텍스트, 원본 타깃) 목록. 코드블록 안은 제외한다."""
        found = []
        for lineno, line in enumerate(self.text.split("\n"), start=1):
            for m in LINK_RE.finditer(line):
                found.append((lineno, m.group(1), m.group(2)))
        return found

    def wikilinks(self):
        found = []
        for lineno, line in enumerate(self.text.split("\n"), start=1):
            for m in WIKILINK_RE.finditer(line):
                found.append((lineno, m.group(1)))
        return found

    def resolve(self, target):
        """상대 링크 타깃을 실제 경로로 변환한다. 외부/앵커 링크는 None."""
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            return None
        clean = unquote(target.split("#")[0])
        if not clean:
            return None
        return (self.path.parent / clean).resolve()


def load(root):
    """루트 아래 모든 .md 문서를 읽는다."""
    docs = []
    for path in sorted(root.rglob("*.md")):
        docs.append(Doc(path, root))
    return docs


def notes_of(docs):
    return [d for d in docs if d.kind == "notes"]


def maps_of(docs):
    return [d for d in docs if d.kind == "maps"]


def normalize(text):
    """검색·중복 비교용 정규화. 대소문자와 유니코드 형태를 통일한다."""
    return unicodedata.normalize("NFC", text).casefold()
