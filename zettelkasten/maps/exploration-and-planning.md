# 탐색과 계획

이 지도는 **코드를 쓰기 전 단계**를 묶는다. 무엇을 만들지 정하고, 현재 시스템을 파악하고, 작업을 어떤 단위로 쪼갤지 결정하는 구간이다.

## 탐색을 어떻게 하는가

- [탐색은 범위를 좁혀 가며 앞 단계 결과를 다음 입력으로 넘긴다](../notes/narrow-the-scope-instead-of-asking-everything.md) — 이 지도의 기본 원리
- [세 도구는 서로 다른 병목을 푼다](../notes/tools-solve-different-bottlenecks-not-the-same-one.md) — 탐색·계획을 외부 도구로 보조하는 선택지

## 실행과 분리하기

같은 목적(탐색 중 실수로 바뀌는 것을 막는다)에 대한 두 가지 강도의 답이다.

- [플랜 모드는 탐색과 실행을 분리한다](../notes/plan-mode-separates-exploration-from-execution.md) — 같은 대화 안에서 쓰기 권한만 잠근다
- [context: fork는 결론만 필요한 작업에 적합하다](../notes/context-fork-suits-conclusion-only-tasks.md) — 대화 자체를 분리한다

## 작업 단위를 어떻게 정하는가

- [한 번에 검증 가능한 최소 변경이 작업 단위다](../notes/atomic-sub-requirement-not-line-count.md) — 크기가 아니라 검증 가능성이 단위를 정한다
- [좋은 프롬프트보다 좋은 피드백 루프가 중요하다](../notes/feedback-loop-beats-prompt-quality.md) — 그 검증이 실제로 돌아야 하는 이유

## 무엇으로 확장할 것인가

- [스킬은 지식을 확장하고 서브에이전트는 능력을 확장한다](../notes/skill-extends-knowledge-subagent-extends-capability.md) — 확장 도구를 "무엇을 확장하는가"로 나눈 축

## 관련 지도

- [설정 계층](./configuration-layers.md) — 이 단계의 규칙을 어디에 적어둘 것인가
- [context: fork로 컨텍스트 격리하기](./context-isolation-with-fork.md) — 격리 쪽의 상세
- [점진적 공개와 토큰 비용](./progressive-disclosure-and-token-cost.md) — "필요할 때까지 안 가져온다"가 파일 로딩에 적용된 형태
