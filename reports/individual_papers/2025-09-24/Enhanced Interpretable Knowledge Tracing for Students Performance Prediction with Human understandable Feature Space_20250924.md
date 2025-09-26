<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:43:40.335585",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Knowledge Tracing",
    "Deep Learning",
    "Human-understandable Features",
    "Cognitive Theory"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Knowledge Tracing": 0.8,
    "Deep Learning": 0.75,
    "Human-understandable Features": 0.78,
    "Cognitive Theory": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Knowledge Tracing",
        "canonical": "Knowledge Tracing",
        "aliases": [
          "KT"
        ],
        "category": "unique_technical",
        "rationale": "Knowledge Tracing is a specific concept central to the paper's focus on student performance prediction.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational technology used in the KT models discussed in the paper.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "Human-understandable Features",
        "canonical": "Human-understandable Features",
        "aliases": [
          "Interpretable Features"
        ],
        "category": "unique_technical",
        "rationale": "These features are crucial for enhancing interpretability in the KT models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Cognitive Theory",
        "canonical": "Cognitive Theory",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Cognitive Theory provides the theoretical framework for aligning KT models with educational psychology.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "students",
      "performance",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Knowledge Tracing",
      "resolved_canonical": "Knowledge Tracing",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
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
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Human-understandable Features",
      "resolved_canonical": "Human-understandable Features",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Cognitive Theory",
      "resolved_canonical": "Cognitive Theory",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Enhanced Interpretable Knowledge Tracing for Students Performance Prediction with Human understandable Feature Space

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18231.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18231](https://arxiv.org/abs/2509.18231)

## 🔗 유사한 논문
- [[2025-09-23/Advancing Knowledge Tracing by Exploring Follow-up Performance Trends_20250923|Advancing Knowledge Tracing by Exploring Follow-up Performance Trends]] (88.7% similar)
- [[2025-09-19/Delta Knowledge Distillation for Large Language Models_20250919|Delta Knowledge Distillation for Large Language Models]] (83.3% similar)
- [[2025-09-22/Boosting Active Learning with Knowledge Transfer_20250922|Boosting Active Learning with Knowledge Transfer]] (82.0% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (81.6% similar)
- [[2025-09-23/Model Guidance via Robust Feature Attribution_20250923|Model Guidance via Robust Feature Attribution]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Cognitive Theory|Cognitive Theory]]
**⚡ Unique Technical**: [[keywords/Knowledge Tracing|Knowledge Tracing]], [[keywords/Human-understandable Features|Human-understandable Features]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18231v1 Announce Type: cross 
Abstract: Knowledge Tracing (KT) plays a central role in assessing students skill mastery and predicting their future performance. While deep learning based KT models achieve superior predictive accuracy compared to traditional methods, their complexity and opacity hinder their ability to provide psychologically meaningful explanations. This disconnect between model parameters and cognitive theory poses challenges for understanding and enhancing the learning process, limiting their trustworthiness in educational applications. To address these challenges, we enhance interpretable KT models by exploring human-understandable features derived from students interaction data. By incorporating additional features, particularly those reflecting students learning abilities, our enhanced approach improves predictive accuracy while maintaining alignment with cognitive theory. Our contributions aim to balance predictive power with interpretability, advancing the utility of adaptive learning systems.

## 📝 요약

이 논문은 학생의 학습 능력을 평가하고 미래 성과를 예측하는 지식 추적(KT) 모델의 해석 가능성을 개선하는 방법을 제안합니다. 기존의 딥러닝 기반 KT 모델은 높은 예측 정확성을 제공하지만, 복잡성과 불투명성 때문에 심리적으로 의미 있는 설명을 제공하는 데 어려움이 있습니다. 이를 해결하기 위해, 학생의 상호작용 데이터에서 파생된 인간이 이해할 수 있는 특징을 탐구하여 해석 가능한 KT 모델을 강화했습니다. 특히 학생의 학습 능력을 반영하는 추가 특징을 포함함으로써, 예측 정확성을 향상시키면서도 인지 이론과의 일치를 유지했습니다. 이 연구는 예측력과 해석 가능성의 균형을 맞추어 적응형 학습 시스템의 유용성을 증진시키는 데 기여합니다.

## 🎯 주요 포인트

- 1. 지식 추적(KT)은 학생의 기술 숙달도를 평가하고 미래 성과를 예측하는 데 중요한 역할을 한다.
- 2. 딥러닝 기반 KT 모델은 전통적인 방법보다 예측 정확도가 뛰어나지만, 복잡성과 불투명성 때문에 심리적으로 의미 있는 설명을 제공하는 데 어려움이 있다.
- 3. 모델 매개변수와 인지 이론 간의 단절은 학습 과정을 이해하고 개선하는 데 도전 과제를 제시하며, 교육적 응용에서 신뢰성을 제한한다.
- 4. 학생의 상호작용 데이터에서 파생된 인간이 이해할 수 있는 특징을 탐색하여 해석 가능한 KT 모델을 강화하였다.
- 5. 학생의 학습 능력을 반영하는 추가 특징을 포함하여 예측 정확도를 개선하면서 인지 이론과의 정렬을 유지하였다.


---

*Generated on 2025-09-24 13:43:40*