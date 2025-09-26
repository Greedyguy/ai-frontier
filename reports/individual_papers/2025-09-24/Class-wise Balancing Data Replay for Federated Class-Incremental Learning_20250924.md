<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:26:18.241081",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Class Incremental Learning",
    "Data Replay",
    "Class Imbalance",
    "Temperature Scaling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Class Incremental Learning": 0.78,
    "Data Replay": 0.81,
    "Class Imbalance": 0.77,
    "Temperature Scaling": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Class Incremental Learning",
        "canonical": "Federated Class Incremental Learning",
        "aliases": [
          "FCIL"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific approach within federated learning that addresses class incrementality, making it highly relevant for linking to related research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "data replay",
        "canonical": "Data Replay",
        "aliases": [
          "replay buffer"
        ],
        "category": "specific_connectable",
        "rationale": "Data replay is a crucial technique in mitigating forgetting in incremental learning, connecting well with memory and learning strategies.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.81
      },
      {
        "surface": "class imbalance",
        "canonical": "Class Imbalance",
        "aliases": [
          "imbalanced classes"
        ],
        "category": "specific_connectable",
        "rationale": "Class imbalance is a common issue in machine learning that affects model performance, linking to various balancing techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.68,
        "link_intent_score": 0.77
      },
      {
        "surface": "temperature scaling",
        "canonical": "Temperature Scaling",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Temperature scaling is a technique used to calibrate model predictions, relevant for linking to methods addressing model confidence.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Class Incremental Learning",
      "resolved_canonical": "Federated Class Incremental Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "data replay",
      "resolved_canonical": "Data Replay",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "class imbalance",
      "resolved_canonical": "Class Imbalance",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.68,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "temperature scaling",
      "resolved_canonical": "Temperature Scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Class-wise Balancing Data Replay for Federated Class-Incremental Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.07712.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2507.07712](https://arxiv.org/abs/2507.07712)

## 🔗 유사한 논문
- [[2025-09-24/FedFusion_ Federated Learning with Diversity- and Cluster-Aware Encoders for Robust Adaptation under Label Scarcity_20250924|FedFusion: Federated Learning with Diversity- and Cluster-Aware Encoders for Robust Adaptation under Label Scarcity]] (82.0% similar)
- [[2025-09-17/FedSSG_ Expectation-Gated and History-Aware Drift Alignment for Federated Learning_20250917|FedSSG: Expectation-Gated and History-Aware Drift Alignment for Federated Learning]] (80.6% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (80.5% similar)
- [[2025-09-23/Intra-Cluster Mixup_ An Effective Data Augmentation Technique for Complementary-Label Learning_20250923|Intra-Cluster Mixup: An Effective Data Augmentation Technique for Complementary-Label Learning]] (80.3% similar)
- [[2025-09-23/Min_ Mixture of Noise for Pre-Trained Model-Based Class-Incremental Learning_20250923|Min: Mixture of Noise for Pre-Trained Model-Based Class-Incremental Learning]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Data Replay|Data Replay]], [[keywords/Class Imbalance|Class Imbalance]], [[keywords/Temperature Scaling|Temperature Scaling]]
**⚡ Unique Technical**: [[keywords/Federated Class Incremental Learning|Federated Class Incremental Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.07712v2 Announce Type: replace 
Abstract: Federated Class Incremental Learning (FCIL) aims to collaboratively process continuously increasing incoming tasks across multiple clients. Among various approaches, data replay has become a promising solution, which can alleviate forgetting by reintroducing representative samples from previous tasks. However, their performance is typically limited by class imbalance, both within the replay buffer due to limited global awareness and between replayed and newly arrived classes. To address this issue, we propose a class wise balancing data replay method for FCIL (FedCBDR), which employs a global coordination mechanism for class-level memory construction and reweights the learning objective to alleviate the aforementioned imbalances. Specifically, FedCBDR has two key components: 1) the global-perspective data replay module reconstructs global representations of prior task in a privacy-preserving manner, which then guides a class-aware and importance-sensitive sampling strategy to achieve balanced replay; 2) Subsequently, to handle class imbalance across tasks, the task aware temperature scaling module adaptively adjusts the temperature of logits at both class and instance levels based on task dynamics, which reduces the model's overconfidence in majority classes while enhancing its sensitivity to minority classes. Experimental results verified that FedCBDR achieves balanced class-wise sampling under heterogeneous data distributions and improves generalization under task imbalance between earlier and recent tasks, yielding a 2%-15% Top-1 accuracy improvement over six state-of-the-art methods.

## 📝 요약

연합 클래스 증분 학습(FCIL)은 여러 클라이언트 간에 지속적으로 증가하는 작업을 협력적으로 처리하는 것을 목표로 합니다. 데이터 재생은 이전 작업의 대표 샘플을 재도입하여 망각을 완화하는 유망한 솔루션으로 떠올랐지만, 클래스 불균형으로 인해 성능이 제한됩니다. 이를 해결하기 위해, 우리는 클래스별 균형 데이터 재생 방법인 FedCBDR을 제안합니다. FedCBDR은 클래스 수준의 메모리 구축을 위한 글로벌 조정 메커니즘을 사용하고, 학습 목표를 재조정하여 불균형을 완화합니다. 주요 구성 요소로는 1) 글로벌 관점의 데이터 재생 모듈이 있으며, 이는 이전 작업의 글로벌 표현을 프라이버시를 보호하면서 재구성하고, 클래스 인식 및 중요도 민감 샘플링 전략을 통해 균형 잡힌 재생을 달성합니다. 2) 작업 인식 온도 조정 모듈은 작업 역학에 따라 클래스 및 인스턴스 수준에서 로짓의 온도를 조정하여 다수 클래스에 대한 모델의 과신을 줄이고 소수 클래스에 대한 민감도를 높입니다. 실험 결과, FedCBDR은 이질적인 데이터 분포에서 균형 잡힌 클래스별 샘플링을 달성하고, 초기 및 최근 작업 간의 불균형을 개선하여 6가지 최첨단 방법 대비 2%-15%의 Top-1 정확도 향상을 보였습니다.

## 🎯 주요 포인트

- 1. 연합 클래스 증분 학습(FCIL)은 여러 클라이언트에서 지속적으로 증가하는 작업을 협력적으로 처리하는 것을 목표로 한다.
- 2. 데이터 리플레이는 이전 작업의 대표 샘플을 재도입하여 망각을 완화하는 유망한 솔루션으로 부상했다.
- 3. FedCBDR은 클래스 수준 메모리 구축을 위한 글로벌 조정 메커니즘을 사용하여 클래스 불균형 문제를 해결한다.
- 4. FedCBDR의 글로벌 관점 데이터 리플레이 모듈은 프라이버시를 보장하면서 이전 작업의 글로벌 표현을 재구성한다.
- 5. FedCBDR은 6개의 최신 방법에 비해 2%-15%의 Top-1 정확도 향상을 달성했다.


---

*Generated on 2025-09-24 15:26:18*