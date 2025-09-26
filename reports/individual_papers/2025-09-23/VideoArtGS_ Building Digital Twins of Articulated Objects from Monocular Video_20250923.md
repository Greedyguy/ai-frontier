---
keywords:
  - Digital Twin
  - Articulated Object
  - Monocular Video
  - Motion Prior
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17647
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:04:32.852191",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Digital Twin",
    "Articulated Object",
    "Monocular Video",
    "Motion Prior"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Digital Twin": 0.8,
    "Articulated Object": 0.78,
    "Monocular Video": 0.75,
    "Motion Prior": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "digital twins",
        "canonical": "Digital Twin",
        "aliases": [
          "virtual twin",
          "digital replica"
        ],
        "category": "specific_connectable",
        "rationale": "Digital twins are increasingly relevant in computer vision for modeling and simulation, providing strong linkage opportunities.",
        "novelty_score": 0.65,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "articulated objects",
        "canonical": "Articulated Object",
        "aliases": [
          "jointed object",
          "linked object"
        ],
        "category": "unique_technical",
        "rationale": "Articulated objects are a specialized focus within computer vision, offering unique insights into object dynamics.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "monocular video",
        "canonical": "Monocular Video",
        "aliases": [
          "single-camera video",
          "single-view video"
        ],
        "category": "unique_technical",
        "rationale": "Monocular video is a distinct input format in vision tasks, crucial for understanding single-camera dynamics.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "motion prior",
        "canonical": "Motion Prior",
        "aliases": [
          "movement prior",
          "dynamic prior"
        ],
        "category": "specific_connectable",
        "rationale": "Motion priors are essential for improving model predictions in dynamic environments, linking to broader motion analysis.",
        "novelty_score": 0.6,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "reconstruction error"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "digital twins",
      "resolved_canonical": "Digital Twin",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "articulated objects",
      "resolved_canonical": "Articulated Object",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "monocular video",
      "resolved_canonical": "Monocular Video",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "motion prior",
      "resolved_canonical": "Motion Prior",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# VideoArtGS: Building Digital Twins of Articulated Objects from Monocular Video

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17647.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17647](https://arxiv.org/abs/2509.17647)

## 🔗 유사한 논문
- [[2025-09-19/FMGS-Avatar_ Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction_20250919|FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (84.5% similar)
- [[2025-09-22/MoAngelo_ Motion-Aware Neural Surface Reconstruction for Dynamic Scenes_20250922|MoAngelo: Motion-Aware Neural Surface Reconstruction for Dynamic Scenes]] (83.4% similar)
- [[2025-09-19/WorldForge_ Unlocking Emergent 3D/4D Generation in Video Diffusion Model via Training-Free Guidance_20250919|WorldForge: Unlocking Emergent 3D/4D Generation in Video Diffusion Model via Training-Free Guidance]] (82.4% similar)
- [[2025-09-22/Recovering Parametric Scenes from Very Few Time-of-Flight Pixels_20250922|Recovering Parametric Scenes from Very Few Time-of-Flight Pixels]] (81.3% similar)
- [[2025-09-18/\textsc{Gen2Real}_ Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Digital Twin|Digital Twin]], [[keywords/Motion Prior|Motion Prior]]
**⚡ Unique Technical**: [[keywords/Articulated Object|Articulated Object]], [[keywords/Monocular Video|Monocular Video]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17647v1 Announce Type: cross 
Abstract: Building digital twins of articulated objects from monocular video presents an essential challenge in computer vision, which requires simultaneous reconstruction of object geometry, part segmentation, and articulation parameters from limited viewpoint inputs. Monocular video offers an attractive input format due to its simplicity and scalability; however, it's challenging to disentangle the object geometry and part dynamics with visual supervision alone, as the joint movement of the camera and parts leads to ill-posed estimation. While motion priors from pre-trained tracking models can alleviate the issue, how to effectively integrate them for articulation learning remains largely unexplored. To address this problem, we introduce VideoArtGS, a novel approach that reconstructs high-fidelity digital twins of articulated objects from monocular video. We propose a motion prior guidance pipeline that analyzes 3D tracks, filters noise, and provides reliable initialization of articulation parameters. We also design a hybrid center-grid part assignment module for articulation-based deformation fields that captures accurate part motion. VideoArtGS demonstrates state-of-the-art performance in articulation and mesh reconstruction, reducing the reconstruction error by about two orders of magnitude compared to existing methods. VideoArtGS enables practical digital twin creation from monocular video, establishing a new benchmark for video-based articulated object reconstruction. Our work is made publicly available at: https://videoartgs.github.io.

## 📝 요약

이 논문은 단안 비디오에서 관절 객체의 디지털 트윈을 구축하는 새로운 방법론인 VideoArtGS를 제안합니다. 이 방법은 객체의 기하학, 부품 분할, 관절 매개변수를 동시에 재구성하는 과제를 해결합니다. 단안 비디오는 간단하고 확장성이 있지만, 시각적 감독만으로는 객체 기하학과 부품 동작을 분리하기 어려운 문제가 있습니다. 이를 해결하기 위해, 사전 학습된 추적 모델의 운동 사전 지식을 효과적으로 통합하는 방법을 제안합니다. VideoArtGS는 3D 트랙을 분석하고 노이즈를 필터링하여 신뢰할 수 있는 관절 매개변수 초기화를 제공하며, 하이브리드 중심-그리드 부품 할당 모듈을 설계하여 정확한 부품 동작을 포착합니다. 이 방법은 관절 및 메시 재구성에서 최첨단 성능을 보여주며, 기존 방법에 비해 재구성 오류를 약 100배 줄였습니다. VideoArtGS는 단안 비디오에서 실용적인 디지털 트윈 생성을 가능하게 하며, 비디오 기반 관절 객체 재구성의 새로운 기준을 세웁니다.

## 🎯 주요 포인트

- 1. VideoArtGS는 단안 비디오에서 고충실도의 디지털 트윈을 재구성하는 새로운 접근법을 제안합니다.
- 2. 모션 프라이어 가이드라인 파이프라인을 통해 3D 트랙을 분석하고 노이즈를 필터링하여 관절 매개변수의 신뢰성 있는 초기화를 제공합니다.
- 3. 하이브리드 중심-그리드 부품 할당 모듈을 설계하여 정확한 부품 운동을 포착합니다.
- 4. VideoArtGS는 기존 방법에 비해 재구성 오류를 약 두 자릿수 감소시키며, 관절 및 메쉬 재구성에서 최첨단 성능을 보여줍니다.
- 5. 본 연구는 단안 비디오 기반의 관절 객체 재구성을 위한 새로운 벤치마크를 설정하며, 실용적인 디지털 트윈 생성이 가능합니다.


---

*Generated on 2025-09-24 00:04:32*