---
keywords:
  - Concept Bottleneck Models
  - Large Language Model
  - Unsupervised Concept Bottleneck Models
  - Few-Shot Learning
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17522
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:54:46.210806",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Concept Bottleneck Models",
    "Large Language Model",
    "Unsupervised Concept Bottleneck Models",
    "Few-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Concept Bottleneck Models": 0.8,
    "Large Language Model": 0.85,
    "Unsupervised Concept Bottleneck Models": 0.78,
    "Few-Shot Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Concept Bottleneck Models",
        "canonical": "Concept Bottleneck Models",
        "aliases": [
          "CBM"
        ],
        "category": "unique_technical",
        "rationale": "This is a central concept of the paper, representing a specific model type that enhances interpretability.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "These models are integral to the proposed method, enabling language-based reasoning over concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Unsupervised CBMs",
        "canonical": "Unsupervised Concept Bottleneck Models",
        "aliases": [
          "Unsupervised CBM"
        ],
        "category": "unique_technical",
        "rationale": "This variant of CBMs is highlighted for its challenges and the improvements offered by the proposed method.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Few-Shot Capabilities",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "The paper leverages few-shot learning capabilities of large language models for improved interventions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
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
      "candidate_surface": "Concept Bottleneck Models",
      "resolved_canonical": "Concept Bottleneck Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Unsupervised CBMs",
      "resolved_canonical": "Unsupervised Concept Bottleneck Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Few-Shot Capabilities",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Chat-CBM: Towards Interactive Concept Bottleneck Models with Frozen Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17522.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17522](https://arxiv.org/abs/2509.17522)

## 🔗 유사한 논문
- [[2025-09-22/Bayesian Concept Bottleneck Models with LLM Priors_20250922|Bayesian Concept Bottleneck Models with LLM Priors]] (88.2% similar)
- [[2025-09-19/EnCoBo_ Energy-Guided Concept Bottlenecks for Interpretable Generation_20250919|EnCoBo: Energy-Guided Concept Bottlenecks for Interpretable Generation]] (85.4% similar)
- [[2025-09-23/MCP_ A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models_20250923|MCP: A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models]] (82.1% similar)
- [[2025-09-23/OptiChat_ Bridging Optimization Models and Practitioners with Large Language Models_20250923|OptiChat: Bridging Optimization Models and Practitioners with Large Language Models]] (81.6% similar)
- [[2025-09-23/WISE_ Weak-Supervision-Guided Step-by-Step Explanations for Multimodal LLMs in Image Classification_20250923|WISE: Weak-Supervision-Guided Step-by-Step Explanations for Multimodal LLMs in Image Classification]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Concept Bottleneck Models|Concept Bottleneck Models]], [[keywords/Unsupervised Concept Bottleneck Models|Unsupervised Concept Bottleneck Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17522v1 Announce Type: new 
Abstract: Concept Bottleneck Models (CBMs) provide inherent interpretability by first predicting a set of human-understandable concepts and then mapping them to labels through a simple classifier. While users can intervene in the concept space to improve predictions, traditional CBMs typically employ a fixed linear classifier over concept scores, which restricts interventions to manual value adjustments and prevents the incorporation of new concepts or domain knowledge at test time. These limitations are particularly severe in unsupervised CBMs, where concept activations are often noisy and densely activated, making user interventions ineffective. We introduce Chat-CBM, which replaces score-based classifiers with a language-based classifier that reasons directly over concept semantics. By grounding prediction in the semantic space of concepts, Chat-CBM preserves the interpretability of CBMs while enabling richer and more intuitive interventions, such as concept correction, addition or removal of concepts, incorporation of external knowledge, and high-level reasoning guidance. Leveraging the language understanding and few-shot capabilities of frozen large language models, Chat-CBM extends the intervention interface of CBMs beyond numerical editing and remains effective even in unsupervised settings. Experiments on nine datasets demonstrate that Chat-CBM achieves higher predictive performance and substantially improves user interactivity while maintaining the concept-based interpretability of CBMs.

## 📝 요약

이 논문에서는 Chat-CBM이라는 새로운 개념 병목 모델을 제안합니다. 기존의 개념 병목 모델은 개념 점수에 기반한 고정된 선형 분류기를 사용하여 사용자가 개념 공간에서의 개입이 제한적이었습니다. Chat-CBM은 점수 기반 분류기를 언어 기반 분류기로 대체하여 개념의 의미적 공간에서 예측을 수행합니다. 이를 통해 개념 수정, 추가, 제거, 외부 지식 통합 및 고차원적 추론 지침 등 더 풍부하고 직관적인 개입이 가능해집니다. 특히, 대형 언어 모델의 언어 이해와 소수 샷 학습 능력을 활용하여, Chat-CBM은 비지도 학습 환경에서도 효과적입니다. 9개의 데이터셋 실험 결과, Chat-CBM은 예측 성능을 높이고 사용자 상호작용을 크게 개선하면서도 개념 기반의 해석 가능성을 유지합니다.

## 🎯 주요 포인트

- 1. Concept Bottleneck Models(CBMs)는 개념을 예측하고 이를 라벨로 매핑하여 해석 가능성을 제공합니다.
- 2. 기존 CBMs는 고정된 선형 분류기를 사용하여 개념 점수에 기반한 수동 조정만 가능하며, 새로운 개념이나 도메인 지식을 테스트 시 반영할 수 없습니다.
- 3. Chat-CBM은 점수 기반 분류기를 언어 기반 분류기로 대체하여 개념 의미를 직접적으로 해석하고, 개념 수정, 추가, 제거 및 외부 지식 통합을 가능하게 합니다.
- 4. Chat-CBM은 대형 언어 모델의 언어 이해 및 소수의 샘플로 학습하는 능력을 활용하여 CBMs의 개입 인터페이스를 확장하고, 비지도 학습 환경에서도 효과적입니다.
- 5. 아홉 개의 데이터셋 실험에서 Chat-CBM은 예측 성능을 높이고 사용자 상호작용을 개선하면서 CBMs의 개념 기반 해석 가능성을 유지합니다.


---

*Generated on 2025-09-24 04:54:46*