---
keywords:
  - Large Language Model
  - Targeted Persuasion Score
  - Wasserstein Distance
  - Persuasiveness
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17879
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:11:38.565592",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Targeted Persuasion Score",
    "Wasserstein Distance",
    "Persuasiveness"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Targeted Persuasion Score": 0.75,
    "Wasserstein Distance": 0.78,
    "Persuasiveness": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LM",
          "language model"
        ],
        "category": "broad_technical",
        "rationale": "Essential for understanding the context adaptation and persuasion capabilities discussed.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "targeted persuasion score",
        "canonical": "Targeted Persuasion Score",
        "aliases": [
          "TPS"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel metric for evaluating the persuasiveness of context in language models.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Wasserstein distance",
        "canonical": "Wasserstein Distance",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Used as a mathematical tool to measure context shift in model answer distributions.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "persuasiveness",
        "canonical": "Persuasiveness",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Central concept of the paper, focusing on how context influences model responses.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "context",
      "entities",
      "answer"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "targeted persuasion score",
      "resolved_canonical": "Targeted Persuasion Score",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Wasserstein distance",
      "resolved_canonical": "Wasserstein Distance",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "persuasiveness",
      "resolved_canonical": "Persuasiveness",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# How Persuasive is Your Context?

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17879.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17879](https://arxiv.org/abs/2509.17879)

## 🔗 유사한 논문
- [[2025-09-23/TactfulToM_ Do LLMs Have the Theory of Mind Ability to Understand White Lies?_20250923|TactfulToM: Do LLMs Have the Theory of Mind Ability to Understand White Lies?]] (82.7% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (81.6% similar)
- [[2025-09-19/CLEAR_ A Comprehensive Linguistic Evaluation of Argument Rewriting by Large Language Models_20250919|CLEAR: A Comprehensive Linguistic Evaluation of Argument Rewriting by Large Language Models]] (81.4% similar)
- [[2025-09-23/Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs_ A Case Study with In-the-Wild Data_20250923|Benchmarking Contextual and Paralinguistic Reasoning in Speech-LLMs: A Case Study with In-the-Wild Data]] (81.3% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box: Interpretable LLMs via Semantic Resonance Architecture]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Wasserstein Distance|Wasserstein Distance]]
**⚡ Unique Technical**: [[keywords/Targeted Persuasion Score|Targeted Persuasion Score]], [[keywords/Persuasiveness|Persuasiveness]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17879v1 Announce Type: cross 
Abstract: Two central capabilities of language models (LMs) are: (i) drawing on prior knowledge about entities, which allows them to answer queries such as "What's the official language of Austria?", and (ii) adapting to new information provided in context, e.g., "Pretend the official language of Austria is Tagalog.", that is pre-pended to the question. In this article, we introduce targeted persuasion score (TPS), designed to quantify how persuasive a given context is to an LM where persuasion is operationalized as the ability of the context to alter the LM's answer to the question. In contrast to evaluating persuasiveness only by inspecting the greedily decoded answer under the model, TPS provides a more fine-grained view of model behavior. Based on the Wasserstein distance, TPS measures how much a context shifts a model's original answer distribution toward a target distribution. Empirically, through a series of experiments, we show that TPS captures a more nuanced notion of persuasiveness than previously proposed metrics.

## 📝 요약

이 논문은 언어 모델(LM)의 두 가지 핵심 능력인 기존 지식 활용과 새로운 정보에 대한 적응을 다룹니다. 저자들은 주어진 문맥이 LM의 답변을 얼마나 설득력 있게 변화시키는지를 측정하기 위해 '타겟 설득 점수(TPS)'를 제안합니다. TPS는 모델의 답변 분포가 목표 분포로 얼마나 이동하는지를 Wasserstein 거리로 측정하여, 기존의 단순한 답변 평가보다 더 정교한 설득력 평가를 제공합니다. 실험을 통해 TPS가 기존 지표보다 더 미세한 설득력 개념을 포착함을 입증했습니다.

## 🎯 주요 포인트

- 1. 언어 모델의 두 가지 핵심 기능은 기존 지식을 활용하여 질문에 답하는 것과 새로운 정보를 문맥에서 적응하는 것이다.
- 2. 본 논문에서는 주어진 문맥이 언어 모델에 얼마나 설득력 있는지를 정량화하기 위한 지표인 TPS(타겟 설득 점수)를 소개한다.
- 3. TPS는 모델의 원래 답변 분포가 목표 분포로 얼마나 이동하는지를 측정하여 설득력을 평가한다.
- 4. TPS는 기존의 설득력 평가 방식보다 모델의 행동을 더 세밀하게 분석할 수 있는 도구를 제공한다.
- 5. 실험을 통해 TPS가 이전에 제안된 지표들보다 더 미묘한 설득력 개념을 포착함을 입증하였다.


---

*Generated on 2025-09-24 00:11:38*