---
title: "CLAUDE.md는 항상 로드되고 스킬은 조건부로 로드된다"
type: "claim"
status: "growing"
tags: ["progressive-disclosure", "token-cost", "team-convention", "cross-chapter"]
---

# CLAUDE.md는 항상 로드되고 스킬은 조건부로 로드된다

같은 지침을 `CLAUDE.md`에 두느냐 스킬에 두느냐는 내용의 문제가 아니라 **로딩 시점의 문제**다. `CLAUDE.md`는 매 세션 컨텍스트에 자동으로 들어가므로 항상 지불하는 고정비이고, 스킬은 트리거될 때만 들어간다. 항상 적용돼야 하는 짧은 규칙은 `CLAUDE.md`, 특정 상황에서만 필요한 긴 절차는 스킬이 맞다.

## 근거와 출처

- [2장 홍섭 정리](../../chapters/ch2/hongseob/정리본.md): "`CLAUDE.md`는 매 세션 컨텍스트에 자동 로드됨 → '서버 실행해줘'만 해도 Claude가 이 규칙을 보고 빌드 명령을 붙여 실행한다." 같은 효과를 스킬이나 슬래시 커맨드(`/run-server`)로 만들어도 된다고 덧붙였다. 3계층 구분도 함께 정리했다 — `./CLAUDE.md`(팀 공유·커밋) / `./CLAUDE.local.md`(나만·gitignore) / `~/.claude/CLAUDE.md`(모든 프로젝트).
- [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md): 빌드·테스트·린트 명령과 코드 스타일, 커밋 규칙을 `CLAUDE.md`에 기록하되 "**문서가 길어지면 참조용 절차를 Skill로 분리한다**"는 기준을 세웠다.

두 지침 위치를 로딩 비용의 관점에서 대비한 것은 합성자의 해석이다. 3장에서 확인된 스킬의 로딩 모델과 맞물린다.

## 연결

- [점진적 공개는 쓰지 않는 지식의 비용을 0으로 만든다](./progressive-disclosure-makes-unused-knowledge-free.md) — 스킬이 조건부인 이유의 메커니즘이다. `CLAUDE.md`에는 이 이점이 없다.
- [SKILL.md 본문은 세션 내내 남는 상주 비용이다](./skill-body-is-recurring-context-cost.md) — 스킬도 한 번 호출되면 `CLAUDE.md`와 같은 처지가 된다는 점에서, 둘의 차이는 "항상"과 "한 번 불린 뒤부터"다.
- [스킬에는 클로드가 모르는 것만 담는다](./skill-should-contain-only-what-claude-cannot-know.md) — 무엇을 담을지의 기준이라면 이 메모는 어디에 담을지의 기준이다.
- [설정 우선순위와 스킬 우선순위는 사용자·프로젝트 구간에서 뒤집힌다](./settings-hierarchy-inverts-skill-priority.md) — 팀 규약을 어디에 둘지 정할 때 함께 봐야 한다.
- [`agent: Explore`와 `Plan`은 CLAUDE.md를 건너뛴다](./background-fork-edits-escape-rewind.md) — 포크된 서브에이전트에서는 이 "항상"이 깨진다.

## 열린 질문

- 우리 저장소의 루트 `CLAUDE.md`는 문서 언어·작업 경계·스킬 승격 규칙을 담고 있다. 이 중 매 세션 상주할 값을 하는 것과 스킬로 내려도 되는 것을 구분해본 적이 없다.
