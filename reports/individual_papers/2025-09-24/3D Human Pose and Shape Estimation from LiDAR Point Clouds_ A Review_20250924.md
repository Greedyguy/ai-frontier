<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:34:00.221149",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Human Pose Estimation",
    "Human Mesh Recovery",
    "LiDAR Point Clouds",
    "Evaluation Metrics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Human Pose Estimation": 0.8,
    "Human Mesh Recovery": 0.78,
    "LiDAR Point Clouds": 0.75,
    "Evaluation Metrics": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D human pose estimation",
        "canonical": "3D Human Pose Estimation",
        "aliases": [
          "3D pose estimation",
          "human pose estimation"
        ],
        "category": "unique_technical",
        "rationale": "This is a core technical term specific to the field of computer vision and LiDAR applications.",
        "novelty_score": 0.75,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "human mesh recovery",
        "canonical": "Human Mesh Recovery",
        "aliases": [
          "mesh recovery",
          "3D mesh recovery"
        ],
        "category": "unique_technical",
        "rationale": "It represents a specific task in reconstructing human shapes from point clouds, crucial for linking related studies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "LiDAR point clouds",
        "canonical": "LiDAR Point Clouds",
        "aliases": [
          "LiDAR data",
          "point clouds"
        ],
        "category": "broad_technical",
        "rationale": "LiDAR point clouds are fundamental data types in 3D modeling and computer vision, connecting to a wide range of applications.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "evaluation metrics",
        "canonical": "Evaluation Metrics",
        "aliases": [
          "metrics",
          "performance metrics"
        ],
        "category": "specific_connectable",
        "rationale": "Standardized metrics are essential for comparing methods, facilitating connections across different studies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "comparison"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D human pose estimation",
      "resolved_canonical": "3D Human Pose Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "human mesh recovery",
      "resolved_canonical": "Human Mesh Recovery",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "LiDAR point clouds",
      "resolved_canonical": "LiDAR Point Clouds",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "evaluation metrics",
      "resolved_canonical": "Evaluation Metrics",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# 3D Human Pose and Shape Estimation from LiDAR Point Clouds: A Review

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.12197.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.12197](https://arxiv.org/abs/2509.12197)

## 🔗 유사한 논문
- [[2025-09-23/PoseBench3D_ A Cross-Dataset Analysis Framework for 3D Human Pose Estimation via Pose Lifting Networks_20250923|PoseBench3D: A Cross-Dataset Analysis Framework for 3D Human Pose Estimation via Pose Lifting Networks]] (86.4% similar)
- [[2025-09-24/RS3DBench_ A Comprehensive Benchmark for 3D Spatial Perception in Remote Sensing_20250924|RS3DBench: A Comprehensive Benchmark for 3D Spatial Perception in Remote Sensing]] (81.2% similar)
- [[2025-09-19/Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (80.7% similar)
- [[2025-09-23/L2M-Reg_ Building-level Uncertainty-aware Registration of Outdoor LiDAR Point Clouds and Semantic 3D City Models_20250923|L2M-Reg: Building-level Uncertainty-aware Registration of Outdoor LiDAR Point Clouds and Semantic 3D City Models]] (80.4% similar)
- [[2025-09-24/Towards Robust LiDAR Localization_ Deep Learning-based Uncertainty Estimation_20250924|Towards Robust LiDAR Localization: Deep Learning-based Uncertainty Estimation]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/LiDAR Point Clouds|LiDAR Point Clouds]]
**🔗 Specific Connectable**: [[keywords/Evaluation Metrics|Evaluation Metrics]]
**⚡ Unique Technical**: [[keywords/3D Human Pose Estimation|3D Human Pose Estimation]], [[keywords/Human Mesh Recovery|Human Mesh Recovery]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12197v2 Announce Type: replace 
Abstract: In this paper, we present a comprehensive review of 3D human pose estimation and human mesh recovery from in-the-wild LiDAR point clouds. We compare existing approaches across several key dimensions, and propose a structured taxonomy to classify these methods. Following this taxonomy, we analyze each method's strengths, limitations, and design choices. In addition, (i) we perform a quantitative comparison of the three most widely used datasets, detailing their characteristics; (ii) we compile unified definitions of all evaluation metrics; and (iii) we establish benchmark tables for both tasks on these datasets to enable fair comparisons and promote progress in the field. We also outline open challenges and research directions critical for advancing LiDAR-based 3D human understanding. Moreover, we maintain an accompanying webpage that organizes papers according to our taxonomy and continuously update it with new studies: https://github.com/valeoai/3D-Human-Pose-Shape-Estimation-from-LiDAR

## 📝 요약

이 논문은 야외 LiDAR 포인트 클라우드에서 3D 인간 자세 추정 및 인간 메쉬 복구에 대한 포괄적인 리뷰를 제공합니다. 기존 접근 방식을 여러 차원에서 비교하고, 이를 분류하기 위한 체계적인 분류법을 제안합니다. 각 방법의 강점과 한계, 설계 선택을 분석하며, 세 가지 주요 데이터셋의 정량적 비교, 평가 지표의 통일된 정의, 벤치마크 테이블을 제시하여 공정한 비교와 연구 발전을 도모합니다. 또한, LiDAR 기반 3D 인간 이해를 위한 연구 방향과 과제를 제시하고, 관련 논문을 체계적으로 정리한 웹페이지를 운영합니다.

## 🎯 주요 포인트

- 1. 본 논문은 야외 LiDAR 포인트 클라우드에서 3D 인간 자세 추정 및 인간 메쉬 복구에 대한 포괄적인 리뷰를 제공합니다.
- 2. 기존 접근 방식을 여러 주요 차원에서 비교하고, 이를 분류하기 위한 체계적인 분류법을 제안합니다.
- 3. 세 가지 널리 사용되는 데이터셋의 특성을 상세히 설명하며 정량적 비교를 수행합니다.
- 4. 모든 평가 지표의 통일된 정의를 수집하고, 데이터셋에 대한 벤치마크 테이블을 설정하여 공정한 비교와 분야의 발전을 촉진합니다.
- 5. LiDAR 기반 3D 인간 이해를 발전시키기 위한 개방형 과제와 연구 방향을 제시합니다.


---

*Generated on 2025-09-24 16:34:00*