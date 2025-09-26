---
keywords:
  - Compute as Teacher
  - Self-Proposed Rubrics
  - Large Language Models
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:58:36.427081",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Compute as Teacher",
    "Self-Proposed Rubrics",
    "Large Language Models"
  ],
  "rejected_keywords": [
    "Reinforcement Learning"
  ],
  "similarity_scores": {
    "Compute as Teacher": 0.8,
    "Self-Proposed Rubrics": 0.77,
    "Large Language Models": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Compute as Teacher: Turning Inference Compute Into Reference-Free Supervision

**Korean Title:** 교사로서의 계산: 추론 계산을 참조 없는 감독으로 전환하기

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Compute as Teacher|Compute as Teacher]], [[keywords/Self-Proposed Rubrics|Self-Proposed Rubrics]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Teaching According to Talents! Instruction Tuning LLMs with Competence-Aware Curriculum Learning_20250917|Teaching According to Talents! Instruction Tuning LLMs with Competence-Aware Curriculum Learning]] (80.9% similar)
- [[TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (80.4% similar)
- [[From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (79.9% similar)
- [[Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (79.7% similar)
- [[Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (79.6% similar)

## 📋 저자 정보

**Authors:** Dulhan Jayalath, Shashwat Goel, Thomas Foster, Parag Jain, Suchin Gururangan, Cheng Zhang, Anirudh Goyal, Alan Schelten

## 📄 Abstract (원문)

Where do learning signals come from when there is no ground truth in
post-training? We propose turning exploration into supervision through Compute
as Teacher (CaT), which converts the model's own exploration at inference-time
into reference-free supervision by synthesizing a single reference from a group
of parallel rollouts and then optimizing toward it. Concretely, the current
policy produces a group of rollouts; a frozen anchor (the initial policy)
reconciles omissions and contradictions to estimate a reference, turning extra
inference-time compute into a teacher signal. We turn this into rewards in two
regimes: (i) verifiable tasks use programmatic equivalence on final answers;
(ii) non-verifiable tasks use self-proposed rubrics-binary, auditable criteria
scored by an independent LLM judge, with reward given by the fraction
satisfied. Unlike selection methods (best-of-N, majority, perplexity, or judge
scores), synthesis may disagree with the majority and be correct even when all
rollouts are wrong; performance scales with the number of rollouts. As a
test-time procedure, CaT improves Gemma 3 4B, Qwen 3 4B, and Llama 3.1 8B (up
to +27% on MATH-500; +12% on HealthBench). With reinforcement learning
(CaT-RL), we obtain further gains (up to +33% and +30%), with the trained
policy surpassing the initial teacher signal.

## 🔍 Abstract (한글 번역)

학습 신호는 훈련 후에 정답이 없을 때 어디에서 오는가? 우리는 Compute as Teacher (CaT)를 통해 탐색을 감독으로 전환하는 방법을 제안한다. 이는 모델의 추론 시간 탐색을 병렬 롤아웃 그룹에서 단일 참조를 합성하여 참조 없는 감독으로 변환한 후 이를 최적화하는 방식이다. 구체적으로, 현재 정책은 롤아웃 그룹을 생성하고, 고정된 앵커(초기 정책)는 누락 및 모순을 조정하여 참조를 추정하며, 추가적인 추론 시간 계산을 교사 신호로 전환한다. 우리는 이를 두 가지 체제에서 보상으로 전환한다: (i) 검증 가능한 작업은 최종 답변의 프로그램적 동등성을 사용한다; (ii) 검증 불가능한 작업은 독립적인 LLM 심판에 의해 점수화된 이진, 감사 가능한 기준인 자체 제안 루브릭을 사용하며, 만족된 비율에 따라 보상이 주어진다. 선택 방법(최상의 N, 다수결, 당혹도, 또는 심판 점수)과 달리, 합성은 다수와 의견이 다를 수 있으며 모든 롤아웃이 틀렸을 때도 올바를 수 있다; 성능은 롤아웃 수에 따라 확장된다. 테스트 시간 절차로서, CaT는 Gemma 3 4B, Qwen 3 4B, 그리고 Llama 3.1 8B의 성능을 향상시킨다 (MATH-500에서 최대 +27%; HealthBench에서 +12%). 강화 학습(CaT-RL)과 함께, 우리는 추가적인 향상을 얻으며 (최대 +33% 및 +30%), 훈련된 정책이 초기 교사 신호를 능가한다.

## 📝 요약

이 논문은 학습 신호가 없는 상황에서 모델의 탐색을 감독 신호로 전환하는 방법인 Compute as Teacher (CaT)를 제안합니다. CaT는 모델의 추론 시 탐색을 통해 생성된 여러 결과를 하나의 참조로 합성하고, 이를 기반으로 최적화합니다. 두 가지 방식으로 보상을 제공합니다: 검증 가능한 작업에서는 프로그램적 동등성을 사용하고, 비검증 작업에서는 독립적인 LLM 심판이 평가하는 기준을 사용합니다. CaT는 다수의 결과와 다를 수 있지만, 오히려 정확할 수 있으며, 롤아웃 수에 따라 성능이 향상됩니다. 실험 결과, CaT는 여러 모델의 성능을 크게 향상시켰으며, 강화 학습을 통해 추가적인 성능 향상을 달성했습니다.

## 🎯 주요 포인트

- 1. Compute as Teacher (CaT)는 모델의 탐색 과정을 감독 신호로 전환하여 참조 없이 최적화하는 방법을 제안합니다.

- 2. CaT는 병렬 롤아웃 그룹에서 단일 참조를 합성하여 추가 추론 시간 계산을 교사 신호로 전환합니다.

- 3. 검증 가능한 작업에서는 최종 답변의 프로그램적 동등성을 사용하고, 검증 불가능한 작업에서는 독립적인 LLM 판사가 채점하는 기준을 사용하여 보상을 제공합니다.

- 4. CaT는 롤아웃 수에 따라 성능이 확장되며, 모든 롤아웃이 틀린 경우에도 다수결과 다르게 정답을 제시할 수 있습니다.

- 5. 강화 학습(CaT-RL)을 통해 추가적인 성능 향상을 이루며, 훈련된 정책이 초기 교사 신호를 능가합니다.

---

*Generated on 2025-09-20 07:39:42*