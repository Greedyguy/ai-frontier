<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:18:32.962295",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "On-Manifold Exploration",
    "Latent Representation",
    "Robotic Manipulation",
    "Policy Self-Improvement"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "On-Manifold Exploration": 0.8,
    "Latent Representation": 0.72,
    "Robotic Manipulation": 0.75,
    "Policy Self-Improvement": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "On-Manifold Exploration",
        "canonical": "On-Manifold Exploration",
        "aliases": [
          "Manifold Exploration"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's approach and offers a novel method for enhancing exploration in robotic policies.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Latent Representation",
        "canonical": "Latent Representation",
        "aliases": [
          "Compact Latent Space"
        ],
        "category": "broad_technical",
        "rationale": "Latent representations are critical for understanding the structured space in which exploration occurs, linking to broader machine learning concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "Robotic Manipulation",
        "canonical": "Robotic Manipulation",
        "aliases": [
          "Robot Manipulation"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specific application area for the proposed method, connecting to existing work in robotics.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Policy Self-Improvement",
        "canonical": "Policy Self-Improvement",
        "aliases": [
          "Self-Improving Policies"
        ],
        "category": "unique_technical",
        "rationale": "The concept of self-improvement in policies is a unique contribution of the paper, relevant for linking to adaptive learning strategies.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "action mode collapse",
      "random perturbations",
      "task success rates"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "On-Manifold Exploration",
      "resolved_canonical": "On-Manifold Exploration",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Latent Representation",
      "resolved_canonical": "Latent Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Robotic Manipulation",
      "resolved_canonical": "Robotic Manipulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Policy Self-Improvement",
      "resolved_canonical": "Policy Self-Improvement",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SOE: Sample-Efficient Robot Policy Self-Improvement via On-Manifold Exploration

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19292.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19292](https://arxiv.org/abs/2509.19292)

## 🔗 유사한 논문
- [[2025-09-24/PEEK_ Guiding and Minimal Image Representations for Zero-Shot Generalization of Robot Manipulation Policies_20250924|PEEK: Guiding and Minimal Image Representations for Zero-Shot Generalization of Robot Manipulation Policies]] (83.5% similar)
- [[2025-09-23/Sight Over Site_ Perception-Aware Reinforcement Learning for Efficient Robotic Inspection_20250923|Sight Over Site: Perception-Aware Reinforcement Learning for Efficient Robotic Inspection]] (83.0% similar)
- [[2025-09-23/Latent Policy Steering with Embodiment-Agnostic Pretrained World Models_20250923|Latent Policy Steering with Embodiment-Agnostic Pretrained World Models]] (82.6% similar)
- [[2025-09-23/Sample-Efficient Reinforcement Learning with Symmetry-Guided Demonstrations for Robotic Manipulation_20250923|Sample-Efficient Reinforcement Learning with Symmetry-Guided Demonstrations for Robotic Manipulation]] (82.2% similar)
- [[2025-09-23/Safe Guaranteed Dynamics Exploration with Probabilistic Models_20250923|Safe Guaranteed Dynamics Exploration with Probabilistic Models]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Latent Representation|Latent Representation]]
**🔗 Specific Connectable**: [[keywords/Robotic Manipulation|Robotic Manipulation]]
**⚡ Unique Technical**: [[keywords/On-Manifold Exploration|On-Manifold Exploration]], [[keywords/Policy Self-Improvement|Policy Self-Improvement]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19292v1 Announce Type: cross 
Abstract: Intelligent agents progress by continually refining their capabilities through actively exploring environments. Yet robot policies often lack sufficient exploration capability due to action mode collapse. Existing methods that encourage exploration typically rely on random perturbations, which are unsafe and induce unstable, erratic behaviors, thereby limiting their effectiveness. We propose Self-Improvement via On-Manifold Exploration (SOE), a framework that enhances policy exploration and improvement in robotic manipulation. SOE learns a compact latent representation of task-relevant factors and constrains exploration to the manifold of valid actions, ensuring safety, diversity, and effectiveness. It can be seamlessly integrated with arbitrary policy models as a plug-in module, augmenting exploration without degrading the base policy performance. Moreover, the structured latent space enables human-guided exploration, further improving efficiency and controllability. Extensive experiments in both simulation and real-world tasks demonstrate that SOE consistently outperforms prior methods, achieving higher task success rates, smoother and safer exploration, and superior sample efficiency. These results establish on-manifold exploration as a principled approach to sample-efficient policy self-improvement. Project website: https://ericjin2002.github.io/SOE

## 📝 요약

이 논문은 로봇 조작에서 정책 탐색과 개선을 위한 새로운 프레임워크인 SOE(Self-Improvement via On-Manifold Exploration)를 제안합니다. 기존 방법들은 무작위 변동에 의존하여 불안정한 행동을 초래하는 반면, SOE는 작업 관련 요소의 잠재 표현을 학습하고 유효한 행동의 다양체에 탐색을 제한하여 안전성과 다양성을 보장합니다. 이 방법은 임의의 정책 모델에 플러그인 모듈로 통합 가능하며, 기본 정책 성능을 저하시키지 않고 탐색을 강화합니다. 또한, 구조화된 잠재 공간을 통해 인간이 탐색을 안내할 수 있어 효율성과 제어성을 높입니다. 시뮬레이션 및 실제 작업에서의 실험 결과, SOE는 기존 방법보다 높은 작업 성공률과 안전하고 매끄러운 탐색, 뛰어난 샘플 효율성을 보여줍니다. 이러한 결과는 다양체 기반 탐색이 샘플 효율적인 정책 자기 개선을 위한 원칙적인 접근법임을 입증합니다.

## 🎯 주요 포인트

- 1. SOE는 로봇 조작에서 정책 탐색과 개선을 강화하는 프레임워크로, 유효한 행동의 매니폴드에 탐색을 제한하여 안전성과 다양성, 효과성을 보장합니다.
- 2. SOE는 임의의 정책 모델과 플러그인 모듈로 통합될 수 있어, 기본 정책 성능을 저하시키지 않으면서 탐색을 증대시킵니다.
- 3. 구조화된 잠재 공간은 인간이 탐색을 안내할 수 있게 하여 효율성과 제어 가능성을 더욱 향상시킵니다.
- 4. 시뮬레이션 및 실제 작업에서의 광범위한 실험 결과, SOE는 이전 방법들보다 일관되게 높은 작업 성공률과 부드럽고 안전한 탐색, 우수한 샘플 효율성을 달성합니다.
- 5. 매니폴드 탐색은 샘플 효율적인 정책 자기 개선을 위한 원칙적인 접근법으로 자리 잡았습니다.


---

*Generated on 2025-09-24 14:18:32*