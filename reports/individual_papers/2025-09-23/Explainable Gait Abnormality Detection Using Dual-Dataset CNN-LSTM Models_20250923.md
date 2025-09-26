---
keywords:
  - Neural Network
  - SHAP
  - Grad-CAM
  - Gait Analysis
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16472
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:21:34.008294",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "SHAP",
    "Grad-CAM",
    "Gait Analysis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.82,
    "SHAP": 0.78,
    "Grad-CAM": 0.8,
    "Gait Analysis": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "CNN-LSTM",
        "canonical": "Neural Network",
        "aliases": [
          "Convolutional Neural Network",
          "Long Short-Term Memory"
        ],
        "category": "broad_technical",
        "rationale": "Combining CNN and LSTM models is a common neural network approach that enhances connectivity with existing neural network concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.82
      },
      {
        "surface": "SHAP",
        "canonical": "SHAP",
        "aliases": [
          "SHapley Additive exPlanations"
        ],
        "category": "unique_technical",
        "rationale": "SHAP is a specific method for interpretability that is gaining traction in explainable AI, offering unique linkage opportunities.",
        "novelty_score": 0.75,
        "connectivity_score": 0.67,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Grad-CAM",
        "canonical": "Grad-CAM",
        "aliases": [
          "Gradient-weighted Class Activation Mapping"
        ],
        "category": "unique_technical",
        "rationale": "Grad-CAM is a widely recognized technique for visual explanations in deep learning models, enhancing specificity in linking.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "Gait Analysis",
        "canonical": "Gait Analysis",
        "aliases": [
          "Gait Abnormality Detection"
        ],
        "category": "unique_technical",
        "rationale": "Gait analysis is a specialized field within movement disorder diagnosis, offering strong specificity for linking.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "dual-branch",
      "held-out sets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "CNN-LSTM",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "SHAP",
      "resolved_canonical": "SHAP",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.67,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Grad-CAM",
      "resolved_canonical": "Grad-CAM",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Gait Analysis",
      "resolved_canonical": "Gait Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Explainable Gait Abnormality Detection Using Dual-Dataset CNN-LSTM Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16472.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16472](https://arxiv.org/abs/2509.16472)

## 🔗 유사한 논문
- [[2025-09-23/MSGAT-GRU_ A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction_20250923|MSGAT-GRU: A Multi-Scale Graph Attention and Recurrent Model for Spatiotemporal Road Accident Prediction]] (81.2% similar)
- [[2025-09-19/Fine-tuning Vision Language Models with Graph-based Knowledge for Explainable Medical Image Analysis_20250919|Fine-tuning Vision Language Models with Graph-based Knowledge for Explainable Medical Image Analysis]] (80.9% similar)
- [[2025-09-22/Training A Neural Network For Partially Occluded Road Sign Identification In The Context Of Autonomous Vehicles_20250922|Training A Neural Network For Partially Occluded Road Sign Identification In The Context Of Autonomous Vehicles]] (80.6% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (80.3% similar)
- [[2025-09-18/ProtoMedX_ Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification_20250918|ProtoMedX: Towards Explainable Multi-Modal Prototype Learning for Bone Health Classification]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/SHAP|SHAP]], [[keywords/Grad-CAM|Grad-CAM]], [[keywords/Gait Analysis|Gait Analysis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16472v1 Announce Type: new 
Abstract: Gait is a key indicator in diagnosing movement disorders, but most models lack interpretability and rely on single datasets. We propose a dual-branch CNN-LSTM framework a 1D branch on joint-based features from GAVD and a 3D branch on silhouettes from OU-MVLP. Interpretability is provided by SHAP (temporal attributions) and Grad-CAM (spatial localization).On held-out sets, the system achieves 98.6% accuracy with strong recall and F1. This approach advances explainable gait analysis across both clinical and biometric domains.

## 📝 요약

이 논문은 움직임 장애 진단에서 중요한 보행 분석을 위해 해석 가능한 모델을 제안합니다. 제안된 모델은 GAVD의 관절 기반 1D 특징과 OU-MVLP의 실루엣 기반 3D 특징을 사용하는 이중 가지 CNN-LSTM 프레임워크입니다. SHAP과 Grad-CAM을 통해 시간적 및 공간적 해석 가능성을 제공합니다. 제안된 시스템은 테스트 세트에서 98.6%의 정확도를 기록하며, 임상 및 생체 인식 분야에서 해석 가능한 보행 분석을 발전시킵니다.

## 🎯 주요 포인트

- 1. 보행은 운동 장애 진단의 핵심 지표로, 대부분의 모델은 해석 가능성이 부족하고 단일 데이터셋에 의존한다.
- 2. 제안된 모델은 GAVD의 관절 기반 특징을 활용한 1D 브랜치와 OU-MVLP의 실루엣을 활용한 3D 브랜치로 구성된 이중 브랜치 CNN-LSTM 프레임워크이다.
- 3. SHAP(시간적 기여도)와 Grad-CAM(공간적 위치)을 통해 모델의 해석 가능성을 제공한다.
- 4. 제안된 시스템은 테스트 세트에서 98.6%의 정확도를 달성하며, 높은 재현율과 F1 점수를 기록한다.
- 5. 이 접근법은 임상 및 생체 인식 분야에서 설명 가능한 보행 분석을 발전시킨다.


---

*Generated on 2025-09-24 04:21:34*