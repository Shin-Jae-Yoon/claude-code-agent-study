---
title: "스킬 토큰 비용은 컨텍스트의 15% 이내를 목표로 한다"
type: "practice"
status: "growing"
tags: ["token-cost", "measurement", "context-management"]
---

# 스킬 토큰 비용은 컨텍스트의 15% 이내를 목표로 한다

20만 토큰 윈도우에서 시스템 프롬프트와 대화 히스토리를 빼면 스킬에 실질적으로 할당 가능한 예산은 약 3만~5만 토큰이다. 목표는 스킬 전체 비용을 컨텍스트 윈도우의 15% 이내로 유지하는 것이고, 이 값은 추정식으로 예측하고 `/context`로 실측한다.

## 근거와 출처

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 예산(3만~5만 토큰)과 목표(15%), 그리고 추정식을 제시했다. `1단계 = 스킬 수 × 100` / `2단계 = 동시 활성화 수 × 평균 SKILL.md 토큰` / `3단계 = 로드된 지원 파일 줄 수 × 10`. 자기 시스템에 대입해 1단계 약 900토큰, 3단계 약 1,770토큰을 얻었다.
- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md): 같은 15%를 **어떻게 볼 것인가**로 조사했다. `/context`의 Skills row가 스킬 목록 점유 크기를 보여주고, statusline에 컨텍스트 사용 바를 상시 표시할 수 있다. 15%는 Skills row ÷ 전체 윈도우(모델별 200K~400K)로 비교한다.

한 사람은 예측식을, 다른 사람은 관측 수단을 담당했다는 점이 이 메모의 관찰이다(합성자 해석).

## 연결

- [자동 압축은 스킬을 5,000 / 25,000토큰까지만 되살린다](./compaction-reattachment-budget-limits-skill-persistence.md) — 예산 관리의 또 다른 상한이다.
- [스킬 측정에는 네 개의 축이 있다](./skill-measurement-has-four-axes.md) — 15%는 그중 비용 축에 해당한다.
- [SKILL.md 본문은 세션 내내 남는 상주 비용이다](./skill-body-is-recurring-context-cost.md) — 예산을 실제로 소모하는 주체다.

## 열린 질문

- 15%라는 수치의 출처가 무엇인가. 재윤 정리본은 교재 기준으로 제시했고 공식 근거는 아직 확인되지 않았다. [SKILL.md 분량 기준은 세 사람이 다르게 본다](./skill-md-length-standard-is-contested.md)와 같은 검증 대상일 수 있다.
