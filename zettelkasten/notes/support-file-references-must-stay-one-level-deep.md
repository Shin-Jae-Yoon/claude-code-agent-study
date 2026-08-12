---
title: "지원 파일 참조는 한 단계 깊이까지만 유지한다"
type: "practice"
status: "growing"
tags: ["progressive-disclosure", "skill-authoring"]
---

# 지원 파일 참조는 한 단계 깊이까지만 유지한다

SKILL.md가 지원 파일을 가리키는 것까지는 좋지만, 그 지원 파일이 또 다른 파일을 가리키면 안 된다. 중첩 참조가 생기면 클로드가 `head -100` 같은 부분 읽기로 훑고 넘어가 정보가 불완전해진다. 지원 파일은 도메인별로 나누되 깊이는 1단계로 잠근다.

## 근거와 출처

- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): 이유를 가장 구체적으로 댔다. "참조는 SKILL.md에서 한 단계만. 참조 파일이 또 다른 파일을 참조하면 Claude가 `head -100` 같은 부분 읽기로 훑고 넘어가 정보가 불완전해진다." 덧붙여 100줄이 넘는 참조 파일에는 목차를 달아 부분 읽기가 일어나도 전체 범위는 보이게 하라고 했다.
- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 최적화 5전략의 세 번째. 자기 시스템에서 `references/*.md`가 다른 지원 파일을 로드하는 구조가 없음을 실측으로 확인했다.
- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md): 지원 파일 공통 규칙으로 "도메인별 분리, 깊이 1단계까지, 중첩 참조 금지"를 정리했다.

## 연결

- [점진적 공개는 쓰지 않는 지식의 비용을 0으로 만든다](./progressive-disclosure-makes-unused-knowledge-free.md) — 3단계가 실제로 작동하기 위한 조건이다.
- [입출력 예시는 스킬 토큰의 5분의 1에서 절반을 차지한다](./examples-consume-a-fifth-to-half-of-skill-tokens.md) — 예시를 별도 파일로 빼는 것이 이 규칙 안에서 이뤄져야 한다.
