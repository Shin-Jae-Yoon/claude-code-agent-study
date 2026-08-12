# 준호 (junho)

각자 제작한 플러그인/스킬을 이 폴더에 넣습니다.

## 도구 목록

| 이름 | 종류 | 커맨드 | 목적 | 상태 |
|------|------|--------|------|------|
| [mid-update-claude-code-docs](../../.claude/skills/mid-update-claude-code-docs/SKILL.md) | skill | `/mid-update-claude-code-docs [주차\|날짜]` | 공식 What's New 에서 Claude Code 신규 기능을 수집해 `insight/claude-code-updates/` 에 주차별 한국어 md로 축적 (2026-05-21 이후, 이미 있는 주차는 건너뜀) | 승격 (`.claude/skills/`) |
| [pre-tell-me-about-claude-code](../../.claude/skills/pre-tell-me-about-claude-code/SKILL.md) | skill | `/pre-tell-me-about-claude-code <키워드>` | 키워드를 공식문서 근거로 한국어 설명 (예: `remote control`, `hooks`) | 승격 (`.claude/skills/`) |

두 스킬 모두 `disable-model-invocation: true` — 커맨드를 직접 입력했을 때만 동작하고, 일반 대화 중 자동 발동하지 않습니다.

## 설치

레포 공통 `.claude/skills/` 로 **승격됨** — 이 레포에서 클로드 코드를 열면 팀 전체가 별도 설치 없이 `/mid-update-claude-code-docs`, `/pre-tell-me-about-claude-code` 로 바로 사용합니다. (심볼릭 링크 불필요)

`/` 자동완성에 안 보이면 클로드 코드를 재시작합니다.

## 산출물

- [`insight/claude-code-updates/`](../../insight/claude-code-updates/) — `/mid-update-claude-code-docs` 가 생성·갱신하는 업데이트 기록. 개인 산출물이 아니라 팀이 같이 보는 기록이라, 이 폴더(`members/junho/docs/`)가 아니라 공용 `insight/` 아래에 쌓습니다.
