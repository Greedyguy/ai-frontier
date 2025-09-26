---
keywords:
  - Large Language Model
  - Cross-Lingual Reward Model
  - Mathematical Reasoning
  - Multilingual Language Model
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15811
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:16:32.119910",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Cross-Lingual Reward Model",
    "Mathematical Reasoning",
    "Multilingual Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Cross-Lingual Reward Model": 0.78,
    "Mathematical Reasoning": 0.8,
    "Multilingual Language Model": 0.77
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
        "rationale": "Central to the study, linking to broader discussions on language model capabilities.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cross-Lingual Reward Model",
        "canonical": "Cross-Lingual Reward Model",
        "aliases": [
          "Cross-Lingual RM"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to reward modeling across languages, enhancing multilingual reasoning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Mathematical Reasoning",
        "canonical": "Mathematical Reasoning",
        "aliases": [
          "Math Reasoning"
        ],
        "category": "specific_connectable",
        "rationale": "Focuses on a specific application of LLMs, relevant to specialized reasoning tasks.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multilingual Models",
        "canonical": "Multilingual Language Model",
        "aliases": [
          "Multilingual LLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the multilingual aspect of LLMs, connecting to cross-lingual research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method",
      "experiment"
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
      "candidate_surface": "Cross-Lingual Reward Model",
      "resolved_canonical": "Cross-Lingual Reward Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Mathematical Reasoning",
      "resolved_canonical": "Mathematical Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multilingual Models",
      "resolved_canonical": "Multilingual Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Best-of-L: Cross-Lingual Reward Modeling for Mathematical Reasoning

**Korean Title:** Best-of-L: 수학적 추론을 위한 교차 언어 보상 모델링

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15811.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15811](https://arxiv.org/abs/2509.15811)

## 🔗 유사한 논문
- [[2025-09-22/Language Mixing in Reasoning Language Models_ Patterns, Impact, and Internal Causes_20250922|Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes]] (87.0% similar)
- [[2025-09-22/Entropy-Regularized Process Reward Model_20250922|Entropy-Regularized Process Reward Model]] (85.2% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (84.9% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (84.9% similar)
- [[2025-09-22/Reward Hacking Mitigation using Verifiable Composite Rewards_20250922|Reward Hacking Mitigation using Verifiable Composite Rewards]] (84.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Mathematical Reasoning|Mathematical Reasoning]], [[keywords/Multilingual Language Model|Multilingual Language Model]]
**⚡ Unique Technical**: [[keywords/Cross-Lingual Reward Model|Cross-Lingual Reward Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15811v1 Announce Type: cross 
Abstract: While the reasoning abilities of large language models (LLMs) continue to advance, it remains unclear how such ability varies across languages in multilingual LLMs and whether different languages produce reasoning paths that complement each other. To investigate this question, we train a reward model to rank generated responses for a given question across languages. Our results show that our cross-lingual reward model substantially improves mathematical reasoning performance compared to using reward modeling within a single language, benefiting even high-resource languages. While English often exhibits the highest performance in multilingual models, we find that cross-lingual sampling particularly benefits English under low sampling budgets. Our findings reveal new opportunities to improve multilingual reasoning by leveraging the complementary strengths of diverse languages.

## 🔍 Abstract (한글 번역)

arXiv:2509.15811v1 발표 유형: 교차  
초록: 대형 언어 모델(LLM)의 추론 능력이 계속 발전하고 있지만, 다국어 LLM에서 이러한 능력이 언어에 따라 어떻게 달라지는지, 그리고 서로 다른 언어가 서로 보완하는 추론 경로를 생성하는지 여부는 여전히 불분명합니다. 이 질문을 조사하기 위해, 우리는 여러 언어에 걸쳐 주어진 질문에 대한 생성된 응답을 순위 매기는 보상 모델을 훈련했습니다. 우리의 결과는 단일 언어 내에서 보상 모델링을 사용하는 것과 비교하여, 교차 언어 보상 모델이 수학적 추론 성능을 상당히 향상시키며, 심지어 자원이 풍부한 언어에도 이점이 있음을 보여줍니다. 영어는 종종 다국어 모델에서 가장 높은 성능을 보이지만, 우리는 교차 언어 샘플링이 낮은 샘플링 예산 하에서 특히 영어에 이점을 준다는 것을 발견했습니다. 우리의 발견은 다양한 언어의 상호 보완적인 강점을 활용하여 다국어 추론을 개선할 수 있는 새로운 기회를 제시합니다.

## 📝 요약

이 논문은 다국어 대형 언어 모델(LLM)에서 언어 간 추론 능력의 차이를 조사합니다. 연구팀은 언어별로 생성된 응답을 평가하는 보상 모델을 개발하여, 수학적 추론 성능을 향상시켰습니다. 특히, 영어는 다국어 모델에서 높은 성능을 보이지만, 저비용 샘플링 환경에서는 언어 간 샘플링이 영어의 성능을 더욱 개선시킵니다. 이 연구는 다양한 언어의 상호 보완적 강점을 활용하여 다국어 추론을 개선할 수 있는 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 추론 능력은 언어에 따라 다르게 나타나며, 다양한 언어가 서로 보완적인 추론 경로를 생성할 수 있는지에 대한 연구가 필요하다.
- 2. 연구 결과, 교차 언어 보상 모델이 단일 언어 보상 모델에 비해 수학적 추론 성능을 크게 향상시키며, 이는 자원이 풍부한 언어에도 이점을 제공한다.
- 3. 영어는 다국어 모델에서 종종 가장 높은 성능을 보이지만, 교차 언어 샘플링은 낮은 샘플링 예산 하에서 특히 영어에 이점을 준다.
- 4. 다양한 언어의 상호 보완적 강점을 활용하여 다국어 추론을 개선할 수 있는 새로운 기회를 발견했다.


---

*Generated on 2025-09-23 09:16:32*