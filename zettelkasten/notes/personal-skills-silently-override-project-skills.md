---
title: "개인 스킬이 프로젝트 스킬을 조용히 덮어쓴다"
type: "claim"
status: "growing"
tags: ["distribution", "team-convention", "naming"]
---

# 개인 스킬이 프로젝트 스킬을 조용히 덮어쓴다

같은 이름의 스킬이 여러 레벨에 있으면 우선순위는 `enterprise > personal > project`다. 팀이 저장소에 커밋한 프로젝트 스킬보다 팀원 개인의 `~/.claude/skills/` 스킬이 이긴다. 경고 없이 일어나므로, 팀 표준으로 정한 스킬이 특정 팀원의 로컬에서만 조용히 무력화될 수 있다.

## 근거와 출처

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 교재 노트의 `project > user > managed`가 공식과 **반대**임을 대조로 확인했다. 원문: *"When skills share the same name across levels, enterprise overrides personal, and personal overrides project."* 실무 영향을 이렇게 짚었다 — "팀이 `.claude/skills/deploy`를 커밋해도, 팀원 중 누군가 `~/.claude/skills/deploy`를 갖고 있으면 그 사람 로컬에서는 개인 스킬이 실행된다."
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): 같은 우선순위를 기록하고, 이 셋 중 아무거나 번들 스킬과 이름이 같으면 번들을 덮어쓴다는 점(프로젝트에 `code-review`를 두면 기본 `/code-review`가 교체됨)까지 덧붙였다. 플러그인 스킬은 `plugin-name:skill-name` 네임스페이스라 충돌하지 않는다.

## 연결

- [스킬 이름은 규칙이 아니라 라벨이다](./skill-name-is-a-label-not-a-rule.md) — 충돌 단위가 디렉터리 이름이라는 뜻이므로 네이밍 규약의 근거가 된다.
- [스킬은 표면을 넘을 때 그대로 가지 않는다](./skills-do-not-travel-across-surfaces-unchanged.md) — 스킬이 "어디에 두느냐"로 동작이 갈리는 같은 계열의 문제다.
- [nova-workflow는 팀 배포 스킬의 실물 사례다](./nova-workflow-as-team-plugin-distribution.md) — 플러그인 배포는 네임스페이스 덕에 이 충돌을 피한다.
- [설정 우선순위와 스킬 우선순위는 사용자·프로젝트 구간에서 뒤집힌다](./settings-hierarchy-inverts-skill-priority.md) — **2장 합성으로 드러난 대조.** 같은 저장소에서 설정은 팀 값을 강제하는데 스킬은 강제하지 못한다.

## 열린 질문

- 우리 팀은 `pre-`/`mid-` 접두사 규약을 쓰고 있다. 개인 스킬에 같은 접두사를 쓰지 않기로 정할 것인가? 재윤 정리본은 앞으로 개인 스킬을 만들 때 접두사가 겹치면 "팀 스킬이 조용히 무시된다"고 경고했다.
