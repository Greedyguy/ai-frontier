---
keywords:
  - Multimodal Learning
  - Part-aware 3D Generation
  - Vision-Language Model
  - Generative 3D Modeling
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16768
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:34:04.526670",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Part-aware 3D Generation",
    "Vision-Language Model",
    "Generative 3D Modeling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.82,
    "Part-aware 3D Generation": 0.78,
    "Vision-Language Model": 0.84,
    "Generative 3D Modeling": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-Modal Large Language Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal LLMs",
          "Vision-Language Models"
        ],
        "category": "evolved_concepts",
        "rationale": "This concept bridges language and vision, crucial for understanding and linking multimodal research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Part-aware 3D Generation",
        "canonical": "Part-aware 3D Generation",
        "aliases": [
          "3D Component Decomposition"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach in 3D modeling, focusing on decomposing objects into meaningful parts.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM"
        ],
        "category": "evolved_concepts",
        "rationale": "This model type is essential for linking tasks involving both vision and language inputs.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.84
      },
      {
        "surface": "Generative 3D Modeling",
        "canonical": "Generative 3D Modeling",
        "aliases": [
          "3D Model Generation"
        ],
        "category": "broad_technical",
        "rationale": "A fundamental concept in 3D design, linking to various applications in VR/AR and robotics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "closed mesh",
      "structural information",
      "isolation phase"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-Modal Large Language Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Part-aware 3D Generation",
      "resolved_canonical": "Part-aware 3D Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.84
      }
    },
    {
      "candidate_surface": "Generative 3D Modeling",
      "resolved_canonical": "Generative 3D Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# MMPart: Harnessing Multi-Modal Large Language Models for Part-Aware 3D Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16768.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16768](https://arxiv.org/abs/2509.16768)

## 🔗 유사한 논문
- [[2025-09-19/A Mutual Information Perspective on Multiple Latent Variable Generative Models for Positive View Generation_20250919|A Mutual Information Perspective on Multiple Latent Variable Generative Models for Positive View Generation]] (83.5% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (83.0% similar)
- [[2025-09-19/SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN: Layout-guided 3D Indoor Scene Generation]] (82.7% similar)
- [[2025-09-23/Octree Latent Diffusion for Semantic 3D Scene Generation and Completion_20250923|Octree Latent Diffusion for Semantic 3D Scene Generation and Completion]] (82.5% similar)
- [[2025-09-23/Learning Primitive Embodied World Models_ Towards Scalable Robotic Learning_20250923|Learning Primitive Embodied World Models: Towards Scalable Robotic Learning]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Generative 3D Modeling|Generative 3D Modeling]]
**⚡ Unique Technical**: [[keywords/Part-aware 3D Generation|Part-aware 3D Generation]]
**🚀 Evolved Concepts**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16768v1 Announce Type: new 
Abstract: Generative 3D modeling has advanced rapidly, driven by applications in VR/AR, metaverse, and robotics. However, most methods represent the target object as a closed mesh devoid of any structural information, limiting editing, animation, and semantic understanding. Part-aware 3D generation addresses this problem by decomposing objects into meaningful components, but existing pipelines face challenges: in existing methods, the user has no control over which objects are separated and how model imagine the occluded parts in isolation phase. In this paper, we introduce MMPart, an innovative framework for generating part-aware 3D models from a single image. We first use a VLM to generate a set of prompts based on the input image and user descriptions. In the next step, a generative model generates isolated images of each object based on the initial image and the previous step's prompts as supervisor (which control the pose and guide model how imagine previously occluded areas). Each of those images then enters the multi-view generation stage, where a number of consistent images from different views are generated. Finally, a reconstruction model converts each of these multi-view images into a 3D model.

## 📝 요약

이 논문은 단일 이미지로부터 부분 인식 3D 모델을 생성하는 혁신적인 프레임워크인 MMPart를 소개합니다. 기존의 3D 생성 방법은 구조적 정보를 포함하지 않아 편집과 애니메이션에 한계가 있었으나, MMPart는 객체를 의미 있는 구성 요소로 분해하여 이를 해결합니다. 이 방법론은 입력 이미지와 사용자 설명을 바탕으로 VLM을 사용해 프롬프트를 생성하고, 생성 모델이 초기 이미지와 프롬프트를 기반으로 객체의 분리된 이미지를 생성합니다. 이후 다중 뷰 생성 단계에서 일관된 이미지를 생성하고, 마지막으로 재구성 모델이 이를 3D 모델로 변환합니다. 주요 기여는 사용자 제어가 가능한 부분 인식 3D 모델 생성의 가능성을 제시한 것입니다.

## 🎯 주요 포인트

- 1. 생성적 3D 모델링은 VR/AR, 메타버스, 로보틱스 분야의 응용으로 급속히 발전하고 있습니다.
- 2. 기존의 3D 모델링 방법은 구조적 정보를 포함하지 않는 폐쇄형 메쉬로 객체를 표현하여 편집, 애니메이션, 의미 이해에 제한이 있습니다.
- 3. MMPart는 단일 이미지로부터 부품 인식 3D 모델을 생성하는 혁신적인 프레임워크를 제안합니다.
- 4. MMPart는 입력 이미지와 사용자 설명을 기반으로 VLM을 사용하여 프롬프트 세트를 생성하고, 이를 통해 각 객체의 고립된 이미지를 생성합니다.
- 5. 생성된 다중 뷰 이미지를 3D 모델로 변환하여 구조적 정보를 포함한 3D 모델을 제공합니다.


---

*Generated on 2025-09-24 04:34:04*