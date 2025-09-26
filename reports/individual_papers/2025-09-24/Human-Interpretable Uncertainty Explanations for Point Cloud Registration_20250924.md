<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:23:47.963989",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Point Cloud Registration",
    "Gaussian Process Concept Attribution",
    "Active Learning",
    "Robotic Perception"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Point Cloud Registration": 0.78,
    "Gaussian Process Concept Attribution": 0.8,
    "Active Learning": 0.75,
    "Robotic Perception": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Point Cloud Registration",
        "canonical": "Point Cloud Registration",
        "aliases": [
          "3D Registration",
          "Cloud Alignment"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific problem in computer vision and robotics, crucial for linking related research on 3D data processing.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Gaussian Process Concept Attribution",
        "canonical": "Gaussian Process Concept Attribution",
        "aliases": [
          "GP-CA"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for explaining uncertainty in registration, connecting to Gaussian processes and interpretability.",
        "novelty_score": 0.82,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "Active Learning",
        "canonical": "Active Learning",
        "aliases": [
          "Query Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Active learning is a well-known technique that enhances model efficiency, relevant for linking to machine learning strategies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.87,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Robotic Perception",
        "canonical": "Robotic Perception",
        "aliases": [
          "Robot Vision"
        ],
        "category": "specific_connectable",
        "rationale": "This connects to research on how robots interpret and understand their environment, crucial for linking to robotics.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "sensor noise",
      "pose-estimation errors",
      "partial overlap"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Point Cloud Registration",
      "resolved_canonical": "Point Cloud Registration",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Gaussian Process Concept Attribution",
      "resolved_canonical": "Gaussian Process Concept Attribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Active Learning",
      "resolved_canonical": "Active Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.87,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Robotic Perception",
      "resolved_canonical": "Robotic Perception",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Human-Interpretable Uncertainty Explanations for Point Cloud Registration

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18786.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18786](https://arxiv.org/abs/2509.18786)

## 🔗 유사한 논문
- [[2025-09-22/GP3_ A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation_20250922|GP3: A 3D Geometry-Aware Policy with Multi-View Images for Robotic Manipulation]] (82.3% similar)
- [[2025-09-22/Kernel Model Validation_ How To Do It, And Why You Should Care_20250922|Kernel Model Validation: How To Do It, And Why You Should Care]] (82.3% similar)
- [[2025-09-22/Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration_20250922|Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration]] (81.7% similar)
- [[2025-09-19/Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data_20250919|Compactly-supported nonstationary kernels for computing exact Gaussian processes on big data]] (81.6% similar)
- [[2025-09-23/Robust, Online, and Adaptive Decentralized Gaussian Processes_20250923|Robust, Online, and Adaptive Decentralized Gaussian Processes]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Active Learning|Active Learning]], [[keywords/Robotic Perception|Robotic Perception]]
**⚡ Unique Technical**: [[keywords/Point Cloud Registration|Point Cloud Registration]], [[keywords/Gaussian Process Concept Attribution|Gaussian Process Concept Attribution]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18786v1 Announce Type: cross 
Abstract: In this paper, we address the point cloud registration problem, where well-known methods like ICP fail under uncertainty arising from sensor noise, pose-estimation errors, and partial overlap due to occlusion. We develop a novel approach, Gaussian Process Concept Attribution (GP-CA), which not only quantifies registration uncertainty but also explains it by attributing uncertainty to well-known sources of errors in registration problems. Our approach leverages active learning to discover new uncertainty sources in the wild by querying informative instances. We validate GP-CA on three publicly available datasets and in our real-world robot experiment. Extensive ablations substantiate our design choices. Our approach outperforms other state-of-the-art methods in terms of runtime, high sample-efficiency with active learning, and high accuracy. Our real-world experiment clearly demonstrates its applicability. Our video also demonstrates that GP-CA enables effective failure-recovery behaviors, yielding more robust robotic perception.

## 📝 요약

이 논문은 센서 노이즈, 자세 추정 오류, 가림으로 인한 부분적 중첩 등으로 인해 기존의 ICP 방법이 실패하는 점군 등록 문제를 다룹니다. 저자들은 등록 불확실성을 정량화하고 설명하는 새로운 접근법인 Gaussian Process Concept Attribution (GP-CA)을 개발했습니다. 이 방법은 능동 학습을 활용하여 정보가 풍부한 사례를 질의함으로써 새로운 불확실성의 원인을 발견합니다. 세 개의 공개 데이터셋과 실제 로봇 실험에서 GP-CA를 검증했으며, 광범위한 실험을 통해 설계 선택의 타당성을 입증했습니다. GP-CA는 실행 시간, 능동 학습을 통한 높은 샘플 효율성, 높은 정확성 측면에서 최신 방법들을 능가하며, 실제 실험에서 그 적용 가능성을 명확히 보여줍니다. 또한, GP-CA는 효과적인 실패 복구 행동을 가능하게 하여 더 견고한 로봇 인식을 제공합니다.

## 🎯 주요 포인트

- 1. GP-CA는 센서 노이즈, 자세 추정 오류, 가림으로 인한 부분적 중첩 등에서 발생하는 불확실성을 정량화하고 설명하는 새로운 방법입니다.
- 2. 능동 학습을 활용하여 새로운 불확실성 원인을 발견하고, 정보가 풍부한 사례를 질의하여 이를 설명합니다.
- 3. 세 가지 공개 데이터셋과 실제 로봇 실험에서 GP-CA의 유효성을 검증하였으며, 설계 선택을 뒷받침하는 광범위한 분석을 수행했습니다.
- 4. GP-CA는 실행 시간, 능동 학습을 통한 높은 샘플 효율성, 높은 정확도 면에서 최신 방법들보다 우수한 성능을 보입니다.
- 5. 실제 실험에서 GP-CA의 적용 가능성을 명확히 보여주며, 실패 복구 행동을 효과적으로 가능하게 하여 더 견고한 로봇 인식을 제공합니다.


---

*Generated on 2025-09-24 16:23:47*