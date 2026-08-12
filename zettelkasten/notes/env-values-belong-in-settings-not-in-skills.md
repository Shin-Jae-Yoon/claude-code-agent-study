---
title: "환경변수 값은 스킬이 아니라 설정에 둔다"
type: "practice"
status: "growing"
tags: ["skill-authoring", "team-convention", "security", "settings"]
---

# 환경변수 값은 스킬이 아니라 설정에 둔다

절차를 스킬로 만드는 것과 값을 스킬에 넣는 것은 다르다. "어떤 env를 읽어 빌드하고 E2E를 실행하는가"는 SKILL.md에 쓰되, env 값 자체는 설정 파일로 분리한다. `settings.json`의 `env` 필드는 모든 세션에 자동 적용되므로 1순위이고, 비밀값과 환경별 오버라이드는 gitignore되는 `settings.local.json`에 둔다. 환경 전환은 이 파일만 교체하면 된다.

## 근거와 출처

- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md): E2E API 테스트를 스킬로 만들 수 있는지 스스로 던진 질문에 대한 결론이다. "스킬화 O. 단 env 값은 스킬에 안 넣는다." 스코프 3단계(User `~/.claude/settings.json` / Project `.claude/settings.json` / Local `.claude/settings.local.json`)와 우선순위 **Local > Project > User**를 확인했고, 필수 env는 `CLAUDE.md`의 "required env vars" 섹션에 문서화하는 패턴을 권했다. 출처는 공식문서 settings.md, best-practices.md.
- [2장 홍섭 정리](../../chapters/ch2/hongseob/정리본.md) — **이 실천의 출발점.** 스프링부트 `.env` 문제를 추적해 `settings.json`의 `env`가 정답임을 확인했다. 공식문서 인용: `env`는 "모든 세션과 클로드 코드가 띄우는 **모든 subprocess**에 환경변수를 주입"한다. 그래서 `gradle bootRun`이 그 OS 환경변수를 가진 채로 돈다. 실전 2안도 비교했다 — **A** `settings.local.json`의 `env`로 값 이관(자동 주입, 단 `.env`와 이중 관리) vs **B** 빌드 명령에서 `set -a; . ./.env; set +a && ./gradlew bootRun`(이중 관리 없음, **추천**). 그리고 B를 "서버 실행해줘"로 자동화하려면 `CLAUDE.md`(팀 공유) 또는 `CLAUDE.local.md`(나만)에 규칙 한 줄을 넣으면 된다.
- [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md): `env`를 기본 설정 후보로 들면서 열린 질문을 남겼다. "셸 환경 변수가 이미 존재할 때와 `settings.json` 값이 충돌하는 경우의 우선순위는 확인이 필요하다."

## 연결

- [.env는 셸도 스프링부트도 자동으로 읽지 않는다](./dotenv-is-not-read-by-shell-or-spring.md) — 이 실천이 나온 진단이다. 누가 `.env`를 읽는지를 먼저 갈라야 값을 어디에 둘지 정할 수 있었다.
- [스킬에는 클로드가 모르는 것만 담는다](./skill-should-contain-only-what-claude-cannot-know.md) — "스킬에 담지 말아야 할 것"의 또 다른 사례다. 앞의 메모가 비용 이유라면 이쪽은 보안·운영 이유다.
- [CLAUDE.md는 항상 로드되고 스킬은 조건부로 로드된다](./claude-md-is-always-loaded-skills-are-conditional.md) — 절차를 어디에 적을지의 선택지다. 홍섭은 `CLAUDE.md` 규칙 한 줄과 슬래시 커맨드를 동등한 대안으로 봤다.
- [스킬은 스스로에게 넓은 도구 권한을 줄 수 있다](./skills-can-grant-themselves-broad-tool-access.md) — 스킬 파일이 저장소를 통해 공유된다는 전제가 두 메모에 공통으로 깔려 있다.
- [Read 차단은 Bash 우회를 막지 못한다](./read-deny-does-not-block-bash-bypass.md) — 값을 분리해 둬도 읽기 경로가 여럿이라는 반대편 문제다.

## 열린 질문

- 스킬 우선순위(`enterprise > personal > project`)와 설정 우선순위(`Local > Project > User`)는 방향이 반대로 보인다. → **2장 합성에서 확인됐다.** 두 체계는 사용자·프로젝트 구간에서 실제로 뒤집힌다: [설정 우선순위와 스킬 우선순위는 사용자·프로젝트 구간에서 뒤집힌다](./settings-hierarchy-inverts-skill-priority.md)
- 셸 환경변수와 `settings.json`의 `env`가 충돌할 때 어느 쪽이 이기는가. 2장 재윤 정리본이 남긴 질문이며 아직 닫히지 않았다.
