---
title: "단계 단위 포크가 가능한지 아직 모른다"
type: "tension"
status: "growing"
tags: ["context-fork", "team-convention", "open-question"]
---

# 단계 단위 포크가 가능한지 아직 모른다

같은 스킬(`pre-chapter-prep`)을 두고 두 사람이 반대 판단을 내렸다. 한쪽은 그 스킬의 특정 단계가 포크의 첫 적용 지점이라고 봤고, 다른 쪽은 그 스킬 전체가 포크에 부적합하다고 판정했다. `context`는 스킬 단위 frontmatter 필드이므로, "일부 단계만 포크"가 성립하는지가 결론을 가른다.

## 근거와 출처

- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md) — **도입 후보로 지목.** "`pre-chapter-prep`이 이미 3단계 HTML 생성을 '서브에이전트 위임 가능'이라 명시 → 여기에 `context: fork` + `agent: general-purpose`를 붙이는 게 첫 적용 지점."
- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md) — **부적합으로 판정.** "이 스킬 전체를 `context: fork`로 만들면 1→2단계의 역질문 게이트(사람과의 대화)가 불가능해진다. 부모 대화 맥락이 필수인 스킬이기 때문이다." 대신 `mid-zettelkasten-synthesis`를 도입 대상으로 확정했다. 다만 같은 정리본은 현재 이 스킬이 **본문 자연어로** 위임을 권하는 형태(프론트매터 필드가 아니라)라는 점도 실측했다.

두 판단의 대상 층위가 다르다는 것이 이 메모의 관찰이다(합성자 해석). 홍섭은 3단계만, 재윤은 스킬 전체를 말하고 있다.

## 연결

- [context: fork는 결론만 필요한 작업에 적합하다](./context-fork-suits-conclusion-only-tasks.md) — 두 판단이 공유하는 기준이다. 기준이 아니라 적용 범위에서 갈렸다.
- [태스크 없는 스킬을 포크하면 빈손으로 돌아온다](./forked-skill-without-a-task-returns-nothing.md) — 지침과 태스크가 한 스킬에 섞여 있을 때 무엇이 넘어가는지의 문제로 이어진다.
- [백그라운드 포크의 편집은 되돌릴 수 없다](./background-fork-edits-escape-rewind.md) — HTML 생성처럼 파일을 쓰는 단계라면 추가로 걸리는 조건이다.

## 열린 질문

- `context: fork`가 스킬 단위 필드라면, 본문 자연어로 "이 단계는 서브에이전트에 위임하라"고 쓰는 현재 방식이 사실상 유일한 부분 격리 수단인가?
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md)의 기준을 대면 판단 재료가 둘 더 붙는다 — "다른 스킬과 스택해서 쓰는 스킬은 포크에서 확장이 끊긴다", 그리고 백그라운드 포크의 좁은 도구셋. 우리 스터디 스킬은 서로를 이어 쓰는 구조이므로 이 조건을 먼저 확인해야 한다.
