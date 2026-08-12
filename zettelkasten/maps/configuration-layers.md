# 설정 계층

이 지도는 **무엇을 어디에 적을 것인가**를 묶는다. 같은 규칙도 어느 파일에 두느냐에 따라 적용 범위, 로딩 비용, 우선순위가 달라진다.

## 어느 계층이 이기는가

- [설정 우선순위와 스킬 우선순위는 사용자·프로젝트 구간에서 뒤집힌다](../notes/settings-hierarchy-inverts-skill-priority.md) — 이 지도의 중심. 두 체계를 같은 방향으로 가정하면 팀 규약이 새어나간다
- [개인 스킬이 프로젝트 스킬을 조용히 덮어쓴다](../notes/personal-skills-silently-override-project-skills.md) — 스킬 쪽 절반

## 언제 로드되는가

- [CLAUDE.md는 항상 로드되고 스킬은 조건부로 로드된다](../notes/claude-md-is-always-loaded-skills-are-conditional.md) — 위치 선택이 곧 비용 선택이다

## 값은 어디에 두는가

- [환경변수 값은 스킬이 아니라 설정에 둔다](../notes/env-values-belong-in-settings-not-in-skills.md) — 절차와 값의 분리
- [.env는 셸도 스프링부트도 자동으로 읽지 않는다](../notes/dotenv-is-not-read-by-shell-or-spring.md) — 그 분리가 필요했던 이유의 진단

## 설정이 조용히 실패할 때

- [미정의 설정 key는 거부되지 않고 조용히 무시된다](../notes/undefined-settings-keys-are-silently-ignored.md) — 오타 난 key는 아무 신호 없이 사라진다

## 관련 지도

- [스킬 권한과 배포](./skill-permissions-and-distribution.md) — 권한 규칙도 이 계층 위에 얹힌다
- [탐색과 계획](./exploration-and-planning.md) — 워크플로 규칙을 어디에 적어둘지의 실제 사례
- [열려 있는 긴장](./open-tensions.md) — 우선순위 역전을 팀 규약에 어떻게 반영할지가 미결
