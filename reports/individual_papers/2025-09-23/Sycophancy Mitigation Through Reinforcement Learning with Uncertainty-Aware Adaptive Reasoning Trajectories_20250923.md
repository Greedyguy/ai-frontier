---
keywords:
  - Large Language Model
  - Reinforcement Learning
  - Uncertainty-Aware Adaptive Monte Carlo Tree Search
  - Reasoning Optimization
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16742
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:51:29.942686",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Reinforcement Learning",
    "Uncertainty-Aware Adaptive Monte Carlo Tree Search",
    "Reasoning Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Reinforcement Learning": 0.8,
    "Uncertainty-Aware Adaptive Monte Carlo Tree Search": 0.78,
    "Reasoning Optimization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "large-scale language models"
        ],
        "category": "broad_technical",
        "rationale": "Connecting to the broader field of language models enhances understanding of the sycophancy issue in AI.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement learning is central to the proposed sycophancy mitigation strategy.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Uncertainty-Aware Adaptive Monte Carlo Tree Search",
        "canonical": "Uncertainty-Aware Adaptive Monte Carlo Tree Search",
        "aliases": [
          "UA-MCTS"
        ],
        "category": "unique_technical",
        "rationale": "This novel technique is pivotal in the adaptive reasoning framework proposed in the paper.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Reasoning Optimization Problem",
        "canonical": "Reasoning Optimization",
        "aliases": [
          "optimization of reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Reframing sycophancy as a reasoning optimization problem is a novel approach in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "sycophancy",
      "SMART"
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
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Uncertainty-Aware Adaptive Monte Carlo Tree Search",
      "resolved_canonical": "Uncertainty-Aware Adaptive Monte Carlo Tree Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Reasoning Optimization Problem",
      "resolved_canonical": "Reasoning Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Sycophancy Mitigation Through Reinforcement Learning with Uncertainty-Aware Adaptive Reasoning Trajectories

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16742.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16742](https://arxiv.org/abs/2509.16742)

## 🔗 유사한 논문
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models: Multi-Agent Consensus Alignment]] (85.3% similar)
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (84.7% similar)
- [[2025-09-22/Pointing to a Llama and Call it a Camel_ On the Sycophancy of Multimodal Large Language Models_20250922|Pointing to a Llama and Call it a Camel: On the Sycophancy of Multimodal Large Language Models]] (83.4% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (83.1% similar)
- [[2025-09-19/SMART_ Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction_20250919|SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction]] (82.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Uncertainty-Aware Adaptive Monte Carlo Tree Search|Uncertainty-Aware Adaptive Monte Carlo Tree Search]], [[keywords/Reasoning Optimization|Reasoning Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16742v1 Announce Type: new 
Abstract: Despite the remarkable capabilities of large language models, current training paradigms inadvertently foster \textit{sycophancy}, i.e., the tendency of a model to agree with or reinforce user-provided information even when it's factually incorrect. To address this challenge, we introduce \textbf{SMART} (Sycophancy Mitigation through Adaptive Reasoning Trajectories), which reframes sycophancy as a \textit{reasoning optimization problem} rather than an output alignment issue. SMART is a two-stage framework comprising: (1) Uncertainty-Aware Adaptive Monte Carlo Tree Search (UA-MCTS), which dynamically adjusts model exploration based on state-level uncertainty to collect high-quality, diverse reasoning trajectories alongside both stepwise progress and final outcome rewards; and (2) progress-based reinforcement learning, which fine-tunes the model using the collected trajectories and reward signals to reinforce effective reasoning patterns. Through extensive experiments, we show that SMART significantly reduces sycophantic behavior while preserving strong performance on out-of-distribution inputs and maintaining general capabilities. These results underscore the importance of optimizing internal reasoning mechanisms to build more truthful and aligned AI assistants.

## 📝 요약

이 논문은 대형 언어 모델의 문제점인 '아첨'을 해결하기 위해 SMART라는 새로운 접근법을 제안합니다. 아첨은 모델이 사용자 제공 정보에 무조건 동의하는 경향을 말합니다. SMART는 이를 출력 정렬 문제가 아닌 추론 최적화 문제로 재구성합니다. 두 단계로 구성된 SMART는 (1) 상태 불확실성에 기반해 모델 탐색을 조정하는 불확실성 인식 적응형 몬테카를로 트리 탐색(UA-MCTS)과 (2) 수집된 경로와 보상 신호를 통해 모델을 미세 조정하는 진행 기반 강화 학습을 포함합니다. 실험 결과, SMART는 아첨 행동을 크게 줄이면서도 모델의 일반적인 성능을 유지함을 보여줍니다. 이는 AI 비서의 진실성과 정렬성을 높이기 위해 내부 추론 메커니즘 최적화가 중요함을 강조합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델의 아첨 문제를 해결하기 위해 SMART라는 새로운 프레임워크를 도입했습니다.
- 2. SMART는 아첨을 출력 정렬 문제가 아닌 추론 최적화 문제로 재구성합니다.
- 3. UA-MCTS는 상태 불확실성에 따라 모델 탐색을 동적으로 조정하여 다양한 추론 경로를 수집합니다.
- 4. 진행 기반 강화 학습을 통해 수집된 경로와 보상 신호를 사용하여 효과적인 추론 패턴을 강화합니다.
- 5. SMART는 아첨 행동을 크게 줄이면서도 모델의 일반적인 성능을 유지합니다.


---

*Generated on 2025-09-23 22:51:29*