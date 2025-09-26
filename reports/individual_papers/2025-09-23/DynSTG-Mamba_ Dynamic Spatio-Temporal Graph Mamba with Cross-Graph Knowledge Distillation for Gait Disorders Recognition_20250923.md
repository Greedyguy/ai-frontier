---
keywords:
  - Graph Neural Network
  - Cross-Graph Relational Knowledge Distillation
  - Gait Disorder Recognition
  - Dynamic Spatio-Temporal Filter
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2503.13156
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:19:59.772610",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Cross-Graph Relational Knowledge Distillation",
    "Gait Disorder Recognition",
    "Dynamic Spatio-Temporal Filter"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.8,
    "Cross-Graph Relational Knowledge Distillation": 0.78,
    "Gait Disorder Recognition": 0.75,
    "Dynamic Spatio-Temporal Filter": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "spatio-temporal graph convolutional networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "ST-GCN",
          "spatio-temporal GCN"
        ],
        "category": "specific_connectable",
        "rationale": "This term is directly related to Graph Neural Networks, which are crucial for modeling spatio-temporal data.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Cross-Graph Relational Knowledge Distillation",
        "canonical": "Cross-Graph Relational Knowledge Distillation",
        "aliases": [
          "CGRKD"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique introduced in the paper, enhancing knowledge transfer between models.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "gait disorder recognition",
        "canonical": "Gait Disorder Recognition",
        "aliases": [
          "gait analysis",
          "movement disorder assessment"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area of the proposed framework, linking to medical and clinical research.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.81,
        "link_intent_score": 0.75
      },
      {
        "surface": "dynamic spatio-temporal filter",
        "canonical": "Dynamic Spatio-Temporal Filter",
        "aliases": [
          "DSTF"
        ],
        "category": "unique_technical",
        "rationale": "This filter is a key component of the proposed model, enhancing feature propagation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.79,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "motion sequence",
      "model parameters",
      "computational costs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "spatio-temporal graph convolutional networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Cross-Graph Relational Knowledge Distillation",
      "resolved_canonical": "Cross-Graph Relational Knowledge Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "gait disorder recognition",
      "resolved_canonical": "Gait Disorder Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.81,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "dynamic spatio-temporal filter",
      "resolved_canonical": "Dynamic Spatio-Temporal Filter",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.79,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# DynSTG-Mamba: Dynamic Spatio-Temporal Graph Mamba with Cross-Graph Knowledge Distillation for Gait Disorders Recognition

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2503.13156.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2503.13156](https://arxiv.org/abs/2503.13156)

## 🔗 유사한 논문
- [[2025-09-23/CGTGait_ Collaborative Graph and Transformer for Gait Emotion Recognition_20250923|CGTGait: Collaborative Graph and Transformer for Gait Emotion Recognition]] (85.8% similar)
- [[2025-09-23/Explainable Gait Abnormality Detection Using Dual-Dataset CNN-LSTM Models_20250923|Explainable Gait Abnormality Detection Using Dual-Dataset CNN-LSTM Models]] (85.6% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (83.4% similar)
- [[2025-09-18/LSTC-MDA_ A Unified Framework for Long-Short Term Temporal Convolution and Mixed Data Augmentation in Skeleton-Based Action Recognition_20250918|LSTC-MDA: A Unified Framework for Long-Short Term Temporal Convolution and Mixed Data Augmentation in Skeleton-Based Action Recognition]] (83.2% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Cross-Graph Relational Knowledge Distillation|Cross-Graph Relational Knowledge Distillation]], [[keywords/Gait Disorder Recognition|Gait Disorder Recognition]], [[keywords/Dynamic Spatio-Temporal Filter|Dynamic Spatio-Temporal Filter]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.13156v2 Announce Type: replace 
Abstract: Gait disorder recognition plays a crucial role in the early diagnosis and monitoring of movement disorders. Existing approaches, including spatio-temporal graph convolutional networks (ST-GCNs), often face high memory demands and struggle to capture complex spatio-temporal dependencies, limiting their efficiency in clinical applications. To address these challenges, we introduce DynSTG-Mamba (Dynamic Spatio-Temporal Graph Mamba), a novel framework that combines DF-STGNN and STG-Mamba to enhance motion sequence modeling. The DF-STGNN incorporates a dynamic spatio-temporal filter that adaptively adjusts spatial connections between skeletal joints and temporal interactions across different movement phases. This approach ensures better feature propagation through dynamic graph structures by considering the hierarchical nature and dynamics of skeletal gait data. Meanwhile, STG-Mamba, an extension of Mamba adapted for skeletal motion data, ensures a continuous propagation of states, facilitating the capture of long-term dependencies while reducing computational complexity. To reduce the number of model parameters and computational costs while maintaining consistency, we propose Cross-Graph Relational Knowledge Distillation, a novel knowledge transfer mechanism that aligns relational information between teacher (large architecture) and student models (small architecture) while using shared memory. This ensures that the interactions and movement patterns of the joints are accurately preserved in the motion sequences. We validate our DynSTG-Mamba on KOA-NM, PD-WALK, and ATAXIA datasets, where it outperforms state-of-the-art approaches by achieving in terms of Accuracy, F1-score, and Recall. Our results highlight the efficiency and robustness of our approach, offering a lightweight yet highly accurate solution for automated gait analysis and movement disorder assessment.

## 📝 요약

이 논문은 움직임 장애의 조기 진단 및 모니터링을 위한 걸음걸이 장애 인식에 관한 연구로, 기존 방법의 메모리 요구량과 복잡한 시공간 의존성 문제를 해결하기 위해 DynSTG-Mamba라는 새로운 프레임워크를 제안합니다. 이 프레임워크는 DF-STGNN과 STG-Mamba를 결합하여 동적 시공간 필터를 통해 골격 관절 간의 공간적 연결과 다양한 움직임 단계 간의 상호작용을 적응적으로 조정합니다. 또한, Cross-Graph Relational Knowledge Distillation을 통해 대형 모델과 소형 모델 간의 관계 정보를 정렬하여 모델의 효율성을 높입니다. KOA-NM, PD-WALK, ATAXIA 데이터셋에서의 실험 결과, DynSTG-Mamba는 정확도, F1-스코어, 재현율 측면에서 최첨단 방법들을 능가하며, 경량화된 고정밀 자동 걸음걸이 분석 및 움직임 장애 평가 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. DynSTG-Mamba는 DF-STGNN과 STG-Mamba를 결합하여 동작 시퀀스 모델링을 향상시키는 새로운 프레임워크입니다.
- 2. DF-STGNN은 동적 시공간 필터를 사용하여 골격 관절 간의 공간적 연결과 다양한 움직임 단계 간의 시간적 상호작용을 적응적으로 조정합니다.
- 3. STG-Mamba는 골격 운동 데이터에 맞게 확장된 Mamba로, 상태의 지속적인 전파를 통해 장기 의존성을 포착하면서 계산 복잡성을 줄입니다.
- 4. Cross-Graph Relational Knowledge Distillation은 대규모 모델과 소규모 모델 간의 관계 정보를 정렬하여 일관성을 유지하면서 모델 파라미터 수와 계산 비용을 줄입니다.
- 5. DynSTG-Mamba는 KOA-NM, PD-WALK, ATAXIA 데이터셋에서 정확도, F1-스코어, 리콜 측면에서 최신 기법들을 능가하는 성능을 보였습니다.


---

*Generated on 2025-09-24 05:19:59*