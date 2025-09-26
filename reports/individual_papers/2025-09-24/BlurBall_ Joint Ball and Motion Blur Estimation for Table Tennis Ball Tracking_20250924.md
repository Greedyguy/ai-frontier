<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:58:28.592259",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Motion Blur",
    "Attention Mechanism",
    "Table Tennis Ball Detection",
    "Squeeze-and-Excitation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Motion Blur": 0.85,
    "Attention Mechanism": 0.88,
    "Table Tennis Ball Detection": 0.7,
    "Squeeze-and-Excitation": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "motion blur",
        "canonical": "Motion Blur",
        "aliases": [
          "blur",
          "image blur"
        ],
        "category": "unique_technical",
        "rationale": "Motion blur is central to the paper's methodology and contributes to advancements in detection accuracy.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "attention mechanisms",
        "canonical": "Attention Mechanism",
        "aliases": [
          "attention layers",
          "attention modules"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are crucial for the model's performance, linking to broader machine learning techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.88
      },
      {
        "surface": "table tennis ball detection",
        "canonical": "Table Tennis Ball Detection",
        "aliases": [
          "ping pong ball tracking",
          "table tennis tracking"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area of the research, highlighting its niche focus.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.7
      },
      {
        "surface": "Squeeze-and-Excitation",
        "canonical": "Squeeze-and-Excitation",
        "aliases": [
          "SE block",
          "SE layer"
        ],
        "category": "specific_connectable",
        "rationale": "Squeeze-and-Excitation is a specific technique used to enhance model performance, linking to neural network design.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "detection systems",
      "sports analytics"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "motion blur",
      "resolved_canonical": "Motion Blur",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "attention mechanisms",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "table tennis ball detection",
      "resolved_canonical": "Table Tennis Ball Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Squeeze-and-Excitation",
      "resolved_canonical": "Squeeze-and-Excitation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# BlurBall: Joint Ball and Motion Blur Estimation for Table Tennis Ball Tracking

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18387.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.18387](https://arxiv.org/abs/2509.18387)

## 🔗 유사한 논문
- [[2025-09-19/BST_ Badminton Stroke-type Transformer for Skeleton-based Action Recognition in Racket Sports_20250919|BST: Badminton Stroke-type Transformer for Skeleton-based Action Recognition in Racket Sports]] (83.0% similar)
- [[2025-09-22/Towards Sharper Object Boundaries in Self-Supervised Depth Estimation_20250922|Towards Sharper Object Boundaries in Self-Supervised Depth Estimation]] (78.7% similar)
- [[2025-09-23/BaseBoostDepth_ Exploiting Larger Baselines For Self-supervised Monocular Depth Estimation_20250923|BaseBoostDepth: Exploiting Larger Baselines For Self-supervised Monocular Depth Estimation]] (78.3% similar)
- [[2025-09-23/DepTR-MOT_ Unveiling the Potential of Depth-Informed Trajectory Refinement for Multi-Object Tracking_20250923|DepTR-MOT: Unveiling the Potential of Depth-Informed Trajectory Refinement for Multi-Object Tracking]] (78.2% similar)
- [[2025-09-24/T-Detect_ Tail-Aware Statistical Normalization for Robust Detection of Adversarial Machine-Generated Text_20250924|T-Detect: Tail-Aware Statistical Normalization for Robust Detection of Adversarial Machine-Generated Text]] (77.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Squeeze-and-Excitation|Squeeze-and-Excitation]]
**⚡ Unique Technical**: [[keywords/Motion Blur|Motion Blur]], [[keywords/Table Tennis Ball Detection|Table Tennis Ball Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18387v1 Announce Type: new 
Abstract: Motion blur reduces the clarity of fast-moving objects, posing challenges for detection systems, especially in racket sports, where balls often appear as streaks rather than distinct points. Existing labeling conventions mark the ball at the leading edge of the blur, introducing asymmetry and ignoring valuable motion cues correlated with velocity. This paper introduces a new labeling strategy that places the ball at the center of the blur streak and explicitly annotates blur attributes. Using this convention, we release a new table tennis ball detection dataset. We demonstrate that this labeling approach consistently enhances detection performance across various models. Furthermore, we introduce BlurBall, a model that jointly estimates ball position and motion blur attributes. By incorporating attention mechanisms such as Squeeze-and-Excitation over multi-frame inputs, we achieve state-of-the-art results in ball detection. Leveraging blur not only improves detection accuracy but also enables more reliable trajectory prediction, benefiting real-time sports analytics.

## 📝 요약

이 논문은 빠르게 움직이는 물체의 모호함을 줄이기 위한 새로운 라벨링 전략을 제안합니다. 기존의 라벨링 방식은 모션 블러의 앞부분에 공을 표시하여 비대칭성을 초래했지만, 본 연구에서는 블러의 중심에 공을 배치하고 블러 속성을 명시적으로 주석 처리합니다. 이를 통해 새로운 탁구공 탐지 데이터셋을 공개하고, 다양한 모델에서 탐지 성능이 향상됨을 입증했습니다. 또한, BlurBall 모델을 소개하여 공 위치와 모션 블러 속성을 동시에 추정하며, Squeeze-and-Excitation 같은 주의 메커니즘을 활용해 최첨단 결과를 달성했습니다. 블러 정보를 활용함으로써 탐지 정확도를 높이고 실시간 스포츠 분석에 유리한 궤적 예측이 가능해졌습니다.

## 🎯 주요 포인트

- 1. 기존의 라벨링 방식은 모션 블러의 선두에 공을 표시하여 비대칭성을 초래하고 속도와 관련된 중요한 모션 정보를 무시합니다.
- 2. 본 논문은 블러 스트릭의 중심에 공을 배치하고 블러 속성을 명시적으로 주석하는 새로운 라벨링 전략을 제안합니다.
- 3. 새로운 라벨링 방식을 사용하여 탁구공 탐지 데이터셋을 공개하고, 다양한 모델에서 탐지 성능이 일관되게 향상됨을 입증합니다.
- 4. BlurBall 모델은 공의 위치와 모션 블러 속성을 공동으로 추정하며, Squeeze-and-Excitation과 같은 주의 메커니즘을 활용하여 최첨단 결과를 달성합니다.
- 5. 블러를 활용함으로써 탐지 정확도가 향상될 뿐만 아니라, 실시간 스포츠 분석에 유리한 더 신뢰할 수 있는 궤적 예측이 가능해집니다.


---

*Generated on 2025-09-24 15:58:28*