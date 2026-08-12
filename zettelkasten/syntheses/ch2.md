# ch2 합성 기록 — 워크플로와 설정

> 합성일: 2026-08-12 · **두 번째 합성.** 3장을 먼저 합성한 뒤 소급해서 2장을 넣었으므로, 이번 기록의 핵심은 새 메모보다 **기존 메모와의 연결**이다.

## 입력

| 작성자 | 파일 | 줄 수 |
| --- | --- | --- |
| 홍섭 | [chapters/ch2/hongseob/정리본.md](../../chapters/ch2/hongseob/정리본.md) | 137 |
| 재윤 | [chapters/ch2/jaeyoon/정리본.md](../../chapters/ch2/jaeyoon/정리본.md) | 485 |

준호는 2장 정리본이 없다. 1장은 홍섭 정리본 하나뿐이라 입력 최소 조건(2개 이상)에 못 미쳐 이번에도 제외했다.

## 신호

### 반복 — 두 문서 모두에서 등장

- 설정 위계, 더 구체적인 쪽이 이김 → [settings-hierarchy-inverts-skill-priority](../notes/settings-hierarchy-inverts-skill-priority.md)
- `settings.json`의 `env`로 환경변수 주입 → [env-values-belong-in-settings-not-in-skills](../notes/env-values-belong-in-settings-not-in-skills.md)
- `CLAUDE.md` 3계층과 자동 로드 → [claude-md-is-always-loaded-skills-are-conditional](../notes/claude-md-is-always-loaded-skills-are-conditional.md)
- 탐색은 범위를 좁혀 가며 앞 단계 결과를 다음 입력으로 → [narrow-the-scope-instead-of-asking-everything](../notes/narrow-the-scope-instead-of-asking-everything.md)
- 피드백 루프가 프롬프트보다 중요 → [feedback-loop-beats-prompt-quality](../notes/feedback-loop-beats-prompt-quality.md)
- 작업 단위는 검증 가능한 최소 변경 → [atomic-sub-requirement-not-line-count](../notes/atomic-sub-requirement-not-line-count.md)
- 플랜 모드로 탐색과 실행 분리 → [plan-mode-separates-exploration-from-execution](../notes/plan-mode-separates-exploration-from-execution.md)

### 강조 — 한 문서에서 근거·사례와 함께 깊게

- **홍섭**: 실험 3개로 층을 갈랐다. 임의 key(`--settings`로 미정의 key 주입), `.env`(셸 3줄 실험), `settings env`(공식문서 대조). 특히 스프링부트 문제를 셸 레이어와 스프링 레이어로 나눠 진단하고 실전 2안까지 비교했다.
- **재윤**: Graphify·CodeGraph·Ouroboros를 각 저장소 공식 문서로 조사해 "경쟁 도구가 아니라 서로 다른 병목"이라는 배치를 만들었다. 확장 도구 5종(Skill·서브에이전트·MCP·Hooks·Plugin)도 역할 축으로 정리했다.

### 긴장 — 두 문서의 판단이 갈림

| 긴장 | 갈린 방식 | 처리 |
| --- | --- | --- |
| 워크플로 단계 명명 | 재윤 5단계(탐색→계획→구현→검증→커밋) / 홍섭 3단계(탐색→분석→심화) | 실질 차이가 아니라 서술 입도 차이로 판단해 별도 메모를 만들지 않았다 |
| `env` 주제 깊이 | 홍섭은 실행까지(A vs B 비교, B 추천) / 재윤은 개념 소개 후 충돌 우선순위를 "확인 필요"로 열어둠 | 두 관점을 한 메모의 근거와 열린 질문으로 합쳤다 |
| 점진 개발 단위 | 홍섭은 정량 기준에 회의적 / 재윤은 3축으로 절차화 | [atomic-sub-requirement-not-line-count](../notes/atomic-sub-requirement-not-line-count.md)로 만들었고, 3장의 분량 논쟁과 이어지며 챕터 간 긴장이 됐다 |

