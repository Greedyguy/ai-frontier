---
keywords:
  - 3D Human Mesh Recovery
  - Amputated Joint Aware
  - Synthetic Dataset
  - Pose Estimation
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19939
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:53:57.913732",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Human Mesh Recovery",
    "Amputated Joint Aware",
    "Synthetic Dataset",
    "Pose Estimation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Human Mesh Recovery": 0.78,
    "Amputated Joint Aware": 0.8,
    "Synthetic Dataset": 0.7,
    "Pose Estimation": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Human Mesh Recovery",
        "canonical": "3D Human Mesh Recovery",
        "aliases": [
          "3D Mesh Reconstruction",
          "Human Mesh Recovery"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a specialized process in computer vision, crucial for linking to related research on human pose estimation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Amputated Joint Aware",
        "canonical": "Amputated Joint Aware",
        "aliases": [
          "AJAHR"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach specifically addressing the challenge of mesh recovery for individuals with limb loss.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Synthetic Dataset",
        "canonical": "Synthetic Dataset",
        "aliases": [
          "Simulated Dataset"
        ],
        "category": "broad_technical",
        "rationale": "Synthetic datasets are widely used in machine learning for training models, making this a valuable link to data generation techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "Pose Estimation",
        "canonical": "Pose Estimation",
        "aliases": [
          "Human Pose Estimation"
        ],
        "category": "specific_connectable",
        "rationale": "Pose estimation is a key component of the proposed method, linking it to a broader field of study within computer vision.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Human Mesh Recovery",
      "resolved_canonical": "3D Human Mesh Recovery",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Amputated Joint Aware",
      "resolved_canonical": "Amputated Joint Aware",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Synthetic Dataset",
      "resolved_canonical": "Synthetic Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Pose Estimation",
      "resolved_canonical": "Pose Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# AJAHR: Amputated Joint Aware 3D Human Mesh Recovery

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19939.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19939](https://arxiv.org/abs/2509.19939)

## 🔗 유사한 논문
- [[2025-09-23/PoseBench3D_ A Cross-Dataset Analysis Framework for 3D Human Pose Estimation via Pose Lifting Networks_20250923|PoseBench3D: A Cross-Dataset Analysis Framework for 3D Human Pose Estimation via Pose Lifting Networks]] (83.5% similar)
- [[2025-09-23/DynSTG-Mamba_ Dynamic Spatio-Temporal Graph Mamba with Cross-Graph Knowledge Distillation for Gait Disorders Recognition_20250923|DynSTG-Mamba: Dynamic Spatio-Temporal Graph Mamba with Cross-Graph Knowledge Distillation for Gait Disorders Recognition]] (81.9% similar)
- [[2025-09-24/3D Human Pose and Shape Estimation from LiDAR Point Clouds_ A Review_20250924|3D Human Pose and Shape Estimation from LiDAR Point Clouds: A Review]] (81.6% similar)
- [[2025-09-24/Event-guided 3D Gaussian Splatting for Dynamic Human and Scene Reconstruction_20250924|Event-guided 3D Gaussian Splatting for Dynamic Human and Scene Reconstruction]] (81.4% similar)
- [[2025-09-18/Embracing Bulky Objects with Humanoid Robots_ Whole-Body Manipulation with Reinforcement Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Synthetic Dataset|Synthetic Dataset]]
**🔗 Specific Connectable**: [[keywords/Pose Estimation|Pose Estimation]]
**⚡ Unique Technical**: [[keywords/3D Human Mesh Recovery|3D Human Mesh Recovery]], [[keywords/Amputated Joint Aware|Amputated Joint Aware]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19939v1 Announce Type: cross 
Abstract: Existing human mesh recovery methods assume a standard human body structure, overlooking diverse anatomical conditions such as limb loss. This assumption introduces bias when applied to individuals with amputations - a limitation further exacerbated by the scarcity of suitable datasets. To address this gap, we propose Amputated Joint Aware 3D Human Mesh Recovery (AJAHR), which is an adaptive pose estimation framework that improves mesh reconstruction for individuals with limb loss. Our model integrates a body-part amputation classifier, jointly trained with the mesh recovery network, to detect potential amputations. We also introduce Amputee 3D (A3D), which is a synthetic dataset offering a wide range of amputee poses for robust training. While maintaining competitive performance on non-amputees, our approach achieves state-of-the-art results for amputated individuals. Additional materials can be found at the project webpage.

## 📝 요약

기존의 인간 메쉬 복원 방법은 표준적인 신체 구조를 가정하여, 절단 등의 다양한 해부학적 조건을 간과합니다. 이러한 가정은 절단 장애가 있는 개인에게 적용될 때 편향을 초래하며, 적절한 데이터셋의 부족으로 인해 문제가 더욱 심화됩니다. 이를 해결하기 위해, 우리는 절단 관절 인식 3D 인간 메쉬 복원(AJAHR)을 제안합니다. 이 프레임워크는 절단 장애가 있는 개인의 메쉬 복원을 개선하는 적응형 자세 추정 방법론입니다. 모델은 메쉬 복원 네트워크와 함께 훈련되는 신체 부위 절단 분류기를 통합하여 잠재적인 절단을 감지합니다. 또한, 다양한 절단 장애 포즈를 제공하는 합성 데이터셋인 Amputee 3D (A3D)를 도입하여 강력한 훈련을 지원합니다. 우리의 접근 방식은 비절단자에 대한 경쟁력 있는 성능을 유지하면서, 절단 장애가 있는 개인에 대해 최첨단 결과를 달성합니다. 추가 자료는 프로젝트 웹페이지에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. 기존의 인간 메쉬 복원 방법은 표준적인 신체 구조를 가정하여 절단 장애를 가진 개인에게 편향을 초래한다.
- 2. Amputated Joint Aware 3D Human Mesh Recovery (AJAHR)는 절단 장애인을 위한 메쉬 복원을 개선하는 적응형 자세 추정 프레임워크이다.
- 3. AJAHR 모델은 신체 부위 절단 분류기를 메쉬 복원 네트워크와 공동으로 훈련하여 잠재적인 절단을 감지한다.
- 4. Amputee 3D (A3D)는 다양한 절단 장애인 자세를 제공하는 합성 데이터셋으로, 강력한 훈련을 지원한다.
- 5. 제안된 접근법은 절단 장애인에 대해 최첨단 결과를 달성하면서 비장애인에 대해서도 경쟁력 있는 성능을 유지한다.


---

*Generated on 2025-09-25 15:53:57*