---
keywords:
  - Deep Time Series Hashing
  - von Mises-Fisher Likelihood Loss
  - Hyperspherical Space
  - Deep Learning
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19625
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:37:57.365329",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Time Series Hashing",
    "von Mises-Fisher Likelihood Loss",
    "Hyperspherical Space",
    "Deep Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Time Series Hashing": 0.78,
    "von Mises-Fisher Likelihood Loss": 0.79,
    "Hyperspherical Space": 0.77,
    "Deep Learning": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Time Series Hashing",
        "canonical": "Deep Time Series Hashing",
        "aliases": [
          "Time Series Hashing",
          "Deep Hashing"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's contribution and offers a novel approach to indexing time series data.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "von Mises-Fisher Likelihood Loss",
        "canonical": "von Mises-Fisher Likelihood Loss",
        "aliases": [
          "vMF Loss",
          "vMF Likelihood"
        ],
        "category": "unique_technical",
        "rationale": "The proposed loss function is a novel contribution that enhances the hashing process by reducing information loss.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "Hyperspherical Space",
        "canonical": "Hyperspherical Space",
        "aliases": [
          "Spherical Space",
          "M-dimensional Hypersphere"
        ],
        "category": "unique_technical",
        "rationale": "The mapping to hyperspherical space is a key component of the method, providing a unique approach to data representation.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep learning is the foundational technique used in the hashing method, linking it to a broad range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "Indexing",
      "Binary Representations",
      "Semantic Meaning"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Time Series Hashing",
      "resolved_canonical": "Deep Time Series Hashing",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "von Mises-Fisher Likelihood Loss",
      "resolved_canonical": "von Mises-Fisher Likelihood Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Hyperspherical Space",
      "resolved_canonical": "Hyperspherical Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# Adaptive von Mises-Fisher Likelihood Loss for Supervised Deep Time Series Hashing

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19625.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19625](https://arxiv.org/abs/2509.19625)

## 🔗 유사한 논문
- [[2025-09-23/Learning Attribute-Aware Hash Codes for Fine-Grained Image Retrieval via Query Optimization_20250923|Learning Attribute-Aware Hash Codes for Fine-Grained Image Retrieval via Query Optimization]] (82.7% similar)
- [[2025-09-18/DiffHash_ Text-Guided Targeted Attack via Diffusion Models against Deep Hashing Image Retrieval_20250918|DiffHash: Text-Guided Targeted Attack via Diffusion Models against Deep Hashing Image Retrieval]] (81.6% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (81.5% similar)
- [[2025-09-19/Hashing-Baseline_ Rethinking Hashing in the Age of Pretrained Models_20250919|Hashing-Baseline: Rethinking Hashing in the Age of Pretrained Models]] (81.4% similar)
- [[2025-09-22/VMDNet_ Time Series Forecasting with Leakage-Free Samplewise Variational Mode Decomposition and Multibranch Decoding_20250922|VMDNet: Time Series Forecasting with Leakage-Free Samplewise Variational Mode Decomposition and Multibranch Decoding]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**⚡ Unique Technical**: [[keywords/Deep Time Series Hashing|Deep Time Series Hashing]], [[keywords/von Mises-Fisher Likelihood Loss|von Mises-Fisher Likelihood Loss]], [[keywords/Hyperspherical Space|Hyperspherical Space]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19625v1 Announce Type: new 
Abstract: Indexing time series by creating compact binary representations is a fundamental task in time series data mining. Recently, deep learning-based hashing methods have proven effective for indexing time series based on semantic meaning rather than just raw similarity. The purpose of deep hashing is to map samples with the same semantic meaning to identical binary hash codes, enabling more efficient search and retrieval. Unlike other supervised representation learning methods, supervised deep hashing requires a discretization step to convert real-valued representations into binary codes, but this can induce significant information loss. In this paper, we propose a von Mises-Fisher (vMF) hashing loss. The proposed deep hashing model maps data to an M-dimensional hyperspherical space to effectively reduce information loss and models each data class as points following distinct vMF distributions. The designed loss aims to maximize the separation between each modeled vMF distribution to provide a better way to maximize the margin between each semantically different data sample. Experimental results show that our method outperforms existing baselines. The implementation is publicly available at https://github.com/jmpq97/vmf-hashing

## 📝 요약

이 논문은 시계열 데이터를 효율적으로 인덱싱하기 위한 딥러닝 기반 해싱 방법을 제안합니다. 기존의 방법들이 실수 값을 이진 코드로 변환하는 과정에서 정보 손실을 초래하는 문제를 해결하기 위해, 저자들은 von Mises-Fisher(vMF) 해싱 손실을 도입했습니다. 이 방법은 데이터를 M차원 초구형 공간에 매핑하여 정보 손실을 줄이고, 각 데이터 클래스를 개별적인 vMF 분포로 모델링합니다. 이러한 접근은 서로 다른 의미를 가진 데이터 샘플 간의 여백을 최대화하여 검색 효율성을 높입니다. 실험 결과, 제안된 방법이 기존의 기준 방법들보다 우수한 성능을 보였습니다. 구현 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 시계열 데이터를 의미 기반으로 효율적으로 인덱싱하기 위해 딥러닝 기반 해싱 방법이 효과적임을 입증했습니다.
- 2. 제안된 vMF 해싱 손실은 M차원 초구 공간으로 데이터를 매핑하여 정보 손실을 줄이고, 각 데이터 클래스를 vMF 분포로 모델링합니다.
- 3. 설계된 손실은 각 vMF 분포 간의 분리를 최대화하여 의미적으로 다른 데이터 샘플 간의 여유를 극대화합니다.
- 4. 실험 결과, 제안된 방법이 기존의 기준선보다 우수한 성능을 보였습니다.
- 5. 구현 코드는 https://github.com/jmpq97/vmf-hashing에서 공개되어 있습니다.


---

*Generated on 2025-09-25 16:37:57*