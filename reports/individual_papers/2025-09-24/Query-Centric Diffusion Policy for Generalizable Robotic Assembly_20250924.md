<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:11:58.596252",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Query-centric Diffusion Policy",
    "Robotic Assembly",
    "Point Cloud Observations",
    "Hierarchical Framework"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Query-centric Diffusion Policy": 0.8,
    "Robotic Assembly": 0.85,
    "Point Cloud Observations": 0.78,
    "Hierarchical Framework": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Query-centric Diffusion Policy",
        "canonical": "Query-centric Diffusion Policy",
        "aliases": [
          "QDP"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel hierarchical framework proposed in the paper, crucial for linking specific research on robotic assembly.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Robotic Assembly",
        "canonical": "Robotic Assembly",
        "aliases": [
          "Assembly Task"
        ],
        "category": "specific_connectable",
        "rationale": "A key application area in robotics, linking to research on automation and machine learning in physical tasks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Point Cloud Observations",
        "canonical": "Point Cloud Observations",
        "aliases": [
          "Point Cloud Data"
        ],
        "category": "specific_connectable",
        "rationale": "Critical for linking to computer vision and 3D data processing in robotics.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hierarchical Framework",
        "canonical": "Hierarchical Framework",
        "aliases": [
          "Hierarchical Policy"
        ],
        "category": "broad_technical",
        "rationale": "A common structure in robotics and AI, linking to broader discussions on multi-level decision-making systems.",
        "novelty_score": 0.45,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "high-level planning",
      "low-level control",
      "skill precision",
      "long-horizon success rate"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Query-centric Diffusion Policy",
      "resolved_canonical": "Query-centric Diffusion Policy",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Robotic Assembly",
      "resolved_canonical": "Robotic Assembly",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Point Cloud Observations",
      "resolved_canonical": "Point Cloud Observations",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hierarchical Framework",
      "resolved_canonical": "Hierarchical Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Query-Centric Diffusion Policy for Generalizable Robotic Assembly

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18686.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18686](https://arxiv.org/abs/2509.18686)

## 🔗 유사한 논문
- [[2025-09-24/PEEK_ Guiding and Minimal Image Representations for Zero-Shot Generalization of Robot Manipulation Policies_20250924|PEEK: Guiding and Minimal Image Representations for Zero-Shot Generalization of Robot Manipulation Policies]] (83.8% similar)
- [[2025-09-18/PRISM-DP_ Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking_20250918|PRISM-DP: Spatial Pose-based Observations for Diffusion-Policies via Segmentation, Mesh Generation, and Pose Tracking]] (83.4% similar)
- [[2025-09-22/GP3_ A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation_20250922|GP3: A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation]] (83.4% similar)
- [[2025-09-24/VGGT-DP_ Generalizable Robot Control via Vision Foundation Models_20250924|VGGT-DP: Generalizable Robot Control via Vision Foundation Models]] (83.0% similar)
- [[2025-09-19/M4Diffuser_ Multi-View Diffusion Policy with Manipulability-Aware Control for Robust Mobile Manipulation_20250919|M4Diffuser: Multi-View Diffusion Policy with Manipulability-Aware Control for Robust Mobile Manipulation]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Hierarchical Framework|Hierarchical Framework]]
**🔗 Specific Connectable**: [[keywords/Robotic Assembly|Robotic Assembly]], [[keywords/Point Cloud Observations|Point Cloud Observations]]
**⚡ Unique Technical**: [[keywords/Query-centric Diffusion Policy|Query-centric Diffusion Policy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18686v1 Announce Type: cross 
Abstract: The robotic assembly task poses a key challenge in building generalist robots due to the intrinsic complexity of part interactions and the sensitivity to noise perturbations in contact-rich settings. The assembly agent is typically designed in a hierarchical manner: high-level multi-part reasoning and low-level precise control. However, implementing such a hierarchical policy is challenging in practice due to the mismatch between high-level skill queries and low-level execution. To address this, we propose the Query-centric Diffusion Policy (QDP), a hierarchical framework that bridges high-level planning and low-level control by utilizing queries comprising objects, contact points, and skill information. QDP introduces a query-centric mechanism that identifies task-relevant components and uses them to guide low-level policies, leveraging point cloud observations to improve the policy's robustness. We conduct comprehensive experiments on the FurnitureBench in both simulation and real-world settings, demonstrating improved performance in skill precision and long-horizon success rate. In the challenging insertion and screwing tasks, QDP improves the skill-wise success rate by over 50% compared to baselines without structured queries.

## 📝 요약

이 논문은 로봇 조립 작업의 복잡성과 소음에 민감한 환경에서의 문제를 해결하기 위해 계층적 정책을 제안합니다. 기존의 고수준 계획과 저수준 제어 간의 불일치를 해결하기 위해, 저자들은 Query-centric Diffusion Policy(QDP)를 개발했습니다. QDP는 객체, 접촉 지점, 기술 정보를 포함하는 쿼리를 활용하여 고수준 계획과 저수준 제어를 연결합니다. 이를 통해 정책의 견고성을 향상시키고, 포인트 클라우드 관찰을 활용하여 저수준 정책을 안내합니다. 실험 결과, QDP는 시뮬레이션 및 실제 환경에서 기술의 정밀도와 장기 성공률을 크게 향상시켰으며, 특히 삽입 및 나사 조립 작업에서 기술 성공률을 50% 이상 개선했습니다.

## 🎯 주요 포인트

- 1. 로봇 조립 작업은 부품 상호작용의 복잡성과 접촉이 많은 환경에서의 노이즈 민감성 때문에 일반 로봇 개발에 중요한 도전 과제입니다.
- 2. QDP(Query-centric Diffusion Policy)는 객체, 접점, 기술 정보를 포함하는 쿼리를 활용하여 고수준 계획과 저수준 제어를 연결하는 계층적 프레임워크입니다.
- 3. QDP는 쿼리 중심 메커니즘을 도입하여 작업 관련 요소를 식별하고 이를 사용하여 저수준 정책을 안내하며, 포인트 클라우드 관찰을 활용하여 정책의 강인성을 향상시킵니다.
- 4. FurnitureBench에서의 실험 결과, QDP는 기술 정밀도와 장기 성공률에서 개선된 성능을 보여주었습니다.
- 5. 특히 삽입 및 나사 조립 작업에서 QDP는 구조화된 쿼리가 없는 기준선에 비해 기술별 성공률을 50% 이상 향상시켰습니다.


---

*Generated on 2025-09-24 15:11:58*