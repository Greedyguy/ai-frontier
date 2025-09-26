---
keywords:
  - Pose Estimation
  - Energy-based Model
  - Sim-to-real Transfer
  - Render-compare Architecture
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15934
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:38:50.072286",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Pose Estimation",
    "Energy-based Model",
    "Sim-to-real Transfer",
    "Render-compare Architecture"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Pose Estimation": 0.82,
    "Energy-based Model": 0.75,
    "Sim-to-real Transfer": 0.77,
    "Render-compare Architecture": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "In-hand Pose Estimation",
        "canonical": "Pose Estimation",
        "aliases": [
          "Object Pose Estimation"
        ],
        "category": "specific_connectable",
        "rationale": "Pose estimation is a crucial task in robotics and computer vision, facilitating connections to related techniques and applications.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Energy-based Diffusion Model",
        "canonical": "Energy-based Model",
        "aliases": [
          "Diffusion Model"
        ],
        "category": "unique_technical",
        "rationale": "This model type is central to the paper's methodology, offering a unique approach to pose estimation.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Sim-to-real Performance",
        "canonical": "Sim-to-real Transfer",
        "aliases": [
          "Simulation to Real World"
        ],
        "category": "specific_connectable",
        "rationale": "Sim-to-real transfer is a key challenge in robotics, linking to broader discussions on model generalization.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Render-compare Architecture",
        "canonical": "Render-compare Architecture",
        "aliases": [
          "Render and Compare"
        ],
        "category": "unique_technical",
        "rationale": "This architecture is a novel contribution that enhances model performance, relevant for linking to visualization techniques.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.79,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "Regression",
      "Matching",
      "Registration Techniques"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "In-hand Pose Estimation",
      "resolved_canonical": "Pose Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Energy-based Diffusion Model",
      "resolved_canonical": "Energy-based Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Sim-to-real Performance",
      "resolved_canonical": "Sim-to-real Transfer",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Render-compare Architecture",
      "resolved_canonical": "Render-compare Architecture",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.79,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# UniTac2Pose: A Unified Approach Learned in Simulation for Category-level Visuotactile In-hand Pose Estimation

