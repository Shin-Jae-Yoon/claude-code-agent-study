---
title: "allowed-tools는 제한이 아니라 사전 승인이다"
type: "claim"
status: "evergreen"
tags: ["permissions", "security", "skill-authoring"]
---

# allowed-tools는 제한이 아니라 사전 승인이다

`allowed-tools`는 나열된 도구를 스킬 호출 턴 동안 **승인 없이 쓸 수 있게 해주는** 필드다. 나열되지 않은 도구를 막지 않는다 — 모든 도구는 여전히 호출 가능하고 기존 권한 설정을 따른다. 승인 효과는 호출한 그 턴에만 유효해 다음 메시지에서 해제된다. 실제로 도구를 제거하는 필드는 `disallowed-tools`다.

## 근거와 출처

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 교재 노트가 이 필드를 "위험한 작업을 원천 차단하는 장치"로 서술한 것을 공식문서와 대조해 정정했다. 원문 인용: *"It does not restrict which tools are available: every tool remains callable, and your permission settings still govern tools that are not listed."* 결론은 교재의 `safe-file-reader` 예시(`allowed-tools: Read, Grep, Glob`)가 **이름과 달리 파일 수정을 막지 못한다**는 것이다.
- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): frontmatter 레퍼런스에 처음부터 "호출 턴 동안 승인 없이 쓸 도구. 다음 메시지에 해제"로 정확히 기록했고, 진짜 제한은 `disallowed-tools`("스킬 활성 중 제거할 도구")로 구분했다.

- [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md) — **한 챕터 앞서 이미 맞게 적혀 있었다.** Skill frontmatter 필드를 설명하며 "`allowed-tools`: Skill 실행 중 **사전 승인**할 도구"라고 썼다.

두 사람이 서로 다른 경로(정정 / 원 서술)로 같은 지점에 도달했다는 것이 이 메모의 관찰이다(합성자 해석). 여기에 2장 기록이 더해지면서 시간 순서가 드러난다 — 2장 정리본은 처음부터 "사전 승인"이라 적었고, 3장 교재 노트가 이를 "원천 차단"으로 잘못 서술했으며, 3장 공식문서 대조가 원래 이해로 되돌렸다. 정정이 아니라 **복귀**였던 셈이다.

## 연결

- [스킬은 스스로에게 넓은 도구 권한을 줄 수 있다](./skills-can-grant-themselves-broad-tool-access.md) — 이 필드가 승인이기 때문에 생기는 보안 귀결이다.
- [user-invocable은 자율 실행을 막지 못한다](./user-invocable-does-not-block-autonomous-execution.md) — 이름이 제한처럼 읽히지만 막지 않는다는 같은 패턴이다.
- [제한처럼 읽히지만 막지 않는 장치가 반복해서 나타난다](./controls-that-read-as-limits-but-do-not-block.md) — 이 사례를 포함해 두 챕터에서 최소 다섯 번 반복된 패턴을 묶은 상위 메모다.
- [Read 차단은 Bash 우회를 막지 못한다](./read-deny-does-not-block-bash-bypass.md) — 권한 선언과 실제 차단이 어긋나는 같은 성격의 문제가 2장 권한 설정에도 있었다.

## 열린 질문

- 우리 저장소의 `pre-tell-me-about-claude-code`는 `allowed-tools: WebFetch(domain:code.claude.com) WebSearch`로 도메인까지 좁혀 두었다. 이것이 "공식문서 외 출처를 못 쓰게 막는" 장치가 아니라 "이 도구는 묻지 말고 쓰라"는 장치라면, 원래 의도한 출처 제한은 무엇으로 달성하는가?
