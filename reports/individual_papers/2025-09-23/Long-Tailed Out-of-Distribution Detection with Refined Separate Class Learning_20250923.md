---
keywords:
  - Out-of-Distribution Detection
  - Long-Tailed Distribution
  - Separate Class Learning
  - Dynamic Temperature Adjustment
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17034
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:45:58.694159",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Out-of-Distribution Detection",
    "Long-Tailed Distribution",
    "Separate Class Learning",
    "Dynamic Temperature Adjustment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Out-of-Distribution Detection": 0.78,
    "Long-Tailed Distribution": 0.72,
    "Separate Class Learning": 0.75,
    "Dynamic Temperature Adjustment": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Out-of-Distribution Detection",
        "canonical": "Out-of-Distribution Detection",
        "aliases": [
          "OOD Detection"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to the paper and connects to various machine learning tasks involving data distribution.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Long-Tailed Distribution",
        "canonical": "Long-Tailed Distribution",
        "aliases": [
          "Long-Tail Distribution"
        ],
        "category": "unique_technical",
        "rationale": "Understanding this distribution is crucial for addressing class imbalance in machine learning.",
        "novelty_score": 0.67,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Separate Class Learning",
        "canonical": "Separate Class Learning",
        "aliases": [
          "SCL"
        ],
        "category": "unique_technical",
        "rationale": "It represents a specific approach to improve OOD detection, relevant for specialized learning strategies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Dynamic Temperature Adjustment",
        "canonical": "Dynamic Temperature Adjustment",
        "aliases": [
          "Temperature Scaling"
        ],
        "category": "unique_technical",
        "rationale": "This technique is innovative for improving model calibration and performance in OOD detection.",
        "novelty_score": 0.65,
        "connectivity_score": 0.68,
        "specificity_score": 0.77,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "Refined Separate Class Learning",
      "Informative Outlier Mining"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Out-of-Distribution Detection",
      "resolved_canonical": "Out-of-Distribution Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Long-Tailed Distribution",
      "resolved_canonical": "Long-Tailed Distribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.67,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Separate Class Learning",
      "resolved_canonical": "Separate Class Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Dynamic Temperature Adjustment",
      "resolved_canonical": "Dynamic Temperature Adjustment",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.68,
        "specificity": 0.77,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Long-Tailed Out-of-Distribution Detection with Refined Separate Class Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17034.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17034](https://arxiv.org/abs/2509.17034)

## 🔗 유사한 논문
- [[2025-09-18/GROOD_ GRadient-Aware Out-of-Distribution Detection_20250918|GROOD: GRadient-Aware Out-of-Distribution Detection]] (84.3% similar)
- [[2025-09-19/ToolSample_ Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning_20250919|ToolSample: Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning]] (80.0% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (79.6% similar)
- [[2025-09-22/Inference Offloading for Cost-Sensitive Binary Classification at the Edge_20250922|Inference Offloading for Cost-Sensitive Binary Classification at the Edge]] (79.1% similar)
- [[2025-09-19/MADAR_ Efficient Continual Learning for Malware Analysis with Distribution-Aware Replay_20250919|MADAR: Efficient Continual Learning for Malware Analysis with Distribution-Aware Replay]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Out-of-Distribution Detection|Out-of-Distribution Detection]]
**⚡ Unique Technical**: [[keywords/Long-Tailed Distribution|Long-Tailed Distribution]], [[keywords/Separate Class Learning|Separate Class Learning]], [[keywords/Dynamic Temperature Adjustment|Dynamic Temperature Adjustment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17034v1 Announce Type: new 
Abstract: Out-of-distribution (OOD) detection is crucial for deploying robust machine learning models. However, when training data follows a long-tailed distribution, the model's ability to accurately detect OOD samples is significantly compromised, due to the confusion between OOD samples and head/tail classes. To distinguish OOD samples from both head and tail classes, the separate class learning (SCL) approach has emerged as a promising solution, which separately conduct head-specific and tail-specific class learning. To this end, we examine the limitations of existing works of SCL and reveal that the OOD detection performance is notably influenced by the use of static scaling temperature value and the presence of uninformative outliers. To mitigate these limitations, we propose a novel approach termed Refined Separate Class Learning (RSCL), which leverages dynamic class-wise temperature adjustment to modulate the temperature parameter for each in-distribution class and informative outlier mining to identify diverse types of outliers based on their affinity with head and tail classes. Extensive experiments demonstrate that RSCL achieves superior OOD detection performance while improving the classification accuracy on in-distribution data.

## 📝 요약

이 논문은 긴 꼬리 분포를 따르는 데이터에서 OOD(분포 외) 샘플을 효과적으로 탐지하는 방법을 제안합니다. 기존의 별도 클래스 학습(SCL) 방법의 한계를 분석하고, 정적 스케일링 온도 값과 비정보성 이상치의 존재가 OOD 탐지 성능에 미치는 영향을 밝혀냈습니다. 이를 개선하기 위해, 각 클래스별 동적 온도 조정과 정보성 이상치 탐색을 활용한 새로운 방법인 정제된 별도 클래스 학습(RSCL)을 제안합니다. 실험 결과, RSCL은 OOD 탐지 성능을 향상시키고, 분포 내 데이터의 분류 정확도도 개선하는 것으로 나타났습니다.

## 🎯 주요 포인트

- 1. OOD(Out-of-distribution) 검출은 강건한 머신러닝 모델 배포에 필수적이다.
- 2. 긴 꼬리 분포를 따르는 데이터에서는 OOD 샘플과 헤드/테일 클래스 간의 혼동으로 인해 OOD 검출 능력이 저하된다.
- 3. Separate Class Learning(SCL) 접근법은 헤드와 테일 클래스를 별도로 학습하여 OOD 샘플을 구분하는 유망한 솔루션으로 부상했다.
- 4. 기존 SCL의 한계로는 정적 스케일링 온도 값 사용과 비정보성 이상치의 존재가 OOD 검출 성능에 영향을 미친다는 점이 있다.
- 5. 제안된 Refined Separate Class Learning(RSCL) 접근법은 동적 클래스별 온도 조정과 정보성 이상치 마이닝을 통해 OOD 검출 성능을 향상시킨다.


---

*Generated on 2025-09-24 01:45:58*