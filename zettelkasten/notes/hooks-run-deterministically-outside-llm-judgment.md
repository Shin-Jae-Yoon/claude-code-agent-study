---
title: "Hooks는 LLM 판단 밖에서 결정론적으로 실행된다"
type: "concept"
status: "seed"
tags: ["hooks", "settings", "evaluation"]
---

# Hooks는 LLM 판단 밖에서 결정론적으로 실행된다

Hooks는 모델이 판단해서 부르는 것이 아니라 생명주기 이벤트에 바인딩되어 무조건 실행되는 명령이다. matcher 패턴으로 특정 도구나 상황에만 반응하게 할 수 있다. "이렇게 해 달라"고 지침으로 부탁하는 것과 성격이 근본적으로 다르다.

## 근거와 출처

- [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md): "Hooks는 LLM의 판단과 별개로 생명주기 이벤트에 바인딩되어 결정론적으로 실행되는 명령이다." 이 챕터에서 다음으로 적용해 볼 설정으로 Hook을 지목했고, 포맷 검사나 위험 명령 감지를 `.claude/settings.json`의 `hooks`에 정의할 수 있다고 봤다.
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): 스킬 프론트매터의 `hooks` 필드를 소개하며 같은 성격을 짚었다. "지침이 아니라 결정론적 강제가 필요할 때." `allowed-tools`나 `hooks`를 쓰는 스킬은 첫 사용 전 사용자 승인이 필요하다는 조건도 함께.

## 연결

- [환각 방지에 지침으로 충분한가 검증 장치까지 필요한가](./instructions-lower-probability-verification-is-deterministic.md) — **"지침은 확률을 낮추고 검증은 결정론적이다"의 구현 수단이 Hooks다.** 3장에서 구조적 검증을 요구한 쪽의 답이 2장에 이미 있었던 셈이다(합성자 해석).
- [스킬은 지식을 확장하고 서브에이전트는 능력을 확장한다](./skill-extends-knowledge-subagent-extends-capability.md) — 확장 도구 분류에서 Hooks가 차지하는 자리다.
- [좋은 프롬프트보다 좋은 피드백 루프가 중요하다](./feedback-loop-beats-prompt-quality.md) — 피드백을 사람이 기억해 돌리는 대신 이벤트에 붙여 자동화하는 형태다.

## 열린 질문

- 재윤이 "다음으로 적용해 볼 설정"으로 Hook을 지목했으나 아직 도입되지 않았다. 우리 저장소에서 결정론적 강제가 필요한 규칙이 무엇인가? 문서 언어(한국어), 개인 폴더 경계 같은 `CLAUDE.md` 규약이 후보로 보인다.
