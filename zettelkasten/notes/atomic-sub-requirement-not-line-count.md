---
title: "한 번에 검증 가능한 최소 변경이 작업 단위다"
type: "practice"
status: "growing"
tags: ["workflow", "feedback", "measurement"]
---

# 한 번에 검증 가능한 최소 변경이 작업 단위다

"몇 줄 이내로 나눠라" 같은 정량 기준보다, **한 번에 검증 가능한 최소 변경(atomic sub-requirement)** 으로 쪼개는 것이 실질적인 기준이다. 크기가 아니라 검증 가능성이 단위를 정한다.

## 근거와 출처

- [2장 홍섭 정리](../../chapters/ch2/hongseob/정리본.md): 팀에 던질 질문("다들 얼마나 작은 단위로 작업하나? 정량 기준 두나?")을 스스로 조사해 답한 결과다. "'몇 줄' 같은 정량 기준보다 한 번에 검증 가능한 최소 변경(atomic sub-requirement)으로 쪼개는 게 정설." Claude Code는 plan mode로 탐색과 실행을 분리하고 `Explore → Plan → Implement → Commit` 4단계를 권장한다는 점도 함께.
- [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md): 점진적 개발의 첫 축을 "작업 범위를 명확하게 정의한다"로 두고, "복잡한 기능은 독립적으로 테스트 가능한 작은 단위로 나누어 순차적으로 구현한다"고 서술했다.

## 연결

- [분량의 실제 기준은 줄 수가 아니라 토큰이다](./token-count-not-line-count-is-the-real-measure.md) — **같은 형태의 주장이 다른 대상에 적용된 것이다.** 한쪽은 작업 크기, 한쪽은 문서 길이지만 둘 다 "줄 수는 진짜 기준이 아니다"라고 말한다. 3장의 분량 논쟁을 2장의 이 관점으로 다시 보면, 줄 수 대신 무엇을 기준으로 삼을지가 공통 질문이 된다(합성자 해석).
- [좋은 프롬프트보다 좋은 피드백 루프가 중요하다](./feedback-loop-beats-prompt-quality.md) — 검증 가능한 단위여야 피드백 루프가 돈다.
- [플랜 모드는 탐색과 실행을 분리한다](./plan-mode-separates-exploration-from-execution.md) — 단위를 정하는 작업 자체를 실행과 분리하는 수단이다.

## 열린 질문

- 홍섭이 팀에 던진 질문이 아직 답을 못 받았다. 각자 실제로 어느 정도 단위로 작업하고 어떤 자동 검증 수단을 쓰는지.
