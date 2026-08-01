# Codex 변환 규칙

## 기본 구조

```text
.codex/skills/<skill-name>/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/, scripts/, assets/  # 실제로 필요한 것만
```

`SKILL.md` YAML frontmatter에는 `name`과 `description`만 둔다. 이름은 원본 폴더 및 `name`과 일치하는 영문 소문자 kebab-case를 사용한다.

## 문법 변환

| Claude Code 원본 | Codex 결과 |
|---|---|
| `argument-hint` | 제거하고 입력 처리 규칙을 본문에 작성 |
| `disable-model-invocation` | 제거. 명시 호출이 필요하면 `agents/openai.yaml`의 `policy.allow_implicit_invocation: false` 사용 |
| `allowed-tools` | 제거하고 필요한 능력과 안전 범위를 본문에 설명 |
| `$ARGUMENTS` | 사용자의 현재 요청이나 명시된 입력으로 표현 |
| `${CLAUDE_PROJECT_DIR}` | 저장소 루트 또는 실제 상대 경로로 표현 |
| `` !`command` `` | 필요할 때 셸 도구로 실행하고 결과를 확인하라는 절차로 변환 |
| `WebFetch`, `WebSearch` | 사용 가능한 웹 도구로 원문을 조회하도록 제품 독립적으로 표현 |
| Claude 전용 에이전트·도구 이름 | Codex에 같은 기능이 확인된 경우만 대응 도구로 변경 |

Codex에 존재하는지 확인하지 못한 도구 이름을 만들어내지 마라. 기능 대응이 불가능하면 제약으로 명시하라.

## 본문 보존 기준

그대로 유지할 내용:

- 도메인 지식과 판단 기준
- 입력·출력 파일 경로
- 순서가 중요한 워크플로
- 결과물 형식과 검증 조건
- Markdown으로 연결된 references

수정할 내용:

- Claude Code UI나 전용 명령을 전제로 한 조작법
- Claude에서만 유효한 권한·도구 선언
- 제품별 모델이나 컨텍스트 동작을 사실처럼 가정한 문장

## 리소스 처리

- `references/`: 대상 `SKILL.md`가 참조하거나 실행에 필요한 파일만 복사한다.
- `scripts/`: Codex 환경에서도 실행 가능하고 실제로 필요한 경우만 복사하고 실행 검증한다.
- `assets/`: 결과 생성에 사용하는 자산만 복사한다.
- `README.md`, 설치 안내, 변경 이력과 개인 메모는 스킬 패키지에 복사하지 않는다.

## `agents/openai.yaml`

최소 형식:

```yaml
interface:
  display_name: "skill-name"
  short_description: "25~64자의 간결한 스킬 설명"
  default_prompt: "Use $skill-name to perform the requested workflow."
```

- 모든 문자열 값은 따옴표로 감싼다.
- `display_name`은 자동완성에서 호출명을 식별할 수 있도록 폴더명 및 `name`과 정확히 같은 영문 slug를 사용한다. 번역하거나 `$`를 붙이지 않는다.
- `default_prompt`에는 반드시 `$skill-name`을 포함한다.
- MCP가 필수일 때만 `dependencies.tools`를 추가한다.
- Claude의 `disable-model-invocation: true` 의미를 유지해야 할 때만 다음을 추가한다.

```yaml
policy:
  allow_implicit_invocation: false
```

## 검증 체크리스트

- `.claude` 원본 파일은 변경되지 않았는가?
- 대상 폴더명과 `name`이 같은가?
- frontmatter에 `name`, `description` 외 필드가 없는가?
- `SKILL.md`의 모든 상대 참조가 실제 파일을 가리키는가?
- Claude 전용 변수와 도구명이 남아 있지 않은가?
- `openai.yaml`의 설명 길이와 기본 프롬프트 형식이 맞는가?
- 기존 Codex 전용 개선 사항을 불필요하게 덮어쓰지 않았는가?
