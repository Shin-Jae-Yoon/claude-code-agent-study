---
title: "스킬 측정에는 네 개의 축이 있다"
type: "concept"
status: "growing"
tags: ["measurement", "evaluation", "token-cost"]
---

# 스킬 측정에는 네 개의 축이 있다

스킬이 "잘 되고 있는가"는 하나의 질문이 아니라 네 개다 — **로드**(제대로 읽히는가), **발동**(불려야 할 때 불리는가), **품질**(불렸을 때 결과가 나아지는가), **비용**(얼마를 쓰는가). 각 축은 수단이 다르고 한 축이 통과해도 다른 축은 알 수 없다.

| 축 | 묻는 것 | 수단 |
| --- | --- | --- |
| 로드 | 스킬이 제대로 읽히는가 | `/skills`, `--debug`, YAML 유효성, 경로 규칙 |
| 발동 | 불려야 할 때 불리는가 | OTEL `skill_activated`의 자동/수동 비율, description 튜닝 |
| 품질 | 결과가 실제로 나아지는가 | with/without 벤치마크, 블라인드 A/B |
| 비용 | 얼마를 쓰는가 | `/context` Skills row, statusline, `/doctor` |

## 근거와 출처

네 축의 구분은 합성자의 해석이다. 세 정리본이 각각 한 축씩만 다뤘다는 관찰에서 나왔다.

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md) — **로드 축.** 테스트와 검증 방법을 `description` 구체성, 스킬 디렉터리 경로, YAML 유효성, `claude --debug` 순으로 정리했다. 자기 시스템에서 1·2·3은 통과 상태이고 `--debug`는 아직 돌린 적 없다고 실측했다.
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md) — **발동·품질 축.** `skill-creator`의 eval·벤치마크·블라인드 A/B, 그리고 OTEL `claude_code.skill_activated`의 `invocation_trigger`로 `user-slash`/`claude-proactive`/`nested-skill`을 구분해 "자동 발동 대 수동 호출 비율이 낮으면 description이 안 먹고 있다는 신호"로 읽었다.
- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md) — **비용 축.** `/context`의 Skills row와 statusline 컨텍스트 바로 토큰 점유를 상시 관측하는 방법을 조사했다.

## 연결

- [발동을 봤다고 스킬이 잘 동작하는 것은 아니다](./skill-activation-is-not-evidence-of-quality.md) — 발동 축 통과가 품질 축을 보장하지 않는다는 주장이다.
- [YAML이 깨지면 본문만 빈 메타데이터로 로드된다](./yaml-error-loads-body-with-empty-metadata.md) — 로드 축을 따로 봐야 하는 이유를 보여주는 실패 모드다.
- [스킬 토큰 비용은 컨텍스트의 15% 이내를 목표로 한다](./skill-token-budget-target-15-percent.md) — 비용 축의 목표값이다.
- [스킬은 평가부터 만든다](./eval-first-skill-development.md) — 이 축들을 언제 재기 시작할지에 대한 답이다.

## 열린 질문

- 우리 스킬 9개는 로드 축만 확인된 상태다(재윤 실측). 발동·품질·비용 축은 아무도 재지 않았다. 어느 축부터 도입할 것인가?
