<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:36:55.310827",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Software Configuration",
    "Performance Metrics",
    "Machine Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Software Configuration": 0.78,
    "Performance Metrics": 0.77,
    "Machine Learning": 0.8
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
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the study and provide a strong connection to the field of machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.67,
        "link_intent_score": 0.85
      },
      {
        "surface": "Software Configuration",
        "canonical": "Software Configuration",
        "aliases": [
          "Configuring Software"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on using LLMs for software configuration, making it a unique technical aspect of the study.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Performance Metrics",
        "canonical": "Performance Metrics",
        "aliases": [
          "Performance Measurement"
        ],
        "category": "specific_connectable",
        "rationale": "Performance metrics are crucial for evaluating the effectiveness of software configurations.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Machine Learning Techniques",
        "canonical": "Machine Learning",
        "aliases": [
          "ML Techniques"
        ],
        "category": "broad_technical",
        "rationale": "Machine learning techniques are used to explore configuration spaces, linking to broader machine learning concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "execution time",
      "memory usage",
      "binary size",
      "bitrate"
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
        "specificity": 0.67,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Software Configuration",
      "resolved_canonical": "Software Configuration",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Performance Metrics",
      "resolved_canonical": "Performance Metrics",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Machine Learning Techniques",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Prompting for Performance: Exploring LLMs for Configuring Software

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.09790.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2507.09790](https://arxiv.org/abs/2507.09790)

## 🔗 유사한 논문
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (87.7% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (86.0% similar)
- [[2025-09-23/Measuring Scalar Constructs in Social Science with LLMs_20250923|Measuring Scalar Constructs in Social Science with LLMs]] (85.8% similar)
- [[2025-09-24/From Parameters to Performance_ A Data-Driven Study on LLM Structure and Development_20250924|From Parameters to Performance: A Data-Driven Study on LLM Structure and Development]] (85.7% similar)
- [[2025-09-23/Large Language Models as End-to-end Combinatorial Optimization Solvers_20250923|Large Language Models as End-to-end Combinatorial Optimization Solvers]] (85.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Performance Metrics|Performance Metrics]]
**⚡ Unique Technical**: [[keywords/Software Configuration|Software Configuration]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.09790v2 Announce Type: replace-cross 
Abstract: Software systems usually provide numerous configuration options that can affect performance metrics such as execution time, memory usage, binary size, or bitrate. On the one hand, making informed decisions is challenging and requires domain expertise in options and their combinations. On the other hand, machine learning techniques can search vast configuration spaces, but with a high computational cost, since concrete executions of numerous configurations are required. In this exploratory study, we investigate whether large language models (LLMs) can assist in performance-oriented software configuration through prompts. We evaluate several LLMs on tasks including identifying relevant options, ranking configurations, and recommending performant configurations across various configurable systems, such as compilers, video encoders, and SAT solvers. Our preliminary results reveal both positive abilities and notable limitations: depending on the task and systems, LLMs can well align with expert knowledge, whereas hallucinations or superficial reasoning can emerge in other cases. These findings represent a first step toward systematic evaluations and the design of LLM-based solutions to assist with software configuration.

## 📝 요약

이 연구는 대형 언어 모델(LLM)이 성능 중심의 소프트웨어 구성에 도움을 줄 수 있는지를 탐구합니다. 연구진은 LLM을 사용하여 관련 옵션 식별, 구성 순위 매기기, 성능이 좋은 구성 추천 등의 작업을 수행하고, 컴파일러, 비디오 인코더, SAT 솔버 등 다양한 시스템에서 이를 평가했습니다. 초기 결과는 LLM이 전문가 지식과 잘 맞아떨어지는 경우도 있지만, 환각이나 피상적인 추론이 나타날 수 있음을 보여줍니다. 이는 LLM 기반 소프트웨어 구성 지원 솔루션 설계를 위한 체계적인 평가의 첫 단계로 의미가 있습니다.

## 🎯 주요 포인트

- 1. 소프트웨어 시스템의 성능 지표에 영향을 미치는 다양한 구성 옵션을 이해하고 결정하는 것은 도메인 전문 지식이 필요하다.
- 2. 머신러닝 기법은 방대한 구성 공간을 탐색할 수 있지만, 많은 구성의 구체적인 실행이 필요하여 높은 계산 비용이 든다.
- 3. 대형 언어 모델(LLM)이 프롬프트를 통해 성능 지향 소프트웨어 구성에 도움을 줄 수 있는지를 탐구하였다.
- 4. 여러 LLM을 사용하여 관련 옵션 식별, 구성 순위 매기기, 성능이 좋은 구성 추천 등의 작업을 평가하였다.
- 5. 초기 결과는 LLM이 전문가 지식과 잘 일치할 수 있지만, 경우에 따라 환각이나 피상적 추론이 나타날 수 있음을 보여준다.


---

*Generated on 2025-09-24 14:36:55*