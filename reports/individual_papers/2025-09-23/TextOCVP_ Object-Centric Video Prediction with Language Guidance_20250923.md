---
keywords:
  - Object-Centric Video Prediction
  - Transformer
  - Vision-Language Model
  - Structured Latent Space
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2502.11655
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:16:52.839446",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Object-Centric Video Prediction",
    "Transformer",
    "Vision-Language Model",
    "Structured Latent Space"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Object-Centric Video Prediction": 0.78,
    "Transformer": 0.85,
    "Vision-Language Model": 0.8,
    "Structured Latent Space": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Object-Centric Video Prediction",
        "canonical": "Object-Centric Video Prediction",
        "aliases": [
          "OCVP"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach that combines object-centric models with video prediction, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Text-Conditioned Transformer",
        "canonical": "Transformer",
        "aliases": [
          "Text-Conditioned Transformer"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a fundamental component of the proposed model, linking to broader technical concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "The integration of textual descriptions with visual data aligns with the evolving concept of vision-language models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Structured Latent Space",
        "canonical": "Structured Latent Space",
        "aliases": [
          "Latent Space"
        ],
        "category": "specific_connectable",
        "rationale": "Structured latent spaces are crucial for understanding the model's ability to control and predict object dynamics.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "autonomous agents",
      "complex environments",
      "video frames"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Object-Centric Video Prediction",
      "resolved_canonical": "Object-Centric Video Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Text-Conditioned Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Structured Latent Space",
      "resolved_canonical": "Structured Latent Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# TextOCVP: Object-Centric Video Prediction with Language Guidance

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2502.11655.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2502.11655](https://arxiv.org/abs/2502.11655)

## 🔗 유사한 논문
- [[2025-09-22/OSPO_ Object-centric Self-improving Preference Optimization for Text-to-Image Generation_20250922|OSPO: Object-centric Self-improving Preference Optimization for Text-to-Image Generation]] (81.4% similar)
- [[2025-09-22/Enriched Feature Representation and Motion Prediction Module for MOSEv2 Track of 7th LSVOS Challenge_ 3rd Place Solution_20250922|Enriched Feature Representation and Motion Prediction Module for MOSEv2 Track of 7th LSVOS Challenge: 3rd Place Solution]] (80.8% similar)
- [[2025-09-23/Text-Scene_ A Scene-to-Language Parsing Framework for 3D Scene Understanding_20250923|Text-Scene: A Scene-to-Language Parsing Framework for 3D Scene Understanding]] (80.6% similar)
- [[2025-09-23/VidCLearn_ A Continual Learning Approach for Text-to-Video Generation_20250923|VidCLearn: A Continual Learning Approach for Text-to-Video Generation]] (80.2% similar)
- [[2025-09-22/Enhancing Sa2VA for Referent Video Object Segmentation_ 2nd Solution for 7th LSVOS RVOS Track_20250922|Enhancing Sa2VA for Referent Video Object Segmentation: 2nd Solution for 7th LSVOS RVOS Track]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Structured Latent Space|Structured Latent Space]]
**⚡ Unique Technical**: [[keywords/Object-Centric Video Prediction|Object-Centric Video Prediction]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.11655v2 Announce Type: replace 
Abstract: Understanding and forecasting future scene states is critical for autonomous agents to plan and act effectively in complex environments. Object-centric models, with structured latent spaces, have shown promise in modeling object dynamics and predicting future scene states, but often struggle to scale beyond simple synthetic datasets and to integrate external guidance, limiting their applicability in robotics. To address these limitations, we propose TextOCVP, an object-centric model for video prediction guided by textual descriptions. TextOCVP parses an observed scene into object representations, called slots, and utilizes a text-conditioned transformer predictor to forecast future object states and video frames. Our approach jointly models object dynamics and interactions while incorporating textual guidance, enabling accurate and controllable predictions. TextOCVP's structured latent space offers a more precise control of the forecasting process, outperforming several video prediction baselines on two datasets. Additionally, we show that structured object-centric representations provide superior robustness to novel scene configurations, as well as improved controllability and interpretability, enabling more precise and understandable predictions. Videos and code are available at https://play-slot.github.io/TextOCVP.

## 📝 요약

TextOCVP는 텍스트 설명을 활용한 객체 중심의 비디오 예측 모델로, 복잡한 환경에서의 객체 동역학과 상호작용을 효과적으로 예측합니다. 이 모델은 관찰된 장면을 객체 표현으로 분해하고, 텍스트로 조건화된 트랜스포머 예측기를 사용하여 미래의 객체 상태와 비디오 프레임을 예측합니다. TextOCVP는 구조화된 잠재 공간을 통해 예측 과정을 더 정확하게 제어하며, 두 개의 데이터셋에서 기존 비디오 예측 모델들을 능가하는 성능을 보입니다. 또한, 새로운 장면 구성에 대한 강인성과 예측의 제어 가능성 및 해석 가능성을 향상시킵니다.

## 🎯 주요 포인트

- 1. TextOCVP는 텍스트 설명을 통해 비디오 예측을 수행하는 객체 중심 모델로, 객체 동역학과 상호작용을 모델링하여 정확하고 제어 가능한 예측을 가능하게 합니다.
- 2. 이 모델은 관찰된 장면을 객체 표현인 슬롯으로 파싱하고, 텍스트 조건부 트랜스포머 예측기를 사용하여 미래 객체 상태와 비디오 프레임을 예측합니다.
- 3. TextOCVP는 구조화된 잠재 공간을 통해 예측 과정을 보다 정밀하게 제어할 수 있으며, 두 개의 데이터셋에서 여러 비디오 예측 기준 모델을 능가합니다.
- 4. 구조화된 객체 중심 표현은 새로운 장면 구성에 대한 뛰어난 견고성을 제공하며, 예측의 제어 가능성과 해석 가능성을 향상시킵니다.


---

*Generated on 2025-09-24 05:16:52*