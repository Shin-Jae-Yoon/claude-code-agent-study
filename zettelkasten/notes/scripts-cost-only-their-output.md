---
title: "스크립트는 출력만큼만 토큰을 쓴다"
type: "practice"
status: "growing"
tags: ["progressive-disclosure", "token-cost", "skill-authoring"]
---

# 스크립트는 출력만큼만 토큰을 쓴다

`scripts/`의 파일은 읽히는 것이 아니라 실행된다. 코드 자체는 컨텍스트에 들어가지 않고 실행 결과만 토큰을 소비한다. LLM이 매번 다르게 할 이유가 없는 결정론적 작업(검증, 변환, 리포트 생성)은 문서가 아니라 스크립트로 내리는 것이 비용 면에서 유리하다.

## 근거와 출처

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 같은 규칙을 문서로 쓸 때와 스크립트로 쓸 때를 토큰으로 대비했다. 검증 규칙을 `reference.md`에 200줄로 기술하면 약 2,000토큰, `validate_schema.py`로 구현하면 실행 결과 100~200토큰.
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): "읽히는 게 아니라 실행된다. 컨텍스트를 전혀 먹지 않고, 출력만 토큰을 소비한다." 경로는 `${CLAUDE_SKILL_DIR}`로 참조해야 설치 위치와 무관하게 깨지지 않는다는 조건도 함께.
- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md): 토큰 최적화 5원칙의 마지막 항목. "반복 로직은 코드로. 실행해 결과만 컨텍스트에 남긴다."

## 연결

- [점진적 공개는 쓰지 않는 지식의 비용을 0으로 만든다](./progressive-disclosure-makes-unused-knowledge-free.md) — 이 실천이 그 원리를 한 단계 더 밀어붙인 형태다.
- [스크립트는 실행인지 참조인지 명시해야 한다](./script-invocation-must-be-explicit.md) — 이 이점이 유지되기 위한 필수 조건이다.
- [자유도는 작업에 맞춰 조절한다](./degrees-of-freedom-should-match-the-task.md) — 스크립트는 자유도를 가장 낮게 잠그는 수단이다.
- [우리 팀 스킬에는 아직 스크립트가 없다](./team-has-no-skill-scripts-yet.md) — 이 실천이 적용되지 않은 공백이다.
