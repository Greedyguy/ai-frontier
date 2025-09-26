---
keywords:
  - Deep Learning
  - Entropy Regularization
  - Autonomous Driving Perception
  - Mutual Information
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16277
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:12:16.368009",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Entropy Regularization",
    "Autonomous Driving Perception",
    "Mutual Information"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Entropy Regularization": 0.78,
    "Autonomous Driving Perception": 0.77,
    "Mutual Information": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep perception networks",
        "canonical": "Deep Learning",
        "aliases": [
          "Deep Neural Networks"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a fundamental concept in the paper, linking to broader technical discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Entropy-based regularizer",
        "canonical": "Entropy Regularization",
        "aliases": [
          "Eloss"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to stabilize information flow, crucial for linking to entropy and regularization topics.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Autonomous driving perception",
        "canonical": "Autonomous Driving Perception",
        "aliases": [
          "Self-driving Car Perception"
        ],
        "category": "specific_connectable",
        "rationale": "Focuses on the application domain, linking to discussions on perception systems in autonomous vehicles.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Mutual information",
        "canonical": "Mutual Information",
        "aliases": [
          "Information Theory"
        ],
        "category": "specific_connectable",
        "rationale": "A key theoretical concept used to ensure stable information flow, linking to information theory discussions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
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
      "candidate_surface": "Deep perception networks",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Entropy-based regularizer",
      "resolved_canonical": "Entropy Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Autonomous driving perception",
      "resolved_canonical": "Autonomous Driving Perception",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Mutual information",
      "resolved_canonical": "Mutual Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Stabilizing Information Flow Entropy: Regularization for Safe and Interpretable Autonomous Driving Perception

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16277.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16277](https://arxiv.org/abs/2509.16277)

## 🔗 유사한 논문
- [[2025-09-22/A re-calibration method for object detection with multi-modal alignment bias in autonomous driving_20250922|A re-calibration method for object detection with multi-modal alignment bias in autonomous driving]] (82.8% similar)
- [[2025-09-22/Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection_20250922|Training More Robust Classification Model via Discriminative Loss and Gaussian Noise Injection]] (81.4% similar)
- [[2025-09-22/DAOcc_ 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction_20250922|DAOcc: 3D Object Detection Assisted Multi-Sensor Fusion for 3D Occupancy Prediction]] (81.1% similar)
- [[2025-09-22/Towards Sharper Object Boundaries in Self-Supervised Depth Estimation_20250922|Towards Sharper Object Boundaries in Self-Supervised Depth Estimation]] (80.8% similar)
- [[2025-09-22/Adversarial generalization of unfolding (model-based) networks_20250922|Adversarial generalization of unfolding (model-based) networks]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Autonomous Driving Perception|Autonomous Driving Perception]], [[keywords/Mutual Information|Mutual Information]]
**⚡ Unique Technical**: [[keywords/Entropy Regularization|Entropy Regularization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16277v1 Announce Type: cross 
Abstract: Deep perception networks in autonomous driving traditionally rely on data-intensive training regimes and post-hoc anomaly detection, often disregarding fundamental information-theoretic constraints governing stable information processing. We reconceptualize deep neural encoders as hierarchical communication chains that incrementally compress raw sensory inputs into task-relevant latent features. Within this framework, we establish two theoretically justified design principles for robust perception: (D1) smooth variation of mutual information between consecutive layers, and (D2) monotonic decay of latent entropy with network depth. Our analysis shows that, under realistic architectural assumptions, particularly blocks comprising repeated layers of similar capacity, enforcing smooth information flow (D1) naturally encourages entropy decay (D2), thus ensuring stable compression. Guided by these insights, we propose Eloss, a novel entropy-based regularizer designed as a lightweight, plug-and-play training objective. Rather than marginal accuracy improvements, this approach represents a conceptual shift: it unifies information-theoretic stability with standard perception tasks, enabling explicit, principled detection of anomalous sensor inputs through entropy deviations. Experimental validation on large-scale 3D object detection benchmarks (KITTI and nuScenes) demonstrates that incorporating Eloss consistently achieves competitive or improved accuracy while dramatically enhancing sensitivity to anomalies, amplifying distribution-shift signals by up to two orders of magnitude. This stable information-compression perspective not only improves interpretability but also establishes a solid theoretical foundation for safer, more robust autonomous driving perception systems.

## 📝 요약

이 논문은 자율주행의 심층 인식 네트워크에서 정보 이론적 제약을 고려한 새로운 접근 방식을 제안합니다. 전통적으로 데이터 집약적 학습과 사후 이상 탐지에 의존하는 대신, 심층 신경 인코더를 계층적 통신 체인으로 재구성하여 원시 센서 입력을 점진적으로 압축합니다. 이를 통해 두 가지 설계 원칙을 제시합니다: (D1) 연속적인 계층 간 상호 정보의 부드러운 변화, (D2) 네트워크 깊이에 따른 잠재 엔트로피의 단조 감소. 이러한 원칙을 기반으로 Eloss라는 새로운 엔트로피 기반 정규화를 제안하며, 이는 정보 이론적 안정성과 표준 인식 작업을 통합하여 이상 센서 입력을 명시적으로 탐지할 수 있게 합니다. 대규모 3D 객체 탐지 벤치마크(KITTI 및 nuScenes) 실험에서는 Eloss가 정확도를 유지하거나 개선하면서도 이상 탐지 민감도를 크게 향상시킴을 보여줍니다. 이 접근 방식은 자율주행 인식 시스템의 안전성과 견고성을 강화하는 이론적 기반을 제공합니다.

## 🎯 주요 포인트

- 1. 자율주행의 심층 인식 네트워크는 정보 이론적 제약을 무시하고 데이터 집중적 훈련과 사후 이상 탐지에 의존해 왔습니다.
- 2. 심층 신경 인코더를 계층적 통신 체인으로 재구성하여 원시 감각 입력을 과제 관련 잠재 특징으로 압축하는 방식을 제안합니다.
- 3. 두 가지 설계 원칙을 제시하며, 연속 계층 간 상호 정보의 부드러운 변화(D1)와 네트워크 깊이에 따른 잠재 엔트로피의 단조 감소(D2)를 강조합니다.
- 4. Eloss라는 새로운 엔트로피 기반 정규화를 제안하여 정보 이론적 안정성과 표준 인식 작업을 통합하고, 이상 센서 입력을 명시적으로 탐지할 수 있게 합니다.
- 5. 대규모 3D 객체 탐지 벤치마크 실험에서 Eloss를 도입하면 정확도가 향상되거나 유지되면서 이상 감지 민감도가 크게 향상됨을 확인했습니다.


---

*Generated on 2025-09-23 23:12:16*