**Korean Title:** UniTac2Pose: 범주 수준의 시각촉각 인핸드 자세 추정을 위한 시뮬레이션에서 학습된 통합 접근법

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15934.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15934](https://arxiv.org/abs/2509.15934)

## 🔗 유사한 논문
- [[2025-09-22/GenCAD-3D_ CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing_20250922|GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing]] (81.4% similar)
- [[2025-09-22/cadrille_ Multi-modal CAD Reconstruction with Online Reinforcement Learning_20250922|cadrille: Multi-modal CAD Reconstruction with Online Reinforcement Learning]] (81.1% similar)
- [[2025-09-22/Recovering Parametric Scenes from Very Few Time-of-Flight Pixels_20250922|Recovering Parametric Scenes from Very Few Time-of-Flight Pixels]] (81.0% similar)
- [[2025-09-22/A re-calibration method for object detection with multi-modal alignment bias in autonomous driving_20250922|A re-calibration method for object detection with multi-modal alignment bias in autonomous driving]] (80.9% similar)
- [[2025-09-22/PAN_ Pillars-Attention-Based Network for 3D Object Detection_20250922|PAN: Pillars-Attention-Based Network for 3D Object Detection]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Pose Estimation|Pose Estimation]], [[keywords/Sim-to-real Transfer|Sim-to-real Transfer]]
**⚡ Unique Technical**: [[keywords/Energy-based Model|Energy-based Model]], [[keywords/Render-compare Architecture|Render-compare Architecture]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15934v1 Announce Type: new 
Abstract: Accurate estimation of the in-hand pose of an object based on its CAD model is crucial in both industrial applications and everyday tasks, ranging from positioning workpieces and assembling components to seamlessly inserting devices like USB connectors. While existing methods often rely on regression, feature matching, or registration techniques, achieving high precision and generalizability to unseen CAD models remains a significant challenge. In this paper, we propose a novel three-stage framework for in-hand pose estimation. The first stage involves sampling and pre-ranking pose candidates, followed by iterative refinement of these candidates in the second stage. In the final stage, post-ranking is applied to identify the most likely pose candidates. These stages are governed by a unified energy-based diffusion model, which is trained solely on simulated data. This energy model simultaneously generates gradients to refine pose estimates and produces an energy scalar that quantifies the quality of the pose estimates. Additionally, borrowing the idea from the computer vision domain, we incorporate a render-compare architecture within the energy-based score network to significantly enhance sim-to-real performance, as demonstrated by our ablation studies. We conduct comprehensive experiments to show that our method outperforms conventional baselines based on regression, matching, and registration techniques, while also exhibiting strong intra-category generalization to previously unseen CAD models. Moreover, our approach integrates tactile object pose estimation, pose tracking, and uncertainty estimation into a unified framework, enabling robust performance across a variety of real-world conditions.

## 🔍 Abstract (한글 번역)

arXiv:2509.15934v1 발표 유형: 신규  
초록: CAD 모델을 기반으로 한 물체의 손안에서의 자세를 정확하게 추정하는 것은 산업 응용과 일상적인 작업에서 매우 중요합니다. 이는 작업물의 위치를 정하고, 부품을 조립하며, USB 커넥터와 같은 장치를 매끄럽게 삽입하는 것에 이르기까지 다양합니다. 기존 방법들은 주로 회귀, 특징 매칭, 또는 정합 기법에 의존하지만, 높은 정밀도와 보지 못한 CAD 모델에 대한 일반화를 달성하는 것은 여전히 큰 도전 과제입니다. 본 논문에서는 손안에서의 자세 추정을 위한 새로운 3단계 프레임워크를 제안합니다. 첫 번째 단계에서는 자세 후보를 샘플링하고 사전 순위를 매기며, 두 번째 단계에서는 이러한 후보를 반복적으로 정제합니다. 마지막 단계에서는 사후 순위를 적용하여 가장 가능성 있는 자세 후보를 식별합니다. 이러한 단계들은 통합된 에너지 기반 확산 모델에 의해 관리되며, 이 모델은 오로지 시뮬레이션 데이터로만 훈련됩니다. 이 에너지 모델은 자세 추정을 정제하기 위한 그래디언트를 생성하는 동시에 자세 추정의 품질을 정량화하는 에너지 스칼라를 생성합니다. 또한, 컴퓨터 비전 분야의 아이디어를 차용하여 에너지 기반 점수 네트워크 내에 렌더-비교 아키텍처를 통합하여, 우리의 절단 연구에서 입증된 바와 같이 시뮬레이션에서 실제로의 성능을 크게 향상시킵니다. 우리는 포괄적인 실험을 통해 우리의 방법이 회귀, 매칭, 정합 기법에 기반한 기존의 기준선을 능가하며, 이전에 보지 못한 CAD 모델에 대한 강력한 범주 내 일반화를 보여줍니다. 더욱이, 우리의 접근법은 촉각 물체 자세 추정, 자세 추적, 불확실성 추정을 통합된 프레임워크로 통합하여 다양한 실제 조건에서 강력한 성능을 가능하게 합니다.

## 📝 요약

이 논문은 CAD 모델을 기반으로 한 물체의 손 안에서의 자세를 정확히 추정하는 새로운 3단계 프레임워크를 제안합니다. 첫 번째 단계에서는 자세 후보를 샘플링하고 사전 순위를 매기며, 두 번째 단계에서는 후보를 반복적으로 정제합니다. 마지막 단계에서는 후보의 사후 순위를 매겨 가장 가능성이 높은 자세를 식별합니다. 이 과정은 시뮬레이션 데이터로만 훈련된 통합 에너지 기반 확산 모델에 의해 조정됩니다. 이 모델은 자세 추정을 정제하는 그래디언트를 생성하고, 자세 추정의 품질을 정량화하는 에너지 스칼라를 제공합니다. 또한, 컴퓨터 비전 분야의 렌더-비교 아키텍처를 도입하여 시뮬레이션에서 실제로의 성능을 향상시켰습니다. 실험 결과, 제안된 방법은 기존의 회귀, 매칭, 등록 기법을 기반으로 한 방법보다 우수한 성능을 보였으며, 새로운 CAD 모델에 대한 강력한 일반화 능력을 나타냈습니다. 추가적으로, 촉각 기반의 물체 자세 추정, 자세 추적, 불확실성 추정을 통합하여 다양한 실제 조건에서 강력한 성능을 발휘합니다.

## 🎯 주요 포인트

- 1. CAD 모델 기반의 물체의 인핸드 자세 추정은 산업 및 일상 작업에서 중요한 역할을 한다.
- 2. 본 논문은 인핸드 자세 추정을 위한 새로운 3단계 프레임워크를 제안한다.
- 3. 제안된 프레임워크는 에너지 기반 확산 모델을 사용하여 자세 후보를 샘플링, 정제, 후순위화한다.
- 4. 렌더-비교 아키텍처를 통합하여 시뮬레이션에서 실제 환경으로의 성능을 향상시켰다.
- 5. 제안된 방법은 기존의 회귀, 매칭, 등록 기법을 능가하며, 새로운 CAD 모델에 대한 일반화 능력을 보인다.


---

*Generated on 2025-09-23 10:38:50*