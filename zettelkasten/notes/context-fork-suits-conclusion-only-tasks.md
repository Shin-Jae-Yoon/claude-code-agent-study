---
title: "context: fork는 결론만 필요한 작업에 적합하다"
type: "practice"
status: "growing"
tags: ["context-fork", "subagent", "context-management"]
---

# context: fork는 결론만 필요한 작업에 적합하다

`context: fork`를 쓰면 SKILL.md 본문이 서브에이전트를 구동하는 프롬프트가 되고, 그 서브에이전트는 부모 대화 히스토리에 접근하지 못한 채 결과 요약만 돌려준다. 탐색 과정이 아니라 결론만 필요하고, 필요한 입력을 전부 인자로 넘길 수 있는 작업에 적합하다. 반대로 부모 대화 맥락을 계속 참조해야 하거나 도구 호출 몇 번으로 끝나는 작은 일에는 오히려 손해다.

## 근거와 출처

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 토큰 효과를 수치로 제시했다. 포크 없이 대규모 탐색을 하면 30,000~50,000토큰을 소비하지만, 포크하면 최종 요약 1,000~2,000토큰만 부모로 전달된다. 부적합은 부모 컨텍스트 참조가 필요한 스킬과 소규모 작업.
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): 세 조건이 모두 참일 때 쓰라고 정리했다 — ① 결론만 필요하다 ② 실행할 태스크가 있다 ③ 대화 히스토리가 필요 없다. 쓰면 안 되는 경우로 레퍼런스형 스킬, 되돌릴 여지가 필요한 편집, 넓은 도구셋이 필요한 작업, 다른 스킬과 스택해서 쓰는 스킬, 작은 일, 그리고 **검증 목적**을 들었다. "애매하면 인라인으로 시작하고, '이 스킬 돌리면 컨텍스트가 지저분해진다'는 체감이 오면 `context: fork` 한 줄 추가."
- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md): 적절한 경우를 "HTML 생성·대량 검색·리서치처럼 초점이 좁고 산출물만 필요한 작업", 부적절한 경우를 "메인 대화 맥락을 계속 참조·왕복해야 하는 작업"으로 정리했다.

## 연결

- [태스크 없는 스킬을 포크하면 빈손으로 돌아온다](./forked-skill-without-a-task-returns-nothing.md) — 세 조건 중 ②가 깨졌을 때 벌어지는 일이다.
- [백그라운드 포크의 편집은 되돌릴 수 없다](./background-fork-edits-escape-rewind.md) — 적합해 보여도 편집이 섞이면 따로 감수해야 할 비용이다.
- [단계 단위 포크가 가능한지 아직 모른다](./context-fork-scope-is-per-skill-not-per-step.md) — 이 실천을 우리 스킬에 적용할 때 막힌 지점이다.
- [Opus 5에서는 출력 규범은 남기고 절차 지시는 뺀다](./opus5-keep-output-norms-drop-procedure-instructions.md) — 검증 목적 포크를 반대하는 근거가 여기서 나온다.
- [스킬은 지식을 확장하고 서브에이전트는 능력을 확장한다](./skill-extends-knowledge-subagent-extends-capability.md) — **2장의 구분에서 보면 `context: fork`는 두 축이 만나는 필드다.** 지식 확장 수단인 스킬을 능력 확장 수단인 서브에이전트로 실행하는 것이기 때문이다.
- [플랜 모드는 탐색과 실행을 분리한다](./plan-mode-separates-exploration-from-execution.md) — 격리의 다른 방식이다. 플랜 모드는 같은 대화 안에서 쓰기 권한을 잠그고, 포크는 대화 자체를 분리한다.
