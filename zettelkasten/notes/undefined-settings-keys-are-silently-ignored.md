---
title: "미정의 설정 key는 거부되지 않고 조용히 무시된다"
type: "claim"
status: "seed"
tags: ["settings", "debugging"]
---

# 미정의 설정 key는 거부되지 않고 조용히 무시된다

공식문서는 user/project/local 설정을 strict(검증 실패 시 파일 통째 거부)라고 안내하지만, 스펙에 없는 key를 넣는 것은 그 "검증 실패"로 취급되지 않는다. 스키마가 추가 속성을 허용하기 때문에 경고 없이 무시되고 세션은 정상 실행된다. 오타 난 설정 key는 아무 신호 없이 사라진다.

## 근거와 출처

- [2장 홍섭 정리](../../chapters/ch2/hongseob/정리본.md): 유저 설정을 건드리지 않고 별도 파일로 직접 실험했다.
  ```
  claude -p "OK만 답해" --settings '{"홍섭_임의테스트키_xyz":"hello"}'
  → exit 0, "OK" 출력, 경고 없음
  ```
  대응책도 함께 확인했다 — 편집기에서 `$schema`를 넣으면 미정의 key를 편집 단계에서 잡아준다.

## 연결

- [제한처럼 읽히지만 막지 않는 장치가 반복해서 나타난다](./controls-that-read-as-limits-but-do-not-block.md) — 이 사례가 그 패턴의 한 행이다.
- [YAML이 깨지면 본문만 빈 메타데이터로 로드된다](./yaml-error-loads-body-with-empty-metadata.md) — 설정 파일과 프론트매터에서 같은 성격의 조용한 실패가 일어난다. 잘못 쓴 것이 에러가 아니라 침묵으로 돌아온다는 점이 같다(합성자 해석).

## 열린 질문

- 문서의 "strict"가 가리키는 검증 실패는 정확히 무엇인가? 값 타입 오류나 JSON 구문 오류에는 실제로 파일 전체가 거부되는지 확인되지 않았다.
