---
title: ".env는 셸도 스프링부트도 자동으로 읽지 않는다"
type: "example"
status: "seed"
tags: ["settings", "example", "debugging"]
---

# .env는 셸도 스프링부트도 자동으로 읽지 않는다

클로드 코드로 스프링부트를 빌드·실행할 때 `.env` 값이 안 들어가던 문제의 원인이 **이중**이었다. 파일명 앞의 `.` 때문이 아니다.

1. **셸 레이어** — 빌드 명령이 도는 셸은 `.env`를 자동 로드하지 않는다. 명시적 `source`/`export`가 필요하다.
2. **스프링 레이어** — 스프링부트도 `.env`를 기본으로 읽지 않는다. `application.yml`, **OS 환경변수**, 시스템 프로퍼티, 실행 인자만 본다(`spring-dotenv` 같은 라이브러리를 넣지 않는 한). IDE에서 되던 건 IDE 실행 구성이 env를 넣어줬기 때문이다.

## 근거와 출처

- [2장 홍섭 정리](../../chapters/ch2/hongseob/정리본.md): 세 줄짜리 실험으로 층을 갈랐다.
  ```
  (a) cat .env         → 읽힘        # . prefix는 문제 아님
  (b) 새 셸에서 echo $FOO → []        # 셸이 .env 자동 로드 안 함
  (c) source .env 후 echo $FOO → bar  # 로드하면 들어감
  ```
  결정적 정정도 함께 남겼다 — `settings.json`의 `env`도 IDE도 **yaml 파일을 수정하지 않는다.** 프로세스의 OS 환경변수로 넣을 뿐이고 스프링이 실행 시점에 그걸 읽어 Environment를 구성한다. 값이 맞게 뜨는 건 세 가지 덕분이다: 프로파일 선택(`SPRING_PROFILES_ACTIVE`), 런타임 오버라이드(OS 환경변수가 yaml보다 우선순위가 높음), placeholder 치환(`${...}`).

## 연결

- [환경변수 값은 스킬이 아니라 설정에 둔다](./env-values-belong-in-settings-not-in-skills.md) — 이 진단이 그 실천의 근거다. 값을 어디에 두느냐를 정하려면 먼저 누가 읽는지를 알아야 했다.
- [Read 차단은 Bash 우회를 막지 못한다](./read-deny-does-not-block-bash-bypass.md) — 같은 `.env` 파일을 다루는 보안 쪽 관점이다. 이쪽은 "왜 안 읽히나", 저쪽은 "왜 못 막나"를 묻는다.
- [미정의 설정 key는 거부되지 않고 조용히 무시된다](./undefined-settings-keys-are-silently-ignored.md) — 둘 다 "설정을 넣었는데 왜 반영이 안 되나"의 서로 다른 원인이다(합성자 해석).
