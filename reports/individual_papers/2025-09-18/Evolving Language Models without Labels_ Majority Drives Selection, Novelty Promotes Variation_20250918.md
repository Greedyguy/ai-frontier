---
keywords:
  - Reinforcement Learning
  - Large Language Models
  - Evolution-Oriented and Label-free Reinforcement Learning
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:29:35.060196",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Large Language Models",
    "Evolution-Oriented and Label-free Reinforcement Learning"
  ],
  "rejected_keywords": [
    "Entropy Regularizer",
    "Semantic Space"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.85,
    "Large Language Models": 0.8,
    "Evolution-Oriented and Label-free Reinforcement Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Evolving Language Models without Labels: Majority Drives Selection, Novelty Promotes Variation

**Korean Title:** 레이블 없이 진화하는 언어 모델: 다수는 선택을 주도하고, 참신함은 변화를 촉진한다.

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]], [[keywords/Large Language Models|Large Language Models]]
**⚡ Unique Technical**: [[keywords/Evolution-Oriented and Label-free Reinforcement Learning|Evolution-Oriented and Label-free Reinforcement Learning]]

## 🔗 유사한 논문
- [[Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (84.0% similar)
- [[Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (83.7% similar)
- [[Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (83.1% similar)
- [[FlowRL_ Matching Reward Distributions for LLM Reasoning_20250919|FlowRL Matching Reward Distributions for LLM Reasoning]] (82.5% similar)
- [[Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (82.1% similar)

## 📋 저자 정보

**Authors:** Yujun Zhou, Zhenwen Liang, Haolin Liu, Wenhao Yu, Kishan Panaganti, Linfeng Song, Dian Yu, Xiangliang Zhang, Haitao Mi, Dong Yu

## 📄 Abstract (원문)

Large language models (LLMs) are increasingly trained with reinforcement
learning from verifiable rewards (RLVR), yet real-world deployment demands
models that can self-improve without labels or external judges. Existing
label-free methods, confidence minimization, self-consistency, or majority-vote
objectives, stabilize learning but steadily shrink exploration, causing an
entropy collapse: generations become shorter, less diverse, and brittle. Unlike
prior approaches such as Test-Time Reinforcement Learning (TTRL), which
primarily adapt models to the immediate unlabeled dataset at hand, our goal is
broader: to enable general improvements without sacrificing the model's
inherent exploration capacity and generalization ability, i.e., evolving. We
formalize this issue and propose EVolution-Oriented and Label-free
Reinforcement Learning (EVOL-RL), a simple rule that couples stability with
variation under a label-free setting. EVOL-RL keeps the majority-voted answer
as a stable anchor (selection) while adding a novelty-aware reward that favors
responses whose reasoning differs from what has already been produced
(variation), measured in semantic space. Implemented with GRPO, EVOL-RL also
uses asymmetric clipping to preserve strong signals and an entropy regularizer
to sustain search. This majority-for-selection + novelty-for-variation design
prevents collapse, maintains longer and more informative chains of thought, and
improves both pass@1 and pass@n. EVOL-RL consistently outperforms the
majority-only TTRL baseline; e.g., training on label-free AIME24 lifts
Qwen3-4B-Base AIME25 pass@1 from TTRL's 4.6% to 16.4%, and pass@16 from 18.5%
to 37.9%. EVOL-RL not only prevents diversity collapse but also unlocks
stronger generalization across domains (e.g., GPQA). Furthermore, we
demonstrate that EVOL-RL also boosts performance in the RLVR setting,
highlighting its broad applicability.

## 🔍 Abstract (한글 번역)

대형 언어 모델(LLM)은 점점 더 검증 가능한 보상(RLVR)을 통한 강화 학습으로 훈련되고 있지만, 실제 세계에서의 배포는 라벨이나 외부 심판 없이도 스스로 개선할 수 있는 모델을 요구합니다. 기존의 라벨 없는 방법들, 즉 신뢰도 최소화, 자기 일관성, 또는 다수결 목표는 학습을 안정화하지만 탐색을 점진적으로 축소시켜 엔트로피 붕괴를 초래합니다: 생성물이 짧아지고, 다양성이 줄어들며, 취약해집니다. 테스트 시간 강화 학습(TTRL)과 같은 이전 접근 방식은 주로 즉각적인 라벨 없는 데이터셋에 모델을 적응시키는 데 중점을 두지만, 우리의 목표는 더 광범위합니다: 모델의 고유한 탐색 능력과 일반화 능력을 희생하지 않고 일반적인 개선을 가능하게 하는 것입니다, 즉 진화하는 것입니다. 우리는 이 문제를 공식화하고 진화 지향적이고 라벨 없는 강화 학습(EVOL-RL)을 제안합니다. 이는 라벨 없는 환경에서 안정성과 변화를 결합하는 간단한 규칙입니다. EVOL-RL은 다수결로 선택된 답변을 안정적인 기준점(선택)으로 유지하면서, 이미 생성된 것과 다른 추론을 가진 응답을 선호하는 참신성 인식 보상을 추가하여(변화) 의미 공간에서 측정합니다. GRPO로 구현된 EVOL-RL은 강력한 신호를 보존하기 위해 비대칭 클리핑을 사용하고, 탐색을 지속하기 위해 엔트로피 정규화를 사용합니다. 이 다수결-선택 + 참신성-변화 설계는 붕괴를 방지하고, 더 길고 정보가 풍부한 사고의 연쇄를 유지하며, pass@1 및 pass@n 모두를 향상시킵니다. EVOL-RL은 다수결만 사용하는 TTRL 기준선을 일관되게 능가합니다; 예를 들어, 라벨 없는 AIME24에서의 훈련은 Qwen3-4B-Base AIME25의 pass@1을 TTRL의 4.6%에서 16.4%로, pass@16을 18.5%에서 37.9%로 향상시킵니다. EVOL-RL은 다양성 붕괴를 방지할 뿐만 아니라 도메인 전반에 걸쳐 더 강력한 일반화를 가능하게 합니다(예: GPQA). 더욱이, 우리는 EVOL-RL이 RLVR 환경에서도 성능을 향상시킨다는 것을 증명하여 그 광범위한 적용 가능성을 강조합니다.

## 📝 요약

대형 언어 모델(LLM)의 학습에 있어 검증 가능한 보상을 통한 강화 학습(RLVR)이 증가하고 있지만, 실제 환경에서는 라벨이나 외부 심판 없이 스스로 개선할 수 있는 모델이 필요합니다. 기존의 라벨 없는 방법들은 학습의 안정성을 제공하지만 탐색을 줄여 다양성이 감소하는 문제를 초래합니다. 이를 해결하기 위해, 우리는 진화 지향적 라벨 없는 강화 학습(EVOL-RL)을 제안합니다. EVOL-RL은 다수결로 선택된 답변을 안정적인 기준으로 삼고, 새로운 사고를 장려하는 보상을 추가하여 다양성을 유지합니다. 이 방법은 모델의 탐색 능력과 일반화 능력을 유지하면서도 성능을 향상시킵니다. 실험 결과, EVOL-RL은 기존의 TTRL보다 우수한 성능을 보였으며, 다양한 도메인에서의 일반화 능력도 강화되었습니다. EVOL-RL은 RLVR 환경에서도 성능을 높여 그 적용 가능성을 입증했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 실제 활용을 위해서는 라벨이나 외부 심판 없이도 스스로 개선할 수 있는 능력이 필요합니다.

- 2. 기존의 라벨 없는 방법들은 학습의 안정성을 제공하지만 탐색 능력을 감소시켜 다양성 붕괴를 초래합니다.

- 3. EVOL-RL은 라벨 없는 환경에서 안정성과 변화를 결합하여 모델의 탐색 능력과 일반화 능력을 유지합니다.

- 4. EVOL-RL은 다수결로 선택된 답변을 안정적인 기준으로 삼고, 새로운 사고를 장려하는 보상을 추가하여 다양성을 유지합니다.

- 5. EVOL-RL은 TTRL 기반보다 우수한 성능을 보이며, 다양한 도메인에서의 일반화 능력을 강화합니다.

---

*Generated on 2025-09-20 00:52:07*