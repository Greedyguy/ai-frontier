---
keywords:
  - Dynamic 3D Reconstruction
  - Simultaneous Localization and Mapping
  - Motion Masking
  - Motion Scaffolds Graph
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17864
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:05:10.193026",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dynamic 3D Reconstruction",
    "Simultaneous Localization and Mapping",
    "Motion Masking",
    "Motion Scaffolds Graph"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dynamic 3D Reconstruction": 0.78,
    "Simultaneous Localization and Mapping": 0.75,
    "Motion Masking": 0.72,
    "Motion Scaffolds Graph": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "dynamic 3D reconstruction",
        "canonical": "Dynamic 3D Reconstruction",
        "aliases": [
          "3D Scene Reconstruction",
          "Dynamic Scene Reconstruction"
        ],
        "category": "specific_connectable",
        "rationale": "This term is crucial for linking research on reconstructing dynamic environments in 3D, which is a key area in computer vision.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "SLAM system",
        "canonical": "Simultaneous Localization and Mapping",
        "aliases": [
          "SLAM"
        ],
        "category": "broad_technical",
        "rationale": "SLAM is a foundational concept in robotics and computer vision, providing strong connectivity to related works.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "motion masking strategy",
        "canonical": "Motion Masking",
        "aliases": [
          "Motion Masking Strategy"
        ],
        "category": "unique_technical",
        "rationale": "This novel strategy is specific to the paper's approach, offering a unique link to innovations in motion tracking.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Motion Scaffolds graph",
        "canonical": "Motion Scaffolds Graph",
        "aliases": [
          "Motion Graph"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a new concept for dynamic part reconstruction, enhancing specificity and novelty in the field.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "online operation",
      "detailed appearance modeling"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "dynamic 3D reconstruction",
      "resolved_canonical": "Dynamic 3D Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "SLAM system",
      "resolved_canonical": "Simultaneous Localization and Mapping",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "motion masking strategy",
      "resolved_canonical": "Motion Masking",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Motion Scaffolds graph",
      "resolved_canonical": "Motion Scaffolds Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# ProDyG: Progressive Dynamic Scene Reconstruction via Gaussian Splatting from Monocular Videos

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17864.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17864](https://arxiv.org/abs/2509.17864)

## 🔗 유사한 논문
- [[2025-09-22/MoAngelo_ Motion-Aware Neural Surface Reconstruction for Dynamic Scenes_20250922|MoAngelo: Motion-Aware Neural Surface Reconstruction for Dynamic Scenes]] (85.9% similar)
- [[2025-09-23/ConfidentSplat_ Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM_20250923|ConfidentSplat: Confidence-Weighted Depth Fusion for Accurate 3D Gaussian Splatting SLAM]] (85.6% similar)
- [[2025-09-23/3D Gaussian Flats_ Hybrid 2D/3D Photometric Scene Reconstruction_20250923|3D Gaussian Flats: Hybrid 2D/3D Photometric Scene Reconstruction]] (85.1% similar)
- [[2025-09-18/MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (84.9% similar)
- [[2025-09-23/4DGCPro_ Efficient Hierarchical 4D Gaussian Compression for Progressive Volumetric Video Streaming_20250923|4DGCPro: Efficient Hierarchical 4D Gaussian Compression for Progressive Volumetric Video Streaming]] (84.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Simultaneous Localization and Mapping|Simultaneous Localization and Mapping]]
**🔗 Specific Connectable**: [[keywords/Dynamic 3D Reconstruction|Dynamic 3D Reconstruction]]
**⚡ Unique Technical**: [[keywords/Motion Masking|Motion Masking]], [[keywords/Motion Scaffolds Graph|Motion Scaffolds Graph]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17864v1 Announce Type: new 
Abstract: Achieving truly practical dynamic 3D reconstruction requires online operation, global pose and map consistency, detailed appearance modeling, and the flexibility to handle both RGB and RGB-D inputs. However, existing SLAM methods typically merely remove the dynamic parts or require RGB-D input, while offline methods are not scalable to long video sequences, and current transformer-based feedforward methods lack global consistency and appearance details. To this end, we achieve online dynamic scene reconstruction by disentangling the static and dynamic parts within a SLAM system. The poses are tracked robustly with a novel motion masking strategy, and dynamic parts are reconstructed leveraging a progressive adaptation of a Motion Scaffolds graph. Our method yields novel view renderings competitive to offline methods and achieves on-par tracking with state-of-the-art dynamic SLAM methods.

## 📝 요약

이 논문은 실시간으로 동적인 3D 재구성을 가능하게 하는 방법을 제안합니다. 기존 SLAM 방법은 주로 동적 부분을 제거하거나 RGB-D 입력에 의존하며, 오프라인 방법은 긴 비디오 시퀀스에 적합하지 않습니다. 본 연구에서는 SLAM 시스템 내에서 정적 및 동적 부분을 분리하여 온라인 동적 장면 재구성을 수행합니다. 새로운 모션 마스킹 전략을 통해 포즈를 견고하게 추적하고, 모션 스캐폴드 그래프의 점진적 적응을 통해 동적 부분을 재구성합니다. 이 방법은 오프라인 방법과 비교해 경쟁력 있는 새로운 뷰 렌더링을 제공하며, 최신 동적 SLAM 방법과 동등한 수준의 추적 성능을 달성합니다.

## 🎯 주요 포인트

- 1. 본 연구는 온라인에서 동적 3D 재구성을 실현하기 위해 정적 및 동적 부분을 SLAM 시스템 내에서 분리하여 처리합니다.
- 2. 새로운 모션 마스킹 전략을 통해 자세를 견고하게 추적하며, 모션 스캐폴드 그래프의 점진적 적응을 활용하여 동적 부분을 재구성합니다.
- 3. 제안된 방법은 오프라인 방법과 경쟁력 있는 새로운 뷰 렌더링을 제공하며, 최첨단 동적 SLAM 방법과 동등한 수준의 추적 성능을 달성합니다.
- 4. RGB와 RGB-D 입력 모두를 처리할 수 있는 유연성을 갖추고 있으며, 전역 일관성과 상세한 외관 모델링을 제공합니다.


---

*Generated on 2025-09-24 05:05:10*