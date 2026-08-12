---
title: "Read 차단은 Bash 우회를 막지 못한다"
type: "claim"
status: "seed"
tags: ["permissions", "security"]
---

# Read 차단은 Bash 우회를 막지 못한다

`permissions.deny`로 `.env`나 자격 증명 파일의 Read를 막아도, Bash가 허용되어 있으면 `cat .env` 같은 명령이 다른 경로로 같은 내용을 가져올 수 있다. 민감 파일 보호는 파일 읽기 도구만 막고 끝낼 문제가 아니라 명령 실행 경로까지 함께 점검해야 하는 문제다.

## 근거와 출처

- [2장 재윤 정리](../../chapters/ch2/jaeyoon/정리본.md): "Read 차단만으로 Bash를 통한 우회까지 완전히 막을 수 있는지는 별도로 고려해야 한다. 예를 들어 Bash가 허용되면 `cat .env` 같은 명령이 파일 읽기 제한과 다른 경로가 될 수 있다." 이 챕터의 권한·보안 대표 사례를 `.env` 보호로 잡고, 핵심은 "Read 차단만 설정하고 끝내지 않고 Bash 우회 가능성까지 함께 점검하는 것"이라고 정리했다. Bash 규칙의 와일드카드 공백 차이(`Bash(ls *)`는 `lsof`와 매칭하지 않지만 `Bash(ls*)`는 매칭 가능)도 함께 확인했다.

## 연결

- [제한처럼 읽히지만 막지 않는 장치가 반복해서 나타난다](./controls-that-read-as-limits-but-do-not-block.md) — 이 사례가 그 패턴의 한 행이다.
- [allowed-tools는 제한이 아니라 사전 승인이다](./allowed-tools-grants-rather-than-restricts.md) — 도구 단위 선언이 실제 차단과 다르다는 같은 성격의 문제다.
- [환경변수 값은 스킬이 아니라 설정에 둔다](./env-values-belong-in-settings-not-in-skills.md) — 값을 어디에 두든 읽기 경로가 여럿이라는 점에서 함께 봐야 한다.

## 열린 질문

- Bash 우회를 실제로 막으려면 무엇이 필요한가? `Bash(cat *)` 같은 명령 단위 deny를 일일이 쓰는 방식은 우회 명령(`less`, `head`, `od` …)이 무한해 현실적이지 않아 보인다.
