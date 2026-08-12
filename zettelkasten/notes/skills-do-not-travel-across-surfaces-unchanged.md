---
title: "스킬은 표면을 넘을 때 그대로 가지 않는다"
type: "claim"
status: "seed"
tags: ["distribution", "team-convention"]
---

# 스킬은 표면을 넘을 때 그대로 가지 않는다

Claude Code에서 잘 도는 스킬이 다른 표면에서도 그대로 동작하지 않는다. 두 가지가 걸린다. 첫째, **Cowork와 클라우드 세션은 로컬 `~/.claude/skills/`를 읽지 않는다** — claude.ai 계정에 활성화해둔 스킬을 세션 시작 시 동기화받고, 클라우드 세션만 추가로 클론한 저장소의 `.claude/skills/`를 읽는다. 둘째, **Claude Code 밖에서는 frontmatter 필드가 6개로 제한되고, 스펙 밖 필드는 무시가 아니라 하드 에러로 실패한다.**

## 근거와 출처

- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): 두 제약을 모두 기록했다. 개인 스킬만 만들어두면 웹·Cowork에서는 "스킬을 찾을 수 없다"가 되므로 "여러 표면을 쓰는 팀이라면 배포 경로를 처음부터 이걸 전제로 설계해야 한다". 필드 제한은 `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` 6개이며, 실패 메시지 예시까지 실었다 — `Unexpected key(s) in SKILL.md frontmatter: argument-hint.` 결론은 "웹·Cowork까지 커버해야 하는 공용 스킬은 6개 필드로만 작성하고, 호출 제어가 필요한 것은 Claude Code 전용 세트로 분리한다".

## 연결

- [개인 스킬이 프로젝트 스킬을 조용히 덮어쓴다](./personal-skills-silently-override-project-skills.md) — 스킬을 "어디에 두느냐"가 동작을 바꾸는 같은 계열의 문제다.
- [커맨드와 스킬의 남은 차이는 호출 제어뿐이다](./commands-and-skills-differ-only-in-invocation-control.md) — 그 호출 제어 필드들이 정확히 표면을 못 넘는 필드라는 점에서 이어진다.

## 열린 질문

- 우리 공통 스킬 9개는 프로젝트 스킬이므로 클라우드 세션은 커버되지만 Cowork는 커버되지 않는다. 우리 중 Cowork를 쓰는 사람이 있는가?
- 우리 스킬이 쓰는 Claude Code 전용 필드가 무엇인지 아직 세어보지 않았다. `argument-hint`, `disable-model-invocation`은 확실히 스펙 밖이다.
