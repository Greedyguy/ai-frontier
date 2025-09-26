---
keywords:
  - Computer Vision
  - Parkinson's Disease Diagnosis
  - Supervised Learning
  - Medical Imaging
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17566
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:01:55.483667",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Computer Vision",
    "Parkinson's Disease Diagnosis",
    "Supervised Learning",
    "Medical Imaging"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Computer Vision": 0.78,
    "Parkinson's Disease Diagnosis": 0.79,
    "Supervised Learning": 0.81,
    "Medical Imaging": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "2D Vision Foundation Models",
        "canonical": "Computer Vision",
        "aliases": [
          "2D VFMs",
          "Vision Foundation Models"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the broader field of computer vision, which is crucial for understanding the adaptation of 2D models to 3D medical imaging.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Parkinson's Disease Diagnosis",
        "canonical": "Parkinson's Disease Diagnosis",
        "aliases": [
          "PD Diagnosis"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specific application area for medical imaging and machine learning, facilitating links to related healthcare studies.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "Multi-ROI Supervised Contrastive Learning",
        "canonical": "Supervised Learning",
        "aliases": [
          "Multi-ROI Contrastive Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights a specific learning technique that enhances model performance, linking to broader machine learning discussions.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.81
      },
      {
        "surface": "QSM and NM-MRI Images",
        "canonical": "Medical Imaging",
        "aliases": [
          "QSM",
          "NM-MRI"
        ],
        "category": "broad_technical",
        "rationale": "Essential for linking discussions on specific imaging modalities used in medical diagnostics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.83,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "automatic diagnosis",
      "dataset",
      "accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "2D Vision Foundation Models",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Parkinson's Disease Diagnosis",
      "resolved_canonical": "Parkinson's Disease Diagnosis",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Multi-ROI Supervised Contrastive Learning",
      "resolved_canonical": "Supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "QSM and NM-MRI Images",
      "resolved_canonical": "Medical Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.83,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# MRN: Harnessing 2D Vision Foundation Models for Diagnosing Parkinson's Disease with Limited 3D MR Data

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17566.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17566](https://arxiv.org/abs/2509.17566)

## 🔗 유사한 논문
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (84.3% similar)
- [[2025-09-22/NeuroRAD-FM_ A Foundation Model for Neuro-Oncology with Distributionally Robust Training_20250922|NeuroRAD-FM: A Foundation Model for Neuro-Oncology with Distributionally Robust Training]] (83.8% similar)
- [[2025-09-18/Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (83.5% similar)
- [[2025-09-22/Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture_20250922|Self-supervised learning of imaging and clinical signatures using a multimodal joint-embedding predictive architecture]] (83.2% similar)
- [[2025-09-22/iCBIR-Sli_ Interpretable Content-Based Image Retrieval with 2D Slice Embeddings_20250922|iCBIR-Sli: Interpretable Content-Based Image Retrieval with 2D Slice Embeddings]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Computer Vision|Computer Vision]], [[keywords/Medical Imaging|Medical Imaging]]
**🔗 Specific Connectable**: [[keywords/Supervised Learning|Supervised Learning]]
**⚡ Unique Technical**: [[keywords/Parkinson's Disease Diagnosis|Parkinson's Disease Diagnosis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17566v1 Announce Type: cross 
Abstract: The automatic diagnosis of Parkinson's disease is in high clinical demand due to its prevalence and the importance of targeted treatment. Current clinical practice often relies on diagnostic biomarkers in QSM and NM-MRI images. However, the lack of large, high-quality datasets makes training diagnostic models from scratch prone to overfitting. Adapting pre-trained 3D medical models is also challenging, as the diversity of medical imaging leads to mismatches in voxel spacing and modality between pre-training and fine-tuning data. In this paper, we address these challenges by leveraging 2D vision foundation models (VFMs). Specifically, we crop multiple key ROIs from NM and QSM images, process each ROI through separate branches to compress the ROI into a token, and then combine these tokens into a unified patient representation for classification. Within each branch, we use 2D VFMs to encode axial slices of the 3D ROI volume and fuse them into the ROI token, guided by an auxiliary segmentation head that steers the feature extraction toward specific brain nuclei. Additionally, we introduce multi-ROI supervised contrastive learning, which improves diagnostic performance by pulling together representations of patients from the same class while pushing away those from different classes. Our approach achieved first place in the MICCAI 2025 PDCADxFoundation challenge, with an accuracy of 86.0% trained on a dataset of only 300 labeled QSM and NM-MRI scans, outperforming the second-place method by 5.5%.These results highlight the potential of 2D VFMs for clinical analysis of 3D MR images.

## 📝 요약

이 논문은 파킨슨병의 자동 진단을 위해 2D 비전 기초 모델(VFM)을 활용하는 방법을 제안합니다. 기존의 3D 의료 모델을 활용하기 어려운 문제를 해결하기 위해, NM 및 QSM 이미지에서 여러 관심 영역(ROI)을 잘라내고, 각 ROI를 별도의 분기로 처리하여 토큰으로 압축한 후 이를 통합하여 환자 표현을 생성합니다. 각 분기에서는 2D VFM을 사용하여 3D ROI 볼륨의 축 방향 슬라이스를 인코딩하고, 보조 분할 헤드를 통해 특정 뇌 핵으로의 특징 추출을 유도합니다. 또한, 다중 ROI 감독 대조 학습을 도입하여 같은 클래스의 환자 표현을 가까이하고 다른 클래스의 표현을 멀리함으로써 진단 성능을 향상시킵니다. 이 접근법은 MICCAI 2025 PDCADxFoundation 챌린지에서 86.0%의 정확도로 1위를 차지했으며, 이는 300개의 라벨링된 QSM 및 NM-MRI 스캔 데이터셋으로 훈련된 결과로, 2위 방법보다 5.5% 높은 성능을 보였습니다. 이 결과는 2D VFM이 3D MR 이미지의 임상 분석에 유망한 가능성을 지님을 강조합니다.

## 🎯 주요 포인트

- 1. 파킨슨병의 자동 진단을 위해 NM 및 QSM 이미지를 활용하여 다중 ROI를 추출하고, 이를 통합하여 환자 표현으로 분류하는 방법을 제안합니다.
- 2. 2D 비전 기초 모델(VFMs)을 사용하여 3D ROI 볼륨의 축 방향 슬라이스를 인코딩하고, 보조 분할 헤드를 통해 특정 뇌 핵으로의 특징 추출을 유도합니다.
- 3. 다중 ROI 지도 대조 학습을 도입하여 같은 클래스의 환자 표현을 가까이 모으고 다른 클래스의 환자 표현을 멀리 떨어뜨림으로써 진단 성능을 향상시킵니다.
- 4. 제안된 방법은 MICCAI 2025 PDCADxFoundation 챌린지에서 86.0%의 정확도로 1위를 차지했으며, 300개의 라벨링된 QSM 및 NM-MRI 스캔 데이터셋에서 훈련되었습니다.
- 5. 2D VFMs가 3D MR 이미지의 임상 분석에 있어 잠재력이 있음을 강조합니다.


---

*Generated on 2025-09-24 00:01:55*