### 독창 — 한 문서에만 있으나 후속 가치가 높음

- **홍섭**: [undefined-settings-keys-are-silently-ignored](../notes/undefined-settings-keys-are-silently-ignored.md), [dotenv-is-not-read-by-shell-or-spring](../notes/dotenv-is-not-read-by-shell-or-spring.md)
- **재윤**: [read-deny-does-not-block-bash-bypass](../notes/read-deny-does-not-block-bash-bypass.md), [mcp-wildcard-permissions-auto-approve-every-tool](../notes/mcp-wildcard-permissions-auto-approve-every-tool.md), [hooks-run-deterministically-outside-llm-judgment](../notes/hooks-run-deterministically-outside-llm-judgment.md), [skill-extends-knowledge-subagent-extends-capability](../notes/skill-extends-knowledge-subagent-extends-capability.md), [tools-solve-different-bottlenecks-not-the-same-one](../notes/tools-solve-different-bottlenecks-not-the-same-one.md)

## 챕터 간 연결 — 이번 합성의 실제 산출

3장 메모와 맞물리면서 드러난 것들이다. 어느 한 챕터만 봐서는 나오지 않는다.

**① `allowed-tools`를 2장은 처음부터 맞게 적었다.** 3장 교재 노트가 이 필드를 "원천 차단"으로 서술했고 3장 공식문서 대조가 이를 정정했는데, [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md)에는 이미 "Skill 실행 중 **사전 승인**할 도구"라고 쓰여 있었다. 3장의 정정은 새 발견이 아니라 **복귀**였다. → [allowed-tools-grants-rather-than-restricts](../notes/allowed-tools-grants-rather-than-restricts.md) `status: evergreen`으로 승격.

**② 설정과 스킬의 우선순위가 사용자·프로젝트 구간에서 뒤집힌다.** 설정은 프로젝트가 사용자를 이기고, 스킬은 사용자가 프로젝트를 이긴다. 두 챕터의 우선순위 표를 나란히 놓기 전에는 아무도 지적하지 않았다. 실무 함의가 크다 — 같은 저장소에서 `.claude/settings.json`은 팀 값을 강제하는데 `.claude/skills/`는 팀 스킬을 강제하지 못한다. → 새 메모 [settings-hierarchy-inverts-skill-priority](../notes/settings-hierarchy-inverts-skill-priority.md)

**③ 줄 수를 기준에서 밀어내는 주장이 두 챕터에서 반복된다.** 2장은 작업 크기를 "몇 줄"이 아니라 검증 가능성으로, 3장은 문서 길이를 "몇 줄"이 아니라 토큰으로 재라고 한다. 대상은 다르고 형태는 같다. 우리 팀이 정량 기준을 두고 반복해서 같은 곳에서 막힌다는 신호로 읽을 수 있다.

**④ "제한처럼 읽히지만 막지 않는" 장치가 다섯 번 반복됐다.** 3장에서 둘(`allowed-tools`, `user-invocable`), 2장에서 둘(Read deny의 Bash 우회, 미정의 설정 key), 그리고 YAML 파싱 실패까지. 개별 함정으로 흩어져 있던 것을 하나의 패턴으로 묶었다. → 새 메모 [controls-that-read-as-limits-but-do-not-block](../notes/controls-that-read-as-limits-but-do-not-block.md)

**⑤ 3장이 던진 질문의 답이 2장에 있었다.** 3장의 "지침은 확률을 낮추고 검증은 결정론적이다"라는 긴장에서, 결정론적 강제의 구현 수단으로 2장의 Hooks가 그대로 들어맞는다. 스크립트가 스킬 안의 결정론이라면 Hooks는 생명주기에 붙은 결정론이다. 마찬가지로 3장의 "평가부터 만든다"는 2장의 "좋은 프롬프트보다 좋은 피드백 루프"와 같은 사고가 대상만 바꾼 것이다.

