---
title: "스킬은 스스로에게 넓은 도구 권한을 줄 수 있다"
type: "claim"
status: "growing"
tags: ["security", "permissions", "distribution", "team-convention"]
---

# 스킬은 스스로에게 넓은 도구 권한을 줄 수 있다

프로젝트 스킬의 `allowed-tools`는 워크스페이스 신뢰를 수락한 뒤 유효해진다. 스킬 파일 자체가 자기에게 넓은 도구 권한을 부여할 수 있으므로, 남의 저장소를 신뢰하기 전에 스킬 내용을 읽어봐야 한다. 스킬을 주고받는 행위는 문서를 주고받는 것이 아니라 실행 권한을 주고받는 것에 가깝다.

## 근거와 출처

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 공식문서 인용 — *"Review project skills before trusting a repository, since a skill can grant itself broad tool access."* 스킬을 PR로 주고받는 우리 팀에 직접적인 리뷰 항목이라고 봤다.
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): 같은 경고를 프로젝트 스킬 절에 배치하고, 조직 차원의 대응(Enterprise 스킬 보안 스캐닝)이 Team·Enterprise 플랜 기능임을 밝혔다. "개인 요금제 환경이라 이 경로를 못 쓴다면, 그만큼 리뷰 절차를 사람이 대신해야 한다." 벳팅 체크리스트는 SKILL.md와 참조 마크다운, 번들 스크립트를 전부 읽고 스크립트 동작이 명시된 목적과 일치하는지 확인하는 것이다.

## 연결

- [allowed-tools는 제한이 아니라 사전 승인이다](./allowed-tools-grants-rather-than-restricts.md) — 이 위험이 성립하는 메커니즘이다.
- [스크립트는 출력만큼만 토큰을 쓴다](./scripts-cost-only-their-output.md) — 스크립트는 읽히지 않고 실행되므로, 리뷰하지 않으면 무엇이 실행되는지 아무도 보지 않는다는 뒤집힌 함의가 있다(합성자 해석).
- [nova-workflow는 팀 배포 스킬의 실물 사례다](./nova-workflow-as-team-plugin-distribution.md) — 실제로 스킬을 배포하는 쪽에서 이 검토 책임이 발생한다.
- [MCP 권한 와일드카드는 그 서버의 모든 도구를 자동 승인한다](./mcp-wildcard-permissions-auto-approve-every-tool.md) — **확장을 설치하는 행위가 곧 권한 부여라는 같은 구조다.** 한쪽은 스킬 파일이, 한쪽은 MCP 설정이 통로일 뿐이다.
- [제한처럼 읽히지만 막지 않는 장치가 반복해서 나타난다](./controls-that-read-as-limits-but-do-not-block.md) — 이 위험이 왜 눈에 안 띄는지에 대한 상위 패턴이다.

## 열린 질문

- 우리 팀의 공통 스킬 승격 절차(`members/` → 논의 → `.claude/skills/` → PR)에 권한 검토 항목을 넣을 것인가? 넣는다면 최소 체크리스트는 `allowed-tools`·`hooks`·번들 스크립트 3종인가?
