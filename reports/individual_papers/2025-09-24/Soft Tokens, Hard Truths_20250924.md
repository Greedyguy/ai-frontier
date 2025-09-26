<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:14:44.166482",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Chain-of-Thought",
    "Continuous Tokens",
    "Reinforcement Learning",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Chain-of-Thought": 0.78,
    "Continuous Tokens": 0.82,
    "Reinforcement Learning": 0.75,
    "Large Language Model": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Chain-of-Thought",
        "canonical": "Chain-of-Thought",
        "aliases": [
          "CoT"
        ],
        "category": "unique_technical",
        "rationale": "Chain-of-Thought is a unique reasoning approach in LLMs, crucial for understanding the paper's focus on continuous tokens.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "continuous tokens",
        "canonical": "Continuous Tokens",
        "aliases": [
          "soft tokens"
        ],
        "category": "unique_technical",
        "rationale": "Continuous tokens are central to the paper's novel approach, offering a new perspective on token usage in LLMs.",
        "novelty_score": 0.8,
        "connectivity_score": 0.72,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "reinforcement learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a key method used in the paper to train continuous CoTs, linking it to broader machine learning strategies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Llama and Qwen models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Llama",
          "Qwen"
        ],
        "category": "broad_technical",
        "rationale": "These models are specific instances of LLMs, relevant for understanding the context and application of the study.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "training difficulties",
      "computational costs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Chain-of-Thought",
      "resolved_canonical": "Chain-of-Thought",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "continuous tokens",
      "resolved_canonical": "Continuous Tokens",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.72,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "reinforcement learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Llama and Qwen models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Soft Tokens, Hard Truths

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19170.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19170](https://arxiv.org/abs/2509.19170)

## 🔗 유사한 논문
- [[2025-09-23/EvoCoT_ Overcoming the Exploration Bottleneck in Reinforcement Learning_20250923|EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning]] (86.2% similar)
- [[2025-09-18/Early Stopping Chain-of-thoughts in Large Language Models_20250918|Early Stopping Chain-of-thoughts in Large Language Models]] (83.9% similar)
- [[2025-09-23/LTA-thinker_ Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning_20250923|LTA-thinker: Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning]] (83.3% similar)
- [[2025-09-17/Reasoning Efficiently Through Adaptive Chain-of-Thought Compression_ A Self-Optimizing Framework_20250917|Reasoning Efficiently Through Adaptive Chain-of-Thought Compression: A Self-Optimizing Framework]] (83.1% similar)
- [[2025-09-19/Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning_20250919|Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]], [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Chain-of-Thought|Chain-of-Thought]], [[keywords/Continuous Tokens|Continuous Tokens]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19170v1 Announce Type: cross 
Abstract: The use of continuous instead of discrete tokens during the Chain-of-Thought (CoT) phase of reasoning LLMs has garnered attention recently, based on the intuition that a continuous mixture of discrete tokens could simulate a superposition of several reasoning paths simultaneously. Theoretical results have formally proven that continuous tokens have much greater expressivity and can solve specific problems more efficiently. However, practical use of continuous tokens has been limited by strong training difficulties: previous works either just use continuous tokens at inference time on a pre-trained discrete-token model, or must distill the continuous CoT from ground-truth discrete CoTs and face computational costs that limit the CoT to very few tokens.
  This is the first work introducing a scalable method to learn continuous CoTs via reinforcement learning (RL), without distilling from reference discrete CoTs. We use "soft" tokens: mixtures of tokens together with noise on the input embedding to provide RL exploration. Computational overhead is minimal, enabling us to learn continuous CoTs with hundreds of tokens. On math reasoning benchmarks with Llama and Qwen models up to 8B, training with continuous CoTs match discrete-token CoTs for pass@1 and surpass them for pass@32, showing greater CoT diversity. In systematic comparisons, the best-performing scenario is to train with continuous CoT tokens then use discrete tokens for inference, meaning the "soft" models can be deployed in a standard way. Finally, we show continuous CoT RL training better preserves the predictions of the base model on out-of-domain tasks, thus providing a softer touch to the base model.

## 📝 요약

이 논문은 연속적인 토큰을 활용한 연쇄 사고(Chain-of-Thought, CoT) 학습 방법을 제안합니다. 기존의 이산 토큰 대신 연속 토큰을 사용하면 여러 사고 경로를 동시에 시뮬레이션할 수 있어 문제 해결 능력이 향상됩니다. 그러나 연속 토큰의 실용성은 학습의 어려움 때문에 제한적이었습니다. 본 연구는 참조 이산 CoT 없이 강화 학습(RL)을 통해 연속 CoT를 학습하는 확장 가능한 방법을 처음으로 도입했습니다. "소프트" 토큰과 입력 임베딩에 노이즈를 추가하여 RL 탐색을 촉진하며, 최소한의 계산 비용으로 수백 개의 토큰을 학습할 수 있습니다. Llama 및 Qwen 모델을 사용한 수학적 추론 벤치마크에서 연속 CoT는 이산 CoT와 유사한 성능을 보였으며, 특히 pass@32에서 더 나은 성과를 나타냈습니다. 최적의 성과는 연속 CoT로 학습한 후 이산 토큰으로 추론할 때 나타났으며, 이는 "소프트" 모델이 표준 방식으로 배포될 수 있음을 의미합니다. 또한, 연속 CoT RL 학습은 기본 모델의 예측을 더 잘 보존하여 모델의 유연성을 높입니다.

## 🎯 주요 포인트

- 1. 연속적인 토큰을 사용한 Chain-of-Thought(연쇄적 사고) 방식이 이론적으로 더 높은 표현력을 가지며 특정 문제를 더 효율적으로 해결할 수 있음을 증명했습니다.
- 2. 이 연구는 참조 이산 토큰 없이 강화 학습을 통해 연속적인 CoT를 학습하는 확장 가능한 방법을 처음으로 도입했습니다.
- 3. "소프트" 토큰을 사용하여 입력 임베딩에 노이즈를 추가함으로써 강화 학습 탐색을 가능하게 하고, 수백 개의 연속적인 CoT 토큰을 학습할 수 있습니다.
- 4. 수학적 추론 벤치마크에서 연속적인 CoT로 훈련한 모델이 이산 토큰 CoT와 비교하여 더 높은 다양성을 보여줍니다.
- 5. 연속적인 CoT 강화 학습은 기본 모델의 예측을 더 잘 보존하여, 모델의 기본 성능에 부드러운 영향을 미칩니다.


---

*Generated on 2025-09-24 14:14:44*