---
title: "MCP 권한 와일드카드는 그 서버의 모든 도구를 자동 승인한다"
type: "claim"
status: "seed"
tags: ["permissions", "security", "mcp"]
---

# MCP 권한 와일드카드는 그 서버의 모든 도구를 자동 승인한다

`mcp__codegraph__*`처럼 서버 단위로 권한을 열면 그 서버가 활성화한 **모든** 도구가 자동 승인된다. 도구 하나를 편하게 쓰려고 연 와일드카드가 서버가 제공하는 나머지 전부에 적용되므로, MCP를 붙일 때는 도구 목록과 권한 범위를 함께 봐야 한다.

## 근거와 출처

- [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md): CodeGraph를 조사하면서 경계와 주의점으로 기록했다. "MCP 권한을 `mcp__codegraph__*`처럼 광범위하게 허용하면 활성화한 모든 CodeGraph 도구가 자동 승인되므로 권한 범위를 함께 검토해야 한다."

## 연결

- [스킬은 스스로에게 넓은 도구 권한을 줄 수 있다](./skills-can-grant-themselves-broad-tool-access.md) — 확장을 설치하는 행위가 곧 권한 부여라는 같은 구조다. 한쪽은 스킬 파일이, 한쪽은 MCP 설정이 그 통로다.
- [제한처럼 읽히지만 막지 않는 장치가 반복해서 나타난다](./controls-that-read-as-limits-but-do-not-block.md) — 반대 방향의 사례다. 그 표의 항목들이 이름보다 좁게 막는다면 이쪽은 이름보다 넓게 허용한다.
- [세 도구는 서로 다른 병목을 푼다](./tools-solve-different-bottlenecks-not-the-same-one.md) — 도입 후보 도구들이 실제로 MCP로 붙는다면 바로 걸리는 조건이다.
