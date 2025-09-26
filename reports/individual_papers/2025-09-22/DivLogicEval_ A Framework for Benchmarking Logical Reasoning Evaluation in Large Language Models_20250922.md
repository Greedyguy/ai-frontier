---
keywords:
  - Large Language Model
  - Logical Reasoning
  - DivLogicEval
  - Evaluation Metric for Bias Mitigation
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15587
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:06:49.012984",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Logical Reasoning",
    "DivLogicEval",
    "Evaluation Metric for Bias Mitigation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Logical Reasoning": 0.78,
    "DivLogicEval": 0.8,
    "Evaluation Metric for Bias Mitigation": 0.77
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
        "rationale": "Central to the paper's focus on evaluating logical reasoning capabilities.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "logical reasoning",
        "canonical": "Logical Reasoning",
        "aliases": [
          "logic reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Key concept for evaluating intelligence in language models, central to the paper's thesis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "DivLogicEval",
        "canonical": "DivLogicEval",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The proposed benchmark is a unique contribution of the paper.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "evaluation metric",
        "canonical": "Evaluation Metric for Bias Mitigation",
        "aliases": [
          "bias mitigation metric"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel metric to improve evaluation reliability, significant for linking.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "popular",
      "performance"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "logical reasoning",
      "resolved_canonical": "Logical Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "DivLogicEval",
      "resolved_canonical": "DivLogicEval",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "evaluation metric",
      "resolved_canonical": "Evaluation Metric for Bias Mitigation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models

**Korean Title:** DivLogicEval: 대규모 언어 모델에서 논리적 추론 평가를 벤치마킹하기 위한 프레임워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15587.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15587](https://arxiv.org/abs/2509.15587)

## 🔗 유사한 논문
- [[2025-09-19/Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (86.6% similar)
- [[2025-09-22/REFER_ Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting_20250922|REFER: Mitigating Bias in Opinion Summarisation via Frequency Framed Prompting]] (85.5% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (85.4% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text?_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text?]] (84.9% similar)
- [[2025-09-22/Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics_20250922|Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics]] (84.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Logical Reasoning|Logical Reasoning]], [[keywords/DivLogicEval|DivLogicEval]], [[keywords/Evaluation Metric for Bias Mitigation|Evaluation Metric for Bias Mitigation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15587v1 Announce Type: cross 
Abstract: Logic reasoning in natural language has been recognized as an important measure of human intelligence for Large Language Models (LLMs). Popular benchmarks may entangle multiple reasoning skills and thus provide unfaithful evaluations on the logic reasoning skill. Meanwhile, existing logic reasoning benchmarks are limited in language diversity and their distributions are deviated from the distribution of an ideal logic reasoning benchmark, which may lead to biased evaluation results. This paper thereby proposes a new classical logic benchmark DivLogicEval, consisting of natural sentences composed of diverse statements in a counterintuitive way. To ensure a more reliable evaluation, we also introduce a new evaluation metric that mitigates the influence of bias and randomness inherent in LLMs. Through experiments, we demonstrate the extent to which logical reasoning is required to answer the questions in DivLogicEval and compare the performance of different popular LLMs in conducting logical reasoning.

## 🔍 Abstract (한글 번역)

arXiv:2509.15587v1 발표 유형: 교차  
초록: 자연어에서의 논리적 추론은 대형 언어 모델(LLMs)의 인간 지능을 측정하는 중요한 척도로 인식되어 왔습니다. 인기 있는 벤치마크는 여러 추론 기술을 얽히게 하여 논리적 추론 기술에 대한 신뢰할 수 없는 평가를 제공할 수 있습니다. 동시에 기존의 논리적 추론 벤치마크는 언어 다양성이 제한적이며, 이상적인 논리적 추론 벤치마크의 분포와는 다른 분포를 가지고 있어 편향된 평가 결과를 초래할 수 있습니다. 따라서 본 논문에서는 다양한 진술로 구성된 자연 문장을 직관에 반하는 방식으로 포함하는 새로운 고전 논리 벤치마크인 DivLogicEval을 제안합니다. 보다 신뢰할 수 있는 평가를 보장하기 위해, LLM에 내재된 편향성과 무작위성의 영향을 완화하는 새로운 평가 지표도 도입합니다. 실험을 통해 DivLogicEval의 질문에 답하기 위해 요구되는 논리적 추론의 정도를 입증하고, 논리적 추론을 수행하는 데 있어 다양한 인기 있는 LLM의 성능을 비교합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 논리적 추론 능력을 평가하기 위한 새로운 벤치마크인 DivLogicEval을 제안합니다. 기존의 논리 추론 벤치마크는 언어 다양성이 부족하고 이상적인 분포와 차이가 있어 평가 결과에 편향을 초래할 수 있습니다. DivLogicEval은 다양한 진술로 구성된 자연어 문장을 사용하여 이러한 문제를 해결하고자 하며, 편향과 무작위성을 줄이기 위한 새로운 평가 지표도 도입합니다. 실험을 통해 DivLogicEval에서 논리적 추론이 얼마나 필요한지, 그리고 다양한 LLM의 성능을 비교하여 논리적 추론 능력을 평가합니다.

## 🎯 주요 포인트

- 1. 자연어에서의 논리적 추론은 대형 언어 모델(LLM)의 인간 지능 측정에 중요한 요소로 인식되고 있다.
- 2. 기존의 논리적 추론 벤치마크는 언어 다양성이 제한적이며, 이상적인 논리적 추론 벤치마크의 분포와 차이가 있어 편향된 평가 결과를 초래할 수 있다.
- 3. 새로운 논리 벤치마크인 DivLogicEval을 제안하여 다양한 진술로 구성된 자연 문장을 통해 보다 신뢰할 수 있는 평가를 목표로 한다.
- 4. 편향과 무작위성을 완화하는 새로운 평가 지표를 도입하여 LLM의 논리적 추론 능력을 보다 정확하게 평가한다.
- 5. 실험을 통해 DivLogicEval에서 논리적 추론이 필요한 정도를 입증하고, 다양한 인기 있는 LLM의 논리적 추론 성능을 비교한다.


---

*Generated on 2025-09-23 09:06:49*