# ch2 — 워크플로와 설정

> 그 주 챕터 결과물. 개인 정리본(재윤·홍섭)을 4개 고정 렌즈로 종합했다.
> 이번 주 병합 참여: **재윤·홍섭 2인** (준호는 2장 정리본 없음).
> 개인 정리 원문: [재윤](./jaeyoon/정리본.md) · [홍섭](./hongseob/정리본.md)

---

## 참여자별 (원문 보존)

### 재윤 — 탐색→계획→구현→검증 워크플로 + 도구·확장 지형도

- **중심 메시지**: 좋은 결과는 `탐색 → 계획 → 구현 → 검증 → 커밋` 워크플로에서 나온다. 각 단계는 독립 수행하거나 검증 결과에 따라 앞 단계로 되돌아 반복한다.
- **탐색**: 처음부터 "전체 설명" 말고 `Glob/Grep → Read → 실행 흐름 추적`으로 범위를 좁혀 컨텍스트 절약.
- **탐색·계획 보조 세 도구를 지형도로 정리** (2026-08-05 기준 공식 저장소 확인) — 경쟁이 아니라 서로 다른 병목을 푼다고 봄:
  - **Graphify** — 코드+문서+미디어+DB를 하나의 질의 가능한 지식 그래프로. Tree-sitter AST 로컬 파싱, 관계에 근거 수준(`EXTRACTED`/`INFERRED`/`AMBIGUOUS`) 표기. "무엇이 있고 왜 이렇게 연결됐나".
  - **CodeGraph** — 에이전트가 한 번의 질의로 소스·호출 경로·변경 영향(blast radius)을 받는 SQLite 코드 인덱스. Rust 커널, MCP 중심, 파일 watcher 증분 동기화.
  - **Ouroboros** — 코드 검색이 아니라 **명세 우선** 계획 도구. 소크라테스식 질문으로 숨은 가정을 드러내 Ambiguity를 낮춤(≤0.2에서 Seed 허용). "어떻게 만들까"보다 "정확히 무엇을 만들까".
- **계획**: 플랜 모드(`claude --permission-mode plan`, 세션 중 `Shift+Tab`)로 읽기 전용 탐색·방향 조정.
- **구현**: 점진 개발 3축(범위 정의 / 피드백 루프 / 컨텍스트 관리), TDD `Red→Green→Refactor`, `/compact`·`/clear`, worktree 병렬.
- **검토·커밋**: 자동 커밋 메시지를 그대로 쓰지 말고 실제 변경과 대조. `npm run lint:claude`로 AI 검토 자동화.
- **확장 도구 4종을 역할로 구분**: Skill=**지식 확장**, 서브에이전트=**능력 확장**(컨텍스트 격리), MCP=외부 데이터+도구+표준 컨텍스트의 조합, Hooks=생명주기 이벤트의 결정론적 실행, Plugin=이 넷을 묶는 배포 단위.
- **내 시스템 실측 관점**: 이 저장소는 현재 settings 대부분이 비어 있음(`~/.claude/settings.json`=`{}`, 프로젝트 settings·agents·MCP·Hooks 없음). 그래서 각 개념을 "지금 어디에 도입하면 되는지" 위치로 매핑.

### 홍섭 — 워크플로 실측 + 설정·환경변수 실전

