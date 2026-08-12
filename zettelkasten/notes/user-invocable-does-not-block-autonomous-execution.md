---
title: "user-invocable은 자율 실행을 막지 못한다"
type: "claim"
status: "seed"
tags: ["invocation", "permissions"]
---

# user-invocable은 자율 실행을 막지 못한다

`user-invocable: false`는 `/` 메뉴 노출만 제어하는 UI 설정이다. 클로드가 스스로 그 스킬을 실행하는 것은 막지 못한다. 자율 실행을 실제로 차단하려면 `disable-model-invocation`을 써야 한다.

## 근거와 출처

- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): "이 필드는 `/` 메뉴 노출만 제어하는 UI 설정이다. Claude의 자율 실행을 막지 못한다. 막으려면 `disable-model-invocation`을 써야 한다." 반대로 `disable-model-invocation`은 스킬 목록에서 아예 빠져 컨텍스트 비용까지 줄인다는 부수 효과도 함께 정리했다.

## 연결

- [커맨드와 스킬의 남은 차이는 호출 제어뿐이다](./commands-and-skills-differ-only-in-invocation-control.md) — 그 호출 제어 필드 중 하나다.
- [allowed-tools는 제한이 아니라 사전 승인이다](./allowed-tools-grants-rather-than-restricts.md) — 이름이 제한처럼 읽히지만 실제로는 막지 않는다는 같은 패턴이다.
- [제한처럼 읽히지만 막지 않는 장치가 반복해서 나타난다](./controls-that-read-as-limits-but-do-not-block.md) — 2장 합성 후 같은 패턴이 최소 다섯 번으로 늘어 상위 메모로 분리했다.
