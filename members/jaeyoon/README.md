# 재윤 (jaeyoon)

각자 제작한 플러그인/스킬을 이 폴더에 넣습니다.

## 도구 목록

2주차에 만든 스킬 3종은 팀 논의를 거쳐 `.claude/skills/`로 승격됨 (모임중 `mid-` / 상시는 접두사 없음):

| 이름 | 종류 | 목적 | 상태 |
|------|------|------|------|
| [mid-zettelkasten-synthesis](../../.claude/skills/mid-zettelkasten-synthesis/SKILL.md) | skill | 챕터별 개인 정리본 → 저장소 전체에 누적되는 원자 메모와 주제 지도 | 승격 (`.claude/skills/`) |
| [mid-study-deep-dive](../../.claude/skills/mid-study-deep-dive/SKILL.md) | skill | 챕터 결과물 → 이해 질문·토론거리·반례·최신 변경점 (실행 시점 웹 조회) | 승격 (`.claude/skills/`) |
| [sync-claude-skills-to-codex](../../.claude/skills/sync-claude-skills-to-codex/SKILL.md) | skill | `.claude/skills` 원본 → Codex 호환 형식으로 변환해 `.codex/skills` 갱신 | 승격 (`.claude/skills/`) |

`sync-claude-skills-to-codex`만 모임 시점과 무관한 상시 도구라 접두사가 없습니다.

## 산출물

| 스킬 | 쌓이는 곳 |
|------|-----------|
| `mid-zettelkasten-synthesis` | [`zettelkasten/`](../../zettelkasten/) — `notes/` · `maps/` · `syntheses/` |
| `mid-study-deep-dive` | `deep-dive/<주제>.md` |
| `sync-claude-skills-to-codex` | [`.codex/skills/`](../../.codex/skills/) |

## 스크립트 도입 기록

`mid-zettelkasten-synthesis`는 **팀에서 처음으로 `scripts/`를 쓰는 스킬**입니다. 3장에서 "결정론적 작업은 문서가 아니라 스크립트로" 원칙에 셋 다 동의했지만 실제 적용은 비어 있었고([우리 팀 스킬에는 아직 스크립트가 없다](../../zettelkasten/notes/team-has-no-skill-scripts-yet.md)), 그때 후보로 지목된 "제텔카스텐 링크 유효성 검증"을 여기에 넣었습니다.

| 스크립트 | 역할 |
|----------|------|
| `scripts/index_notes.py` | 합성 전 기존 메모 인벤토리. `--query`로 중복 후보만 추려 새 메모 생성 전 비교 |
| `scripts/check_links.py` | 합성 후 링크·스키마·고립 검사. 오류가 있으면 종료 코드 1 |
| `scripts/zk.py` | 두 스크립트가 공유하는 파싱 유틸 (단독 실행하지 않음) |

Python 3 표준 라이브러리만 씁니다. SKILL.md는 실행 방법만 담고 코드는 컨텍스트에 올리지 않습니다 — [스크립트는 실행인지 참조인지 명시해야 한다](../../zettelkasten/notes/script-invocation-must-be-explicit.md).
