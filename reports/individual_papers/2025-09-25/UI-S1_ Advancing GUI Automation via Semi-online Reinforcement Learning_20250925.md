---
keywords:
  - Semi-online Reinforcement Learning
  - Graphical User Interface
  - Discounted Future Returns
  - Multi-turn Reasoning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.11543
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:34:46.015124",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Semi-online Reinforcement Learning",
    "Graphical User Interface",
    "Discounted Future Returns",
    "Multi-turn Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Semi-online Reinforcement Learning": 0.78,
    "Graphical User Interface": 0.72,
    "Discounted Future Returns": 0.65,
    "Multi-turn Reasoning": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Semi-online Reinforcement Learning",
        "canonical": "Semi-online Reinforcement Learning",
        "aliases": [
          "Semi-online RL"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel paradigm that bridges offline and online RL, enhancing connectivity with reinforcement learning topics.",
        "novelty_score": 0.85,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Graphical User Interface agents",
        "canonical": "Graphical User Interface",
        "aliases": [
          "GUI agents"
        ],
        "category": "specific_connectable",
        "rationale": "Connects with existing GUI automation and agent-based interaction frameworks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Discounted future returns",
        "canonical": "Discounted Future Returns",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Essential for understanding reward computation in the proposed RL paradigm.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.65
      },
      {
        "surface": "Multi-turn reasoning",
        "canonical": "Multi-turn Reasoning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Links to broader discussions on dialogue systems and reasoning tasks in AI.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "offline RL",
      "online RL",
      "SOTA performance",
      "real-world evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Semi-online Reinforcement Learning",
      "resolved_canonical": "Semi-online Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Graphical User Interface agents",
      "resolved_canonical": "Graphical User Interface",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Discounted future returns",
      "resolved_canonical": "Discounted Future Returns",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "Multi-turn reasoning",
      "resolved_canonical": "Multi-turn Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# UI-S1: Advancing GUI Automation via Semi-online Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.11543.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.11543](https://arxiv.org/abs/2509.11543)

## 🔗 유사한 논문
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (87.2% similar)
- [[2025-09-24/MobileRL_ Online Agentic Reinforcement Learning for Mobile GUI Agents_20250924|MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents]] (86.2% similar)
- [[2025-09-23/Mano Report_20250923|Mano Report]] (85.3% similar)
- [[2025-09-18/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250918|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (85.1% similar)
- [[2025-09-24/Online Process Reward Leanring for Agentic Reinforcement Learning_20250924|Online Process Reward Leanring for Agentic Reinforcement Learning]] (85.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graphical User Interface|Graphical User Interface]], [[keywords/Multi-turn Reasoning|Multi-turn Reasoning]]
**⚡ Unique Technical**: [[keywords/Semi-online Reinforcement Learning|Semi-online Reinforcement Learning]], [[keywords/Discounted Future Returns|Discounted Future Returns]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.11543v2 Announce Type: replace-cross 
Abstract: Graphical User Interface (GUI) agents have demonstrated remarkable progress in automating complex user interface interactions through reinforcement learning. However, current approaches face a fundamental dilemma: offline RL enables stable training on pre-collected trajectories, but struggles with multi-step task execution for lack of trajectory-level reward signals; online RL captures these signals through environment interaction, but suffers from sparse rewards and prohibitive deployment costs. To address it, we present Semi-online Reinforcement Learning, a novel paradigm that simulates online RL on offline trajectories. During each rollout process, we preserve the original model output within the multi-turn dialogue, where a Patch Module adaptively recovers the divergence between rollout and expert trajectories. To capture long-term training signals, Semi-online RL introduces discounted future returns into the reward computation and optimizes the policy with weighted step-level and episode-level advantages. We further introduce Semi-Online Performance (SOP), a metric that aligns better with true online performance, serving as a practical and effective proxy for real-world evaluation. Experiments show that ours Semi-online RL achieves SOTA performance among 7B models across four dynamic benchmarks, with significant gains over the base model (e.g., +12.0% on AndroidWorld, +23.8% on AITW), demonstrating significant progress in bridging the gap between offline training efficiency and online multi-turn reasoning. The code is available at https://github.com/X-PLUG/MobileAgent/tree/main/UI-S1.

## 📝 요약

이 논문은 GUI 에이전트의 복잡한 사용자 인터페이스 상호작용 자동화를 위한 새로운 강화 학습 패러다임인 세미-온라인 강화 학습을 제안합니다. 기존의 오프라인 강화 학습은 안정적인 훈련을 제공하지만 다단계 작업 실행에 어려움을 겪고, 온라인 강화 학습은 환경 상호작용을 통해 신호를 포착하지만 비용이 많이 듭니다. 이를 해결하기 위해 세미-온라인 강화 학습은 오프라인 궤적에서 온라인 강화 학습을 시뮬레이션하며, 롤아웃 과정에서 패치 모듈을 통해 궤적 간의 차이를 보정합니다. 또한, 장기적인 훈련 신호를 포착하기 위해 할인된 미래 수익을 도입하고, 정책 최적화를 위해 가중치가 부여된 단계별 및 에피소드별 이점을 사용합니다. 실험 결과, 제안된 방법은 7B 모델 중 최고 성능을 달성하며, 오프라인 훈련 효율성과 온라인 다중 턴 추론 간의 격차를 효과적으로 줄였습니다.

## 🎯 주요 포인트

- 1. GUI 에이전트의 복잡한 사용자 인터페이스 상호작용 자동화에서 강화 학습의 진전을 보여줍니다.
- 2. 오프라인 강화 학습은 안정적인 훈련을 가능하게 하지만, 다단계 작업 실행에서 보상 신호 부족 문제를 겪습니다.
- 3. 세미-온라인 강화 학습은 오프라인 궤적에서 온라인 강화 학습을 시뮬레이션하여 이 문제를 해결합니다.
- 4. 세미-온라인 성능(SOP)이라는 새로운 지표를 도입하여 실제 온라인 성능과 더 잘 맞추고 평가의 실용적 대리로 사용합니다.
- 5. 실험 결과, 세미-온라인 강화 학습이 7B 모델에서 SOTA 성능을 달성하며, 오프라인 훈련 효율성과 온라인 다중 턴 추론 간의 격차를 줄이는 데 큰 진전을 보였습니다.


---

*Generated on 2025-09-25 16:34:46*