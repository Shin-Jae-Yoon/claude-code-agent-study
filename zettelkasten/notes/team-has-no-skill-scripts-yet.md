---
title: "우리 팀 스킬에는 아직 스크립트가 없다"
type: "claim"
status: "seed"
tags: ["team-convention", "skill-authoring", "token-cost"]
---

# 우리 팀 스킬에는 아직 스크립트가 없다

두 사람이 각자 자기 시스템을 실측한 결과, 스킬 안에서 `scripts/`와 `templates/`를 쓰는 사례가 사실상 없다. 세 문서가 모두 "로직은 스크립트로"를 원칙으로 인정했지만 실제 적용은 비어 있는 상태다. 원칙과 실천 사이의 가장 큰 간격이 여기다.

## 근거와 출처

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 이 저장소 `.claude/skills/`의 9개 스킬 실측 결과 "`scripts/`와 `templates/`는 어느 스킬에도 없다. 현재 모든 스킬이 문서형이다." 도입한다면 `sync-claude-skills-to-codex`의 결정론적 변환 절차가 1순위 후보라고 봤다.
- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md): 자기 시스템에서 `scripts/`·`templates/`는 개별 스킬 폴더가 아니라 nova-workflow 플러그인 루트에 있고, 스킬 안에 `scripts/`를 둔 건 `admin-guide-writer` 하나뿐이었다. "내 스킬은 아직 references 위주, script/template 활용은 약함."

## 연결

- [스크립트는 출력만큼만 토큰을 쓴다](./scripts-cost-only-their-output.md) — 적용되지 않고 있는 원칙이 이것이다.
- [스크립트는 실행인지 참조인지 명시해야 한다](./script-invocation-must-be-explicit.md) — 도입할 때 함께 지켜야 할 조건이다.

## 열린 질문

- 첫 스크립트를 어디에 도입할 것인가. 재윤은 `sync-claude-skills-to-codex`를 후보로 지목했다. 공식문서의 `codebase-visualizer` 예제(SKILL.md에는 사용법만, 스크립트 코드는 컨텍스트에 들어가지 않음)가 참고 형태로 제시됐다.
- 왜 원칙에 동의하면서도 아무도 쓰지 않았는가? 문서형 스킬이 만들기 쉬워서인지, 결정론적 작업이 실제로 적어서인지는 확인되지 않았다.
