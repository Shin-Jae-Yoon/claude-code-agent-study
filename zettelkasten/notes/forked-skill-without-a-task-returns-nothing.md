---
title: "태스크 없는 스킬을 포크하면 빈손으로 돌아온다"
type: "claim"
status: "growing"
tags: ["context-fork", "subagent"]
---

# 태스크 없는 스킬을 포크하면 빈손으로 돌아온다

`context: fork`는 SKILL.md 본문을 서브에이전트의 프롬프트로 넘긴다. 본문이 "이 API 컨벤션을 따르라" 같은 지침만 담고 수행할 태스크가 없으면, 서브에이전트는 지침만 받고 실행할 것이 없어 의미 있는 결과 없이 돌아온다. 레퍼런스·가이드라인형 스킬에는 포크를 쓰면 안 된다.

## 근거와 출처

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 공식문서 경고를 인용했다. *"`context: fork` only makes sense for skills with explicit instructions. If your skill contains guidelines like 'use these API conventions' without a task, the subagent receives the guidelines but no actionable prompt, and returns without meaningful output."* 이 기준을 자기 스킬에 적용해 `mid-zettelkasten-synthesis`는 "원자 메모와 주제 지도를 재구성하라"는 명확한 태스크가 있어 경고에 걸리지 않는다고 판단했다.
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): 포크의 세 조건 중 하나로 "실행할 태스크가 있다 — 지침만 있고 태스크가 없으면 서브에이전트는 할 일 없이 끝난다"를 들고, 쓰면 안 되는 경우 첫 항목을 "레퍼런스·가이드라인형 스킬 (태스크가 없다)"로 두었다.

## 연결

- [context: fork는 결론만 필요한 작업에 적합하다](./context-fork-suits-conclusion-only-tasks.md) — 그 적합 조건 중 하나를 이 메모가 상세히 다룬다.
- [단계 단위 포크가 가능한지 아직 모른다](./context-fork-scope-is-per-skill-not-per-step.md) — 지침과 태스크가 한 스킬에 섞여 있을 때 무엇이 포크되는가라는 문제로 이어진다.
