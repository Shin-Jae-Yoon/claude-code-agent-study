---
title: "제한처럼 읽히지만 막지 않는 장치가 반복해서 나타난다"
type: "concept"
status: "growing"
tags: ["permissions", "security", "cross-chapter"]
---

# 제한처럼 읽히지만 막지 않는 장치가 반복해서 나타난다

Claude Code의 설정·프론트매터에는 이름이 금지처럼 읽히지만 실제로는 아무것도 막지 않는 항목이 여럿 있다. 각각은 개별 함정이지만 모아 놓으면 하나의 패턴이다 — **이름을 근거로 안전하다고 판단하면 안 되고, 무엇이 실제로 차단되는지 따로 확인해야 한다.** 두 챕터에 걸쳐 최소 다섯 번 반복됐다.

| 장치 | 이름이 시사하는 것 | 실제 동작 |
| --- | --- | --- |
| `allowed-tools` | 이 도구만 쓸 수 있다 | 나열된 도구를 **사전 승인**할 뿐, 나머지도 호출 가능 |
| `user-invocable: false` | 사용자만 못 쓴다 | `/` 메뉴 노출만 제어. 클로드의 자율 실행은 그대로 |
| `permissions.deny`의 Read 차단 | 이 파일을 못 읽는다 | Bash가 열려 있으면 `cat`으로 우회 가능 |
| 설정 파일의 strict 검증 | 잘못된 key는 거부된다 | 미정의 key는 조용히 무시되고 실행됨 |
| 프론트매터 YAML | 깨지면 스킬이 안 뜬다 | 본문은 빈 메타데이터로 로드되어 절반만 동작 |

## 근거와 출처

이 표는 합성자가 두 챕터의 개별 발견을 묶은 것이다. 각 행의 근거는 아래 메모에 있다.

- [allowed-tools는 제한이 아니라 사전 승인이다](./allowed-tools-grants-rather-than-restricts.md) — 3장 재윤·준호
- [user-invocable은 자율 실행을 막지 못한다](./user-invocable-does-not-block-autonomous-execution.md) — 3장 준호
- [Read 차단은 Bash 우회를 막지 못한다](./read-deny-does-not-block-bash-bypass.md) — 2장 재윤
- [미정의 설정 key는 거부되지 않고 조용히 무시된다](./undefined-settings-keys-are-silently-ignored.md) — 2장 홍섭
- [YAML이 깨지면 본문만 빈 메타데이터로 로드된다](./yaml-error-loads-body-with-empty-metadata.md) — 3장 준호

## 연결

- [스킬은 스스로에게 넓은 도구 권한을 줄 수 있다](./skills-can-grant-themselves-broad-tool-access.md) — 이 패턴이 보안 문제가 되는 지점이다.
- [MCP 권한 와일드카드는 그 서버의 모든 도구를 자동 승인한다](./mcp-wildcard-permissions-auto-approve-every-tool.md) — 반대로 "허용" 쪽이 이름보다 넓게 작동하는 사례다.
- [환각 방지에 지침으로 충분한가 검증 장치까지 필요한가](./instructions-lower-probability-verification-is-deterministic.md) — 같은 교훈의 다른 영역판이다. 선언은 확률을 바꾸고 강제는 결정론적이다.

## 열린 질문

- 다섯 사례 중 넷이 "조용히" 실패한다. 경고 없이 넘어가는 실패를 어떻게 우리 리뷰 절차에서 잡을 것인가? `$schema` 지정(설정), `--debug`(프론트매터)처럼 항목별로 다른 수단이 필요해 보인다.
