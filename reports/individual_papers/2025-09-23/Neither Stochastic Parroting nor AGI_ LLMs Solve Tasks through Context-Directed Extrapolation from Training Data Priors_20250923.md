---
keywords:
  - Large Language Model
  - Context-Directed Extrapolation
  - In-Context Learning
  - Instruction Tuning
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2505.23323
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:01:40.980221",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Context-Directed Extrapolation",
    "In-Context Learning",
    "Instruction Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Context-Directed Extrapolation": 0.7,
    "In-Context Learning": 0.68,
    "Instruction Tuning": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's discussion, linking to a broad range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "context-directed extrapolation",
        "canonical": "Context-Directed Extrapolation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept specific to the paper's argument, offering new linkage opportunities.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "in-context learning",
        "canonical": "In-Context Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A specific mechanism discussed in the paper, relevant to recent advancements in LLMs.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.68
      },
      {
        "surface": "instruction tuning",
        "canonical": "Instruction Tuning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Highlights a method for enhancing LLM capabilities, connecting to ongoing research in model fine-tuning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "stochastic parroting",
      "emergent advanced reasoning"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
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
      "candidate_surface": "context-directed extrapolation",
      "resolved_canonical": "Context-Directed Extrapolation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "in-context learning",
      "resolved_canonical": "In-Context Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.68
      }
    },
    {
      "candidate_surface": "instruction tuning",
      "resolved_canonical": "Instruction Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Neither Stochastic Parroting nor AGI: LLMs Solve Tasks through Context-Directed Extrapolation from Training Data Priors

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.23323.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2505.23323](https://arxiv.org/abs/2505.23323)

## 🔗 유사한 논문
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (88.2% similar)
- [[2025-09-23/Question Answering with LLMs and Learning from Answer Sets_20250923|Question Answering with LLMs and Learning from Answer Sets]] (87.6% similar)
- [[2025-09-23/No Need for Explanations_ LLMs can implicitly learn from mistakes in-context_20250923|No Need for Explanations: LLMs can implicitly learn from mistakes in-context]] (87.3% similar)
- [[2025-09-22/Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics_20250922|Can LLMs Judge Debates? Evaluating Non-Linear Reasoning via Argumentation Theory Semantics]] (87.2% similar)
- [[2025-09-23/Reinforcement Learning Meets Large Language Models_ A Survey of Advancements and Applications Across the LLM Lifecycle_20250923|Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle]] (87.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/In-Context Learning|In-Context Learning]], [[keywords/Instruction Tuning|Instruction Tuning]]
**⚡ Unique Technical**: [[keywords/Context-Directed Extrapolation|Context-Directed Extrapolation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.23323v2 Announce Type: replace 
Abstract: In this position paper we raise critical awareness of a realistic view of LLM capabilities that eschews extreme alternative views that LLMs are either 'stochastic parrots' or in possession of 'emergent' advanced reasoning capabilities, which, due to their unpredictable emergence, constitute an existential threat. Our middle-ground view is that LLMs extrapolate from priors from their training data while using context to guide the model to the appropriate priors; we call this "context-directed extrapolation." Specifically, this context direction is achieved through examples in base models, leading to in-context learning, while instruction tuning allows LLMs to perform similarly based on prompts rather than explicit examples. Under this view, substantiated though existing literature, while reasoning capabilities go well beyond stochastic parroting, such capabilities are predictable, controllable, not indicative of advanced reasoning akin to high-level cognitive capabilities in humans, and not infinitely scalable with additional training. As a result, fears of uncontrollable emergence of agency are allayed, while research advances are appropriately refocused on the processes of context-directed extrapolation and how this interacts with training data to produce valuable capabilities in LLMs. Future work can therefore explore alternative augmenting techniques that do not rely on inherent advanced reasoning in LLMs.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 능력에 대한 현실적인 관점을 제시하며, LLM이 단순히 '확률적 앵무새'이거나 예측 불가능한 고급 추론 능력을 가진다는 극단적인 견해를 지양합니다. 저자들은 LLM이 훈련 데이터의 사전 정보를 바탕으로 문맥을 활용해 적절한 사전 정보를 추론하는 "문맥 지향적 외삽"을 수행한다고 주장합니다. 이 과정은 기본 모델의 예제를 통해 이루어지며, 지시 조정을 통해 명시적 예제 없이도 유사한 성능을 발휘할 수 있습니다. 이러한 관점에서 LLM의 추론 능력은 예측 가능하고 통제 가능하며, 인간의 고급 인지 능력과는 다르다고 설명합니다. 따라서 LLM의 통제 불가능한 자율성에 대한 우려를 완화하고, 문맥 지향적 외삽 과정과 훈련 데이터의 상호작용에 대한 연구에 집중할 것을 제안합니다. 향후 연구는 LLM의 고급 추론에 의존하지 않는 대체 보강 기법을 탐구할 수 있습니다.

## 🎯 주요 포인트

- 1. LLM의 능력은 극단적인 관점이 아닌, 훈련 데이터의 사전 지식을 문맥을 통해 적절히 활용하는 "문맥 지향적 외삽"으로 설명됩니다.
- 2. 문맥 지향적 외삽은 기본 모델의 예시를 통해 이루어지며, 명시적인 예시 없이도 프롬프트를 통해 유사한 성능을 발휘할 수 있도록 합니다.
- 3. LLM의 추론 능력은 예측 가능하고 제어 가능하며, 인간의 고차원 인지 능력과 유사한 고급 추론을 나타내지 않습니다.
- 4. LLM의 능력은 추가 훈련을 통해 무한히 확장되지 않으며, 자율성의 통제 불가능한 출현에 대한 우려를 해소합니다.
- 5. 미래 연구는 LLM의 고유한 고급 추론에 의존하지 않는 대체 보강 기술을 탐구할 수 있습니다.


---

*Generated on 2025-09-24 04:01:40*