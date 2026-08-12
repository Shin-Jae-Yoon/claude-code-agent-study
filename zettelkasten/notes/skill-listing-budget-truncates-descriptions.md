---
title: "스킬 목록 예산을 넘으면 description부터 잘려나간다"
type: "claim"
status: "growing"
tags: ["discovery", "token-cost", "invocation"]
---

# 스킬 목록 예산을 넘으면 description부터 잘려나간다

스킬 목록(1단계 메타데이터)에는 예산이 있다. 기본 리스팅 예산은 모델 컨텍스트 윈도우의 1%이고, 이를 넘으면 덜 쓰는 스킬의 `description`부터 통째로 사라져 이름만 남는다. 스킬 저장소가 커질수록 이것이 현실적인 발동 실패 원인이 된다.

## 근거와 출처

- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): 예산 비율과 잘림 순서를 명시하고 대응 수단을 정리했다. `/doctor`로 리스팅 비용과 주요 기여자 확인, `skillListingBudgetFraction`으로 예산 상향(예: `0.02` = 2%), 저우선순위 스킬은 `skillOverrides`에서 `name-only`로.
- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 같은 조정 수단(`skillListingBudgetFraction`, `SLASH_COMMAND_TOOL_CHAR_BUDGET`, `skillOverrides: name-only`)을 공식문서에서 확인하고, 교재의 "스킬당 약 100토큰" 추정이 "실제로는 예산제이고 튜닝 가능한 값"이라고 보정했다.

## 연결

- [발동을 결정하는 것은 name이 아니라 description이다](./description-decides-activation.md) — 그 description이 사라지는 조건이다.
- [점진적 공개는 쓰지 않는 지식의 비용을 0으로 만든다](./progressive-disclosure-makes-unused-knowledge-free.md) — "비용 0"이 1단계에는 적용되지 않는다는 한계를 보여준다.
- [ECC의 286개 스킬은 점진적 공개의 실증이다](./ecc-286-skills-as-progressive-disclosure-proof.md) — 그 규모에서 이 예산을 어떻게 감당하는지가 검증 대상이다.

## 열린 질문

- ECC 규모(286개 스킬)에서 기본 1% 예산이면 대부분의 description이 잘릴 텐데, 실제로 발동이 어떻게 유지되는가? 두 메모가 정면으로 만나는 지점인데 어느 정리본도 답을 갖고 있지 않다.
