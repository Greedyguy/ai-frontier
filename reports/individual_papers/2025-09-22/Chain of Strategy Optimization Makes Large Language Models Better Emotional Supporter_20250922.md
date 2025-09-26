---
keywords:
  - Large Language Model
  - Emotional Support Conversations
  - Chain-of-Strategy Optimization
  - Monte Carlo Tree Search
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2503.05362
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:42:26.859233",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Emotional Support Conversations",
    "Chain-of-Strategy Optimization",
    "Monte Carlo Tree Search"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Emotional Support Conversations": 0.7,
    "Chain-of-Strategy Optimization": 0.8,
    "Monte Carlo Tree Search": 0.78
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
        "rationale": "Large Language Models are central to the paper's discussion and connect broadly with existing research in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Emotional Support Conversations",
        "canonical": "Emotional Support Conversations",
        "aliases": [
          "ESC"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application context for LLMs, highlighting a unique domain of interaction.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Chain-of-Strategy Optimization",
        "canonical": "Chain-of-Strategy Optimization",
        "aliases": [
          "CSO"
        ],
        "category": "unique_technical",
        "rationale": "This novel approach is central to the paper's contribution and represents a unique method for improving LLMs.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Monte Carlo Tree Search",
        "canonical": "Monte Carlo Tree Search",
        "aliases": [
          "MCTS"
        ],
        "category": "specific_connectable",
        "rationale": "A well-known method used in the paper to enhance strategy optimization, linking to broader AI techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "strategy selection accuracy",
      "preference bias",
      "fine-tuning"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Emotional Support Conversations",
      "resolved_canonical": "Emotional Support Conversations",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Chain-of-Strategy Optimization",
      "resolved_canonical": "Chain-of-Strategy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Monte Carlo Tree Search",
      "resolved_canonical": "Monte Carlo Tree Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Chain of Strategy Optimization Makes Large Language Models Better Emotional Supporter

**Korean Title:** 전략 최적화의 연쇄가 대형 언어 모델을 더 나은 감정 지원자로 만든다

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2503.05362.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2503.05362](https://arxiv.org/abs/2503.05362)

## 🔗 유사한 논문
- [[2025-09-22/Empathy-R1_ A Chain-of-Empathy and Reinforcement Learning Framework for Long-Form Mental Health Support_20250922|Empathy-R1: A Chain-of-Empathy and Reinforcement Learning Framework for Long-Form Mental Health Support]] (81.0% similar)
- [[2025-09-22/Beyond Linear Steering_ Unified Multi-Attribute Control for Language Models_20250922|Beyond Linear Steering: Unified Multi-Attribute Control for Language Models]] (80.5% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (80.3% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (80.1% similar)
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Monte Carlo Tree Search|Monte Carlo Tree Search]]
**⚡ Unique Technical**: [[keywords/Emotional Support Conversations|Emotional Support Conversations]], [[keywords/Chain-of-Strategy Optimization|Chain-of-Strategy Optimization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.05362v3 Announce Type: replace 
Abstract: The growing emotional stress in modern society has increased the demand for Emotional Support Conversations (ESC). While Large Language Models (LLMs) show promise for ESC, they face two key challenges: (1) low strategy selection accuracy, and (2) preference bias, limiting their adaptability to emotional needs of users. Existing supervised fine-tuning (SFT) struggles to address these issues, as it rigidly trains models on single gold-standard responses without modeling nuanced strategy trade-offs. To overcome these limitations, we propose Chain-of-Strategy Optimization (CSO), a novel approach that optimizes strategy selection preferences at each dialogue turn. We first leverage Monte Carlo Tree Search to construct ESC-Pro, a high-quality preference dataset with turn-level strategy-response pairs. Training on ESC-Pro with CSO improves both strategy accuracy and bias mitigation, enabling LLMs to generate more empathetic and contextually appropriate responses. Experiments on LLaMA-3.1-8B, Gemma-2-9B, and Qwen2.5-7B demonstrate that CSO outperforms standard SFT, highlighting the efficacy of fine-grained, turn-level preference modeling in ESC.

## 🔍 Abstract (한글 번역)

arXiv:2503.05362v3 발표 유형: 교체  
초록: 현대 사회에서 증가하는 정서적 스트레스는 정서적 지원 대화(ESC)에 대한 수요를 증가시켰습니다. 대형 언어 모델(LLM)은 ESC에 유망한 가능성을 보여주지만, 두 가지 주요 과제에 직면해 있습니다: (1) 낮은 전략 선택 정확도, (2) 사용자 정서적 요구에 대한 적응성을 제한하는 선호 편향. 기존의 지도 학습(SFT)은 단일 표준 응답에 모델을 엄격하게 훈련시키면서 미묘한 전략적 절충을 모델링하지 못해 이러한 문제를 해결하는 데 어려움을 겪고 있습니다. 이러한 한계를 극복하기 위해, 우리는 각 대화 턴에서 전략 선택 선호도를 최적화하는 새로운 접근법인 전략 체인 최적화(CSO)를 제안합니다. 먼저 몬테카를로 트리 탐색을 활용하여 턴 수준의 전략-응답 쌍으로 구성된 고품질 선호 데이터셋인 ESC-Pro를 구축합니다. CSO를 사용하여 ESC-Pro에서 훈련하면 전략 정확도와 편향 완화가 모두 향상되어, LLM이 더 공감적이고 상황에 적절한 응답을 생성할 수 있게 됩니다. LLaMA-3.1-8B, Gemma-2-9B, Qwen2.5-7B에 대한 실험은 CSO가 표준 SFT보다 우수하다는 것을 입증하며, ESC에서 세밀하고 턴 수준의 선호 모델링의 효율성을 강조합니다.

## 📝 요약

현대 사회의 감정적 스트레스 증가로 감정 지원 대화(ESC)에 대한 수요가 증가하고 있습니다. 대형 언어 모델(LLM)은 ESC에 유망하지만, 전략 선택 정확도가 낮고 사용자 감정에 대한 적응성이 제한되는 편향 문제를 겪고 있습니다. 기존의 지도 학습은 단일 정답에만 집중하여 이러한 문제를 해결하기 어렵습니다. 이를 극복하기 위해, 우리는 대화의 각 턴에서 전략 선택을 최적화하는 새로운 접근법인 전략 체인 최적화(CSO)를 제안합니다. 몬테카를로 트리 탐색을 활용해 턴 수준의 전략-응답 쌍을 포함한 고품질 데이터셋 ESC-Pro를 구축하고, 이를 통해 CSO를 훈련하여 전략 정확도와 편향 완화를 개선했습니다. 실험 결과, CSO가 기존의 지도 학습보다 우수한 성능을 보이며, 감정 지원 대화에서의 세밀한 선호도 모델링의 효과를 입증했습니다.

## 🎯 주요 포인트

- 1. 현대 사회의 감정적 스트레스 증가로 인해 감정 지원 대화(ESC)에 대한 수요가 증가하고 있다.
- 2. 대형 언어 모델(LLM)은 ESC에 유망하지만, 전략 선택 정확도 낮음과 선호 편향이라는 두 가지 주요 문제에 직면하고 있다.
- 3. 기존의 지도 학습 미세 조정(SFT)은 단일 정답에 모델을 훈련시켜 전략 선택의 미묘한 균형을 모델링하지 못한다.
- 4. 체인 오브 스트래티지 최적화(CSO)는 각 대화 턴에서 전략 선택 선호도를 최적화하여 이러한 한계를 극복한다.
- 5. CSO는 ESC-Pro 데이터셋을 활용하여 전략 정확도와 편향 완화를 개선하고, 더 공감적이고 상황에 맞는 응답을 생성할 수 있게 한다.


---

*Generated on 2025-09-23 11:42:26*