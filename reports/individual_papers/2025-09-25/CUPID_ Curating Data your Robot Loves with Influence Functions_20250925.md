---
keywords:
  - Imitation Learning
  - Influence Functions
  - Closed-loop Performance
  - Distribution Shift
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2506.19121
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:28:56.177415",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Imitation Learning",
    "Influence Functions",
    "Closed-loop Performance",
    "Distribution Shift"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Imitation Learning": 0.78,
    "Influence Functions": 0.8,
    "Closed-loop Performance": 0.7,
    "Distribution Shift": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Imitation Learning",
        "canonical": "Imitation Learning",
        "aliases": [
          "Behavioral Cloning",
          "Learning from Demonstration"
        ],
        "category": "specific_connectable",
        "rationale": "Imitation Learning is a specific technique within machine learning that directly relates to the paper's focus on policy performance from demonstration data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Influence Functions",
        "canonical": "Influence Functions",
        "aliases": [
          "Influence Analysis"
        ],
        "category": "unique_technical",
        "rationale": "Influence Functions are central to the proposed method CUPID, providing a novel approach to data curation in imitation learning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Closed-loop Performance",
        "canonical": "Closed-loop Performance",
        "aliases": [
          "Feedback Loop Performance"
        ],
        "category": "unique_technical",
        "rationale": "Closed-loop Performance is a key outcome measure in the paper, relevant for understanding the effectiveness of the curated data.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Distribution Shift",
        "canonical": "Distribution Shift",
        "aliases": [
          "Domain Shift",
          "Covariate Shift"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding and handling Distribution Shift is crucial for the robustness of machine learning models, especially in robotics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "robot",
      "data",
      "method",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Imitation Learning",
      "resolved_canonical": "Imitation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Influence Functions",
      "resolved_canonical": "Influence Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Closed-loop Performance",
      "resolved_canonical": "Closed-loop Performance",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Distribution Shift",
      "resolved_canonical": "Distribution Shift",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# CUPID: Curating Data your Robot Loves with Influence Functions

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.19121.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2506.19121](https://arxiv.org/abs/2506.19121)

## 🔗 유사한 논문
- [[2025-09-23/Latent Policy Steering with Embodiment-Agnostic Pretrained World Models_20250923|Latent Policy Steering with Embodiment-Agnostic Pretrained World Models]] (83.3% similar)
- [[2025-09-24/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training_20250924|Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training]] (83.0% similar)
- [[2025-09-24/PEEK_ Guiding and Minimal Image Representations for Zero-Shot Generalization of Robot Manipulation Policies_20250924|PEEK: Guiding and Minimal Image Representations for Zero-Shot Generalization of Robot Manipulation Policies]] (82.3% similar)
- [[2025-09-22/Uncertainty-Based Smooth Policy Regularisation for Reinforcement Learning with Few Demonstrations_20250922|Uncertainty-Based Smooth Policy Regularisation for Reinforcement Learning with Few Demonstrations]] (82.1% similar)
- [[2025-09-23/UniSkill_ Imitating Human Videos via Cross-Embodiment Skill Representations_20250923|UniSkill: Imitating Human Videos via Cross-Embodiment Skill Representations]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Imitation Learning|Imitation Learning]], [[keywords/Distribution Shift|Distribution Shift]]
**⚡ Unique Technical**: [[keywords/Influence Functions|Influence Functions]], [[keywords/Closed-loop Performance|Closed-loop Performance]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.19121v2 Announce Type: replace-cross 
Abstract: In robot imitation learning, policy performance is tightly coupled with the quality and composition of the demonstration data. Yet, developing a precise understanding of how individual demonstrations contribute to downstream outcomes - such as closed-loop task success or failure - remains a persistent challenge. We propose CUPID, a robot data curation method based on a novel influence function-theoretic formulation for imitation learning policies. Given a set of evaluation rollouts, CUPID estimates the influence of each training demonstration on the policy's expected return. This enables ranking and selection of demonstrations according to their impact on the policy's closed-loop performance. We use CUPID to curate data by 1) filtering out training demonstrations that harm policy performance and 2) subselecting newly collected trajectories that will most improve the policy. Extensive simulated and hardware experiments show that our approach consistently identifies which data drives test-time performance. For example, training with less than 33% of curated data can yield state-of-the-art diffusion policies on the simulated RoboMimic benchmark, with similar gains observed in hardware. Furthermore, hardware experiments show that our method can identify robust strategies under distribution shift, isolate spurious correlations, and even enhance the post-training of generalist robot policies. Videos and code are made available at: https://cupid-curation.github.io.

## 📝 요약

이 논문에서는 로봇 모방 학습에서 시연 데이터의 품질과 구성이 정책 성능에 미치는 영향을 분석하기 위해 CUPID라는 데이터 큐레이션 방법을 제안합니다. CUPID는 새로운 영향 함수 이론을 기반으로 하여 각 시연이 정책의 기대 수익에 미치는 영향을 추정합니다. 이를 통해 정책의 성능에 긍정적 영향을 미치는 시연을 선별하고, 성능을 저해하는 데이터를 필터링합니다. 시뮬레이션 및 하드웨어 실험에서 CUPID는 테스트 성능에 기여하는 데이터를 효과적으로 식별하며, RoboMimic 벤치마크에서 33% 미만의 데이터로도 최첨단 성능을 달성할 수 있음을 보여줍니다. 또한, 분포 변화에 강한 전략을 식별하고, 잘못된 상관관계를 분리하며, 일반 로봇 정책의 후속 학습을 향상시킬 수 있음을 입증합니다.

## 🎯 주요 포인트

- 1. CUPID는 로봇 모방 학습 정책을 위한 새로운 영향 함수 이론적 접근을 기반으로 한 데이터 큐레이션 방법입니다.
- 2. CUPID는 각 훈련 시연이 정책의 기대 수익에 미치는 영향을 추정하여 시연을 정책의 성능에 따라 순위화하고 선택할 수 있게 합니다.
- 3. CUPID를 통해 정책 성능을 저해하는 시연을 필터링하고, 정책을 가장 향상시킬 수 있는 새로운 경로를 선택할 수 있습니다.
- 4. 실험 결과, 전체 데이터의 33% 미만을 사용해도 최첨단 확산 정책을 달성할 수 있으며, 하드웨어 실험에서도 유사한 성과를 보였습니다.
- 5. CUPID는 분포 변화에 강한 전략을 식별하고, 잘못된 상관관계를 분리하며, 일반 로봇 정책의 사후 학습을 향상시킬 수 있습니다.


---

*Generated on 2025-09-25 16:28:56*