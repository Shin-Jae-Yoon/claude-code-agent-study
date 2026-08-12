#!/usr/bin/env python3
"""제텔카스텐의 링크·스키마·고립 상태를 결정론적으로 검사한다 — 합성을 마친 뒤 실행한다.

사람이 눈으로 훑던 SKILL.md 의 '마무리 점검'을 그대로 옮긴 것이다.
오류가 하나라도 있으면 종료 코드 1 로 끝난다.

사용:
  python3 check_links.py
  python3 check_links.py --root /path/to/zettelkasten
"""

import argparse
import sys
from collections import Counter, defaultdict

import zk


def main():
    parser = argparse.ArgumentParser(description="제텔카스텐 무결성 검사")
    parser.add_argument("--root", help="제텔카스텐 루트 (기본: $CLAUDE_PROJECT_DIR/zettelkasten)")
    parser.add_argument("--quiet", action="store_true", help="오류만 출력하고 경고는 생략")
    args = parser.parse_args()

    root = zk.find_root(args.root)
    docs = zk.load(root)
    notes = zk.notes_of(docs)
    maps = zk.maps_of(docs)

    errors = []    # (위치, 메시지)
    warnings = []

    note_paths = {n.path for n in notes}
    inbound = defaultdict(set)   # 메모 경로 -> 링크를 건 문서 slug 집합
    link_total = 0

    # 1. 파일명 대소문자 충돌
    by_lower = defaultdict(list)
    for d in docs:
        by_lower[(d.kind, d.slug.casefold())].append(d.rel)
    for (kind, slug), rels in sorted(by_lower.items()):
        if len(rels) > 1:
            errors.append((f"{kind}/", f"대소문자만 다른 파일명 충돌: {', '.join(rels)}"))

    # 2. 문서별 검사
    for doc in docs:
        # 2-1. 링크 유효성 — 모든 문서 공통
        for lineno, text, target in doc.links():
            link_total += 1
            resolved = doc.resolve(target)
            if resolved is None:
                continue
            if not resolved.exists():
                errors.append((f"{doc.rel}:{lineno}", f"링크 대상 없음: {target}"))
            elif resolved in note_paths:
                inbound[resolved].add(doc.rel)
            if text.strip() == "":
                warnings.append((f"{doc.rel}:{lineno}", f"링크 텍스트가 비어 있다: {target}"))

        # 2-2. 위키 링크 금지
        for lineno, inner in doc.wikilinks():
            errors.append((f"{doc.rel}:{lineno}", f"위키 링크는 쓰지 않는다: [[{inner}]]"))

        # 2-3. 원자 메모 스키마 — notes/ 만
        if doc.kind != "notes":
            continue
        if doc.frontmatter is None:
            errors.append((doc.rel, "frontmatter 가 없거나 --- 로 닫히지 않았다"))
            continue
        if not doc.fm.get("title"):
            errors.append((doc.rel, "frontmatter 에 title 이 없다"))
        if doc.note_type not in zk.ALLOWED_TYPES:
            errors.append((doc.rel, f"type 값이 잘못됐다: {doc.note_type!r} "
                                    f"(허용: {', '.join(sorted(zk.ALLOWED_TYPES))})"))
        if doc.status not in zk.ALLOWED_STATUS:
            errors.append((doc.rel, f"status 값이 잘못됐다: {doc.status!r} "
                                    f"(허용: {', '.join(sorted(zk.ALLOWED_STATUS))})"))
        if not doc.tags:
            warnings.append((doc.rel, "tags 가 비어 있다 — 지도 후보 탐지에서 빠진다"))
        if doc.h1 is None:
            warnings.append((doc.rel, "본문에 H1 제목이 없다"))
        elif zk.normalize(doc.h1) != zk.normalize(doc.title):
            warnings.append((doc.rel, f"H1 과 frontmatter title 이 다르다: «{doc.h1}» vs «{doc.title}»"))

    # 3. 고립 메모 — 아무도 링크하지 않는 메모
    for note in sorted(notes, key=lambda d: d.slug):
        if not inbound[note.path]:
            warnings.append((note.rel, "인바운드 링크가 없다 — 관련 메모나 지도에 연결하거나 합성 기록에 이유를 남겨라"))
        outbound = [t for _, _, t in note.links() if note.resolve(t) in note_paths]
        if not outbound:
            warnings.append((note.rel, "다른 메모로 나가는 링크가 없다"))

    # 4. 제목 중복
    title_counts = Counter(zk.normalize(n.title) for n in notes)
    for title, count in title_counts.items():
        if count > 1:
            same = sorted(n.rel for n in notes if zk.normalize(n.title) == title)
            errors.append(("notes/", f"제목이 같은 메모 {count}건: {', '.join(same)}"))

    # 5. 지도 후보 — 같은 태그 메모가 3개 이상인데 지도에 3개 미만만 실린 경우
    in_maps = set()
    for m in maps:
        for _, _, target in m.links():
            resolved = m.resolve(target)
            if resolved in note_paths:
                in_maps.add(resolved)
    tag_notes = defaultdict(list)
    for note in notes:
        for tag in note.tags:
            tag_notes[tag].append(note)
    candidates = []
    for tag, tagged in sorted(tag_notes.items()):
        if len(tagged) < 3:
            continue
        missing = [n for n in tagged if n.path not in in_maps]
        if len(missing) >= 3:
            candidates.append((tag, len(tagged), [n.slug for n in missing]))

    # 6. 보고
    print(f"제텔카스텐 검사 — {root}")
    print(f"문서 {len(docs)} (메모 {len(notes)} · 지도 {len(maps)}) · 링크 {link_total}")

    if errors:
        print(f"\n## 오류 {len(errors)}건 — 반드시 고칠 것")
        for where, msg in errors:
            print(f"  ✗ {where}  {msg}")
    else:
        print("\n## 오류 없음")

    if warnings and not args.quiet:
        print(f"\n## 경고 {len(warnings)}건 — 판단해서 처리")
        for where, msg in warnings:
            print(f"  ! {where}  {msg}")

    if candidates and not args.quiet:
        print(f"\n## 지도 후보 {len(candidates)}건 — 태그당 메모 3개 이상이 어느 지도에도 없다")
        for tag, total, missing in candidates:
            shown = ", ".join(missing[:6]) + (" …" if len(missing) > 6 else "")
            print(f"  + #{tag} (총 {total}건, 미수록 {len(missing)}): {shown}")

    if errors:
        print(f"\n실패 — 오류 {len(errors)}건")
        return 1
    print(f"\n통과 — 오류 0건, 경고 {len(warnings)}건")
    return 0


if __name__ == "__main__":
    sys.exit(main())
