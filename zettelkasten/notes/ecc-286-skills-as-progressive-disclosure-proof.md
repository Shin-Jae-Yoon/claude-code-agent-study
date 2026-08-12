---
title: "ECC의 286개 스킬은 점진적 공개의 실증이다"
type: "example"
status: "seed"
tags: ["progressive-disclosure", "example", "token-cost"]
---

# ECC의 286개 스킬은 점진적 공개의 실증이다

[ECC — Everything Claude Code](https://github.com/affaan-m/ecc)는 68개 에이전트와 286개 스킬을 한 플러그인으로 제공한다. 이 규모를 깔고도 세션이 감당되는 이유가 정확히 점진적 공개다. 1단계 메타데이터만 상주하고 본문은 on-demand로 로드되기 때문이다. 프로젝트 표어도 같은 이야기를 한다 — *"Optimize the context window. Persist everything else."*

## 근거와 출처

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 외부 레퍼런스로 조사했다. 인용 — *"Access to 68 agents, 286 skills, and 94 legacy command shims"*, *"Keeping those jobs separate is how ECC adds capability without dumping the entire repository into every session."* 대표 스킬로 `tdd-workflow`, `security-review`, `e2e-testing`, `search-first`를 들었고, Claude Code·Codex·Cursor·OpenCode에서 함께 동작한다는 점이 우리가 `.codex/skills`를 미러링하는 것과 같은 문제의식이라고 봤다.

> 수치는 프로젝트 자체 문서에서 나온 값이며 독립 검증된 것이 아니다. ECC는 공식 Anthropic 산출물이 아닌 서드파티 커뮤니티 플러그인이다.

## 연결

- [점진적 공개는 쓰지 않는 지식의 비용을 0으로 만든다](./progressive-disclosure-makes-unused-knowledge-free.md) — 이 사례가 뒷받침하는 주장이다.
- [스킬 목록 예산을 넘으면 description부터 잘려나간다](./skill-listing-budget-truncates-descriptions.md) — 이 사례와 정면으로 부딪히는 제약이다. 286개 규모에서 기본 1% 예산이면 대부분의 description이 잘릴 텐데 어떻게 발동이 유지되는지는 확인되지 않았다.
- [스킬은 스스로에게 넓은 도구 권한을 줄 수 있다](./skills-can-grant-themselves-broad-tool-access.md) — 서드파티 플러그인이므로 설치 전 검토 대상이다.
