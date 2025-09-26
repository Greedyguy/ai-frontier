<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:25:44.914831",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Stochastic Cortical Self-Reconstruction",
    "Deep Learning",
    "Cortical Thickness Mapping",
    "Vertex Level Reconstruction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Stochastic Cortical Self-Reconstruction": 0.8,
    "Deep Learning": 0.85,
    "Cortical Thickness Mapping": 0.78,
    "Vertex Level Reconstruction": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Stochastic Cortical Self-Reconstruction",
        "canonical": "Stochastic Cortical Self-Reconstruction",
        "aliases": [
          "SCSR"
        ],
        "category": "unique_technical",
        "rationale": "This novel method is central to the paper's contribution and offers a new approach to cortical thickness mapping.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep learning is the foundational technology used in the proposed method, linking it to a broader technical context.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cortical Thickness Mapping",
        "canonical": "Cortical Thickness Mapping",
        "aliases": [
          "Cortical Thickness Measurement"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key application area of the method, facilitating connections to related research in neurology.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vertex Level Reconstruction",
        "canonical": "Vertex Level Reconstruction",
        "aliases": [
          "Vertex-wise Reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "This specific approach enhances the granularity of cortical mapping, distinguishing it from region-wise averages.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Stochastic Cortical Self-Reconstruction",
      "resolved_canonical": "Stochastic Cortical Self-Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cortical Thickness Mapping",
      "resolved_canonical": "Cortical Thickness Mapping",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vertex Level Reconstruction",
      "resolved_canonical": "Vertex Level Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Individualized Mapping of Aberrant Cortical Thickness via Stochastic Cortical Self-Reconstruction

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2403.06837.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2403.06837](https://arxiv.org/abs/2403.06837)

## 🔗 유사한 논문
- [[2025-09-18/Template-Based Cortical Surface Reconstruction with Minimal Energy Deformation_20250918|Template-Based Cortical Surface Reconstruction with Minimal Energy Deformation]] (83.5% similar)
- [[2025-09-24/SSCM_ A Spatial-Semantic Consistent Model for Multi-Contrast MRI Super-Resolution_20250924|SSCM: A Spatial-Semantic Consistent Model for Multi-Contrast MRI Super-Resolution]] (82.2% similar)
- [[2025-09-23/Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology_20250923|Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology]] (81.9% similar)
- [[2025-09-18/Brain age identification from diffusion MRI synergistically predicts neurodegenerative disease_20250918|Brain age identification from diffusion MRI synergistically predicts neurodegenerative disease]] (81.5% similar)
- [[2025-09-24/DiSSECT_ Structuring Transfer-Ready Medical Image Representations through Discrete Self-Supervision_20250924|DiSSECT: Structuring Transfer-Ready Medical Image Representations through Discrete Self-Supervision]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Cortical Thickness Mapping|Cortical Thickness Mapping]]
**⚡ Unique Technical**: [[keywords/Stochastic Cortical Self-Reconstruction|Stochastic Cortical Self-Reconstruction]], [[keywords/Vertex Level Reconstruction|Vertex Level Reconstruction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2403.06837v2 Announce Type: replace 
Abstract: Understanding individual differences in cortical structure is key to advancing diagnostics in neurology and psychiatry. Reference models aid in detecting aberrant cortical thickness, yet site-specific biases limit their direct application to unseen data, and region-wise averages prevent the detection of localized cortical changes. To address these limitations, we developed the Stochastic Cortical Self-Reconstruction (SCSR), a novel method that leverages deep learning to reconstruct cortical thickness maps at the vertex level without needing additional subject information. Trained on over 25,000 healthy individuals, SCSR generates highly individualized cortical reconstructions that can detect subtle thickness deviations. Our evaluations on independent test sets demonstrated that SCSR achieved significantly lower reconstruction errors and identified atrophy patterns that enabled better disease discrimination than established methods. It also hints at cortical thinning in preterm infants that went undetected by existing models, showcasing its versatility. Finally, SCSR excelled in mapping highly resolved cortical deviations of dementia patients from clinical data, highlighting its potential for supporting diagnosis in clinical practice.

## 📝 요약

이 논문은 신경학 및 정신의학 진단을 위한 새로운 방법론인 확률적 피질 자가 재구성(SCSR)을 제안합니다. SCSR은 딥러닝을 활용하여 피질 두께 지도를 정밀하게 재구성하며, 25,000명 이상의 건강한 개인 데이터를 기반으로 훈련되었습니다. 이 방법은 기존 모델의 한계를 극복하고, 독립적인 테스트에서 낮은 재구성 오류와 질병 구별 능력을 보여주었습니다. 특히, 기존 모델로는 감지되지 않았던 미숙아의 피질 얇아짐과 치매 환자의 세밀한 피질 변화를 효과적으로 탐지하여 임상 진단 지원에 유용함을 입증했습니다.

## 🎯 주요 포인트

- 1. SCSR는 딥러닝을 활용하여 추가적인 피험자 정보 없이 버텍스 수준에서 피질 두께 지도를 재구성하는 새로운 방법입니다.
- 2. 25,000명 이상의 건강한 개인 데이터를 기반으로 훈련된 SCSR는 미세한 두께 편차를 감지할 수 있는 개별화된 피질 재구성을 생성합니다.
- 3. 독립적인 테스트 세트 평가에서 SCSR는 기존 방법보다 낮은 재구성 오류와 더 나은 질병 구별을 가능하게 하는 위축 패턴을 식별했습니다.
- 4. SCSR는 기존 모델로는 감지되지 않았던 미숙아의 피질 얇아짐을 포착하여 그 다양성을 보여줍니다.
- 5. SCSR는 임상 데이터에서 치매 환자의 고해상도 피질 편차를 매핑하는 데 뛰어나며, 임상 진단 지원에 대한 잠재력을 강조합니다.


---

*Generated on 2025-09-24 16:25:44*