---
keywords:
  - Transformer
  - Multimodal Learning
  - Diffusion Models
  - Trajectory Anchors
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20253
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:04:35.091592",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Multimodal Learning",
    "Diffusion Models",
    "Trajectory Anchors"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Multimodal Learning": 0.82,
    "Diffusion Models": 0.75,
    "Trajectory Anchors": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational architecture in deep learning, crucial for processing sequential data.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "end-to-end multi-modal planning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "multi-modal planning"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal learning is key for integrating diverse data types, enhancing autonomous driving systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.87,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "diffusion policy",
        "canonical": "Diffusion Models",
        "aliases": [
          "diffusion policy"
        ],
        "category": "unique_technical",
        "rationale": "Diffusion models are emerging as a powerful generative approach, relevant for trajectory prediction.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "trajectory anchors",
        "canonical": "Trajectory Anchors",
        "aliases": [
          "hybrid trajectory anchors"
        ],
        "category": "unique_technical",
        "rationale": "Trajectory anchors provide a novel method for initializing planning algorithms in autonomous systems.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "end-to-end",
      "framework",
      "state-of-the-art"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "end-to-end multi-modal planning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.87,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "diffusion policy",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "trajectory anchors",
      "resolved_canonical": "Trajectory Anchors",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# AnchDrive: Bootstrapping Diffusion Policies with Hybrid Trajectory Anchors for End-to-End Driving

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20253.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20253](https://arxiv.org/abs/2509.20253)

## 🔗 유사한 논문
- [[2025-09-25/Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving_20250925|Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving]] (86.2% similar)
- [[2025-09-18/FlightDiffusion_ Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video_20250918|FlightDiffusion: Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (85.1% similar)
- [[2025-09-19/FlowDrive_ Energy Flow Field for End-to-End Autonomous Driving_20250919|FlowDrive: Energy Flow Field for End-to-End Autonomous Driving]] (84.4% similar)
- [[2025-09-23/DriveDPO_ Policy Learning via Safety DPO For End-to-End Autonomous Driving_20250923|DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving]] (83.2% similar)
- [[2025-09-22/CoPAD _ Multi-source Trajectory Fusion and Cooperative Trajectory Prediction with Anchor-oriented Decoder in V2X Scenarios_20250922|CoPAD : Multi-source Trajectory Fusion and Cooperative Trajectory Prediction with Anchor-oriented Decoder in V2X Scenarios]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Diffusion Models|Diffusion Models]], [[keywords/Trajectory Anchors|Trajectory Anchors]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20253v1 Announce Type: cross 
Abstract: End-to-end multi-modal planning has become a transformative paradigm in autonomous driving, effectively addressing behavioral multi-modality and the generalization challenge in long-tail scenarios. We propose AnchDrive, a framework for end-to-end driving that effectively bootstraps a diffusion policy to mitigate the high computational cost of traditional generative models. Rather than denoising from pure noise, AnchDrive initializes its planner with a rich set of hybrid trajectory anchors. These anchors are derived from two complementary sources: a static vocabulary of general driving priors and a set of dynamic, context-aware trajectories. The dynamic trajectories are decoded in real-time by a Transformer that processes dense and sparse perceptual features. The diffusion model then learns to refine these anchors by predicting a distribution of trajectory offsets, enabling fine-grained refinement. This anchor-based bootstrapping design allows for efficient generation of diverse, high-quality trajectories. Experiments on the NAVSIM benchmark confirm that AnchDrive sets a new state-of-the-art and shows strong gen?eralizability

## 📝 요약

AnchDrive는 자율 주행에서 엔드 투 엔드 멀티모달 계획을 위한 프레임워크로, 전통적인 생성 모델의 높은 계산 비용을 줄이기 위해 확산 정책을 활용합니다. 이 프레임워크는 순수한 노이즈에서 시작하는 대신, 일반적인 주행 사전 지식과 동적, 상황 인식 궤적에서 파생된 하이브리드 궤적 앵커를 사용하여 계획을 초기화합니다. 동적 궤적은 Transformer를 통해 실시간으로 해독되며, 확산 모델은 궤적 오프셋 분포를 예측하여 앵커를 정교하게 다듬습니다. 이러한 앵커 기반 부트스트래핑 설계는 다양한 고품질 궤적을 효율적으로 생성할 수 있게 합니다. NAVSIM 벤치마크 실험에서 AnchDrive는 새로운 최첨단 성능을 기록하며 높은 일반화 능력을 보였습니다.

## 🎯 주요 포인트

- 1. AnchDrive는 하이브리드 궤적 앵커를 사용하여 전통적인 생성 모델의 높은 계산 비용을 줄이는 엔드 투 엔드 운전 프레임워크입니다.
- 2. 앵커는 일반 운전 사전 지식의 정적 어휘와 동적, 상황 인식 궤적으로부터 파생됩니다.
- 3. Transformer는 조밀하고 희소한 인지적 특징을 처리하여 실시간으로 동적 궤적을 디코딩합니다.
- 4. 확산 모델은 궤적 오프셋 분포를 예측하여 앵커를 세밀하게 조정합니다.
- 5. NAVSIM 벤치마크 실험에서 AnchDrive는 새로운 최첨단 성능을 기록하고 강력한 일반화 능력을 보여줍니다.


---

*Generated on 2025-09-25 16:04:35*