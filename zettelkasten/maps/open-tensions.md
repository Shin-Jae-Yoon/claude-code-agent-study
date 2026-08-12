# 열려 있는 긴장

이 지도는 **팀원 간 판단이 갈렸거나 근거가 충돌해 아직 결론이 없는 것**만 모은다. 주차마다 여기에 쌓고, 해소되면 해당 메모의 `status`를 올리고 이 지도에서 내린다. 나머지 지도가 "무엇을 알게 됐나"라면 이 지도는 "무엇이 아직 안 정해졌나"다.

## 규약에 숫자를 넣을 것인가

같은 구도가 두 필드에서 반복된다 — 한 사람은 실무 기준으로 채택하고, 한 사람은 안전선으로 유지하고, 한 사람은 근거 없는 수치로 분류한다.

- [SKILL.md 분량 기준은 세 사람이 다르게 본다](../notes/skill-md-length-standard-is-contested.md) — 본문 길이
- [description 길이 기준을 두고 해석이 갈린다](../notes/description-length-limit-is-contested.md) — 설명 길이
- [분량의 실제 기준은 줄 수가 아니라 토큰이다](../notes/token-count-not-line-count-is-the-real-measure.md) — 숫자 자체를 거부하는 쪽의 논거
- [한 번에 검증 가능한 최소 변경이 작업 단위다](../notes/atomic-sub-requirement-not-line-count.md) — **2장에서 이미 같은 형태로 나왔다.** 대상만 다를 뿐(작업 크기 vs 문서 길이) 둘 다 줄 수를 기준에서 밀어낸다. 정량 기준을 두고 우리 팀이 반복해서 같은 곳에서 막힌다는 신호

## 어디까지 격리할 것인가

- [단계 단위 포크가 가능한지 아직 모른다](../notes/context-fork-scope-is-per-skill-not-per-step.md) — 같은 스킬을 두고 도입 후보와 부적합 판정이 맞섰다

## 지침으로 충분한가

- [환각 방지에 지침으로 충분한가 검증 장치까지 필요한가](../notes/instructions-lower-probability-verification-is-deterministic.md) — 지침 계열에서 멈출지 구조적 검증까지 갈지

## 근거가 충돌하는 사실

정리본끼리 서술이 달라 직접 재현해봐야 확정되는 것들.

- [YAML이 깨지면 본문만 빈 메타데이터로 로드된다](../notes/yaml-error-loads-body-with-empty-metadata.md) — "스킬 전체가 로드되지 않는다"(교재)와 "본문은 로드되고 메타데이터만 빈다"(공식 디버그 문서)가 맞선다
- [스킬 목록 예산을 넘으면 description부터 잘려나간다](../notes/skill-listing-budget-truncates-descriptions.md)와 [ECC의 286개 스킬은 점진적 공개의 실증이다](../notes/ecc-286-skills-as-progressive-disclosure-proof.md) — 두 메모가 정면으로 부딪히는데 어느 정리본도 답을 갖고 있지 않다

## 체계 간 규칙이 어긋나는 것

- [설정 우선순위와 스킬 우선순위는 사용자·프로젝트 구간에서 뒤집힌다](../notes/settings-hierarchy-inverts-skill-priority.md) — 같은 저장소에서 한쪽은 팀 값을 강제하고 한쪽은 못 한다. 왜 다른지 공식 설명을 못 찾았다
- [환경변수 값은 스킬이 아니라 설정에 둔다](../notes/env-values-belong-in-settings-not-in-skills.md) — 셸 환경변수와 `settings.json`의 `env`가 충돌할 때의 우선순위. 2장 재윤 정리본이 남긴 질문이 아직 열려 있다

## 조용히 실패하는 것들

경고 없이 넘어가므로 규약이나 도구로 잡지 않으면 발견되지 않는다.

- [제한처럼 읽히지만 막지 않는 장치가 반복해서 나타난다](../notes/controls-that-read-as-limits-but-do-not-block.md) — 두 챕터에 걸쳐 최소 다섯 번 반복된 패턴. 항목마다 잡는 수단이 달라 통합 대응책이 없다
- [미정의 설정 key는 거부되지 않고 조용히 무시된다](../notes/undefined-settings-keys-are-silently-ignored.md) — `$schema`로 편집 단계에서 잡는 방법은 확인됐으나 우리 저장소에는 적용되지 않았다
- [Read 차단은 Bash 우회를 막지 못한다](../notes/read-deny-does-not-block-bash-bypass.md) — 우회 명령이 무한해서 deny 나열로는 닫히지 않는다

## 비용 축과 품질 축이 다른 답을 주는 것

- [입출력 예시는 스킬 토큰의 5분의 1에서 절반을 차지한다](../notes/examples-consume-a-fifth-to-half-of-skill-tokens.md) — 비용으로는 줄이라 하고 품질로는 조건부로 넣으라 한다
- [자유도는 작업에 맞춰 조절한다](../notes/degrees-of-freedom-should-match-the-task.md) — 그 조건을 정하는 기준

## 팀 규약으로 정해야 하는 것

메모 자체는 결론이 나 있으나 우리 저장소에 적용할지가 미정인 것들.

- [스킬은 스스로에게 넓은 도구 권한을 줄 수 있다](../notes/skills-can-grant-themselves-broad-tool-access.md) — 승격 절차에 권한 검토를 넣을 것인가
- [개인 스킬이 프로젝트 스킬을 조용히 덮어쓴다](../notes/personal-skills-silently-override-project-skills.md) — 개인 스킬 네이밍 규약이 필요한가
- [우리 팀 스킬에는 아직 스크립트가 없다](../notes/team-has-no-skill-scripts-yet.md) — 첫 스크립트를 어디에 도입할 것인가
- [스킬은 평가부터 만든다](../notes/eval-first-skill-development.md) — 기존 스킬에 소급할 것인가 신규부터 적용할 것인가
