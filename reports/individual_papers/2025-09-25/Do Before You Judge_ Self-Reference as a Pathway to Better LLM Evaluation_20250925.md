---
keywords:
  - Large Language Model Evaluation
  - Self-Reference Evaluation
  - Large Language Model
  - Model Abilities Correlation
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19880
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:52:26.009322",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model Evaluation",
    "Self-Reference Evaluation",
    "Large Language Model",
    "Model Abilities Correlation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model Evaluation": 0.78,
    "Self-Reference Evaluation": 0.82,
    "Large Language Model": 0.85,
    "Model Abilities Correlation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLM-as-Judge",
        "canonical": "Large Language Model Evaluation",
        "aliases": [
          "LLM Evaluation",
          "LLM Judge"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a specific framework for evaluating AI models, which is central to the paper's contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "self-reference-guided evaluation",
        "canonical": "Self-Reference Evaluation",
        "aliases": [
          "Self-Reference Method"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel evaluation strategy introduced in the paper, enhancing the linkage between generation and judgment abilities.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper, this term ties the evaluation framework to a well-established concept in AI.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "generation and judgment abilities",
        "canonical": "Model Abilities Correlation",
        "aliases": [
          "Generation-Judgment Correlation"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on the correlation between these abilities, which is a key aspect of the proposed evaluation strategy.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "task",
      "sensitivity"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLM-as-Judge",
      "resolved_canonical": "Large Language Model Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "self-reference-guided evaluation",
      "resolved_canonical": "Self-Reference Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Large Language Model",
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
      "candidate_surface": "generation and judgment abilities",
      "resolved_canonical": "Model Abilities Correlation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Do Before You Judge: Self-Reference as a Pathway to Better LLM Evaluation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19880.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19880](https://arxiv.org/abs/2509.19880)

## 🔗 유사한 논문
- [[2025-09-23/Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues_20250923|Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues]] (86.5% similar)
- [[2025-09-25/Unveiling the Merits and Defects of LLMs in Automatic Review Generation for Scientific Papers_20250925|Unveiling the Merits and Defects of LLMs in Automatic Review Generation for Scientific Papers]] (86.2% similar)
- [[2025-09-24/Analyzing Uncertainty of LLM-as-a-Judge_ Interval Evaluations with Conformal Prediction_20250924|Analyzing Uncertainty of LLM-as-a-Judge: Interval Evaluations with Conformal Prediction]] (85.4% similar)
- [[2025-09-24/AECBench_ A Hierarchical Benchmark for Knowledge Evaluation of Large Language Models in the AEC Field_20250924|AECBench: A Hierarchical Benchmark for Knowledge Evaluation of Large Language Models in the AEC Field]] (85.3% similar)
- [[2025-09-23/Improving User Interface Generation Models from Designer Feedback_20250923|Improving User Interface Generation Models from Designer Feedback]] (84.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Large Language Model Evaluation|Large Language Model Evaluation]], [[keywords/Self-Reference Evaluation|Self-Reference Evaluation]], [[keywords/Model Abilities Correlation|Model Abilities Correlation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19880v1 Announce Type: cross 
Abstract: LLM-as-Judge frameworks are increasingly popular for AI evaluation, yet research findings on the relationship between models' generation and judgment abilities remain inconsistent. We investigate this relationship through systematic dataset- and instance-level analyses across 11 models and 21 diverse tasks. Despite both capabilities relying on the same underlying knowledge, our analyses reveal they are only weakly correlated, primarily due to LLMs' sensitivity to the responses being judged. To address this, we propose a self-reference-guided evaluation strategy that leverages a model's own answers as references. This approach significantly strengthens the correlation between generation and judgment abilities, offering a practical path to align these skills and providing a reliable proxy for model selection in evaluation tasks.

## 📝 요약

이 논문은 AI 평가에서 사용되는 LLM-as-Judge 프레임워크의 생성 능력과 판단 능력 간의 관계를 조사합니다. 11개 모델과 21개 다양한 작업을 통해 분석한 결과, 두 능력은 동일한 지식에 기반하지만 약하게 상관되어 있음을 발견했습니다. 이는 LLM이 평가하는 응답에 민감하기 때문입니다. 이를 해결하기 위해, 모델의 자체 응답을 참조로 사용하는 자기 참조 기반 평가 전략을 제안합니다. 이 접근법은 생성과 판단 능력 간의 상관성을 강화하여, 평가 작업에서 모델 선택의 신뢰할 수 있는 기준을 제공합니다.

## 🎯 주요 포인트

- 1. LLM-as-Judge 프레임워크는 AI 평가에서 인기를 끌고 있지만, 모델의 생성 능력과 판단 능력 간의 관계에 대한 연구 결과는 일관되지 않습니다.
- 2. 11개의 모델과 21개의 다양한 작업을 통해 데이터셋 및 인스턴스 수준에서 이 관계를 체계적으로 조사했습니다.
- 3. 분석 결과, 두 능력이 동일한 지식에 기반을 두고 있음에도 불구하고, LLM의 응답에 대한 민감성 때문에 약한 상관관계를 보였습니다.
- 4. 이를 해결하기 위해, 모델의 자체 답변을 참조로 활용하는 자기 참조 기반 평가 전략을 제안했습니다.
- 5. 이 접근법은 생성 및 판단 능력 간의 상관관계를 크게 강화하여, 평가 작업에서 모델 선택을 위한 신뢰할 수 있는 기준을 제공합니다.


---

*Generated on 2025-09-25 15:52:26*