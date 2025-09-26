---
keywords:
  - Large Language Model
  - seqBench
  - Sequential Reasoning
  - Logical Depth
  - Commonsense Reasoning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16866
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:53:37.618580",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "seqBench",
    "Sequential Reasoning",
    "Logical Depth",
    "Commonsense Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "seqBench": 0.8,
    "Sequential Reasoning": 0.78,
    "Logical Depth": 0.72,
    "Commonsense Reasoning": 0.77
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
        "rationale": "Central to the paper's focus, linking to existing discussions on LLM capabilities.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "seqBench",
        "canonical": "seqBench",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a new benchmark specific to the paper, useful for linking related research.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "sequential reasoning",
        "canonical": "Sequential Reasoning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Key concept for understanding LLM limitations in the paper.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "logical depth",
        "canonical": "Logical Depth",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Specific metric introduced in the paper for evaluating reasoning complexity.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "commonsense reasoning",
        "canonical": "Commonsense Reasoning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Highlights a critical area of LLM evaluation discussed in the paper.",
        "novelty_score": 0.45,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "accuracy",
      "evaluation metrics"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "seqBench",
      "resolved_canonical": "seqBench",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "sequential reasoning",
      "resolved_canonical": "Sequential Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "logical depth",
      "resolved_canonical": "Logical Depth",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "commonsense reasoning",
      "resolved_canonical": "Commonsense Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16866.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16866](https://arxiv.org/abs/2509.16866)

## 🔗 유사한 논문
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (88.0% similar)
- [[2025-09-23/On LLM-Based Scientific Inductive Reasoning Beyond Equations_20250923|On LLM-Based Scientific Inductive Reasoning Beyond Equations]] (86.9% similar)
- [[2025-09-19/Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (85.4% similar)
- [[2025-09-22/How Good are Foundation Models in Step-by-Step Embodied Reasoning?_20250922|How Good are Foundation Models in Step-by-Step Embodied Reasoning?]] (84.7% similar)
- [[2025-09-23/Roundtable Policy_ Improving Scientific Reasoning and Narratives through Confidence-Weighted Consensus of LLMs_20250923|Roundtable Policy: Improving Scientific Reasoning and Narratives through Confidence-Weighted Consensus of LLMs]] (84.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Sequential Reasoning|Sequential Reasoning]], [[keywords/Commonsense Reasoning|Commonsense Reasoning]]
**⚡ Unique Technical**: [[keywords/seqBench|seqBench]], [[keywords/Logical Depth|Logical Depth]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16866v1 Announce Type: new 
Abstract: We introduce seqBench, a parametrized benchmark for probing sequential reasoning limits in Large Language Models (LLMs) through precise, multi-dimensional control over several key complexity dimensions. seqBench allows systematic variation of (1) the logical depth, defined as the number of sequential actions required to solve the task; (2) the number of backtracking steps along the optimal path, quantifying how often the agent must revisit prior states to satisfy deferred preconditions (e.g., retrieving a key after encountering a locked door); and (3) the noise ratio, defined as the ratio between supporting and distracting facts about the environment. Our evaluations on state-of-the-art LLMs reveal a universal failure pattern: accuracy collapses exponentially beyond a model-specific logical depth. Unlike existing benchmarks, seqBench's fine-grained control facilitates targeted analyses of these reasoning failures, illuminating universal scaling laws and statistical limits, as detailed in this paper alongside its generation methodology and evaluation metrics. We find that even top-performing models systematically fail on seqBench's structured reasoning tasks despite minimal search complexity, underscoring key limitations in their commonsense reasoning capabilities. Designed for future evolution to keep pace with advancing models, the seqBench datasets are publicly released to spur deeper scientific inquiry into LLM reasoning, aiming to establish a clearer understanding of their true potential and current boundaries for robust real-world application.

## 📝 요약

seqBench는 대형 언어 모델(LLM)의 순차적 추론 한계를 탐구하기 위한 매개변수화된 벤치마크로, 논리적 깊이, 최적 경로에서의 백트래킹 단계 수, 환경에 대한 지원 및 방해 사실 비율 등의 복잡성 차원을 정밀하게 제어합니다. 최신 LLM 평가 결과, 모델별 논리적 깊이를 초과하면 정확도가 급격히 감소하는 보편적 실패 패턴이 드러났습니다. seqBench는 기존 벤치마크와 달리 세분화된 제어를 통해 이러한 추론 실패를 분석하고, 모델의 상식 추론 한계를 강조합니다. seqBench 데이터셋은 LLM의 추론 능력에 대한 심층적 과학적 탐구를 촉진하기 위해 공개되었습니다.

## 🎯 주요 포인트

- 1. seqBench는 대규모 언어 모델(LLM)의 순차적 추론 한계를 탐구하기 위한 매개변수화된 벤치마크로, 여러 복잡성 차원을 정밀하게 제어합니다.
- 2. seqBench는 논리적 깊이, 최적 경로에서의 백트래킹 단계 수, 환경에 대한 지원 및 방해 사실의 비율을 체계적으로 변화시킵니다.
- 3. 최첨단 LLM에 대한 평가 결과, 모델별 논리적 깊이를 초과하면 정확도가 기하급수적으로 감소하는 보편적인 실패 패턴이 드러났습니다.
- 4. seqBench는 기존 벤치마크와 달리 세밀한 제어를 통해 이러한 추론 실패에 대한 목표 분석을 가능하게 하며, 보편적인 스케일링 법칙과 통계적 한계를 밝혀냅니다.
- 5. seqBench 데이터셋은 LLM의 추론 능력에 대한 더 깊은 과학적 탐구를 촉진하기 위해 공개되었으며, 실세계 응용을 위한 명확한 이해를 목표로 합니다.


---

*Generated on 2025-09-23 22:53:37*