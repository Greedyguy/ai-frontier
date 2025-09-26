---
keywords:
  - Dataset Distillation
  - Synthetic Datasets
  - Decoupled Dataset Distillation
  - Evaluation Protocols
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19743
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:05:05.911843",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dataset Distillation",
    "Synthetic Datasets",
    "Decoupled Dataset Distillation",
    "Evaluation Protocols"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dataset Distillation": 0.78,
    "Synthetic Datasets": 0.75,
    "Decoupled Dataset Distillation": 0.77,
    "Evaluation Protocols": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Dataset Distillation",
        "canonical": "Dataset Distillation",
        "aliases": [
          "Data Distillation"
        ],
        "category": "unique_technical",
        "rationale": "Dataset Distillation is a core concept of the paper, focusing on generating compact datasets, which is crucial for linking to related work in data efficiency.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Synthetic Datasets",
        "canonical": "Synthetic Datasets",
        "aliases": [
          "Artificial Datasets"
        ],
        "category": "specific_connectable",
        "rationale": "Synthetic Datasets are central to the paper's methodology, providing a link to discussions on data generation techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Decoupled Dataset Distillation",
        "canonical": "Decoupled Dataset Distillation",
        "aliases": [
          "Decoupled Distillation"
        ],
        "category": "unique_technical",
        "rationale": "This approach is a novel method discussed in the paper, highlighting a specific technique for dataset distillation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Post-Evaluation Protocols",
        "canonical": "Evaluation Protocols",
        "aliases": [
          "Post-Evaluation Methods"
        ],
        "category": "specific_connectable",
        "rationale": "Evaluation protocols are critical for assessing the effectiveness of dataset distillation methods, linking to broader discussions on evaluation standards.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method",
      "test accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Dataset Distillation",
      "resolved_canonical": "Dataset Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Synthetic Datasets",
      "resolved_canonical": "Synthetic Datasets",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Decoupled Dataset Distillation",
      "resolved_canonical": "Decoupled Dataset Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Post-Evaluation Protocols",
      "resolved_canonical": "Evaluation Protocols",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Rectified Decoupled Dataset Distillation: A Closer Look for Fair and Comprehensive Evaluation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19743.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19743](https://arxiv.org/abs/2509.19743)

## 🔗 유사한 논문
- [[2025-09-23/DD-Ranking_ Rethinking the Evaluation of Dataset Distillation_20250923|DD-Ranking: Rethinking the Evaluation of Dataset Distillation]] (90.2% similar)
- [[2025-09-22/Efficient Multimodal Dataset Distillation via Generative Models_20250922|Efficient Multimodal Dataset Distillation via Generative Models]] (83.8% similar)
- [[2025-09-22/RMT-KD_ Random Matrix Theoretic Causal Knowledge Distillation_20250922|RMT-KD: Random Matrix Theoretic Causal Knowledge Distillation]] (82.4% similar)
- [[2025-09-23/RCTDistill_ Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion_20250923|RCTDistill: Cross-Modal Knowledge Distillation Framework for Radar-Camera 3D Object Detection with Temporal Fusion]] (81.7% similar)
- [[2025-09-24/"What is Different Between These Datasets?" A Framework for Explaining Data Distribution Shifts_20250924|"What is Different Between These Datasets?" A Framework for Explaining Data Distribution Shifts]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Synthetic Datasets|Synthetic Datasets]], [[keywords/Evaluation Protocols|Evaluation Protocols]]
**⚡ Unique Technical**: [[keywords/Dataset Distillation|Dataset Distillation]], [[keywords/Decoupled Dataset Distillation|Decoupled Dataset Distillation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19743v1 Announce Type: new 
Abstract: Dataset distillation aims to generate compact synthetic datasets that enable models trained on them to achieve performance comparable to those trained on full real datasets, while substantially reducing storage and computational costs. Early bi-level optimization methods (e.g., MTT) have shown promising results on small-scale datasets, but their scalability is limited by high computational overhead. To address this limitation, recent decoupled dataset distillation methods (e.g., SRe$^2$L) separate the teacher model pre-training from the synthetic data generation process. These methods also introduce random data augmentation and epoch-wise soft labels during the post-evaluation phase to improve performance and generalization. However, existing decoupled distillation methods suffer from inconsistent post-evaluation protocols, which hinders progress in the field. In this work, we propose Rectified Decoupled Dataset Distillation (RD$^3$), and systematically investigate how different post-evaluation settings affect test accuracy. We further examine whether the reported performance differences across existing methods reflect true methodological advances or stem from discrepancies in evaluation procedures. Our analysis reveals that much of the performance variation can be attributed to inconsistent evaluation rather than differences in the intrinsic quality of the synthetic data. In addition, we identify general strategies that improve the effectiveness of distilled datasets across settings. By establishing a standardized benchmark and rigorous evaluation protocol, RD$^3$ provides a foundation for fair and reproducible comparisons in future dataset distillation research.

## 📝 요약

데이터셋 증류는 모델이 전체 실제 데이터셋이 아닌 압축된 합성 데이터셋으로도 유사한 성능을 내도록 하는 방법입니다. 초기 이중 최적화 방법은 소규모 데이터셋에서 유망한 결과를 보였으나, 높은 계산 비용으로 확장성에 한계가 있었습니다. 이를 해결하기 위해 최근 분리된 데이터셋 증류 방법은 교사 모델의 사전 훈련과 합성 데이터 생성 과정을 분리하고, 성능 향상을 위해 무작위 데이터 증강과 에포크별 소프트 라벨을 도입했습니다. 그러나 기존 방법들은 일관되지 않은 평가 프로토콜로 인해 발전에 어려움을 겪고 있습니다. 본 연구에서는 Rectified Decoupled Dataset Distillation (RD$^3$)을 제안하고, 다양한 평가 설정이 테스트 정확도에 미치는 영향을 체계적으로 조사했습니다. 분석 결과, 성능 차이의 대부분은 평가 절차의 불일치에서 비롯되었음을 확인했습니다. 또한, 증류된 데이터셋의 효과를 높이는 일반적인 전략을 제시하며, RD$^3$은 공정하고 재현 가능한 비교를 위한 표준화된 벤치마크와 평가 프로토콜을 제공합니다.

## 🎯 주요 포인트

- 1. 데이터셋 증류는 저장 및 계산 비용을 줄이면서도 전체 실제 데이터셋으로 훈련된 모델과 유사한 성능을 달성할 수 있는 압축된 합성 데이터셋을 생성하는 것을 목표로 합니다.
- 2. 초기 이중 최적화 방법은 소규모 데이터셋에서 유망한 결과를 보였으나, 높은 계산 오버헤드로 인해 확장성에 한계가 있습니다.
- 3. 최근의 분리된 데이터셋 증류 방법은 교사 모델의 사전 훈련과 합성 데이터 생성 과정을 분리하여 성능과 일반화를 개선합니다.
- 4. 기존의 분리된 증류 방법은 일관되지 않은 사후 평가 프로토콜로 인해 발전에 장애가 되고 있습니다.
- 5. RD$^3$는 표준화된 벤치마크와 엄격한 평가 프로토콜을 수립하여 데이터셋 증류 연구에서 공정하고 재현 가능한 비교를 위한 기초를 제공합니다.


---

*Generated on 2025-09-26 09:05:05*