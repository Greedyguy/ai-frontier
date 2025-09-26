---
keywords:
  - Mixture-of-Experts
  - Roster of Experts
  - Hyper-parallel scaling
  - Large Language Model
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17238
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:57:21.891931",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mixture-of-Experts",
    "Roster of Experts",
    "Hyper-parallel scaling",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mixture-of-Experts": 0.88,
    "Roster of Experts": 0.92,
    "Hyper-parallel scaling": 0.89,
    "Large Language Model": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Mixture-of-Experts",
        "canonical": "Mixture-of-Experts",
        "aliases": [
          "MoE"
        ],
        "category": "specific_connectable",
        "rationale": "Mixture-of-Experts is a key model architecture discussed in the paper, relevant for linking to other works on model ensembles.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.88
      },
      {
        "surface": "Roster of Experts",
        "canonical": "Roster of Experts",
        "aliases": [
          "RoE"
        ],
        "category": "unique_technical",
        "rationale": "Roster of Experts is a novel inference algorithm introduced in the paper, offering a unique approach to model scaling.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.92
      },
      {
        "surface": "Hyper-parallel scaling",
        "canonical": "Hyper-parallel scaling",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Hyper-parallel scaling is a new framework proposed in the paper, enhancing token-level prediction quality.",
        "novelty_score": 0.88,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.89
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's discussion, providing context for the proposed scaling methods.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "inference",
      "performance",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Mixture-of-Experts",
      "resolved_canonical": "Mixture-of-Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Roster of Experts",
      "resolved_canonical": "Roster of Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Hyper-parallel scaling",
      "resolved_canonical": "Hyper-parallel scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.88,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.89
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# MoEs Are Stronger than You Think: Hyper-Parallel Inference Scaling with RoE

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17238.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17238](https://arxiv.org/abs/2509.17238)

## 🔗 유사한 논문
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box: Interpretable LLMs via Semantic Resonance Architecture]] (86.8% similar)
- [[2025-09-22/DiEP_ Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning_20250922|DiEP: Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning]] (86.7% similar)
- [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE: Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (86.4% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals: Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (84.3% similar)
- [[2025-09-22/LongCat-Flash Technical Report_20250922|LongCat-Flash Technical Report]] (84.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Mixture-of-Experts|Mixture-of-Experts]]
**⚡ Unique Technical**: [[keywords/Roster of Experts|Roster of Experts]], [[keywords/Hyper-parallel scaling|Hyper-parallel scaling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17238v1 Announce Type: new 
Abstract: The generation quality of large language models (LLMs) is often improved by utilizing inference-time sequence-level scaling methods (e.g., Chain-of-Thought). We introduce hyper-parallel scaling, a complementary framework that improves prediction quality at the token level. Hyper-parallel scaling computes and aggregates multiple output proposals for a single token from the model. We implement this concept in Mixture-of-Experts (MoE) models, which we refer to as Roster of Experts (RoE). RoE is a training-free inference algorithm that turns a single MoE into a dynamic ensemble of MoEs. RoE injects controlled stochasticity into the expert routing mechanism, enabling it to sample multiple diverse experts for each token and aggregate their outputs for a more accurate final prediction.To overcome the computational cost, we introduce an efficient batching strategy and a specialized KV-caching mechanism that minimizes compute and memory overhead. For example, RoE enables a 7B MoE model to match the performance of a 10.5B MoE model while using 30% less compute for inference. These gains are achieved without any fine-tuning of model parameters.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 예측 품질을 향상시키기 위한 새로운 방법인 하이퍼 병렬 스케일링을 소개합니다. 이는 토큰 수준에서 여러 출력 제안을 계산하고 집계하여 예측 정확도를 높입니다. 이 방법은 전문가 혼합(MoE) 모델에 적용되어 '전문가 명단(RoE)'이라는 알고리즘으로 구현됩니다. RoE는 훈련 없이 단일 MoE를 동적 MoE 앙상블로 변환하며, 전문가 라우팅 메커니즘에 통제된 확률성을 주입해 각 토큰에 대해 다양한 전문가를 샘플링하고 그 출력을 집계합니다. 계산 비용을 줄이기 위해 효율적인 배칭 전략과 특수한 KV-캐싱 메커니즘을 도입하여 계산 및 메모리 오버헤드를 최소화합니다. 이를 통해 RoE는 7B MoE 모델이 10.5B MoE 모델의 성능을 30% 적은 계산 비용으로 달성할 수 있게 합니다. 이러한 성과는 모델 파라미터의 미세 조정 없이 이루어집니다.

## 🎯 주요 포인트

- 1. Hyper-parallel scaling은 토큰 수준에서 예측 품질을 향상시키는 보완적 프레임워크입니다.
- 2. Roster of Experts (RoE)는 Mixture-of-Experts (MoE) 모델에 적용된 훈련이 필요 없는 추론 알고리즘입니다.
- 3. RoE는 전문가 라우팅 메커니즘에 제어된 확률성을 주입하여 각 토큰에 대해 다양한 전문가를 샘플링하고 그 출력을 집계합니다.
- 4. RoE는 효율적인 배칭 전략과 KV-caching 메커니즘을 도입하여 계산 및 메모리 오버헤드를 최소화합니다.
- 5. RoE는 모델 파라미터의 미세 조정 없이도 7B MoE 모델이 10.5B MoE 모델의 성능을 30% 적은 계산 비용으로 달성할 수 있게 합니다.


---

*Generated on 2025-09-23 22:57:21*