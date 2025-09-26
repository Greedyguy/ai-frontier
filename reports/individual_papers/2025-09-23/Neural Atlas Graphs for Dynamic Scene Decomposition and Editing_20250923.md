---
keywords:
  - Neural Atlas Graphs
  - Dynamic Scene Decomposition
  - High-Resolution Scene Representation
  - Autonomous Driving
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16336
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:06:37.348291",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Atlas Graphs",
    "Dynamic Scene Decomposition",
    "High-Resolution Scene Representation",
    "Autonomous Driving"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Atlas Graphs": 0.88,
    "Dynamic Scene Decomposition": 0.8,
    "High-Resolution Scene Representation": 0.78,
    "Autonomous Driving": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Atlas Graphs",
        "canonical": "Neural Atlas Graphs",
        "aliases": [
          "NAGs"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel hybrid representation for dynamic scene editing, enhancing connectivity with existing scene graph and neural atlas concepts.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Dynamic Scene Decomposition",
        "canonical": "Dynamic Scene Decomposition",
        "aliases": [
          "Scene Decomposition"
        ],
        "category": "specific_connectable",
        "rationale": "Facilitates connections with research on scene understanding and editing in computer vision.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "High-Resolution Scene Representation",
        "canonical": "High-Resolution Scene Representation",
        "aliases": [
          "Scene Representation"
        ],
        "category": "specific_connectable",
        "rationale": "Links to advancements in high-resolution modeling techniques in computer vision.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.77,
        "link_intent_score": 0.78
      },
      {
        "surface": "Autonomous Driving",
        "canonical": "Autonomous Driving",
        "aliases": [
          "Self-Driving Cars"
        ],
        "category": "broad_technical",
        "rationale": "Connects with a broad range of research in autonomous vehicle technology and scene understanding.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Atlas Graphs",
      "resolved_canonical": "Neural Atlas Graphs",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Dynamic Scene Decomposition",
      "resolved_canonical": "Dynamic Scene Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "High-Resolution Scene Representation",
      "resolved_canonical": "High-Resolution Scene Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.77,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Autonomous Driving",
      "resolved_canonical": "Autonomous Driving",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Neural Atlas Graphs for Dynamic Scene Decomposition and Editing

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16336.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16336](https://arxiv.org/abs/2509.16336)

## 🔗 유사한 논문
- [[2025-09-22/MoAngelo_ Motion-Aware Neural Surface Reconstruction for Dynamic Scenes_20250922|MoAngelo: Motion-Aware Neural Surface Reconstruction for Dynamic Scenes]] (84.2% similar)
- [[2025-09-19/SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN: Layout-guided 3D Indoor Scene Generation]] (81.9% similar)
- [[2025-09-23/Robust Anomaly Detection Under Normality Distribution Shift in Dynamic Graphs_20250923|Robust Anomaly Detection Under Normality Distribution Shift in Dynamic Graphs]] (80.8% similar)
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods: Reviving Transformer for Graph Clustering]] (80.7% similar)
- [[2025-09-19/FMGS-Avatar_ Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction_20250919|FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Autonomous Driving|Autonomous Driving]]
**🔗 Specific Connectable**: [[keywords/Dynamic Scene Decomposition|Dynamic Scene Decomposition]], [[keywords/High-Resolution Scene Representation|High-Resolution Scene Representation]]
**⚡ Unique Technical**: [[keywords/Neural Atlas Graphs|Neural Atlas Graphs]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16336v1 Announce Type: cross 
Abstract: Learning editable high-resolution scene representations for dynamic scenes is an open problem with applications across the domains from autonomous driving to creative editing - the most successful approaches today make a trade-off between editability and supporting scene complexity: neural atlases represent dynamic scenes as two deforming image layers, foreground and background, which are editable in 2D, but break down when multiple objects occlude and interact. In contrast, scene graph models make use of annotated data such as masks and bounding boxes from autonomous-driving datasets to capture complex 3D spatial relationships, but their implicit volumetric node representations are challenging to edit view-consistently. We propose Neural Atlas Graphs (NAGs), a hybrid high-resolution scene representation, where every graph node is a view-dependent neural atlas, facilitating both 2D appearance editing and 3D ordering and positioning of scene elements. Fit at test-time, NAGs achieve state-of-the-art quantitative results on the Waymo Open Dataset - by 5 dB PSNR increase compared to existing methods - and make environmental editing possible in high resolution and visual quality - creating counterfactual driving scenarios with new backgrounds and edited vehicle appearance. We find that the method also generalizes beyond driving scenes and compares favorably - by more than 7 dB in PSNR - to recent matting and video editing baselines on the DAVIS video dataset with a diverse set of human and animal-centric scenes.

## 📝 요약

이 논문에서는 동적 장면의 고해상도 장면 표현을 학습하는 문제를 다룹니다. 기존 방법들은 편집 가능성과 장면 복잡성 간의 절충이 필요했으나, 저자는 Neural Atlas Graphs(NAGs)라는 하이브리드 고해상도 장면 표현 방식을 제안합니다. NAGs는 각 그래프 노드가 시점 의존적인 신경 아틀라스로 구성되어 2D 외관 편집과 3D 장면 요소의 정렬 및 위치 조정이 가능합니다. 이 방법은 Waymo Open Dataset에서 기존 방법 대비 5 dB 높은 PSNR을 기록하며, 고해상도 환경 편집을 가능하게 합니다. 또한, DAVIS 비디오 데이터셋에서도 최근의 매팅 및 비디오 편집 기법보다 7 dB 이상 높은 PSNR을 기록하며, 운전 장면 외의 다양한 장면에서도 우수한 성능을 보입니다.

## 🎯 주요 포인트

- 1. Neural Atlas Graphs (NAGs)는 동적 장면의 고해상도 표현을 위한 하이브리드 모델로, 2D 외관 편집과 3D 장면 요소의 정렬 및 위치 조정을 용이하게 한다.
- 2. NAGs는 Waymo Open Dataset에서 기존 방법들에 비해 5 dB PSNR 증가를 달성하며, 고해상도 및 시각적 품질로 환경 편집을 가능하게 한다.
- 3. 이 방법은 운전 장면을 넘어 일반화되며, DAVIS 비디오 데이터셋에서 최근 매팅 및 비디오 편집 기준선보다 7 dB 이상 PSNR에서 우수한 성능을 보인다.
- 4. Neural atlases는 2D에서 편집 가능한 두 개의 변형 이미지 레이어로 동적 장면을 표현하지만, 여러 객체가 가려지거나 상호작용할 때 한계를 가진다.
- 5. 장면 그래프 모델은 자율 주행 데이터셋의 마스크 및 바운딩 박스와 같은 주석 데이터를 활용하여 복잡한 3D 공간 관계를 포착하지만, 암시적 부피 노드 표현은 일관된 보기 편집이 어렵다.


---

*Generated on 2025-09-24 02:06:37*