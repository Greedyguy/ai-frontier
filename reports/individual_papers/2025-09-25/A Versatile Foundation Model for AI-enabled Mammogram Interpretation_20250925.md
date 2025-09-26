---
keywords:
  - Self-supervised Learning
  - Knowledge Distillation
  - Mammogram Foundation Model
  - Lesion Detection
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.20271
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:15:05.273665",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Knowledge Distillation",
    "Mammogram Foundation Model",
    "Lesion Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Knowledge Distillation": 0.8,
    "Mammogram Foundation Model": 0.78,
    "Lesion Detection": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised learning",
        "canonical": "Self-supervised Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Self-supervised learning is a key technique used in the model's training process, enhancing its connectivity with other AI methodologies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Knowledge distillation",
        "canonical": "Knowledge Distillation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Knowledge distillation is crucial for transferring learned features and clinical knowledge, linking it to educational and model compression techniques.",
        "novelty_score": 0.58,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Mammogram foundation model",
        "canonical": "Mammogram Foundation Model",
        "aliases": [
          "VersaMammo"
        ],
        "category": "unique_technical",
        "rationale": "This represents a novel application of foundation models specifically tailored for mammogram analysis, offering unique insights into medical imaging.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Lesion detection",
        "canonical": "Lesion Detection",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Lesion detection is a primary clinical task, linking it to broader medical imaging and diagnostic processes.",
        "novelty_score": 0.4,
        "connectivity_score": 0.76,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "breast cancer",
      "mammography",
      "clinical tasks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-supervised learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Knowledge distillation",
      "resolved_canonical": "Knowledge Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Mammogram foundation model",
      "resolved_canonical": "Mammogram Foundation Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Lesion detection",
      "resolved_canonical": "Lesion Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.76,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# A Versatile Foundation Model for AI-enabled Mammogram Interpretation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20271.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.20271](https://arxiv.org/abs/2509.20271)

## 🔗 유사한 논문
- [[2025-09-23/Parameter-efficient fine-tuning (PEFT) of Vision Foundation Models for Atypical Mitotic Figure Classification_20250923|Parameter-efficient fine-tuning (PEFT) of Vision Foundation Models for Atypical Mitotic Figure Classification]] (83.4% similar)
- [[2025-09-22/NeuroRAD-FM_ A Foundation Model for Neuro-Oncology with Distributionally Robust Training_20250922|NeuroRAD-FM: A Foundation Model for Neuro-Oncology with Distributionally Robust Training]] (83.3% similar)
- [[2025-09-23/Breast Cancer Classification Using Gradient Boosting Algorithms Focusing on Reducing the False Negative and SHAP for Explainability_20250923|Breast Cancer Classification Using Gradient Boosting Algorithms Focusing on Reducing the False Negative and SHAP for Explainability]] (83.0% similar)
- [[2025-09-24/Learning neuroimaging models from health system-scale data_20250924|Learning neuroimaging models from health system-scale data]] (82.9% similar)
- [[2025-09-23/Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images_20250923|Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Knowledge Distillation|Knowledge Distillation]], [[keywords/Lesion Detection|Lesion Detection]]
**⚡ Unique Technical**: [[keywords/Mammogram Foundation Model|Mammogram Foundation Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20271v1 Announce Type: new 
Abstract: Breast cancer is the most commonly diagnosed cancer and the leading cause of cancer-related mortality in women globally. Mammography is essential for the early detection and diagnosis of breast lesions. Despite recent progress in foundation models (FMs) for mammogram analysis, their clinical translation remains constrained by several fundamental limitations, including insufficient diversity in training data, limited model generalizability, and a lack of comprehensive evaluation across clinically relevant tasks. Here, we introduce VersaMammo, a versatile foundation model for mammograms, designed to overcome these limitations. We curated the largest multi-institutional mammogram dataset to date, comprising 706,239 images from 21 sources. To improve generalization, we propose a two-stage pre-training strategy to develop VersaMammo, a mammogram foundation model. First, a teacher model is trained via self-supervised learning to extract transferable features from unlabeled mammograms. Then, supervised learning combined with knowledge distillation transfers both features and clinical knowledge into VersaMammo. To ensure a comprehensive evaluation, we established a benchmark comprising 92 specific tasks, including 68 internal tasks and 24 external validation tasks, spanning 5 major clinical task categories: lesion detection, segmentation, classification, image retrieval, and visual question answering. VersaMammo achieves state-of-the-art performance, ranking first in 50 out of 68 specific internal tasks and 20 out of 24 external validation tasks, with average ranks of 1.5 and 1.2, respectively. These results demonstrate its superior generalization and clinical utility, offering a substantial advancement toward reliable and scalable breast cancer screening and diagnosis.

## 📝 요약

VersaMammo는 유방암 조기 발견을 위한 다재다능한 기초 모델로, 기존 모델의 한계를 극복하고자 개발되었습니다. 21개 출처에서 수집한 706,239개의 이미지를 포함한 대규모 데이터셋을 활용하여, 두 단계의 사전 학습 전략을 통해 모델의 일반화 능력을 향상시켰습니다. 첫 번째 단계에서는 자가 지도 학습을 통해 전이 가능한 특징을 추출하고, 두 번째 단계에서는 지도 학습과 지식 증류를 통해 임상 지식을 통합했습니다. 92개의 임상 과제를 포함한 벤치마크를 통해 평가한 결과, VersaMammo는 68개의 내부 과제 중 50개, 24개의 외부 검증 과제 중 20개에서 최고 성능을 기록했습니다. 이는 유방암 스크리닝과 진단의 신뢰성과 확장성을 크게 향상시킵니다.

## 🎯 주요 포인트

- 1. VersaMammo는 유방촬영술 분석을 위한 다재다능한 기초 모델로, 기존 모델의 한계를 극복하기 위해 설계되었습니다.
- 2. 21개 출처에서 706,239개의 이미지를 포함한 최대 규모의 다기관 유방촬영술 데이터셋을 구축하였습니다.
- 3. 두 단계의 사전 학습 전략을 통해 일반화 성능을 향상시켰으며, 자가 지도 학습과 지식 증류를 결합하여 임상 지식을 모델에 통합했습니다.
- 4. 5개의 주요 임상 과제 범주에 걸친 92개의 특정 과제를 포함하는 벤치마크를 설정하여 포괄적인 평가를 보장했습니다.
- 5. VersaMammo는 68개의 내부 과제 중 50개, 24개의 외부 검증 과제 중 20개에서 1위를 차지하며, 우수한 일반화 성능과 임상적 유용성을 입증했습니다.


---

*Generated on 2025-09-26 09:15:05*