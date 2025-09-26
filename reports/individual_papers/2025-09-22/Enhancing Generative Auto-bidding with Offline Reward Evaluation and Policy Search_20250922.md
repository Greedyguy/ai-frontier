---
keywords:
  - Auto-bidding
  - Large Language Model
  - Policy Optimization
  - Trajectory Evaluator
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15927
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:20:43.881905",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Auto-bidding",
    "Large Language Model",
    "Policy Optimization",
    "Trajectory Evaluator"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Auto-bidding": 0.75,
    "Large Language Model": 0.8,
    "Policy Optimization": 0.77,
    "Trajectory Evaluator": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Auto-bidding",
        "canonical": "Auto-bidding",
        "aliases": [
          "Automatic Bidding",
          "Programmatic Bidding"
        ],
        "category": "unique_technical",
        "rationale": "Auto-bidding is central to the paper's focus on enhancing advertising strategies through AI, providing a unique technical concept for linking.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are integral to the architecture proposed in the paper, linking to broader AI advancements.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Policy Optimization",
        "canonical": "Policy Optimization",
        "aliases": [
          "Policy Search"
        ],
        "category": "specific_connectable",
        "rationale": "Policy Optimization is a key component of the proposed method, facilitating connections to reinforcement learning techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Trajectory Evaluator",
        "canonical": "Trajectory Evaluator",
        "aliases": [
          "Path Evaluator",
          "Route Evaluator"
        ],
        "category": "unique_technical",
        "rationale": "This concept is novel and specific to the paper's approach, offering a unique point for linking within the context of generative planning.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
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
      "candidate_surface": "Auto-bidding",
      "resolved_canonical": "Auto-bidding",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Policy Optimization",
      "resolved_canonical": "Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Trajectory Evaluator",
      "resolved_canonical": "Trajectory Evaluator",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search

