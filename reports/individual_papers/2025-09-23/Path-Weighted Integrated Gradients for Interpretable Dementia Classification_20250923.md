---
keywords:
  - Integrated Gradients
  - Path-Weighted Integrated Gradients
  - Explainable Artificial Intelligence
  - Dementia Classification
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17491
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:53:15.772946",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Integrated Gradients",
    "Path-Weighted Integrated Gradients",
    "Explainable Artificial Intelligence",
    "Dementia Classification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Integrated Gradients": 0.85,
    "Path-Weighted Integrated Gradients": 0.78,
    "Explainable Artificial Intelligence": 0.8,
    "Dementia Classification": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Integrated Gradients",
        "canonical": "Integrated Gradients",
        "aliases": [
          "IG"
        ],
        "category": "specific_connectable",
        "rationale": "Integrated Gradients is a foundational method in explainable AI, providing a strong link to discussions on model interpretability.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Path-Weighted Integrated Gradients",
        "canonical": "Path-Weighted Integrated Gradients",
        "aliases": [
          "PWIG"
        ],
        "category": "unique_technical",
        "rationale": "PWIG represents a novel extension of Integrated Gradients, offering a new approach to interpretability in AI models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Explainable Artificial Intelligence",
        "canonical": "Explainable Artificial Intelligence",
        "aliases": [
          "XAI"
        ],
        "category": "broad_technical",
        "rationale": "XAI is a broad technical area relevant to the paper's focus on interpretability and attribution methods.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Dementia Classification",
        "canonical": "Dementia Classification",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a specific application of the proposed method, linking to medical AI and classification tasks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Integrated Gradients",
      "resolved_canonical": "Integrated Gradients",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Path-Weighted Integrated Gradients",
      "resolved_canonical": "Path-Weighted Integrated Gradients",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Explainable Artificial Intelligence",
      "resolved_canonical": "Explainable Artificial Intelligence",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Dementia Classification",
      "resolved_canonical": "Dementia Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Path-Weighted Integrated Gradients for Interpretable Dementia Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17491.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17491](https://arxiv.org/abs/2509.17491)

## 🔗 유사한 논문
- [[2025-09-23/IPGPhormer_ Interpretable Pathology Graph-Transformer for Survival Analysis_20250923|IPGPhormer: Interpretable Pathology Graph-Transformer for Survival Analysis]] (81.6% similar)
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (80.2% similar)
- [[2025-09-18/ProtoMedX_ Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification_20250918|ProtoMedX: Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification]] (80.1% similar)
- [[2025-09-22/DPC-QA Net_ A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images_20250922|DPC-QA Net: A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images]] (80.0% similar)
- [[2025-09-22/PRISM_ Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images_20250922|PRISM: Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Explainable Artificial Intelligence|Explainable Artificial Intelligence]]
**🔗 Specific Connectable**: [[keywords/Integrated Gradients|Integrated Gradients]]
**⚡ Unique Technical**: [[keywords/Path-Weighted Integrated Gradients|Path-Weighted Integrated Gradients]], [[keywords/Dementia Classification|Dementia Classification]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17491v1 Announce Type: new 
Abstract: Integrated Gradients (IG) is a widely used attribution method in explainable artificial intelligence (XAI). In this paper, we introduce Path-Weighted Integrated Gradients (PWIG), a generalization of IG that incorporates a customizable weighting function into the attribution integral. This modification allows for targeted emphasis along different segments of the path between a baseline and the input, enabling improved interpretability, noise mitigation, and the detection of path-dependent feature relevance. We establish its theoretical properties and illustrate its utility through experiments on a dementia classification task using the OASIS-1 MRI dataset. Attribution maps generated by PWIG highlight clinically meaningful brain regions associated with various stages of dementia, providing users with sharp and stable explanations. The results suggest that PWIG offers a flexible and theoretically grounded approach for enhancing attribution quality in complex predictive models.

## 📝 요약

이 논문에서는 설명 가능한 인공지능(XAI)에서 널리 사용되는 기법인 통합 기울기(Integrated Gradients, IG)를 확장한 경로 가중 통합 기울기(Path-Weighted Integrated Gradients, PWIG)를 제안합니다. PWIG는 가중 함수의 도입을 통해 경로의 특정 구간에 대한 강조를 가능하게 하여 해석력을 높이고, 노이즈를 줄이며, 경로 의존적 특징의 중요성을 감지할 수 있습니다. 이론적 특성을 확립하고, OASIS-1 MRI 데이터셋을 활용한 치매 분류 실험을 통해 PWIG의 유용성을 입증했습니다. PWIG로 생성된 속성 맵은 치매의 다양한 단계와 관련된 임상적으로 의미 있는 뇌 영역을 강조하여 명확하고 안정적인 설명을 제공합니다. 결과적으로 PWIG는 복잡한 예측 모델에서 속성 품질을 향상시키는 유연하고 이론적으로 탄탄한 접근법을 제공합니다.

## 🎯 주요 포인트

- 1. Path-Weighted Integrated Gradients (PWIG)는 Integrated Gradients (IG)의 일반화로, 가중치 함수를 통합하여 설명 가능 인공지능(XAI)에서의 해석력을 향상시킵니다.
- 2. PWIG는 경로의 다양한 구간에 맞춤형 강조를 제공하여 해석력 개선, 노이즈 완화, 경로 의존적 특징 중요성 탐지를 가능하게 합니다.
- 3. OASIS-1 MRI 데이터셋을 사용한 치매 분류 실험에서 PWIG는 임상적으로 의미 있는 뇌 영역을 강조하여 명확하고 안정적인 설명을 제공합니다.
- 4. PWIG는 복잡한 예측 모델에서 설명 품질을 향상시키기 위한 유연하고 이론적으로 기반이 있는 접근 방식을 제안합니다.


---

*Generated on 2025-09-24 01:53:15*