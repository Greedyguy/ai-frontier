<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:57:09.648554",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Self-supervised Learning",
    "Modality Dropout",
    "Disease Detection and Prediction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Self-supervised Learning": 0.83,
    "Modality Dropout": 0.78,
    "Disease Detection and Prediction": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "multimodal learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "multimodal fusion",
          "multimodal framework"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is central to the paper's approach, linking to a trending concept with high connectivity in current research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "contrastive learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "contrastive objectives"
        ],
        "category": "specific_connectable",
        "rationale": "Contrastive learning is a form of self-supervised learning, which is a key technique discussed in the paper.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.83
      },
      {
        "surface": "modality dropout",
        "canonical": "Modality Dropout",
        "aliases": [
          "enhanced modality dropout"
        ],
        "category": "unique_technical",
        "rationale": "Modality Dropout is a unique technique introduced in the paper, enhancing robustness to missing data.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "disease detection and prediction",
        "canonical": "Disease Detection and Prediction",
        "aliases": [
          "clinical prediction",
          "medical diagnosis"
        ],
        "category": "unique_technical",
        "rationale": "This is the primary application domain of the paper, linking to healthcare-focused research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experimental results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "multimodal learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "contrastive learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.83
      }
    },
    {
      "candidate_surface": "modality dropout",
      "resolved_canonical": "Modality Dropout",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "disease detection and prediction",
      "resolved_canonical": "Disease Detection and Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Learning Contrastive Multimodal Fusion with Improved Modality Dropout for Disease Detection and Prediction

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18284.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18284](https://arxiv.org/abs/2509.18284)

## 🔗 유사한 논문
- [[2025-09-23/Multimodal Medical Image Classification via Synergistic Learning Pre-training_20250923|Multimodal Medical Image Classification via Synergistic Learning Pre-training]] (87.8% similar)
- [[2025-09-22/DAFTED_ Decoupled Asymmetric Fusion of Tabular and Echocardiographic Data for Cardiac Hypertension Diagnosis_20250922|DAFTED: Decoupled Asymmetric Fusion of Tabular and Echocardiographic Data for Cardiac Hypertension Diagnosis]] (87.0% similar)
- [[2025-09-22/Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture_20250922|Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture]] (86.8% similar)
- [[2025-09-23/Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis_20250923|Multi-View Contrastive Learning for Robust Domain Adaptation in Medical Time Series Analysis]] (86.3% similar)
- [[2025-09-23/Causal Representation Learning from Multimodal Clinical Records under Non-Random Modality Missingness_20250923|Causal Representation Learning from Multimodal Clinical Records under Non-Random Modality Missingness]] (85.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Modality Dropout|Modality Dropout]], [[keywords/Disease Detection and Prediction|Disease Detection and Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18284v1 Announce Type: new 
Abstract: As medical diagnoses increasingly leverage multimodal data, machine learning models are expected to effectively fuse heterogeneous information while remaining robust to missing modalities. In this work, we propose a novel multimodal learning framework that integrates enhanced modalities dropout and contrastive learning to address real-world limitations such as modality imbalance and missingness. Our approach introduces learnable modality tokens for improving missingness-aware fusion of modalities and augments conventional unimodal contrastive objectives with fused multimodal representations. We validate our framework on large-scale clinical datasets for disease detection and prediction tasks, encompassing both visual and tabular modalities. Experimental results demonstrate that our method achieves state-of-the-art performance, particularly in challenging and practical scenarios where only a single modality is available. Furthermore, we show its adaptability through successful integration with a recent CT foundation model. Our findings highlight the effectiveness, efficiency, and generalizability of our approach for multimodal learning, offering a scalable, low-cost solution with significant potential for real-world clinical applications. The code is available at https://github.com/omron-sinicx/medical-modality-dropout.

## 📝 요약

이 논문은 의료 진단에서 멀티모달 데이터를 효과적으로 융합하고 누락된 모달리티에 강인한 기계 학습 모델을 제안합니다. 제안된 프레임워크는 모달리티 드롭아웃과 대조 학습을 통합하여 모달리티 불균형과 누락 문제를 해결합니다. 학습 가능한 모달리티 토큰을 도입하여 모달리티 융합을 개선하고, 단일 모달리티 대조 목표를 융합된 멀티모달 표현으로 확장합니다. 대규모 임상 데이터셋을 통해 실험한 결과, 특히 단일 모달리티만 사용 가능한 상황에서 최첨단 성능을 보였습니다. 또한, 최신 CT 모델과의 통합을 통해 적응성을 입증했습니다. 이 접근법은 멀티모달 학습의 효율성과 일반화 가능성을 강조하며, 실제 임상 응용에 잠재력을 제공합니다.

## 🎯 주요 포인트

- 1. 본 연구는 의료 진단에서 모달리티 불균형과 결측 문제를 해결하기 위해 향상된 모달리티 드롭아웃과 대조 학습을 통합한 새로운 다중 모달 학습 프레임워크를 제안합니다.
- 2. 학습 가능한 모달리티 토큰을 도입하여 결측을 인식하는 모달리티 융합을 개선하고, 기존의 단일 모달 대조 목표를 융합된 다중 모달 표현으로 확장합니다.
- 3. 대규모 임상 데이터셋을 활용한 실험 결과, 단일 모달리티만 사용 가능한 어려운 상황에서도 최첨단 성능을 달성했습니다.
- 4. 최근 CT 기반 모델과의 성공적인 통합을 통해 본 접근 방식의 적응성을 입증했습니다.
- 5. 본 연구는 다중 모달 학습의 효과성, 효율성, 일반화 가능성을 강조하며, 실제 임상 응용에 유망한 확장 가능하고 저비용의 솔루션을 제공합니다.


---

*Generated on 2025-09-24 15:57:09*