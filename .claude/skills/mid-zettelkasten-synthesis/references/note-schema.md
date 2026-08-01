# 제텔카스텐 문서 스키마

## 원자 메모

파일명은 `short-descriptive-slug.md` 형식의 구체적인 영문 소문자 kebab-case를 사용한다. 파일명이 안정적인 식별자이므로 같은 주장의 기존 파일이 있으면 새 파일을 만들지 말고 갱신한다.

```markdown
---
title: "서브에이전트는 메인 컨텍스트 오염을 줄인다"
type: "claim"
status: "growing"
tags: ["context-management", "subagent"]
---

# 서브에이전트는 메인 컨텍스트 오염을 줄인다

탐색 작업을 서브에이전트에 맡기면 메인 에이전트가 모든 중간 정보를 보유하지 않아도 된다.

## 근거와 출처

- [3장 재윤 정리](../../chapters/ch3/jaeyoon/정리본.md): 탐색 결과만 반환했을 때 메인 컨텍스트 사용량이 줄었다.
- [5장 준호 정리](../../chapters/ch5/junho/정리본.md): 역할 분리 실험에서도 같은 효과를 관찰했다.

## 연결

- [위임에는 명확한 작업 경계가 필요하다](./delegation-requires-clear-boundaries.md) — 이 효과가 성립하기 위한 조건이다.
- [에이전트 분리는 조정 비용을 증가시킨다](./agent-separation-increases-coordination-cost.md) — 컨텍스트 절약과 맞바꾸는 비용이다.

## 열린 질문

- 결과 요약 과정의 정보 손실을 어떤 기준으로 검증할 수 있는가?
```

### 허용 값

- `type`: `concept`, `claim`, `practice`, `question`, `tension`, `example`
- `status`: `seed`, `growing`, `evergreen`
- 관계 표현: `supports`, `contrasts`, `extends`, `requires`, `applies`, `updates`

관계 값은 별도 ID에 저장하지 말고 링크 옆 설명으로 의미를 드러낸다.

## 주제 지도

관련 메모가 3개 이상일 때 `maps/<topic>.md`를 만든다.

```markdown
# 컨텍스트 관리

이 지도는 에이전틱 코딩에서 컨텍스트를 절약하는 방법과 그 비용을 연결한다.

## 절약 방법

- [서브에이전트는 메인 컨텍스트 오염을 줄인다](../notes/subagents-protect-main-context.md)

## 비용과 한계

- [에이전트 분리는 조정 비용을 증가시킨다](../notes/agent-separation-increases-coordination-cost.md)
```

지도에는 원자 메모의 내용을 복사하지 말고 분류 기준과 연결 이유만 적는다.

## 합성 기록

`syntheses/` 문서에는 다음을 기록한다.

- 입력 파일과 작성자
- 반복, 강조, 긴장, 독창 신호
- 생성한 원자 메모
- 갱신한 기존 원자 메모
- 생성·갱신한 지도
- 해결되지 않은 질문과 다음 검증 항목

## 점검

- 제목이 하나의 주장 또는 질문인가?
- 원문 출처와 합성자의 해석을 구분했는가?
- 링크마다 연결 이유가 설명되어 있는가?
- 링크 대상 파일이 실제로 존재하는가?
