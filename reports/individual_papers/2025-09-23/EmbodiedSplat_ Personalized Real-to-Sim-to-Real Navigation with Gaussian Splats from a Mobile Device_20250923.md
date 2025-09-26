---
keywords:
  - Embodied AI
  - Sim-to-Real Transfer
  - 3D Gaussian Splatting
  - Habitat-Sim
  - Image Navigation Task
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17430
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:51:03.383708",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Embodied AI",
    "Sim-to-Real Transfer",
    "3D Gaussian Splatting",
    "Habitat-Sim",
    "Image Navigation Task"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Embodied AI": 0.78,
    "Sim-to-Real Transfer": 0.82,
    "3D Gaussian Splatting": 0.79,
    "Habitat-Sim": 0.81,
    "Image Navigation Task": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Embodied AI",
        "canonical": "Embodied AI",
        "aliases": [
          "Embodied Artificial Intelligence"
        ],
        "category": "unique_technical",
        "rationale": "Embodied AI is a distinct field focusing on the integration of AI with physical environments, which is central to the paper's theme.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sim-to-Real Transfer",
        "canonical": "Sim-to-Real Transfer",
        "aliases": [
          "Simulation to Real Transfer"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding the challenges and solutions proposed in the paper for transferring learned policies from simulated to real environments.",
        "novelty_score": 0.68,
        "connectivity_score": 0.85,
        "specificity_score": 0.77,
        "link_intent_score": 0.82
      },
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [
          "3D GS"
        ],
        "category": "unique_technical",
        "rationale": "A novel technique introduced in the paper for mesh reconstruction, which is pivotal for the proposed navigation system.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "Habitat-Sim",
        "canonical": "Habitat-Sim",
        "aliases": [
          "Habitat Simulator"
        ],
        "category": "specific_connectable",
        "rationale": "A widely used simulator in Embodied AI research, crucial for the implementation and evaluation of the proposed method.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.81
      },
      {
        "surface": "Image Navigation Task",
        "canonical": "Image Navigation Task",
        "aliases": [
          "Visual Navigation Task"
        ],
        "category": "specific_connectable",
        "rationale": "A specific task used to evaluate the effectiveness of the proposed navigation method, linking to broader research in visual navigation.",
        "novelty_score": 0.65,
        "connectivity_score": 0.83,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "training strategies"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Embodied AI",
      "resolved_canonical": "Embodied AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sim-to-Real Transfer",
      "resolved_canonical": "Sim-to-Real Transfer",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.85,
        "specificity": 0.77,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Habitat-Sim",
      "resolved_canonical": "Habitat-Sim",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Image Navigation Task",
      "resolved_canonical": "Image Navigation Task",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.83,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# EmbodiedSplat: Personalized Real-to-Sim-to-Real Navigation with Gaussian Splats from a Mobile Device

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17430.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17430](https://arxiv.org/abs/2509.17430)

## 🔗 유사한 논문
- [[2025-09-23/Efficient 3D Scene Reconstruction and Simulation from Sparse Endoscopic Views_20250923|Efficient 3D Scene Reconstruction and Simulation from Sparse Endoscopic Views]] (83.1% similar)
- [[2025-09-23/End-to-end RL Improves Dexterous Grasping Policies_20250923|End-to-end RL Improves Dexterous Grasping Policies]] (82.3% similar)
- [[2025-09-19/M4Diffuser_ Multi-View Diffusion Policy with Manipulability-Aware Control for Robust Mobile Manipulation_20250919|M4Diffuser: Multi-View Diffusion Policy with Manipulability-Aware Control for Robust Mobile Manipulation]] (82.0% similar)
- [[2025-09-23/ConfidentSplat_ Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM_20250923|ConfidentSplat: Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM]] (81.8% similar)
- [[2025-09-23/Latent Policy Steering with Embodiment-Agnostic Pretrained World Models_20250923|Latent Policy Steering with Embodiment-Agnostic Pretrained World Models]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Sim-to-Real Transfer|Sim-to-Real Transfer]], [[keywords/Habitat-Sim|Habitat-Sim]], [[keywords/Image Navigation Task|Image Navigation Task]]
**⚡ Unique Technical**: [[keywords/Embodied AI|Embodied AI]], [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17430v1 Announce Type: new 
Abstract: The field of Embodied AI predominantly relies on simulation for training and evaluation, often using either fully synthetic environments that lack photorealism or high-fidelity real-world reconstructions captured with expensive hardware. As a result, sim-to-real transfer remains a major challenge. In this paper, we introduce EmbodiedSplat, a novel approach that personalizes policy training by efficiently capturing the deployment environment and fine-tuning policies within the reconstructed scenes. Our method leverages 3D Gaussian Splatting (GS) and the Habitat-Sim simulator to bridge the gap between realistic scene capture and effective training environments. Using iPhone-captured deployment scenes, we reconstruct meshes via GS, enabling training in settings that closely approximate real-world conditions. We conduct a comprehensive analysis of training strategies, pre-training datasets, and mesh reconstruction techniques, evaluating their impact on sim-to-real predictivity in real-world scenarios. Experimental results demonstrate that agents fine-tuned with EmbodiedSplat outperform both zero-shot baselines pre-trained on large-scale real-world datasets (HM3D) and synthetically generated datasets (HSSD), achieving absolute success rate improvements of 20\% and 40\% on real-world Image Navigation task. Moreover, our approach yields a high sim-vs-real correlation (0.87--0.97) for the reconstructed meshes, underscoring its effectiveness in adapting policies to diverse environments with minimal effort. Project page: https://gchhablani.github.io/embodied-splat

## 📝 요약

Embodied AI 분야에서는 주로 시뮬레이션을 통해 훈련 및 평가를 진행하지만, 현실감이 부족한 완전 합성 환경이나 고가의 장비로 촬영한 고품질 현실 재구성 환경을 사용합니다. 이러한 문제를 해결하기 위해, 본 논문에서는 EmbodiedSplat이라는 새로운 접근법을 제안합니다. 이 방법은 3D Gaussian Splatting(GS)과 Habitat-Sim 시뮬레이터를 활용하여 실환경을 효율적으로 캡처하고, 재구성된 장면 내에서 정책을 미세 조정합니다. iPhone으로 캡처한 장면을 통해 메쉬를 재구성하여 현실에 가까운 환경에서 훈련을 진행합니다. 실험 결과, EmbodiedSplat으로 미세 조정된 에이전트는 대규모 실세계 데이터셋(HM3D)과 합성 데이터셋(HSSD)에서 사전 훈련된 에이전트보다 실제 이미지 내비게이션 작업에서 각각 20%와 40%의 성공률 향상을 보였습니다. 또한, 재구성된 메쉬에 대한 높은 시뮬레이션-현실 상관관계(0.87-0.97)를 보여 다양한 환경에 적응하는 데 효과적임을 입증했습니다.

## 🎯 주요 포인트

- 1. EmbodiedSplat은 3D Gaussian Splatting과 Habitat-Sim 시뮬레이터를 활용하여 현실적인 장면 캡처와 효과적인 훈련 환경 간의 격차를 줄입니다.
- 2. iPhone으로 캡처한 배포 환경을 기반으로 메쉬를 재구성하여 실제 환경과 유사한 조건에서 훈련을 진행할 수 있습니다.
- 3. EmbodiedSplat으로 미세 조정된 에이전트는 대규모 실제 데이터셋(HM3D)과 합성 데이터셋(HSSD)으로 사전 훈련된 제로샷 기준을 능가하며, 실제 이미지 네비게이션 작업에서 20% 및 40%의 성공률 향상을 달성했습니다.
- 4. 재구성된 메쉬에 대한 높은 시뮬레이션 대 실제 상관관계(0.87-0.97)를 보여주며, 다양한 환경에 정책을 적응시키는 데 효과적입니다.


---

*Generated on 2025-09-24 04:51:03*