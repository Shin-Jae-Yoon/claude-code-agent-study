---
title: "SKILL.md 본문은 세션 내내 남는 상주 비용이다"
type: "claim"
status: "growing"
tags: ["progressive-disclosure", "token-cost", "skill-authoring"]
---

# SKILL.md 본문은 세션 내내 남는 상주 비용이다

스킬이 한 번 호출되면 렌더된 본문이 메시지 하나로 대화에 들어가 세션이 끝날 때까지 남는다. 이후 턴에서 파일을 다시 읽지 않는다. 따라서 2단계(본문) 비용은 호출 시점의 일회성 지출이 아니라 **누적 고정비**이며, 본문의 한 줄 한 줄이 반복해서 지불된다.

## 근거와 출처

- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): "한 번 호출되면 렌더된 내용이 메시지 하나로 들어가 세션 끝까지 남는다. (…) 본문 한 줄 한 줄이 반복되는 상주 비용이다." 여기서 500줄 이하 유지와 "일회성 절차가 아니라 상시 지침처럼 써야 한다"는 두 결론을 끌어냈다.
- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 공식문서 원문을 인용해 같은 지점을 확인했다. *"the rendered SKILL.md content enters the conversation as a single message and stays there for the rest of the session"* → "2단계 비용은 일회성이 아니라 누적 고정비로 봐야 한다."

## 연결

- [점진적 공개는 쓰지 않는 지식의 비용을 0으로 만든다](./progressive-disclosure-makes-unused-knowledge-free.md) — 그 주장이 적용되지 않는 층이 여기다.
- [자동 압축은 스킬을 5,000 / 25,000토큰까지만 되살린다](./compaction-reattachment-budget-limits-skill-persistence.md) — 상주가 무조건 유지되지는 않는다는 반대 방향의 제약이다.
- [SKILL.md 분량 기준은 세 사람이 다르게 본다](./skill-md-length-standard-is-contested.md) — 이 비용을 어떤 숫자로 관리할지에서 의견이 갈렸다.
- [스킬에는 클로드가 모르는 것만 담는다](./skill-should-contain-only-what-claude-cannot-know.md) — 상주 비용을 줄이는 가장 직접적인 실천이다.
