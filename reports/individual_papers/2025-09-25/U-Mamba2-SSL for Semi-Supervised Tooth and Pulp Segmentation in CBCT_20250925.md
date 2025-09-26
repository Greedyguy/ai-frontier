---
keywords:
  - Self-supervised Learning
  - Cone-Beam Computed Tomography
  - U-Mamba2-SSL
  - Disruptive Autoencoder
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20154
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:00:06.821143",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Cone-Beam Computed Tomography",
    "U-Mamba2-SSL",
    "Disruptive Autoencoder"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.8,
    "Cone-Beam Computed Tomography": 0.78,
    "U-Mamba2-SSL": 0.75,
    "Disruptive Autoencoder": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Semi-Supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "Links to existing knowledge on leveraging unlabeled data, enhancing connectivity.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Cone-Beam Computed Tomography",
        "canonical": "Cone-Beam Computed Tomography",
        "aliases": [
          "CBCT"
        ],
        "category": "unique_technical",
        "rationale": "Specific to dental imaging, offering unique insights into medical imaging techniques.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "U-Mamba2-SSL",
        "canonical": "U-Mamba2-SSL",
        "aliases": [
          "U-Mamba2"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel framework specific to the study, crucial for understanding the paper's contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.5,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      },
      {
        "surface": "Disruptive Autoencoder",
        "canonical": "Disruptive Autoencoder",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach within the model, enhancing understanding of the framework's innovation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "treatment planning",
      "diagnosis",
      "clinical applications"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Semi-Supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Cone-Beam Computed Tomography",
      "resolved_canonical": "Cone-Beam Computed Tomography",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "U-Mamba2-SSL",
      "resolved_canonical": "U-Mamba2-SSL",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.5,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Disruptive Autoencoder",
      "resolved_canonical": "Disruptive Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# U-Mamba2-SSL for Semi-Supervised Tooth and Pulp Segmentation in CBCT

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20154.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20154](https://arxiv.org/abs/2509.20154)

## 🔗 유사한 논문
- [[2025-09-24/An Efficient Self-Supervised Framework for Long-Sequence EEG Modeling_20250924|An Efficient Self-Supervised Framework for Long-Sequence EEG Modeling]] (82.6% similar)
- [[2025-09-24/DiSSECT_ Structuring Transfer-Ready Medical Image Representations through Discrete Self-Supervision_20250924|DiSSECT: Structuring Transfer-Ready Medical Image Representations through Discrete Self-Supervision]] (82.5% similar)
- [[2025-09-18/Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model_20250918|Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model]] (82.3% similar)
- [[2025-09-23/Surgical-MambaLLM_ Mamba2-enhanced Multimodal Large Language Model for VQLA in Robotic Surgery_20250923|Surgical-MambaLLM: Mamba2-enhanced Multimodal Large Language Model for VQLA in Robotic Surgery]] (82.1% similar)
- [[2025-09-24/UltraBoneUDF_ Self-supervised Bone Surface Reconstruction from Ultrasound Based on Neural Unsigned Distance Functions_20250924|UltraBoneUDF: Self-supervised Bone Surface Reconstruction from Ultrasound Based on Neural Unsigned Distance Functions]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Cone-Beam Computed Tomography|Cone-Beam Computed Tomography]], [[keywords/U-Mamba2-SSL|U-Mamba2-SSL]], [[keywords/Disruptive Autoencoder|Disruptive Autoencoder]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20154v1 Announce Type: cross 
Abstract: Accurate segmentation of teeth and pulp in Cone-Beam Computed Tomography (CBCT) is vital for clinical applications like treatment planning and diagnosis. However, this process requires extensive expertise and is exceptionally time-consuming, highlighting the critical need for automated algorithms that can effectively utilize unlabeled data. In this paper, we propose U-Mamba2-SSL, a novel semi-supervised learning framework that builds on the U-Mamba2 model and employs a multi-stage training strategy. The framework first pre-trains U-Mamba2 in a self-supervised manner using a disruptive autoencoder. It then leverages unlabeled data through consistency regularization, where we introduce input and feature perturbations to ensure stable model outputs. Finally, a pseudo-labeling strategy is implemented with a reduced loss weighting to minimize the impact of potential errors. U-Mamba2-SSL achieved an average score of 0.872 and a DSC of 0.969 on the validation dataset, demonstrating the superior performance of our approach. The code is available at https://github.com/zhiqin1998/UMamba2.

## 📝 요약

이 논문은 치과 진단 및 치료 계획에 중요한 CBCT에서의 치아와 치수의 정확한 분할을 자동화하기 위해 U-Mamba2-SSL이라는 새로운 반지도 학습 프레임워크를 제안합니다. 이 프레임워크는 U-Mamba2 모델을 기반으로 하며, 자기 지도 학습과 일관성 정규화를 통해 비지도 데이터를 활용합니다. 또한, 입력 및 특징 변형을 도입하여 모델 출력의 안정성을 확보하고, 오류 영향을 최소화하기 위해 가중치를 줄인 의사 레이블링 전략을 사용합니다. 제안된 방법은 검증 데이터셋에서 평균 점수 0.872와 DSC 0.969를 기록하며 우수한 성능을 입증했습니다.

## 🎯 주요 포인트

- 1. 치아와 치수의 정확한 분할은 임상 응용에서 중요하지만, 많은 전문 지식과 시간이 필요하여 자동화된 알고리즘의 필요성이 대두되고 있습니다.
- 2. 본 논문에서는 U-Mamba2 모델을 기반으로 한 새로운 반지도 학습 프레임워크인 U-Mamba2-SSL을 제안합니다.
- 3. U-Mamba2-SSL은 자기 지도 학습, 일관성 정규화, 가중치 감소된 의사 레이블링 전략을 통해 모델의 성능을 향상시킵니다.
- 4. 제안된 U-Mamba2-SSL은 검증 데이터셋에서 평균 점수 0.872와 DSC 0.969를 기록하며 우수한 성능을 입증했습니다.
- 5. 연구의 코드는 https://github.com/zhiqin1998/UMamba2에서 제공됩니다.


---

*Generated on 2025-09-25 16:00:06*