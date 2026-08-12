---
title: "스킬 이름은 규칙이 아니라 라벨이다"
type: "claim"
status: "growing"
tags: ["naming", "invocation", "skill-authoring"]
---

# 스킬 이름은 규칙이 아니라 라벨이다

frontmatter의 `name`은 목록에 표시되는 라벨이고, 실제 `/` 커맨드 이름은 **디렉터리 이름**에서 나온다(플러그인 스킬은 예외로, 거기서만 `name`이 커맨드의 마지막 세그먼트를 바꾼다). 형식도 강제되지 않는다. 교재가 권한 동명사 형태는 공식 규칙이 아니라 관례이며, 동사형 이름도 규칙 위반이 아니다.

## 근거와 출처

- [3장 홍섭 정리](../../chapters/ch3/hongseob/정리본.md): 공식문서를 직접 확인한 결과 "동명사(gerund) 형태" 규칙은 존재하지 않았다. "공식 예제는 kebab-case일 뿐 형식 강제 없음. 게다가 `name`은 디스플레이 라벨이고, 실제 커맨드명은 디렉토리 이름에서 온다." 결론은 "동명사는 강제가 아니라 관례/가독성 권장이며, 동사형(`commit`, `pr`, `handoff`)도 커맨드 성격엔 오히려 자연스럽다".
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): 같은 사실을 독립적으로 기록했다. "커맨드 이름은 디렉터리명에서 나온다. frontmatter의 `name`은 목록 표시용 라벨일 뿐 호출 이름을 바꾸지 않는다." 플러그인 스킬에서만 예외가 적용된다는 점도 명시했다.
- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 교재는 동명사 형태를 권장한다고 정리했고, 실측에서는 이 저장소 9개 스킬이 모두 명사형(`pre-chapter-prep` 등)임을 확인했다.

## 연결

- [발동을 결정하는 것은 name이 아니라 description이다](./description-decides-activation.md) — `name`의 비중이 낮은 또 다른 이유다.
- [커맨드와 스킬의 남은 차이는 호출 제어뿐이다](./commands-and-skills-differ-only-in-invocation-control.md) — 통합 이후 커맨드 이름이 어디서 오는지에 대한 답을 이 메모가 제공한다.
- [개인 스킬이 프로젝트 스킬을 조용히 덮어쓴다](./personal-skills-silently-override-project-skills.md) — 이름이 곧 디렉터리라면 이름 충돌은 곧 디렉터리 충돌이라는 뜻이다.
