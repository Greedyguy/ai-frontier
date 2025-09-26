---
keywords:
  - Federated Learning
  - Size-Based Adaptive Federated Learning
  - Multimodal Learning
  - Communication Efficiency
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.20685
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:09:21.085291",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Size-Based Adaptive Federated Learning",
    "Multimodal Learning",
    "Communication Efficiency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.85,
    "Size-Based Adaptive Federated Learning": 0.8,
    "Multimodal Learning": 0.82,
    "Communication Efficiency": 0.75
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
        "rationale": "Federated Learning is central to the paper's theme and is a key concept in distributed machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Size-Based Adaptive Federated Learning",
        "canonical": "Size-Based Adaptive Federated Learning",
        "aliases": [
          "SAFL"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced by the paper, offering a unique approach to federated learning based on dataset size.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Heterogeneous Multi-Modal Data",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multi-Modal Data"
        ],
        "category": "specific_connectable",
        "rationale": "The paper addresses learning across multiple data modalities, making it relevant to the concept of Multimodal Learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Communication Efficiency",
        "canonical": "Communication Efficiency",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Communication efficiency is a critical aspect of federated learning systems, especially in reducing data transfer.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "dataset size",
      "performance hierarchy",
      "real-time monitoring"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Size-Based Adaptive Federated Learning",
      "resolved_canonical": "Size-Based Adaptive Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Heterogeneous Multi-Modal Data",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Communication Efficiency",
      "resolved_canonical": "Communication Efficiency",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Progressive Size-Adaptive Federated Learning: A Comprehensive Framework for Heterogeneous Multi-Modal Data Systems

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.20685.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.20685](https://arxiv.org/abs/2506.20685)

## 🔗 유사한 논문
- [[2025-09-19/Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning]] (83.9% similar)
- [[2025-09-18/Towards Privacy-Preserving and Heterogeneity-aware Split Federated Learning via Probabilistic Masking_20250918|Towards Privacy-Preserving and Heterogeneity-aware Split Federated Learning via Probabilistic Masking]] (83.8% similar)
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (82.8% similar)
- [[2025-09-19/FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT: Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (82.7% similar)
- [[2025-09-19/Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Size-Based Adaptive Federated Learning|Size-Based Adaptive Federated Learning]], [[keywords/Communication Efficiency|Communication Efficiency]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.20685v2 Announce Type: replace-cross 
Abstract: Federated Learning (FL) has emerged as a transformative paradigm for distributed machine learning while preserving data privacy. However, existing approaches predominantly focus on model heterogeneity and aggregation techniques, largely overlooking the fundamental impact of dataset size characteristics on federated training dynamics. This paper introduces Size-Based Adaptive Federated Learning (SAFL), a novel progressive training framework that systematically organizes federated learning based on dataset size characteristics across heterogeneous multi-modal data. Our comprehensive experimental evaluation across 13 diverse datasets spanning 7 modalities (vision, text, time series, audio, sensor, medical vision, and multimodal) reveals critical insights: 1) an optimal dataset size range of 1000-1500 samples for federated learning effectiveness; 2) a clear modality performance hierarchy with structured data (time series, sensor) significantly outperforming unstructured data (text, multimodal); and 3) systematic performance degradation for large datasets exceeding 2000 samples. SAFL achieves an average accuracy of 87.68% across all datasets, with structured data modalities reaching 99%+ accuracy. The framework demonstrates superior communication efficiency, reducing total data transfer to 7.38 GB across 558 communications while maintaining high performance. Our real-time monitoring framework provides unprecedented insights into system resource utilization, network efficiency, and training dynamics. This work fills critical gaps in understanding how data characteristics should drive federated learning strategies, providing both theoretical insights and practical guidance for real-world FL deployments in neural network and learning systems.

## 📝 요약

이 논문은 데이터 크기 특성이 연합 학습에 미치는 영향을 분석하는 새로운 접근법인 크기 기반 적응 연합 학습(SAFL)을 제안합니다. 13개의 다양한 데이터셋을 대상으로 한 실험 결과, 연합 학습에 가장 효과적인 데이터셋 크기는 1000-1500 샘플이며, 구조화된 데이터(예: 시계열, 센서)가 비구조화된 데이터(예: 텍스트, 멀티모달)보다 성능이 우수하다는 점을 발견했습니다. 또한, 2000 샘플을 초과하는 대규모 데이터셋에서는 성능 저하가 발생했습니다. SAFL은 평균 87.68%의 정확도를 달성했으며, 구조화된 데이터에서는 99% 이상의 정확도를 기록했습니다. 이 프레임워크는 통신 효율성을 높여 총 데이터 전송량을 7.38GB로 줄이면서도 높은 성능을 유지합니다. 이 연구는 데이터 특성이 연합 학습 전략에 어떻게 영향을 미치는지를 이해하는 데 중요한 통찰을 제공하며, 실제 연합 학습 시스템 구현에 대한 이론적 및 실용적 지침을 제시합니다.

## 🎯 주요 포인트

- 1. SAFL은 데이터셋 크기 특성에 기반하여 연합 학습을 체계적으로 조직하는 새로운 진행형 학습 프레임워크입니다.
- 2. 연합 학습의 효과적인 데이터셋 크기 범위는 1000-1500 샘플로 나타났습니다.
- 3. 구조화된 데이터(시계열, 센서)가 비구조화된 데이터(텍스트, 멀티모달)보다 성능이 우수합니다.
- 4. 2000 샘플을 초과하는 대규모 데이터셋에서는 성능 저하가 체계적으로 발생합니다.
- 5. SAFL은 모든 데이터셋에서 평균 87.68%의 정확도를 달성하며, 구조화된 데이터 모달리티는 99% 이상의 정확도를 기록합니다.


---

*Generated on 2025-09-24 01:09:21*