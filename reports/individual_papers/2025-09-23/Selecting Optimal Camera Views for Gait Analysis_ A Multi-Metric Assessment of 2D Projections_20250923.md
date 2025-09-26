---
keywords:
  - 2D Gait Analysis
  - 3D Motion Capture
  - Dynamic Time Warping
  - Kullback-Leibler Divergence
  - Information Entropy
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17805
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:04:02.012168",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "2D Gait Analysis",
    "3D Motion Capture",
    "Dynamic Time Warping",
    "Kullback-Leibler Divergence",
    "Information Entropy"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "2D Gait Analysis": 0.78,
    "3D Motion Capture": 0.85,
    "Dynamic Time Warping": 0.8,
    "Kullback-Leibler Divergence": 0.77,
    "Information Entropy": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "2D markerless gait analysis",
        "canonical": "2D Gait Analysis",
        "aliases": [
          "markerless gait analysis",
          "2D gait assessment"
        ],
        "category": "unique_technical",
        "rationale": "This term is specific to the study of gait using 2D projections and is central to the paper's focus.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "3D motion capture",
        "canonical": "3D Motion Capture",
        "aliases": [
          "3D capture",
          "motion capture"
        ],
        "category": "broad_technical",
        "rationale": "3D motion capture is a well-established technique that provides a reference point for the paper's analysis.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Dynamic Time Warping",
        "canonical": "Dynamic Time Warping",
        "aliases": [
          "DTW"
        ],
        "category": "specific_connectable",
        "rationale": "DTW is a key metric used in the paper for temporal alignment and is widely applicable in time series analysis.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Kullback-Leibler Divergence",
        "canonical": "Kullback-Leibler Divergence",
        "aliases": [
          "KLD"
        ],
        "category": "specific_connectable",
        "rationale": "KLD is a statistical measure used in the paper to assess distribution differences, relevant in various analytical contexts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Information Entropy",
        "canonical": "Information Entropy",
        "aliases": [
          "Entropy"
        ],
        "category": "specific_connectable",
        "rationale": "Information Entropy is used in the paper to evaluate complexity, a concept with broad applicability in information theory.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "camera view",
      "pose estimation",
      "statistical differences"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "2D markerless gait analysis",
      "resolved_canonical": "2D Gait Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "3D motion capture",
      "resolved_canonical": "3D Motion Capture",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Dynamic Time Warping",
      "resolved_canonical": "Dynamic Time Warping",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Kullback-Leibler Divergence",
      "resolved_canonical": "Kullback-Leibler Divergence",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Information Entropy",
      "resolved_canonical": "Information Entropy",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Selecting Optimal Camera Views for Gait Analysis: A Multi-Metric Assessment of 2D Projections

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17805.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17805](https://arxiv.org/abs/2509.17805)

## 🔗 유사한 논문
- [[2025-09-23/Explainable Gait Abnormality Detection Using Dual-Dataset CNN-LSTM Models_20250923|Explainable Gait Abnormality Detection Using Dual-Dataset CNN-LSTM Models]] (81.4% similar)
- [[2025-09-18/Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction_20250918|Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction]] (80.7% similar)
- [[2025-09-19/Cam-2-Cam_ Exploring the Design Space of Dual-Camera Interactions for Smartphone-based Augmented Reality_20250919|Cam-2-Cam: Exploring the Design Space of Dual-Camera Interactions for Smartphone-based Augmented Reality]] (79.9% similar)
- [[2025-09-18/MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (79.2% similar)
- [[2025-09-22/RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes_20250922|RGB-Only Supervised Camera Parameter Optimization in Dynamic Scenes]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/3D Motion Capture|3D Motion Capture]]
**🔗 Specific Connectable**: [[keywords/Dynamic Time Warping|Dynamic Time Warping]], [[keywords/Kullback-Leibler Divergence|Kullback-Leibler Divergence]], [[keywords/Information Entropy|Information Entropy]]
**⚡ Unique Technical**: [[keywords/2D Gait Analysis|2D Gait Analysis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17805v1 Announce Type: new 
Abstract: Objective: To systematically quantify the effect of the camera view (frontal vs. lateral) on the accuracy of 2D markerless gait analysis relative to 3D motion capture ground truth. Methods: Gait data from 18 subjects were recorded simultaneously using frontal, lateral and 3D motion capture systems. Pose estimation used YOLOv8. Four metrics were assessed to evaluate agreement: Dynamic Time Warping (DTW) for temporal alignment, Maximum Cross-Correlation (MCC) for signal similarity, Kullback-Leibler Divergence (KLD) for distribution differences, and Information Entropy (IE) for complexity. Wilcoxon signed-rank tests (significance: $p < 0.05$) and Cliff's delta ($\delta$) were used to measure statistical differences and effect sizes. Results: Lateral views significantly outperformed frontal views for sagittal plane kinematics: step length (DTW: $53.08 \pm 24.50$ vs. $69.87 \pm 25.36$, $p = 0.005$) and knee rotation (DTW: $106.46 \pm 38.57$ vs. $155.41 \pm 41.77$, $p = 0.004$). Frontal views were superior for symmetry parameters: trunk rotation (KLD: $0.09 \pm 0.06$ vs. $0.30 \pm 0.19$, $p < 0.001$) and wrist-to-hipmid distance (MCC: $105.77 \pm 29.72$ vs. $75.20 \pm 20.38$, $p = 0.003$). Effect sizes were medium-to-large ($\delta: 0.34$--$0.76$). Conclusion: Camera view critically impacts gait parameter accuracy. Lateral views are optimal for sagittal kinematics; frontal views excel for trunk symmetry. Significance: This first systematic evidence enables data-driven camera deployment in 2D gait analysis, enhancing clinical utility. Future implementations should leverage both views via disease-oriented setups.

## 📝 요약

이 연구는 2D 마커리스 보행 분석에서 카메라 시야(정면 vs. 측면)가 3D 모션 캡처와 비교하여 정확성에 미치는 영향을 체계적으로 분석했습니다. 18명의 피험자 데이터를 YOLOv8을 사용하여 분석했으며, 동적 시간 왜곡(DTW), 최대 상관(MCC), 쿨백-라이블러 발산(KLD), 정보 엔트로피(IE) 등의 지표를 통해 평가했습니다. 결과적으로, 측면 시야는 시상면 운동학에서 우수한 성능을 보였고, 정면 시야는 대칭성 파라미터에서 더 나은 결과를 나타냈습니다. 이러한 연구는 2D 보행 분석에서 카메라 배치의 중요성을 강조하며, 임상적 활용성을 높이는 데 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. 측면 카메라 뷰는 시상면 운동학에서 정면 카메라 뷰보다 유의미하게 우수한 성능을 보였습니다.
- 2. 정면 카메라 뷰는 몸통 회전과 같은 대칭성 파라미터에서 측면 뷰보다 더 나은 결과를 나타냈습니다.
- 3. 카메라 뷰는 보행 분석의 정확성에 중요한 영향을 미치며, 시상면 운동학에는 측면 뷰가, 몸통 대칭성에는 정면 뷰가 최적입니다.
- 4. 이 연구는 2D 보행 분석에서 데이터 기반의 카메라 배치를 가능하게 하여 임상적 유용성을 향상시킵니다.
- 5. 향후 구현에서는 질병 지향적 설정을 통해 두 가지 뷰를 모두 활용하는 것이 권장됩니다.


---

*Generated on 2025-09-24 05:04:02*