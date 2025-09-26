---
keywords:
  - 3D Indoor Scene Generation
  - SpatialGen
  - Multimodal Learning
  - Semantic Segmentation
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.14981
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:40:57.148255",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Indoor Scene Generation",
    "SpatialGen",
    "Multimodal Learning",
    "Semantic Segmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Indoor Scene Generation": 0.78,
    "SpatialGen": 0.82,
    "Multimodal Learning": 0.77,
    "Semantic Segmentation": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Indoor Scene Generation",
        "canonical": "3D Indoor Scene Generation",
        "aliases": [
          "Indoor Scene Synthesis",
          "3D Scene Creation"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task central to the paper, linking to research on automated scene synthesis.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "SpatialGen",
        "canonical": "SpatialGen",
        "aliases": [
          "Spatial Generation Model"
        ],
        "category": "unique_technical",
        "rationale": "SpatialGen is the novel model introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multi-modal Diffusion Model",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multi-modal Model"
        ],
        "category": "specific_connectable",
        "rationale": "This connects to the broader concept of multimodal learning, relevant for linking cross-disciplinary research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Semantic Segmentation",
        "canonical": "Semantic Segmentation",
        "aliases": [
          "Scene Segmentation"
        ],
        "category": "broad_technical",
        "rationale": "Semantic segmentation is a key process in computer vision, relevant for scene understanding.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "model",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Indoor Scene Generation",
      "resolved_canonical": "3D Indoor Scene Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "SpatialGen",
      "resolved_canonical": "SpatialGen",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multi-modal Diffusion Model",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Semantic Segmentation",
      "resolved_canonical": "Semantic Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# SPATIALGEN: Layout-guided 3D Indoor Scene Generation

