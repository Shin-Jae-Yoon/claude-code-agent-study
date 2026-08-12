# ch3 합성 기록 — 에이전트 스킬

> 합성일: 2026-08-12 · **제텔카스텐 첫 합성**. 기존 `notes/`·`maps/`가 비어 있어 비교 대상 없이 새로 만들었다.

## 입력

| 작성자 | 파일 | 줄 수 |
| --- | --- | --- |
| 홍섭 | [chapters/ch3/hongseob/정리본.md](../../chapters/ch3/hongseob/정리본.md) | 93 |
| 재윤 | [chapters/ch3/jaeyoon/정리본.md](../../chapters/ch3/jaeyoon/정리본.md) | 1,052 |
| 준호 | [chapters/ch3/junho/Chapter 03. 에이전트 스킬.md](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md) | 697 |

참고: 준호 파일만 `정리본.md` 규약을 따르지 않아 `chapters/chN/*/정리본.md` 글롭으로는 수집되지 않는다. 이번에는 수동으로 포함했다.

## 신호

### 반복 — 둘 이상의 독립 문서에서 등장

세 문서 모두에서 나온 것:

- 점진적 공개 3단계와 "읽히지 않은 파일은 토큰 0" → [progressive-disclosure-makes-unused-knowledge-free](../notes/progressive-disclosure-makes-unused-knowledge-free.md)
- 커맨드·스킬 통합, 차이는 호출 제어 필드 → [commands-and-skills-differ-only-in-invocation-control](../notes/commands-and-skills-differ-only-in-invocation-control.md)
- 컴팩션 재부착 예산 5,000 / 25,000토큰 → [compaction-reattachment-budget-limits-skill-persistence](../notes/compaction-reattachment-budget-limits-skill-persistence.md)
- 스크립트는 출력만 토큰을 쓴다 → [scripts-cost-only-their-output](../notes/scripts-cost-only-their-output.md)
- 지원 파일 참조는 깊이 1단계 → [support-file-references-must-stay-one-level-deep](../notes/support-file-references-must-stay-one-level-deep.md)
- 범용 지식은 빼고 클로드가 모르는 것만 → [skill-should-contain-only-what-claude-cannot-know](../notes/skill-should-contain-only-what-claude-cannot-know.md)
- description이 발동을 결정한다 → [description-decides-activation](../notes/description-decides-activation.md)
- `context: fork`는 결론만 필요한 작업에 → [context-fork-suits-conclusion-only-tasks](../notes/context-fork-suits-conclusion-only-tasks.md)

두 문서에서 나온 것:

- `allowed-tools`는 사전 승인 (재윤 정정 · 준호 원 서술) → [allowed-tools-grants-rather-than-restricts](../notes/allowed-tools-grants-rather-than-restricts.md)
- 우선순위 `enterprise > personal > project` (재윤 · 준호) → [personal-skills-silently-override-project-skills](../notes/personal-skills-silently-override-project-skills.md)
- `name`은 라벨, 커맨드명은 디렉터리명 (홍섭 · 준호) → [skill-name-is-a-label-not-a-rule](../notes/skill-name-is-a-label-not-a-rule.md)
- SKILL.md 본문은 세션 내내 남는다 (재윤 · 준호) → [skill-body-is-recurring-context-cost](../notes/skill-body-is-recurring-context-cost.md)
- 태스크 없는 포크는 빈손 (재윤 · 준호) → [forked-skill-without-a-task-returns-nothing](../notes/forked-skill-without-a-task-returns-nothing.md)
- 리스팅 예산 조정 수단 (재윤 · 준호) → [skill-listing-budget-truncates-descriptions](../notes/skill-listing-budget-truncates-descriptions.md)
- 예시 비중 20~50% (재윤 · 홍섭) → [examples-consume-a-fifth-to-half-of-skill-tokens](../notes/examples-consume-a-fifth-to-half-of-skill-tokens.md)
- `scripts/`·`templates/` 미적용 실측 (재윤 · 홍섭) → [team-has-no-skill-scripts-yet](../notes/team-has-no-skill-scripts-yet.md)
- 15% 목표 — 재윤은 추정식, 홍섭은 관측 수단 → [skill-token-budget-target-15-percent](../notes/skill-token-budget-target-15-percent.md)

> 반복은 중요도의 신호로만 사용했다. 세 문서가 같은 교재를 읽고 정리했으므로 반복이 곧 독립 검증을 뜻하지는 않는다. 다만 `allowed-tools`와 우선순위 두 건은 **교재와 어긋나는 방향으로** 두 사람이 각각 공식문서에서 확인한 것이라 성격이 다르다.

### 강조 — 한 문서에서 근거·사례와 함께 깊게

