<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:25:32.712149",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Gaussian Process Diffeomorphic Statistical Shape Model",
    "Hip Dysplasia",
    "Volumetric CT Scans",
    "Osteoarthritis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Gaussian Process Diffeomorphic Statistical Shape Model": 0.8,
    "Hip Dysplasia": 0.78,
    "Volumetric CT Scans": 0.7,
    "Osteoarthritis": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Gaussian Process Diffeomorphic Statistical Shape Model",
        "canonical": "Gaussian Process Diffeomorphic Statistical Shape Model",
        "aliases": [
          "GPDSSM"
        ],
        "category": "unique_technical",
        "rationale": "This model is central to the paper and represents a novel approach to hip dysplasia assessment.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "dysplasia",
        "canonical": "Hip Dysplasia",
        "aliases": [
          "dysplastic",
          "hip dysplasia"
        ],
        "category": "specific_connectable",
        "rationale": "Hip dysplasia is a key medical condition discussed in the paper, relevant for linking to medical and orthopedic studies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "volumetric CT scans",
        "canonical": "Volumetric CT Scans",
        "aliases": [
          "CT scans",
          "computed tomography"
        ],
        "category": "broad_technical",
        "rationale": "CT scans are a fundamental technology used in the study, relevant for linking to imaging and diagnostic technologies.",
        "novelty_score": 0.3,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      },
      {
        "surface": "osteoarthritis",
        "canonical": "Osteoarthritis",
        "aliases": [
          "OA"
        ],
        "category": "specific_connectable",
        "rationale": "Osteoarthritis is a related condition that the paper addresses, useful for connecting to broader discussions on joint diseases.",
        "novelty_score": 0.35,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "classification",
      "accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Gaussian Process Diffeomorphic Statistical Shape Model",
      "resolved_canonical": "Gaussian Process Diffeomorphic Statistical Shape Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "dysplasia",
      "resolved_canonical": "Hip Dysplasia",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "volumetric CT scans",
      "resolved_canonical": "Volumetric CT Scans",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "osteoarthritis",
      "resolved_canonical": "Osteoarthritis",
      "decision": "linked",
      "scores": {
        "novelty": 0.35,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Gaussian Process Diffeomorphic Statistical Shape Modelling Outperforms Angle-Based Methods for Assessment of Hip Dysplasia

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.04886.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2506.04886](https://arxiv.org/abs/2506.04886)

## 🔗 유사한 논문
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (81.8% similar)
- [[2025-09-24/Your Turn_ At Home Turning Angle Estimation for Parkinson's Disease Severity Assessment_20250924|Your Turn: At Home Turning Angle Estimation for Parkinson's Disease Severity Assessment]] (81.2% similar)
- [[2025-09-18/ProtoMedX_ Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification_20250918|ProtoMedX: Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification]] (80.8% similar)
- [[2025-09-23/Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology_20250923|Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology]] (80.4% similar)
- [[2025-09-24/Visionerves_ Automatic and Reproducible Hybrid AI for Peripheral Nervous System Recognition Applied to Endometriosis Cases_20250924|Visionerves: Automatic and Reproducible Hybrid AI for Peripheral Nervous System Recognition Applied to Endometriosis Cases]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Volumetric CT Scans|Volumetric CT Scans]]
**🔗 Specific Connectable**: [[keywords/Hip Dysplasia|Hip Dysplasia]], [[keywords/Osteoarthritis|Osteoarthritis]]
**⚡ Unique Technical**: [[keywords/Gaussian Process Diffeomorphic Statistical Shape Model|Gaussian Process Diffeomorphic Statistical Shape Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.04886v2 Announce Type: replace 
Abstract: Dysplasia is a recognised risk factor for osteoarthritis (OA) of the hip, early diagnosis of dysplasia is important to provide opportunities for surgical interventions aimed at reducing the risk of hip OA. We have developed a pipeline for semi-automated classification of dysplasia using volumetric CT scans of patients' hips and a minimal set of clinically annotated landmarks, combining the framework of the Gaussian Process Latent Variable Model with diffeomorphism to create a statistical shape model, which we termed the Gaussian Process Diffeomorphic Statistical Shape Model (GPDSSM). We used 192 CT scans, 100 for model training and 92 for testing. The GPDSSM effectively distinguishes dysplastic samples from controls while also highlighting regions of the underlying surface that show dysplastic variations. As well as improving classification accuracy compared to angle-based methods (AUC 96.2% vs 91.2%), the GPDSSM can save time for clinicians by removing the need to manually measure angles and interpreting 2D scans for possible markers of dysplasia.

## 📝 요약

이 논문은 고관절 이형성이 골관절염(OA)의 위험 요인임을 인식하고, 조기 진단을 통해 수술적 개입 기회를 제공하는 중요성을 강조합니다. 연구진은 환자의 고관절 CT 스캔과 최소한의 임상 주석 랜드마크를 사용하여 이형성을 반자동으로 분류하는 파이프라인을 개발했습니다. 이 과정에서 가우시안 프로세스 잠재 변수 모델과 미분동형사상을 결합하여 가우시안 프로세스 미분동형 통계적 형태 모델(GPDSSM)을 만들었습니다. 192개의 CT 스캔을 사용하여 모델을 훈련(100개)하고 테스트(92개)했으며, GPDSSM은 이형성 샘플을 효과적으로 구분하고 이형성 변화를 보이는 표면 영역을 강조합니다. 각도 기반 방법보다 높은 분류 정확도(AUC 96.2% vs 91.2%)를 제공하며, 각도를 수동으로 측정하고 2D 스캔을 해석하는 과정을 생략함으로써 임상의의 시간을 절약할 수 있습니다.

## 🎯 주요 포인트

- 1. 고관절 이형성증은 골관절염의 위험 요인으로, 조기 진단이 중요합니다.
- 2. 연구팀은 환자의 고관절 CT 스캔과 최소한의 임상 주석 랜드마크를 사용하여 이형성증을 반자동으로 분류하는 파이프라인을 개발했습니다.
- 3. Gaussian Process Latent Variable Model과 미분동형사상을 결합한 통계적 형태 모델인 GPDSSM을 제안했습니다.
- 4. GPDSSM은 이형성증 샘플을 효과적으로 구분하며, 기존의 각도 기반 방법보다 높은 분류 정확도를 보입니다 (AUC 96.2% vs 91.2%).
- 5. GPDSSM은 각도를 수동으로 측정하고 2D 스캔을 해석할 필요성을 제거하여 임상의의 시간을 절약할 수 있습니다.


---

*Generated on 2025-09-24 15:25:32*