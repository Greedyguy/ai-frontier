---
keywords:
  - Reinforcement Learning
  - Heterogeneous Adaptive Policy Optimization
  - Adaptive Temperature Sampling
  - Token Level Group Average
  - Asymmetric Adaptive Clipping
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16591
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:14:24.350444",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Heterogeneous Adaptive Policy Optimization",
    "Adaptive Temperature Sampling",
    "Token Level Group Average",
    "Asymmetric Adaptive Clipping"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning": 0.78,
    "Heterogeneous Adaptive Policy Optimization": 0.8,
    "Adaptive Temperature Sampling": 0.75,
    "Token Level Group Average": 0.72,
    "Asymmetric Adaptive Clipping": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a foundational concept in optimizing reasoning processes in LLMs, providing strong connectivity to related works.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Heterogeneous Adaptive Policy Optimization",
        "canonical": "Heterogeneous Adaptive Policy Optimization",
        "aliases": [
          "HAPO"
        ],
        "category": "unique_technical",
        "rationale": "HAPO is a novel algorithm introduced in the paper, offering a unique approach to token-aware optimization.",
        "novelty_score": 0.92,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Adaptive Temperature Sampling",
        "canonical": "Adaptive Temperature Sampling",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is crucial for dynamically adjusting sampling strategies based on token entropy, enhancing exploration.",
        "novelty_score": 0.87,
        "connectivity_score": 0.55,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Token Level Group Average",
        "canonical": "Token Level Group Average",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This method normalizes advantages at the token level, contributing to fine-grained control in optimization.",
        "novelty_score": 0.78,
        "connectivity_score": 0.5,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "Asymmetric Adaptive Clipping",
        "canonical": "Asymmetric Adaptive Clipping",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This approach allows for targeted probability adjustments, crucial for managing token-level noise and exploration.",
        "novelty_score": 0.85,
        "connectivity_score": 0.52,
        "specificity_score": 0.83,
        "link_intent_score": 0.74
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
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Heterogeneous Adaptive Policy Optimization",
      "resolved_canonical": "Heterogeneous Adaptive Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Adaptive Temperature Sampling",
      "resolved_canonical": "Adaptive Temperature Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.87,
        "connectivity": 0.55,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Token Level Group Average",
      "resolved_canonical": "Token Level Group Average",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.5,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Asymmetric Adaptive Clipping",
      "resolved_canonical": "Asymmetric Adaptive Clipping",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.52,
        "specificity": 0.83,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# From Uniform to Heterogeneous: Tailoring Policy Optimization to Every Token's Nature

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16591.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16591](https://arxiv.org/abs/2509.16591)

## 🔗 유사한 논문
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (85.0% similar)
- [[2025-09-23/Adaptive Overclocking_ Dynamic Control of Thinking Path Length via Real-Time Reasoning Signals_20250923|Adaptive Overclocking: Dynamic Control of Thinking Path Length via Real-Time Reasoning Signals]] (84.0% similar)
- [[2025-09-23/Building Coding Agents via Entropy-Enhanced Multi-Turn Preference Optimization_20250923|Building Coding Agents via Entropy-Enhanced Multi-Turn Preference Optimization]] (83.4% similar)
- [[2025-09-22/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250922|Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (83.2% similar)
- [[2025-09-23/GPO_ Learning from Critical Steps to Improve LLM Reasoning_20250923|GPO: Learning from Critical Steps to Improve LLM Reasoning]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Heterogeneous Adaptive Policy Optimization|Heterogeneous Adaptive Policy Optimization]], [[keywords/Adaptive Temperature Sampling|Adaptive Temperature Sampling]], [[keywords/Token Level Group Average|Token Level Group Average]], [[keywords/Asymmetric Adaptive Clipping|Asymmetric Adaptive Clipping]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16591v1 Announce Type: new 
Abstract: Reinforcement Learning has emerged as the fundamental technique for enhancing reasoning in LLMs. However, existing algorithms apply uniform optimization to all tokens, ignoring their different roles in reasoning process. To address this limitation, we introduce Heterogeneous Adaptive Policy Optimization (HAPO), a comprehensive token-aware algorithm that dynamically adapts optimization based on token entropy. For rollout sampling, we propose Adaptive Temperature Sampling, which adjusts sampling temperature in real time, promoting exploration at high-entropy tokens while preserving coherence at low-entropy ones. For advantage calculation, we introduce Token Level Group Average that normalizes advantages at token level, jointly accounting for sequence-length as in token-mean loss while preserving non-biased treatment. We then develop Differential Advantage Redistribution that leverages entropy and importance ratios to modulate rewards-adjusting updates for tokens with clear signals. For clipping loss, we design Asymmetric Adaptive Clipping, allowing aggressive probability reduction for noisy low-entropy tokens while enabling exploration for high-entropy tokens. Through systematic investigation between entropy and training dynamics, we embedded token-level treatment into every stages to achieve fine-grained control. Extensive experiments demonstrate that HAPO consistently outperforms DAPO across multiple model scales. Our code can be found in https://github.com/starriver030515/HAPO.

## 📝 요약

강화 학습은 대형 언어 모델(LLM)의 추론 능력을 향상시키는 핵심 기술로 자리 잡았습니다. 그러나 기존 알고리즘은 모든 토큰에 동일한 최적화를 적용하여, 추론 과정에서의 토큰 역할 차이를 무시합니다. 이를 해결하기 위해, 우리는 Heterogeneous Adaptive Policy Optimization (HAPO)을 제안합니다. HAPO는 토큰 엔트로피에 기반하여 최적화를 동적으로 조정하는 알고리즘입니다. Adaptive Temperature Sampling을 통해 롤아웃 샘플링 시 실시간으로 샘플링 온도를 조절하여, 엔트로피가 높은 토큰에서는 탐색을 촉진하고, 낮은 토큰에서는 일관성을 유지합니다. 또한, Token Level Group Average를 도입하여 토큰 수준에서 이점을 정규화하며, Differential Advantage Redistribution을 통해 명확한 신호를 가진 토큰의 보상 조정을 최적화합니다. Asymmetric Adaptive Clipping은 엔트로피가 낮은 토큰에 대해 공격적인 확률 감소를 허용하고, 높은 토큰에서는 탐색을 가능하게 합니다. 실험 결과, HAPO는 다양한 모델 규모에서 DAPO보다 일관되게 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. HAPO는 토큰의 엔트로피에 기반하여 최적화를 동적으로 조정하는 토큰 인식 알고리즘입니다.
- 2. Adaptive Temperature Sampling은 엔트로피 수준에 따라 샘플링 온도를 실시간으로 조정하여 탐색과 일관성을 조절합니다.
- 3. Token Level Group Average는 토큰 수준에서의 이점을 정규화하여 시퀀스 길이를 고려하면서도 편향 없는 처리를 유지합니다.
- 4. Differential Advantage Redistribution은 엔트로피와 중요도 비율을 활용하여 명확한 신호를 가진 토큰의 보상 조정을 최적화합니다.
- 5. Asymmetric Adaptive Clipping은 엔트로피 수준에 따라 확률 감소와 탐색을 조절하여 훈련 동적성을 개선합니다.


---

*Generated on 2025-09-24 03:14:24*