- **재윤**: 점진적 공개를 중심 메시지로 세우고 토큰 프레임워크·자기 시스템 실측·외부 사례로 삼중 뒷받침. 그리고 공식문서 대조 3건을 별도 섹션으로 분리.
- **홍섭**: 자기 스킬을 실제로 재서 기준에 대봄(66·68줄 양호 / 257줄 리팩터 후보). 스스로 던진 질문 2개를 조사로 닫음.
- **준호**: 운영·디버깅·배포·측정의 전 구간 레퍼런스. 특히 실패 모드(YAML 파싱, 리스팅 잘림, 하드 에러)를 증상 기준으로 정리.

### 긴장 — 문서 간 해석·판단이 다름

전부 [maps/open-tensions.md](../maps/open-tensions.md)에 모았다.

| 긴장 | 갈린 방식 | 메모 |
| --- | --- | --- |
| SKILL.md 분량 기준 | 실무 기준(홍섭) / 안전선 유지(재윤) / 잘못된 수치(준호) | [skill-md-length-standard-is-contested](../notes/skill-md-length-standard-is-contested.md) |
| description 100토큰 | 원칙 채택(홍섭) / 단위 사용 후 보정(재윤) / 잘못된 수치(준호) | [description-length-limit-is-contested](../notes/description-length-limit-is-contested.md) |
| `pre-chapter-prep` 포크 | 도입 후보(홍섭) / 부적합 판정(재윤) | [context-fork-scope-is-per-skill-not-per-step](../notes/context-fork-scope-is-per-skill-not-per-step.md) |
| 환각 방지 범위 | 지침 3종(재윤) / 지침 + 구조적 검증(준호) | [instructions-lower-probability-verification-is-deterministic](../notes/instructions-lower-probability-verification-is-deterministic.md) |
| YAML 오류 시 동작 | 스킬 전체 미로드(재윤·교재) / 본문만 로드(준호·공식 디버그 문서) | [yaml-error-loads-body-with-empty-metadata](../notes/yaml-error-loads-body-with-empty-metadata.md) |

측정 축도 셋이 달랐으나(홍섭 비용 / 재윤 정합성 / 준호 효과) 서로 배타적이지 않고 상보적이어서 긴장이 아니라 개념 메모로 통합했다 → [skill-measurement-has-four-axes](../notes/skill-measurement-has-four-axes.md). 네 축 구분은 합성자의 해석이며 원문에 그런 분류는 없다.

### 독창 — 한 문서에만 있으나 후속 가치가 높음

- **준호**: [yaml-error-loads-body-with-empty-metadata](../notes/yaml-error-loads-body-with-empty-metadata.md), [skills-do-not-travel-across-surfaces-unchanged](../notes/skills-do-not-travel-across-surfaces-unchanged.md), [user-invocable-does-not-block-autonomous-execution](../notes/user-invocable-does-not-block-autonomous-execution.md), [skill-activation-is-not-evidence-of-quality](../notes/skill-activation-is-not-evidence-of-quality.md), [eval-first-skill-development](../notes/eval-first-skill-development.md), [opus5-keep-output-norms-drop-procedure-instructions](../notes/opus5-keep-output-norms-drop-procedure-instructions.md), [degrees-of-freedom-should-match-the-task](../notes/degrees-of-freedom-should-match-the-task.md), [cite-sources-invites-fabricated-sources](../notes/cite-sources-invites-fabricated-sources.md), [background-fork-edits-escape-rewind](../notes/background-fork-edits-escape-rewind.md), [script-invocation-must-be-explicit](../notes/script-invocation-must-be-explicit.md), [token-count-not-line-count-is-the-real-measure](../notes/token-count-not-line-count-is-the-real-measure.md)
- **홍섭**: [nova-workflow-as-team-plugin-distribution](../notes/nova-workflow-as-team-plugin-distribution.md), [env-values-belong-in-settings-not-in-skills](../notes/env-values-belong-in-settings-not-in-skills.md)
- **재윤**: [ecc-286-skills-as-progressive-disclosure-proof](../notes/ecc-286-skills-as-progressive-disclosure-proof.md), [omc-triggers-field-separates-activation-from-description](../notes/omc-triggers-field-separates-activation-from-description.md)

준호 정리본에서 독창 항목이 많은 것은 그 문서만 운영·측정·배포 영역을 다뤘기 때문이지 다른 문서가 부실해서가 아니다. 세 문서의 관심 영역이 겹치지 않게 나뉘어 있었다.

## 생성한 원자 메모 (38개)

