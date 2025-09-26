---
keywords:
  - Multi-view Crowd Counting
  - Active View Selection
  - Cross-scene Generalization
  - Label Efficiency
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16684
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:31:47.423951",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-view Crowd Counting",
    "Active View Selection",
    "Cross-scene Generalization",
    "Label Efficiency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-view Crowd Counting": 0.8,
    "Active View Selection": 0.85,
    "Cross-scene Generalization": 0.78,
    "Label Efficiency": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "multi-view crowd counting",
        "canonical": "Multi-view Crowd Counting",
        "aliases": [
          "multi-view counting",
          "crowd counting"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific technique relevant to the paper's focus on crowd counting using multiple views, offering unique insights into scene analysis.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "active view selection",
        "canonical": "Active View Selection",
        "aliases": [
          "AVS"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's contribution, emphasizing the dynamic selection of views for improved results.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "cross-scene ability",
        "canonical": "Cross-scene Generalization",
        "aliases": [
          "cross-scene capability"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding the paper's approach to applying methods across different scenes, enhancing its applicability.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "limited label demand",
        "canonical": "Label Efficiency",
        "aliases": [
          "limited labeling",
          "label-efficient"
        ],
        "category": "specific_connectable",
        "rationale": "This highlights the paper's focus on reducing the need for extensive labeled data, which is a significant advantage in machine learning contexts.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "multi-view crowd counting",
      "resolved_canonical": "Multi-view Crowd Counting",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "active view selection",
      "resolved_canonical": "Active View Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "cross-scene ability",
      "resolved_canonical": "Cross-scene Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "limited label demand",
      "resolved_canonical": "Label Efficiency",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Active View Selection for Scene-level Multi-view Crowd Counting and Localization with Limited Labels

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16684.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16684](https://arxiv.org/abs/2509.16684)

## 🔗 유사한 논문
- [[2025-09-22/Camera Splatting for Continuous View Optimization_20250922|Camera Splatting for Continuous View Optimization]] (81.7% similar)
- [[2025-09-23/Audio-Guided Dynamic Modality Fusion with Stereo-Aware Attention for Audio-Visual Navigation_20250923|Audio-Guided Dynamic Modality Fusion with Stereo-Aware Attention for Audio-Visual Navigation]] (80.7% similar)
- [[2025-09-18/VSE-MOT_ Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement_20250918|VSE-MOT: Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (80.2% similar)
- [[2025-09-19/Multi-label Scene Classification for Autonomous Vehicles_ Acquiring and Accumulating Knowledge from Diverse Datasets_20250919|Multi-label Scene Classification for Autonomous Vehicles: Acquiring and Accumulating Knowledge from Diverse Datasets]] (80.1% similar)
- [[2025-09-23/Learning Fused State Representations for Control from Multi-View Observations_20250923|Learning Fused State Representations for Control from Multi-View Observations]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Cross-scene Generalization|Cross-scene Generalization]], [[keywords/Label Efficiency|Label Efficiency]]
**⚡ Unique Technical**: [[keywords/Multi-view Crowd Counting|Multi-view Crowd Counting]], [[keywords/Active View Selection|Active View Selection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16684v1 Announce Type: new 
Abstract: Multi-view crowd counting and localization fuse the input multi-views for estimating the crowd number or locations on the ground. Existing methods mainly focus on accurately predicting on the crowd shown in the input views, which neglects the problem of choosing the `best' camera views to perceive all crowds well in the scene. Besides, existing view selection methods require massive labeled views and images, and lack the ability for cross-scene settings, reducing their application scenarios. Thus, in this paper, we study the view selection issue for better scene-level multi-view crowd counting and localization results with cross-scene ability and limited label demand, instead of input-view-level results. We first propose an independent view selection method (IVS) that considers view and scene geometries in the view selection strategy and conducts the view selection, labeling, and downstream tasks independently. Based on IVS, we also put forward an active view selection method (AVS) that jointly optimizes the view selection, labeling, and downstream tasks. In AVS, we actively select the labeled views and consider both the view/scene geometries and the predictions of the downstream task models in the view selection process. Experiments on multi-view counting and localization tasks demonstrate the cross-scene and the limited label demand advantages of the proposed active view selection method (AVS), outperforming existing methods and with wider application scenarios.

## 📝 요약

이 논문은 다중 시점 군중 수 및 위치 추정에서 최적의 카메라 시점을 선택하는 문제를 다룹니다. 기존 방법들은 주로 입력된 시점에서의 정확한 예측에 집중하지만, 모든 군중을 잘 인식할 수 있는 '최적'의 시점을 선택하는 문제를 간과합니다. 이에 따라, 본 연구에서는 장면 수준에서의 다중 시점 군중 수 및 위치 추정 결과를 개선하기 위해 독립적 시점 선택 방법(IVS)과 능동적 시점 선택 방법(AVS)을 제안합니다. IVS는 시점 및 장면의 기하학적 특성을 고려하여 시점 선택, 라벨링, 후속 작업을 독립적으로 수행합니다. AVS는 시점 선택, 라벨링, 후속 작업을 공동 최적화하며, 시점/장면 기하학과 후속 작업 모델의 예측을 고려합니다. 실험 결과, AVS는 제한된 라벨 수요와 장면 간 적용 가능성에서 기존 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 본 연구는 장면 수준의 다중 시점 군중 수 계산 및 위치 추정에서 효과적인 시점 선택 문제를 다루며, 교차 장면 능력과 제한된 레이블 수요를 강조합니다.
- 2. 독립적 시점 선택 방법(IVS)은 시점 및 장면 기하학을 고려하여 시점 선택, 레이블링, 다운스트림 작업을 독립적으로 수행합니다.
- 3. 능동적 시점 선택 방법(AVS)은 시점 선택, 레이블링, 다운스트림 작업을 공동으로 최적화하며, 시점/장면 기하학과 다운스트림 작업 모델의 예측을 고려합니다.
- 4. 실험 결과, 제안된 능동적 시점 선택 방법(AVS)은 기존 방법보다 교차 장면 및 제한된 레이블 수요에서 우수한 성능을 보이며, 더 넓은 응용 시나리오를 제공합니다.


---

*Generated on 2025-09-24 04:31:47*