**Korean Title:** 생성적 자동 입찰 향상을 위한 오프라인 보상 평가 및 정책 탐색

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15927.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15927](https://arxiv.org/abs/2509.15927)

## 🔗 유사한 논문
- [[2025-09-19/JU-NLP at Touch\'e_ Covert Advertisement in Conversational AI-Generation and Detection Strategies_20250919|JU-NLP at Touch\'e: Covert Advertisement in Conversational AI-Generation and Detection Strategies]] (83.2% similar)
- [[2025-09-19/Optimal Type-Dependent Liquid Welfare Guarantees for Autobidding Agents with Budgets_20250919|Optimal Type-Dependent Liquid Welfare Guarantees for Autobidding Agents with Budgets]] (82.3% similar)
- [[2025-09-18/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250918|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (81.5% similar)
- [[2025-09-17/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250917|TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (81.4% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Policy Optimization|Policy Optimization]]
**⚡ Unique Technical**: [[keywords/Auto-bidding|Auto-bidding]], [[keywords/Trajectory Evaluator|Trajectory Evaluator]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15927v1 Announce Type: cross 
Abstract: Auto-bidding is an essential tool for advertisers to enhance their advertising performance. Recent progress has shown that AI-Generated Bidding (AIGB), which formulates the auto-bidding as a trajectory generation task and trains a conditional diffusion-based planner on offline data, achieves superior and stable performance compared to typical offline reinforcement learning (RL)-based auto-bidding methods. However, existing AIGB methods still encounter a performance bottleneck due to their neglect of fine-grained generation quality evaluation and inability to explore beyond static datasets. To address this, we propose AIGB-Pearl (\emph{Planning with EvAluator via RL}), a novel method that integrates generative planning and policy optimization. The key to AIGB-Pearl is to construct a non-bootstrapped \emph{trajectory evaluator} to assign rewards and guide policy search, enabling the planner to optimize its generation quality iteratively through interaction. Furthermore, to enhance trajectory evaluator accuracy in offline settings, we incorporate three key techniques: (i) a Large Language Model (LLM)-based architecture for better representational capacity, (ii) hybrid point-wise and pair-wise losses for better score learning, and (iii) adaptive integration of expert feedback for better generalization ability. Extensive experiments on both simulated and real-world advertising systems demonstrate the state-of-the-art performance of our approach.

## 🔍 Abstract (한글 번역)

arXiv:2509.15927v1 발표 유형: 교차  
초록: 자동 입찰은 광고주가 광고 성과를 향상시키기 위한 필수 도구입니다. 최근의 발전은 자동 입찰을 궤적 생성 작업으로 공식화하고 오프라인 데이터에서 조건부 확산 기반 계획자를 훈련하는 AI 생성 입찰(AIGB)이 전형적인 오프라인 강화 학습(RL) 기반 자동 입찰 방법에 비해 우수하고 안정적인 성능을 달성한다는 것을 보여주었습니다. 그러나 기존의 AIGB 방법은 세밀한 생성 품질 평가를 무시하고 정적 데이터셋을 넘어 탐색할 수 없는 문제로 인해 여전히 성능 병목 현상을 겪고 있습니다. 이를 해결하기 위해 우리는 생성 계획과 정책 최적화를 통합한 새로운 방법인 AIGB-Pearl(\emph{RL을 통한 평가자와의 계획})을 제안합니다. AIGB-Pearl의 핵심은 비부트스트랩 \emph{궤적 평가자}를 구성하여 보상을 할당하고 정책 탐색을 안내하여 계획자가 상호작용을 통해 생성 품질을 반복적으로 최적화할 수 있도록 하는 것입니다. 더욱이, 오프라인 환경에서 궤적 평가자의 정확성을 향상시키기 위해 우리는 세 가지 주요 기술을 통합합니다: (i) 더 나은 표현 능력을 위한 대형 언어 모델(LLM) 기반 아키텍처, (ii) 더 나은 점수 학습을 위한 하이브리드 포인트-와이즈 및 페어-와이즈 손실, (iii) 더 나은 일반화 능력을 위한 전문가 피드백의 적응적 통합. 시뮬레이션 및 실제 광고 시스템 모두에서의 광범위한 실험은 우리 접근법의 최첨단 성능을 입증합니다.

## 📝 요약

자동 입찰은 광고주가 광고 성과를 향상시키기 위한 필수 도구입니다. 최근 연구에서는 AI 생성 입찰(AIGB)이 오프라인 데이터를 기반으로 조건부 확산 기반 계획자를 훈련하여 전형적인 오프라인 강화 학습 기반 자동 입찰 방법보다 우수하고 안정적인 성능을 보여주었습니다. 그러나 기존 AIGB 방법은 세밀한 생성 품질 평가를 간과하고 정적 데이터셋을 넘어 탐색하지 못해 성능 한계에 직면합니다. 이를 해결하기 위해 우리는 생성적 계획과 정책 최적화를 통합한 AIGB-Pearl을 제안합니다. AIGB-Pearl의 핵심은 비부트스트랩 방식의 경로 평가자를 구축하여 보상을 할당하고 정책 탐색을 안내하는 것입니다. 이를 통해 계획자는 상호작용을 통해 생성 품질을 반복적으로 최적화할 수 있습니다. 또한, 오프라인 환경에서 경로 평가자의 정확성을 높이기 위해 대형 언어 모델(LLM) 기반 아키텍처, 혼합형 손실 함수, 전문가 피드백의 적응적 통합을 활용합니다. 시뮬레이션 및 실제 광고 시스템 실험에서 우리의 접근 방식이 최첨단 성능을 입증했습니다.

## 🎯 주요 포인트

- 1. AI-Generated Bidding(AIGB)는 자동 입찰을 궤적 생성 과제로 공식화하여 기존의 오프라인 강화 학습 기반 자동 입찰 방법보다 우수하고 안정적인 성능을 보여준다.
- 2. AIGB-Pearl은 생성 계획과 정책 최적화를 통합한 새로운 방법으로, 비부트스트랩 궤적 평가자를 구축하여 보상을 할당하고 정책 탐색을 안내한다.
- 3. 궤적 평가자의 정확성을 향상시키기 위해 대형 언어 모델(LLM) 기반 아키텍처, 하이브리드 점수 학습 손실, 전문가 피드백의 적응적 통합을 포함한 세 가지 기술을 도입한다.
- 4. 제안된 AIGB-Pearl 방법은 시뮬레이션 및 실제 광고 시스템에서 최첨단 성능을 입증한다.


---

*Generated on 2025-09-23 09:20:43*