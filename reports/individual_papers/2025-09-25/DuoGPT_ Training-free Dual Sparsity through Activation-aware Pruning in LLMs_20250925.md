---
keywords:
  - Large Language Model
  - Activation Sparsity
  - Optimal Brain Compression
  - Structured Pruning
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2506.20194
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T17:08:41.208850",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Activation Sparsity",
    "Optimal Brain Compression",
    "Structured Pruning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Activation Sparsity": 0.78,
    "Optimal Brain Compression": 0.77,
    "Structured Pruning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus on pruning and optimization, providing a strong link to existing research on model efficiency.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Activation Sparsity",
        "canonical": "Activation Sparsity",
        "aliases": [
          "Dynamic Structured Weight Sparsity"
        ],
        "category": "unique_technical",
        "rationale": "Activation Sparsity is a novel concept in the paper, crucial for understanding the proposed dual-sparsity framework.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Optimal Brain Compression",
        "canonical": "Optimal Brain Compression",
        "aliases": [
          "OBC"
        ],
        "category": "unique_technical",
        "rationale": "The Optimal Brain Compression framework is extended in the paper, making it a key technical contribution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Structured Pruning",
        "canonical": "Structured Pruning",
        "aliases": [
          "Structured Sparsity"
        ],
        "category": "specific_connectable",
        "rationale": "Structured Pruning is compared against the proposed method, providing a basis for evaluating the paper's contributions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "accuracy",
      "baseline"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Activation Sparsity",
      "resolved_canonical": "Activation Sparsity",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Optimal Brain Compression",
      "resolved_canonical": "Optimal Brain Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Structured Pruning",
      "resolved_canonical": "Structured Pruning",
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

# DuoGPT: Training-free Dual Sparsity through Activation-aware Pruning in LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.20194.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2506.20194](https://arxiv.org/abs/2506.20194)

## 🔗 유사한 논문
- [[2025-09-24/Speculate Deep and Accurate_ Lossless and Training-Free Acceleration for Offloaded LLMs via Substitute Speculative Decoding_20250924|Speculate Deep and Accurate: Lossless and Training-Free Acceleration for Offloaded LLMs via Substitute Speculative Decoding]] (85.1% similar)
- [[2025-09-23/GALLa_ Graph Aligned Large Language Models for Improved Source Code Understanding_20250923|GALLa: Graph Aligned Large Language Models for Improved Source Code Understanding]] (84.9% similar)
- [[2025-09-24/Sparse Training Scheme for Multimodal LLM_20250924|Sparse Training Scheme for Multimodal LLM]] (84.3% similar)
- [[2025-09-17/NIRVANA_ Structured pruning reimagined for large language models compression_20250917|NIRVANA: Structured pruning reimagined for large language models compression]] (83.3% similar)
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Structured Pruning|Structured Pruning]]
**⚡ Unique Technical**: [[keywords/Activation Sparsity|Activation Sparsity]], [[keywords/Optimal Brain Compression|Optimal Brain Compression]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.20194v2 Announce Type: replace 
Abstract: Large language models (LLMs) deliver strong performance but are difficult to deploy due to high memory and compute costs. While pruning reduces these demands, most methods ignore activation sparsity observed at runtime. We reinterpret activation sparsity as dynamic structured weight sparsity and propose DuoGPT, a unified framework that constructs dual-sparse (spMspV) workloads by combining unstructured weight pruning with activation sparsity. To preserve accuracy, we extend the Optimal Brain Compression (OBC) framework with activation-aware calibration and introduce output residuals from the dense model as correction terms. We further optimize the solution for efficient GPU execution, enabling scalability to billion-parameter LLMs. Evaluations on LLaMA-2 and LLaMA-3 show that DuoGPT outperforms state-of-the-art structured pruning methods by up to 9.17% accuracy at an iso-speedup of 1.39$\times$ compared to the baseline dense model. Code is available at Github.

## 📝 요약

대형 언어 모델(LLM)의 높은 메모리와 연산 비용 문제를 해결하기 위해 DuoGPT라는 프레임워크를 제안합니다. DuoGPT는 실행 시 발생하는 활성화 희소성을 동적 구조적 가중치 희소성으로 재해석하여, 비구조적 가중치 가지치기와 활성화 희소성을 결합한 이중 희소 작업을 구성합니다. 정확성을 유지하기 위해 최적의 뇌 압축(OBC) 프레임워크를 활성화 인식 보정으로 확장하고, 밀집 모델의 출력 잔차를 보정 항으로 도입합니다. DuoGPT는 GPU 실행 효율성을 최적화하여 수십억 개의 매개변수를 가진 LLM에 확장 가능하며, LLaMA-2 및 LLaMA-3 평가에서 기존 구조적 가지치기 방법보다 최대 9.17% 높은 정확성을 보여줍니다. 코드는 Github에서 제공됩니다.

## 🎯 주요 포인트

- 1. DuoGPT는 실행 시 관찰되는 활성화 희소성을 동적 구조적 가중치 희소성으로 재해석하여, 비구조적 가중치 가지치기와 활성화 희소성을 결합한 이중 희소 작업 부하를 구성합니다.
- 2. 정확도를 유지하기 위해, 활성화 인식 보정을 통해 최적의 뇌 압축(OBC) 프레임워크를 확장하고, 밀집 모델의 출력 잔차를 보정 항으로 도입합니다.
- 3. DuoGPT는 효율적인 GPU 실행을 위해 솔루션을 최적화하여, 수십억 개의 매개변수를 가진 대형 언어 모델(LLM)로의 확장을 가능하게 합니다.
- 4. LLaMA-2 및 LLaMA-3에 대한 평가에서 DuoGPT는 최첨단 구조적 가지치기 방법보다 최대 9.17% 더 높은 정확도를 제공하며, 기준 밀집 모델 대비 1.39배의 동일 속도 향상을 달성합니다.
- 5. DuoGPT의 코드는 Github에서 제공됩니다.


---

*Generated on 2025-09-25 17:08:41*