- **워크플로 핵심**: `탐색 → 분석 → 심화(+코드 작업)`. 한 번에 다 시키지 않고 **앞 단계 결과를 다음 단계 입력으로** 넘긴다. 실제 사례: ch1 `@경로` vs 풀경로 토큰 실측(10,500 vs 175) → "큰 파일은 풀경로" 결론.
- **settings.json 임의 key 실험(실측)**: `--settings '{"임의키":"..."}'`로 미정의 key를 넣어도 **거부되지 않고 그냥 무시되고 실행**됨(exit 0). 공식문서는 user/project/local을 strict(검증 실패 시 파일 통째 거부)라 하지만, 미정의 key는 그 "검증 실패"로 안 잡힘(스키마가 추가 속성 허용). `$schema`를 넣으면 편집 단계에서 잡아줌.
- **점진 개발 단위 조사**: "몇 줄" 같은 정량 기준보다 **한 번에 검증 가능한 최소 변경(atomic sub-requirement)**. `Explore→Plan→Implement→Commit`. 자동 검증 도구(ESLint·Prettier·Vitest·SonarQube)가 AI에 코칭 신호. 핵심: **"좋은 프롬프트보다 좋은 피드백 루프가 더 중요"**.
- **settings.json 위계(실측)**: 관리자(`managed-settings.json`) > CLI 인자 > 로컬 > 프로젝트 > 사용자. 겹치면 위가 이김. 내 환경엔 사용자 설정만 존재.
- **스프링부트 `.env`가 빌드/실행에서 안 읽히던 문제(정답 도출)**: 원인이 이중 — ① 셸이 `.env`를 자동 로드 안 함(명시적 `source` 필요, 앞의 `.`은 무관), ② 스프링부트도 `.env`를 기본으로 안 읽음(OS 환경변수·`application.yml`만 봄). **정답은 `settings.json`의 `env`** — 모든 subprocess에 OS 환경변수로 주입되어 `gradle bootRun`이 그 값을 갖고 돈다. **중요: yaml 파일을 수정하는 게 아니라** 실행 시점에 스프링이 OS 환경변수를 읽는 것(프로파일 선택 + 런타임 오버라이드 + placeholder 치환).
- **실전 2안 비교**: A) `settings.local.json`의 `env`로 값 이관(자동 주입, 단 `.env`와 이중 관리) vs **B) 빌드 명령에서 `set -a; . ./.env; set +a && ./gradlew bootRun`(이중 관리 없음, 추천)**. `CLAUDE.md`/`CLAUDE.local.md`에 규칙 한 줄 넣어 "서버 실행해줘"만으로 자동화.

---

## 공통 (둘 다 짚은 것)

- **단계형 워크플로 + 앞 단계 → 다음 단계 이월** — 재윤 `탐색→계획→구현→검증→커밋`, 홍섭 `탐색→분석→심화`. 명칭은 달라도 "범위를 좁혀 순차로, 결과를 다음 입력으로"가 공통.
- **점진 개발과 피드백 루프의 중요성** — 재윤은 점진 개발 3축·TDD·구조화된 피드백, 홍섭은 "좋은 프롬프트보다 피드백 루프"·자동 검증 도구를 코칭 신호로. 결론이 같은 방향.
- **`settings.json` 설정 위계/범위** — 관리자·엔터프라이즈 > 프로젝트 > 로컬 > 사용자, 더 구체적·높은 우선순위가 덮어씀. 둘 다 동일 구조로 정리.
- **`settings.json`의 `env` 키로 환경변수 주입** — 재윤은 설정 후보 항목으로, 홍섭은 스프링부트 문제의 정답으로 도달.
- **`CLAUDE.md` / `CLAUDE.local.md` / `~/.claude/CLAUDE.md` 3계층** — 팀 공유 / 개인·프로젝트 / 개인·전역. 둘 다 표로 구분.
- **`.env`·민감값 보호** — 재윤은 `permissions.deny`와 Bash 우회(`cat .env`) 점검, 홍섭은 커밋 금지·gitignore·`settings.local.json`만 사용. 같은 "비밀값 노출 방지" 주제.

## 흥미로운 것 (인상 깊었던 개념·경험)

