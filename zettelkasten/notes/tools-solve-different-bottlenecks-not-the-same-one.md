---
title: "세 도구는 서로 다른 병목을 푼다"
type: "example"
status: "seed"
tags: ["workflow", "example", "mcp"]
---

# 세 도구는 서로 다른 병목을 푼다

Graphify·CodeGraph·Ouroboros를 경쟁 도구로 보면 선택 기준이 안 나온다. 각각이 워크플로의 다른 지점에서 막히는 것을 푼다고 봐야 배치가 정해진다.

| 도구 | 푸는 병목 | 성격 |
| --- | --- | --- |
| Ouroboros | 무엇을 만들지가 안 정해짐 | 소크라테스식 질문으로 명세 수렴. 계획 단계 |
| Graphify | 저장소에 무엇이 있고 **왜** 이렇게 연결됐나 | 코드+문서+미디어+DB를 한 지식 그래프로. 사람도 읽는 아키텍처 지도 |
| CodeGraph | 이 심볼을 바꾸면 **무엇이** 영향받나 | SQLite 코드 인덱스. 에이전트가 한 번의 질의로 호출 경로와 blast radius |

## 근거와 출처

- [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md): 2026-08-05 기준 공식 저장소를 확인하고 세 도구를 조사했다. "같은 종류의 경쟁 도구로 보기보다 워크플로의 서로 다른 병목을 해결한다고 보는 편이 정확하다." Graphify는 관계에 근거 수준(`EXTRACTED`/`INFERRED`/`AMBIGUOUS`)을 붙이고, Ouroboros는 Ambiguity `0.2` 이하에서 Seed 생성을 허용하는 등 종료 조건을 수치화한다. 다만 "이 수치는 일반적인 소프트웨어 공학 표준이 아니라 Ouroboros가 채택한 내부 운영 기준"이라고 단서를 달았다. [Serena MCP](https://github.com/oraios/serena)는 LSP 기반 심볼 탐색이라는 또 다른 접근으로 함께 언급했다.

> 각 도구의 성능 수치와 내부 임계값은 해당 프로젝트 자체 문서 기준이며 업계 표준이 아니다.

## 연결

- [탐색은 범위를 좁혀 가며 앞 단계 결과를 다음 입력으로 넘긴다](./narrow-the-scope-instead-of-asking-everything.md) — 이 도구들이 보조하려는 단계다.
- [MCP 권한 와일드카드는 그 서버의 모든 도구를 자동 승인한다](./mcp-wildcard-permissions-auto-approve-every-tool.md) — CodeGraph를 MCP로 붙일 때 바로 걸리는 조건이다.
- [스킬은 지식을 확장하고 서브에이전트는 능력을 확장한다](./skill-extends-knowledge-subagent-extends-capability.md) — 이 도구들이 확장 도구 분류의 어디에 들어가는지의 축이다.

## 열린 질문

- 이 저장소는 Markdown과 발표 산출물 비중이 크므로 재윤은 Graphify가 자연스럽다고 봤다. 실제로 도입해 우리 제텔카스텐과 어떻게 겹치거나 나뉘는지는 확인되지 않았다.
