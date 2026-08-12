---
title: "스킬은 지식을 확장하고 서브에이전트는 능력을 확장한다"
type: "concept"
status: "growing"
tags: ["subagent", "context-management", "cross-chapter"]
---

# 스킬은 지식을 확장하고 서브에이전트는 능력을 확장한다

확장 도구를 기능 목록이 아니라 **무엇을 확장하는가**로 나눈 구분이다. 스킬은 마크다운으로 지식과 절차를 더하고, 서브에이전트는 컨텍스트 격리와 독립 실행으로 역할을 더한다. 같은 축에서 MCP는 외부 데이터 연결과 도구 실행과 표준화된 컨텍스트 제공의 조합, Hooks는 생명주기 이벤트의 결정론적 실행, Plugin은 이 넷을 묶는 배포 단위다.

## 근거와 출처

- [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md): "Skill을 지식이나 절차의 확장으로 본다면, 서브에이전트는 컨텍스트 격리와 독립 실행을 이용한 역할 확장으로 볼 수 있다. 이 정리에서는 Skill을 **지식 확장**, 서브에이전트를 **능력 확장**으로 구분한다." 확정한 관점에도 이 구분을 유지한다고 명시했다.

## 연결

- [context: fork는 결론만 필요한 작업에 적합하다](./context-fork-suits-conclusion-only-tasks.md) — **두 축이 만나는 지점이다.** `context: fork`는 지식 확장 수단인 스킬을 능력 확장 수단인 서브에이전트로 실행하는 것이므로, 이 구분이 3장에서 하나의 필드로 합쳐진다(합성자 해석).
- [Hooks는 LLM 판단 밖에서 결정론적으로 실행된다](./hooks-run-deterministically-outside-llm-judgment.md) — 같은 분류의 다른 항목이며, 지식·능력과 구분되는 세 번째 성격이다.
- [MCP 권한 와일드카드는 그 서버의 모든 도구를 자동 승인한다](./mcp-wildcard-permissions-auto-approve-every-tool.md) — MCP를 붙일 때 따라오는 권한 조건이다.
- [점진적 공개는 쓰지 않는 지식의 비용을 0으로 만든다](./progressive-disclosure-makes-unused-knowledge-free.md) — 지식 확장 쪽이 비용 없이 성립하는 이유다.
