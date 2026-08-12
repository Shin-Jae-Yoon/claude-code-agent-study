---
title: "플랜 모드는 탐색과 실행을 분리한다"
type: "practice"
status: "growing"
tags: ["workflow", "context-management"]
---

# 플랜 모드는 탐색과 실행을 분리한다

플랜 모드는 읽기 전용 상태에서 구조를 파악하고 방향을 사람과 조정하는 단계다. 여러 파일을 바꾸는 기능, 되돌리기 어려운 아키텍처 결정, 변경 전 코드 조사에 적합하다. 탐색 중 실수로 파일이 바뀌는 일을 구조적으로 막는다.

```bash
claude --permission-mode plan                 # 새 세션에서 플랜 모드로 시작
claude --permission-mode plan -p "..."        # 비대화형
# 세션 중에는 Shift+Tab으로 권한 모드 전환
```

## 근거와 출처

- [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md): 계획 단계의 도구로 정리했다. "플랜 모드는 읽기 전용 상태에서 구조를 탐색하고 사용자와 반복적으로 방향을 조정할 때 사용할 수 있다."
- [2장 홍섭 정리](../../chapters/ch2/hongseob/정리본.md): 작업 단위를 조사하다가 같은 지점에 도달했다. "Claude Code는 plan mode로 **탐색과 실행을 분리**하고 `Explore → Plan → Implement → Commit` 4단계 권장."

## 연결

- [탐색은 범위를 좁혀 가며 앞 단계 결과를 다음 입력으로 넘긴다](./narrow-the-scope-instead-of-asking-everything.md) — 그 탐색 단계를 읽기 전용으로 잠그는 수단이다.
- [한 번에 검증 가능한 최소 변경이 작업 단위다](./atomic-sub-requirement-not-line-count.md) — 단위를 정하는 일 자체를 실행에서 떼어내는 방법이다.
- [context: fork는 결론만 필요한 작업에 적합하다](./context-fork-suits-conclusion-only-tasks.md) — **격리의 두 가지 방식이다.** 플랜 모드는 같은 대화 안에서 쓰기 권한을 잠그고, 포크는 대화 자체를 분리한다. `agent: Plan`은 이 둘이 만나는 지점이다(합성자 해석).
