---
title: "설정 우선순위와 스킬 우선순위는 사용자·프로젝트 구간에서 뒤집힌다"
type: "claim"
status: "growing"
tags: ["team-convention", "distribution", "settings", "cross-chapter"]
---

# 설정 우선순위와 스킬 우선순위는 사용자·프로젝트 구간에서 뒤집힌다

두 체계가 같은 방향일 것 같지만 다르다. **설정**은 더 구체적인 쪽이 이겨서 프로젝트가 사용자를 덮어쓴다. **스킬**은 개인이 이겨서 사용자가 프로젝트를 덮어쓴다. 같은 저장소에서 `.claude/settings.json`은 팀 값을 강제하는데 `.claude/skills/`는 팀 스킬을 강제하지 못한다.

| | 우선순위 (높음 → 낮음) | 사용자 vs 프로젝트 |
| --- | --- | --- |
| 설정 | 관리자 > CLI 인자 > 로컬 > **프로젝트 > 사용자** | 프로젝트가 이김 |
| 스킬 | enterprise > **personal > project** | 사용자가 이김 |

## 근거와 출처

- [2장 홍섭 정리](../../chapters/ch2/hongseob/정리본.md): 설정 위계를 5단계 표로 정리했다. 관리자(`managed-settings.json`) > CLI 인자 > 로컬(`.claude/settings.local.json`) > 프로젝트(`.claude/settings.json`) > 사용자(`~/.claude/settings.json`). "겹치면 위(관리자)가 이긴다."
- [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md): 같은 방향을 원칙으로 서술했다. "더 구체적이고 우선순위가 높은 설정이 낮은 설정을 덮어쓴다." 권한 배열은 병합 방식과 `deny` 우선 규칙이 별도로 적용된다는 단서도 달았다.
- 스킬 쪽 순서는 [개인 스킬이 프로젝트 스킬을 조용히 덮어쓴다](./personal-skills-silently-override-project-skills.md)에서 3장 두 정리본이 공식문서로 확인한 것이다.

두 체계를 나란히 놓고 방향이 뒤집힌다는 것은 합성자의 해석이다. 어느 정리본도 두 우선순위를 함께 비교하지 않았다.

## 연결

- [개인 스킬이 프로젝트 스킬을 조용히 덮어쓴다](./personal-skills-silently-override-project-skills.md) — 스킬 쪽 절반이다. 이 메모가 그 발견을 설정 체계와 대조해 확장한다.
- [환경변수 값은 스킬이 아니라 설정에 둔다](./env-values-belong-in-settings-not-in-skills.md) — 절차와 값을 나눠 담을 때 두 그릇의 우선순위가 반대라는 실무 함의가 생긴다.
- [CLAUDE.md는 항상 로드되고 스킬은 조건부로 로드된다](./claude-md-is-always-loaded-skills-are-conditional.md) — 팀 규약을 어디에 두느냐를 정할 때 함께 봐야 할 축이다.

## 열린 질문

- 왜 다른가. 설정은 "환경이 구체적일수록 이긴다", 스킬은 "사람이 고른 것이 이긴다"는 서로 다른 원칙을 따르는 것으로 보이지만 공식 설명은 확인하지 못했다.
- 팀 규약을 강제하고 싶다면 스킬보다 설정·`CLAUDE.md` 쪽이 더 확실한 수단인가?
