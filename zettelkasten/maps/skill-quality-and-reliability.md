# 스킬 품질과 신뢰성

이 지도는 "스킬이 잘 되고 있는가"를 묻는 방법과, 출력을 믿을 수 있게 만드는 설계를 묶는다. 앞쪽은 측정, 뒤쪽은 환각 방지다.

## 측정

- [스킬 측정에는 네 개의 축이 있다](../notes/skill-measurement-has-four-axes.md) — 이 지도의 뼈대. 로드·발동·품질·비용
- [발동을 봤다고 스킬이 잘 동작하는 것은 아니다](../notes/skill-activation-is-not-evidence-of-quality.md) — 한 축의 통과가 다른 축을 보장하지 않는다
- [스킬은 평가부터 만든다](../notes/eval-first-skill-development.md) — 측정을 개발 초기로 당기는 실천
- [좋은 프롬프트보다 좋은 피드백 루프가 중요하다](../notes/feedback-loop-beats-prompt-quality.md) — 같은 사고가 2장에서 코드 작업 쪽에 먼저 적용돼 있었다

## 출력을 믿게 만드는 설계

- [환각 방지에 지침으로 충분한가 검증 장치까지 필요한가](../notes/instructions-lower-probability-verification-is-deterministic.md) — 이 절의 중심 질문
- [출처를 요구하면 출처를 지어낸다](../notes/cite-sources-invites-fabricated-sources.md) — "지침만으로 부족하다" 쪽의 핵심 반례
- [Opus 5에서는 출력 규범은 남기고 절차 지시는 뺀다](../notes/opus5-keep-output-norms-drop-procedure-instructions.md) — 어떤 지침을 남기고 뺄지의 최신 기준
- [Hooks는 LLM 판단 밖에서 결정론적으로 실행된다](../notes/hooks-run-deterministically-outside-llm-judgment.md) — "검증은 결정론적이다" 쪽의 구현 수단. 2장에 이미 있었다

## 얼마나 촘촘히 쓸 것인가

- [자유도는 작업에 맞춰 조절한다](../notes/degrees-of-freedom-should-match-the-task.md) — 지침·템플릿·스크립트 중 무엇으로 쓸지를 작업 성격이 정한다

## 관련 지도

- [점진적 공개와 토큰 비용](./progressive-disclosure-and-token-cost.md) — 비용 축의 상세
- [스킬 호출과 발견](./skill-invocation-and-discovery.md) — 로드·발동 축의 실패 모드
- [열려 있는 긴장](./open-tensions.md)
