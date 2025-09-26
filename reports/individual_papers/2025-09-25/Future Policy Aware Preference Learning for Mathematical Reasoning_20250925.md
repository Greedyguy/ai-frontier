---
keywords:
  - Large Language Model
  - Preference Learning
  - Mathematical Reasoning
  - Future Policy Aware Preference Learning
  - SimPER
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2509.19893
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:46:36.552481",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Preference Learning",
    "Mathematical Reasoning",
    "Future Policy Aware Preference Learning",
    "SimPER"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Preference Learning": 0.8,
    "Mathematical Reasoning": 0.75,
    "Future Policy Aware Preference Learning": 0.8,
    "SimPER": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Essential for understanding the context of preference learning in the paper.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Preference Learning",
        "canonical": "Preference Learning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Central to the paper's contribution, focusing on improving mathematical reasoning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Mathematical Reasoning",
        "canonical": "Mathematical Reasoning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Key application area where the proposed method is evaluated.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Future Policy Aware",
        "canonical": "Future Policy Aware Preference Learning",
        "aliases": [
          "FPA"
        ],
        "category": "unique_technical",
        "rationale": "The novel method proposed by the authors to enhance preference learning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "SimPER",
        "canonical": "SimPER",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "One of the methods evaluated with significant performance gains using FPA.",
        "novelty_score": 0.7,
        "connectivity_score": 0.5,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "trajectory",
      "probability",
      "regularization"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Preference Learning",
      "resolved_canonical": "Preference Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Mathematical Reasoning",
      "resolved_canonical": "Mathematical Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Future Policy Aware",
      "resolved_canonical": "Future Policy Aware Preference Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "SimPER",
      "resolved_canonical": "SimPER",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.5,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Future Policy Aware Preference Learning for Mathematical Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19893.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2509.19893](https://arxiv.org/abs/2509.19893)

## 🔗 유사한 논문
- [[2025-09-25/AAPO_ Enhancing the Reasoning Capabilities of LLMs with Advantage Momentum_20250925|AAPO: Enhancing the Reasoning Capabilities of LLMs with Advantage Momentum]] (85.7% similar)
- [[2025-09-23/From Uniform to Heterogeneous_ Tailoring Policy Optimization to Every Token's Nature_20250923|From Uniform to Heterogeneous: Tailoring Policy Optimization to Every Token's Nature]] (85.3% similar)
- [[2025-09-22/Entropy-Regularized Process Reward Model_20250922|Entropy-Regularized Process Reward Model]] (84.9% similar)
- [[2025-09-24/Exploiting Tree Structure for Credit Assignment in RL Training of LLMs_20250924|Exploiting Tree Structure for Credit Assignment in RL Training of LLMs]] (84.7% similar)
- [[2025-09-23/GPO_ Learning from Critical Steps to Improve LLM Reasoning_20250923|GPO: Learning from Critical Steps to Improve LLM Reasoning]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Preference Learning|Preference Learning]], [[keywords/Mathematical Reasoning|Mathematical Reasoning]], [[keywords/Future Policy Aware Preference Learning|Future Policy Aware Preference Learning]], [[keywords/SimPER|SimPER]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19893v1 Announce Type: new 
Abstract: Preference learning methods such as Direct Preference Optimization (DPO) have become standard for Large Language Model (LLM) post-training, yet they are often ineffective for mathematical reasoning. A key challenge is the large token overlap between preferred and dispreferred trajectories; lowering the probability of dispreferred trajectories also reduces the probability of shared useful tokens, leading to over-penalization and overall performance collapse. As a mitigation, existing algorithms include the probability of a trajectory under the current policy as a regularization term, which decreases the effect of the gradient when the probability is low. However, by the time this effect takes hold, useful tokens may have already been over-penalized as the model has begun to degrade. To address this, we propose Future Policy Aware (FPA) preference learning, which replaces the current policy with a future policy in the regularization term. This future policy is estimated via lightweight, logit-space extrapolation from a reference model toward the current model. FPA enables safer training by preemptively regularizing potentially problematic gradients. We apply FPA to DPO, RPO, and SimPER and evaluate them on the MATH and GSM8K benchmarks. FPA yields consistent performance gains, with the largest improvements observed with SimPER, achieving gains of up to 5.75%. We demonstrate that FPA provides proactive regularization while preserving the probability of shared, useful mathematical tokens, and enables longer, degradation-free training with negligible computational overhead. We will release our code publicly upon publication.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 수학적 추론 성능을 향상시키기 위한 Future Policy Aware (FPA) 선호 학습 방법을 제안합니다. 기존 방법은 선호되지 않는 경로의 확률을 낮추는 과정에서 유용한 토큰도 과도하게 패널티를 받아 성능 저하를 초래합니다. FPA는 현재 정책 대신 미래 정책을 정규화 항에 사용하여 이러한 문제를 해결합니다. 이를 통해 잠재적으로 문제가 될 수 있는 그래디언트를 사전에 정규화하고, 유용한 수학적 토큰의 확률을 유지하면서 성능을 개선합니다. MATH와 GSM8K 벤치마크에서 FPA를 적용한 결과, 특히 SimPER에서 최대 5.75%의 성능 향상을 보였습니다. FPA는 최소한의 계산 비용으로 더 긴 훈련을 가능하게 하며, 코드 공개를 예정하고 있습니다.

## 🎯 주요 포인트

- 1. Direct Preference Optimization(DPO)와 같은 선호 학습 방법은 대형 언어 모델(LLM) 후속 훈련에 표준으로 자리잡았지만, 수학적 추론에는 비효율적입니다.
- 2. 선호 및 비선호 경로 간의 큰 토큰 중복이 문제로, 비선호 경로의 확률을 낮추면 유용한 토큰의 확률도 감소하여 과도한 패널티와 성능 저하를 초래합니다.
- 3. Future Policy Aware(FPA) 선호 학습은 현재 정책 대신 미래 정책을 정규화 항에 사용하여 문제를 해결합니다.
- 4. FPA는 DPO, RPO, SimPER에 적용되어 MATH와 GSM8K 벤치마크에서 일관된 성능 향상을 보였으며, 특히 SimPER에서 최대 5.75%의 향상을 달성했습니다.
- 5. FPA는 유용한 수학적 토큰의 확률을 보존하면서도, 잠재적으로 문제를 일으킬 수 있는 그래디언트를 사전에 정규화하여 안전한 훈련을 가능하게 합니다.


---

*Generated on 2025-09-26 08:46:36*