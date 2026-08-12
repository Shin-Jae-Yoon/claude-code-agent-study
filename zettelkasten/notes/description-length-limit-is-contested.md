---
title: "description 길이 기준을 두고 해석이 갈린다"
type: "tension"
status: "growing"
tags: ["discovery", "skill-authoring", "open-question"]
---

# description 길이 기준을 두고 해석이 갈린다

"description은 약 100토큰"이라는 수치를 세 정리본이 다르게 다뤘다. 원칙으로 그대로 채택한 쪽, 비용 추정의 기본 단위로 쓰되 보정한 쪽, 근거 없는 수치로 분류한 쪽이 갈린다. 실제 스펙은 `name` 64자 / `description` 1,024자이고, Claude Code에서는 `description`과 `when_to_use` 합산 1,536자에서 잘린다.

## 근거와 출처

- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md) — **원칙으로 채택.** 토큰 최적화 5원칙의 첫 항목: "description 압축 — 100토큰 예산 안에서 발견 확률 극대화."
- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md) — **추정 단위로 사용 후 보정.** 비용 추정식의 기본 단위로 "스킬당 약 100토큰"(`name` 15~20 + `description` 60~80)을 썼다. 별도로 공식문서를 확인해 "노트의 '스킬당 약 100토큰' 추정은 여전히 유효한 감각이지만, 실제로는 예산제이고 튜닝 가능한 값"이라고 보정했다.
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md) — **근거 없는 수치로 분류.** "자주 도는 잘못된 수치" 표에 넣고 실제 스펙을 제시했다: `name` 64자, `description` 1,024자, Claude Code에서는 `description` + `when_to_use` 합산 1,536자에서 잘림.

## 연결

- [발동을 결정하는 것은 name이 아니라 description이다](./description-decides-activation.md) — 이 필드가 왜 중요한지의 전제다.
- [스킬 목록 예산을 넘으면 description부터 잘려나간다](./skill-listing-budget-truncates-descriptions.md) — 개별 필드 상한과 전체 목록 예산은 다른 층위라는 점이 두 수치를 헷갈리게 만든다(합성자 해석).
- [SKILL.md 분량 기준은 세 사람이 다르게 본다](./skill-md-length-standard-is-contested.md) — 같은 구도가 본문 길이에서도 반복된다.

## 열린 질문

- 셋이 실제로 충돌하는지 확인이 필요하다. "1,024자 상한"과 "실무상 100토큰 정도로 압축하라"는 서로 모순이 아니라 상한과 권장의 차이일 수 있다. 그렇다면 이건 긴장이 아니라 용어 혼동이다.
