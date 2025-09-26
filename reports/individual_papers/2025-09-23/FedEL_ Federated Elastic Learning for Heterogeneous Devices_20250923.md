---
keywords:
  - Federated Learning
  - Elastic Learning
  - Data Privacy
  - Heterogeneous Devices
  - Tensor Importance
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16902
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:37:36.463293",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Elastic Learning",
    "Data Privacy",
    "Heterogeneous Devices",
    "Tensor Importance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.78,
    "Elastic Learning": 0.72,
    "Data Privacy": 0.75,
    "Heterogeneous Devices": 0.7,
    "Tensor Importance": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Learning",
        "canonical": "Federated Learning",
        "aliases": [
          "FL"
        ],
        "category": "broad_technical",
        "rationale": "Federated Learning is a central theme of the paper and connects to distributed machine learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Elastic Learning",
        "canonical": "Elastic Learning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Elastic Learning is a novel concept introduced by the paper, focusing on adaptive training processes.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Data Privacy",
        "canonical": "Data Privacy",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Data Privacy is a critical aspect of Federated Learning, linking to privacy-preserving techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Heterogeneous Devices",
        "canonical": "Heterogeneous Devices",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The paper addresses challenges specific to heterogeneous devices, which is a unique technical focus.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      },
      {
        "surface": "Tensor Importance",
        "canonical": "Tensor Importance",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Tensor Importance is a specific technique proposed to improve model training efficiency.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.78,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "training process",
      "model accuracy",
      "experiment results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Elastic Learning",
      "resolved_canonical": "Elastic Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Data Privacy",
      "resolved_canonical": "Data Privacy",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Heterogeneous Devices",
      "resolved_canonical": "Heterogeneous Devices",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Tensor Importance",
      "resolved_canonical": "Tensor Importance",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.78,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# FedEL: Federated Elastic Learning for Heterogeneous Devices

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16902.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16902](https://arxiv.org/abs/2509.16902)

## 🔗 유사한 논문
- [[2025-09-19/FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT: Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (84.4% similar)
- [[2025-09-18/Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning_20250918|Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning]] (82.3% similar)
- [[2025-09-22/Towards Communication-efficient Federated Learning via Sparse and Aligned Adaptive Optimization_20250922|Towards Communication-efficient Federated Learning via Sparse and Aligned Adaptive Optimization]] (81.9% similar)
- [[2025-09-19/Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning]] (81.7% similar)
- [[2025-09-19/Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]]
**🔗 Specific Connectable**: [[keywords/Data Privacy|Data Privacy]]
**⚡ Unique Technical**: [[keywords/Elastic Learning|Elastic Learning]], [[keywords/Heterogeneous Devices|Heterogeneous Devices]], [[keywords/Tensor Importance|Tensor Importance]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16902v1 Announce Type: cross 
Abstract: Federated learning (FL) enables distributed devices to collaboratively train machine learning models while maintaining data privacy. However, the heterogeneous hardware capabilities of devices often result in significant training delays, as straggler clients with limited resources prolong the aggregation process. Existing solutions such as client selection, asynchronous FL, and partial training partially address these challenges but encounter issues such as reduced accuracy, stale updates, and compromised model performance due to inconsistent training contributions. To overcome these limitations, we propose FedEL, a federated elastic learning framework that enhances training efficiency while maintaining model accuracy. FedEL introduces a novel window-based training process, sliding the window to locate the training part of the model and dynamically selecting important tensors for training within a coordinated runtime budget. This approach ensures progressive and balanced training across all clients, including stragglers. Additionally, FedEL employs a tensor importance adjustment module, harmonizing local and global tensor importance to mitigate biases caused by data heterogeneity. The experiment results show that FedEL achieves up to 3.87x improvement in time-to-accuracy compared to baselines while maintaining or exceeding final test accuracy.

## 📝 요약

연합 학습(FL)은 데이터 프라이버시를 유지하면서 분산된 장치들이 협력하여 기계 학습 모델을 훈련할 수 있게 합니다. 그러나 장치의 이질적인 하드웨어 성능 때문에 훈련 지연이 발생하는 문제가 있습니다. 기존 해결책들은 정확도 저하, 업데이트 지연 등의 문제를 겪습니다. 이를 해결하기 위해, 우리는 FedEL이라는 연합 탄력 학습 프레임워크를 제안합니다. FedEL은 창 기반 훈련 과정을 도입하여 모델의 중요한 텐서를 동적으로 선택하고, 모든 클라이언트에서 균형 잡힌 훈련을 보장합니다. 또한, 텐서 중요도 조정 모듈을 통해 데이터 이질성으로 인한 편향을 완화합니다. 실험 결과, FedEL은 기존 방법에 비해 최대 3.87배의 시간 효율성을 보이며, 최종 테스트 정확도를 유지하거나 초과합니다.

## 🎯 주요 포인트

- 1. FedEL은 이질적인 하드웨어 성능을 가진 장치들 간의 훈련 지연 문제를 해결하기 위해 제안된 연합 학습 프레임워크입니다.
- 2. FedEL은 창 기반 훈련 프로세스를 도입하여 모델의 훈련 부분을 동적으로 선택하고 중요한 텐서를 훈련하는 방식으로 훈련 효율성을 향상시킵니다.
- 3. 텐서 중요도 조정 모듈을 통해 데이터 이질성으로 인한 편향을 완화하고, 모든 클라이언트에서 점진적이고 균형 잡힌 훈련을 보장합니다.
- 4. 실험 결과, FedEL은 기존 방법들에 비해 최대 3.87배 빠른 시간 내에 정확도를 달성하면서도 최종 테스트 정확도를 유지하거나 초과합니다.


---

*Generated on 2025-09-23 23:37:36*