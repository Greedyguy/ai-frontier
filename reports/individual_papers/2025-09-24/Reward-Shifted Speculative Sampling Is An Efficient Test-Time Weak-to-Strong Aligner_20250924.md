<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:54:28.696835",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Reward-Shifted Speculative Sampling",
    "Test-Time Alignment",
    "Reinforcement Learning with Human Feedback"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Reward-Shifted Speculative Sampling": 0.9,
    "Test-Time Alignment": 0.85,
    "Reinforcement Learning with Human Feedback": 0.8
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
        "rationale": "Essential for understanding the context of alignment and efficiency improvements discussed in the paper.",
        "novelty_score": 0.2,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Reward-Shifted Speculative Sampling",
        "canonical": "Reward-Shifted Speculative Sampling",
        "aliases": [
          "SSS"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's contribution, offering a novel approach to test-time alignment.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.9
      },
      {
        "surface": "Test-Time Alignment",
        "canonical": "Test-Time Alignment",
        "aliases": [
          "Inference-Time Alignment"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for understanding the efficiency and safety improvements in LLMs.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "RLHF Optimal Solution",
        "canonical": "Reinforcement Learning with Human Feedback",
        "aliases": [
          "RLHF"
        ],
        "category": "specific_connectable",
        "rationale": "Relevant for linking to broader discussions on aligning AI with human values.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "inference cost",
      "gold reward scores",
      "efficiency bottleneck"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Reward-Shifted Speculative Sampling",
      "resolved_canonical": "Reward-Shifted Speculative Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Test-Time Alignment",
      "resolved_canonical": "Test-Time Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "RLHF Optimal Solution",
      "resolved_canonical": "Reinforcement Learning with Human Feedback",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Reward-Shifted Speculative Sampling Is An Efficient Test-Time Weak-to-Strong Aligner

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2508.15044.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2508.15044](https://arxiv.org/abs/2508.15044)

## 🔗 유사한 논문
- [[2025-09-23/LifeAlign_ Lifelong Alignment for Large Language Models with Memory-Augmented Focalized Preference Optimization_20250923|LifeAlign: Lifelong Alignment for Large Language Models with Memory-Augmented Focalized Preference Optimization]] (85.4% similar)
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL: Replacing Human Feedback for Reward Shaping]] (85.1% similar)
- [[2025-09-23/Post-hoc Reward Calibration_ A Case Study on Length Bias_20250923|Post-hoc Reward Calibration: A Case Study on Length Bias]] (84.6% similar)
- [[2025-09-23/ConfClip_ Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs_20250923|ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs]] (83.3% similar)
- [[2025-09-24/DRO-REBEL_ Distributionally Robust Relative-Reward Regression for Fast and Efficient LLM Alignment_20250924|DRO-REBEL: Distributionally Robust Relative-Reward Regression for Fast and Efficient LLM Alignment]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Test-Time Alignment|Test-Time Alignment]], [[keywords/Reinforcement Learning with Human Feedback|Reinforcement Learning with Human Feedback]]
**⚡ Unique Technical**: [[keywords/Reward-Shifted Speculative Sampling|Reward-Shifted Speculative Sampling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.15044v3 Announce Type: replace 
Abstract: Aligning large language models (LLMs) with human preferences has become a critical step in their development. Recent research has increasingly focused on test-time alignment, where additional compute is allocated during inference to enhance LLM safety and reasoning capabilities. However, these test-time alignment techniques often incur substantial inference costs, limiting their practical application. We are inspired by the speculative sampling acceleration, which leverages a small draft model to efficiently predict future tokens, to address the efficiency bottleneck of test-time alignment. We introduce the reward-shifted speculative sampling (SSS) algorithm, in which the draft model is aligned with human preferences, while the target model remains unchanged. We theoretically demonstrate that the distributional shift between the aligned draft model and the unaligned target model can be exploited to recover the RLHF optimal solution without actually obtaining it, by modifying the acceptance criterion and bonus token distribution. Our algorithm achieves superior gold reward scores at a significantly reduced inference cost in test-time weak-to-strong alignment experiments, thereby validating both its effectiveness and efficiency.

## 📝 요약

대형 언어 모델(LLM)의 인간 선호도에 맞춘 정렬은 개발의 중요한 단계입니다. 최근 연구는 추론 시 추가 계산을 통해 LLM의 안전성과 추론 능력을 향상시키는 테스트 시 정렬에 집중하고 있습니다. 그러나 이러한 방법은 높은 추론 비용을 초래하여 실용성을 제한합니다. 우리는 효율성을 높이기 위해 작은 초안 모델을 사용하여 미래 토큰을 예측하는 투기적 샘플링 가속화에서 영감을 받았습니다. 이에 따라 인간 선호도에 맞춘 초안 모델과 변경되지 않은 목표 모델 간의 분포 변화를 활용하는 보상 이동 투기 샘플링(SSS) 알고리즘을 제안합니다. 이 알고리즘은 수용 기준과 보너스 토큰 분포를 수정하여 RLHF 최적 솔루션을 실제로 얻지 않고도 회복할 수 있음을 이론적으로 입증합니다. 우리의 알고리즘은 테스트 시 약한-강한 정렬 실험에서 낮은 추론 비용으로 우수한 보상 점수를 달성하여 그 효과와 효율성을 입증합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)을 인간의 선호에 맞추는 것이 개발의 중요한 단계로 부각되고 있습니다.
- 2. 테스트 시점에서의 정렬은 LLM의 안전성과 추론 능력을 향상시키기 위해 추가적인 계산을 할당하는 방법입니다.
- 3. 테스트 시점 정렬 기술은 높은 추론 비용을 초래하여 실용성을 제한합니다.
- 4. 보상 이동 추측 샘플링(SSS) 알고리즘은 초안 모델을 인간의 선호에 맞추어 효율성을 개선합니다.
- 5. 제안된 알고리즘은 테스트 시점 약-강 정렬 실험에서 낮은 추론 비용으로 우수한 보상 점수를 달성합니다.


---

*Generated on 2025-09-24 15:54:28*