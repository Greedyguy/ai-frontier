<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:59:10.237306",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Visuomotor Policies",
    "Proprioceptive States",
    "State-free Policy",
    "Robot Manipulation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Visuomotor Policies": 0.75,
    "Proprioceptive States": 0.73,
    "State-free Policy": 0.78,
    "Robot Manipulation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Visuomotor Policies",
        "canonical": "Visuomotor Policies",
        "aliases": [
          "Visual-Motor Policies"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and connects to research on robot control strategies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Proprioceptive States",
        "canonical": "Proprioceptive States",
        "aliases": [
          "Proprioceptive Inputs"
        ],
        "category": "unique_technical",
        "rationale": "Understanding the role of proprioceptive states is crucial for linking studies on sensory input in robotics.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.73
      },
      {
        "surface": "State-free Policy",
        "canonical": "State-free Policy",
        "aliases": [
          "State-independent Policy"
        ],
        "category": "unique_technical",
        "rationale": "This novel approach is a key contribution of the paper and offers a new perspective on policy design.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Robot Manipulation",
        "canonical": "Robot Manipulation",
        "aliases": [
          "Robotic Manipulation"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental area in robotics that connects to various manipulation techniques and strategies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "Imitation Learning",
      "Spatial Generalization"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Visuomotor Policies",
      "resolved_canonical": "Visuomotor Policies",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Proprioceptive States",
      "resolved_canonical": "Proprioceptive States",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.73
      }
    },
    {
      "candidate_surface": "State-free Policy",
      "resolved_canonical": "State-free Policy",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Robot Manipulation",
      "resolved_canonical": "Robot Manipulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Do You Need Proprioceptive States in Visuomotor Policies?

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18644.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18644](https://arxiv.org/abs/2509.18644)

## 🔗 유사한 논문
- [[2025-09-23/Latent Policy Steering with Embodiment-Agnostic Pretrained World Models_20250923|Latent Policy Steering with Embodiment-Agnostic Pretrained World Models]] (87.7% similar)
- [[2025-09-24/PEEK_ Guiding and Minimal Image Representations for Zero-Shot Generalization of Robot Manipulation Policies_20250924|PEEK: Guiding and Minimal Image Representations for Zero-Shot Generalization of Robot Manipulation Policies]] (85.6% similar)
- [[2025-09-22/GP3_ A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation_20250922|GP3: A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation]] (84.9% similar)
- [[2025-09-24/Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training_20250924|Generalizable Domain Adaptation for Sim-and-Real Policy Co-Training]] (83.7% similar)
- [[2025-09-23/Prepare Before You Act_ Learning From Humans to Rearrange Initial States_20250923|Prepare Before You Act: Learning From Humans to Rearrange Initial States]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Robot Manipulation|Robot Manipulation]]
**⚡ Unique Technical**: [[keywords/Visuomotor Policies|Visuomotor Policies]], [[keywords/Proprioceptive States|Proprioceptive States]], [[keywords/State-free Policy|State-free Policy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18644v1 Announce Type: cross 
Abstract: Imitation-learning-based visuomotor policies have been widely used in robot manipulation, where both visual observations and proprioceptive states are typically adopted together for precise control. However, in this study, we find that this common practice makes the policy overly reliant on the proprioceptive state input, which causes overfitting to the training trajectories and results in poor spatial generalization. On the contrary, we propose the State-free Policy, removing the proprioceptive state input and predicting actions only conditioned on visual observations. The State-free Policy is built in the relative end-effector action space, and should ensure the full task-relevant visual observations, here provided by dual wide-angle wrist cameras. Empirical results demonstrate that the State-free policy achieves significantly stronger spatial generalization than the state-based policy: in real-world tasks such as pick-and-place, challenging shirt-folding, and complex whole-body manipulation, spanning multiple robot embodiments, the average success rate improves from 0\% to 85\% in height generalization and from 6\% to 64\% in horizontal generalization. Furthermore, they also show advantages in data efficiency and cross-embodiment adaptation, enhancing their practicality for real-world deployment.

## 📝 요약

이 논문은 로봇 조작에서 모방 학습 기반의 시각-운동 정책이 일반적으로 시각적 관찰과 고유 감각 상태를 함께 사용하지만, 이는 훈련 경로에 과적합되어 공간 일반화가 저하된다고 지적합니다. 이를 해결하기 위해, 고유 감각 상태 입력을 제거하고 시각적 관찰에만 기반한 '상태 비의존 정책'을 제안합니다. 이 정책은 상대적 말단 작용 공간에서 작동하며, 듀얼 광각 손목 카메라를 통해 시각 정보를 제공합니다. 실험 결과, 이 정책은 기존의 상태 기반 정책보다 공간 일반화에서 우수한 성능을 보였으며, 실제 작업에서 성공률이 높아졌습니다. 또한 데이터 효율성과 다양한 로봇 적용 가능성에서도 장점을 보여 실제 환경에서의 활용 가능성을 높였습니다.

## 🎯 주요 포인트

- 1. 기존의 모방 학습 기반 시각-운동 정책은 고유 감각 상태 입력에 과도하게 의존하여 훈련 경로에 과적합되고 공간 일반화가 저조합니다.
- 2. 본 연구에서는 고유 감각 상태 입력을 제거하고 시각적 관찰에만 의존하는 State-free Policy를 제안합니다.
- 3. State-free Policy는 상대적인 말단 작용 공간에서 구축되며, 듀얼 광각 손목 카메라를 통해 과제 관련 시각 정보를 완전히 확보해야 합니다.
- 4. 실험 결과, State-free Policy는 공간 일반화에서 기존의 상태 기반 정책보다 월등히 뛰어난 성능을 보입니다.
- 5. State-free Policy는 데이터 효율성과 다양한 로봇 구현 간 적응력에서도 장점을 보여 실제 적용 가능성을 높입니다.


---

*Generated on 2025-09-24 13:59:10*