| 축 | 메모 |
| --- | --- |
| 점진적 공개·토큰 비용 | progressive-disclosure-makes-unused-knowledge-free · skill-body-is-recurring-context-cost · compaction-reattachment-budget-limits-skill-persistence · scripts-cost-only-their-output · script-invocation-must-be-explicit · support-file-references-must-stay-one-level-deep · skill-should-contain-only-what-claude-cannot-know · examples-consume-a-fifth-to-half-of-skill-tokens · skill-token-budget-target-15-percent · team-has-no-skill-scripts-yet |
| 호출·발견 | commands-and-skills-differ-only-in-invocation-control · user-invocable-does-not-block-autonomous-execution · description-decides-activation · skill-listing-budget-truncates-descriptions · skill-name-is-a-label-not-a-rule · yaml-error-loads-body-with-empty-metadata |
| 권한·배포 | allowed-tools-grants-rather-than-restricts · skills-can-grant-themselves-broad-tool-access · personal-skills-silently-override-project-skills · skills-do-not-travel-across-surfaces-unchanged · env-values-belong-in-settings-not-in-skills |
| 격리 실행 | context-fork-suits-conclusion-only-tasks · forked-skill-without-a-task-returns-nothing · background-fork-edits-escape-rewind · context-fork-scope-is-per-skill-not-per-step |
| 품질·신뢰성 | skill-activation-is-not-evidence-of-quality · skill-measurement-has-four-axes · eval-first-skill-development · instructions-lower-probability-verification-is-deterministic · cite-sources-invites-fabricated-sources · opus5-keep-output-norms-drop-procedure-instructions · degrees-of-freedom-should-match-the-task |
| 기준 논쟁 | skill-md-length-standard-is-contested · token-count-not-line-count-is-the-real-measure · description-length-limit-is-contested |
| 사례 | nova-workflow-as-team-plugin-distribution · ecc-286-skills-as-progressive-disclosure-proof · omc-triggers-field-separates-activation-from-description |

## 갱신한 기존 메모

없음. 첫 합성이라 기존 `notes/`가 비어 있었다.

## 생성한 지도 (6개)

- [progressive-disclosure-and-token-cost](../maps/progressive-disclosure-and-token-cost.md)
- [skill-invocation-and-discovery](../maps/skill-invocation-and-discovery.md)
- [skill-permissions-and-distribution](../maps/skill-permissions-and-distribution.md)
- [context-isolation-with-fork](../maps/context-isolation-with-fork.md)
- [skill-quality-and-reliability](../maps/skill-quality-and-reliability.md)
- [open-tensions](../maps/open-tensions.md) — 주차마다 누적하고, 해소되면 해당 메모의 `status`를 올리고 내리는 운영용 지도

## 해결되지 않은 질문과 다음 검증 항목

재현·확인으로 닫을 수 있는 것부터 배치했다.

1. **YAML 파싱 오류 시 실제 동작.** 프론트매터를 일부러 깨뜨린 임시 스킬을 만들어 `/skills` 노출과 직접 호출 가능 여부를 확인하면 두 서술 중 어느 쪽인지 바로 갈린다.
2. **ECC 규모에서 리스팅 예산.** 286개 스킬이면 기본 1% 예산으로 대부분의 description이 잘릴 텐데 발동이 어떻게 유지되는가. 두 메모가 정면으로 부딪히는데 어느 정리본에도 답이 없다.
3. **단계 단위 포크 가능 여부.** `context`가 스킬 단위 필드라면 "3단계만 포크"가 성립하지 않는다. 확인되면 홍섭·재윤의 판단 차이가 자동으로 정리된다.
4. **우리 스킬 9개의 스펙 밖 필드 목록.** `argument-hint`, `disable-model-invocation`은 확실히 Claude Code 전용이다. 웹·Cowork 배포를 고려한다면 전수 조사가 필요하다.
5. **팀 규약 3건.** 분량 기준에 숫자를 넣을지 / 개인 스킬 네이밍 규약 / 승격 절차에 권한 검토 항목을 넣을지.
6. **개별 SKILL.md 본문의 토큰 수 측정 수단.** 줄 수 대신 토큰을 기준으로 쓰자는 주장에 대응하는 측정 도구가 어느 정리본에도 없다.

## 이번 합성의 한계

- **첫 합성이라 챕터 간 연결이 없다.** 모든 메모의 출처가 3장 하나다. 다음 챕터 합성부터 기존 메모 갱신이 발생한다.
- **ch2 정리본(홍섭·재윤 2개)이 아직 합성되지 않았다.** 유효한 입력 단위인데 이번 범위에 넣지 않았다. ch2의 설정 위계·확장 도구 구분(Skill=지식 확장 / 서브에이전트=능력 확장)은 이번 메모들과 직접 이어질 가능성이 높다. ch1은 정리본이 홍섭 1개뿐이라 입력 최소 조건(2개 이상)에 못 미친다.
- **연결 없는 메모는 없다.** 38개 전부 최소 1개 이상의 다른 메모 또는 지도에 연결되어 있다.
