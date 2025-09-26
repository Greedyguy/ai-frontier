---
keywords:
  - Persistence Spheres
  - Persistence Diagrams
  - Wasserstein Distance
  - Functional Data Analysis
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16999
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:45:44.568230",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Persistence Spheres",
    "Persistence Diagrams",
    "Wasserstein Distance",
    "Functional Data Analysis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Persistence Spheres": 0.78,
    "Persistence Diagrams": 0.8,
    "Wasserstein Distance": 0.77,
    "Functional Data Analysis": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "persistence spheres",
        "canonical": "Persistence Spheres",
        "aliases": [
          "bi-continuous representations",
          "functional representation of persistence diagrams"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel representation method that enhances stability and geometric fidelity in persistence diagram analysis.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "persistence diagrams",
        "canonical": "Persistence Diagrams",
        "aliases": [
          "PDs"
        ],
        "category": "specific_connectable",
        "rationale": "A fundamental concept in topological data analysis, crucial for understanding the context of the paper.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "1-Wasserstein distance",
        "canonical": "Wasserstein Distance",
        "aliases": [
          "1-Wasserstein metric"
        ],
        "category": "specific_connectable",
        "rationale": "Key metric for measuring stability and geometric fidelity in persistence diagrams.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "functional data",
        "canonical": "Functional Data Analysis",
        "aliases": [
          "FDA"
        ],
        "category": "broad_technical",
        "rationale": "Relevant to the application domain of the proposed method, linking to broader data analysis techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "task"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "persistence spheres",
      "resolved_canonical": "Persistence Spheres",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "persistence diagrams",
      "resolved_canonical": "Persistence Diagrams",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "1-Wasserstein distance",
      "resolved_canonical": "Wasserstein Distance",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "functional data",
      "resolved_canonical": "Functional Data Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Persistence Spheres: Bi-continuous Representations of Persistence Diagrams

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16999.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16999](https://arxiv.org/abs/2509.16999)

## 🔗 유사한 논문
- [[2025-09-18/Robust Barycenters of Persistence Diagrams_20250918|Robust Barycenters of Persistence Diagrams]] (83.7% similar)
- [[2025-09-22/Cosmology with Persistent Homology_ Parameter Inference via Machine Learning_20250922|Cosmology with Persistent Homology: Parameter Inference via Machine Learning]] (80.0% similar)
- [[2025-09-22/Kuramoto Orientation Diffusion Models_20250922|Kuramoto Orientation Diffusion Models]] (78.1% similar)
- [[2025-09-19/Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data_20250919|Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data]] (77.2% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (77.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Functional Data Analysis|Functional Data Analysis]]
**🔗 Specific Connectable**: [[keywords/Persistence Diagrams|Persistence Diagrams]], [[keywords/Wasserstein Distance|Wasserstein Distance]]
**⚡ Unique Technical**: [[keywords/Persistence Spheres|Persistence Spheres]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16999v1 Announce Type: new 
Abstract: We introduce persistence spheres, a novel functional representation of persistence diagrams. Unlike existing embeddings (such as persistence images, landscapes, or kernel methods), persistence spheres provide a bi-continuous mapping: they are Lipschitz continuous with respect to the 1-Wasserstein distance and admit a continuous inverse on their image. This ensures, in a theoretically optimal way, both stability and geometric fidelity, making persistence spheres the representation that most closely mirrors the Wasserstein geometry of PDs in linear space. We derive explicit formulas for persistence spheres, showing that they can be computed efficiently and parallelized with minimal overhead. Empirically, we evaluate them on diverse regression and classification tasks involving functional data, time series, graphs, meshes, and point clouds. Across these benchmarks, persistence spheres consistently deliver state-of-the-art or competitive performance compared to persistence images, persistence landscapes, and the sliced Wasserstein kernel.

## 📝 요약

이 논문은 새로운 지속성 다이어그램 표현 방식인 '지속성 구'를 소개합니다. 지속성 구는 1-Wasserstein 거리와 관련하여 Lipschitz 연속성을 가지며, 그 이미지에 대해 연속적인 역함수를 허용합니다. 이는 이론적으로 최적의 안정성과 기하학적 충실도를 보장하여, 지속성 다이어그램의 Wasserstein 기하학을 선형 공간에서 가장 잘 반영합니다. 지속성 구의 명시적 공식이 제시되며, 효율적이고 병렬화가 용이하게 계산될 수 있음을 보여줍니다. 다양한 회귀 및 분류 작업에서 지속성 구는 지속성 이미지, 지속성 랜드스케이프, 슬라이스드 Wasserstein 커널과 비교하여 일관되게 최첨단 또는 경쟁력 있는 성능을 제공합니다.

## 🎯 주요 포인트

- 1. 지속성 구체(persistence spheres)는 지속성 다이어그램의 새로운 기능적 표현으로, 1-Wasserstein 거리와 관련하여 Lipschitz 연속성을 가지며, 이미지에 대한 연속 역함수를 허용하는 양방향 연속 매핑을 제공합니다.
- 2. 지속성 구체는 지속성 다이어그램의 Wasserstein 기하학을 선형 공간에서 가장 잘 반영하는 표현으로, 이론적으로 최적의 안정성과 기하학적 충실도를 보장합니다.
- 3. 지속성 구체의 명시적 공식은 효율적으로 계산할 수 있으며, 최소한의 오버헤드로 병렬화가 가능합니다.
- 4. 다양한 기능적 데이터, 시계열, 그래프, 메시, 점 구름을 포함한 회귀 및 분류 작업에서 지속성 구체는 지속성 이미지, 지속성 랜드스케이프, 슬라이스드 Wasserstein 커널과 비교하여 일관되게 최첨단 또는 경쟁력 있는 성능을 제공합니다.


---

*Generated on 2025-09-24 01:45:44*