---
title: "OMC는 트리거를 description에서 분리해 별도 필드로 둔다"
type: "example"
status: "seed"
tags: ["discovery", "example", "invocation"]
---

# OMC는 트리거를 description에서 분리해 별도 필드로 둔다

[oh-my-claudecode(OMC)](https://github.com/Yeachan-Heo/oh-my-claudecode)는 frontmatter에 `triggers` 배열을 둔다. 교재가 "고유 트리거 용어를 `description`에 넣어라"라고 한 것을 별도 필드로 분리한 설계다. 같은 문제(무엇이 이 스킬을 부르게 하는가)에 대한 다른 해법이다.

```yaml
name: Fix Proxy Crash
description: aiohttp proxy crashes on ClientDisconnectedError
triggers: ["proxy", "aiohttp", "disconnected"]
source: extracted
```

## 근거와 출처

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 외부 레퍼런스로 조사했다. OMC는 19개 전문 에이전트와 39개 스킬로 Claude·Gemini·Codex를 함께 굴리는 멀티에이전트 오케스트레이션 플러그인이며, 자체 스코프(`.omc/skills/` 프로젝트 / `~/.omc/skills/` 사용자)를 쓴다는 점도 함께 기록했다. 이는 교재의 개인·프로젝트 2단 구조와 같은 발상이다.

> 서드파티 커뮤니티 플러그인이며, 스킬·에이전트 개수는 프로젝트 자체 문서 기준이다.

## 연결

- [발동을 결정하는 것은 name이 아니라 description이다](./description-decides-activation.md) — 이 사례가 그 설계를 다르게 푼 대안이다.
- [description 길이 기준을 두고 해석이 갈린다](./description-length-limit-is-contested.md) — 트리거를 분리하면 description 길이 압박이 줄어든다는 함의가 있다(합성자 해석). 참고로 Claude Code에도 같은 목적의 `when_to_use` 필드가 있으나, 이쪽은 description과 1,536자 캡을 공유한다.
- [스킬은 표면을 넘을 때 그대로 가지 않는다](./skills-do-not-travel-across-surfaces-unchanged.md) — `triggers`는 표준 스펙 밖 필드이므로 Claude Code 외 표면에서 어떻게 처리되는지는 별개 문제다.
