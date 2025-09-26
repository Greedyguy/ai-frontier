---
keywords:
  - 3D Gaussian Splatting
  - Structure from Motion
  - Intermediate View Rendering
  - Feature Matching
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19898
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:09:28.548922",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Gaussian Splatting",
    "Structure from Motion",
    "Intermediate View Rendering",
    "Feature Matching"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Gaussian Splatting": 0.8,
    "Structure from Motion": 0.75,
    "Intermediate View Rendering": 0.78,
    "Feature Matching": 0.7
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
        "rationale": "This technique is central to the paper's approach to rendering scenes and is novel in the context of aerial-ground image integration.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Structure from Motion",
        "canonical": "Structure from Motion",
        "aliases": [
          "SfM"
        ],
        "category": "broad_technical",
        "rationale": "A well-known technique in computer vision for 3D reconstruction, crucial for understanding the paper's methodology.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Intermediate View Rendering",
        "canonical": "Intermediate View Rendering",
        "aliases": [
          "IVR"
        ],
        "category": "unique_technical",
        "rationale": "Key to the paper's contribution in bridging aerial and ground images, enhancing feature matching.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Feature Matching",
        "canonical": "Feature Matching",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A fundamental process in computer vision, central to the paper's proposed solution.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
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
      "candidate_surface": "3D Gaussian Splatting",
      "resolved_canonical": "3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Structure from Motion",
      "resolved_canonical": "Structure from Motion",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Intermediate View Rendering",
      "resolved_canonical": "Intermediate View Rendering",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Feature Matching",
      "resolved_canonical": "Feature Matching",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Aerial-Ground Image Feature Matching via 3D Gaussian Splatting-based Intermediate View Rendering

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19898.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19898](https://arxiv.org/abs/2509.19898)

## 🔗 유사한 논문
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (84.8% similar)
- [[2025-09-23/3D Gaussian Flats_ Hybrid 2D/3D Photometric Scene Reconstruction_20250923|3D Gaussian Flats: Hybrid 2D/3D Photometric Scene Reconstruction]] (83.6% similar)
- [[2025-09-23/Multi-viewregulated gaussian splatting for novel view synthesis_20250923|Multi-viewregulated gaussian splatting for novel view synthesis]] (83.2% similar)
- [[2025-09-19/FMGS-Avatar_ Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction_20250919|FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (83.0% similar)
- [[2025-09-22/SGMAGNet_ A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark_20250922|SGMAGNet: A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Structure from Motion|Structure from Motion]]
**🔗 Specific Connectable**: [[keywords/Feature Matching|Feature Matching]]
**⚡ Unique Technical**: [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]], [[keywords/Intermediate View Rendering|Intermediate View Rendering]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19898v1 Announce Type: new 
Abstract: The integration of aerial and ground images has been a promising solution in 3D modeling of complex scenes, which is seriously restricted by finding reliable correspondences. The primary contribution of this study is a feature matching algorithm for aerial and ground images, whose core idea is to generate intermediate views to alleviate perspective distortions caused by the extensive viewpoint changes. First, by using aerial images only, sparse models are reconstructed through an incremental SfM (Structure from Motion) engine due to their large scene coverage. Second, 3D Gaussian Splatting is then adopted for scene rendering by taking as inputs sparse points and oriented images. For accurate view rendering, a render viewpoint determination algorithm is designed by using the oriented camera poses of aerial images, which is used to generate high-quality intermediate images that can bridge the gap between aerial and ground images. Third, with the aid of intermediate images, reliable feature matching is conducted for match pairs from render-aerial and render-ground images, and final matches can be generated by transmitting correspondences through intermediate views. By using real aerial and ground datasets, the validation of the proposed solution has been verified in terms of feature matching and scene rendering and compared comprehensively with widely used methods. The experimental results demonstrate that the proposed solution can provide reliable feature matches for aerial and ground images with an obvious increase in the number of initial and refined matches, and it can provide enough matches to achieve accurate ISfM reconstruction and complete 3DGS-based scene rendering.

## 📝 요약

이 연구는 항공 및 지상 이미지의 3D 모델링에서 신뢰할 수 있는 대응점을 찾는 문제를 해결하기 위해 새로운 특징 매칭 알고리즘을 제안합니다. 주요 기여는 시점 변화로 인한 왜곡을 줄이기 위해 중간 이미지를 생성하는 것입니다. 먼저, 항공 이미지만을 사용하여 SfM 엔진을 통해 희소 모델을 재구성합니다. 그 후, 3D 가우시안 스플래팅을 사용하여 장면을 렌더링하고, 항공 이미지의 카메라 자세를 활용한 렌더링 시점 결정 알고리즘으로 고품질 중간 이미지를 생성합니다. 이러한 중간 이미지를 통해 항공 및 지상 이미지 간의 신뢰할 수 있는 특징 매칭을 수행하며, 실험 결과 제안된 방법이 초기 및 정제된 매칭 수를 증가시켜 정확한 ISfM 재구성과 3DGS 기반의 장면 렌더링을 가능하게 함을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 연구는 항공 및 지상 이미지의 3D 모델링에서 신뢰할 수 있는 대응점을 찾는 문제를 해결하기 위한 특징 매칭 알고리즘을 제안합니다.
- 2. 중간 뷰 생성을 통해 광범위한 시점 변화로 인한 원근 왜곡을 완화하는 것이 핵심 아이디어입니다.
- 3. 항공 이미지만을 사용하여 대규모 장면 커버리지를 바탕으로 점진적 구조-이동(SfM) 엔진을 통해 희소 모델을 재구성합니다.
- 4. 중간 이미지를 활용하여 항공 및 지상 이미지 간의 신뢰할 수 있는 특징 매칭을 수행하고, 최종 매칭은 중간 뷰를 통해 전달된 대응점을 통해 생성됩니다.
- 5. 제안된 솔루션은 실험 결과를 통해 항공 및 지상 이미지에 대한 신뢰할 수 있는 특징 매칭을 제공하며, 초기 및 정제된 매칭 수의 명확한 증가를 보여줍니다.


---

*Generated on 2025-09-26 09:09:28*