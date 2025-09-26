---
keywords:
  - 360-Degree Video
  - WorldPrompter
  - Gaussian Splats
  - 3D Scene Generation
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2504.02045
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:34:25.695810",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "360-Degree Video",
    "WorldPrompter",
    "Gaussian Splats",
    "3D Scene Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "360-Degree Video": 0.8,
    "WorldPrompter": 0.78,
    "Gaussian Splats": 0.72,
    "3D Scene Generation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "360° video",
        "canonical": "360-Degree Video",
        "aliases": [
          "360-degree video",
          "panoramic video"
        ],
        "category": "specific_connectable",
        "rationale": "360° video is central to the paper's approach for 3D scene generation and connects with existing work on panoramic and immersive media.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "WorldPrompter",
        "canonical": "WorldPrompter",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "WorldPrompter is a novel generative pipeline introduced in the paper, offering a unique approach to 3D scene synthesis from text prompts.",
        "novelty_score": 0.9,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Gaussian splats",
        "canonical": "Gaussian Splats",
        "aliases": [
          "Gaussian splatting"
        ],
        "category": "unique_technical",
        "rationale": "Gaussian splats are a specific technique used for reconstructing 3D scenes, providing a unique method for scene visualization.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "3D scene generation",
        "canonical": "3D Scene Generation",
        "aliases": [
          "3D scene synthesis"
        ],
        "category": "broad_technical",
        "rationale": "3D scene generation is a broad technical area that the paper contributes to, linking with other research in computer vision and graphics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "navigational freedom"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "360° video",
      "resolved_canonical": "360-Degree Video",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "WorldPrompter",
      "resolved_canonical": "WorldPrompter",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Gaussian splats",
      "resolved_canonical": "Gaussian Splats",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "3D scene generation",
      "resolved_canonical": "3D Scene Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Generating 360{\deg} Video is What You Need For a 3D Scene

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2504.02045.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2504.02045](https://arxiv.org/abs/2504.02045)

## 🔗 유사한 논문
- [[2025-09-19/WorldForge_ Unlocking Emergent 3D/4D Generation in Video Diffusion Model via Training-Free Guidance_20250919|WorldForge: Unlocking Emergent 3D/4D Generation in Video Diffusion Model via Training-Free Guidance]] (85.2% similar)
- [[2025-09-19/SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN: Layout-guided 3D Indoor Scene Generation]] (83.0% similar)
- [[2025-09-23/Text-Scene_ A Scene-to-Language Parsing Framework for 3D Scene Understanding_20250923|Text-Scene: A Scene-to-Language Parsing Framework for 3D Scene Understanding]] (82.4% similar)
- [[2025-09-22/Spatial Understanding from Videos_ Structured Prompts Meet Simulation Data_20250922|Spatial Understanding from Videos: Structured Prompts Meet Simulation Data]] (82.4% similar)
- [[2025-09-23/ProDyG_ Progressive Dynamic Scene Reconstruction via Gaussian Splatting from Monocular Videos_20250923|ProDyG: Progressive Dynamic Scene Reconstruction via Gaussian Splatting from Monocular Videos]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/3D Scene Generation|3D Scene Generation]]
**🔗 Specific Connectable**: [[keywords/360-Degree Video|360-Degree Video]]
**⚡ Unique Technical**: [[keywords/WorldPrompter|WorldPrompter]], [[keywords/Gaussian Splats|Gaussian Splats]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.02045v2 Announce Type: replace-cross 
Abstract: Generating 3D scenes is still a challenging task due to the lack of readily available scene data. Most existing methods only produce partial scenes and provide limited navigational freedom. We introduce a practical and scalable solution that uses 360{\deg} video as an intermediate scene representation, capturing the full-scene context and ensuring consistent visual content throughout the generation. We propose WorldPrompter, a generative pipeline that synthesizes traversable 3D scenes from text prompts. WorldPrompter incorporates a conditional 360{\deg} panoramic video generator, capable of producing a 128-frame video that simulates a person walking through and capturing a virtual environment. The resulting video is then reconstructed as Gaussian splats by a fast feedforward 3D reconstructor, enabling a true walkable experience within the 3D scene. Experiments demonstrate that our panoramic video generation model, trained with a mix of image and video data, achieves convincing spatial and temporal consistency for static scenes. This is validated by an average COLMAP matching rate of 94.6\%, allowing for high-quality panoramic Gaussian splat reconstruction and improved navigation throughout the scene. Qualitative and quantitative results also show it outperforms the state-of-the-art 360{\deg} video generators and 3D scene generation models.

## 📝 요약

이 논문은 3D 장면 생성을 위한 새로운 방법론인 WorldPrompter를 제안합니다. 이는 360도 비디오를 중간 표현으로 사용하여 전체 장면을 포괄하고 일관된 시각적 콘텐츠를 보장합니다. WorldPrompter는 텍스트 프롬프트로부터 탐색 가능한 3D 장면을 생성하며, 조건부 360도 파노라마 비디오 생성기를 통해 가상 환경을 걷는 128프레임 비디오를 만듭니다. 이 비디오는 빠른 피드포워드 3D 재구성기를 통해 가우시안 스플랫으로 재구성되어 실제로 걸을 수 있는 3D 장면을 제공합니다. 실험 결과, 이미지와 비디오 데이터를 혼합하여 훈련된 파노라마 비디오 생성 모델이 정적 장면에서 공간적, 시간적 일관성을 달성했음을 보여줍니다. 평균 COLMAP 매칭률 94.6%로 높은 품질의 파노라마 가우시안 스플랫 재구성을 가능하게 하며, 기존의 360도 비디오 생성기와 3D 장면 생성 모델을 능가하는 성능을 입증합니다.

## 🎯 주요 포인트

- 1. 3D 장면 생성을 위한 WorldPrompter라는 텍스트 기반 생성 파이프라인을 제안합니다.
- 2. WorldPrompter는 360도 파노라마 비디오 생성기를 사용하여 가상 환경을 걷는 듯한 128프레임 비디오를 생성합니다.
- 3. 생성된 비디오는 빠른 피드포워드 3D 재구성기를 통해 가우시안 스플랫으로 재구성되어 3D 장면 내에서 실제로 걸을 수 있는 경험을 제공합니다.
- 4. 실험 결과, 이미지와 비디오 데이터를 혼합하여 훈련된 파노라마 비디오 생성 모델이 정적 장면에 대해 높은 공간적 및 시간적 일관성을 달성함을 보여줍니다.
- 5. 제안된 방법은 최첨단 360도 비디오 생성기 및 3D 장면 생성 모델을 능가하는 성능을 보입니다.


---

*Generated on 2025-09-24 05:34:25*