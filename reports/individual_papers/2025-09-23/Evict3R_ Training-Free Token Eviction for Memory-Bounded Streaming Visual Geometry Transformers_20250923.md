---
keywords:
  - Transformer
  - Token Eviction
  - 3D Perception
  - Memory-Bounded Streaming
  - 3D Reconstruction
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17650
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:58:13.839012",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Token Eviction",
    "3D Perception",
    "Memory-Bounded Streaming",
    "3D Reconstruction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Token Eviction": 0.78,
    "3D Perception": 0.82,
    "Memory-Bounded Streaming": 0.77,
    "3D Reconstruction": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Streaming Visual Transformers",
        "canonical": "Transformer",
        "aliases": [
          "StreamVGGT",
          "Visual Transformers"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the broader concept of Transformers, which is pivotal in the context of visual data processing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.68,
        "link_intent_score": 0.85
      },
      {
        "surface": "Token Eviction",
        "canonical": "Token Eviction",
        "aliases": [
          "Eviction Policy",
          "Token Discarding"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for managing memory in streaming transformers, which is central to the paper's contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "3D Perception",
        "canonical": "3D Perception",
        "aliases": [
          "3D Vision",
          "Three-Dimensional Perception"
        ],
        "category": "specific_connectable",
        "rationale": "Key aspect of the paper's focus on visual data processing, relevant for linking to other 3D vision research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.71,
        "link_intent_score": 0.82
      },
      {
        "surface": "Memory-Bounded Streaming",
        "canonical": "Memory-Bounded Streaming",
        "aliases": [
          "Memory Constraints",
          "Streaming Constraints"
        ],
        "category": "unique_technical",
        "rationale": "Highlights the paper's focus on memory efficiency, a unique technical challenge addressed.",
        "novelty_score": 0.68,
        "connectivity_score": 0.67,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "3D Reconstruction",
        "canonical": "3D Reconstruction",
        "aliases": [
          "Three-Dimensional Reconstruction"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's experiments and relevant for connecting to other works in 3D data processing.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
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
      "candidate_surface": "Streaming Visual Transformers",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.68,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Token Eviction",
      "resolved_canonical": "Token Eviction",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "3D Perception",
      "resolved_canonical": "3D Perception",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.71,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Memory-Bounded Streaming",
      "resolved_canonical": "Memory-Bounded Streaming",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.67,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "3D Reconstruction",
      "resolved_canonical": "3D Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Evict3R: Training-Free Token Eviction for Memory-Bounded Streaming Visual Geometry Transformers

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17650.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17650](https://arxiv.org/abs/2509.17650)

## 🔗 유사한 논문
- [[2025-09-23/FG-Attn_ Leveraging Fine-Grained Sparsity In Diffusion Transformers_20250923|FG-Attn: Leveraging Fine-Grained Sparsity In Diffusion Transformers]] (83.7% similar)
- [[2025-09-23/VQToken_ Neural Discrete Token Representation Learning for Extreme Token Reduction in Video Large Language Models_20250923|VQToken: Neural Discrete Token Representation Learning for Extreme Token Reduction in Video Large Language Models]] (83.2% similar)
- [[2025-09-17/Where Do Tokens Go? Understanding Pruning Behaviors in STEP at High Resolutions_20250917|Where Do Tokens Go? Understanding Pruning Behaviors in STEP at High Resolutions]] (83.2% similar)
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (82.0% similar)
- [[2025-09-23/4D-MoDe_ Towards Editable and Scalable Volumetric Streaming via Motion-Decoupled 4D Gaussian Compression_20250923|4D-MoDe: Towards Editable and Scalable Volumetric Streaming via Motion-Decoupled 4D Gaussian Compression]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/3D Perception|3D Perception]], [[keywords/3D Reconstruction|3D Reconstruction]]
**⚡ Unique Technical**: [[keywords/Token Eviction|Token Eviction]], [[keywords/Memory-Bounded Streaming|Memory-Bounded Streaming]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17650v1 Announce Type: new 
Abstract: Streaming visual transformers like StreamVGGT achieve strong 3D perception but suffer from unbounded growth of key value (KV) memory, which limits scalability. We propose a training-free, inference-time token eviction policy that bounds memory by discarding redundant tokens while keeping the most informative ones. Our method uses significantly less memory with little to no drop in accuracy: on 7-Scenes with long sequences it reduces peak memory from 18.63 GB to 9.39 GB while accuracy and completeness drop by only 0.003. Under strict memory budgets, eviction enables denser frame sampling, which improves reconstruction accuracy compared to the baseline. Experiments across video depth estimation (Sintel, KITTI), 3D reconstruction (7-Scenes, NRGBD), and camera pose estimation (Sintel, TUM-dynamics) show that our approach closely matches StreamVGGT at a fraction of the memory and makes long-horizon streaming inference more practical.

## 📝 요약

이 논문은 스트리밍 비주얼 트랜스포머의 메모리 문제를 해결하기 위해 훈련 없이 추론 시에 불필요한 토큰을 제거하는 방법을 제안합니다. 제안된 방법은 메모리를 크게 절약하면서도 정확도 저하를 최소화합니다. 7-Scenes 데이터셋에서 메모리 사용량을 18.63GB에서 9.39GB로 줄이면서 정확도는 거의 유지됩니다. 이 방법은 메모리 제약이 있는 상황에서 프레임 샘플링을 더 촘촘히 하여 재구성 정확도를 향상시킵니다. 실험 결과, 제안된 방법은 다양한 데이터셋에서 기존 방법과 유사한 성능을 보이면서 메모리 사용량을 크게 줄여 장기 스트리밍 추론의 실용성을 높입니다.

## 🎯 주요 포인트

- 1. StreamVGGT와 같은 스트리밍 비주얼 트랜스포머는 강력한 3D 인식을 제공하지만, 무한히 증가하는 키 값 메모리로 인해 확장성에 제한이 있습니다.
- 2. 우리는 훈련 없이 추론 시점에서 불필요한 토큰을 제거하여 메모리를 제한하는 토큰 제거 정책을 제안합니다.
- 3. 제안된 방법은 메모리를 크게 줄이면서도 정확도 저하가 거의 없으며, 7-Scenes 데이터셋에서 메모리를 18.63GB에서 9.39GB로 줄였습니다.
- 4. 엄격한 메모리 제한 하에서는 제거 정책이 더 조밀한 프레임 샘플링을 가능하게 하여 재구성 정확도를 향상시킵니다.
- 5. 다양한 실험 결과, 제안된 방법은 StreamVGGT와 유사한 성능을 보이며, 메모리 사용량을 크게 줄여 장기 스트리밍 추론을 더 실용적으로 만듭니다.


---

*Generated on 2025-09-24 04:58:13*