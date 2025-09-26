---
keywords:
  - Long-tailed Semi-Supervised Learning
  - Open-World Scenarios
  - Parameter-Efficient Fine-Tuning
  - Large Language Model
  - Out-of-Distribution Samples
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.09926
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:52:27.559295",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Long-tailed Semi-Supervised Learning",
    "Open-World Scenarios",
    "Parameter-Efficient Fine-Tuning",
    "Large Language Model",
    "Out-of-Distribution Samples"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Long-tailed Semi-Supervised Learning": 0.78,
    "Open-World Scenarios": 0.77,
    "Parameter-Efficient Fine-Tuning": 0.79,
    "Large Language Model": 0.75,
    "Out-of-Distribution Samples": 0.76
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Long-tailed Semi-Supervised Learning",
        "canonical": "Long-tailed Semi-Supervised Learning",
        "aliases": [
          "LTSSL"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and connects to niche research in handling imbalanced datasets.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Open-World Scenarios",
        "canonical": "Open-World Scenarios",
        "aliases": [
          "Open World"
        ],
        "category": "unique_technical",
        "rationale": "The concept of open-world scenarios is crucial for understanding the challenges addressed in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Parameter-Efficient Fine-Tuning",
        "canonical": "Parameter-Efficient Fine-Tuning",
        "aliases": [
          "Efficient Fine-Tuning"
        ],
        "category": "unique_technical",
        "rationale": "This approach is a key innovation in the paper, linking to efficiency in model training.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Foundation Model",
        "canonical": "Large Language Model",
        "aliases": [
          "Foundation Models"
        ],
        "category": "broad_technical",
        "rationale": "Foundation models are a broad category that connects to the use of large pre-trained models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "Out-of-Distribution Samples",
        "canonical": "Out-of-Distribution Samples",
        "aliases": [
          "OOD Samples"
        ],
        "category": "specific_connectable",
        "rationale": "Handling OOD samples is critical for the proposed method's effectiveness in open-world scenarios.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.76
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
      "candidate_surface": "Long-tailed Semi-Supervised Learning",
      "resolved_canonical": "Long-tailed Semi-Supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Open-World Scenarios",
      "resolved_canonical": "Open-World Scenarios",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Parameter-Efficient Fine-Tuning",
      "resolved_canonical": "Parameter-Efficient Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Foundation Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Out-of-Distribution Samples",
      "resolved_canonical": "Out-of-Distribution Samples",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.76
      }
    }
  ]
}
-->

# LoFT: Parameter-Efficient Fine-Tuning for Long-tailed Semi-Supervised Learning in Open-World Scenarios

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.09926.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.09926](https://arxiv.org/abs/2509.09926)

## 🔗 유사한 논문
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (85.1% similar)
- [[2025-09-22/Not All Parameters Are Created Equal_ Smart Isolation Boosts Fine-Tuning Performance_20250922|Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance]] (83.2% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (82.8% similar)
- [[2025-09-22/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250922|Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (82.1% similar)
- [[2025-09-23/LLM-Guided Co-Training for Text Classification_20250923|LLM-Guided Co-Training for Text Classification]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Out-of-Distribution Samples|Out-of-Distribution Samples]]
**⚡ Unique Technical**: [[keywords/Long-tailed Semi-Supervised Learning|Long-tailed Semi-Supervised Learning]], [[keywords/Open-World Scenarios|Open-World Scenarios]], [[keywords/Parameter-Efficient Fine-Tuning|Parameter-Efficient Fine-Tuning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.09926v2 Announce Type: replace 
Abstract: Long-tailed learning has garnered increasing attention due to its wide applicability in real-world scenarios. Among existing approaches, Long-Tailed Semi-Supervised Learning (LTSSL) has emerged as an effective solution by incorporating a large amount of unlabeled data into the imbalanced labeled dataset. However, most prior LTSSL methods are designed to train models from scratch, which often leads to issues such as overconfidence and low-quality pseudo-labels. To address these challenges, we extend LTSSL into the foundation model fine-tuning paradigm and propose a novel framework: LoFT (Long-tailed semi-supervised learning via parameter-efficient Fine-Tuning). We demonstrate that fine-tuned foundation models can generate more reliable pseudolabels, thereby benefiting imbalanced learning. Furthermore, we explore a more practical setting by investigating semi-supervised learning under open-world conditions, where the unlabeled data may include out-of-distribution (OOD) samples. To handle this problem, we propose LoFT-OW (LoFT under Open-World scenarios) to improve the discriminative ability. Experimental results on multiple benchmarks demonstrate that our method achieves superior performance compared to previous approaches, even when utilizing only 1\% of the unlabeled data compared with previous works.

## 📝 요약

이 논문은 긴 꼬리 학습(Long-tailed learning)에서의 문제점을 해결하기 위해 새로운 프레임워크인 LoFT를 제안합니다. 기존의 긴 꼬리 반지도 학습(LTSSL) 방법은 모델을 처음부터 훈련시키는 방식으로, 과신과 낮은 품질의 가짜 레이블 문제를 야기할 수 있습니다. 이를 해결하기 위해, 이 연구는 파운데이션 모델의 파라미터 효율적 미세 조정을 통해 더 신뢰할 수 있는 가짜 레이블을 생성하는 방법을 제안합니다. 또한, 열린 세계 조건에서의 반지도 학습을 탐구하여 분류 능력을 향상시키는 LoFT-OW를 소개합니다. 여러 벤치마크 실험 결과, 제안된 방법은 이전 방법들보다 뛰어난 성능을 보였으며, 적은 양의 미라벨 데이터를 사용하면서도 우수한 결과를 달성했습니다.

## 🎯 주요 포인트

- 1. Long-Tailed Semi-Supervised Learning (LTSSL)은 불균형한 라벨 데이터셋에 많은 양의 비라벨 데이터를 통합하여 효과적인 솔루션을 제공합니다.
- 2. 기존 LTSSL 방법은 모델을 처음부터 학습시키는 방식으로, 과신 및 낮은 품질의 가짜 라벨 문제를 초래할 수 있습니다.
- 3. 우리는 LTSSL을 기초 모델 미세 조정 패러다임으로 확장하여, LoFT라는 새로운 프레임워크를 제안합니다.
- 4. 미세 조정된 기초 모델은 더 신뢰할 수 있는 가짜 라벨을 생성하여 불균형 학습에 이점을 제공합니다.
- 5. LoFT-OW는 개방형 세계 시나리오에서 비라벨 데이터에 포함될 수 있는 분포 외 샘플을 처리하여 판별 능력을 향상시킵니다.


---

*Generated on 2025-09-24 02:52:27*