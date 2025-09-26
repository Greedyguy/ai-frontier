---
keywords:
  - 3D Gaussian Splatting
  - Online Language Splatting
  - CLIP Embedding
  - Vision-Language Model
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2503.09447
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:11:11.293725",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Online Language Splatting",
    "CLIP Embedding",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.78,
    "Online Language Splatting": 0.82,
    "CLIP Embedding": 0.8,
    "Vision-Language Model": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Gaussian Splatting",
        "canonical": "3D Gaussian Splatting",
        "aliases": [
          "3DGS"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific technique central to the paper's methodology, offering a unique approach to 3D scene representation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Online Language Splatting",
        "canonical": "Online Language Splatting",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework for real-time language mapping in 3D environments, distinct from existing methods.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "CLIP embedding module",
        "canonical": "CLIP Embedding",
        "aliases": [
          "CLIP"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to existing work on multimodal learning and language-image embeddings, enhancing understanding of language features.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Vision-Language",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Relevant to the integration of visual and linguistic data, a key aspect of the paper's approach.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "3D representations",
      "language features",
      "rendering quality"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Online Language Splatting",
      "resolved_canonical": "Online Language Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "CLIP embedding module",
      "resolved_canonical": "CLIP Embedding",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Vision-Language",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Online Language Splatting

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2503.09447.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2503.09447](https://arxiv.org/abs/2503.09447)

## 🔗 유사한 논문
- [[2025-09-23/Federated Learning with Ad-hoc Adapter Insertions_ The Case of Soft-Embeddings for Training Classifier-as-Retriever_20250923|Federated Learning with Ad-hoc Adapter Insertions: The Case of Soft-Embeddings for Training Classifier-as-Retriever]] (83.6% similar)
- [[2025-09-23/ProDyG_ Progressive Dynamic Scene Reconstruction via Gaussian Splatting from Monocular Videos_20250923|ProDyG: Progressive Dynamic Scene Reconstruction via Gaussian Splatting from Monocular Videos]] (82.3% similar)
- [[2025-09-22/Using Natural Language for Human-Robot Collaboration in the Real World_20250922|Using Natural Language for Human-Robot Collaboration in the Real World]] (81.7% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (81.5% similar)
- [[2025-09-23/Dynamic Speculative Agent Planning_20250923|Dynamic Speculative Agent Planning]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/CLIP Embedding|CLIP Embedding]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Online Language Splatting|Online Language Splatting]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.09447v2 Announce Type: replace 
Abstract: To enable AI agents to interact seamlessly with both humans and 3D environments, they must not only perceive the 3D world accurately but also align human language with 3D spatial representations. While prior work has made significant progress by integrating language features into geometrically detailed 3D scene representations using 3D Gaussian Splatting (GS), these approaches rely on computationally intensive offline preprocessing of language features for each input image, limiting adaptability to new environments. In this work, we introduce Online Language Splatting, the first framework to achieve online, near real-time, open-vocabulary language mapping within a 3DGS-SLAM system without requiring pre-generated language features. The key challenge lies in efficiently fusing high-dimensional language features into 3D representations while balancing the computation speed, memory usage, rendering quality and open-vocabulary capability. To this end, we innovatively design: (1) a high-resolution CLIP embedding module capable of generating detailed language feature maps in 18ms per frame, (2) a two-stage online auto-encoder that compresses 768-dimensional CLIP features to 15 dimensions while preserving open-vocabulary capabilities, and (3) a color-language disentangled optimization approach to improve rendering quality. Experimental results show that our online method not only surpasses the state-of-the-art offline methods in accuracy but also achieves more than 40x efficiency boost, demonstrating the potential for dynamic and interactive AI applications.

## 📝 요약

이 논문은 AI 에이전트가 인간과 3D 환경과 원활하게 상호작용할 수 있도록 하는 방법을 제안합니다. 기존의 연구는 3D Gaussian Splatting을 사용하여 언어 기능을 3D 장면 표현에 통합했지만, 새로운 환경에 적응하는 데 한계가 있었습니다. 본 연구에서는 사전 생성된 언어 기능 없이도 3DGS-SLAM 시스템 내에서 실시간으로 언어 매핑을 수행하는 'Online Language Splatting' 프레임워크를 소개합니다. 주요 기여로는 (1) 고해상도 CLIP 임베딩 모듈, (2) 768차원 CLIP 기능을 15차원으로 압축하는 온라인 오토인코더, (3) 색상-언어 분리 최적화 접근법이 있습니다. 실험 결과, 이 온라인 방법은 기존의 오프라인 방법보다 정확도가 높고, 효율성은 40배 이상 향상되었습니다.

## 🎯 주요 포인트

- 1. AI 에이전트가 인간 언어와 3D 공간 표현을 매핑하여 상호작용할 수 있도록 하는 온라인 언어 스플래팅 프레임워크를 소개합니다.
- 2. 18ms 내에 세부적인 언어 특징 맵을 생성할 수 있는 고해상도 CLIP 임베딩 모듈을 설계했습니다.
- 3. 768차원의 CLIP 특징을 15차원으로 압축하면서도 개방형 어휘 기능을 유지하는 2단계 온라인 오토인코더를 개발했습니다.
- 4. 렌더링 품질을 향상시키기 위해 색상-언어 분리 최적화 접근 방식을 도입했습니다.
- 5. 실험 결과, 제안된 온라인 방법이 정확도에서 최신 오프라인 방법을 능가하며 40배 이상의 효율성을 보여줍니다.


---

*Generated on 2025-09-25 16:11:11*