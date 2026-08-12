# 스킬 호출과 발견

이 지도는 "누가 이 스킬을 부르는가"와 "왜 안 불리는가"를 묶는다. 커맨드와 스킬이 통합된 이후 남은 구분선이 전부 여기에 있다.

## 호출 주체를 정하는 것

- [커맨드와 스킬의 남은 차이는 호출 제어뿐이다](../notes/commands-and-skills-differ-only-in-invocation-control.md) — 이 지도의 출발점
- [user-invocable은 자율 실행을 막지 못한다](../notes/user-invocable-does-not-block-autonomous-execution.md) — 호출 제어 필드 중 이름과 동작이 어긋나는 쪽

## 자동 발동을 결정하는 것

- [발동을 결정하는 것은 name이 아니라 description이다](../notes/description-decides-activation.md)
- [스킬 이름은 규칙이 아니라 라벨이다](../notes/skill-name-is-a-label-not-a-rule.md) — `name`의 비중이 낮은 이유

## 발동이 실패하는 세 가지 경로

증상은 비슷하고 원인은 전부 다르다. 순서대로 의심하는 것이 진단 비용을 줄인다.

1. [YAML이 깨지면 본문만 빈 메타데이터로 로드된다](../notes/yaml-error-loads-body-with-empty-metadata.md) — 파일이 잘못된 경우
2. [스킬 목록 예산을 넘으면 description부터 잘려나간다](../notes/skill-listing-budget-truncates-descriptions.md) — 파일은 멀쩡하나 목록에서 잘린 경우
3. [description 길이 기준을 두고 해석이 갈린다](../notes/description-length-limit-is-contested.md) — 무엇을 얼마나 쓸지 자체가 미정인 경우

## 대안 설계

- [OMC는 트리거를 description에서 분리해 별도 필드로 둔다](../notes/omc-triggers-field-separates-activation-from-description.md) — 같은 문제를 다른 필드 구조로 푼 사례

## 관련 지도

- [스킬 권한과 배포](./skill-permissions-and-distribution.md) — 이름 충돌이 어느 스킬을 실행할지 바꾸는 문제
- [스킬 품질과 신뢰성](./skill-quality-and-reliability.md) — 발동률을 실제로 재는 방법