**⑥ 점진적 공개와 범위 좁히기는 같은 원리의 두 층이다.** 3장은 파일 로딩에서, 2장은 대화 진행에서 "필요할 때까지 안 가져온다"를 실현한다.

**⑦ `context: fork`는 2장의 두 축이 만나는 필드다.** 2장이 스킬을 지식 확장, 서브에이전트를 능력 확장으로 나눴는데, 3장의 `context: fork`는 지식 확장 수단을 능력 확장 수단으로 실행하는 것이다. 격리의 강도 축도 생겼다 — 플랜 모드는 같은 대화에서 쓰기 권한만 잠그고, 포크는 대화 자체를 분리한다.

**⑧ 지침을 어디에 두느냐가 곧 비용 결정이다.** `CLAUDE.md`는 매 세션 상주하고 스킬은 조건부다. 2장은 이 선택을 "문서가 길어지면 Skill로 분리한다"는 실무 기준으로만 다뤘는데, 3장의 로딩 모델이 그 기준에 비용 근거를 붙여준다.

## 생성한 원자 메모 (14개)

| 축 | 메모 |
| --- | --- |
| 설정 계층 | settings-hierarchy-inverts-skill-priority · claude-md-is-always-loaded-skills-are-conditional · undefined-settings-keys-are-silently-ignored · dotenv-is-not-read-by-shell-or-spring |
| 권한·보안 | controls-that-read-as-limits-but-do-not-block · read-deny-does-not-block-bash-bypass · mcp-wildcard-permissions-auto-approve-every-tool |
| 탐색·계획 | narrow-the-scope-instead-of-asking-everything · plan-mode-separates-exploration-from-execution · tools-solve-different-bottlenecks-not-the-same-one |
| 작업 방식 | feedback-loop-beats-prompt-quality · atomic-sub-requirement-not-line-count |
| 확장 도구 | skill-extends-knowledge-subagent-extends-capability · hooks-run-deterministically-outside-llm-judgment |

## 갱신한 기존 메모 (11개)

| 메모 | 갱신 내용 |
| --- | --- |
| [allowed-tools-grants-rather-than-restricts](../notes/allowed-tools-grants-rather-than-restricts.md) | 2장 재윤 출처 추가. "정정이 아니라 복귀"라는 해석 추가. `status: growing → evergreen` |
| [env-values-belong-in-settings-not-in-skills](../notes/env-values-belong-in-settings-not-in-skills.md) | 2장 홍섭·재윤 출처 추가(이 실천의 원 출처). 열린 질문 하나 해소. `status: seed → growing` |
| [commands-and-skills-differ-only-in-invocation-control](../notes/commands-and-skills-differ-only-in-invocation-control.md) | 2장 재윤의 6항목 비교표 출처 추가 |
| [personal-skills-silently-override-project-skills](../notes/personal-skills-silently-override-project-skills.md) | 설정 우선순위와의 역전 대조 링크 |
| [user-invocable-does-not-block-autonomous-execution](../notes/user-invocable-does-not-block-autonomous-execution.md) | 상위 패턴 메모로 연결 |
| [yaml-error-loads-body-with-empty-metadata](../notes/yaml-error-loads-body-with-empty-metadata.md) | 설정 key의 조용한 무시와 같은 계열로 연결 |
| [token-count-not-line-count-is-the-real-measure](../notes/token-count-not-line-count-is-the-real-measure.md) | 2장의 동형 주장(atomic sub-requirement) 연결 |
| [instructions-lower-probability-verification-is-deterministic](../notes/instructions-lower-probability-verification-is-deterministic.md) | Hooks·피드백 루프 연결 |
| [context-fork-suits-conclusion-only-tasks](../notes/context-fork-suits-conclusion-only-tasks.md) | 지식·능력 확장 구분, 플랜 모드 연결 |
| [skill-should-contain-only-what-claude-cannot-know](../notes/skill-should-contain-only-what-claude-cannot-know.md) | "무엇을" vs "어디에"의 짝 연결 |
| [eval-first-skill-development](../notes/eval-first-skill-development.md) | 2장 피드백 루프 연결 |
| [skills-can-grant-themselves-broad-tool-access](../notes/skills-can-grant-themselves-broad-tool-access.md) | MCP 와일드카드, 상위 패턴 연결 |
| [progressive-disclosure-makes-unused-knowledge-free](../notes/progressive-disclosure-makes-unused-knowledge-free.md) | CLAUDE.md 대비, 범위 좁히기 연결 |

