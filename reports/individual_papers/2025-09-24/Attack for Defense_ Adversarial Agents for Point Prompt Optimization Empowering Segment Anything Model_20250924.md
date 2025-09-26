<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:10:37.663354",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Segment Anything Model",
    "Point Prompt Defender",
    "Deep Q-Network",
    "Adversarial Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Segment Anything Model": 0.9,
    "Point Prompt Defender": 0.85,
    "Deep Q-Network": 0.8,
    "Adversarial Reinforcement Learning": 0.9
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Segment Anything Model",
        "canonical": "Segment Anything Model",
        "aliases": [
          "SAM"
        ],
        "category": "unique_technical",
        "rationale": "This model is central to the paper's proposed framework and its optimization, making it a unique technical concept.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      },
      {
        "surface": "Point Prompt Defender",
        "canonical": "Point Prompt Defender",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The framework introduced in the paper, crucial for understanding the adversarial approach to prompt optimization.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Deep Q-Networks",
        "canonical": "Deep Q-Network",
        "aliases": [
          "DQN"
        ],
        "category": "specific_connectable",
        "rationale": "A key machine learning technique used in the paper, facilitating connections with reinforcement learning topics.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "adversarial reinforcement learning",
        "canonical": "Adversarial Reinforcement Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The paper's method relies on this approach, linking it to broader adversarial and reinforcement learning research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.9
      }
    ],
    "ban_list_suggestions": [
      "prompt",
      "environment",
      "agent"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Segment Anything Model",
      "resolved_canonical": "Segment Anything Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Point Prompt Defender",
      "resolved_canonical": "Point Prompt Defender",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Deep Q-Networks",
      "resolved_canonical": "Deep Q-Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "adversarial reinforcement learning",
      "resolved_canonical": "Adversarial Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.9
      }
    }
  ]
}
-->

# Attack for Defense: Adversarial Agents for Point Prompt Optimization Empowering Segment Anything Model

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18891.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18891](https://arxiv.org/abs/2509.18891)

## 🔗 유사한 논문
- [[2025-09-23/BiPrompt-SAM_ Enhancing Image Segmentation via Explicit Selection between Point and Text Prompts_20250923|BiPrompt-SAM: Enhancing Image Segmentation via Explicit Selection between Point and Text Prompts]] (87.5% similar)
- [[2025-09-24/HyPSAM_ Hybrid Prompt-driven Segment Anything Model for RGB-Thermal Salient Object Detection_20250924|HyPSAM: Hybrid Prompt-driven Segment Anything Model for RGB-Thermal Salient Object Detection]] (84.5% similar)
- [[2025-09-23/SAM-DCE_ Addressing Token Uniformity and Semantic Over-Smoothing in Medical Segmentation_20250923|SAM-DCE: Addressing Token Uniformity and Semantic Over-Smoothing in Medical Segmentation]] (84.3% similar)
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (83.8% similar)
- [[2025-09-23/DescriptorMedSAM_ Language-Image Fusion with Multi-Aspect Text Guidance for Medical Image Segmentation_20250923|DescriptorMedSAM: Language-Image Fusion with Multi-Aspect Text Guidance for Medical Image Segmentation]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Deep Q-Network|Deep Q-Network]], [[keywords/Adversarial Reinforcement Learning|Adversarial Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Segment Anything Model|Segment Anything Model]], [[keywords/Point Prompt Defender|Point Prompt Defender]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18891v1 Announce Type: new 
Abstract: Prompt quality plays a critical role in the performance of the Segment Anything Model (SAM), yet existing approaches often rely on heuristic or manually crafted prompts, limiting scalability and generalization. In this paper, we propose Point Prompt Defender, an adversarial reinforcement learning framework that adopts an attack-for-defense paradigm to automatically optimize point prompts. We construct a task-agnostic point prompt environment by representing image patches as nodes in a dual-space graph, where edges encode both physical and semantic distances. Within this environment, an attacker agent learns to activate a subset of prompts that maximally degrade SAM's segmentation performance, while a defender agent learns to suppress these disruptive prompts and restore accuracy. Both agents are trained using Deep Q-Networks with a reward signal based on segmentation quality variation. During inference, only the defender is deployed to refine arbitrary coarse prompt sets, enabling enhanced SAM segmentation performance across diverse tasks without retraining. Extensive experiments show that Point Prompt Defender effectively improves SAM's robustness and generalization, establishing a flexible, interpretable, and plug-and-play framework for prompt-based segmentation.

## 📝 요약

이 논문에서는 Segment Anything Model (SAM)의 성능을 향상시키기 위해 Point Prompt Defender라는 프레임워크를 제안합니다. 이는 공격-방어 패러다임을 채택한 적대적 강화 학습 방법으로, 자동으로 포인트 프롬프트를 최적화합니다. 이미지 패치를 이중 공간 그래프의 노드로 표현하여 물리적 및 의미적 거리를 인코딩하고, 공격자 에이전트는 SAM의 성능을 저하시키는 프롬프트를 활성화하며, 방어자 에이전트는 이를 억제하여 정확성을 회복합니다. 두 에이전트는 Deep Q-Networks를 사용해 학습하며, 방어자는 다양한 작업에서 SAM의 세분화 성능을 향상시킵니다. 실험 결과, Point Prompt Defender는 SAM의 견고성과 일반화를 효과적으로 개선하는 것으로 나타났습니다.

## 🎯 주요 포인트

- 1. Segment Anything Model(SAM)의 성능은 프롬프트의 품질에 크게 의존하며, 기존 접근법은 주로 수작업으로 만들어진 프롬프트에 의존하여 확장성과 일반화에 한계가 있다.
- 2. 본 논문에서는 공격-방어 패러다임을 채택하여 포인트 프롬프트를 자동으로 최적화하는 적대적 강화 학습 프레임워크인 Point Prompt Defender를 제안한다.
- 3. 이미지 패치를 이중 공간 그래프의 노드로 표현하여 물리적 및 의미적 거리를 인코딩하는 프롬프트 환경을 구축하고, 공격자 에이전트와 방어자 에이전트가 각각 프롬프트를 활성화 및 억제하여 세그먼트 성능을 조절한다.
- 4. 방어자 에이전트는 Deep Q-Networks를 사용하여 학습하며, 추론 시에는 방어자만 배치되어 다양한 작업에서 SAM의 세그먼트 성능을 향상시킨다.
- 5. 광범위한 실험 결과, Point Prompt Defender는 SAM의 견고성과 일반화를 효과적으로 개선하며, 프롬프트 기반 세분화를 위한 유연하고 해석 가능하며 플러그 앤 플레이 가능한 프레임워크를 확립한다.


---

*Generated on 2025-09-24 16:10:37*