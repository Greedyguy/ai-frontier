<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:44:20.711901",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Vision-Language Model",
    "Policy-agnostic Extraction of Essential Keypoints",
    "End-effector Paths"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.85,
    "Vision-Language Model": 0.89,
    "Policy-agnostic Extraction of Essential Keypoints": 0.8,
    "End-effector Paths": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-Shot Generalization",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot learning is crucial for understanding how the model generalizes without prior examples, directly linking to existing research on learning paradigms.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-language models are central to the paper's approach, providing a bridge between visual and linguistic data processing.",
        "novelty_score": 0.6,
        "connectivity_score": 0.9,
        "specificity_score": 0.78,
        "link_intent_score": 0.89
      },
      {
        "surface": "PEEK",
        "canonical": "Policy-agnostic Extraction of Essential Keypoints",
        "aliases": [
          "PEEK"
        ],
        "category": "unique_technical",
        "rationale": "PEEK is a novel method introduced in the paper, representing a unique contribution to robot manipulation policy generalization.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "End-effector Paths",
        "canonical": "End-effector Paths",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "End-effector paths are a specific technical aspect of the manipulation policies, crucial for understanding action execution.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "robot",
      "manipulation",
      "policy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Zero-Shot Generalization",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.9,
        "specificity": 0.78,
        "link_intent": 0.89
      }
    },
    {
      "candidate_surface": "PEEK",
      "resolved_canonical": "Policy-agnostic Extraction of Essential Keypoints",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "End-effector Paths",
      "resolved_canonical": "End-effector Paths",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# PEEK: Guiding and Minimal Image Representations for Zero-Shot Generalization of Robot Manipulation Policies

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18282.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18282](https://arxiv.org/abs/2509.18282)

## 🔗 유사한 논문
- [[2025-09-23/Latent Policy Steering with Embodiment-Agnostic Pretrained World Models_20250923|Latent Policy Steering with Embodiment-Agnostic Pretrained World Models]] (86.7% similar)
- [[2025-09-18/Robot Control Stack_ A Lean Ecosystem for Robot Learning at Scale_20250918|Robot Control Stack: A Lean Ecosystem for Robot Learning at Scale]] (86.2% similar)
- [[2025-09-22/GP3_ A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation_20250922|GP3: A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation]] (85.7% similar)
- [[2025-09-22/A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning_20250922|A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning]] (85.4% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Policy-agnostic Extraction of Essential Keypoints|Policy-agnostic Extraction of Essential Keypoints]], [[keywords/End-effector Paths|End-effector Paths]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18282v1 Announce Type: cross 
Abstract: Robotic manipulation policies often fail to generalize because they must simultaneously learn where to attend, what actions to take, and how to execute them. We argue that high-level reasoning about where and what can be offloaded to vision-language models (VLMs), leaving policies to specialize in how to act. We present PEEK (Policy-agnostic Extraction of Essential Keypoints), which fine-tunes VLMs to predict a unified point-based intermediate representation: 1. end-effector paths specifying what actions to take, and 2. task-relevant masks indicating where to focus. These annotations are directly overlaid onto robot observations, making the representation policy-agnostic and transferable across architectures. To enable scalable training, we introduce an automatic annotation pipeline, generating labeled data across 20+ robot datasets spanning 9 embodiments. In real-world evaluations, PEEK consistently boosts zero-shot generalization, including a 41.4x real-world improvement for a 3D policy trained only in simulation, and 2-3.5x gains for both large VLAs and small manipulation policies. By letting VLMs absorb semantic and visual complexity, PEEK equips manipulation policies with the minimal cues they need--where, what, and how. Website at https://peek-robot.github.io/.

## 📝 요약

로봇 조작 정책은 일반화에 어려움을 겪는데, 이는 어디에 주목하고 어떤 행동을 취하며 어떻게 실행할지를 동시에 학습해야 하기 때문입니다. 본 연구에서는 고차원적 추론을 시각-언어 모델(VLMs)에 맡기고, 정책은 행동 실행에 집중하도록 제안합니다. 이를 위해 PEEK(Policy-agnostic Extraction of Essential Keypoints)를 소개하며, VLMs를 미세 조정하여 통합된 중간 표현을 예측하도록 합니다. 이 표현은 로봇 관찰에 직접 적용되어 정책에 구애받지 않고 다양한 구조에 전이 가능합니다. 자동 주석 파이프라인을 도입해 20개 이상의 로봇 데이터셋에서 주석 데이터를 생성하며, 실제 평가에서 PEEK는 제로샷 일반화를 크게 향상시켰습니다. 시뮬레이션에서만 훈련된 3D 정책의 경우 41.4배, 대형 VLA와 소형 조작 정책에서는 2-3.5배의 성능 향상을 보였습니다. PEEK는 시각 및 의미적 복잡성을 VLMs에 흡수시켜 조작 정책에 필요한 최소한의 단서를 제공합니다.

## 🎯 주요 포인트

- 1. 로봇 조작 정책의 일반화 문제를 해결하기 위해 시각-언어 모델(VLMs)을 활용하여 고수준의 '어디'와 '무엇'에 대한 추론을 담당하게 하고, 정책은 '어떻게' 행동할지를 전문화하도록 제안합니다.
- 2. PEEK(Policy-agnostic Extraction of Essential Keypoints)은 VLMs를 미세 조정하여 통합된 점 기반 중간 표현을 예측하도록 하며, 이는 로봇 관찰에 직접 오버레이되어 정책에 구애받지 않고 다양한 아키텍처에 전이 가능합니다.
- 3. 자동 주석 파이프라인을 도입하여 9개의 구현을 포함한 20개 이상의 로봇 데이터 세트에서 라벨이 지정된 데이터를 생성함으로써 대규모 학습을 가능하게 합니다.
- 4. 실제 평가에서 PEEK는 시뮬레이션에서만 훈련된 3D 정책의 41.4배 실세계 개선을 포함하여, 대형 VLA와 소형 조작 정책 모두에서 2-3.5배의 제로샷 일반화 성능 향상을 보여줍니다.
- 5. PEEK는 VLMs가 의미적 및 시각적 복잡성을 흡수하게 하여 조작 정책에 필요한 최소한의 단서(어디, 무엇, 어떻게)를 제공합니다.


---

*Generated on 2025-09-24 13:44:20*