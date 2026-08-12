#!/usr/bin/env python3
"""기존 제텔카스텐의 압축 인덱스를 출력한다 — 새 메모를 만들기 전에 실행한다.

52개 메모를 전부 읽는 대신 한 줄 요약 목록만 컨텍스트에 올리기 위한 스크립트다.
--query 를 주면 그 주제와 겹치는 기존 메모를 점수순으로 뽑아 중복 생성을 막는다.

사용:
  python3 index_notes.py
  python3 index_notes.py --query "서브에이전트 컨텍스트 격리"
  python3 index_notes.py --tag skill-authoring --verbose
"""

import argparse
import sys
from collections import Counter, defaultdict

import zk


def score(doc, terms):
    """질의어와 메모의 겹침 점수. 제목 3배, 태그 2배, 본문 1배."""
    title = zk.normalize(doc.title + " " + doc.slug.replace("-", " "))
    tags = zk.normalize(" ".join(doc.tags))
    body = zk.normalize(doc.text)
    total = 0
    for term in terms:
        total += 3 * title.count(term)
        total += 2 * tags.count(term)
        total += 1 * body.count(term)
    return total


def line_for(doc, verbose=False):
    meta = f"{doc.note_type or '?'}/{doc.status or '?'}"
    tags = " ".join("#" + t for t in doc.tags)
    out = f"- {doc.slug} [{meta}] {doc.title}"
    if tags:
        out += f"  {tags}"
    if verbose:
        summary = doc.summary_line()
        if summary:
            out += f"\n    {summary}"
    return out


def main():
    parser = argparse.ArgumentParser(description="제텔카스텐 인덱스 출력")
    parser.add_argument("--root", help="제텔카스텐 루트 (기본: $CLAUDE_PROJECT_DIR/zettelkasten)")
    parser.add_argument("--query", help="이 주제와 겹치는 기존 메모를 점수순으로 출력")
    parser.add_argument("--tag", action="append", default=[], help="이 태그를 가진 메모만 출력 (반복 가능)")
    parser.add_argument("--top", type=int, default=15, help="--query 결과 개수 (기본 15)")
    parser.add_argument("--verbose", action="store_true", help="메모마다 첫 문장도 출력")
    args = parser.parse_args()

    root = zk.find_root(args.root)
    docs = zk.load(root)
    notes = zk.notes_of(docs)
    maps = zk.maps_of(docs)
    syntheses = [d for d in docs if d.kind == "syntheses"]

    if not notes:
        sys.exit(f"[오류] {root}/notes 에 메모가 없다.")

    print(f"제텔카스텐 인덱스 — {root}")
    print(f"메모 {len(notes)} · 지도 {len(maps)} · 합성 기록 {len(syntheses)}")

    # --query: 중복 후보만 좁혀서 출력한다.
    if args.query:
        terms = [zk.normalize(t) for t in args.query.split() if len(t) > 1]
        ranked = sorted(
            ((score(n, terms), n) for n in notes),
            key=lambda pair: (-pair[0], pair[1].slug),
        )
        hits = [(s, n) for s, n in ranked if s > 0][: args.top]
        print(f"\n## 질의 «{args.query}» 와 겹치는 기존 메모 {len(hits)}건")
        if not hits:
            print("(없음 — 새 메모를 만들어도 중복 위험이 낮다)")
        for s, note in hits:
            print(f"{line_for(note, args.verbose)}  ⟨{s}점⟩")
        return

    selected = notes
    if args.tag:
        wanted = {zk.normalize(t) for t in args.tag}
        selected = [n for n in notes if wanted & {zk.normalize(t) for t in n.tags}]
        print(f"태그 필터 {', '.join(args.tag)} → {len(selected)}건")

    print(f"\n## 메모 ({len(selected)})")
    for note in sorted(selected, key=lambda d: d.slug):
        print(line_for(note, args.verbose))

    tag_counts = Counter(t for n in notes for t in n.tags)
    if tag_counts:
        print(f"\n## 태그 분포 ({len(tag_counts)}종)")
        print("  ".join(f"{t}:{c}" for t, c in tag_counts.most_common()))

    if maps:
        # 지도가 실제로 링크하는 메모 수를 센다. 지도 본문의 상대 링크가 근거다.
        note_paths = {n.path for n in notes}
        covered = defaultdict(set)
        for m in maps:
            for _, _, target in m.links():
                resolved = m.resolve(target)
                if resolved in note_paths:
                    covered[m.slug].add(resolved)
        print(f"\n## 지도 ({len(maps)})")
        for m in sorted(maps, key=lambda d: d.slug):
            print(f"- {m.slug} — 수록 메모 {len(covered[m.slug])}  «{m.title}»")

        linked_anywhere = {p for s in covered.values() for p in s}
        uncovered = sorted(n.slug for n in notes if n.path not in linked_anywhere)
        if uncovered:
            print(f"\n## 어느 지도에도 없는 메모 ({len(uncovered)})")
            for slug in uncovered:
                print(f"- {slug}")


if __name__ == "__main__":
    main()