## 생성·갱신한 지도

**생성 (2개)**

- [exploration-and-planning](../maps/exploration-and-planning.md) — 코드를 쓰기 전 단계
- [configuration-layers](../maps/configuration-layers.md) — 무엇을 어디에 적을 것인가

**갱신 (5개)**

- [skill-permissions-and-distribution](../maps/skill-permissions-and-distribution.md) — 권한 절을 "이름보다 좁게 막는 것"과 "이름보다 넓게 여는 것"으로 재편
- [open-tensions](../maps/open-tensions.md) — "체계 간 규칙이 어긋나는 것"과 "조용히 실패하는 것들" 두 절 신설
- [progressive-disclosure-and-token-cost](../maps/progressive-disclosure-and-token-cost.md) — 대화 층위와 CLAUDE.md 반대편 추가
- [skill-quality-and-reliability](../maps/skill-quality-and-reliability.md) — Hooks와 피드백 루프 추가
- [context-isolation-with-fork](../maps/context-isolation-with-fork.md) — "다른 강도의 격리" 절 신설

## 해결되지 않은 질문과 다음 검증 항목

3장 합성의 목록에 이어 2장에서 새로 열린 것들이다.

1. **셸 환경변수와 `settings.json`의 `env`가 충돌하면 어느 쪽이 이기는가.** 2장 재윤 정리본이 남긴 질문이고 아직 아무도 확인하지 않았다. 셸에서 `export FOO=a` 한 뒤 `settings.json`에 `FOO=b`를 넣고 실행하면 바로 갈린다.
2. **설정과 스킬의 우선순위가 왜 반대인가.** 설정은 "환경이 구체적일수록 이긴다", 스킬은 "사람이 고른 것이 이긴다"로 보이지만 공식 설명을 못 찾았다.
3. **`$schema`를 우리 설정 파일에 넣을 것인가.** 미정의 key를 편집 단계에서 잡는 유일한 확인된 수단이다.
4. **Hook 도입 대상.** 재윤이 2장에서 "다음으로 적용해 볼 설정"으로 지목했으나 그대로 남아 있다. `CLAUDE.md`의 한국어 규약이나 개인 폴더 경계처럼 결정론적 강제가 어울리는 규칙이 후보다.
5. **홍섭이 팀에 던진 질문이 아직 답을 못 받았다.** 각자 어느 단위로 작업하고 어떤 자동 검증 수단을 쓰는지.
6. **Bash 우회를 실제로 막는 방법.** deny 나열로는 우회 명령이 무한해 닫히지 않는다.

## 이번 합성의 한계

- **1장은 여전히 미합성이다.** 홍섭 정리본 하나뿐이라 입력 최소 조건에 못 미친다. 다른 사람의 1장 정리본이 생기면 그때 합성한다. 다만 홍섭 2장 정리본에 1장의 `@경로` 토큰 실험(10,500 대 175)이 사례로 인용되어 있어, 그 결과는 [narrow-the-scope-instead-of-asking-everything](../notes/narrow-the-scope-instead-of-asking-everything.md)에 간접적으로 들어와 있다.
- **2장을 소급 합성했으므로 3장 메모의 "첫 출처"가 실제로는 2장인 경우가 있다.** `allowed-tools`가 그 사례다. 앞으로는 챕터 순서대로 합성하는 편이 출처 이력이 자연스럽다.
- **연결 없는 메모는 없다.** 52개 전부 최소 1개 이상의 다른 메모 또는 지도에 연결되어 있다.
