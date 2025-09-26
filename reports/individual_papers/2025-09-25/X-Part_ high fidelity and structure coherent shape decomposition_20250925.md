---
keywords:
  - 3D Shape Generation
  - Semantic Decomposition
  - Interactive Part Generation
  - Structural Coherence
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.08643
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:30:06.713390",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Shape Generation",
    "Semantic Decomposition",
    "Interactive Part Generation",
    "Structural Coherence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Shape Generation": 0.85,
    "Semantic Decomposition": 0.8,
    "Interactive Part Generation": 0.78,
    "Structural Coherence": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D shape generation",
        "canonical": "3D Shape Generation",
        "aliases": [
          "3D modeling",
          "3D asset creation"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's contribution, linking to 3D modeling and asset creation fields.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "semantic decomposition",
        "canonical": "Semantic Decomposition",
        "aliases": [
          "meaningful decomposition",
          "semantic segmentation"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for linking to semantic analysis and segmentation techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "interactive part generation",
        "canonical": "Interactive Part Generation",
        "aliases": [
          "editable part creation",
          "interactive modeling"
        ],
        "category": "unique_technical",
        "rationale": "Highlights the paper's novel approach to user interaction in 3D modeling.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "structurally coherent parts",
        "canonical": "Structural Coherence",
        "aliases": [
          "coherent structure",
          "structural integrity"
        ],
        "category": "specific_connectable",
        "rationale": "Important for linking to structural analysis and integrity in 3D design.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "high fidelity",
      "state-of-the-art",
      "extensive experimental results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D shape generation",
      "resolved_canonical": "3D Shape Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "semantic decomposition",
      "resolved_canonical": "Semantic Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "interactive part generation",
      "resolved_canonical": "Interactive Part Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "structurally coherent parts",
      "resolved_canonical": "Structural Coherence",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# X-Part: high fidelity and structure coherent shape decomposition

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.08643.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.08643](https://arxiv.org/abs/2509.08643)

## 🔗 유사한 논문
- [[2025-09-23/MMPart_ Harnessing Multi-Modal Large Language Models for Part-Aware 3D Generation_20250923|MMPart: Harnessing Multi-Modal Large Language Models for Part-Aware 3D Generation]] (85.3% similar)
- [[2025-09-22/GenCAD-3D_ CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing_20250922|GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment and Synthetic Dataset Balancing]] (81.2% similar)
- [[2025-09-23/Guided and Unguided Conditional Diffusion Mechanisms for Structured and Semantically-Aware 3D Point Cloud Generation_20250923|Guided and Unguided Conditional Diffusion Mechanisms for Structured and Semantically-Aware 3D Point Cloud Generation]] (81.1% similar)
- [[2025-09-23/SCORP_ Scene-Consistent Object Refinement via Proxy Generation and Tuning_20250923|SCORP: Scene-Consistent Object Refinement via Proxy Generation and Tuning]] (80.8% similar)
- [[2025-09-23/Emergent 3D Correspondence from Neural Shape Representation_20250923|Emergent 3D Correspondence from Neural Shape Representation]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Semantic Decomposition|Semantic Decomposition]], [[keywords/Structural Coherence|Structural Coherence]]
**⚡ Unique Technical**: [[keywords/3D Shape Generation|3D Shape Generation]], [[keywords/Interactive Part Generation|Interactive Part Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.08643v2 Announce Type: replace-cross 
Abstract: Generating 3D shapes at part level is pivotal for downstream applications such as mesh retopology, UV mapping, and 3D printing. However, existing part-based generation methods often lack sufficient controllability and suffer from poor semantically meaningful decomposition. To this end, we introduce X-Part, a controllable generative model designed to decompose a holistic 3D object into semantically meaningful and structurally coherent parts with high geometric fidelity. X-Part exploits the bounding box as prompts for the part generation and injects point-wise semantic features for meaningful decomposition. Furthermore, we design an editable pipeline for interactive part generation. Extensive experimental results show that X-Part achieves state-of-the-art performance in part-level shape generation. This work establishes a new paradigm for creating production-ready, editable, and structurally sound 3D assets. Codes will be released for public research.

## 📝 요약

X-Part는 3D 객체를 의미론적으로 의미 있는 부분으로 분해하는 제어 가능한 생성 모델로, 기존 방법의 제어력 부족과 의미 있는 분해 문제를 해결합니다. 이 모델은 바운딩 박스를 활용하여 부분 생성을 유도하고, 점별 의미론적 특징을 주입하여 구조적으로 일관된 분해를 실현합니다. 또한, 상호작용 가능한 부분 생성을 위한 편집 가능한 파이프라인을 설계했습니다. 실험 결과, X-Part는 부분 수준의 형태 생성에서 최첨단 성능을 달성했으며, 생산 준비가 된 편집 가능한 3D 자산 생성의 새로운 패러다임을 제시합니다. 코드도 공개될 예정입니다.

## 🎯 주요 포인트

- 1. X-Part는 전체 3D 객체를 의미론적으로 의미 있는 부분으로 분해하는 제어 가능한 생성 모델입니다.
- 2. X-Part는 바운딩 박스를 파트 생성의 프롬프트로 활용하고, 점별 의미론적 특징을 주입하여 의미 있는 분해를 수행합니다.
- 3. X-Part는 상호작용적인 부분 생성이 가능한 편집 가능한 파이프라인을 설계했습니다.
- 4. 실험 결과, X-Part는 부분 수준의 형태 생성에서 최첨단 성능을 달성했습니다.
- 5. 이 연구는 생산 준비가 된 편집 가능하고 구조적으로 견고한 3D 자산을 생성하는 새로운 패러다임을 확립했습니다.


---

*Generated on 2025-09-26 09:30:06*