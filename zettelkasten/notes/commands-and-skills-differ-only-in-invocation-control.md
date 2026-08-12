---
title: "커맨드와 스킬의 남은 차이는 호출 제어뿐이다"
type: "claim"
status: "growing"
tags: ["invocation", "skill-authoring"]
---

# 커맨드와 스킬의 남은 차이는 호출 제어뿐이다

커스텀 커맨드와 스킬은 통합됐다. 두 위치의 파일이 동일한 `/슬래시` 인터페이스를 만들고 같은 frontmatter를 지원한다. 남은 차이는 "누가 호출하는가"를 정하는 필드이며, 그중 `disable-model-invocation`이 성격을 가른다 — 있으면 사람만 부르는 커맨드형, 없으면 클로드도 부르는 스킬형이다.

## 근거와 출처

- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md): "통합의 실체 = 호출 방식 통합"으로 확정했다. 실측 대비도 함께 — nova-workflow의 `commit`·`pr`·`handoff`는 `disable-model-invocation` + `argument-hint`를 달아 커맨드 성격이고, `humanize-korean`은 description에 트리거 문구를 넣어 자연어로 발동한다.
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): "`.claude/commands/deploy.md`와 `.claude/skills/deploy/SKILL.md`는 똑같이 `/deploy`를 만든다. 신규는 무조건 스킬로." 스킬만 되는 것으로 딸린 파일, 중첩 디렉터리 자동 탐색, 플러그인 패키징을 들었고 이름 충돌 시 스킬이 이긴다고 정리했다.
- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 실측으로 확인했다. 이 저장소에 `.claude/commands/`는 없고, 스킬 2개가 `disable-model-invocation: true`로 자동 호출을 끄고 `/` 수동 호출만 남겨 커맨드처럼 쓰이고 있다.
- [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md): 한 챕터 앞서 같은 결론에 도달해 있었다. 6항목 비교표(형식·호출·보조 자료·용도·표준·권장 여부)로 정리하고 "커스텀 Commands는 현재 Skills에 통합되어 있으며 기존 `.claude/commands/*.md`도 계속 사용할 수 있다", "같은 이름의 Command와 Skill이 있으면 Skill이 우선한다"고 썼다. 내장 `/help`·`/compact`·`/permissions`는 CLI 구현 명령이라 커스텀 Commands와 별개라는 구분도 덧붙였다.

## 연결

- [user-invocable은 자율 실행을 막지 못한다](./user-invocable-does-not-block-autonomous-execution.md) — 호출 제어 필드 중 이름과 동작이 어긋나는 쪽이다.
- [발동을 결정하는 것은 name이 아니라 description이다](./description-decides-activation.md) — 자동 호출이 켜져 있을 때 무엇이 그 호출을 부르는지에 대한 답이다.
- [스킬 이름은 규칙이 아니라 라벨이다](./skill-name-is-a-label-not-a-rule.md) — 통합 이후 `/` 커맨드 이름이 어디서 오는지에 대한 답이다.
