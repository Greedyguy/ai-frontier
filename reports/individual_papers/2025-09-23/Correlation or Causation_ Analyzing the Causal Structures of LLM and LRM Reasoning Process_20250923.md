---
keywords:
  - Large Language Model
  - Reinforcement Learning
  - Structural Causal Model
  - Causal Reasoning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17380
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:59:20.487646",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Reinforcement Learning",
    "Structural Causal Model",
    "Causal Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Reinforcement Learning": 0.8,
    "Structural Causal Model": 0.78,
    "Causal Reasoning": 0.84
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "This term is central to the paper's focus on reasoning processes and is a key concept in AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "specific_connectable",
        "rationale": "Reinforcement Learning is a significant method discussed in the paper for enhancing causal reasoning in models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Structural Causal Models",
        "canonical": "Structural Causal Model",
        "aliases": [
          "SCM"
        ],
        "category": "unique_technical",
        "rationale": "SCMs are a unique technical concept used in the paper to analyze causal structures, offering new insights.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Causal Reasoning",
        "canonical": "Causal Reasoning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Causal reasoning is a core theme of the paper, crucial for understanding model improvements discussed.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.84
      }
    ],
    "ban_list_suggestions": [
      "unfaithfulness",
      "bias",
      "inconsistency"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Structural Causal Models",
      "resolved_canonical": "Structural Causal Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Causal Reasoning",
      "resolved_canonical": "Causal Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.84
      }
    }
  ]
}
-->

# Correlation or Causation: Analyzing the Causal Structures of LLM and LRM Reasoning Process

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17380.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17380](https://arxiv.org/abs/2509.17380)

## 🔗 유사한 논문
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text?_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text?]] (87.4% similar)
- [[2025-09-19/Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG: The Integration of Causal-Counterfactual Reasoning into RAG]] (85.6% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (85.2% similar)
- [[2025-09-22/Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics_20250922|Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics]] (85.1% similar)
- [[2025-09-19/Understanding the Thinking Process of Reasoning Models_ A Perspective from Schoenfeld's Episode Theory_20250919|Understanding the Thinking Process of Reasoning Models: A Perspective from Schoenfeld's Episode Theory]] (85.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]], [[keywords/Causal Reasoning|Causal Reasoning]]
**⚡ Unique Technical**: [[keywords/Structural Causal Model|Structural Causal Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17380v1 Announce Type: new 
Abstract: LLMs suffer from critical reasoning issues such as unfaithfulness, bias, and inconsistency, since they lack robust causal underpinnings and may rely on superficial correlations rather than genuine understanding. Successive LRMs have emerged as a promising alternative, leveraging advanced training techniques such as reinforcement learning (RL) and distillation to improve task accuracy. However, the impact of these training methods on causality remains largely unexplored. In this study, we conduct a systematic causal analysis on LLMs and LRMs, examining structural causal models (SCMs) of four key variables: problem instruction (Z), thinking process (T), reasoning steps (X), and answer (Y). Our findings reveal that RLVR-trained LRMs exhibit enhanced causal reasoning capabilities, aligning more closely with ideal causal structures, while LLMs and distilled LRMs fail to address causality-related deficiencies. Our further investigation indicates that RLVR reduces spurious correlations and strengthens genuine causal patterns, thereby mitigating unfaithfulness and bias. In addition, our inspection on the dynamics of the RLVR training process observes a high correlation between reduced spurious features and improved causal structures, where the causal relationships consistently improve in the training process. This study contributes to the understanding of causality in reasoning models, highlights the critical role of RLVR in enhancing causal reasoning, and provides insights for designing future AI systems with stronger causal foundations. We release our code and data at https://github.com/Harryking1999/CoT_Causal_Analysis.

## 📝 요약

이 논문은 대형 언어 모델(LLM)과 연속적 학습 모델(LRM)의 인과적 추론 능력을 분석합니다. LLM은 피상적 상관관계에 의존하여 불충실성, 편향, 비일관성 문제를 겪습니다. 이에 비해 강화 학습 및 증류 기법을 사용한 RLVR 훈련 LRM은 인과적 구조와 더 잘 일치하며, 불필요한 상관관계를 줄이고 진정한 인과 패턴을 강화하여 이러한 문제를 완화합니다. 연구는 RLVR의 인과적 추론 향상에 중요한 역할을 강조하며, 향후 AI 시스템 설계에 대한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. LLMs는 피상적인 상관관계에 의존하여 신뢰성, 편향, 일관성 문제를 겪고 있다.
- 2. 강화 학습(RL)과 증류 기법을 활용한 LRMs는 과제 정확도를 향상시키며 유망한 대안으로 부상하고 있다.
- 3. 연구 결과, RLVR로 훈련된 LRMs는 이상적인 인과 구조에 더 가깝게 정렬되어 인과 추론 능력이 향상되었다.
- 4. RLVR는 거짓 상관관계를 줄이고 진정한 인과 패턴을 강화하여 신뢰성 부족과 편향을 완화한다.
- 5. 연구는 인과 관계 이해에 기여하며, RLVR의 인과 추론 강화에서의 중요성을 강조하고 있다.


---

*Generated on 2025-09-23 22:59:20*