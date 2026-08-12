---
title: "발동을 결정하는 것은 name이 아니라 description이다"
type: "claim"
status: "growing"
tags: ["invocation", "discovery", "skill-authoring"]
---

# 발동을 결정하는 것은 name이 아니라 description이다

클로드가 어떤 스킬을 쓸지 고르는 실질적 근거는 `description`이다. 그래서 "무엇을 하는가"와 "언제 쓰는가"를 모두 담고, 트리거가 될 만한 구체적 용어를 포함해야 한다. 수십·수백 개 스킬 중에서 고르는 판단이므로 모호한 설명은 곧 발동 실패다.

## 근거와 출처

- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): "`name`과 `description` 둘 다 트리거 판단에 쓰이지만, 실질적 무게는 `description`에 있다. 100개가 넘는 스킬 중에서 고르는 근거이기 때문이다." 작성 원칙에서 **반드시 3인칭으로 쓸 것**도 함께 — description은 시스템 프롬프트에 주입되므로 "I can help you…" 같은 시점이 섞이면 발견 자체가 망가진다.
- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): "클로드가 요청 분석 시 이 필드를 참조해 활성화 여부를 결정"한다고 정리하고, 이 저장소 9개 스킬이 모두 기능 + 트리거를 담고 있음을 실측했다. `mid-zettelkasten-synthesis`는 트리거 문구를 나열하고 **부정 조건**("단순 문서 요약에는 사용하지 않는다")까지 붙였다.
- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md): `humanize-korean`이 description에 트리거 문구를 잔뜩 넣어 "AI 티 없애줘"라고만 해도 선택된다는 실측 사례를 들었다.

## 연결

- [스킬 목록 예산을 넘으면 description부터 잘려나간다](./skill-listing-budget-truncates-descriptions.md) — 잘 쓴 description도 예산에 걸리면 사라진다는 제약이다.
- [스킬 이름은 규칙이 아니라 라벨이다](./skill-name-is-a-label-not-a-rule.md) — 발동에서 `name`의 비중이 낮은 이유를 뒷받침한다.
- [YAML이 깨지면 본문만 빈 메타데이터로 로드된다](./yaml-error-loads-body-with-empty-metadata.md) — 발동 실패를 description 탓으로 오진하게 만드는 함정이다.
- [description 길이 기준을 두고 해석이 갈린다](./description-length-limit-is-contested.md) — 얼마나 길게 쓸 수 있는지에서 세 사람의 판단이 달랐다.
- [OMC는 트리거를 description에서 분리해 별도 필드로 둔다](./omc-triggers-field-separates-activation-from-description.md) — 같은 문제를 다르게 설계한 사례다.
