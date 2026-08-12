# context: fork로 컨텍스트 격리하기

이 지도는 스킬을 별도 컨텍스트에서 돌리는 선택지를 다룬다. 적합 판단 → 조건 확인 → 남는 비용 → 우리 적용의 순서로 배치했다.

## 적합 판단

- [context: fork는 결론만 필요한 작업에 적합하다](../notes/context-fork-suits-conclusion-only-tasks.md) — 세 정리본이 공유하는 기준
- [스킬은 지식을 확장하고 서브에이전트는 능력을 확장한다](../notes/skill-extends-knowledge-subagent-extends-capability.md) — 2장의 구분에서 보면 이 필드는 두 축이 만나는 지점이다

## 다른 강도의 격리

- [플랜 모드는 탐색과 실행을 분리한다](../notes/plan-mode-separates-exploration-from-execution.md) — 대화를 나누지 않고 쓰기 권한만 잠그는 쪽. 애매하면 여기서 시작한다

## 적합해 보여도 걸리는 조건

- [태스크 없는 스킬을 포크하면 빈손으로 돌아온다](../notes/forked-skill-without-a-task-returns-nothing.md) — 스킬 본문에 실행할 것이 있어야 한다
- [백그라운드 포크의 편집은 되돌릴 수 없다](../notes/background-fork-edits-escape-rewind.md) — 파일을 쓰는 스킬이면 추가로 감수할 위험

## 우리 적용에서 막힌 지점

- [단계 단위 포크가 가능한지 아직 모른다](../notes/context-fork-scope-is-per-skill-not-per-step.md) — 같은 스킬을 두고 두 사람이 반대 판단을 냈다

## 이 지도 밖에서 오는 제약

- [Opus 5에서는 출력 규범은 남기고 절차 지시는 뺀다](../notes/opus5-keep-output-norms-drop-procedure-instructions.md) — "검증 목적 포크"를 반대하는 근거가 여기서 나온다

## 관련 지도

- [점진적 공개와 토큰 비용](./progressive-disclosure-and-token-cost.md) — 포크는 2단계 상주 비용을 회피하는 또 다른 수단이다
- [열려 있는 긴장](./open-tensions.md)