- **[홍섭] settings 임의 key 실험** — 미정의 key를 넣어도 거부 없이 그냥 무시되고 실행된다는 실측. 문서의 "strict" 표현과 실제 동작 사이 간극을 직접 확인.
- **[홍섭] 스프링부트 `.env` 문제의 이중 원인** — 셸 레이어 + 스프링 레이어를 분리해 진단하고, "yaml 수정이 아니라 OS 환경변수 주입"이라는 지점을 명확히 한 것.
- **[홍섭] `@경로` vs 풀경로 토큰 실측(10,500 vs 175)** — 워크플로 "탐색→분석→심화"를 실제 수치 실험으로 뒷받침.
- **[재윤] 세 도구 지형도** — Graphify/CodeGraph/Ouroboros를 "경쟁 도구"가 아니라 **서로 다른 병목**("무엇을 만들지" vs "시스템이 어떻게 구성됐는지")으로 배치한 프레이밍.
- **[재윤] Ouroboros의 수치화된 종료 조건** — Ambiguity `≤0.2`, 온톨로지 유사도 `≥0.95`, 30세대 hard cap. 단 이는 업계 표준이 아닌 **그 도구의 내부 운영 기준**임을 명시한 태도.
- **[재윤] Skill=지식 확장 / 서브에이전트=능력 확장** 구분 — 확장 도구를 역할 축으로 나눈 정리.

## 갈린 관점 (같은 걸 다르게 봄)

- **워크플로 단계 명명** — 재윤은 교재대로 `계획`·`검증`을 명시적 단계로 둠(플랜 모드·TDD 강조), 홍섭은 실측 경험 축으로 `분석`·`심화`에 압축. 계획/검증을 독립 단계로 세우느냐 vs 분석·심화에 녹이느냐.
- **점진 개발 단위 기준** — 홍섭은 "정량(몇 줄) 기준보다 atomic sub-requirement"로 정량 기준에 다소 회의적, 재윤은 "작은 단위로 나눔"을 3축(범위 정의)으로 절차화. 강조점 차이.
- **`env` 주제를 다루는 깊이** — 홍섭은 실전 실행까지(A settings env 이관 vs B source, 이중관리 트레이드오프, B 추천), 재윤은 "셸 export vs settings.json env"를 개념으로 소개하고 **충돌 시 우선순위는 `확인 필요`로 열어둠**. 같은 주제를 한쪽은 결론까지, 한쪽은 열린 질문으로.

## 팀이 더 팔 것 (미해결·궁금)

- **[홍섭 → 팀 질문]** 다들 얼마나 작은 단위로 작업하나? 정량 기준을 두나? 어떤 자동 검증 수단을 쓰나?
- **[재윤 확인 필요]** 셸 환경변수가 이미 있을 때 `settings.json`의 `env`와 **충돌 시 우선순위**.
- **[재윤 확인 필요]** `think` / `ultrathink` / `/config` / `MAX_THINKING_TOKENS`의 현재 동작과 권장 사용법.
- **[재윤 확인 필요]** 자동 압축(`/compact`)의 예약 토큰 수치.
- **[재윤 확인 필요]** 도구별 기본 승인 여부.
- **[재윤 확인 필요]** 원격 분석의 기본값과 비활성화 방식.

---

### 참고 출처 (정리본에서 모음)

- 공식문서 `code.claude.com/docs/en/settings` (settings 위계·`env`)
- [Graphify](https://github.com/Graphify-Labs/graphify) · [CodeGraph](https://github.com/colbymchenry/codegraph) · [Ouroboros(README.ko)](https://github.com/Q00/ouroboros/blob/main/README.ko.md) · [Serena MCP](https://github.com/oraios/serena)
- [CodeScene — Agentic AI Coding Best Practices](https://codescene.com/blog/agentic-ai-coding-best-practice-patterns-for-speed-with-quality) · [MindStudio — What Is an Agentic Loop](https://www.mindstudio.ai/blog/what-is-an-agentic-loop-ai-coding-agents)

> 각 도구가 제시하는 성능 수치·내부 임계값은 해당 프로젝트 자체 문서 기준이며, 업계 표준이나 모든 저장소에 대한 보장으로 해석하지 않는다.
