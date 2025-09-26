---
keywords:
  - Tensor Train
  - Graph Regularization
  - Visual Data Completion
  - Probabilistic Model
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2306.11123
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:29:02.864930",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Tensor Train",
    "Graph Regularization",
    "Visual Data Completion",
    "Probabilistic Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Tensor Train": 0.78,
    "Graph Regularization": 0.83,
    "Visual Data Completion": 0.75,
    "Probabilistic Model": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Tensor Train",
        "canonical": "Tensor Train",
        "aliases": [
          "TT"
        ],
        "category": "unique_technical",
        "rationale": "Tensor Train is a specific technique central to the paper's methodology, providing a unique approach to visual data completion.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Graph Regularization",
        "canonical": "Graph Regularization",
        "aliases": [
          "Graph-based Regularization"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Regularization is a key concept in enhancing local similarity, linking well with graph-based methods in machine learning.",
        "novelty_score": 0.68,
        "connectivity_score": 0.82,
        "specificity_score": 0.8,
        "link_intent_score": 0.83
      },
      {
        "surface": "Visual Data Completion",
        "canonical": "Visual Data Completion",
        "aliases": [
          "Image Completion",
          "Video Completion"
        ],
        "category": "unique_technical",
        "rationale": "This is the main application of the proposed method, providing a specific context for tensor train techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Probabilistic Model",
        "canonical": "Probabilistic Model",
        "aliases": [
          "Probabilistic Framework"
        ],
        "category": "broad_technical",
        "rationale": "Probabilistic models are fundamental in machine learning, offering a broad technical linkage to statistical methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "Method",
      "Experiment",
      "Performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Tensor Train",
      "resolved_canonical": "Tensor Train",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Graph Regularization",
      "resolved_canonical": "Graph Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.82,
        "specificity": 0.8,
        "link_intent": 0.83
      }
    },
    {
      "candidate_surface": "Visual Data Completion",
      "resolved_canonical": "Visual Data Completion",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Probabilistic Model",
      "resolved_canonical": "Probabilistic Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# To Fold or Not to Fold: Graph Regularized Tensor Train for Visual Data Completion

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2306.11123.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2306.11123](https://arxiv.org/abs/2306.11123)

## 🔗 유사한 논문
- [[2025-09-24/Tensor Train Completion from Fiberwise Observations Along a Single Mode_20250924|Tensor Train Completion from Fiberwise Observations Along a Single Mode]] (84.5% similar)
- [[2025-09-22/Adversarial Graph Fusion for Incomplete Multi-view Semi-supervised Learning with Tensorial Imputation_20250922|Adversarial Graph Fusion for Incomplete Multi-view Semi-supervised Learning with Tensorial Imputation]] (81.6% similar)
- [[2025-09-23/A non-smooth regularization framework for learning over multitask graphs_20250923|A non-smooth regularization framework for learning over multitask graphs]] (80.6% similar)
- [[2025-09-23/Evict3R_ Training-Free Token Eviction for Memory-Bounded Streaming Visual Geometry Transformers_20250923|Evict3R: Training-Free Token Eviction for Memory-Bounded Streaming Visual Geometry Transformers]] (79.9% similar)
- [[2025-09-23/Visual Instruction Pretraining for Domain-Specific Foundation Models_20250923|Visual Instruction Pretraining for Domain-Specific Foundation Models]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Probabilistic Model|Probabilistic Model]]
**🔗 Specific Connectable**: [[keywords/Graph Regularization|Graph Regularization]]
**⚡ Unique Technical**: [[keywords/Tensor Train|Tensor Train]], [[keywords/Visual Data Completion|Visual Data Completion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2306.11123v2 Announce Type: replace-cross 
Abstract: Tensor train (TT) representation has achieved tremendous success in visual data completion tasks, especially when it is combined with tensor folding. However, folding an image or video tensor breaks the original data structure, leading to local information loss as nearby pixels may be assigned into different dimensions and become far away from each other. In this paper, to fully preserve the local information of the original visual data, we explore not folding the data tensor, and at the same time adopt graph information to regularize local similarity between nearby entries. To overcome the high computational complexity introduced by the graph-based regularization in the TT completion problem, we propose to break the original problem into multiple sub-problems with respect to each TT core fiber, instead of each TT core as in traditional methods. Furthermore, to avoid heavy parameter tuning, a sparsity promoting probabilistic model is built based on the generalized inverse Gaussian (GIG) prior, and an inference algorithm is derived under the mean-field approximation. Experiments on both synthetic data and real-world visual data show the superiority of the proposed methods.

## 📝 요약

이 논문은 텐서 트레인(TT) 표현을 활용한 시각 데이터 완성 방법을 제안합니다. 기존의 텐서 폴딩 방식은 데이터 구조를 손상시켜 인접한 픽셀 간의 지역 정보를 잃게 만듭니다. 이를 해결하기 위해 데이터 텐서를 폴딩하지 않고, 그래프 정보를 사용하여 인접 항목 간의 유사성을 규제합니다. 그래프 기반 규제의 높은 계산 복잡성을 해결하기 위해, 전통적인 방법과 달리 각 TT 코어 섬유에 대한 여러 하위 문제로 문제를 분할합니다. 또한, 매개변수 조정을 최소화하기 위해 일반화된 역 가우시안(GIG) 사전 기반의 희소성 촉진 확률 모델을 구축하고, 평균장 근사를 통한 추론 알고리즘을 도출합니다. 실험 결과, 제안된 방법이 합성 및 실제 시각 데이터에서 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 텐서 트레인(TT) 표현은 텐서 폴딩과 결합될 때 시각적 데이터 완성 작업에서 큰 성공을 거두었지만, 폴딩은 원래 데이터 구조를 손상시킬 수 있습니다.
- 2. 원본 시각 데이터의 지역 정보를 완전히 보존하기 위해, 데이터 텐서를 폴딩하지 않고 그래프 정보를 사용하여 인접 항목 간의 지역 유사성을 정규화하는 방법을 탐구합니다.
- 3. 그래프 기반 정규화로 인한 높은 계산 복잡성을 해결하기 위해, 전통적인 방법과 달리 각 TT 코어가 아닌 각 TT 코어 섬유에 대해 문제를 여러 하위 문제로 나누는 방법을 제안합니다.
- 4. 무거운 매개 변수 조정을 피하기 위해, 일반화된 역 가우시안(GIG) 사전 기반의 희소성 촉진 확률 모델을 구축하고, 평균-필드 근사를 통한 추론 알고리즘을 도출합니다.
- 5. 실험 결과, 합성 데이터와 실제 시각 데이터 모두에서 제안된 방법의 우수성을 보여줍니다.


---

*Generated on 2025-09-26 09:29:02*