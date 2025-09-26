---
keywords:
  - Multimodal Learning
  - Self-supervised Learning
  - Modality Fusion
  - Distribution Shift
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17492
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:59:54.133158",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Self-supervised Learning",
    "Modality Fusion",
    "Distribution Shift"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.8,
    "Self-supervised Learning": 0.85,
    "Modality Fusion": 0.78,
    "Distribution Shift": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Medical Image Classification",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal Image Classification"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is a trending concept that connects various modalities, enhancing the understanding of complex data structures.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Self-supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised Learning is crucial for leveraging unlabeled data, which is a key aspect of the proposed framework.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Modality Fusion",
        "canonical": "Modality Fusion",
        "aliases": [
          "Fusion of Modalities"
        ],
        "category": "unique_technical",
        "rationale": "Modality Fusion is a unique technical concept central to the paper's approach to integrating various data types.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Distribution Shift",
        "canonical": "Distribution Shift",
        "aliases": [
          "Shift in Distribution"
        ],
        "category": "unique_technical",
        "rationale": "Addressing Distribution Shift is essential for improving model robustness and reducing prediction uncertainty.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.76,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "pretraining",
      "fine-tuning",
      "baseline model",
      "extensive experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Medical Image Classification",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Self-supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Modality Fusion",
      "resolved_canonical": "Modality Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Distribution Shift",
      "resolved_canonical": "Distribution Shift",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.76,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Multimodal Medical Image Classification via Synergistic Learning Pre-training

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17492.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17492](https://arxiv.org/abs/2509.17492)

## 🔗 유사한 논문
- [[2025-09-22/Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture_20250922|Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture]] (84.3% similar)
- [[2025-09-22/Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays_20250922|Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays]] (83.7% similar)
- [[2025-09-22/UniMRSeg_ Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation_20250922|UniMRSeg: Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation]] (83.4% similar)
- [[2025-09-22/SLaM-DiMM_ Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI_20250922|SLaM-DiMM: Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI]] (83.4% similar)
- [[2025-09-22/RegionMed-CLIP_ A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding_20250922|RegionMed-CLIP: A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Modality Fusion|Modality Fusion]], [[keywords/Distribution Shift|Distribution Shift]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17492v1 Announce Type: cross 
Abstract: Multimodal pathological images are usually in clinical diagnosis, but computer vision-based multimodal image-assisted diagnosis faces challenges with modality fusion, especially in the absence of expert-annotated data. To achieve the modality fusion in multimodal images with label scarcity, we propose a novel ``pretraining + fine-tuning" framework for multimodal semi-supervised medical image classification. Specifically, we propose a synergistic learning pretraining framework of consistency, reconstructive, and aligned learning. By treating one modality as an augmented sample of another modality, we implement a self-supervised learning pre-train, enhancing the baseline model's feature representation capability. Then, we design a fine-tuning method for multimodal fusion. During the fine-tuning stage, we set different encoders to extract features from the original modalities and provide a multimodal fusion encoder for fusion modality. In addition, we propose a distribution shift method for multimodal fusion features, which alleviates the prediction uncertainty and overfitting risks caused by the lack of labeled samples. We conduct extensive experiments on the publicly available gastroscopy image datasets Kvasir and Kvasirv2. Quantitative and qualitative results demonstrate that the proposed method outperforms the current state-of-the-art classification methods. The code will be released at: https://github.com/LQH89757/MICS.

## 📝 요약

이 논문은 라벨이 부족한 다중 모달 병리 이미지를 효과적으로 융합하여 진단하는 방법을 제안합니다. 저자들은 '사전 학습 + 미세 조정' 프레임워크를 통해 일관성, 재구성, 정렬 학습을 결합한 시너지 학습을 제안합니다. 한 모달리티를 다른 모달리티의 증강 샘플로 간주하여 자가 지도 학습을 수행하고, 다양한 인코더를 통해 원본 모달리티의 특징을 추출하여 융합 모달리티를 생성합니다. 또한, 분포 이동 방법을 통해 라벨 부족으로 인한 예측 불확실성과 과적합 문제를 완화합니다. Kvasir와 Kvasirv2 데이터셋을 활용한 실험 결과, 제안된 방법이 기존의 최첨단 분류 방법보다 우수함을 입증했습니다.

## 🎯 주요 포인트

- 1. 본 연구는 레이블이 부족한 상황에서 다중 모달리티 이미지를 융합하기 위한 "사전 학습 + 미세 조정" 프레임워크를 제안합니다.
- 2. 제안된 프레임워크는 일관성, 재구성, 정렬 학습의 시너지적 학습 사전 훈련을 통해 특징 표현 능력을 향상시킵니다.
- 3. 미세 조정 단계에서는 원본 모달리티로부터 특징을 추출하는 인코더와 융합 모달리티를 위한 다중 모달리티 융합 인코더를 설계합니다.
- 4. 분포 변화 방법을 제안하여 레이블이 부족한 상황에서 발생할 수 있는 예측 불확실성과 과적합 위험을 완화합니다.
- 5. Kvasir 및 Kvasirv2 데이터셋을 활용한 실험 결과, 제안된 방법이 기존 최첨단 분류 방법보다 우수한 성능을 보였습니다.


---

*Generated on 2025-09-23 23:59:54*