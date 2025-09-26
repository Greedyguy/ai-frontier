---
keywords:
  - Neuro-inspired Communication
  - Sparse Neural Networks
  - Hebbian Learning
  - Dynamic Sparse Training
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2508.14140
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:20:30.408666",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neuro-inspired Communication",
    "Sparse Neural Networks",
    "Hebbian Learning",
    "Dynamic Sparse Training"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neuro-inspired Communication": 0.78,
    "Sparse Neural Networks": 0.81,
    "Hebbian Learning": 0.77,
    "Dynamic Sparse Training": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neuro-inspired Ensemble-to-Ensemble Communication",
        "canonical": "Neuro-inspired Communication",
        "aliases": [
          "Ensemble Communication",
          "Neuro-inspired Connectivity"
        ],
        "category": "unique_technical",
        "rationale": "This concept is novel and specific to the paper, offering a unique perspective on ANN design inspired by biological systems.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sparse and Efficient ANNs",
        "canonical": "Sparse Neural Networks",
        "aliases": [
          "Efficient ANNs",
          "Sparse ANNs"
        ],
        "category": "specific_connectable",
        "rationale": "Sparsity in neural networks is a key concept for improving efficiency and is highly relevant to current research trends.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.76,
        "link_intent_score": 0.81
      },
      {
        "surface": "Hebbian-inspired rewiring rule",
        "canonical": "Hebbian Learning",
        "aliases": [
          "Hebbian Rewiring",
          "Hebbian Rule"
        ],
        "category": "specific_connectable",
        "rationale": "Hebbian principles are foundational in neuroscience and provide a strong link to biologically inspired learning mechanisms.",
        "novelty_score": 0.67,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Dynamic Sparse Training",
        "canonical": "Dynamic Sparse Training",
        "aliases": [
          "DST",
          "Sparse Training"
        ],
        "category": "unique_technical",
        "rationale": "This training mechanism is a novel approach to optimizing neural networks by dynamically adjusting sparsity.",
        "novelty_score": 0.78,
        "connectivity_score": 0.71,
        "specificity_score": 0.81,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "ANN",
      "model",
      "accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neuro-inspired Ensemble-to-Ensemble Communication",
      "resolved_canonical": "Neuro-inspired Communication",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sparse and Efficient ANNs",
      "resolved_canonical": "Sparse Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.76,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Hebbian-inspired rewiring rule",
      "resolved_canonical": "Hebbian Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.67,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Dynamic Sparse Training",
      "resolved_canonical": "Dynamic Sparse Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.71,
        "specificity": 0.81,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.14140.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2508.14140](https://arxiv.org/abs/2508.14140)

## 🔗 유사한 논문
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN: A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (85.4% similar)
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (82.7% similar)
- [[2025-09-22/Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception_20250922|Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception]] (82.5% similar)
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods: Reviving Transformer for Graph Clustering]] (82.4% similar)
- [[2025-09-18/GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque: Torque-Driven Rewiring Graph Neural Network]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Sparse Neural Networks|Sparse Neural Networks]], [[keywords/Hebbian Learning|Hebbian Learning]]
**⚡ Unique Technical**: [[keywords/Neuro-inspired Communication|Neuro-inspired Communication]], [[keywords/Dynamic Sparse Training|Dynamic Sparse Training]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.14140v2 Announce Type: replace-cross 
Abstract: The structure of biological neural circuits-modular, hierarchical, and sparsely interconnected-reflects an efficient trade-off between wiring cost, functional specialization, and robustness. These principles offer valuable insights for artificial neural network (ANN) design, especially as networks grow in depth and scale. Sparsity, in particular, has been widely explored for reducing memory and computation, improving speed, and enhancing generalization. Motivated by systems neuroscience findings, we explore how patterns of functional connectivity in the mouse visual cortex-specifically, ensemble-to-ensemble communication, can inform ANN design. We introduce G2GNet, a novel architecture that imposes sparse, modular connectivity across feedforward layers. Despite having significantly fewer parameters than fully connected models, G2GNet achieves superior accuracy on standard vision benchmarks. To our knowledge, this is the first architecture to incorporate biologically observed functional connectivity patterns as a structural bias in ANN design. We complement this static bias with a dynamic sparse training (DST) mechanism that prunes and regrows edges during training. We also propose a Hebbian-inspired rewiring rule based on activation correlations, drawing on principles of biological plasticity. G2GNet achieves up to 75% sparsity while improving accuracy by up to 4.3% on benchmarks, including Fashion-MNIST, CIFAR-10, and CIFAR-100, outperforming dense baselines with far fewer computations.

## 📝 요약

이 논문은 생물학적 신경 회로의 구조적 특성을 인공지능 신경망(ANN) 설계에 적용하는 연구를 다룹니다. 특히, 쥐의 시각 피질에서 관찰된 기능적 연결 패턴을 활용하여 ANN 설계에 반영한 G2GNet이라는 새로운 아키텍처를 제안합니다. G2GNet은 희소하고 모듈화된 연결성을 도입하여, 적은 수의 파라미터로도 높은 정확도를 달성합니다. 또한, 동적 희소 훈련(DST) 메커니즘과 생물학적 가소성 원리에 기반한 Hebbian 재연결 규칙을 제안하여, Fashion-MNIST, CIFAR-10, CIFAR-100 등의 벤치마크에서 최대 75%의 희소성을 유지하면서 정확도를 최대 4.3% 향상시켰습니다. 이는 기존의 밀집 모델보다 적은 계산으로도 더 나은 성능을 보입니다.

## 🎯 주요 포인트

- 1. 생물학적 신경 회로의 구조는 인공 신경망 설계에 유용한 통찰을 제공하며, 특히 네트워크가 깊고 규모가 커질수록 중요하다.
- 2. G2GNet은 생물학적으로 관찰된 기능적 연결 패턴을 구조적 편향으로 도입한 최초의 인공 신경망 아키텍처이다.
- 3. G2GNet은 피드포워드 계층 전반에 걸쳐 희소하고 모듈식 연결성을 부과하여, 적은 매개변수로도 표준 비전 벤치마크에서 우수한 정확도를 달성한다.
- 4. 동적 희소 훈련 메커니즘을 통해 훈련 중 엣지를 가지치기하고 재성장시키며, 생물학적 가소성 원칙에 기반한 Hebbian 영감을 받은 재배선 규칙을 제안한다.
- 5. G2GNet은 Fashion-MNIST, CIFAR-10, CIFAR-100 벤치마크에서 최대 75%의 희소성을 달성하면서도 정확도를 최대 4.3% 향상시켜, 조밀한 기준선보다 적은 계산으로도 더 나은 성능을 보인다.


---

*Generated on 2025-09-24 01:20:30*