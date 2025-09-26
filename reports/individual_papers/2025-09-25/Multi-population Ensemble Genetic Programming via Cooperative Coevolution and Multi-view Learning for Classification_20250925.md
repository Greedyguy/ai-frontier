---
keywords:
  - Multi-population Ensemble Genetic Programming
  - Cooperative Coevolution
  - Multimodal Learning
  - Ensemble-based Fitness Mechanism
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19339
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:26:41.505948",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-population Ensemble Genetic Programming",
    "Cooperative Coevolution",
    "Multimodal Learning",
    "Ensemble-based Fitness Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-population Ensemble Genetic Programming": 0.78,
    "Cooperative Coevolution": 0.82,
    "Multimodal Learning": 0.8,
    "Ensemble-based Fitness Mechanism": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-population Ensemble Genetic Programming",
        "canonical": "Multi-population Ensemble Genetic Programming",
        "aliases": [
          "MEGP"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced by the paper, providing a unique approach to evolutionary learning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Cooperative Coevolution",
        "canonical": "Cooperative Coevolution",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Cooperative coevolution is a key component of the framework, facilitating inter-population cooperation.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multi-view Learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multi-view Representation Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-view learning aligns with multimodal learning, enhancing the framework's ability to handle diverse data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Ensemble-based Fitness Mechanism",
        "canonical": "Ensemble-based Fitness Mechanism",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This mechanism is central to the framework's operation, promoting adaptive decision fusion.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "classification challenges",
      "high-dimensional feature spaces"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-population Ensemble Genetic Programming",
      "resolved_canonical": "Multi-population Ensemble Genetic Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Cooperative Coevolution",
      "resolved_canonical": "Cooperative Coevolution",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multi-view Learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Ensemble-based Fitness Mechanism",
      "resolved_canonical": "Ensemble-based Fitness Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Multi-population Ensemble Genetic Programming via Cooperative Coevolution and Multi-view Learning for Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19339.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19339](https://arxiv.org/abs/2509.19339)

## 🔗 유사한 논문
- [[2025-09-23/GaussianPSL_ A novel framework based on Gaussian Splatting for exploring the Pareto frontier in multi-criteria optimization_20250923|GaussianPSL: A novel framework based on Gaussian Splatting for exploring the Pareto frontier in multi-criteria optimization]] (81.4% similar)
- [[2025-09-23/Geometric Mixture Classifier (GMC)_ A Discriminative Per-Class Mixture of Hyperplanes_20250923|Geometric Mixture Classifier (GMC): A Discriminative Per-Class Mixture of Hyperplanes]] (81.3% similar)
- [[2025-09-19/Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data_20250919|Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data]] (80.5% similar)
- [[2025-09-23/MCP_ A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models_20250923|MCP: A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models]] (80.3% similar)
- [[2025-09-23/Robust, Online, and Adaptive Decentralized Gaussian Processes_20250923|Robust, Online, and Adaptive Decentralized Gaussian Processes]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Cooperative Coevolution|Cooperative Coevolution]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Multi-population Ensemble Genetic Programming|Multi-population Ensemble Genetic Programming]], [[keywords/Ensemble-based Fitness Mechanism|Ensemble-based Fitness Mechanism]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19339v1 Announce Type: cross 
Abstract: This paper introduces Multi-population Ensemble Genetic Programming (MEGP), a computational intelligence framework that integrates cooperative coevolution and the multiview learning paradigm to address classification challenges in high-dimensional and heterogeneous feature spaces. MEGP decomposes the input space into conditionally independent feature subsets, enabling multiple subpopulations to evolve in parallel while interacting through a dynamic ensemble-based fitness mechanism. Each individual encodes multiple genes whose outputs are aggregated via a differentiable softmax-based weighting layer, enhancing both model interpretability and adaptive decision fusion. A hybrid selection mechanism incorporating both isolated and ensemble-level fitness promotes inter-population cooperation while preserving intra-population diversity. This dual-level evolutionary dynamic facilitates structured search exploration and reduces premature convergence. Experimental evaluations across eight benchmark datasets demonstrate that MEGP consistently outperforms a baseline GP model in terms of convergence behavior and generalization performance. Comprehensive statistical analyses validate significant improvements in Log-Loss, Precision, Recall, F1 score, and AUC. MEGP also exhibits robust diversity retention and accelerated fitness gains throughout evolution, highlighting its effectiveness for scalable, ensemble-driven evolutionary learning. By unifying population-based optimization, multi-view representation learning, and cooperative coevolution, MEGP contributes a structurally adaptive and interpretable framework that advances emerging directions in evolutionary machine learning.

## 📝 요약

이 논문은 고차원 및 이질적 특징 공간에서의 분류 문제를 해결하기 위해 협력적 공진화와 다중 관점 학습 패러다임을 통합한 다중 인구 앙상블 유전 프로그래밍(MEGP)을 소개합니다. MEGP는 입력 공간을 조건부 독립적인 특징 하위 집합으로 분해하여 여러 하위 인구가 병렬로 진화하도록 하며, 동적 앙상블 기반 피트니스 메커니즘을 통해 상호작용합니다. 각 개체는 여러 유전자를 인코딩하며, 이들의 출력은 소프트맥스 기반 가중치 레이어로 집계되어 모델 해석 가능성과 적응적 의사 결정 융합을 향상시킵니다. 실험 결과, MEGP는 기존 유전 프로그래밍 모델보다 수렴 행동과 일반화 성능에서 우수한 성과를 보였으며, 다양한 성능 지표에서 유의미한 개선을 확인했습니다. MEGP는 진화적 머신러닝의 새로운 방향을 제시하는 해석 가능하고 구조적으로 적응적인 프레임워크를 제공합니다.

## 🎯 주요 포인트

- 1. MEGP는 협력적 공동진화와 다중 관점 학습 패러다임을 통합하여 고차원 및 이질적 특징 공간에서의 분류 문제를 해결합니다.
- 2. 입력 공간을 조건부 독립적인 특징 하위 집합으로 분해하여 여러 하위 집단이 병렬로 진화하며 동적 앙상블 기반 적합도 메커니즘을 통해 상호작용합니다.
- 3. 하이브리드 선택 메커니즘은 개별 및 앙상블 수준의 적합도를 통합하여 집단 간 협력을 촉진하고 집단 내 다양성을 유지합니다.
- 4. 실험 결과, MEGP는 수렴 행동 및 일반화 성능 면에서 기존 GP 모델을 일관되게 능가하며, 다양한 성능 지표에서 유의미한 개선을 보였습니다.
- 5. MEGP는 진화 과정에서 강력한 다양성 유지 및 가속화된 적합도 향상을 보여주며, 진화적 기계 학습의 새로운 방향을 제시합니다.


---

*Generated on 2025-09-25 15:26:41*