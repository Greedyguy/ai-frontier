<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:15:32.572104",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "HyKid Dataset",
    "Choroid Plexus",
    "Retrieval Augmented Generation",
    "Pediatric Hydrocephalus"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "HyKid Dataset": 0.8,
    "Choroid Plexus": 0.78,
    "Retrieval Augmented Generation": 0.82,
    "Pediatric Hydrocephalus": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "HyKid",
        "canonical": "HyKid Dataset",
        "aliases": [
          "HyKid",
          "HyKid MRI Dataset"
        ],
        "category": "unique_technical",
        "rationale": "The HyKid dataset is a unique resource for pediatric hydrocephalus research, providing a benchmark for neuroimaging algorithms.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Choroid Plexus",
        "canonical": "Choroid Plexus",
        "aliases": [
          "Choroid Plexus"
        ],
        "category": "specific_connectable",
        "rationale": "Choroid Plexus is a key anatomical structure in hydrocephalus evaluation, offering potential biomarkers.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending method for extracting structured data from clinical reports, enhancing dataset utility.",
        "novelty_score": 0.65,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Pediatric Hydrocephalus",
        "canonical": "Pediatric Hydrocephalus",
        "aliases": [
          "Child Hydrocephalus"
        ],
        "category": "specific_connectable",
        "rationale": "Focusing on pediatric hydrocephalus allows for targeted research and dataset application in child neurology.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "MRI",
      "Dataset",
      "Segmentation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "HyKid",
      "resolved_canonical": "HyKid Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Choroid Plexus",
      "resolved_canonical": "Choroid Plexus",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Pediatric Hydrocephalus",
      "resolved_canonical": "Pediatric Hydrocephalus",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# HyKid: An Open MRI Dataset with Expert-Annotated Multi-Structure and Choroid Plexus in Pediatric Hydrocephalus

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19218.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19218](https://arxiv.org/abs/2509.19218)

## 🔗 유사한 논문
- [[2025-09-23/A Multimodal and Multi-centric Head and Neck Cancer Dataset for Segmentation, Diagnosis and Outcome Prediction_20250923|A Multimodal and Multi-centric Head and Neck Cancer Dataset for Segmentation, Diagnosis and Outcome Prediction]] (82.6% similar)
- [[2025-09-22/From Data to Diagnosis_ A Large, Comprehensive Bone Marrow Dataset and AI Methods for Childhood Leukemia Prediction_20250922|From Data to Diagnosis: A Large, Comprehensive Bone Marrow Dataset and AI Methods for Childhood Leukemia Prediction]] (82.1% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (81.7% similar)
- [[2025-09-23/Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology_20250923|Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology]] (81.1% similar)
- [[2025-09-23/A Novel Metric for Detecting Memorization in Generative Models for Brain MRI Synthesis_20250923|A Novel Metric for Detecting Memorization in Generative Models for Brain MRI Synthesis]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Choroid Plexus|Choroid Plexus]], [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Pediatric Hydrocephalus|Pediatric Hydrocephalus]]
**⚡ Unique Technical**: [[keywords/HyKid Dataset|HyKid Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19218v1 Announce Type: cross 
Abstract: Evaluation of hydrocephalus in children is challenging, and the related research is limited by a lack of publicly available, expert-annotated datasets, particularly those with segmentation of the choroid plexus. To address this, we present HyKid, an open-source dataset from 48 pediatric patients with hydrocephalus. 3D MRIs were provided with 1mm isotropic resolution, which was reconstructed from routine low-resolution images using a slice-to-volume algorithm. Manually corrected segmentations of brain tissues, including white matter, grey matter, lateral ventricle, external CSF, and the choroid plexus, were provided by an experienced neurologist. Additionally, structured data was extracted from clinical radiology reports using a Retrieval-Augmented Generation framework. The strong correlation between choroid plexus volume and total CSF volume provided a potential biomarker for hydrocephalus evaluation, achieving excellent performance in a predictive model (AUC = 0.87). The proposed HyKid dataset provided a high-quality benchmark for neuroimaging algorithms development, and it revealed the choroid plexus-related features in hydrocephalus assessments. Our datasets are publicly available at https://www.synapse.org/Synapse:syn68544889.

## 📝 요약

이 논문은 소아 수두증 평가의 어려움을 해결하기 위해 HyKid라는 오픈소스 데이터셋을 소개합니다. 48명의 소아 환자로부터 얻은 3D MRI 데이터를 포함하며, 1mm 등방성 해상도로 재구성되었습니다. 경험 많은 신경과 전문의가 백질, 회백질, 측뇌실, 외부 뇌척수액(CSF), 맥락총을 수동으로 세분화했습니다. 또한, 임상 방사선 보고서에서 구조화된 데이터를 추출했습니다. 연구 결과, 맥락총 부피와 총 CSF 부피 간의 강한 상관관계가 발견되었으며, 이는 수두증 평가의 잠재적 바이오마커로 활용될 수 있음을 보여주었습니다(AUC = 0.87). HyKid 데이터셋은 신경영상 알고리즘 개발의 고품질 벤치마크를 제공하며, 수두증 평가에서 맥락총 관련 특징을 밝혀냈습니다. 데이터셋은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. HyKid는 48명의 소아 수두증 환자로부터 수집된 오픈 소스 데이터셋으로, 1mm 등방성 해상도의 3D MRI를 제공합니다.
- 2. 경험 많은 신경과 전문의가 백질, 회백질, 측뇌실, 외부 CSF, 맥락총을 포함한 뇌 조직의 수동 수정 분할을 제공합니다.
- 3. 맥락총 부피와 총 CSF 부피 간의 강한 상관관계는 수두증 평가를 위한 잠재적 바이오마커로, 예측 모델에서 우수한 성능(AUC = 0.87)을 달성했습니다.
- 4. HyKid 데이터셋은 신경영상 알고리즘 개발을 위한 고품질 벤치마크를 제공하며, 수두증 평가에서 맥락총 관련 특징을 밝혀냈습니다.
- 5. 데이터셋은 https://www.synapse.org/Synapse:syn68544889에서 공개적으로 이용 가능합니다.


---

*Generated on 2025-09-24 14:15:32*