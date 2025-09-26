---
keywords:
  - Large Language Model
  - HEXACO Personality Framework
  - Bias and Toxicity
  - Content Safety
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2502.12566
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:35:27.661033",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "HEXACO Personality Framework",
    "Bias and Toxicity",
    "Content Safety"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "HEXACO Personality Framework": 0.8,
    "Bias and Toxicity": 0.78,
    "Content Safety": 0.77
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
          "Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study, linking to foundational concepts in AI.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "HEXACO personality framework",
        "canonical": "HEXACO Personality Framework",
        "aliases": [
          "HEXACO"
        ],
        "category": "unique_technical",
        "rationale": "Key framework used in the study for assessing personality traits.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "bias and toxicity",
        "canonical": "Bias and Toxicity",
        "aliases": [
          "bias",
          "toxicity"
        ],
        "category": "specific_connectable",
        "rationale": "Critical aspects of LLM outputs being examined.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "content safety",
        "canonical": "Content Safety",
        "aliases": [
          "safety",
          "content moderation"
        ],
        "category": "specific_connectable",
        "rationale": "Important consideration for LLM deployment and research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "HEXACO personality framework",
      "resolved_canonical": "HEXACO Personality Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "bias and toxicity",
      "resolved_canonical": "Bias and Toxicity",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "content safety",
      "resolved_canonical": "Content Safety",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Exploring the Impact of Personality Traits on LLM Bias and Toxicity

**Korean Title:** 성격 특성이 대규모 언어 모델의 편향성과 유해성에 미치는 영향 탐구

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.12566.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2502.12566](https://arxiv.org/abs/2502.12566)

## 🔗 유사한 논문
- [[2025-09-18/Do LLMs Align Human Values Regarding Social Biases? Judging and Explaining Social Biases with LLMs_20250918|Do LLMs Align Human Values Regarding Social Biases? Judging and Explaining Social Biases with LLMs]] (86.5% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (86.4% similar)
- [[2025-09-22/Bias Beware_ The Impact of Cognitive Biases on LLM-Driven Product Recommendations_20250922|Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations]] (86.0% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (85.3% similar)
- [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM: Language of Browsing]] (85.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Bias and Toxicity|Bias and Toxicity]], [[keywords/Content Safety|Content Safety]]
**⚡ Unique Technical**: [[keywords/HEXACO Personality Framework|HEXACO Personality Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.12566v3 Announce Type: replace 
Abstract: With the different roles that AI is expected to play in human life, imbuing large language models (LLMs) with different personalities has attracted increasing research interests. While the "personification" enhances human experiences of interactivity and adaptability of LLMs, it gives rise to critical concerns about content safety, particularly regarding bias, sentiment and toxicity of LLM generation. This study explores how assigning different personality traits to LLMs affects the toxicity and biases of their outputs. Leveraging the widely accepted HEXACO personality framework developed in social psychology, we design experimentally sound prompts to test three LLMs' performance on three toxic and bias benchmarks. The findings demonstrate the sensitivity of all three models to HEXACO personality traits and, more importantly, a consistent variation in the biases, negative sentiment and toxicity of their output. In particular, adjusting the levels of several personality traits can effectively reduce bias and toxicity in model performance, similar to humans' correlations between personality traits and toxic behaviors. The findings highlight the additional need to examine content safety besides the efficiency of training or fine-tuning methods for LLM personification. They also suggest a potential for the adjustment of personalities to be a simple and low-cost method to conduct controlled text generation.

## 🔍 Abstract (한글 번역)

arXiv:2502.12566v3 발표 유형: 교체  
초록: 인공지능이 인간 생활에서 다양한 역할을 수행할 것으로 기대됨에 따라, 대형 언어 모델(LLM)에 다양한 성격을 부여하는 것이 점점 더 많은 연구 관심을 끌고 있습니다. "인격화"는 LLM의 상호작용성과 적응성을 향상시키지만, LLM 생성의 편향, 감정 및 유해성에 관한 콘텐츠 안전성에 대한 중요한 우려를 야기합니다. 본 연구는 LLM에 다양한 성격 특성을 부여하는 것이 그들의 출력물의 유해성과 편향에 어떻게 영향을 미치는지를 탐구합니다. 사회심리학에서 개발된 널리 인정받는 HEXACO 성격 프레임워크를 활용하여, 세 가지 유해성과 편향 벤치마크에서 세 가지 LLM의 성능을 테스트하기 위한 실험적으로 타당한 프롬프트를 설계합니다. 연구 결과는 세 모델 모두가 HEXACO 성격 특성에 민감하며, 더 중요하게는 그들의 출력물의 편향, 부정적 감정 및 유해성에서 일관된 변화를 보여줍니다. 특히, 여러 성격 특성의 수준을 조정하는 것이 모델 성능의 편향과 유해성을 효과적으로 줄일 수 있으며, 이는 인간의 성격 특성과 유해 행동 간의 상관관계와 유사합니다. 이 연구 결과는 LLM 인격화를 위한 훈련 또는 미세 조정 방법의 효율성 외에도 콘텐츠 안전성을 검토할 추가적인 필요성을 강조합니다. 또한, 성격 조정이 통제된 텍스트 생성을 수행하는 간단하고 저비용의 방법이 될 가능성을 시사합니다.

## 📝 요약

이 연구는 대형 언어 모델(LLM)에 다양한 성격 특성을 부여하는 것이 모델의 편향성과 유해성에 어떤 영향을 미치는지를 탐구합니다. 사회심리학에서 널리 사용되는 HEXACO 성격 프레임워크를 활용하여, 세 가지 LLM의 성능을 세 가지 유해성과 편향성 기준으로 실험적으로 평가했습니다. 연구 결과, 모든 모델이 HEXACO 성격 특성에 민감하며, 성격 특성을 조정함으로써 편향성과 유해성을 효과적으로 줄일 수 있음을 발견했습니다. 이는 LLM의 성격화에서 콘텐츠 안전성을 고려해야 할 필요성을 강조하며, 성격 조정이 통제된 텍스트 생성을 위한 간단하고 저비용의 방법이 될 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)에 다양한 성격을 부여하는 것은 상호작용성과 적응성을 높이는 동시에 편향, 감정 및 독성에 대한 우려를 불러일으킵니다.
- 2. 연구는 HEXACO 성격 모델을 활용하여 LLM의 성격 특성이 출력의 독성과 편향에 미치는 영향을 조사하였습니다.
- 3. 실험 결과, LLM의 성격 특성을 조정함으로써 편향과 독성을 효과적으로 줄일 수 있음을 발견했습니다.
- 4. 연구는 LLM의 인격화에서 훈련 효율성 외에도 콘텐츠 안전성을 검토할 필요성을 강조합니다.
- 5. 성격 조정이 통제된 텍스트 생성을 위한 간단하고 저비용의 방법이 될 가능성을 제안합니다.


---

*Generated on 2025-09-23 09:35:27*