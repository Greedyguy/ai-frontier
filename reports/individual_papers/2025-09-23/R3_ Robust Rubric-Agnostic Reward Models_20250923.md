---
keywords:
  - Reward Models
  - Large Language Model
  - Rubric-Agnostic Evaluation
  - Interpretable Score Assignments
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.13388
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:58:53.065850",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reward Models",
    "Large Language Model",
    "Rubric-Agnostic Evaluation",
    "Interpretable Score Assignments"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reward Models": 0.75,
    "Large Language Model": 0.8,
    "Rubric-Agnostic Evaluation": 0.7,
    "Interpretable Score Assignments": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "reward models",
        "canonical": "Reward Models",
        "aliases": [
          "reward modeling"
        ],
        "category": "unique_technical",
        "rationale": "Reward models are central to the paper's framework and are crucial for linking to discussions on model alignment and evaluation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "language model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Language models are a fundamental component of the study, linking to broader discussions in NLP and AI.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "rubric-agnostic",
        "canonical": "Rubric-Agnostic Evaluation",
        "aliases": [
          "rubric-free evaluation"
        ],
        "category": "unique_technical",
        "rationale": "The concept of rubric-agnostic evaluation is novel and central to the paper's contribution, enhancing model interpretability and generalizability.",
        "novelty_score": 0.8,
        "connectivity_score": 0.5,
        "specificity_score": 0.9,
        "link_intent_score": 0.7
      },
      {
        "surface": "interpretable score assignments",
        "canonical": "Interpretable Score Assignments",
        "aliases": [
          "interpretable scoring"
        ],
        "category": "unique_technical",
        "rationale": "Interpretable score assignments are key to understanding model outputs, linking to transparency and accountability in AI.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "model",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "reward models",
      "resolved_canonical": "Reward Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "language model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "rubric-agnostic",
      "resolved_canonical": "Rubric-Agnostic Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.5,
        "specificity": 0.9,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "interpretable score assignments",
      "resolved_canonical": "Interpretable Score Assignments",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# R3: Robust Rubric-Agnostic Reward Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.13388.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.13388](https://arxiv.org/abs/2505.13388)

## 🔗 유사한 논문
- [[2025-09-22/reWordBench_ Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs_20250922|reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs]] (88.3% similar)
- [[2025-09-23/Post-hoc Reward Calibration_ A Case Study on Length Bias_20250923|Post-hoc Reward Calibration: A Case Study on Length Bias]] (87.1% similar)
- [[2025-09-22/BaseReward_ A Strong Baseline for Multimodal Reward Model_20250922|BaseReward: A Strong Baseline for Multimodal Reward Model]] (87.0% similar)
- [[2025-09-22/MT-RewardTree_ A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling_20250922|MT-RewardTree: A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling]] (86.3% similar)
- [[2025-09-22/Reward Hacking Mitigation using Verifiable Composite Rewards_20250922|Reward Hacking Mitigation using Verifiable Composite Rewards]] (85.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Reward Models|Reward Models]], [[keywords/Rubric-Agnostic Evaluation|Rubric-Agnostic Evaluation]], [[keywords/Interpretable Score Assignments|Interpretable Score Assignments]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.13388v3 Announce Type: replace-cross 
Abstract: Reward models are essential for aligning language model outputs with human preferences, yet existing approaches often lack both controllability and interpretability. These models are typically optimized for narrow objectives, limiting their generalizability to broader downstream tasks. Moreover, their scalar outputs are difficult to interpret without contextual reasoning. To address these limitations, we introduce $\shortmethodname$, a novel reward modeling framework that is rubric-agnostic, generalizable across evaluation dimensions, and provides interpretable, reasoned score assignments. $\shortmethodname$ enables more transparent and flexible evaluation of language models, supporting robust alignment with diverse human values and use cases. Our models, data, and code are available as open source at https://github.com/rubricreward/r3.

## 📝 요약

이 논문은 언어 모델의 출력을 인간의 선호에 맞추기 위한 보상 모델의 문제점을 해결하고자 합니다. 기존 모델은 제어 가능성과 해석 가능성이 부족하며, 좁은 목표에 최적화되어 있어 일반화가 어렵습니다. 이를 해결하기 위해, 저자들은 해석 가능하고 다양한 평가 차원에 일반화 가능한 새로운 보상 모델링 프레임워크인 $\shortmethodname$을 제안합니다. 이 프레임워크는 언어 모델의 평가를 보다 투명하고 유연하게 하여 다양한 인간 가치와 사용 사례에 강력하게 맞출 수 있도록 지원합니다. 연구의 모델, 데이터, 코드는 오픈 소스로 제공됩니다.

## 🎯 주요 포인트

- 1. 기존 보상 모델은 제어 가능성과 해석 가능성이 부족하여 언어 모델 출력을 인간의 선호에 맞추는 데 한계가 있다.
- 2. 기존 모델은 좁은 목표에 최적화되어 있어 더 넓은 다운스트림 작업에 일반화하기 어렵다.
- 3. $\shortmethodname$는 해석 가능한 이유 기반 점수 할당을 제공하여 평가 차원 전반에 걸쳐 일반화 가능한 새로운 보상 모델링 프레임워크이다.
- 4. $\shortmethodname$는 다양한 인간 가치와 사용 사례에 강력하게 맞출 수 있도록 언어 모델의 평가를 더 투명하고 유연하게 만든다.
- 5. 연구의 모델, 데이터, 코드는 오픈 소스로 제공된다.


---

*Generated on 2025-09-24 00:58:53*