---
title: "점진적 공개는 쓰지 않는 지식의 비용을 0으로 만든다"
type: "claim"
status: "growing"
tags: ["progressive-disclosure", "token-cost", "context-management"]
---

# 점진적 공개는 쓰지 않는 지식의 비용을 0으로 만든다

스킬 콘텐츠는 메타데이터 → 본문 → 번들 파일 순으로 단계적으로 로드된다. 접근되지 않은 파일은 토큰을 전혀 소비하지 않으므로, 방대한 API 문서나 데이터셋을 번들해도 설치 비용이 발생하지 않는다. 지식을 늘리면 컨텍스트를 먹는다는 모순을 푸는 것이 이 메커니즘이다.

## 근거와 출처

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 중심 메시지로 세웠다. "필요하지 않은 콘텐츠가 컨텍스트 윈도우를 선점하지 못하게 단계적으로 로드하기 때문에, 스킬을 아무리 많이 갖춰도 쓰지 않는 지식의 비용은 0에 수렴한다."
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): L1 메타데이터 / L2 본문 / L3 번들 파일 3단계로 정리하고 "읽히지 않은 파일은 토큰을 0 쓴다"를 핵심으로 짚었다.
- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md): 같은 원리를 지원 파일 역할로 서술했다. "`references/`는 본문에서 빼고 필요할 때만 로드 → 평소 토큰 절약."

## 연결

- [SKILL.md 본문은 세션 내내 남는 상주 비용이다](./skill-body-is-recurring-context-cost.md) — 이 주장의 한계다. 3단계는 공짜지만 2단계는 그렇지 않다.
- [스크립트는 출력만큼만 토큰을 쓴다](./scripts-cost-only-their-output.md) — 점진적 공개를 한 단계 더 밀어붙인 형태다.
- [지원 파일 참조는 한 단계 깊이까지만 유지한다](./support-file-references-must-stay-one-level-deep.md) — 3단계가 실제로 작동하기 위한 조건이다.
- [ECC의 286개 스킬은 점진적 공개의 실증이다](./ecc-286-skills-as-progressive-disclosure-proof.md) — 이 주장을 외부 규모 사례로 뒷받침한다.
- [CLAUDE.md는 항상 로드되고 스킬은 조건부로 로드된다](./claude-md-is-always-loaded-skills-are-conditional.md) — 이 원리를 누리지 못하는 반대편이다. 같은 지침도 어디에 두느냐로 조건부와 고정비가 갈린다.
- [탐색은 범위를 좁혀 가며 앞 단계 결과를 다음 입력으로 넘긴다](./narrow-the-scope-instead-of-asking-everything.md) — **같은 원리가 파일 로딩이 아니라 대화 진행에 적용된 형태다**(합성자 해석). 2장은 이것을 워크플로 규칙으로, 3장은 스킬 로딩 메커니즘으로 다뤘다.

## 열린 질문

- "비용 0"은 3단계에만 해당한다. 스킬 수가 늘면 1단계 메타데이터는 선형으로 늘어나는데, 그 한계는 어디인가? → [스킬 목록 예산을 넘으면 description부터 잘려나간다](./skill-listing-budget-truncates-descriptions.md)
