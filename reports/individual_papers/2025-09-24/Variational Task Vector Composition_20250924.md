<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:43:11.126713",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Task Vectors",
    "Variational Task Vector Composition",
    "Bayesian Inference",
    "Spike-and-Slab Prior"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Task Vectors": 0.8,
    "Variational Task Vector Composition": 0.85,
    "Bayesian Inference": 0.7,
    "Spike-and-Slab Prior": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "task vectors",
        "canonical": "Task Vectors",
        "aliases": [
          "task vector"
        ],
        "category": "unique_technical",
        "rationale": "Task vectors are central to the paper's methodology and offer a unique concept for linking task-specific model changes.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "variational task vector composition",
        "canonical": "Variational Task Vector Composition",
        "aliases": [
          "variational composition"
        ],
        "category": "unique_technical",
        "rationale": "This is the core innovation of the paper, providing a novel approach to task vector composition.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Bayesian inference framework",
        "canonical": "Bayesian Inference",
        "aliases": [
          "Bayesian framework"
        ],
        "category": "broad_technical",
        "rationale": "Bayesian inference is a foundational concept that connects to probabilistic modeling and statistical methods.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Spike-and-Slab prior",
        "canonical": "Spike-and-Slab Prior",
        "aliases": [
          "spike-slab prior"
        ],
        "category": "specific_connectable",
        "rationale": "This prior is crucial for promoting sparsity in the model, linking to statistical sparsity techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "results",
      "approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "task vectors",
      "resolved_canonical": "Task Vectors",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "variational task vector composition",
      "resolved_canonical": "Variational Task Vector Composition",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Bayesian inference framework",
      "resolved_canonical": "Bayesian Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Spike-and-Slab prior",
      "resolved_canonical": "Spike-and-Slab Prior",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Variational Task Vector Composition

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18208.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18208](https://arxiv.org/abs/2509.18208)

## 🔗 유사한 논문
- [[2025-09-23/A non-smooth regularization framework for learning over multitask graphs_20250923|A non-smooth regularization framework for learning over multitask graphs]] (81.5% similar)
- [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (80.5% similar)
- [[2025-09-23/VQToken_ Neural Discrete Token Representation Learning for Extreme Token Reduction in Video Large Language Models_20250923|VQToken: Neural Discrete Token Representation Learning for Extreme Token Reduction in Video Large Language Models]] (80.0% similar)
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (79.7% similar)
- [[2025-09-23/Unified Framework for Pre-trained Neural Network Compression via Decomposition and Optimized Rank Selection_20250923|Unified Framework for Pre-trained Neural Network Compression via Decomposition and Optimized Rank Selection]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Bayesian Inference|Bayesian Inference]]
**🔗 Specific Connectable**: [[keywords/Spike-and-Slab Prior|Spike-and-Slab Prior]]
**⚡ Unique Technical**: [[keywords/Task Vectors|Task Vectors]], [[keywords/Variational Task Vector Composition|Variational Task Vector Composition]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18208v1 Announce Type: cross 
Abstract: Task vectors capture how a model changes during fine-tuning by recording the difference between pre-trained and task-specific weights. The composition of task vectors, a key operator in task arithmetic, enables models to integrate knowledge from multiple tasks without incurring additional inference costs. In this paper, we propose variational task vector composition, where composition coefficients are taken as latent variables and estimated in a Bayesian inference framework. Unlike previous methods that operate at the task level, our framework focuses on sample-specific composition. Motivated by the observation of structural redundancy in task vectors, we introduce a Spike-and-Slab prior that promotes sparsity and preserves only the most informative components. To further address the high variance and sampling inefficiency in sparse, high-dimensional spaces, we develop a gated sampling mechanism that constructs a controllable posterior by filtering the composition coefficients based on both uncertainty and importance. This yields a more stable and interpretable variational framework by deterministically selecting reliable task components, reducing sampling variance while improving transparency and generalization. Experimental results demonstrate that our method consistently outperforms existing approaches across all datasets by selectively leveraging the most reliable and informative components in task vectors. These findings highlight the practical value of our approach, establishing a new standard for efficient and effective task vector composition.

## 📝 요약

이 논문은 모델의 미세 조정 시 변화하는 가중치 차이를 기록하는 '태스크 벡터'의 조합을 통해 여러 태스크의 지식을 통합하는 방법을 제안합니다. 기존 방법과 달리, 제안된 방법은 샘플별로 조합을 수행하며, 스파이크-앤-슬랩 사전 분포를 도입해 태스크 벡터의 구조적 중복성을 줄이고 가장 유용한 요소만을 보존합니다. 또한, 불확실성과 중요성을 기반으로 조합 계수를 필터링하는 게이트 샘플링 메커니즘을 개발하여 샘플링 변동성을 줄이고 투명성과 일반화를 향상시킵니다. 실험 결과, 이 방법은 모든 데이터셋에서 기존 방법보다 우수한 성능을 보이며, 효율적이고 효과적인 태스크 벡터 조합의 새로운 기준을 제시합니다.

## 🎯 주요 포인트

- 1. 작업 벡터는 사전 훈련된 가중치와 작업별 가중치 간의 차이를 기록하여 모델의 변화를 포착합니다.
- 2. 변동 작업 벡터 합성을 제안하며, 이는 베이지안 추론 프레임워크에서 잠재 변수로 추정됩니다.
- 3. 구조적 중복성을 고려하여 스파이크 앤 슬랩 사전 분포를 도입하여 희소성을 촉진하고 가장 정보가 많은 구성 요소만 보존합니다.
- 4. 불확실성과 중요도를 기반으로 구성 계수를 필터링하는 게이트 샘플링 메커니즘을 개발하여 안정적이고 해석 가능한 변동 프레임워크를 제공합니다.
- 5. 실험 결과, 제안된 방법이 모든 데이터셋에서 기존 방법보다 일관되게 우수한 성능을 보이며, 작업 벡터의 가장 신뢰할 수 있고 정보가 많은 구성 요소를 선택적으로 활용합니다.


---

*Generated on 2025-09-24 13:43:11*