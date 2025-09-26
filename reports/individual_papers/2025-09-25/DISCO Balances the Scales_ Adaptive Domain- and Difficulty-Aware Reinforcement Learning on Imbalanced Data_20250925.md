---
keywords:
  - Large Language Model
  - Reinforcement Learning from Human Feedback
  - Group Relative Policy Optimization
  - Domain-Informed Self-Consistency Policy Optimization
  - Domain-aware reward scaling
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2505.15074
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:25:19.161174",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Reinforcement Learning from Human Feedback",
    "Group Relative Policy Optimization",
    "Domain-Informed Self-Consistency Policy Optimization",
    "Domain-aware reward scaling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Reinforcement Learning from Human Feedback": 0.78,
    "Group Relative Policy Optimization": 0.8,
    "Domain-Informed Self-Consistency Policy Optimization": 0.82,
    "Domain-aware reward scaling": 0.77
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
        "rationale": "This term is central to the paper's focus and aligns with existing vocabulary, facilitating connections to related works in language models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.68,
        "link_intent_score": 0.85
      },
      {
        "surface": "Reinforcement Learning from Human Feedback",
        "canonical": "Reinforcement Learning from Human Feedback",
        "aliases": [
          "RLHF"
        ],
        "category": "unique_technical",
        "rationale": "This concept is a unique approach discussed in the paper, offering a specific method for aligning models with human preferences.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Group Relative Policy Optimization",
        "canonical": "Group Relative Policy Optimization",
        "aliases": [
          "GRPO"
        ],
        "category": "unique_technical",
        "rationale": "GRPO is a specific method critiqued and expanded upon in the paper, making it a key term for understanding the proposed improvements.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Domain-Informed Self-Consistency Policy Optimization",
        "canonical": "Domain-Informed Self-Consistency Policy Optimization",
        "aliases": [
          "DISCO"
        ],
        "category": "unique_technical",
        "rationale": "DISCO is the novel method introduced in the paper, central to its contributions and findings.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Domain-aware reward scaling",
        "canonical": "Domain-aware reward scaling",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This technique is a key innovation in the paper, addressing domain imbalance and enhancing policy learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
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
        "connectivity": 0.92,
        "specificity": 0.68,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Reinforcement Learning from Human Feedback",
      "resolved_canonical": "Reinforcement Learning from Human Feedback",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Group Relative Policy Optimization",
      "resolved_canonical": "Group Relative Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Domain-Informed Self-Consistency Policy Optimization",
      "resolved_canonical": "Domain-Informed Self-Consistency Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Domain-aware reward scaling",
      "resolved_canonical": "Domain-aware reward scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# DISCO Balances the Scales: Adaptive Domain- and Difficulty-Aware Reinforcement Learning on Imbalanced Data

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.15074.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2505.15074](https://arxiv.org/abs/2505.15074)

## 🔗 유사한 논문
- [[2025-09-24/Single-stream Policy Optimization_20250924|Single-stream Policy Optimization]] (85.4% similar)
- [[2025-09-25/Stepwise Guided Policy Optimization_ Coloring your Incorrect Reasoning in GRPO_20250925|Stepwise Guided Policy Optimization: Coloring your Incorrect Reasoning in GRPO]] (85.2% similar)
- [[2025-09-24/NGRPO_ Negative-enhanced Group Relative Policy Optimization_20250924|NGRPO: Negative-enhanced Group Relative Policy Optimization]] (85.2% similar)
- [[2025-09-25/Inverse Reinforcement Learning with Dynamic Reward Scaling for LLM Alignment_20250925|Inverse Reinforcement Learning with Dynamic Reward Scaling for LLM Alignment]] (84.8% similar)
- [[2025-09-24/DRO-REBEL_ Distributionally Robust Relative-Reward Regression for Fast and Efficient LLM Alignment_20250924|DRO-REBEL: Distributionally Robust Relative-Reward Regression for Fast and Efficient LLM Alignment]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Domain-aware reward scaling|Domain-aware reward scaling]]
**⚡ Unique Technical**: [[keywords/Reinforcement Learning from Human Feedback|Reinforcement Learning from Human Feedback]], [[keywords/Group Relative Policy Optimization|Group Relative Policy Optimization]], [[keywords/Domain-Informed Self-Consistency Policy Optimization|Domain-Informed Self-Consistency Policy Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.15074v3 Announce Type: replace-cross 
Abstract: Large Language Models (LLMs) are increasingly aligned with human preferences through Reinforcement Learning from Human Feedback (RLHF). Among RLHF methods, Group Relative Policy Optimization (GRPO) has gained attention for its simplicity and strong performance, notably eliminating the need for a learned value function. However, GRPO implicitly assumes a balanced domain distribution and uniform semantic alignment across groups, assumptions that rarely hold in real-world datasets. When applied to multi-domain, imbalanced data, GRPO disproportionately optimizes for dominant domains, neglecting underrepresented ones and resulting in poor generalization and fairness. We propose Domain-Informed Self-Consistency Policy Optimization (DISCO), a principled extension to GRPO that addresses inter-group imbalance with two key innovations. Domain-aware reward scaling counteracts frequency bias by reweighting optimization based on domain prevalence. Difficulty-aware reward scaling leverages prompt-level self-consistency to identify and prioritize uncertain prompts that offer greater learning value. Together, these strategies promote more equitable and effective policy learning across domains. Extensive experiments across multiple LLMs and skewed training distributions show that DISCO improves generalization, outperforms existing GRPO variants by 5% on Qwen3 models, and sets new state-of-the-art results on multi-domain alignment benchmarks. Our code and data are available at https://github.com/Tonyzhou98/disco_grpo.

## 📝 요약

이 논문은 인간 피드백을 통한 강화 학습(RLHF)을 사용하여 대형 언어 모델(LLM)을 인간의 선호에 맞추는 방법을 연구합니다. 기존의 GRPO 방법은 간단하고 성능이 뛰어나지만, 도메인 불균형 문제로 인해 특정 도메인에 치우치는 경향이 있습니다. 이를 해결하기 위해 제안된 DISCO는 도메인 인식 보상 스케일링과 난이도 인식 보상 스케일링을 통해 불균형을 개선합니다. 실험 결과, DISCO는 여러 LLM에서 일반화 성능을 향상시키며, 특히 Qwen3 모델에서 기존 GRPO 변형보다 5% 더 우수한 성능을 보였습니다. 이는 다중 도메인 정렬 벤치마크에서 새로운 최첨단 결과를 설정합니다.

## 🎯 주요 포인트

- 1. GRPO는 학습된 가치 함수 없이도 강력한 성능을 보이지만, 도메인 불균형 문제를 해결하지 못해 일반화와 공정성에서 한계를 드러냅니다.
- 2. DISCO는 GRPO의 도메인 불균형 문제를 해결하기 위해 도메인 인식 보상 스케일링과 난이도 인식 보상 스케일링을 도입했습니다.
- 3. 도메인 인식 보상 스케일링은 도메인 빈도를 기반으로 최적화를 재조정하여 빈도 편향을 상쇄합니다.
- 4. 난이도 인식 보상 스케일링은 프롬프트 수준의 자기 일관성을 활용해 불확실한 프롬프트를 식별하고 우선순위를 부여합니다.
- 5. DISCO는 여러 LLM과 불균형한 학습 분포에서 일반화를 개선하고, Qwen3 모델에서 기존 GRPO 변형보다 5% 더 나은 성능을 보였습니다.


---

*Generated on 2025-09-25 16:25:19*