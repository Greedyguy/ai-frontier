<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:15:53.119943",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Domain Adaptation",
    "Self-supervised Learning",
    "Pseudo-labels",
    "Frugal Labelling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.85,
    "Domain Adaptation": 0.82,
    "Self-supervised Learning": 0.8,
    "Pseudo-labels": 0.78,
    "Frugal Labelling": 0.77
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
        "rationale": "Federated Learning is a central theme in the paper, crucial for linking to distributed machine learning discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Domain Adaptation",
        "canonical": "Domain Adaptation",
        "aliases": [
          "DA"
        ],
        "category": "specific_connectable",
        "rationale": "Domain Adaptation is key for understanding cross-domain learning strategies discussed in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Self-supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised Learning is a method used in the paper's frugal-labelling pipeline, linking to broader discussions on efficient learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Pseudo-labels",
        "canonical": "Pseudo-labels",
        "aliases": [
          "Pseudo labeling"
        ],
        "category": "unique_technical",
        "rationale": "Pseudo-labels are a unique technique in the paper for guiding learner clients, relevant to semi-supervised learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.78
      },
      {
        "surface": "Frugal Labelling",
        "canonical": "Frugal Labelling",
        "aliases": [
          "Efficient Labelling"
        ],
        "category": "unique_technical",
        "rationale": "Frugal Labelling is a novel concept introduced in the paper, emphasizing label efficiency under constraints.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
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
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Domain Adaptation",
      "resolved_canonical": "Domain Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Self-supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Pseudo-labels",
      "resolved_canonical": "Pseudo-labels",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Frugal Labelling",
      "resolved_canonical": "Frugal Labelling",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# FedFusion: Federated Learning with Diversity- and Cluster-Aware Encoders for Robust Adaptation under Label Scarcity

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19220.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19220](https://arxiv.org/abs/2509.19220)

## 🔗 유사한 논문
- [[2025-09-24/FedFiTS_ Fitness-Selected, Slotted Client Scheduling for Trustworthy Federated Learning in Healthcare AI_20250924|FedFiTS: Fitness-Selected, Slotted Client Scheduling for Trustworthy Federated Learning in Healthcare AI]] (84.8% similar)
- [[2025-09-23/FedEL_ Federated Elastic Learning for Heterogeneous Devices_20250923|FedEL: Federated Elastic Learning for Heterogeneous Devices]] (83.9% similar)
- [[2025-09-18/Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning_20250918|Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning]] (83.8% similar)
- [[2025-09-19/FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT: Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (83.7% similar)
- [[2025-09-17/FedSSG_ Expectation-Gated and History-Aware Drift Alignment for Federated Learning_20250917|FedSSG: Expectation-Gated and History-Aware Drift Alignment for Federated Learning]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]]
**🔗 Specific Connectable**: [[keywords/Domain Adaptation|Domain Adaptation]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Pseudo-labels|Pseudo-labels]], [[keywords/Frugal Labelling|Frugal Labelling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19220v1 Announce Type: cross 
Abstract: Federated learning in practice must contend with heterogeneous feature spaces, severe non-IID data, and scarce labels across clients. We present FedFusion, a federated transfer-learning framework that unifies domain adaptation and frugal labelling with diversity-/cluster-aware encoders (DivEn, DivEn-mix, DivEn-c). Labelled teacher clients guide learner clients via confidence-filtered pseudo-labels and domain-adaptive transfer, while clients maintain personalised encoders tailored to local data. To preserve global coherence under heterogeneity, FedFusion employs similarity-weighted classifier coupling (with optional cluster-wise averaging), mitigating dominance by data-rich sites and improving minority-client performance. The frugal-labelling pipeline combines self-/semi-supervised pretext training with selective fine-tuning, reducing annotation demands without sharing raw data. Across tabular and imaging benchmarks under IID, non-IID, and label-scarce regimes, FedFusion consistently outperforms state-of-the-art baselines in accuracy, robustness, and fairness while maintaining comparable communication and computation budgets. These results show that harmonising personalisation, domain adaptation, and label efficiency is an effective recipe for robust federated learning under real-world constraints.

## 📝 요약

FedFusion은 이질적인 특징 공간, 심각한 비독립적 동일 분포(non-IID) 데이터, 그리고 클라이언트 간의 부족한 라벨 문제를 해결하기 위한 연합 학습 프레임워크입니다. 이 프레임워크는 도메인 적응과 절약형 라벨링을 다양성/클러스터 인식 인코더와 결합합니다. 라벨이 있는 교사 클라이언트는 학습자 클라이언트를 신뢰도 기반의 가짜 라벨과 도메인 적응 전이를 통해 안내하며, 클라이언트는 지역 데이터에 맞춘 개인화된 인코더를 유지합니다. FedFusion은 유사도 가중치 분류기 결합을 통해 데이터가 풍부한 사이트의 지배를 완화하고 소수 클라이언트의 성능을 개선합니다. 절약형 라벨링은 자가/반지도 학습과 선택적 미세 조정을 결합하여 주석 필요성을 줄입니다. 다양한 벤치마크에서 FedFusion은 정확성, 강건성, 공정성 면에서 최신 기법을 능가하며, 개인화, 도메인 적응, 라벨 효율성을 조화롭게 통합하여 현실적인 제약 하에서도 강력한 연합 학습을 가능하게 합니다.

## 🎯 주요 포인트

- 1. FedFusion은 이질적인 특징 공간과 심각한 비독립 동일 분포(non-IID) 데이터, 그리고 클라이언트 간의 희소한 레이블 문제를 해결하는 연합 전이 학습 프레임워크입니다.
- 2. FedFusion은 다양성 및 클러스터 인식 인코더를 사용하여 도메인 적응과 절약형 라벨링을 통합합니다.
- 3. 라벨이 있는 교사 클라이언트는 신뢰도 기반의 가짜 라벨과 도메인 적응 전이를 통해 학습자 클라이언트를 안내합니다.
- 4. FedFusion은 유사성 가중치 분류기 결합을 사용하여 데이터가 풍부한 사이트의 지배를 완화하고 소수 클라이언트의 성능을 향상시킵니다.
- 5. FedFusion은 다양한 벤치마크에서 최신 기법 대비 정확성, 견고성, 공정성 면에서 우수한 성능을 보이며, 통신 및 계산 비용도 유사하게 유지합니다.


---

*Generated on 2025-09-24 14:15:53*