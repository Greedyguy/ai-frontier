<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:09:33.203279",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Election-related Knowledge",
    "Demographic Steering",
    "Implicit Predictions"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Election-related Knowledge": 0.78,
    "Demographic Steering": 0.8,
    "Implicit Predictions": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study, connecting to broader discussions on AI's role in elections.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Election-related knowledge",
        "canonical": "Election-related Knowledge",
        "aliases": [
          "Election Knowledge"
        ],
        "category": "unique_technical",
        "rationale": "Specific to the study's focus on how LLMs handle electoral information.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Demographic steering",
        "canonical": "Demographic Steering",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Highlights the study's analysis of LLM responses influenced by demographic factors.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Implicit predictions",
        "canonical": "Implicit Predictions",
        "aliases": [
          "Model Predictions"
        ],
        "category": "unique_technical",
        "rationale": "Focuses on the models' ability to predict election outcomes, a novel aspect of the study.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "election season",
      "platforms",
      "methodology"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Election-related knowledge",
      "resolved_canonical": "Election-related Knowledge",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Demographic steering",
      "resolved_canonical": "Demographic Steering",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Implicit predictions",
      "resolved_canonical": "Implicit Predictions",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Large-Scale, Longitudinal Study of Large Language Models During the 2024 US Election Season

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18446.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18446](https://arxiv.org/abs/2509.18446)

## 🔗 유사한 논문
- [[2025-09-23/Measuring Scalar Constructs in Social Science with LLMs_20250923|Measuring Scalar Constructs in Social Science with LLMs]] (84.3% similar)
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (83.7% similar)
- [[2025-09-23/Steering Towards Fairness_ Mitigating Political Bias in LLMs_20250923|Steering Towards Fairness: Mitigating Political Bias in LLMs]] (82.6% similar)
- [[2025-09-24/From Parameters to Performance_ A Data-Driven Study on LLM Structure and Development_20250924|From Parameters to Performance: A Data-Driven Study on LLM Structure and Development]] (82.4% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Election-related Knowledge|Election-related Knowledge]], [[keywords/Demographic Steering|Demographic Steering]], [[keywords/Implicit Predictions|Implicit Predictions]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18446v1 Announce Type: cross 
Abstract: The 2024 US presidential election is the first major contest to occur in the US since the popularization of large language models (LLMs). Building on lessons from earlier shifts in media (most notably social media's well studied role in targeted messaging and political polarization) this moment raises urgent questions about how LLMs may shape the information ecosystem and influence political discourse. While platforms have announced some election safeguards, how well they work in practice remains unclear. Against this backdrop, we conduct a large-scale, longitudinal study of 12 models, queried using a structured survey with over 12,000 questions on a near-daily cadence from July through November 2024. Our design systematically varies content and format, resulting in a rich dataset that enables analyses of the models' behavior over time (e.g., across model updates), sensitivity to steering, responsiveness to instructions, and election-related knowledge and "beliefs." In the latter half of our work, we perform four analyses of the dataset that (i) study the longitudinal variation of model behavior during election season, (ii) illustrate the sensitivity of election-related responses to demographic steering, (iii) interrogate the models' beliefs about candidates' attributes, and (iv) reveal the models' implicit predictions of the election outcome. To facilitate future evaluations of LLMs in electoral contexts, we detail our methodology, from question generation to the querying pipeline and third-party tooling. We also publicly release our dataset at https://huggingface.co/datasets/sarahcen/llm-election-data-2024

## 📝 요약

이 논문은 2024년 미국 대통령 선거와 대형 언어 모델(LLM)의 영향력을 연구합니다. 연구진은 12개의 모델을 대상으로 2024년 7월부터 11월까지 12,000개 이상의 질문을 통해 대규모 종단 연구를 수행했습니다. 연구는 모델의 행동 변화, 지시 민감성, 선거 관련 지식 및 "신념"을 분석했습니다. 주요 발견사항으로는 (i) 선거 기간 동안 모델 행동의 변화, (ii) 인구 통계적 조작에 대한 민감성, (iii) 후보 속성에 대한 모델의 신념, (iv) 암묵적 선거 결과 예측이 포함됩니다. 연구 방법론과 데이터셋은 공개되어 향후 연구에 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. 2024년 미국 대통령 선거는 대형 언어 모델(LLM)의 대중화 이후 처음으로 치러지는 주요 선거로, LLM이 정보 생태계와 정치적 담론에 미칠 영향에 대한 긴급한 질문이 제기된다.
- 2. 연구는 2024년 7월부터 11월까지 12개 모델을 대상으로 12,000개 이상의 질문을 통해 대규모, 종단적 조사를 수행하여 모델의 행동 변화를 분석한다.
- 3. 데이터셋 분석을 통해 선거 시즌 동안 모델 행동의 종단적 변화, 인구통계학적 조작에 대한 민감성, 후보 속성에 대한 모델의 신념, 선거 결과에 대한 암묵적 예측을 연구한다.
- 4. 연구는 선거 관련 맥락에서 LLM의 평가를 돕기 위해 질문 생성부터 쿼리 파이프라인 및 타사 도구까지의 방법론을 상세히 설명하고, 데이터셋을 공개한다.


---

*Generated on 2025-09-24 15:09:33*