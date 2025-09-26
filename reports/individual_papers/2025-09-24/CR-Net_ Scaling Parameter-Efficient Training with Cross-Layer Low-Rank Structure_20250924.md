<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:58:14.262926",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Low-rank Architecture",
    "Large Language Model",
    "CR-Net",
    "Activation Recomputation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Low-rank Architecture": 0.82,
    "Large Language Model": 0.85,
    "CR-Net": 0.88,
    "Activation Recomputation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Low-rank architectures",
        "canonical": "Low-rank Architecture",
        "aliases": [
          "Low-rank Models"
        ],
        "category": "unique_technical",
        "rationale": "Low-rank architectures are central to the paper's contribution and provide a novel approach to parameter efficiency in large models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Large language model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large language models are the primary context for the application of the proposed method.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cross-layer Low-Rank residual Network",
        "canonical": "CR-Net",
        "aliases": [
          "Cross-layer Low-Rank Network"
        ],
        "category": "unique_technical",
        "rationale": "CR-Net is the novel framework introduced in the paper, representing a significant advancement in low-rank model training.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Activation recomputation strategy",
        "canonical": "Activation Recomputation",
        "aliases": [
          "Memory Reduction Strategy"
        ],
        "category": "specific_connectable",
        "rationale": "This strategy is crucial for reducing memory requirements, a key challenge addressed by the paper.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
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
      "candidate_surface": "Low-rank architectures",
      "resolved_canonical": "Low-rank Architecture",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Large language model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cross-layer Low-Rank residual Network",
      "resolved_canonical": "CR-Net",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Activation recomputation strategy",
      "resolved_canonical": "Activation Recomputation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# CR-Net: Scaling Parameter-Efficient Training with Cross-Layer Low-Rank Structure

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18993.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18993](https://arxiv.org/abs/2509.18993)

## 🔗 유사한 논문
- [[2025-09-22/Sparsity May Be All You Need_ Sparse Random Parameter Adaptation_20250922|Sparsity May Be All You Need: Sparse Random Parameter Adaptation]] (84.5% similar)
- [[2025-09-24/HyperAdapt_ Simple High-Rank Adaptation_20250924|HyperAdapt: Simple High-Rank Adaptation]] (84.4% similar)
- [[2025-09-23/Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks_20250923|Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks]] (83.9% similar)
- [[2025-09-23/A geometric framework for momentum-based optimizers for low-rank training_20250923|A geometric framework for momentum-based optimizers for low-rank training]] (83.8% similar)
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Activation Recomputation|Activation Recomputation]]
**⚡ Unique Technical**: [[keywords/Low-rank Architecture|Low-rank Architecture]], [[keywords/CR-Net|CR-Net]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18993v1 Announce Type: new 
Abstract: Low-rank architectures have become increasingly important for efficient large language model (LLM) pre-training, providing substantial reductions in both parameter complexity and memory/computational demands. Despite these advantages, current low-rank methods face three critical shortcomings: (1) compromised model performance, (2) considerable computational overhead, and (3) limited activation memory savings. To address these limitations, we propose Cross-layer Low-Rank residual Network (CR-Net), an innovative parameter-efficient framework inspired by our discovery that inter-layer activation residuals possess low-rank properties. CR-Net implements this insight through a dual-path architecture that efficiently reconstructs layer activations by combining previous-layer outputs with their low-rank differences, thereby maintaining high-rank information with minimal parameters. We further develop a specialized activation recomputation strategy tailored for CR-Net that dramatically reduces memory requirements. Extensive pre-training experiments across model scales from 60M to 7B parameters demonstrate that CR-Net consistently outperforms state-of-the-art low-rank frameworks while requiring fewer computational resources and less memory.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 효율적인 사전 학습을 위한 저랭크(low-rank) 아키텍처의 중요성을 다루며, 기존 방법의 성능 저하, 높은 계산 비용, 제한된 메모리 절약 문제를 해결하기 위해 CR-Net을 제안합니다. CR-Net은 층 간 활성화 잔차의 저랭크 특성을 활용하여, 이전 층의 출력과 저랭크 차이를 결합하는 이중 경로 아키텍처로 고랭크 정보를 유지하면서도 매개변수를 최소화합니다. 또한, CR-Net에 특화된 활성화 재계산 전략을 개발하여 메모리 요구 사항을 크게 줄였습니다. 60M에서 7B 매개변수 규모의 모델을 대상으로 한 실험에서, CR-Net은 기존 저랭크 프레임워크보다 적은 자원으로 일관되게 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 저차원 아키텍처는 대형 언어 모델의 효율적인 사전 훈련을 위해 중요해지고 있으며, 매개변수 복잡성과 메모리/계산 요구 사항을 크게 줄여준다.
- 2. 기존 저차원 방법은 모델 성능 저하, 상당한 계산 오버헤드, 제한된 활성화 메모리 절감이라는 세 가지 주요 단점을 가지고 있다.
- 3. CR-Net은 층 간 활성화 잔차의 저차원 특성을 활용하여 매개변수 효율적인 프레임워크를 제공하며, 이전 층 출력과 저차원 차이를 결합하여 층 활성화를 효율적으로 재구성한다.
- 4. CR-Net에 특화된 활성화 재계산 전략을 개발하여 메모리 요구 사항을 크게 줄였다.
- 5. 60M에서 7B 매개변수에 이르는 다양한 모델 규모의 사전 훈련 실험에서 CR-Net은 최신 저차원 프레임워크보다 일관되게 우수한 성능을 보이며, 더 적은 계산 자원과 메모리를 필요로 한다.


---

*Generated on 2025-09-24 14:58:14*