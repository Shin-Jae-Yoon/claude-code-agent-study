# ch3 — 에이전트 스킬

> 그 주 챕터 결과물. 개인 정리본(홍섭·재윤·준호)을 4개 고정 렌즈로 종합했다.
> 이번 주 병합 참여: **3인 전원**.
> 개인 정리 원문: [홍섭](./hongseob/정리본.md) · [재윤](./jaeyoon/정리본.md) · [준호](<./junho/Chapter 03. 에이전트 스킬.md>)
> 개인 발표 자료: [홍섭](./hongseob/발표.html) · [재윤](./jaeyoon/발표.html)

---

## 참여자별 (원문 보존)

### 홍섭 — 커맨드/스킬 통합의 실체 + 팀 배포 실사례(nova-workflow)

- **커맨드 vs 스킬 — 통합의 실체 = 호출 방식 통합**(확정): 이제 둘 다 같은 `SKILL.md` 포맷을 쓰고 `/슬래시` 직접 호출과 자연어 자동 발동을 **양쪽 다** 지원한다. 성격은 frontmatter의 `disable-model-invocation` 유무로 갈린다.
- **발표 대비축**: **커맨드(화이트박스 — 사람이 직접 지정·제어) vs 스킬(블랙박스 — 클로드가 자동 선택)**. 좌우 2열로 시각화.
- **실측**: nova-workflow의 `commit`·`pr`·`handoff`는 `disable-model-invocation` + `argument-hint` → 커맨드 성격. `humanize-korean`은 description에 트리거 문구를 잔뜩 넣어 "AI 티 없애줘"만으로 발동 → 스킬 성격.
- **스킬 유형 3종을 전부 실물로 보유**: 로컬(`~/.claude/skills/*` — `humanize-korean`, `commit-push-pr`) / 프로젝트(이 스터디 레포 `.claude/skills/*`) / **팀 배포** — 회사 개발팀에 만들어 제공한 [nova-workflow](https://github.com/mediquitous-dev/nova-workflow) 플러그인, **18개 스킬을 마켓플레이스로 배포**.
- **`name` 동명사 규칙 — 조사 결과 공식 강제 아님**: 공식문서에 "동명사(gerund)" 규칙은 없다. 게다가 `name`은 **디스플레이 라벨**이고 실제 커맨드명은 **디렉토리 이름**에서 온다(플러그인 스킬 제외). 동사형(`commit`, `pr`, `handoff`)도 규칙 위반이 아니며 커맨드 성격엔 오히려 자연스럽다.
- **분량 — 200줄 = SRP로 해석**. 실측: `pre-chapter-prep` 66줄, `nova-api-planner` 68줄 양호. **초과 사례 `humanize-korean` 257줄** — 오케스트레이터라 길어짐, **리팩터 후보로 스스로 지목**.
- **지원 파일 폴더별 역할 정리**: `references/`(자주 안 읽는 상세 지식 → 필요할 때만 로드) / `scripts/`(반복 로직은 코드로, 결과만 컨텍스트에) / `templates/`(산출물 뼈대). 공통 규칙은 도메인별 분리·깊이 1단계·중첩 참조 금지.
- **실측**: `references/` + `evals/` 구조는 마케팅 스킬군(`seo-audit`, `copywriting`)에 있음. **`scripts/`·`templates/`는 개별 SKILL 폴더가 아니라 nova-workflow 플러그인 루트**에 있고, 스킬 안에 `scripts/`를 둔 건 `admin-guide-writer` 하나뿐 → "내 스킬은 references 위주, script/template 활용이 약하다".
- **`context`/`agent`/`background` 3필드 조사로 실체 확인**: `agent` built-in 3옵션(`Explore` 읽기전용·코드탐색 / `Plan` 계획 수립 / `general-purpose` 기본값), 생략 시 `general-purpose`. **적절** = HTML 생성·대량 검색·리서치처럼 초점이 좁고 산출물만 필요한 작업. **부적절** = 메인 대화 맥락을 계속 왕복해야 하는 작업.
- **실측**: 내 SKILL.md frontmatter 키는 `name`, `description`, `metadata`, `disable-model-invocation`, `argument-hint`, `allowed-tools`뿐 — **`context`/`agent`/`background`는 아직 안 씀.** **도입 후보: `pre-chapter-prep`의 3단계 HTML 생성**(이미 "서브에이전트 위임 가능"이라 명시돼 있음).
- **토큰 최적화 5원칙**: ① description 압축(100토큰 예산) ② 범용 지식 빼기(50~70% 절감) ③ 도메인별 분리·깊이 1단계 ④ 예시는 본문 1~2개, 나머지 `EXAMPLES.md`(예시가 토큰의 20~50%) ⑤ 로직은 스크립트로. **실물 대조**: 마케팅 스킬군이 ③·④의 실물, `humanize-korean` 257줄은 본문 비대 → 개선 대상.
- **스스로 던진 질문 → 답 (조사 확정)**
  - **Q1. E2E API 테스트 스킬화 — env 주입 설계**: **스킬화 O, 단 env 값은 스킬에 안 넣는다.** 절차는 `SKILL.md`, 값은 `settings.local.json`. `settings.json`의 **`env` 필드**가 정답이고 모든 세션에 자동 적용되므로 1순위. 스코프 우선순위 **Local > Project > User**. 필수 env는 `CLAUDE.md`에 문서화 + 값은 gitignore되는 local에.
  - **Q2. 토큰 15% 모니터링 — 쉽게 보는 법**: **`/context`의 Skills row**로 스킬 목록 점유 확인, **statusline**에 컨텍스트 바 상시 표시 가능. 15%는 Skills row ÷ 전체 윈도우(200K~400K)로 비교. 참고로 auto-compaction은 스킬당 첫 **5,000토큰** 유지, 재부착 합산 **25,000토큰** 예산.

### 재윤 — 점진적 공개로 비용 없이 지식 늘리기 + 공식문서 대조

- **중심 메시지**: **스킬은 점진적 공개(progressive disclosure)로 비용 없이 지식을 늘린다.** 전제는 "컨텍스트 윈도우는 공용 자산". 지식을 늘리면 컨텍스트를 먹는다는 모순을 푸는 게 점진적 공개이고, 토큰 비용 프레임워크·최적화 5전략·스크립트 우선·`context: fork`는 전부 이 한 문장을 실현하는 수단.
- **3단계 점진적 공개**: 1단계 메타데이터(시작 시 상시, 스킬당 ~100토큰) / 2단계 지침(트리거 시, 2,000토큰 이하 권장) / 3단계 지원 파일(필요시, 사실상 무제한). 핵심은 **접근되기 전까지 컨텍스트를 소비하지 않는다**.
- **토큰 비용 프레임워크**: 20만 윈도우에서 스킬 예산은 **3만~5만 토큰**, 목표는 **전체의 15% 이내**. 추정식 `1단계 = 스킬 수 × 100` / `2단계 = 동시 활성화 수 × 평균 SKILL.md` / `3단계 = 로드된 줄 수 × 10`.
- **추정식에 자기 실측치 대입**: 1단계 = 9개 × 100 ≈ **900토큰**(+ouroboros 플러그인 스킬 30여 개), 2단계 = `pre-chapter-prep` 66줄 ≈ 660토큰, 3단계 = (16+78+83)줄 × 10 ≈ **1,770토큰**.
- **최적화 5전략**: description 토큰 밀도 / 클로드가 아는 지식 제거(50~70% 절감) / 도메인별 분리 + **1단계 깊이 유지** / 예시 세트는 `EXAMPLES.md`로 / **스크립트 우선**(200줄 `reference.md` ≈ 2,000토큰 vs `validate_schema.py` 실행 결과 100~200토큰).
- **실측 요약** (2026-08-12): 개인 스킬 **없음**(디렉터리 자체 없음) / 프로젝트 스킬 **9개**, 31~130줄로 **전부 200줄 이내** / 플러그인 `ouroboros@ouroboros` v0.51.0 활성 / Commands 없음 / `references/` 3개 / **`scripts/`·`templates/`·`context: fork`·`agent`·`model`·Version History·입출력 예시 세트 전부 없음** / 1단계 깊이 유지는 지켜짐 / `claude --debug` 사용 이력 없음. → **1·2단계는 기준을 지키고, 3단계와 격리 실행은 비어 있다.**
- **`context: fork`**: 포크 없이 실행하면 탐색에 30,000~50,000토큰, 포크하면 **결과 요약 1,000~2,000토큰만** 부모 대화로. 부적합은 부모 맥락 참조가 필요한 스킬과 소규모 작업.
- **판단**: `pre-chapter-prep` **전체를 포크로 만들면 역질문 게이트(사람과의 대화)가 불가능해진다** — 부모 맥락이 필수인 스킬. 대신 **`mid-zettelkasten-synthesis`를 도입 대상으로 확정**(저장소 전체 탐색이라 이득이 크고, "원자 메모와 주제 지도를 재구성하라"는 명확한 task가 있어 공식 경고에 안 걸림).
- **공식문서 대조 — 교재와 다른 3가지 ★**
  - **① 우선순위가 반대다.** 교재 `project > user > managed` vs 공식 *"enterprise overrides personal, and personal overrides project"*. → 팀이 `.claude/skills/deploy`를 커밋해도 팀원이 `~/.claude/skills/deploy`를 갖고 있으면 **그 사람 로컬에선 개인 스킬이 이긴다.** 팀 표준이 조용히 무력화될 수 있다.
  - **② `allowed-tools`는 제한이 아니라 사전 승인이다.** 공식 원문: *"It **does not restrict** which tools are available: every tool remains callable."* 진짜 제한은 `disallowed-tools`. 유효 범위도 **호출한 그 턴에만**. → 교재의 `safe-file-reader` 예시(`allowed-tools: Read, Grep, Glob`)는 **파일 수정을 막지 못한다.** 공식 보안 주의도 함께: *"Review project skills before trusting a repository, since a skill can grant itself broad tool access."*
  - **③ 분량 기준**: 교재 200줄(한국어 150줄) vs 공식 **500줄**. 방향은 같고 임계값만 다름 — **노트 기준을 지키면 공식 기준도 자동 만족**이라 보수적으로 유지.
- **덤(노트에 없는 것)**: 스킬 콘텐츠는 한 번 로드되면 **세션 끝까지 남는다** → 2단계는 일회성이 아니라 **누적 고정비**. 재호출 시 동일 내용이면 사본 미첨부(v2.1.202+). description + `when_to_use` 합산 **1,536자**에서 잘림, `skillListingBudgetFraction`으로 조정 가능.
- **외부 레퍼런스 4종**: [anthropics/skills](https://github.com/anthropics/skills)(교재 PDF 예시의 실물) / 공식 `codebase-visualizer`(**SKILL.md엔 사용법만, 스크립트 코드는 컨텍스트에 안 들어감** — 우리가 `scripts/`를 하나도 안 쓰므로 가장 따라 하기 좋은 형태) / [ECC](https://github.com/affaan-m/ecc)(**286 스킬·68 에이전트** — 깔아도 세션이 안 터지는 이유가 정확히 이 장의 주제) / [OMC](https://github.com/Yeachan-Heo/oh-my-claudecode)(프론트매터에 **`triggers` 배열** — 교재가 description에 넣으라던 걸 별도 필드로 분리).
- **교재 예시를 Java + Spring으로 변환**: 리액트 컴포넌트 스킬 → `creating-spring-rest-controllers`, API 문서화 예시 → `@GetMapping`/`@PostMapping`/`@PreAuthorize` 3단 세트. 스킬 구조와 예시 난이도 배치(단순 GET → 본문 있는 POST → 인증 있는 DELETE)는 원문 그대로 유지.

### 준호 — 스킬 운영·배포·측정 레퍼런스

- **한눈에**: 스킬은 폴더다 / **커스텀 커맨드는 스킬로 통합됐다**(`.claude/commands/deploy.md`와 `.claude/skills/deploy/SKILL.md`가 똑같이 `/deploy`를 만든다, 신규는 무조건 스킬로) / 차이는 frontmatter 두 필드 / 점진적 공개가 핵심 설계 / **만드는 것보다 측정이 어렵다.**
- **커맨드 vs 스킬 기능 비교**: `/x` 호출은 양쪽 다 O. 스킬만 되는 것 — 딸린 파일(reference·scripts·templates), 중첩 디렉터리 자동 탐색, `--add-dir` 로드, 플러그인·마켓플레이스 패키징. **이름 충돌 시 스킬이 이긴다.**
- **호출 제어 두 필드**: `disable-model-invocation: true` = 나만 호출(`/deploy`, `/commit`처럼 부작용 있는 것). 부수 효과로 **스킬 목록에서 빠져 컨텍스트 비용도 준다**. `user-invocable: false` = 클로드만 호출(배경 지식용). **주의: `user-invocable`은 `/` 메뉴 노출만 제어하는 UI 설정이라 자율 실행을 못 막는다** — 막으려면 `disable-model-invocation`.
- **발동 판단은 실질적으로 `description`**이고, **스킬이 많아지면 description이 잘린다.** 리스팅 예산은 컨텍스트 윈도우의 **1%**, 넘치면 **덜 쓰는 스킬의 description부터 통째로 사라진다**(이름만 남음). → `/doctor`로 비용 확인, `skillListingBudgetFraction`(예: `0.02`)로 상향, 저우선순위는 `skillOverrides`에서 `name-only`.
- **위치와 우선순위**: enterprise / personal(`~/.claude/skills/`) / project(`.claude/skills/`) / plugin. **충돌 우선순위 enterprise > personal > project**, 이 셋은 번들 스킬도 덮어쓴다. 플러그인은 `plugin-name:skill-name` 네임스페이스라 충돌 없음.
- **프로젝트 스킬 탐색은 두 갈래**: 상위 방향(시작 디렉터리 → 리포 루트의 모든 `.claude/skills/`) / 하위 방향(하위 디렉터리 스킬은 시작 시 안 잡히고 **그 디렉터리 파일을 다룰 때 로드**, 모노레포 패턴). 겹치면 `/apps/web:deploy`처럼 경로 한정 이름.
- **⚠️ Cowork·클라우드 세션은 로컬 `~/.claude/skills/`를 읽지 않는다.** claude.ai 계정 활성화 스킬을 세션 시작 시 동기화받고, 클라우드 세션만 추가로 클론한 리포의 `.claude/skills/`를 읽는다. **개인 스킬만 만들어두면 웹·Cowork에선 "스킬을 찾을 수 없다"가 된다.**
- **SKILL.md 상주 비용**: 한 번 호출되면 렌더된 내용이 메시지 하나로 들어가 **세션 끝까지 남고 이후 턴에 다시 읽지 않는다.** → 본문 한 줄 한 줄이 **반복되는 상주 비용**, 500줄 이하 유지. 작업 내내 적용될 내용은 일회성 절차가 아니라 **상시 지침**처럼 쓴다.
- **참조 파일 규칙**: 참조는 **SKILL.md에서 한 단계만**(참조가 또 참조하면 `head -100` 식 부분 읽기로 정보가 불완전해진다). **100줄 넘는 참조 파일엔 목차**를 단다.
- **`scripts/`는 읽히는 게 아니라 실행된다** — 컨텍스트를 전혀 안 먹고 출력만 토큰을 쓴다. 경로는 `${CLAUDE_SKILL_DIR}`로. **실행인지 참조인지 반드시 명시할 것** — "실행하라"와 "알고리즘은 이 파일을 보라"는 다르고, 애매하면 클로드가 통째로 읽어버려 토큰 이점이 사라진다.
- **작성 원칙 8가지**: 간결함 최우선("클로드는 이미 매우 똑똑하다"가 기본 가정) / description은 "무엇을 + 언제" + **반드시 3인칭**(시스템 프롬프트에 주입되므로 "I can help you..."는 발견 자체를 망친다) / 도메인별 분리 / **자유도(degrees of freedom)를 작업에 맞춘다** / 입출력 예시는 조건부 / 결정론적 연산은 스크립트로 / **평가부터 만든다** / 체크리스트(시간 종속 정보 배제, 용어 일관성, 검증 루프, Haiku·Sonnet·Opus 전부 테스트, 선택지 남발 금지).
- **자유도 3단계**: 높음 = 서술형 지침(코드 리뷰) / 중간 = 파라미터 있는 템플릿 / 낮음 = 정확한 스크립트, 플래그 추가 금지(DB 마이그레이션). **비유 — 양옆이 절벽인 좁은 다리에선 가드레일, 탁 트인 들판에선 방향만.**
- **자주 도는 잘못된 수치 ★**: "SKILL.md 200줄(한국어 150줄)" → 공식 기준은 **500줄**. "description 100토큰 제한" → 실제는 `name` 64자, `description` 1,024자, Claude Code에선 `description` + `when_to_use` 합산 **1,536자**. 덧붙여 **"500줄은 상한이지 목표가 아니고, 실제 기준은 줄 수가 아니라 토큰"** — 사내 가이드에 숫자를 못박으면 "150줄 안에 넣었으니 됐다"가 되면서 정작 중요한 판단(이 문단이 토큰값을 하는가)이 생략된다.
- **출력 신뢰성(환각 방지)**: 지침 계열 3가지 — 불확실성 표현 허용(단 "확실하지 않으면 말하지 마라"가 아니라 **"확실하지 않은 부분은 그렇다고 표시하고 말하라"**), 참조 범위 명시 + 컨텍스트 출처와 일반 지식 구분, **출처 명시 + 사후 철회**(생성 후 인용구를 못 찾으면 그 주장을 철회하는 루프까지, 출처만 요구하면 출처를 지어내는 실패 모드가 남는다). 구조 계열 — **plan-validate-execute**(분석 → `changes.json` → 스크립트 검증 → 실행), 도구·패키지 실재 확인(MCP는 항상 `ServerName:tool_name`).
- **Opus 5에서 달라진 것 — 두 방향이 반대다 ★**: ① **불확실성 지침의 우선순위는 올라갔다** — 시스템 카드가 "확신 없는 답을 자신 있게 말한 사례가 놀랄 만큼 많이 발견됨", 사실 주장 환각은 Opus 4.8보다 약간 더 많음. ② **검증 지시는 빼야 한다** — 공식 프롬프팅 가이드가 "최종 검증 단계를 포함하라", "서브에이전트로 검증하라", "다시 확인하라"를 **제거하라**고 명시. 과잉 검증으로 토큰만 낭비되고 품질은 개선되지 않는다. **유지 = 출력 규범, 제거 = 절차 지시.** 그 밖에 문구를 문자 그대로 따르는 경향↑, 응답 길어짐(effort는 사고량이지 발화량이 아님), 범위 확장 경향, 서브에이전트 위임 적극.
- **`context: fork` 함정 두 가지**: **백그라운드 포크는 좁은 도구 집합으로 돈다**(밖의 도구가 필요하면 `background: false`), **백그라운드 포크의 편집은 체크포인트 바깥이라 `/rewind`로 못 되돌린다**(git으로만 복구). `agent: Explore`/`Plan`은 **CLAUDE.md와 git status를 건너뛰므로** 꼭 필요한 지침은 스킬 본문에 다시 써야 한다. 쓰면 안 되는 경우에 **"검증 목적 — Opus 5 가이드가 명시적으로 반대"** 포함.
- **문제 해결 순서 `/skills → /context → /doctor → claude --debug`**. **`--debug`가 잡는 고약한 실패 모드 ★**: frontmatter YAML이 깨지면 Claude Code가 **본문을 빈 메타데이터로 로드**한다 → `/skill-name`은 멀쩡히 되는데 매칭할 description이 없다 → 증상이 **"직접 부르면 되는데 자동 발동만 안 된다"**로 나타나 description 문제로 **오진하기 쉽다**.
- **잘 안 알려진 필드**: `paths`(glob으로 자동 활성화 제한 — description을 아무리 다듬어도 오발동하는 스킬은 이걸로), `metadata`(자체 툴링용 자유 맵 — 소유 부서·리뷰 일자를 박고 스크립트로 인덱싱), `disallowed-tools`, `when_to_use`, `hooks`, settings의 `skillOverrides`(`on`/`name-only`/`user-invocable-only`/`off`).
- **skill-creator — 만들었으면 측정하자**: **발동하는 걸 봤다고 잘 동작하는 게 아니다.** 발동률과 출력 품질은 따로 재야 하고 둘 다 **스킬을 끈 상태와의 비교로만** 알 수 있다. Create/Eval/Improve/Benchmark 4모드, `evals/evals.json`, 케이스마다 독립 서브에이전트 병렬, with/without 벤치마크, 블라인드 A/B, description 튜닝. **Anthropic이 자체 시험했을 때 공개 스킬 6개 중 5개에서 트리거가 개선됐다.**
- **관측**: OTEL `claude_code.skill_activated`의 `invocation_trigger`로 `user-slash`/`claude-proactive`/`nested-skill` 구분 → **자동 발동 대 수동 호출 비율이 낮으면 description이 안 먹고 있다는 신호**, 안 잡히는 스킬은 폐기 후보.
- **팀 배포 — frontmatter 호환성 ★**: Claude Code 밖(claude.ai 업로드, Skills API, `package_skill.py`)에서는 `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` **6개만** 쓸 수 있고, **스펙 밖 필드가 있으면 무시가 아니라 하드 에러로 실패한다.** → 웹·Cowork까지 커버할 공용 스킬은 6개 필드로만 쓰고, 호출 제어가 필요한 건 Claude Code 전용 세트로 분리.
- **조직 기능은 Team·Enterprise 플랜 필요**(전사 프로비저닝, 보안 스캐닝). **개인 요금제라 이 경로를 못 쓰면 리뷰 절차를 사람이 대신해야 한다** — SKILL.md·참조 마크다운·번들 스크립트를 전부 읽고 스크립트 동작이 명시된 목적과 일치하는지 확인.
- **최근 변화**: `context: fork` 백그라운드 기본(v2.1.218), 스킬 스태킹(첫 스킬 + 최대 5개, v2.1.199), 재호출 시 동일 내용 재적재 안 함(v2.1.202), 새 번들 스킬 `/run`·`/verify`·`/run-skill-generator`(테스트로 도망가지 않고 **앱을 실제로 띄워** 확인, 레시피를 `.claude/skills/run-<name>/`에 커밋).

---

## 공통 (셋 다 짚은 것)

- **커맨드와 스킬은 이미 통합됐고, 남은 차이는 "누가 호출하느냐" 하나다.** 셋 다 `disable-model-invocation`을 성격 구분자로 지목했다. 홍섭은 "통합의 실체 = 호출 방식 통합"으로 정의, 준호는 두 필드(`disable-model-invocation`/`user-invocable`)로 표를 만들었고, 재윤은 이 저장소 스킬 2개가 이미 그 필드로 커맨드처럼 쓰이고 있음을 실측했다.
- **점진적 공개 3단계 — 읽히지 않은 파일은 토큰을 0 쓴다.** 재윤은 이걸 중심 메시지로 세웠고(1단계 메타데이터 / 2단계 지침 / 3단계 지원 파일), 준호는 L1/L2/L3 표로, 홍섭은 "references는 필요할 때만 로드 → 평소 토큰 절약"으로 같은 이야기에 도달했다.
- **컴팩션 재부착 예산 — 스킬당 앞 5,000토큰, 합산 25,000토큰.** 세 정리본에 같은 수치가 독립적으로 등장한다. 준호는 "스킬이 중간부터 안 듣는다"는 체감의 상당 부분이 이것이라 해석했고, 홍섭은 15% 모니터링의 참고값으로, 재윤은 "2단계 비용은 누적 고정비"의 근거로 썼다.
- **스크립트 우선 — 로직은 코드로 내리고 결과만 컨텍스트에 남긴다.** 재윤은 토큰으로(200줄 `reference.md` ≈ 2,000토큰 vs 실행 결과 100~200토큰), 홍섭은 5원칙의 ⑤로, 준호는 "읽히는 게 아니라 실행된다 + 실행인지 참조인지 명시하라"는 함정까지 짚었다.
- **지원 파일은 도메인별로 나누되 깊이는 1단계까지, 중첩 참조 금지.** 셋 다 동일. 준호가 이유를 가장 구체적으로 댔다 — 참조가 또 참조하면 `head -100` 식 부분 읽기로 정보가 불완전해진다.
- **`context: fork`와 `agent` 3옵션(`Explore`/`Plan`/`general-purpose`, 생략 시 `general-purpose`)**, 그리고 **적합/부적합을 나눠야 한다**는 것. 셋 다 "결론만 필요한 좁은 작업엔 적합, 부모 대화 맥락이 필요하면 부적합"으로 같은 선을 그었다.
- **`description`이 발동을 결정한다 — "무엇을 + 언제"를 트리거 문구까지 담아 쓴다.** 셋 다 최우선 필드로 꼽았다.

## 흥미로운 것 (인상 깊었던 개념·경험)

- **[홍섭] nova-workflow — 교재의 "팀 배포 스킬"을 실물로 갖고 있다.** 회사 개발팀에 18개 스킬을 마켓플레이스로 배포한 사례. 셋 중 유일하게 **팀 배포 경로를 실제로 운영해 본** 축이다.
- **[홍섭] 자기 스킬을 기준에 대보고 초과를 인정한 것** — `humanize-korean` 257줄을 "오케스트레이터라 길어짐, 리팩터 후보"로 스스로 지목. 실측이 자기 비판으로 이어진 드문 경우.
- **[홍섭] `name`은 디스플레이 라벨이고 실제 커맨드명은 디렉토리 이름에서 온다** — 동명사 규칙을 확인하러 갔다가 그보다 더 중요한 사실을 발견. 이름 규칙 논쟁의 전제 자체가 바뀐다.
- **[재윤] ECC의 286개 스킬** — "스킬 286개를 깔아도 세션이 안 터지는 이유가 정확히 이 장의 주제"라는 프레이밍. 중심 메시지를 외부 사례로 직접 증명했다.
- **[재윤] OMC의 `triggers` 배열** — 교재가 "고유 트리거 용어를 `description`에 넣어라"라고 한 걸 **별도 필드로 분리한** 설계. 같은 문제의 다른 해법.
- **[재윤·준호 교차 확인] `allowed-tools`는 제한이 아니라 사전 승인이다.** 재윤은 교재의 "원천 차단" 서술이 틀렸다고 정정했고, 준호는 처음부터 "호출 턴 동안 승인 없이 쓸 도구, 다음 메시지에 해제"로 정확히 적었다. 두 사람이 독립적으로 같은 지점에 도달했고, **보안 경고**("스킬이 스스로에게 넓은 도구 권한을 줄 수 있으니 남의 리포를 신뢰하기 전에 내용을 봐라")도 양쪽에 있다.
- **[재윤·준호 교차 확인] 스킬 우선순위는 `enterprise > personal > project`** — 교재의 `project > user > managed`와 **반대**. 재윤이 실무 위험(팀이 커밋한 스킬을 팀원의 개인 스킬이 덮어써 팀 표준이 조용히 무력화됨)까지 짚었다.
- **[준호] YAML이 깨지면 본문을 빈 메타데이터로 로드한다** — 증상이 "직접 부르면 되는데 자동 발동만 안 된다"로 나타나 description 문제로 **오진하기 쉬운** 실패 모드. 진단 경로를 모르면 영원히 못 찾을 종류.
- **[준호] Cowork·클라우드 세션은 로컬 `~/.claude/skills/`를 읽지 않는다** — 개인 스킬만 만들어두면 웹에선 존재하지 않는다. 배포 표면을 처음부터 전제해야 한다는 지적.
- **[준호] 리스팅 예산 초과 시 덜 쓰는 스킬의 description부터 통째로 사라진다**(이름만 남음). 스킬 저장소가 커질수록 현실적인 발동 실패 원인.
- **[준호] "만들었으면 측정하자"** — 발동하는 걸 봤다고 잘 동작하는 게 아니고, 발동률과 출력 품질은 **스킬을 끈 상태와의 비교로만** 알 수 있다. Anthropic 자체 시험에서 공개 스킬 6개 중 5개 트리거가 개선됐다는 사례.
- **[준호] Opus 5에서 방향이 갈린 두 변화** — 불확실성 지침은 **더 필요해졌고**, 검증 지시는 **빼야 한다**. "유지 = 출력 규범 / 제거 = 절차 지시"라는 분리 기준.
- **[준호] 자유도(degrees of freedom)** — "양옆이 절벽인 좁은 다리에선 정확한 가드레일, 탁 트인 들판에선 방향만 주고 맡긴다." 스킬을 얼마나 촘촘히 쓸지의 기준.

## 갈린 관점 (같은 걸 다르게 봄)

- **200줄 기준을 어떻게 대할 것인가 — 셋이 전부 다르다.**
  - **홍섭**: 200줄 = **SRP의 실무 기준으로 채택**. 자기 스킬을 실제로 재서 66·68줄은 양호, 257줄은 리팩터 후보로 분류했다.
  - **재윤**: 공식이 500줄임을 **확인하고도 교재 기준(200/150줄)을 유지**. 근거는 "노트 쪽이 더 보수적이므로 노트 기준을 지키면 공식 기준도 자동으로 만족한다".
  - **준호**: 200줄을 **"커뮤니티에서 도는 공식 근거 없는 수치"로 분류**하고, 한 발 더 나가 **정량 기준 자체를 경계**한다 — "실제 기준은 줄 수가 아니라 토큰이다. 사내 가이드에 숫자를 못박으면 '150줄 안에 넣었으니 됐다'가 되면서 정작 중요한 판단이 생략된다."
  - → 같은 숫자를 **실무 기준 / 보수적 안전선 / 잘못된 수치**로 셋이 다르게 처리했다. 팀 규약을 쓸 때 정면으로 부딪히는 지점.
- **"description 100토큰"도 같은 구도로 갈렸다.**
  - **홍섭**: 5원칙 ①로 그대로 채택("100토큰 예산 안에서 발견 확률 극대화").
  - **재윤**: 비용 추정식의 **기본 단위로 사용**하되, 별도로 "실제로는 예산제이고 튜닝 가능한 값"이라 보정.
  - **준호**: **근거 없는 수치로 분류** — 실제는 `name` 64자, `description` 1,024자, Claude Code에선 `description` + `when_to_use` 합산 1,536자 캡.
  - → 수치의 성격(감각적 추정치냐, 실제 스펙이냐)에 대한 판단이 다르다.
- **`pre-chapter-prep`에 `context: fork`를 붙일 것인가 — 정반대 판단.**
  - **홍섭**: **첫 적용 지점으로 지목.** 이미 3단계 HTML 생성을 "서브에이전트 위임 가능"이라 명시하고 있으니 `context: fork` + `agent: general-purpose`를 붙이자.
  - **재윤**: **부적합으로 판정.** 이 스킬 전체를 포크로 만들면 **1→2단계의 역질문 게이트(사람과의 대화)가 불가능해진다.** 대신 `mid-zettelkasten-synthesis`를 도입 대상으로 확정.
  - → 층위가 다르다(홍섭은 3단계 HTML 생성만, 재윤은 스킬 전체). `context`는 스킬 단위 필드라 **"일부 단계만 포크"가 가능한지**부터 정리해야 결론이 난다. 준호의 기준을 대면 "지침만 있고 task가 없으면 빈손으로 돌아온다", "다른 스킬과 스택해서 쓰는 스킬은 포크에서 확장이 끊긴다"가 추가 판단 재료다.
- **스킬 품질을 무엇으로 측정하나 — 축이 다르다.**
  - **홍섭**: **비용 축**. `/context`의 Skills row와 statusline으로 토큰 점유를 보고 15% 목표와 비교.
  - **준호**: **효과 축**. skill-creator의 eval·벤치마크·블라인드 A/B로 **발동률과 출력 품질**을 재고, OTEL `skill_activated`로 자동/수동 발동 비율을 본다.
  - **재윤**: **정합성 축**. `description` 구체성, 경로 규칙, YAML 유효성, `--debug` — "제대로 로드되는가"까지.
  - → 셋을 합치면 로드 → 발동 → 품질 → 비용의 전 구간이 되지만, 지금은 각자 한 축씩만 보고 있다.
- **환각 방지를 다루는 결이 다르다.** 재윤은 스킬 본문에 넣을 **지침 3종**(불확실성 허용 / 정보 출처 제한 / 출처 명시)으로 정리했고, 준호는 같은 3종에 **"출처만 요구하면 출처 자체를 지어내는 실패 모드가 남는다"**는 반례와 **구조 계열**(plan-validate-execute — 지침은 확률을 낮추지만 검증은 결정론적이다)을 덧붙였다. 지침으로 충분한가, 검증 장치까지 필요한가의 차이.

## 팀이 더 팔 것 (미해결·궁금)

- **[홍섭 ↔ 재윤 충돌] `context: fork` 도입 대상.** `pre-chapter-prep`의 HTML 단계에 붙일 것인가(홍섭), 스킬 전체는 부적합하니 `mid-zettelkasten-synthesis`로 갈 것인가(재윤). **`context`가 스킬 단위 필드인 이상 "3단계만 포크"가 성립하는지**부터 확인해야 한다.
- **[팀 규약] SKILL.md 분량 기준을 200/500/"숫자 안 씀" 중 무엇으로 정할 것인가.** 준호의 "숫자를 못박으면 판단이 생략된다"는 경고를 규약에 어떻게 반영할지.
- **[팀 규약] 스킬 PR 리뷰 체크리스트.** 재윤 §5-②와 준호 §3이 같은 경고를 한다 — 스킬은 스스로에게 넓은 도구 권한을 줄 수 있다. 우리는 스킬을 PR로 주고받으므로 **`allowed-tools`·번들 스크립트 확인을 승격 절차에 넣을지** 결정 필요. 준호 말대로 개인 요금제라 조직 보안 스캐닝을 못 쓰면 **사람이 대신해야 한다.**
- **[준호 → 팀] 우리 공통 스킬 9개는 웹·Cowork에서 동작하나?** 프로젝트 스킬이라 클라우드 세션은 커버되지만, Cowork는 claude.ai 계정 스킬만 읽는다. 또 **claude.ai 배포 시 스펙 밖 필드는 하드 에러**인데, 우리 스킬이 쓰는 Claude Code 전용 필드가 무엇인지 점검 필요.
- **[재윤 → 팀] 개인 스킬이 프로젝트 스킬을 덮어쓴다.** 앞으로 각자 `~/.claude/skills/`를 만들 때 `pre-`/`mid-` 접두사와 겹치는 이름을 쓰면 **팀 스킬이 조용히 무시된다.** 네이밍 규약이 필요한지.
- **[재윤 확인 필요] 교재 노트 내부 불일치 2건** — 동적 로딩 구조도의 "2단계/3단계" 표기가 1.6절 표와 어긋남(1.6 기준으론 `reference/`·`templates/`·`scripts/` 모두 3단계). Version History 예시에서 v1.0.0과 v2.1.0의 날짜가 같은 `2025-12-01`로 적혀 있어 오기로 보임.
- **[홍섭 실행 대기] E2E API 테스트 스킬화.** 설계는 확정(절차는 SKILL.md, env 값은 `settings.local.json`, 우선순위 Local > Project > User). 실제 제작이 남았다.
- **[재윤 다음에 만들 것 4가지]** ① `sync-claude-skills-to-codex`에 `scripts/` 도입 ② `mid-zettelkasten-synthesis`에 `context: fork` ③ 범용 유틸리티 스킬을 `~/.claude/skills/`에 신설 ④ 기존 스킬에 `EXAMPLES.md` 보강.
- **[팀] `scripts/`·`templates/`가 비어 있다는 공통 실측.** 재윤은 하나도 없고, 홍섭은 플러그인 루트에만 있고 스킬 안엔 `admin-guide-writer` 하나뿐. **공식 `codebase-visualizer`가 가장 따라 하기 좋은 형태**(SKILL.md엔 사용법만, 스크립트 코드는 컨텍스트에 안 들어감)라는 재윤의 제안이 출발점.
- **[팀] eval을 도입할 것인가.** 준호의 "평가부터 만든다"가 가장 강한 권고인데 가장 자주 빠진다는 지적, 그리고 skill-creator로 우리 스킬 9개의 발동률을 재볼지.

---

### 참고 출처 (정리본에서 모음)

**공식 문서**
- [Extend Claude with skills](https://code.claude.com/docs/en/skills) · [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) · [Skills for enterprise](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise)
- [Debug your configuration](https://code.claude.com/docs/en/debug-your-config) · [Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations) · [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)
- [Monitoring (OpenTelemetry)](https://code.claude.com/docs/en/monitoring-usage) · [What's new](https://code.claude.com/docs/en/whats-new) · settings.md · statusline.md · how-claude-code-works.md

**저장소·도구**
- [anthropics/skills](https://github.com/anthropics/skills) · [Agent Skills 오픈 표준](https://agentskills.io) · [skill-creator 업데이트 발표](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)
- [nova-workflow](https://github.com/mediquitous-dev/nova-workflow)(홍섭 제작·사내 배포) · [ECC — Everything Claude Code](https://github.com/affaan-m/ecc) · [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)

> 커뮤니티 프로젝트가 제시하는 스킬·에이전트 개수와 성능 수치는 각 프로젝트 자체 문서 기준이며, 독립적으로 검증된 값이 아니다. 버전에 민감한 내용(v2.1.x 변경점 등)은 공식문서에서 재확인이 필요하다.
