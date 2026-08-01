---
name: sync-claude-skills-to-codex
description: 프로젝트의 `.claude/skills`를 원본으로 삼아 Claude Code 전용 표현을 Codex 호환 형식으로 변환하고 `.codex/skills`에 생성·갱신한다. "Codex 스킬로 옮겨줘", "Claude 스킬 동기화", ".codex에 반영", "sync Claude skills to Codex"라고 하거나 두 도구에서 같은 스터디 스킬을 유지할 때 사용한다. 단순 파일 복사나 전역 `~/.codex/skills` 설치에는 사용하지 않는다.
---

# Sync Claude Skills to Codex

`.claude/skills`를 원본으로 취급하고 저장소 로컬 `.codex/skills`를 파생 산출물로 관리하라. 원본 의미는 유지하되 Codex에서 실행할 수 없는 Claude Code 전용 문법은 그대로 복사하지 마라.

## 범위 결정

- 사용자가 스킬 이름을 지정하면 해당 스킬만 동기화하라.
- 범위를 지정하지 않으면 `.claude/skills/*/SKILL.md`가 있는 모든 스킬을 동기화하라.
- 사용자가 "변경된 스킬만"이라고 명시한 경우에만 Git에서 변경되거나 새로 추가된 스킬로 범위를 줄여라.
- 동기화 시작 전에 Claude 원본과 Codex 대상의 스킬 이름 목록을 비교해 누락과 대상에만 존재하는 스킬을 파악하라.
- `.claude/skills`는 읽기 전용 원본으로 다루고 `.codex/skills`만 생성·수정하라.

## 동기화 절차

1. 대상 Claude 스킬의 `SKILL.md`와 직접 참조하는 `references/`, `scripts/`, `assets/`를 읽어라.
2. 같은 이름의 `.codex/skills/<skill-name>/`이 있으면 먼저 읽고 차이를 비교하라.
3. [Codex 변환 규칙](references/codex-adaptation-rules.md)에 따라 `SKILL.md`를 변환하라.
4. 실제로 참조되는 리소스만 대상 스킬로 복사하라. Claude 스킬의 `README.md`와 사용되지 않는 보조 파일은 복사하지 마라.
5. 대상 스킬마다 `agents/openai.yaml`을 생성하거나 갱신하라.
   - `display_name`: 자동완성에서 호출명을 바로 알 수 있도록 `<skill-name>`과 정확히 같은 영문 slug를 사용하라. 번역하거나 `$`를 붙이지 마라.
   - `short_description`: 25~64자의 간결한 설명을 작성하라.
   - `default_prompt`: `$<skill-name>`을 명시하는 한 문장으로 작성하라.
   - 아이콘, 색상, MCP 의존성은 원본에 명확한 근거가 있을 때만 추가하라.
6. `.codex/skills/README.md`를 원본 스킬 전체 목록과 일치하도록 갱신하라. 부분 동기화일 때는 기존의 다른 스킬 항목을 보존하라.
7. 각 대상 스킬을 Codex `quick_validate.py`로 검증하라. 사용할 수 없으면 frontmatter, 이름, 참조 경로와 `openai.yaml`을 수동 점검하라.
8. `.claude` 원본과 `.codex` 결과의 diff를 검토해 의도하지 않은 의미 변화와 누락된 리소스가 없는지 확인하라.

## 기존 Codex 스킬 처리

- 기존 `.codex` 스킬을 통째로 덮어쓰지 마라.
- 원본에서 파생된 부분은 최신 Claude 의미에 맞춰 갱신하라.
- Codex 전용 도구 지시, 검증 절차와 `agents/openai.yaml`은 원본과 충돌하지 않는 한 보존하라.
- 같은 변경이 양쪽에 서로 다르게 존재하면 자동 병합하지 말고 충돌 내용과 선택지를 보고하라.
- Claude 원본에서 사라진 파일을 Codex에서도 삭제하려면 사용자에게 삭제 범위를 명시적으로 확인하라.
- `.codex`에만 존재하는 스킬은 고아 후보로 보고하되 명시적 요청 없이 삭제하지 마라.

## 완료 보고

다음을 간결하게 보고하라.

- 생성하거나 갱신한 `.codex` 스킬
- Claude 전용 문법을 바꾼 부분
- 보존한 Codex 전용 설정
- 검증 결과
- 자동 변환하지 못한 항목과 이유

동기화가 끝났다는 이유로 변환된 스킬을 실행하지 마라. 커밋도 사용자가 요청한 경우에만 수행하라.
