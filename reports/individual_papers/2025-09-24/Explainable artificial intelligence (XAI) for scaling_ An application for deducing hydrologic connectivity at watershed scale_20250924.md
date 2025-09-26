<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:36:03.964606",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Explainable Artificial Intelligence",
    "Hydrologic Connectivity",
    "Long Short-Term Memory Network",
    "Hydrologic Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Explainable Artificial Intelligence": 0.78,
    "Hydrologic Connectivity": 0.77,
    "Long Short-Term Memory Network": 0.8,
    "Hydrologic Model": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Explainable artificial intelligence",
        "canonical": "Explainable Artificial Intelligence",
        "aliases": [
          "XAI"
        ],
        "category": "broad_technical",
        "rationale": "XAI is a key concept in interpreting model results and is directly applied in this study.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hydrologic connectivity",
        "canonical": "Hydrologic Connectivity",
        "aliases": [
          "Watershed Connectivity"
        ],
        "category": "unique_technical",
        "rationale": "This is a central concept in the paper, linking hydrology and AI.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Long short-term memory network",
        "canonical": "Long Short-Term Memory Network",
        "aliases": [
          "LSTM"
        ],
        "category": "specific_connectable",
        "rationale": "LSTM is a specific neural network architecture used in the study, providing a link to deep learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Hydrologic model",
        "canonical": "Hydrologic Model",
        "aliases": [
          "Hydrological Model"
        ],
        "category": "unique_technical",
        "rationale": "The hydrologic model is fundamental to the study's methodology and results.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "scaling problems",
      "process understanding"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Explainable artificial intelligence",
      "resolved_canonical": "Explainable Artificial Intelligence",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hydrologic connectivity",
      "resolved_canonical": "Hydrologic Connectivity",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Long short-term memory network",
      "resolved_canonical": "Long Short-Term Memory Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Hydrologic model",
      "resolved_canonical": "Hydrologic Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Explainable artificial intelligence (XAI) for scaling: An application for deducing hydrologic connectivity at watershed scale

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.02127.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.02127](https://arxiv.org/abs/2509.02127)

## 🔗 유사한 논문
- [[2025-09-18/From Sea to System_ Exploring User-Centered Explainable AI for Maritime Decision Support_20250918|From Sea to System: Exploring User-Centered Explainable AI for Maritime Decision Support]] (83.5% similar)
- [[2025-09-23/Towards a Transparent and Interpretable AI Model for Medical Image Classifications_20250923|Towards a Transparent and Interpretable AI Model for Medical Image Classifications]] (83.2% similar)
- [[2025-09-23/Energy Equity, Infrastructure and Demographic Analysis with XAI Methods_20250923|Energy Equity, Infrastructure and Demographic Analysis with XAI Methods]] (81.8% similar)
- [[2025-09-23/XAgents_ A Framework for Interpretable Rule-Based Multi-Agents Cooperation_20250923|XAgents: A Framework for Interpretable Rule-Based Multi-Agents Cooperation]] (81.3% similar)
- [[2025-09-23/See What I Mean? CUE_ A Cognitive Model of Understanding Explanations_20250923|See What I Mean? CUE: A Cognitive Model of Understanding Explanations]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Explainable Artificial Intelligence|Explainable Artificial Intelligence]]
**🔗 Specific Connectable**: [[keywords/Long Short-Term Memory Network|Long Short-Term Memory Network]]
**⚡ Unique Technical**: [[keywords/Hydrologic Connectivity|Hydrologic Connectivity]], [[keywords/Hydrologic Model|Hydrologic Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.02127v2 Announce Type: replace-cross 
Abstract: Explainable artificial intelligence (XAI) methods have been applied to interpret deep learning model results. However, applications that integrate XAI with established hydrologic knowledge for process understanding remain limited. Here we show that XAI method, applied at point-scale, could be used for cross-scale aggregation of hydrologic responses, a fundamental question in scaling problems, using hydrologic connectivity as a demonstration. Soil moisture and its movement generated by physically based hydrologic model were used to train a long short-term memory (LSTM) network, whose impacts of inputs were evaluated by XAI methods. Our results suggest that XAI-based classification can effectively identify the differences in the functional roles of various sub-regions at watershed scale. The aggregated XAI results could be considered as an explicit and quantitative indicator of hydrologic connectivity development, offering insights to hydrological organization. This framework could be used to facilitate aggregation of other geophysical responses to advance process understandings.

## 📝 요약

이 논문은 설명 가능한 인공지능(XAI) 방법론을 활용하여 심층 학습 모델의 결과를 해석하고, 이를 수문학적 지식과 통합하여 과정 이해를 돕는 연구를 다루고 있습니다. 연구에서는 물리 기반 수문 모델로 생성된 토양 수분 데이터를 사용하여 장단기 메모리 네트워크(LSTM)를 훈련시켰고, XAI 방법을 통해 입력 변수의 영향을 평가했습니다. 그 결과, XAI 기반 분류가 유역 규모에서 다양한 하위 지역의 기능적 역할 차이를 효과적으로 식별할 수 있음을 보여주었습니다. 또한, 집계된 XAI 결과는 수문 연결성 발전의 명시적이고 정량적인 지표로 활용될 수 있으며, 이는 수문 조직에 대한 통찰을 제공합니다. 이 프레임워크는 다른 지구물리학적 반응의 집계를 촉진하여 과정 이해를 발전시키는 데 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. 설명 가능한 인공지능(XAI) 방법은 심층 학습 모델 결과 해석에 적용되지만, 수문학적 지식과 통합된 응용은 제한적이다.
- 2. XAI 방법을 점 규모에서 적용하여 수문학적 반응의 크로스 스케일 집계를 수행할 수 있으며, 이는 스케일링 문제에서 중요한 질문이다.
- 3. 물리 기반 수문 모델로 생성된 토양 수분과 그 이동을 이용하여 LSTM 네트워크를 훈련하고, 입력의 영향을 XAI 방법으로 평가하였다.
- 4. XAI 기반 분류는 유역 규모에서 다양한 하위 지역의 기능적 역할 차이를 효과적으로 식별할 수 있음을 시사한다.
- 5. 집계된 XAI 결과는 수문 연결성 개발의 명시적이고 정량적인 지표로 간주될 수 있으며, 수문 조직에 대한 통찰을 제공한다.


---

*Generated on 2025-09-24 15:36:03*