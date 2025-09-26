---
keywords:
  - Large Language Model
  - Irrelevant Context
  - Symbolic Reasoning Graphs
  - Stepwise Tree Search
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.18761
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:01:08.179623",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Irrelevant Context",
    "Symbolic Reasoning Graphs",
    "Stepwise Tree Search"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Irrelevant Context": 0.7,
    "Symbolic Reasoning Graphs": 0.65,
    "Stepwise Tree Search": 0.6
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
        "rationale": "Central to the paper's focus, linking to a broad technical category that connects with various NLP concepts.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "irrelevant context",
        "canonical": "Irrelevant Context",
        "aliases": [
          "IC",
          "distracting context"
        ],
        "category": "unique_technical",
        "rationale": "A unique technical term introduced in the paper, critical for understanding the specific challenge addressed.",
        "novelty_score": 0.7,
        "connectivity_score": 0.5,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "symbolic reasoning graphs",
        "canonical": "Symbolic Reasoning Graphs",
        "aliases": [
          "reasoning graphs"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specific method used in the paper, enhancing understanding of the experimental setup.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.65
      },
      {
        "surface": "stepwise tree search",
        "canonical": "Stepwise Tree Search",
        "aliases": [
          "tree search"
        ],
        "category": "unique_technical",
        "rationale": "Describes a novel approach proposed in the paper, crucial for linking to related search algorithms.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.7,
        "link_intent_score": 0.6
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "evaluation",
      "training models"
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
      "candidate_surface": "irrelevant context",
      "resolved_canonical": "Irrelevant Context",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.5,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "symbolic reasoning graphs",
      "resolved_canonical": "Symbolic Reasoning Graphs",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "stepwise tree search",
      "resolved_canonical": "Stepwise Tree Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.7,
        "link_intent": 0.6
      }
    }
  ]
}
-->

# How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.18761.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.18761](https://arxiv.org/abs/2505.18761)

## 🔗 유사한 논문
- [[2025-09-23/No Need for Explanations_ LLMs can implicitly learn from mistakes in-context_20250923|No Need for Explanations: LLMs can implicitly learn from mistakes in-context]] (86.8% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (86.5% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text?_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text?]] (86.3% similar)
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (86.0% similar)
- [[2025-09-23/EngiBench_ A Benchmark for Evaluating Large Language Models on Engineering Problem Solving_20250923|EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving]] (86.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Irrelevant Context|Irrelevant Context]], [[keywords/Symbolic Reasoning Graphs|Symbolic Reasoning Graphs]], [[keywords/Stepwise Tree Search|Stepwise Tree Search]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.18761v2 Announce Type: replace-cross 
Abstract: We introduce Grade School Math with Distracting Context (GSM-DC), a synthetic benchmark to evaluate Large Language Models' (LLMs) reasoning robustness against systematically controlled irrelevant context (IC). GSM-DC constructs symbolic reasoning graphs with precise distractor injections, enabling rigorous, reproducible evaluation. Our experiments demonstrate that LLMs are significantly sensitive to IC, affecting both reasoning path selection and arithmetic accuracy. Additionally, training models with strong distractors improves performance in both in-distribution and out-of-distribution scenarios. We further propose a stepwise tree search guided by a process reward model, which notably enhances robustness in out-of-distribution conditions.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 추론 강건성을 평가하기 위한 새로운 벤치마크인 GSM-DC를 소개합니다. GSM-DC는 체계적으로 제어된 무관한 맥락을 포함하여 상징적 추론 그래프를 구성함으로써 엄밀하고 재현 가능한 평가를 가능하게 합니다. 실험 결과, LLM이 무관한 맥락에 민감하여 추론 경로 선택과 산술 정확도에 영향을 미친다는 것을 보여줍니다. 강력한 방해 요소로 모델을 훈련하면 성능이 향상되며, 특히 분포 내 및 분포 외 시나리오에서 효과적입니다. 또한, 프로세스 보상 모델에 의해 안내되는 단계별 트리 검색을 제안하여 분포 외 조건에서의 강건성을 크게 향상시킵니다.

## 🎯 주요 포인트

- 1. GSM-DC는 대형 언어 모델의 추론 강건성을 평가하기 위한 합성 벤치마크로, 체계적으로 제어된 무관한 맥락을 포함합니다.
- 2. GSM-DC는 정확한 방해 요소 주입을 통해 상징적 추론 그래프를 구성하여 엄격하고 재현 가능한 평가를 가능하게 합니다.
- 3. 실험 결과, 대형 언어 모델은 무관한 맥락에 상당히 민감하며, 이는 추론 경로 선택과 산술 정확도에 영향을 미칩니다.
- 4. 강력한 방해 요소로 모델을 훈련시키면, 분포 내 및 분포 외 시나리오 모두에서 성능이 향상됩니다.
- 5. 프로세스 보상 모델에 의해 안내되는 단계별 트리 검색을 제안하여, 분포 외 조건에서의 강건성을 크게 향상시킵니다.


---

*Generated on 2025-09-24 01:01:08*