**Korean Title:** SPATIALGEN: 레이아웃 기반 3D 실내 장면 생성

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14981.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.14981](https://arxiv.org/abs/2509.14981)

## 🔗 유사한 논문
- [[2025-09-22/OptiScene_ LLM-driven Indoor Scene Layout Generation via Scaled Human-aligned Data Synthesis and Multi-Stage Preference Optimization_20250922|OptiScene: LLM-driven Indoor Scene Layout Generation via Scaled Human-aligned Data Synthesis and Multi-Stage Preference Optimization]] (90.2% similar)
- [[2025-09-22/GenCAD-3D_ CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing_20250922|GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing]] (85.0% similar)
- [[2025-09-22/Causal Reasoning Elicits Controllable 3D Scene Generation_20250922|Causal Reasoning Elicits Controllable 3D Scene Generation]] (84.3% similar)
- [[2025-09-22/Spatial Understanding from Videos_ Structured Prompts Meet Simulation Data_20250922|Spatial Understanding from Videos: Structured Prompts Meet Simulation Data]] (83.1% similar)
- [[2025-09-22/Vision-Language Models as Differentiable Semantic and Spatial Rewards for Text-to-3D Generation_20250922|Vision-Language Models as Differentiable Semantic and Spatial Rewards for Text-to-3D Generation]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Semantic Segmentation|Semantic Segmentation]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/3D Indoor Scene Generation|3D Indoor Scene Generation]], [[keywords/SpatialGen|SpatialGen]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14981v2 Announce Type: replace 
Abstract: Creating high-fidelity 3D models of indoor environments is essential for applications in design, virtual reality, and robotics. However, manual 3D modeling remains time-consuming and labor-intensive. While recent advances in generative AI have enabled automated scene synthesis, existing methods often face challenges in balancing visual quality, diversity, semantic consistency, and user control. A major bottleneck is the lack of a large-scale, high-quality dataset tailored to this task. To address this gap, we introduce a comprehensive synthetic dataset, featuring 12,328 structured annotated scenes with 57,440 rooms, and 4.7M photorealistic 2D renderings. Leveraging this dataset, we present SpatialGen, a novel multi-view multi-modal diffusion model that generates realistic and semantically consistent 3D indoor scenes. Given a 3D layout and a reference image (derived from a text prompt), our model synthesizes appearance (color image), geometry (scene coordinate map), and semantic (semantic segmentation map) from arbitrary viewpoints, while preserving spatial consistency across modalities. SpatialGen consistently generates superior results to previous methods in our experiments. We are open-sourcing our data and models to empower the community and advance the field of indoor scene understanding and generation.

## 🔍 Abstract (한글 번역)

arXiv:2509.14981v2 발표 유형: 교체  
초록: 실내 환경의 고충실도 3D 모델을 생성하는 것은 디자인, 가상 현실, 로봇 공학 분야에서 필수적입니다. 그러나 수작업 3D 모델링은 여전히 시간 소모적이고 노동 집약적입니다. 최근 생성적 인공지능의 발전으로 자동화된 장면 합성이 가능해졌지만, 기존 방법들은 시각적 품질, 다양성, 의미론적 일관성, 사용자 제어 간의 균형을 맞추는 데 어려움을 겪고 있습니다. 주요 병목 현상은 이 작업에 맞춘 대규모 고품질 데이터셋의 부족입니다. 이 격차를 해소하기 위해, 우리는 12,328개의 구조화된 주석이 달린 장면과 57,440개의 방, 그리고 470만 개의 사진 실사 2D 렌더링을 특징으로 하는 포괄적인 합성 데이터셋을 소개합니다. 이 데이터셋을 활용하여, 우리는 현실적이고 의미론적으로 일관된 3D 실내 장면을 생성하는 새로운 다중 뷰 다중 모달 확산 모델인 SpatialGen을 제시합니다. 3D 레이아웃과 참조 이미지(텍스트 프롬프트에서 파생된)가 주어지면, 우리 모델은 임의의 관점에서 외관(컬러 이미지), 기하학(장면 좌표 맵), 의미론(의미론적 분할 맵)을 합성하며, 모달리티 간 공간적 일관성을 유지합니다. SpatialGen은 우리의 실험에서 이전 방법들보다 일관되게 우수한 결과를 생성합니다. 우리는 실내 장면 이해 및 생성 분야를 발전시키고 커뮤니티에 힘을 실어주기 위해 우리의 데이터와 모델을 오픈 소스로 공개하고 있습니다.

## 📝 요약

이 논문은 실내 환경의 고품질 3D 모델 생성을 위한 새로운 접근법을 제시합니다. 기존의 자동 장면 생성 방법은 시각적 품질, 다양성, 의미적 일관성, 사용자 제어 간의 균형을 맞추기 어려웠습니다. 이를 해결하기 위해 12,328개의 구조화된 주석 장면과 57,440개의 방, 470만 개의 사실적인 2D 렌더링을 포함한 대규모 합성 데이터셋을 소개합니다. 이 데이터셋을 활용하여 SpatialGen이라는 새로운 다중 뷰 다중 모달 확산 모델을 개발했습니다. 이 모델은 3D 레이아웃과 텍스트 프롬프트에서 파생된 참조 이미지를 기반으로, 임의의 관점에서 색상 이미지, 장면 좌표 지도, 의미적 분할 지도를 생성하며, 공간적 일관성을 유지합니다. 실험 결과, SpatialGen은 기존 방법들보다 우수한 결과를 일관되게 생성했습니다. 데이터와 모델을 오픈소스로 제공하여 실내 장면 이해 및 생성 분야의 발전을 도모하고자 합니다.

## 🎯 주요 포인트

- 1. 실내 환경의 고품질 3D 모델링은 디자인, 가상 현실, 로봇 공학 분야에서 필수적이지만, 수작업으로는 많은 시간과 노력이 필요합니다.
- 2. 기존의 자동 장면 합성 방법은 시각적 품질, 다양성, 의미론적 일관성, 사용자 제어 간의 균형을 맞추는 데 어려움을 겪고 있습니다.
- 3. 이러한 문제를 해결하기 위해, 12,328개의 구조화된 주석 장면과 57,440개의 방, 470만 개의 사실적인 2D 렌더링을 포함한 종합적인 합성 데이터셋을 소개합니다.
- 4. SpatialGen은 다중 뷰 다중 모달 확산 모델로, 주어진 3D 레이아웃과 참조 이미지로부터 현실적이고 의미론적으로 일관된 3D 실내 장면을 생성합니다.
- 5. 우리는 데이터와 모델을 오픈 소스로 제공하여 실내 장면 이해 및 생성 분야의 발전을 도모하고자 합니다.


---

*Generated on 2025-09-23 12:40:57*