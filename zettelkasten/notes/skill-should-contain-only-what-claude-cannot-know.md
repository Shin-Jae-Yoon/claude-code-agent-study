---
title: "스킬에는 클로드가 모르는 것만 담는다"
type: "practice"
status: "growing"
tags: ["skill-authoring", "token-cost"]
---

# 스킬에는 클로드가 모르는 것만 담는다

기본 가정은 "클로드는 이미 매우 똑똑하다"이다. 범용 지식(언어 문법, 널리 쓰이는 라이브러리 사용법, 개념 설명)은 본문에서 통째로 지우고, 클로드가 알 수 없는 것 — 프로젝트 고유 컨벤션, 팀 특화 패턴, 비공개 내부 API 명세 — 만 남긴다. 같은 기능을 훨씬 적은 토큰으로 구현할 수 있다.

## 근거와 출처

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 최적화 5전략의 두 번째. 파이썬 리스트 컴프리헨션이나 리액트 `useState` 같은 범용 지식을 빼면 동일 기능 대비 약 50~70% 적은 토큰으로 구현 가능하다고 정리했다.
- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md): 토큰 최적화 5원칙의 두 번째로 같은 수치(50~70% 절감)를 들었다.
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): "간결함이 최우선. 컨텍스트 윈도우는 공공재다. (…) PDF가 뭔지 설명하는 문단은 통째로 지워도 된다."

## 연결

- [SKILL.md 본문은 세션 내내 남는 상주 비용이다](./skill-body-is-recurring-context-cost.md) — 이 실천이 줄이는 대상이 그 비용이다.
- [환경변수 값은 스킬이 아니라 설정에 둔다](./env-values-belong-in-settings-not-in-skills.md) — "스킬에 담지 말아야 할 것"의 다른 사례다.
- [자유도는 작업에 맞춰 조절한다](./degrees-of-freedom-should-match-the-task.md) — 무엇을 뺄지는 얼마나 촘촘히 지시할지와 함께 결정된다.
- [CLAUDE.md는 항상 로드되고 스킬은 조건부로 로드된다](./claude-md-is-always-loaded-skills-are-conditional.md) — 이 메모가 **무엇을** 담을지의 기준이라면 그쪽은 **어디에** 담을지의 기준이다. 2장 재윤 정리본의 "문서가 길어지면 참조용 절차를 Skill로 분리한다"가 그 판단선이다.
