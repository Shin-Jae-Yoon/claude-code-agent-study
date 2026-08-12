---
title: "발동을 봤다고 스킬이 잘 동작하는 것은 아니다"
type: "claim"
status: "seed"
tags: ["measurement", "evaluation"]
---

# 발동을 봤다고 스킬이 잘 동작하는 것은 아니다

스킬이 실제로 발동하는 걸 눈으로 확인하는 것과 그 스킬이 결과를 개선했는지는 별개의 질문이다. **발동률**과 **출력 품질**은 따로 재야 하고, 둘 다 스킬을 끈 상태와 비교해야만 알 수 있다. 만드는 것보다 측정이 어렵다.

## 근거와 출처

- [3장 준호 정리](../../chapters/ch3/junho/Chapter%2003.%20에이전트%20스킬.md): "발동하는 걸 봤다고 잘 동작하는 게 아니다. 발동률과 출력 품질은 따로 재야 하고, 둘 다 스킬을 끈 상태와의 비교로만 알 수 있다." `skill-creator` 플러그인의 4모드(Create/Eval/Improve/Benchmark), `evals/evals.json`에 테스트 케이스 저장, 케이스마다 독립 서브에이전트로 병렬 실행, with/without 벤치마크, 두 버전 블라인드 A/B, description 튜닝을 수단으로 들었다. 근거 사례: "Anthropic이 자체 문서 생성 스킬로 시험했을 때 공개 스킬 6개 중 5개에서 트리거가 개선됐다. 측정 인프라 없이는 보이지 않았을 개선이다."

## 연결

- [스킬 측정에는 네 개의 축이 있다](./skill-measurement-has-four-axes.md) — 이 주장이 지목하는 두 축(발동·품질)이 그 지도 안에 놓인다.
- [스킬은 평가부터 만든다](./eval-first-skill-development.md) — 측정을 나중이 아니라 처음에 두라는 실천으로 이어진다.
- [YAML이 깨지면 본문만 빈 메타데이터로 로드된다](./yaml-error-loads-body-with-empty-metadata.md) — 관측한 증상과 실제 원인이 어긋나는 같은 계열의 문제다.
