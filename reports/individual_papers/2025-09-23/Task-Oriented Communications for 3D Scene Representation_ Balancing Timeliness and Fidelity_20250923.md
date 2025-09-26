---
keywords:
  - 3D Scene Representation
  - Proximal Policy Optimization
  - Age of Information
  - Virtual Reality
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17282
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:48:27.915006",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Scene Representation",
    "Proximal Policy Optimization",
    "Age of Information",
    "Virtual Reality"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Scene Representation": 0.8,
    "Proximal Policy Optimization": 0.78,
    "Age of Information": 0.7,
    "Virtual Reality": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Scene Representation",
        "canonical": "3D Scene Representation",
        "aliases": [
          "Three-dimensional Scene Representation"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper, linking to advancements in digital environments and visualization.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Proximal Policy Optimization",
        "canonical": "Proximal Policy Optimization",
        "aliases": [
          "PPO"
        ],
        "category": "specific_connectable",
        "rationale": "A key algorithm used in the paper, relevant to reinforcement learning and decision-making processes.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Age of Information",
        "canonical": "Age of Information",
        "aliases": [
          "AoI"
        ],
        "category": "unique_technical",
        "rationale": "Important for understanding the timeliness aspect in communication systems.",
        "novelty_score": 0.6,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Virtual, Augmented, and Mixed Reality",
        "canonical": "Virtual Reality",
        "aliases": [
          "VR",
          "AR",
          "MR"
        ],
        "category": "broad_technical",
        "rationale": "These technologies are directly impacted by advancements in 3D scene representation.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "timeliness",
      "fidelity",
      "wireless network",
      "edge server"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Scene Representation",
      "resolved_canonical": "3D Scene Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Proximal Policy Optimization",
      "resolved_canonical": "Proximal Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Age of Information",
      "resolved_canonical": "Age of Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Virtual, Augmented, and Mixed Reality",
      "resolved_canonical": "Virtual Reality",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Task-Oriented Communications for 3D Scene Representation: Balancing Timeliness and Fidelity

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17282.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17282](https://arxiv.org/abs/2509.17282)

## 🔗 유사한 논문
- [[2025-09-22/Recovering Parametric Scenes from Very Few Time-of-Flight Pixels_20250922|Recovering Parametric Scenes from Very Few Time-of-Flight Pixels]] (82.7% similar)
- [[2025-09-23/Search-Optimized Quantization in Biomedical Ontology Alignment_20250923|Search-Optimized Quantization in Biomedical Ontology Alignment]] (81.5% similar)
- [[2025-09-23/Octree Latent Diffusion for Semantic 3D Scene Generation and Completion_20250923|Octree Latent Diffusion for Semantic 3D Scene Generation and Completion]] (81.5% similar)
- [[2025-09-23/No Need for Real 3D_ Fusing 2D Vision with Pseudo 3D Representations for Robotic Manipulation Learning_20250923|No Need for Real 3D: Fusing 2D Vision with Pseudo 3D Representations for Robotic Manipulation Learning]] (81.3% similar)
- [[2025-09-22/DAOcc_ 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction_20250922|DAOcc: 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Virtual Reality|Virtual Reality]]
**🔗 Specific Connectable**: [[keywords/Proximal Policy Optimization|Proximal Policy Optimization]]
**⚡ Unique Technical**: [[keywords/3D Scene Representation|3D Scene Representation]], [[keywords/Age of Information|Age of Information]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17282v1 Announce Type: new 
Abstract: Real-time Three-dimensional (3D) scene representation is a foundational element that supports a broad spectrum of cutting-edge applications, including digital manufacturing, Virtual, Augmented, and Mixed Reality (VR/AR/MR), and the emerging metaverse. Despite advancements in real-time communication and computing, achieving a balance between timeliness and fidelity in 3D scene representation remains a challenge. This work investigates a wireless network where multiple homogeneous mobile robots, equipped with cameras, capture an environment and transmit images to an edge server over channels for 3D representation. We propose a contextual-bandit Proximal Policy Optimization (PPO) framework incorporating both Age of Information (AoI) and semantic information to optimize image selection for representation, balancing data freshness and representation quality. Two policies -- the $\omega$-threshold and $\omega$-wait policies -- together with two benchmark methods are evaluated, timeliness embedding and weighted sum, on standard datasets and baseline 3D scene representation models. Experimental results demonstrate improved representation fidelity while maintaining low latency, offering insight into the model's decision-making process. This work advances real-time 3D scene representation by optimizing the trade-off between timeliness and fidelity in dynamic environments.

## 📝 요약

이 논문은 실시간 3D 장면 표현에서 시의성과 정확성 간의 균형을 맞추는 문제를 다룹니다. 여러 대의 동질적 모바일 로봇이 카메라로 환경을 촬영하고 이미지를 엣지 서버로 전송하여 3D 표현을 구현하는 무선 네트워크를 연구합니다. 제안된 방법론은 정보의 신선도(AoI)와 의미 정보를 고려한 문맥적 밴딧 근접 정책 최적화(PPO) 프레임워크로, 데이터 신선도와 표현 품질을 최적화합니다. $\omega$-threshold 및 $\omega$-wait 정책과 두 가지 벤치마크 방법이 표준 데이터셋과 3D 장면 표현 모델에서 평가되었습니다. 실험 결과는 낮은 지연 시간과 향상된 표현 정확성을 보여주며, 모델의 의사결정 과정을 이해하는 데 기여합니다. 이 연구는 동적 환경에서 실시간 3D 장면 표현의 시의성과 정확성 간의 균형을 최적화하는 데 기여합니다.

## 🎯 주요 포인트

- 1. 실시간 3D 장면 표현은 디지털 제조, VR/AR/MR, 메타버스 등 다양한 첨단 응용 분야를 지원하는 핵심 요소입니다.
- 2. 본 연구는 여러 대의 이동 로봇이 카메라로 환경을 촬영하고 이미지를 엣지 서버로 전송하여 3D 표현을 구현하는 무선 네트워크를 조사합니다.
- 3. 정보의 신선도와 표현 품질을 균형 있게 최적화하기 위해 Age of Information(AoI)와 의미 정보를 통합한 컨텍스추얼-밴딧 PPO 프레임워크를 제안합니다.
- 4. $\omega$-threshold 및 $\omega$-wait 정책과 두 가지 벤치마크 방법을 통해 데이터셋과 3D 장면 표현 모델에서 평가한 결과, 낮은 지연 시간을 유지하면서 표현 충실도가 향상되었습니다.
- 5. 본 연구는 동적 환경에서 적시성과 충실도 간의 균형을 최적화하여 실시간 3D 장면 표현을 발전시킵니다.


---

*Generated on 2025-09-24 04:48:27*