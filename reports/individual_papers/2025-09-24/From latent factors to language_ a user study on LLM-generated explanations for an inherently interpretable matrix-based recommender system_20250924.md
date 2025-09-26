<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:31:15.313277",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Explainable AI",
    "Matrix Factorization",
    "User-Centered Design"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Explainable AI": 0.82,
    "Matrix Factorization": 0.78,
    "User-Centered Design": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language Model"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's methodology and are a key concept in modern AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Explainable AI",
        "canonical": "Explainable AI",
        "aliases": [
          "XAI",
          "Interpretable AI"
        ],
        "category": "specific_connectable",
        "rationale": "The paper focuses on generating explanations, making Explainable AI a critical linking concept.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.81,
        "link_intent_score": 0.82
      },
      {
        "surface": "Matrix Factorization",
        "canonical": "Matrix Factorization",
        "aliases": [
          "Constrained Matrix Factorization"
        ],
        "category": "unique_technical",
        "rationale": "Matrix Factorization is the core mathematical technique used in the recommendation model.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "User-Centered Approach",
        "canonical": "User-Centered Design",
        "aliases": [
          "User-Centered Methodology"
        ],
        "category": "evolved_concepts",
        "rationale": "The study's focus on user feedback aligns with the principles of User-Centered Design.",
        "novelty_score": 0.66,
        "connectivity_score": 0.68,
        "specificity_score": 0.77,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "study"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Explainable AI",
      "resolved_canonical": "Explainable AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.81,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Matrix Factorization",
      "resolved_canonical": "Matrix Factorization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "User-Centered Approach",
      "resolved_canonical": "User-Centered Design",
      "decision": "linked",
      "scores": {
        "novelty": 0.66,
        "connectivity": 0.68,
        "specificity": 0.77,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# From latent factors to language: a user study on LLM-generated explanations for an inherently interpretable matrix-based recommender system

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18980.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18980](https://arxiv.org/abs/2509.18980)

## 🔗 유사한 논문
- [[2025-09-23/Challenging the Evaluator_ LLM Sycophancy Under User Rebuttal_20250923|Challenging the Evaluator: LLM Sycophancy Under User Rebuttal]] (86.3% similar)
- [[2025-09-22/Quantifying Uncertainty in Natural Language Explanations of Large Language Models for Question Answering_20250922|Quantifying Uncertainty in Natural Language Explanations of Large Language Models for Question Answering]] (86.1% similar)
- [[2025-09-23/See What I Mean? CUE_ A Cognitive Model of Understanding Explanations_20250923|See What I Mean? CUE: A Cognitive Model of Understanding Explanations]] (85.3% similar)
- [[2025-09-23/No Need for Explanations_ LLMs can implicitly learn from mistakes in-context_20250923|No Need for Explanations: LLMs can implicitly learn from mistakes in-context]] (85.1% similar)
- [[2025-09-22/Bias Beware_ The Impact of Cognitive Biases on LLM-Driven Product Recommendations_20250922|Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations]] (84.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Explainable AI|Explainable AI]]
**⚡ Unique Technical**: [[keywords/Matrix Factorization|Matrix Factorization]]
**🚀 Evolved Concepts**: [[keywords/User-Centered Design|User-Centered Design]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18980v1 Announce Type: new 
Abstract: We investigate whether large language models (LLMs) can generate effective, user-facing explanations from a mathematically interpretable recommendation model. The model is based on constrained matrix factorization, where user types are explicitly represented and predicted item scores share the same scale as observed ratings, making the model's internal representations and predicted scores directly interpretable. This structure is translated into natural language explanations using carefully designed LLM prompts. Many works in explainable AI rely on automatic evaluation metrics, which often fail to capture users' actual needs and perceptions. In contrast, we adopt a user-centered approach: we conduct a study with 326 participants who assessed the quality of the explanations across five key dimensions-transparency, effectiveness, persuasion, trust, and satisfaction-as well as the recommendations themselves.To evaluate how different explanation strategies are perceived, we generate multiple explanation types from the same underlying model, varying the input information provided to the LLM. Our analysis reveals that all explanation types are generally well received, with moderate statistical differences between strategies. User comments further underscore how participants react to each type of explanation, offering complementary insights beyond the quantitative results.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 수학적으로 해석 가능한 추천 모델로부터 효과적인 사용자 중심 설명을 생성할 수 있는지를 연구합니다. 이 모델은 제한된 행렬 분해에 기반하여 사용자 유형을 명시적으로 표현하고, 예측된 아이템 점수가 관찰된 평가와 동일한 척도를 공유합니다. 이를 통해 모델의 내부 표현과 예측 점수를 직접 해석할 수 있습니다. 자연어 설명은 신중하게 설계된 LLM 프롬프트를 통해 생성됩니다. 기존의 설명 가능한 AI 연구는 자동 평가 지표에 의존하지만, 이는 사용자의 실제 요구와 인식을 잘 반영하지 못합니다. 본 연구는 사용자 중심 접근 방식을 채택하여 326명의 참가자가 설명의 투명성, 효과성, 설득력, 신뢰도, 만족도 및 추천 품질을 평가했습니다. 다양한 입력 정보를 LLM에 제공하여 여러 설명 유형을 생성하고, 이들의 인식을 분석했습니다. 모든 설명 유형이 대체로 긍정적으로 평가되었으며, 전략 간의 통계적 차이는 미미했습니다. 사용자 의견은 정량적 결과를 보완하는 추가적인 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)이 수학적으로 해석 가능한 추천 모델로부터 효과적인 사용자 지향 설명을 생성할 수 있는지를 조사합니다.
- 2. 제약 행렬 분해를 기반으로 한 모델은 사용자 유형을 명시적으로 표현하고 예측된 항목 점수가 관찰된 평가와 같은 척도를 공유하여 모델의 내부 표현과 예측 점수를 직접 해석할 수 있게 합니다.
- 3. 사용자 중심 접근 방식을 채택하여 326명의 참가자가 설명의 투명성, 효과성, 설득력, 신뢰, 만족도 및 추천의 질을 평가하는 연구를 수행했습니다.
- 4. 동일한 모델에서 다양한 설명 유형을 생성하여 서로 다른 설명 전략이 어떻게 인식되는지를 평가했습니다.
- 5. 모든 설명 유형이 대체로 긍정적으로 받아들여졌으며, 전략 간에 중간 정도의 통계적 차이가 있음을 발견했습니다.


---

*Generated on 2025-09-24 13:31:15*