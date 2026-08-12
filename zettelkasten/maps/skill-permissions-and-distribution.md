# 스킬 권한과 배포

이 지도는 스킬을 **주고받을 때** 생기는 문제를 묶는다. 혼자 쓸 때는 드러나지 않고, 팀에 배포하거나 남의 저장소를 받을 때 나타나는 것들이다.

## 권한 — 이름이 동작을 오해하게 만든다

- [제한처럼 읽히지만 막지 않는 장치가 반복해서 나타난다](../notes/controls-that-read-as-limits-but-do-not-block.md) — **이 절의 상위 메모.** 두 챕터에서 최소 다섯 번 반복된 패턴을 한 표로 묶었다
- [allowed-tools는 제한이 아니라 사전 승인이다](../notes/allowed-tools-grants-rather-than-restricts.md) — 메커니즘
- [user-invocable은 자율 실행을 막지 못한다](../notes/user-invocable-does-not-block-autonomous-execution.md) — 같은 패턴의 다른 필드
- [Read 차단은 Bash 우회를 막지 못한다](../notes/read-deny-does-not-block-bash-bypass.md) — 프론트매터가 아니라 권한 설정에서 나타나는 같은 문제

## 권한 — 반대로 이름보다 넓게 열리는 것

- [스킬은 스스로에게 넓은 도구 권한을 줄 수 있다](../notes/skills-can-grant-themselves-broad-tool-access.md) — 스킬 파일이 통로
- [MCP 권한 와일드카드는 그 서버의 모든 도구를 자동 승인한다](../notes/mcp-wildcard-permissions-auto-approve-every-tool.md) — MCP 설정이 통로. 확장 설치가 곧 권한 부여라는 같은 구조

## 배포 — 두는 위치가 동작을 바꾼다

- [개인 스킬이 프로젝트 스킬을 조용히 덮어쓴다](../notes/personal-skills-silently-override-project-skills.md) — 같은 표면 안에서의 충돌
- [설정 우선순위와 스킬 우선순위는 사용자·프로젝트 구간에서 뒤집힌다](../notes/settings-hierarchy-inverts-skill-priority.md) — 같은 저장소에서 설정은 팀 값을 강제하는데 스킬은 못 한다
- [스킬은 표면을 넘을 때 그대로 가지 않는다](../notes/skills-do-not-travel-across-surfaces-unchanged.md) — 표면을 넘을 때의 단절

## 스킬에 담지 말아야 할 것

- [환경변수 값은 스킬이 아니라 설정에 둔다](../notes/env-values-belong-in-settings-not-in-skills.md) — 절차와 값의 분리
- (비용 관점의 같은 판단: [스킬에는 클로드가 모르는 것만 담는다](../notes/skill-should-contain-only-what-claude-cannot-know.md))

## 사례

- [nova-workflow는 팀 배포 스킬의 실물 사례다](../notes/nova-workflow-as-team-plugin-distribution.md) — 이 지도의 문제들이 실제로 걸리는 유일한 팀 배포 경험

## 관련 지도

- [설정 계층](./configuration-layers.md) — 권한 규칙이 얹히는 계층 구조
- [스킬 호출과 발견](./skill-invocation-and-discovery.md) — 이름 충돌은 곧 발동 대상이 바뀌는 문제이기도 하다
- [열려 있는 긴장](./open-tensions.md) — 리뷰 체크리스트를 규약에 넣을지가 미결이다
