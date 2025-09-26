---
keywords:
  - Multimodal Learning
  - Bisimulation Metric Learning
  - Multi-view Fusion State for Control
  - Latent Reconstruction
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2502.01316
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:44:25.980321",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Bisimulation Metric Learning",
    "Multi-view Fusion State for Control",
    "Latent Reconstruction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.8,
    "Bisimulation Metric Learning": 0.78,
    "Multi-view Fusion State for Control": 0.82,
    "Latent Reconstruction": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-View Reinforcement Learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MVRL"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the concept of using multiple data modalities, which is central to the paper's approach.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Bisimulation Metric Learning",
        "canonical": "Bisimulation Metric Learning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach for learning task-relevant representations in the context of control tasks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multi-view Fusion State for Control",
        "canonical": "Multi-view Fusion State for Control",
        "aliases": [
          "MFSC"
        ],
        "category": "unique_technical",
        "rationale": "Represents a unique method proposed in the paper, crucial for understanding the specific contributions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Latent Reconstruction Auxiliary Task",
        "canonical": "Latent Reconstruction",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Highlights an auxiliary task that enhances the robustness of the proposed method.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "task"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-View Reinforcement Learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Bisimulation Metric Learning",
      "resolved_canonical": "Bisimulation Metric Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multi-view Fusion State for Control",
      "resolved_canonical": "Multi-view Fusion State for Control",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Latent Reconstruction Auxiliary Task",
      "resolved_canonical": "Latent Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Learning Fused State Representations for Control from Multi-View Observations

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.01316.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2502.01316](https://arxiv.org/abs/2502.01316)

## 🔗 유사한 논문
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (84.2% similar)
- [[2025-09-22/Generalized Deep Multi-view Clustering via Causal Learning with Partially Aligned Cross-view Correspondence_20250922|Generalized Deep Multi-view Clustering via Causal Learning with Partially Aligned Cross-view Correspondence]] (83.8% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (82.7% similar)
- [[2025-09-23/MVCL-DAF++_ Enhancing Multimodal Intent Recognition via Prototype-Aware Contrastive Alignment and Coarse-to-Fine Dynamic Attention Fusion_20250923|MVCL-DAF++: Enhancing Multimodal Intent Recognition via Prototype-Aware Contrastive Alignment and Coarse-to-Fine Dynamic Attention Fusion]] (82.5% similar)
- [[2025-09-23/From Easy to Hard_ The MIR Benchmark for Progressive Interleaved Multi-Image Reasoning_20250923|From Easy to Hard: The MIR Benchmark for Progressive Interleaved Multi-Image Reasoning]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Latent Reconstruction|Latent Reconstruction]]
**⚡ Unique Technical**: [[keywords/Bisimulation Metric Learning|Bisimulation Metric Learning]], [[keywords/Multi-view Fusion State for Control|Multi-view Fusion State for Control]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.01316v4 Announce Type: replace-cross 
Abstract: Multi-View Reinforcement Learning (MVRL) seeks to provide agents with multi-view observations, enabling them to perceive environment with greater effectiveness and precision. Recent advancements in MVRL focus on extracting latent representations from multiview observations and leveraging them in control tasks. However, it is not straightforward to learn compact and task-relevant representations, particularly in the presence of redundancy, distracting information, or missing views. In this paper, we propose Multi-view Fusion State for Control (MFSC), firstly incorporating bisimulation metric learning into MVRL to learn task-relevant representations. Furthermore, we propose a multiview-based mask and latent reconstruction auxiliary task that exploits shared information across views and improves MFSC's robustness in missing views by introducing a mask token. Extensive experimental results demonstrate that our method outperforms existing approaches in MVRL tasks. Even in more realistic scenarios with interference or missing views, MFSC consistently maintains high performance.

## 📝 요약

이 논문은 다중 관찰을 통해 환경을 더 효과적이고 정확하게 인식할 수 있는 다중 관점 강화 학습(MVRL)을 다룹니다. 저자들은 MVRL에서 과제 관련 표현을 학습하기 위해 비시뮬레이션 메트릭 학습을 처음으로 도입한 Multi-view Fusion State for Control (MFSC)을 제안합니다. 또한, 다중 관점 기반 마스크와 잠재 재구성 보조 과제를 통해 관점 간 공유 정보를 활용하고, 마스크 토큰을 도입하여 누락된 관점에서도 강건성을 향상시킵니다. 실험 결과, MFSC는 기존 방법들보다 우수한 성능을 보였으며, 간섭이나 누락된 관점이 있는 현실적인 시나리오에서도 일관되게 높은 성능을 유지했습니다.

## 🎯 주요 포인트

- 1. 다중 관찰을 통해 환경을 더 효과적이고 정밀하게 인식할 수 있는 다중 뷰 강화 학습(MVRL)의 발전이 이루어지고 있다.
- 2. 본 논문에서는 MVRL에 비시뮬레이션 메트릭 학습을 처음으로 도입하여, 과제 관련 표현을 학습하는 Multi-view Fusion State for Control (MFSC)를 제안한다.
- 3. 다중 뷰 기반 마스크와 잠재 재구성 보조 과제를 통해 뷰 간의 공유 정보를 활용하고, 마스크 토큰을 도입하여 누락된 뷰에서도 MFSC의 강건성을 향상시킨다.
- 4. 실험 결과, 제안된 방법이 기존의 MVRL 접근법보다 우수한 성능을 보이며, 간섭이나 누락된 뷰가 있는 현실적인 시나리오에서도 높은 성능을 유지한다.


---

*Generated on 2025-09-24 00:44:25*