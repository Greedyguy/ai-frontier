---
keywords:
  - Zero-Shot Learning
  - 3D Visual Grounding
  - 3D Gaussian Splatting
  - View Retrieval
  - Vision-Language Model
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15871
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:12:47.171099",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "3D Visual Grounding",
    "3D Gaussian Splatting",
    "View Retrieval",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.9,
    "3D Visual Grounding": 0.88,
    "3D Gaussian Splatting": 0.85,
    "View Retrieval": 0.87,
    "Vision-Language Model": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-Shot Visual Grounding",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the concept of learning without labeled data, relevant to zero-shot tasks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "3D Visual Grounding",
        "canonical": "3D Visual Grounding",
        "aliases": [
          "3DVG"
        ],
        "category": "unique_technical",
        "rationale": "Specific to the task of locating objects in 3D scenes based on text, crucial for the paper's focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [
          "3DGS"
        ],
        "category": "unique_technical",
        "rationale": "A unique representation method for spatial textures in 3D, central to the paper's methodology.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "View Retrieval",
        "canonical": "View Retrieval",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Key to transforming 3D visual grounding into a 2D retrieval task, pivotal for the proposed method.",
        "novelty_score": 0.68,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.87
      },
      {
        "surface": "Vision-Language",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Relates to models that integrate visual and textual data, relevant to the grounding task.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
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
      "candidate_surface": "Zero-Shot Visual Grounding",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "3D Visual Grounding",
      "resolved_canonical": "3D Visual Grounding",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "View Retrieval",
      "resolved_canonical": "View Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.87
      }
    },
    {
      "candidate_surface": "Vision-Language",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Zero-Shot Visual Grounding in 3D Gaussians via View Retrieval

**Korean Title:** 3D 가우시안에서의 제로-샷 시각적 그라운딩을 위한 뷰 검색

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15871.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15871](https://arxiv.org/abs/2509.15871)

## 🔗 유사한 논문
- [[2025-09-18/Improving Generalized Visual Grounding with Instance-aware Joint Learning_20250918|Improving Generalized Visual Grounding with Instance-aware Joint Learning]] (84.1% similar)
- [[2025-09-22/Sparse Multiview Open-Vocabulary 3D Detection_20250922|Sparse Multiview Open-Vocabulary 3D Detection]] (83.9% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (82.3% similar)
- [[2025-09-19/Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding_20250919|Unleashing the Potential of Multimodal LLMs for Zero-Shot Spatio-Temporal Video Grounding]] (81.2% similar)
- [[2025-09-22/Spatial Understanding from Videos_ Structured Prompts Meet Simulation Data_20250922|Spatial Understanding from Videos: Structured Prompts Meet Simulation Data]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/3D Visual Grounding|3D Visual Grounding]], [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/View Retrieval|View Retrieval]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15871v1 Announce Type: new 
Abstract: 3D Visual Grounding (3DVG) aims to locate objects in 3D scenes based on text prompts, which is essential for applications such as robotics. However, existing 3DVG methods encounter two main challenges: first, they struggle to handle the implicit representation of spatial textures in 3D Gaussian Splatting (3DGS), making per-scene training indispensable; second, they typically require larges amounts of labeled data for effective training. To this end, we propose \underline{G}rounding via \underline{V}iew \underline{R}etrieval (GVR), a novel zero-shot visual grounding framework for 3DGS to transform 3DVG as a 2D retrieval task that leverages object-level view retrieval to collect grounding clues from multiple views, which not only avoids the costly process of 3D annotation, but also eliminates the need for per-scene training. Extensive experiments demonstrate that our method achieves state-of-the-art visual grounding performance while avoiding per-scene training, providing a solid foundation for zero-shot 3DVG research. Video demos can be found in https://github.com/leviome/GVR_demos.

## 🔍 Abstract (한글 번역)

arXiv:2509.15871v1 발표 유형: 신규  
초록: 3D 시각적 그라운딩(3DVG)은 텍스트 프롬프트를 기반으로 3D 장면에서 객체를 찾는 것을 목표로 하며, 이는 로봇공학과 같은 응용 분야에서 필수적입니다. 그러나 기존의 3DVG 방법은 두 가지 주요 문제에 직면합니다. 첫째, 3D 가우시안 스플래팅(3DGS)에서 공간 텍스처의 암시적 표현을 처리하는 데 어려움을 겪어 장면별 훈련이 필수적입니다. 둘째, 효과적인 훈련을 위해 대량의 레이블이 지정된 데이터가 필요합니다. 이를 해결하기 위해 우리는 \underline{G}rounding via \underline{V}iew \underline{R}etrieval (GVR)을 제안합니다. 이는 3DGS를 위한 새로운 제로샷 시각적 그라운딩 프레임워크로, 3DVG를 객체 수준의 뷰 검색을 활용하여 여러 뷰에서 그라운딩 단서를 수집하는 2D 검색 작업으로 변환합니다. 이는 비용이 많이 드는 3D 주석 과정을 피할 뿐만 아니라 장면별 훈련의 필요성을 제거합니다. 광범위한 실험을 통해 우리의 방법이 장면별 훈련을 피하면서도 최첨단 시각적 그라운딩 성능을 달성하고, 제로샷 3DVG 연구를 위한 견고한 기반을 제공함을 입증합니다. 비디오 데모는 https://github.com/leviome/GVR_demos에서 확인할 수 있습니다.

## 📝 요약

이 논문은 3D 시각적 그라운딩(3DVG)에서 텍스트 프롬프트를 기반으로 3D 장면 내 객체를 찾는 문제를 다룹니다. 기존 방법들은 3D 가우시안 스플래팅(3DGS)의 공간 텍스처 표현 처리와 대량의 라벨 데이터 필요성에서 어려움을 겪습니다. 이를 해결하기 위해, 저자들은 새로운 제로샷 시각적 그라운딩 프레임워크인 GVR(Grounding via View Retrieval)을 제안합니다. GVR은 3DVG를 2D 검색 과제로 변환하여 여러 시점에서 객체 수준의 단서를 수집함으로써 3D 주석과 장면별 훈련의 필요성을 없앱니다. 실험 결과, GVR은 최첨단 성능을 보이며 제로샷 3DVG 연구에 기여합니다.

## 🎯 주요 포인트

- 1. 3D 비주얼 그라운딩(3DVG)은 로봇 공학과 같은 응용 분야에서 텍스트 프롬프트를 기반으로 3D 장면에서 객체를 찾는 것을 목표로 한다.
- 2. 기존 3DVG 방법은 3D 가우시안 스플래팅(3DGS)의 공간 텍스처 표현을 처리하는 데 어려움을 겪고, 장면별 훈련이 필수적이다.
- 3. 우리는 3DGS를 2D 검색 작업으로 변환하여 장면별 훈련을 피하고 3D 주석의 비용을 절감할 수 있는 새로운 제로샷 비주얼 그라운딩 프레임워크인 GVR을 제안한다.
- 4. GVR은 객체 수준의 뷰 검색을 활용하여 여러 뷰에서 그라운딩 단서를 수집하며, 많은 양의 라벨링된 데이터가 필요하지 않다.
- 5. 우리의 방법은 장면별 훈련 없이도 최첨단 비주얼 그라운딩 성능을 달성하며, 제로샷 3DVG 연구의 견고한 기반을 제공한다.


---

*Generated on 2025-09-23 12:12:47*