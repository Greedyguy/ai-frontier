<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:25:04.812023",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Object Shape and Pose Estimation",
    "Category-Level Object Priors",
    "Semantic Keypoints",
    "Linear Active Shape Model",
    "Global Optimality Certificate"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Object Shape and Pose Estimation": 0.78,
    "Category-Level Object Priors": 0.72,
    "Semantic Keypoints": 0.77,
    "Linear Active Shape Model": 0.7,
    "Global Optimality Certificate": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Object Shape and Pose Estimation",
        "canonical": "Object Shape and Pose Estimation",
        "aliases": [
          "Shape and Pose Estimation"
        ],
        "category": "unique_technical",
        "rationale": "This is a central concept of the paper, providing a specific focus on estimating object shape and pose in robotics.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Category-Level Object Priors",
        "canonical": "Category-Level Object Priors",
        "aliases": [
          "Object Priors"
        ],
        "category": "unique_technical",
        "rationale": "This concept is crucial for understanding the method's reliance on prior information about object categories.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Semantic Keypoints",
        "canonical": "Semantic Keypoints",
        "aliases": [
          "Keypoints"
        ],
        "category": "specific_connectable",
        "rationale": "Semantic keypoints are essential for linking to methods in computer vision and robotics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Linear Active Shape Model",
        "canonical": "Linear Active Shape Model",
        "aliases": [
          "Active Shape Model"
        ],
        "category": "unique_technical",
        "rationale": "This model is a specific technique used in the paper, relevant for shape representation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.7
      },
      {
        "surface": "Global Optimality Certificate",
        "canonical": "Global Optimality Certificate",
        "aliases": [
          "Optimality Certificate"
        ],
        "category": "unique_technical",
        "rationale": "This concept is key to understanding the method's efficiency and reliability.",
        "novelty_score": 0.68,
        "connectivity_score": 0.5,
        "specificity_score": 0.82,
        "link_intent_score": 0.65
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
      "candidate_surface": "Object Shape and Pose Estimation",
      "resolved_canonical": "Object Shape and Pose Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Category-Level Object Priors",
      "resolved_canonical": "Category-Level Object Priors",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Semantic Keypoints",
      "resolved_canonical": "Semantic Keypoints",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Linear Active Shape Model",
      "resolved_canonical": "Linear Active Shape Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Global Optimality Certificate",
      "resolved_canonical": "Global Optimality Certificate",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.5,
        "specificity": 0.82,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Category-Level Object Shape and Pose Estimation in Less Than a Millisecond

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18979.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18979](https://arxiv.org/abs/2509.18979)

## 🔗 유사한 논문
- [[2025-09-23/Emergent 3D Correspondence from Neural Shape Representation_20250923|Emergent 3D Correspondence from Neural Shape Representation]] (82.7% similar)
- [[2025-09-22/Sparse Multiview Open-Vocabulary 3D Detection_20250922|Sparse Multiview Open-Vocabulary 3D Detection]] (81.7% similar)
- [[2025-09-23/Domain Adaptive Object Detection for Space Applications with Real-Time Constraints_20250923|Domain Adaptive Object Detection for Space Applications with Real-Time Constraints]] (81.5% similar)
- [[2025-09-22/Recovering Parametric Scenes from Very Few Time-of-Flight Pixels_20250922|Recovering Parametric Scenes from Very Few Time-of-Flight Pixels]] (81.2% similar)
- [[2025-09-24/An Analysis of Kalman Filter based Object Tracking Methods for Fast-Moving Tiny Objects_20250924|An Analysis of Kalman Filter based Object Tracking Methods for Fast-Moving Tiny Objects]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Semantic Keypoints|Semantic Keypoints]]
**⚡ Unique Technical**: [[keywords/Object Shape and Pose Estimation|Object Shape and Pose Estimation]], [[keywords/Category-Level Object Priors|Category-Level Object Priors]], [[keywords/Linear Active Shape Model|Linear Active Shape Model]], [[keywords/Global Optimality Certificate|Global Optimality Certificate]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18979v1 Announce Type: cross 
Abstract: Object shape and pose estimation is a foundational robotics problem, supporting tasks from manipulation to scene understanding and navigation. We present a fast local solver for shape and pose estimation which requires only category-level object priors and admits an efficient certificate of global optimality. Given an RGB-D image of an object, we use a learned front-end to detect sparse, category-level semantic keypoints on the target object. We represent the target object's unknown shape using a linear active shape model and pose a maximum a posteriori optimization problem to solve for position, orientation, and shape simultaneously. Expressed in unit quaternions, this problem admits first-order optimality conditions in the form of an eigenvalue problem with eigenvector nonlinearities. Our primary contribution is to solve this problem efficiently with self-consistent field iteration, which only requires computing a 4-by-4 matrix and finding its minimum eigenvalue-vector pair at each iterate. Solving a linear system for the corresponding Lagrange multipliers gives a simple global optimality certificate. One iteration of our solver runs in about 100 microseconds, enabling fast outlier rejection. We test our method on synthetic data and a variety of real-world settings, including two public datasets and a drone tracking scenario. Code is released at https://github.com/MIT-SPARK/Fast-ShapeAndPose.

## 📝 요약

이 논문은 로봇 공학에서 중요한 문제인 객체의 형태와 자세 추정을 위한 빠른 지역 해법을 제안합니다. 이 방법은 카테고리 수준의 객체 사전 정보만을 필요로 하며, 전역 최적성의 효율적인 증명을 제공합니다. RGB-D 이미지를 기반으로 학습된 전면부를 사용해 객체의 희소한 의미론적 키포인트를 감지하고, 선형 활성 형태 모델을 통해 객체의 미지의 형태를 표현합니다. 이 문제는 단위 사원수로 표현되어 고유값 문제로 변환되며, 자기 일관 필드 반복을 통해 효율적으로 해결됩니다. 이 과정은 4x4 행렬의 최소 고유값-벡터 쌍을 찾는 것으로 간단한 전역 최적성 증명을 제공합니다. 제안된 해법은 약 100마이크로초 내에 실행되며, 다양한 실제 환경에서 테스트되었습니다. 코드도 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 본 연구는 객체의 형태와 자세 추정을 위한 빠른 지역 해법을 제시하며, 이는 범주 수준의 객체 사전 정보만을 필요로 하고 효율적인 전역 최적성 증명을 허용합니다.
- 2. RGB-D 이미지를 사용하여 대상 객체의 범주 수준의 의미론적 키포인트를 감지하는 학습된 프론트엔드를 활용합니다.
- 3. 대상 객체의 미지의 형태를 선형 활성 형태 모델로 표현하고, 위치, 방향, 형태를 동시에 해결하기 위한 최대 사후 확률 최적화 문제를 제시합니다.
- 4. 본 연구의 주요 기여는 자기 일관성 필드 반복을 통해 문제를 효율적으로 해결하는 것으로, 각 반복마다 4x4 행렬을 계산하고 최소 고유값-벡터 쌍을 찾는 것만 필요합니다.
- 5. 제안된 방법은 약 100마이크로초 내에 한 번의 반복을 수행하여 빠른 이상치 제거를 가능하게 하며, 다양한 실제 환경에서 테스트되었습니다.


---

*Generated on 2025-09-24 16:25:04*