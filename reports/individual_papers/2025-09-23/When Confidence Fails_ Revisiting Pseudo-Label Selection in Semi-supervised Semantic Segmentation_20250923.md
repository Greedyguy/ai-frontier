---
keywords:
  - Confidence Separable Learning
  - Pseudo-label Selection
  - Semantic Segmentation
  - Network Overconfidence
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16704
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:33:07.601806",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Confidence Separable Learning",
    "Pseudo-label Selection",
    "Semantic Segmentation",
    "Network Overconfidence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Confidence Separable Learning": 0.78,
    "Pseudo-label Selection": 0.72,
    "Semantic Segmentation": 0.8,
    "Network Overconfidence": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Confidence Separable Learning",
        "canonical": "Confidence Separable Learning",
        "aliases": [
          "CSL"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to pseudo-label selection in semantic segmentation, enhancing connectivity with related methods.",
        "novelty_score": 0.85,
        "connectivity_score": 0.68,
        "specificity_score": 0.92,
        "link_intent_score": 0.78
      },
      {
        "surface": "Pseudo-label Selection",
        "canonical": "Pseudo-label Selection",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Central to the paper's methodology, linking to broader discussions on label selection in machine learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.81,
        "link_intent_score": 0.72
      },
      {
        "surface": "Semantic Segmentation",
        "canonical": "Semantic Segmentation",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A fundamental concept in computer vision, facilitating connections with related segmentation techniques.",
        "novelty_score": 0.42,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Network Overconfidence",
        "canonical": "Network Overconfidence",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Addresses a specific challenge in neural network predictions, relevant to improving model accuracy.",
        "novelty_score": 0.67,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "confidence threshold",
      "context loss",
      "random masking"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Confidence Separable Learning",
      "resolved_canonical": "Confidence Separable Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.68,
        "specificity": 0.92,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Pseudo-label Selection",
      "resolved_canonical": "Pseudo-label Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.81,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Semantic Segmentation",
      "resolved_canonical": "Semantic Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.42,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Network Overconfidence",
      "resolved_canonical": "Network Overconfidence",
      "decision": "linked",
      "scores": {
        "novelty": 0.67,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# When Confidence Fails: Revisiting Pseudo-Label Selection in Semi-supervised Semantic Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16704.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16704](https://arxiv.org/abs/2509.16704)

## 🔗 유사한 논문
- [[2025-09-22/PCSR_ Pseudo-label Consistency-Guided Sample Refinement for Noisy Correspondence Learning_20250922|PCSR: Pseudo-label Consistency-Guided Sample Refinement for Noisy Correspondence Learning]] (83.1% similar)
- [[2025-09-23/Learning from Similarity-Confidence and Confidence-Difference_20250923|Learning from Similarity-Confidence and Confidence-Difference]] (83.0% similar)
- [[2025-09-18/Semi-MoE_ Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation_20250918|Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (82.1% similar)
- [[2025-09-23/Intra-Cluster Mixup_ An Effective Data Augmentation Technique for Complementary-Label Learning_20250923|Intra-Cluster Mixup: An Effective Data Augmentation Technique for Complementary-Label Learning]] (81.7% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Semantic Segmentation|Semantic Segmentation]]
**🔗 Specific Connectable**: [[keywords/Pseudo-label Selection|Pseudo-label Selection]]
**⚡ Unique Technical**: [[keywords/Confidence Separable Learning|Confidence Separable Learning]], [[keywords/Network Overconfidence|Network Overconfidence]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16704v1 Announce Type: new 
Abstract: While significant advances exist in pseudo-label generation for semi-supervised semantic segmentation, pseudo-label selection remains understudied. Existing methods typically use fixed confidence thresholds to retain high-confidence predictions as pseudo-labels. However, these methods cannot cope with network overconfidence tendency, where correct and incorrect predictions overlap significantly in high-confidence regions, making separation challenging and amplifying model cognitive bias. Meanwhile, the direct discarding of low-confidence predictions disrupts spatial-semantic continuity, causing critical context loss. We propose Confidence Separable Learning (CSL) to address these limitations. CSL formulates pseudo-label selection as a convex optimization problem within the confidence distribution feature space, establishing sample-specific decision boundaries to distinguish reliable from unreliable predictions. Additionally, CSL introduces random masking of reliable pixels to guide the network in learning contextual relationships from low-reliability regions, thereby mitigating the adverse effects of discarding uncertain predictions. Extensive experimental results on the Pascal, Cityscapes, and COCO benchmarks show that CSL performs favorably against state-of-the-art methods. Code and model weights are available at https://github.com/PanLiuCSU/CSL.

## 📝 요약

이 논문은 반지도학습 기반의 의미론적 분할에서 의사 라벨 선택의 문제를 다룹니다. 기존 방법들은 고정된 신뢰도 임계값을 사용하여 높은 신뢰도의 예측만을 의사 라벨로 선택하지만, 이는 네트워크의 과신 경향으로 인해 정확한 예측과 부정확한 예측이 고신뢰도 영역에서 중첩되어 구분이 어렵다는 문제를 가집니다. 또한, 낮은 신뢰도의 예측을 버리면 공간-의미적 연속성이 깨져 중요한 문맥이 손실됩니다. 이를 해결하기 위해 제안된 Confidence Separable Learning (CSL)은 신뢰도 분포의 특징 공간에서 의사 라벨 선택을 볼록 최적화 문제로 설정하여 신뢰할 수 있는 예측과 그렇지 않은 예측을 구분하는 샘플별 결정 경계를 만듭니다. 또한, 신뢰할 수 있는 픽셀을 랜덤으로 마스킹하여 네트워크가 낮은 신뢰도 영역에서 문맥적 관계를 학습하도록 유도합니다. Pascal, Cityscapes, COCO 벤치마크에서의 실험 결과, CSL은 최신 방법들에 비해 우수한 성능을 보였습니다. 코드와 모델 가중치는 https://github.com/PanLiuCSU/CSL에서 제공됩니다.

## 🎯 주요 포인트

- 1. 기존의 고정된 신뢰도 임계값을 사용하는 방법은 네트워크의 과신 경향 문제를 해결하지 못하며, 이는 모델의 인지 편향을 증폭시킵니다.
- 2. 신뢰도 분포 특징 공간에서의 볼록 최적화 문제로 가짜 라벨 선택을 공식화하여 신뢰할 수 있는 예측과 그렇지 않은 예측을 구분하는 샘플별 결정 경계를 설정합니다.
- 3. 신뢰할 수 있는 픽셀의 무작위 마스킹을 도입하여 네트워크가 낮은 신뢰도 영역에서의 맥락적 관계를 학습하도록 유도합니다.
- 4. Pascal, Cityscapes, COCO 벤치마크에서의 실험 결과, 제안된 CSL 방법이 최신 기법들에 비해 우수한 성능을 보였습니다.


---

*Generated on 2025-09-24 04:33:07*