---
keywords:
  - Reinforcement Learning from Human Feedback
  - Large Language Model
  - Reward Model
  - Post-hoc Reward Calibration
  - Locally Weighted Regression
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2409.17407
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:22:41.010101",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning from Human Feedback",
    "Large Language Model",
    "Reward Model",
    "Post-hoc Reward Calibration",
    "Locally Weighted Regression"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning from Human Feedback": 0.78,
    "Large Language Model": 0.85,
    "Reward Model": 0.77,
    "Post-hoc Reward Calibration": 0.82,
    "Locally Weighted Regression": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning from Human Feedback",
        "canonical": "Reinforcement Learning from Human Feedback",
        "aliases": [
          "RLHF"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's focus on aligning LLMs with human values, offering a unique perspective on bias correction.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are fundamental to the paper's discussion on bias and reward calibration, providing a broad technical context.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Reward Model",
        "canonical": "Reward Model",
        "aliases": [
          "RM"
        ],
        "category": "unique_technical",
        "rationale": "The reward model is a key component in translating human feedback, crucial for understanding the paper's methodology.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Post-hoc Reward Calibration",
        "canonical": "Post-hoc Reward Calibration",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This new concept introduced in the paper is essential for addressing biases in reward models.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Locally Weighted Regression",
        "canonical": "Locally Weighted Regression",
        "aliases": [
          "LWR"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is used to extend the bias correction approach, linking to broader statistical methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "bias",
      "calibration",
      "alignment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reinforcement Learning from Human Feedback",
      "resolved_canonical": "Reinforcement Learning from Human Feedback",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Reward Model",
      "resolved_canonical": "Reward Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Post-hoc Reward Calibration",
      "resolved_canonical": "Post-hoc Reward Calibration",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Locally Weighted Regression",
      "resolved_canonical": "Locally Weighted Regression",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Post-hoc Reward Calibration: A Case Study on Length Bias

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2409.17407.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2409.17407](https://arxiv.org/abs/2409.17407)

## 🔗 유사한 논문
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL: Replacing Human Feedback for Reward Shaping]] (90.1% similar)
- [[2025-09-22/BaseReward_ A Strong Baseline for Multimodal Reward Model_20250922|BaseReward: A Strong Baseline for Multimodal Reward Model]] (86.5% similar)
- [[2025-09-22/reWordBench_ Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs_20250922|reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs]] (85.7% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (85.3% similar)
- [[2025-09-22/Reward Hacking Mitigation using Verifiable Composite Rewards_20250922|Reward Hacking Mitigation using Verifiable Composite Rewards]] (85.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Locally Weighted Regression|Locally Weighted Regression]]
**⚡ Unique Technical**: [[keywords/Reinforcement Learning from Human Feedback|Reinforcement Learning from Human Feedback]], [[keywords/Reward Model|Reward Model]], [[keywords/Post-hoc Reward Calibration|Post-hoc Reward Calibration]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.17407v2 Announce Type: replace 
Abstract: Reinforcement Learning from Human Feedback aligns the outputs of Large Language Models with human values and preferences. Central to this process is the reward model (RM), which translates human feedback into training signals for optimising LLM behaviour. However, RMs can develop biases by exploiting spurious correlations in their training data, such as favouring outputs based on length or style rather than true quality. These biases can lead to incorrect output rankings, sub-optimal model evaluations, and the amplification of undesirable behaviours in LLMs alignment. This paper addresses the challenge of correcting such biases without additional data and training, introducing the concept of Post-hoc Reward Calibration. We first propose an intuitive approach to estimate the bias term and, thus, remove it to approximate the underlying true reward. We then extend the approach to a more general and robust form with the Locally Weighted Regression. Focusing on the prevalent length bias, we validate our proposed approaches across three experimental settings, demonstrating consistent improvements: (1) a 3.11 average performance gain across 33 reward models on the RewardBench dataset; (2) enhanced alignment of RM rankings with GPT-4 evaluations and human preferences based on the AlpacaEval benchmark; and (3) improved Length-Controlled win rate of the RLHF process in multiple LLM--RM combinations. Our method is computationally efficient and generalisable to other types of bias and RMs, offering a scalable and robust solution for mitigating biases in LLM alignment. Our code and results are available at https://github.com/ZeroYuHuang/Reward-Calibration.

## 📝 요약

이 논문은 인간 피드백을 통한 강화 학습(RLHF)에서 발생하는 보상 모델(RM)의 편향 문제를 해결하기 위해 '사후 보상 보정' 개념을 제안합니다. RM은 훈련 데이터의 잘못된 상관관계를 이용해 편향을 가질 수 있으며, 이는 모델 평가와 LLM의 행동에 부정적인 영향을 미칩니다. 저자들은 추가 데이터나 훈련 없이 이러한 편향을 교정할 수 있는 방법을 제시하며, 특히 길이 편향 문제에 주목합니다. 제안된 방법은 보상 벤치마크 데이터셋에서 평균 3.11의 성능 향상을 보였고, GPT-4 평가 및 인간 선호도와의 정렬을 개선했습니다. 이 방법은 계산 효율성이 높고 다른 편향에도 적용 가능하여 LLM 정렬에서의 편향 완화에 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. 인간 피드백을 통한 강화 학습은 대형 언어 모델의 출력을 인간의 가치와 선호에 맞추는 과정이다.
- 2. 보상 모델(RM)은 훈련 데이터의 잘못된 상관관계를 이용하여 편향을 개발할 수 있으며, 이는 잘못된 출력 순위와 모델 평가를 초래할 수 있다.
- 3. 이 논문은 추가 데이터나 훈련 없이 이러한 편향을 수정하는 '사후 보상 보정' 개념을 도입하여 해결책을 제시한다.
- 4. 제안된 방법은 보상 모델의 순위와 인간의 선호도 간의 일치를 개선하며, 다양한 실험 환경에서 일관된 성능 향상을 보여준다.
- 5. 이 방법은 계산 효율성이 높고 다른 유형의 편향과 보상 모델에도 일반화 가능하여, 대형 언어 모델의 편향 완화에 대한 확장 가능한 솔루션을 제공한다.


---

*Generated on 2025-09-24 00:22:41*