---
keywords:
  - Sparse Neural Network
  - Neural Network
  - Iterative Hard Thresholding
  - Sparse Recovery
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20323
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:48:41.888202",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sparse Neural Network",
    "Neural Network",
    "Iterative Hard Thresholding",
    "Sparse Recovery"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sparse Neural Network": 0.88,
    "Neural Network": 0.7,
    "Iterative Hard Thresholding": 0.78,
    "Sparse Recovery": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sparse Neural Networks",
        "canonical": "Sparse Neural Network",
        "aliases": [
          "Sparse Networks"
        ],
        "category": "specific_connectable",
        "rationale": "Sparse Neural Networks are a specific type of neural network architecture that can be linked to research on efficient model design.",
        "novelty_score": 0.75,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "ReLU Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "ReLU Networks"
        ],
        "category": "broad_technical",
        "rationale": "ReLU Neural Networks are a fundamental type of neural network that connects to a wide range of deep learning research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Iterative Hard Thresholding",
        "canonical": "Iterative Hard Thresholding",
        "aliases": [
          "IHT"
        ],
        "category": "unique_technical",
        "rationale": "Iterative Hard Thresholding is a specific algorithm relevant to sparse recovery, offering unique insights into optimization techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sparse Recovery",
        "canonical": "Sparse Recovery",
        "aliases": [
          "Sparse Signal Recovery"
        ],
        "category": "specific_connectable",
        "rationale": "Sparse Recovery is a key concept in signal processing and neural network optimization, linking to efficient model training.",
        "novelty_score": 0.68,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "simple experiments",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Sparse Neural Networks",
      "resolved_canonical": "Sparse Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "ReLU Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Iterative Hard Thresholding",
      "resolved_canonical": "Iterative Hard Thresholding",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sparse Recovery",
      "resolved_canonical": "Sparse Recovery",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# A Recovery Guarantee for Sparse Neural Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20323.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20323](https://arxiv.org/abs/2509.20323)

## 🔗 유사한 논문
- [[2025-09-23/Pulling Back the Curtain on ReLU Networks_20250923|Pulling Back the Curtain on ReLU Networks]] (83.3% similar)
- [[2025-09-25/Sobolev acceleration for neural networks_20250925|Sobolev acceleration for neural networks]] (83.3% similar)
- [[2025-09-25/Robust Training of Neural Networks at Arbitrary Precision and Sparsity_20250925|Robust Training of Neural Networks at Arbitrary Precision and Sparsity]] (80.6% similar)
- [[2025-09-23/Checking extracted rules in Neural Networks_20250923|Checking extracted rules in Neural Networks]] (80.3% similar)
- [[2025-09-24/Efficient Reinforcement Learning by Reducing Forgetting with Elephant Activation Functions_20250924|Efficient Reinforcement Learning by Reducing Forgetting with Elephant Activation Functions]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Sparse Neural Network|Sparse Neural Network]], [[keywords/Sparse Recovery|Sparse Recovery]]
**⚡ Unique Technical**: [[keywords/Iterative Hard Thresholding|Iterative Hard Thresholding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20323v1 Announce Type: new 
Abstract: We prove the first guarantees of sparse recovery for ReLU neural networks, where the sparse network weights constitute the signal to be recovered. Specifically, we study structural properties of the sparse network weights for two-layer, scalar-output networks under which a simple iterative hard thresholding algorithm recovers these weights exactly, using memory that grows linearly in the number of nonzero weights. We validate this theoretical result with simple experiments on recovery of sparse planted MLPs, MNIST classification, and implicit neural representations. Experimentally, we find performance that is competitive with, and often exceeds, a high-performing but memory-inefficient baseline based on iterative magnitude pruning.

## 📝 요약

이 논문은 ReLU 신경망의 희소 회복에 대한 최초의 보장을 제시합니다. 특히, 2층 스칼라 출력 네트워크의 희소 네트워크 가중치의 구조적 특성을 연구하여, 간단한 반복적 하드 스레숄딩 알고리즘이 메모리를 비선형적으로 증가시키지 않고 정확하게 가중치를 회복할 수 있음을 증명합니다. 이 이론적 결과는 희소하게 심어진 MLP, MNIST 분류, 암묵적 신경 표현의 회복 실험을 통해 검증되었습니다. 실험 결과, 제안된 방법은 메모리 효율성이 떨어지는 반복적 크기 가지치기 기반의 고성능 기준선과 비교하여 경쟁력 있는 성능을 보였으며, 종종 이를 능가했습니다.

## 🎯 주요 포인트

- 1. ReLU 신경망의 희소 복구에 대한 최초의 보장을 증명하였습니다.
- 2. 이 연구는 2층, 스칼라 출력 네트워크의 희소 네트워크 가중치의 구조적 특성을 분석합니다.
- 3. 간단한 반복적 하드 스레숄딩 알고리즘을 사용하여 메모리가 비선형적으로 증가하지 않고 정확하게 가중치를 복구할 수 있음을 입증하였습니다.
- 4. 실험적으로 희소한 MLP, MNIST 분류, 암묵적 신경 표현의 복구에서 높은 성능을 보였습니다.
- 5. 제안된 방법은 메모리 비효율적인 반복적 크기 가지치기 기반의 고성능 기준과 경쟁하며 종종 이를 능가합니다.


---

*Generated on 2025-09-25 16:48:41*