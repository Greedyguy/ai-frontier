<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:56:28.554090",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Shared-Weights Extender",
    "Steepest Voting Distributor",
    "Neural Network Expansion",
    "Neuron Inactivity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Shared-Weights Extender": 0.82,
    "Steepest Voting Distributor": 0.79,
    "Neural Network Expansion": 0.77,
    "Neuron Inactivity": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Shared-Weights Extender",
        "canonical": "Shared-Weights Extender",
        "aliases": [
          "SWE"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for neural network expansion, enhancing connectivity by preventing neuron inactivity.",
        "novelty_score": 0.85,
        "connectivity_score": 0.78,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Steepest Voting Distributor",
        "canonical": "Steepest Voting Distributor",
        "aliases": [
          "SVoD"
        ],
        "category": "unique_technical",
        "rationale": "Presents a new gradient-based method for neuron allocation, crucial for linking expansion techniques.",
        "novelty_score": 0.87,
        "connectivity_score": 0.75,
        "specificity_score": 0.86,
        "link_intent_score": 0.79
      },
      {
        "surface": "Neural Network Expansion",
        "canonical": "Neural Network Expansion",
        "aliases": [
          "NN Expansion"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's theme, facilitating connections with existing neural network literature.",
        "novelty_score": 0.58,
        "connectivity_score": 0.83,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Neuron Inactivity",
        "canonical": "Neuron Inactivity",
        "aliases": [
          "Inactive Neurons"
        ],
        "category": "specific_connectable",
        "rationale": "Addresses a key challenge in neural network training, relevant for linking with optimization strategies.",
        "novelty_score": 0.64,
        "connectivity_score": 0.79,
        "specificity_score": 0.76,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "capacity growth"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Shared-Weights Extender",
      "resolved_canonical": "Shared-Weights Extender",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.78,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Steepest Voting Distributor",
      "resolved_canonical": "Steepest Voting Distributor",
      "decision": "linked",
      "scores": {
        "novelty": 0.87,
        "connectivity": 0.75,
        "specificity": 0.86,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Neural Network Expansion",
      "resolved_canonical": "Neural Network Expansion",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.83,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Neuron Inactivity",
      "resolved_canonical": "Neuron Inactivity",
      "decision": "linked",
      "scores": {
        "novelty": 0.64,
        "connectivity": 0.79,
        "specificity": 0.76,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Shared-Weights Extender and Gradient Voting for Neural Network Expansion

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18842.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18842](https://arxiv.org/abs/2509.18842)

## 🔗 유사한 논문
- [[2025-09-23/Bio-Inspired Adaptive Neurons for Dynamic Weighting in Artificial Neural Networks_20250923|Bio-Inspired Adaptive Neurons for Dynamic Weighting in Artificial Neural Networks]] (82.6% similar)
- [[2025-09-23/Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks_20250923|Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks]] (81.9% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (81.4% similar)
- [[2025-09-23/Word2VecGD_ Neural Graph Drawing with Cosine-Stress Optimization_20250923|Word2VecGD: Neural Graph Drawing with Cosine-Stress Optimization]] (81.3% similar)
- [[2025-09-23/Deep Hierarchical Learning with Nested Subspace Networks_20250923|Deep Hierarchical Learning with Nested Subspace Networks]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Neural Network Expansion|Neural Network Expansion]], [[keywords/Neuron Inactivity|Neuron Inactivity]]
**⚡ Unique Technical**: [[keywords/Shared-Weights Extender|Shared-Weights Extender]], [[keywords/Steepest Voting Distributor|Steepest Voting Distributor]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18842v1 Announce Type: new 
Abstract: Expanding neural networks during training is a promising way to augment capacity without retraining larger models from scratch. However, newly added neurons often fail to adjust to a trained network and become inactive, providing no contribution to capacity growth. We propose the Shared-Weights Extender (SWE), a novel method explicitly designed to prevent inactivity of new neurons by coupling them with existing ones for smooth integration. In parallel, we introduce the Steepest Voting Distributor (SVoD), a gradient-based method for allocating neurons across layers during deep network expansion. Our extensive benchmarking on four datasets shows that our method can effectively suppress neuron inactivity and achieve better performance compared to other expanding methods and baselines.

## 📝 요약

이 논문은 훈련 중 신경망을 확장하여 용량을 증가시키는 방법을 제안합니다. 새로운 뉴런이 비활성화되는 문제를 해결하기 위해, 기존 뉴런과 결합하여 부드럽게 통합할 수 있는 Shared-Weights Extender(SWE) 방법을 개발했습니다. 또한, Steepest Voting Distributor(SVoD)라는 기울기 기반 방법을 통해 심층 네트워크 확장 시 뉴런을 적절히 배분합니다. 네 가지 데이터셋에 대한 광범위한 벤치마킹 결과, 제안된 방법이 뉴런 비활성화를 효과적으로 억제하고 다른 확장 방법 및 기준보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 훈련 중 신경망을 확장하는 것은 모델을 처음부터 다시 훈련하지 않고 용량을 증가시키는 유망한 방법이다.
- 2. 새로 추가된 뉴런이 비활성화되는 문제를 해결하기 위해 기존 뉴런과 결합하여 매끄럽게 통합하는 Shared-Weights Extender (SWE) 방법을 제안한다.
- 3. Steepest Voting Distributor (SVoD)는 깊은 네트워크 확장 시 뉴런을 레이어에 할당하는 기울기 기반 방법이다.
- 4. 네 가지 데이터셋에 대한 광범위한 벤치마킹 결과, 제안된 방법이 뉴런 비활성화를 효과적으로 억제하고 다른 확장 방법 및 기준선보다 더 나은 성능을 달성함을 보여준다.


---

*Generated on 2025-09-24 14:56:28*