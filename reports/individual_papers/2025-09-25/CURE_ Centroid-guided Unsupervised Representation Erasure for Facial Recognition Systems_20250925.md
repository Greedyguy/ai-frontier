---
keywords:
  - Machine Unlearning
  - Facial Recognition Systems
  - Unsupervised Representation Erasure
  - Unlearning Efficiency Score
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19562
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:59:57.345329",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Unlearning",
    "Facial Recognition Systems",
    "Unsupervised Representation Erasure",
    "Unlearning Efficiency Score"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Unlearning": 0.78,
    "Facial Recognition Systems": 0.8,
    "Unsupervised Representation Erasure": 0.77,
    "Unlearning Efficiency Score": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Unlearning",
        "canonical": "Machine Unlearning",
        "aliases": [
          "Unlearning"
        ],
        "category": "unique_technical",
        "rationale": "Machine Unlearning is a novel concept addressing privacy concerns in AI, crucial for linking privacy-focused research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Facial Recognition Systems",
        "canonical": "Facial Recognition Systems",
        "aliases": [
          "Face Recognition"
        ],
        "category": "broad_technical",
        "rationale": "Facial Recognition Systems are a broad technical area with significant cross-disciplinary connections.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Unsupervised Representation Erasure",
        "canonical": "Unsupervised Representation Erasure",
        "aliases": [
          "Unsupervised Erasure"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique approach within the unlearning domain, enhancing connections to unsupervised learning methods.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      },
      {
        "surface": "Unlearning Efficiency Score",
        "canonical": "Unlearning Efficiency Score",
        "aliases": [
          "UES"
        ],
        "category": "unique_technical",
        "rationale": "A novel metric that can link to discussions on evaluation metrics in AI.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "CURE",
      "quality-aware unlearning"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Unlearning",
      "resolved_canonical": "Machine Unlearning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Facial Recognition Systems",
      "resolved_canonical": "Facial Recognition Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Unsupervised Representation Erasure",
      "resolved_canonical": "Unsupervised Representation Erasure",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Unlearning Efficiency Score",
      "resolved_canonical": "Unlearning Efficiency Score",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# CURE: Centroid-guided Unsupervised Representation Erasure for Facial Recognition Systems

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19562.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19562](https://arxiv.org/abs/2509.19562)

## 🔗 유사한 논문
- [[2025-09-23/An Unlearning Framework for Continual Learning_20250923|An Unlearning Framework for Continual Learning]] (83.8% similar)
- [[2025-09-23/SafeEraser_ Enhancing Safety in Multimodal Large Language Models through Multimodal Machine Unlearning_20250923|SafeEraser: Enhancing Safety in Multimodal Large Language Models through Multimodal Machine Unlearning]] (83.7% similar)
- [[2025-09-19/Towards a Real-World Aligned Benchmark for Unlearning in Recommender Systems_20250919|Towards a Real-World Aligned Benchmark for Unlearning in Recommender Systems]] (83.4% similar)
- [[2025-09-18/CUFG_ Curriculum Unlearning Guided by the Forgetting Gradient_20250918|CUFG: Curriculum Unlearning Guided by the Forgetting Gradient]] (82.5% similar)
- [[2025-09-23/Causal Fuzzing for Verifying Machine Unlearning_20250923|Causal Fuzzing for Verifying Machine Unlearning]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Facial Recognition Systems|Facial Recognition Systems]]
**⚡ Unique Technical**: [[keywords/Machine Unlearning|Machine Unlearning]], [[keywords/Unsupervised Representation Erasure|Unsupervised Representation Erasure]], [[keywords/Unlearning Efficiency Score|Unlearning Efficiency Score]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19562v1 Announce Type: new 
Abstract: In the current digital era, facial recognition systems offer significant utility and have been widely integrated into modern technological infrastructures; however, their widespread use has also raised serious privacy concerns, prompting regulations that mandate data removal upon request. Machine unlearning has emerged as a powerful solution to address this issue by selectively removing the influence of specific user data from trained models while preserving overall model performance. However, existing machine unlearning techniques largely depend on supervised techniques requiring identity labels, which are often unavailable in privacy-constrained situations or in large-scale, noisy datasets. To address this critical gap, we introduce CURE (Centroid-guided Unsupervised Representation Erasure), the first unsupervised unlearning framework for facial recognition systems that operates without the use of identity labels, effectively removing targeted samples while preserving overall performance. We also propose a novel metric, the Unlearning Efficiency Score (UES), which balances forgetting and retention stability, addressing shortcomings in the current evaluation metrics. CURE significantly outperforms unsupervised variants of existing unlearning methods. Additionally, we conducted quality-aware unlearning by designating low-quality images as the forget set, demonstrating its usability and benefits, and highlighting the role of image quality in machine unlearning.

## 📝 요약

현재 디지털 시대에서 얼굴 인식 시스템은 유용성을 제공하지만, 개인정보 보호 문제로 인해 데이터 삭제 요구가 증가하고 있습니다. 이를 해결하기 위해 기계적 언러닝이 등장했지만, 기존 방법은 주로 신원 레이블이 필요한 지도 학습에 의존합니다. 이러한 문제를 해결하기 위해, 우리는 CURE(Centroid-guided Unsupervised Representation Erasure)를 제안합니다. CURE는 신원 레이블 없이 작동하는 최초의 비지도 학습 기반 얼굴 인식 언러닝 프레임워크로, 특정 샘플을 효과적으로 제거하면서도 전체 성능을 유지합니다. 또한, 망각과 보존의 균형을 평가하는 새로운 지표인 언러닝 효율 점수(UES)를 제안하여 기존 평가 지표의 한계를 보완합니다. CURE는 기존 비지도 언러닝 방법보다 뛰어난 성능을 보이며, 저품질 이미지를 망각 세트로 지정하여 이미지 품질의 중요성을 강조합니다.

## 🎯 주요 포인트

- 1. 얼굴 인식 시스템의 확산으로 인한 프라이버시 문제를 해결하기 위해 데이터 삭제를 요구하는 규제가 증가하고 있습니다.
- 2. 기존의 기계 학습 제거 기술은 주로 신원 레이블을 필요로 하는 지도 학습에 의존하지만, 이는 프라이버시 제약 상황이나 대규모 데이터셋에서는 어려움이 있습니다.
- 3. CURE는 신원 레이블 없이 작동하는 최초의 비지도 학습 기반 얼굴 인식 시스템 제거 프레임워크로, 특정 샘플을 효과적으로 제거하면서 전체 성능을 유지합니다.
- 4. 새로운 평가 지표인 Unlearning Efficiency Score (UES)를 제안하여, 현재 평가 지표의 단점을 보완하고 망각과 유지의 안정성을 균형 있게 평가합니다.
- 5. 저품질 이미지를 제거 대상으로 지정하여 품질 인식 제거를 수행함으로써 기계 학습 제거에서 이미지 품질의 중요성을 강조합니다.


---

*Generated on 2025-09-26 08:59:57*