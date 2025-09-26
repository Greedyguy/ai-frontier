<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:21:06.424248",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Mixture Modeling",
    "Context-aware Routing",
    "Reinforcement Learning from Human Feedback"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.78,
    "Mixture Modeling": 0.72,
    "Context-aware Routing": 0.7,
    "Reinforcement Learning from Human Feedback": 0.75
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
        "rationale": "LLMs are central to the paper's discussion on personalization and alignment, linking to broader discussions in AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Mixture Modeling",
        "canonical": "Mixture Modeling",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a core component of the proposed framework, critical for understanding the method's novelty.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "Context-aware Routing",
        "canonical": "Context-aware Routing",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is essential for the paper's approach to personalized preference learning, highlighting its novel routing strategy.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Reinforcement Learning from Human Feedback",
        "canonical": "Reinforcement Learning from Human Feedback",
        "aliases": [
          "RLHF"
        ],
        "category": "specific_connectable",
        "rationale": "RLHF is a key technique discussed in the context of aligning LLMs, connecting to broader reinforcement learning topics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "reward modeling",
      "human preferences"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Mixture Modeling",
      "resolved_canonical": "Mixture Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Context-aware Routing",
      "resolved_canonical": "Context-aware Routing",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Reinforcement Learning from Human Feedback",
      "resolved_canonical": "Reinforcement Learning from Human Feedback",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# MiCRo: Mixture Modeling and Context-aware Routing for Personalized Preference Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.24846.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2505.24846](https://arxiv.org/abs/2505.24846)

## 🔗 유사한 논문
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL: Replacing Human Feedback for Reward Shaping]] (86.0% similar)
- [[2025-09-23/Post-hoc Reward Calibration_ A Case Study on Length Bias_20250923|Post-hoc Reward Calibration: A Case Study on Length Bias]] (85.8% similar)
- [[2025-09-23/R3_ Robust Rubric-Agnostic Reward Models_20250923|R3: Robust Rubric-Agnostic Reward Models]] (85.0% similar)
- [[2025-09-22/BaseReward_ A Strong Baseline for Multimodal Reward Model_20250922|BaseReward: A Strong Baseline for Multimodal Reward Model]] (84.6% similar)
- [[2025-09-18/Aligning Audio Captions with Human Preferences_20250918|Aligning Audio Captions with Human Preferences]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning from Human Feedback|Reinforcement Learning from Human Feedback]]
**⚡ Unique Technical**: [[keywords/Mixture Modeling|Mixture Modeling]], [[keywords/Context-aware Routing|Context-aware Routing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.24846v2 Announce Type: replace 
Abstract: Reward modeling is a key step in building safe foundation models when applying reinforcement learning from human feedback (RLHF) to align Large Language Models (LLMs). However, reward modeling based on the Bradley-Terry (BT) model assumes a global reward function, failing to capture the inherently diverse and heterogeneous human preferences. Hence, such oversimplification limits LLMs from supporting personalization and pluralistic alignment. Theoretically, we show that when human preferences follow a mixture distribution of diverse subgroups, a single BT model has an irreducible error. While existing solutions, such as multi-objective learning with fine-grained annotations, help address this issue, they are costly and constrained by predefined attributes, failing to fully capture the richness of human values. In this work, we introduce MiCRo, a two-stage framework that enhances personalized preference learning by leveraging large-scale binary preference datasets without requiring explicit fine-grained annotations. In the first stage, MiCRo introduces context-aware mixture modeling approach to capture diverse human preferences. In the second stage, MiCRo integrates an online routing strategy that dynamically adapts mixture weights based on specific context to resolve ambiguity, allowing for efficient and scalable preference adaptation with minimal additional supervision. Experiments on multiple preference datasets demonstrate that MiCRo effectively captures diverse human preferences and significantly improves downstream personalization.

## 📝 요약

이 논문은 인간 피드백을 통한 강화 학습(RLHF)을 활용하여 대형 언어 모델(LLM)을 정렬할 때 보상 모델링의 중요성을 강조합니다. 기존의 Bradley-Terry(BT) 모델 기반 보상 모델링은 인간의 다양한 선호도를 충분히 반영하지 못해 개인화와 다원적 정렬에 한계가 있습니다. 이를 해결하기 위해, 저자들은 MiCRo라는 두 단계 프레임워크를 제안합니다. 첫 번째 단계에서는 대규모 이진 선호 데이터셋을 활용하여 맥락 인식 혼합 모델링 접근법을 통해 다양한 인간 선호를 포착합니다. 두 번째 단계에서는 온라인 라우팅 전략을 도입하여 맥락에 따라 혼합 가중치를 동적으로 조정함으로써 효율적이고 확장 가능한 선호 적응을 가능하게 합니다. 실험 결과, MiCRo는 다양한 인간 선호를 효과적으로 포착하며 개인화 성능을 크게 향상시킵니다.

## 🎯 주요 포인트

- 1. 보상 모델링은 인간 피드백을 활용한 강화 학습에서 대형 언어 모델을 안전하게 정렬하기 위한 핵심 단계입니다.
- 2. Bradley-Terry 모델 기반의 보상 모델링은 인간의 다양한 선호도를 충분히 반영하지 못해 개인화 및 다원적 정렬을 제한합니다.
- 3. MiCRo는 대규모 이진 선호 데이터셋을 활용하여 명시적인 세부 주석 없이 개인화된 선호 학습을 향상시키는 두 단계 프레임워크입니다.
- 4. MiCRo는 문맥 인식 혼합 모델링 접근법과 온라인 라우팅 전략을 통해 다양한 인간 선호를 효과적으로 포착하고, 효율적이고 확장 가능한 선호 적응을 가능하게 합니다.
- 5. 여러 선호 데이터셋에 대한 실험 결과, MiCRo는 다양한 인간 선호를 효과적으로 포착하고, 하위 개인화를 크게 개선합니다.


---

*Generated on 2025-09-24 14:21:06*