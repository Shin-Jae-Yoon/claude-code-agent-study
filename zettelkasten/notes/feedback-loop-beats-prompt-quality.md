---
title: "좋은 프롬프트보다 좋은 피드백 루프가 중요하다"
type: "claim"
status: "growing"
tags: ["workflow", "evaluation", "feedback"]
---

# 좋은 프롬프트보다 좋은 피드백 루프가 중요하다

한 번의 지시를 완벽하게 다듬는 것보다, 통과·실패가 명확한 신호를 반복해서 돌려주는 구조를 만드는 편이 결과를 더 개선한다. 여러 번 시도할 수 있기 때문이다. 린터·테스트·빌드 로그 같은 자동 검증 도구는 에이전트에게 코칭 신호로 작동한다.

## 근거와 출처

- [2장 홍섭 정리](../../chapters/ch2/hongseob/정리본.md): 조사 결론으로 이 문장을 그대로 뽑았다 — "핵심 통찰: **좋은 프롬프트보다 좋은 피드백 루프가 더 중요** (여러 번 시도 가능하니까)." ESLint·Prettier·Vitest·SonarQube가 AI에게 코칭 신호가 되고, 스펙 끝에 e2e 검증 단계를 둬서 "동작함"을 증명하는 방식을 들었다. 출처는 CodeScene과 MindStudio의 에이전틱 코딩 문서.
- [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md): 점진적 개발의 세 축 중 두 번째로 같은 것을 두었다. "테스트, 린터, 빌드 로그 같은 피드백 루프를 활용한다. Claude Code는 통과와 실패가 명확한 구조화된 피드백을 받을 때 오류를 교정하기 쉽다."

## 연결

- [스킬은 평가부터 만든다](./eval-first-skill-development.md) — 같은 사고를 스킬 개발에 적용한 형태다. 지침을 다듬기 전에 실패 신호를 먼저 만든다.
- [한 번에 검증 가능한 최소 변경이 작업 단위다](./atomic-sub-requirement-not-line-count.md) — 피드백 루프가 성립하려면 변경 단위가 검증 가능해야 한다는 전제 조건이다.
- [환각 방지에 지침으로 충분한가 검증 장치까지 필요한가](./instructions-lower-probability-verification-is-deterministic.md) — "지침을 잘 쓰는 것보다 검증 구조가 낫다"는 같은 방향의 주장이다(합성자 해석).
- [발동을 봤다고 스킬이 잘 동작하는 것은 아니다](./skill-activation-is-not-evidence-of-quality.md) — 신호가 없으면 개선 여부를 알 수 없다는 점에서 이어진다.
