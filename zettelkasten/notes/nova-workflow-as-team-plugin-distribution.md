---
title: "nova-workflow는 팀 배포 스킬의 실물 사례다"
type: "example"
status: "seed"
tags: ["distribution", "example", "team-convention"]
---

# nova-workflow는 팀 배포 스킬의 실물 사례다

교재가 말하는 "팀 스킬"이 추상적 범주가 아니라 실제로 운영 중인 형태로 존재한다. 홍섭이 회사 개발팀에 만들어 제공한 [nova-workflow](https://github.com/mediquitous-dev/nova-workflow) 플러그인은 `nova-api-planner`, `pr`, `commit` 등 18개 스킬을 마켓플레이스로 배포한다. 스터디 3인 중 팀 배포 경로를 실제로 운영해 본 유일한 사례다.

## 근거와 출처

- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md): 스킬 유형 3종(로컬 / 프로젝트 / 팀 배포) 중 팀 배포의 실사례로 소개했다. 이 플러그인의 `commit`·`pr`·`handoff`는 `disable-model-invocation` + `argument-hint`를 달아 커맨드 성격으로 만들었고, `scripts/`·`templates/`는 개별 스킬 폴더가 아니라 플러그인 루트에 두었다.

## 연결

- [커맨드와 스킬의 남은 차이는 호출 제어뿐이다](./commands-and-skills-differ-only-in-invocation-control.md) — 같은 플러그인 안에서 커맨드형과 스킬형을 실제로 나눠 쓴 사례다.
- [개인 스킬이 프로젝트 스킬을 조용히 덮어쓴다](./personal-skills-silently-override-project-skills.md) — 플러그인 스킬은 네임스페이스를 가지므로 이 충돌을 피한다.
- [스킬은 스스로에게 넓은 도구 권한을 줄 수 있다](./skills-can-grant-themselves-broad-tool-access.md) — 배포하는 쪽에 검토 책임이 생기는 지점이다.
- [우리 팀 스킬에는 아직 스크립트가 없다](./team-has-no-skill-scripts-yet.md) — 이 플러그인은 스크립트를 플러그인 루트에 두는 방식을 택했다는 점에서 참고 형태가 된다.
