---
title: "YAML이 깨지면 본문만 빈 메타데이터로 로드된다"
type: "claim"
status: "growing"
tags: ["debugging", "discovery", "invocation"]
---

# YAML이 깨지면 본문만 빈 메타데이터로 로드된다

frontmatter YAML에 구문 오류가 있으면 스킬이 통째로 실패하는 게 아니라, 본문이 **빈 메타데이터로** 로드된다. 그래서 `/skill-name` 직접 호출은 멀쩡히 동작하는데 매칭할 `description`이 없다. 증상이 "직접 부르면 되는데 자동 발동만 안 된다"로 나타나 description 문제로 오진하기 쉽다.

## 근거와 출처

- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): "은근히 고약한 실패 모드다. YAML이 깨져 있으면 Claude Code가 본문은 빈 메타데이터로 로드한다. (…) 증상이 '직접 부르면 되는데 자동 발동만 안 된다'로 나타나 description 문제로 오진하기 쉽다." 진단 순서는 `/skills → /context → /doctor → claude --debug`, 로그는 `~/.claude/debug/<session-id>.txt`.

## 연결

- [발동을 결정하는 것은 name이 아니라 description이다](./description-decides-activation.md) — 이 함정이 오진하게 만드는 대상이 그 메모다.
- [스킬 측정에는 네 개의 축이 있다](./skill-measurement-has-four-axes.md) — "제대로 로드되는가"라는 정합성 축이 왜 따로 필요한지 보여준다.
- [발동을 봤다고 스킬이 잘 동작하는 것은 아니다](./skill-activation-is-not-evidence-of-quality.md) — 관측된 증상과 실제 원인이 어긋나는 같은 계열의 문제다.
- [미정의 설정 key는 거부되지 않고 조용히 무시된다](./undefined-settings-keys-are-silently-ignored.md) — 설정 파일에서 일어나는 같은 성격의 조용한 실패다. 잘못 쓴 것이 에러가 아니라 침묵으로 돌아온다.
- [제한처럼 읽히지만 막지 않는 장치가 반복해서 나타난다](./controls-that-read-as-limits-but-do-not-block.md) — 이 사례가 그 패턴의 한 행이다.

## 열린 질문

- **정리본 간 서술이 다르다.** [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md)는 교재 기준으로 "YAML 파싱 오류 → 스킬 전체가 로드되지 않으므로 구문부터 확인"이라고 적었다. 준호는 공식 디버그 문서를 근거로 "본문은 로드되고 메타데이터만 빈다"고 했다. 후자가 더 최신 근거를 가지지만, 어느 쪽이 현재 동작인지는 직접 재현해봐야 확정된다. 검증 방법은 프론트매터를 일부러 깨뜨린 임시 스킬을 만들어 `/skills` 노출과 직접 호출 가능 여부를 확인하는 것이다.
