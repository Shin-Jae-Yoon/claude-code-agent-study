# 점진적 공개와 토큰 비용

이 지도는 "지식을 늘리면 컨텍스트를 먹는다"는 모순을 푸는 메커니즘과, 그 메커니즘이 통하지 않는 지점을 함께 묶는다. 3장의 중심 축이다.

## 원리

- [점진적 공개는 쓰지 않는 지식의 비용을 0으로 만든다](../notes/progressive-disclosure-makes-unused-knowledge-free.md) — 나머지 메모들이 이 주장을 지지하거나 한계를 짚는다.
- [탐색은 범위를 좁혀 가며 앞 단계 결과를 다음 입력으로 넘긴다](../notes/narrow-the-scope-instead-of-asking-everything.md) — 같은 원리가 파일 로딩이 아니라 대화 진행에 적용된 형태다(2장).

## 원리가 통하지 않는 층

"비용 0"은 3단계에만 해당한다. 아래 두 메모가 각각 2단계와 1단계에서 발생하는 실제 비용을 다룬다.

- [SKILL.md 본문은 세션 내내 남는 상주 비용이다](../notes/skill-body-is-recurring-context-cost.md) — 2단계
- [스킬 목록 예산을 넘으면 description부터 잘려나간다](../notes/skill-listing-budget-truncates-descriptions.md) — 1단계
- [CLAUDE.md는 항상 로드되고 스킬은 조건부로 로드된다](../notes/claude-md-is-always-loaded-skills-are-conditional.md) — 이 원리를 아예 누리지 못하는 반대편
- [자동 압축은 스킬을 5,000 / 25,000토큰까지만 되살린다](../notes/compaction-reattachment-budget-limits-skill-persistence.md) — 상주가 무조건 유지되지도 않는다는 반대 방향의 제약

## 비용을 줄이는 실천

원리를 실제로 적용하는 네 가지 방법. 앞의 둘은 "무엇을 어디에 둘 것인가", 뒤의 둘은 "무엇을 빼거나 내릴 것인가"에 해당한다.

- [지원 파일 참조는 한 단계 깊이까지만 유지한다](../notes/support-file-references-must-stay-one-level-deep.md)
- [입출력 예시는 스킬 토큰의 5분의 1에서 절반을 차지한다](../notes/examples-consume-a-fifth-to-half-of-skill-tokens.md)
- [스킬에는 클로드가 모르는 것만 담는다](../notes/skill-should-contain-only-what-claude-cannot-know.md)
- [스크립트는 출력만큼만 토큰을 쓴다](../notes/scripts-cost-only-their-output.md) — 그 이점을 유지하려면 [스크립트는 실행인지 참조인지 명시해야 한다](../notes/script-invocation-must-be-explicit.md)

## 얼마나 쓰고 있는지 재기

- [스킬 토큰 비용은 컨텍스트의 15% 이내를 목표로 한다](../notes/skill-token-budget-target-15-percent.md)
- [분량의 실제 기준은 줄 수가 아니라 토큰이다](../notes/token-count-not-line-count-is-the-real-measure.md) — 규약을 줄 수로 쓰는 관행에 대한 반론

## 사례와 공백

- [ECC의 286개 스킬은 점진적 공개의 실증이다](../notes/ecc-286-skills-as-progressive-disclosure-proof.md) — 원리가 통하는 최대 규모 사례
- [우리 팀 스킬에는 아직 스크립트가 없다](../notes/team-has-no-skill-scripts-yet.md) — 원리에 동의하면서 실천이 비어 있는 지점

## 관련 지도

- [열려 있는 긴장](./open-tensions.md) — 분량 기준과 예시 비중을 두고 갈린 판단
- [스킬 품질과 신뢰성](./skill-quality-and-reliability.md) — 비용 축 밖의 나머지 측정 축
