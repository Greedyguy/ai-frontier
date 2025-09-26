---
keywords:
  - Vision-Language Model
  - Adversarial Attacks
  - FreezeVLA
  - Multimodal Learning
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19870
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:08:31.906891",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Adversarial Attacks",
    "FreezeVLA",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Adversarial Attacks": 0.8,
    "FreezeVLA": 0.78,
    "Multimodal Learning": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language-Action models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLA models"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's discussion and connect with recent advancements in multimodal learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "adversarial attacks",
        "canonical": "Adversarial Attacks",
        "aliases": [
          "adversarial vulnerability"
        ],
        "category": "broad_technical",
        "rationale": "Adversarial attacks are a crucial aspect of the paper, linking to broader discussions in machine learning safety.",
        "novelty_score": 0.35,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "FreezeVLA",
        "canonical": "FreezeVLA",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "FreezeVLA is a novel attack framework introduced in the paper, essential for understanding the proposed methodology.",
        "novelty_score": 0.9,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "multimodal inputs",
        "canonical": "Multimodal Learning",
        "aliases": [
          "multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is a key concept in understanding how VLA models process diverse data types.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "robot",
      "task",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-Language-Action models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "adversarial attacks",
      "resolved_canonical": "Adversarial Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.35,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "FreezeVLA",
      "resolved_canonical": "FreezeVLA",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "multimodal inputs",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# FreezeVLA: Action-Freezing Attacks against Vision-Language-Action Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19870.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19870](https://arxiv.org/abs/2509.19870)

## 🔗 유사한 논문
- [[2025-09-24/Pure Vision Language Action (VLA) Models_ A Comprehensive Survey_20250924|Pure Vision Language Action (VLA) Models: A Comprehensive Survey]] (88.7% similar)
- [[2025-09-24/Eva-VLA_ Evaluating Vision-Language-Action Models' Robustness Under Real-World Physical Variations_20250924|Eva-VLA: Evaluating Vision-Language-Action Models' Robustness Under Real-World Physical Variations]] (87.8% similar)
- [[2025-09-23/ADVEDM_Fine-grained Adversarial Attack against VLM-based Embodied Agents_20250923|ADVEDM:Fine-grained Adversarial Attack against VLM-based Embodied Agents]] (87.3% similar)
- [[2025-09-19/ForceVLA_ Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation_20250919|ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]] (86.6% similar)
- [[2025-09-23/Evo-0_ Vision-Language-Action Model with Implicit Spatial Understanding_20250923|Evo-0: Vision-Language-Action Model with Implicit Spatial Understanding]] (86.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Adversarial Attacks|Adversarial Attacks]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/FreezeVLA|FreezeVLA]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19870v1 Announce Type: new 
Abstract: Vision-Language-Action (VLA) models are driving rapid progress in robotics by enabling agents to interpret multimodal inputs and execute complex, long-horizon tasks. However, their safety and robustness against adversarial attacks remain largely underexplored. In this work, we identify and formalize a critical adversarial vulnerability in which adversarial images can "freeze" VLA models and cause them to ignore subsequent instructions. This threat effectively disconnects the robot's digital mind from its physical actions, potentially inducing inaction during critical interventions. To systematically study this vulnerability, we propose FreezeVLA, a novel attack framework that generates and evaluates action-freezing attacks via min-max bi-level optimization. Experiments on three state-of-the-art VLA models and four robotic benchmarks show that FreezeVLA attains an average attack success rate of 76.2%, significantly outperforming existing methods. Moreover, adversarial images generated by FreezeVLA exhibit strong transferability, with a single image reliably inducing paralysis across diverse language prompts. Our findings expose a critical safety risk in VLA models and highlight the urgent need for robust defense mechanisms.

## 📝 요약

이 논문은 Vision-Language-Action(VLA) 모델의 안전성과 적대적 공격에 대한 취약성을 탐구합니다. 연구에서는 VLA 모델이 적대적 이미지에 의해 "동결"되어 이후의 명령을 무시하는 취약점을 식별하고 이를 공식화했습니다. 이를 통해 로봇의 디지털 판단과 물리적 행동 간의 연결이 끊어져 중요한 상황에서 무작위 행동이 발생할 수 있습니다. 이 취약점을 체계적으로 연구하기 위해 FreezeVLA라는 새로운 공격 프레임워크를 제안하여, 세 가지 최신 VLA 모델과 네 가지 로봇 벤치마크에서 평균 76.2%의 공격 성공률을 기록했습니다. FreezeVLA가 생성한 적대적 이미지는 강한 전이성을 보여 다양한 언어 명령에서도 일관되게 마비를 유도합니다. 이 연구는 VLA 모델의 중요한 안전 위험을 드러내며, 강력한 방어 메커니즘의 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. Vision-Language-Action(VLA) 모델은 로봇 공학에서 멀티모달 입력을 해석하고 복잡한 작업을 수행할 수 있게 하여 빠른 발전을 이끌고 있다.
- 2. VLA 모델의 안전성과 적대적 공격에 대한 강건성은 아직 충분히 탐구되지 않았다.
- 3. FreezeVLA라는 새로운 공격 프레임워크를 제안하여 VLA 모델의 행동 정지 취약점을 체계적으로 연구하였다.
- 4. FreezeVLA는 세 가지 최신 VLA 모델과 네 가지 로봇 벤치마크에서 평균 76.2%의 공격 성공률을 기록하며 기존 방법을 능가했다.
- 5. FreezeVLA로 생성된 적대적 이미지는 다양한 언어 프롬프트에서 마비를 유도할 수 있는 높은 전이성을 보였다.


---

*Generated on 2025-09-26 09:08:31*