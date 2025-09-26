---
keywords:
  - Self-Evolved Imitation Learning
  - Few-Shot Learning
  - Exponential Moving Average Model
  - Simulator Interactions
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19460
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:36:12.757291",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-Evolved Imitation Learning",
    "Few-Shot Learning",
    "Exponential Moving Average Model",
    "Simulator Interactions"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-Evolved Imitation Learning": 0.8,
    "Few-Shot Learning": 0.9,
    "Exponential Moving Average Model": 0.7,
    "Simulator Interactions": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-Evolved Imitation Learning",
        "canonical": "Self-Evolved Imitation Learning",
        "aliases": [
          "SEIL"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper, representing a unique approach to imitation learning.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Few-Shot Model",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Few-shot learning is a trending topic and connects well with existing research on learning with limited data.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.9
      },
      {
        "surface": "Exponential Moving Average model",
        "canonical": "Exponential Moving Average Model",
        "aliases": [
          "EMA model"
        ],
        "category": "unique_technical",
        "rationale": "The EMA model is a specific technique used in the framework, which could be relevant for discussions on model stability.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Simulator Interactions",
        "canonical": "Simulator Interactions",
        "aliases": [
          "Simulation Interactions"
        ],
        "category": "unique_technical",
        "rationale": "Simulator interactions are central to the proposed method, offering a unique angle on training models in controlled environments.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "demonstrations",
      "tasks",
      "performance",
      "experiments"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-Evolved Imitation Learning",
      "resolved_canonical": "Self-Evolved Imitation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Few-Shot Model",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Exponential Moving Average model",
      "resolved_canonical": "Exponential Moving Average Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Simulator Interactions",
      "resolved_canonical": "Simulator Interactions",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Self-evolved Imitation Learning in Simulated World

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19460.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19460](https://arxiv.org/abs/2509.19460)

## 🔗 유사한 논문
- [[2025-09-24/Dynamic Mixture of Progressive Parameter-Efficient Expert Library for Lifelong Robot Learning_20250924|Dynamic Mixture of Progressive Parameter-Efficient Expert Library for Lifelong Robot Learning]] (81.9% similar)
- [[2025-09-19/LEED_ A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning_20250919|LEED: A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (81.5% similar)
- [[2025-09-18/Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall_20250918|Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall]] (81.3% similar)
- [[2025-09-22/SETrLUSI_ Stochastic Ensemble Multi-Source Transfer Learning Using Statistical Invariant_20250922|SETrLUSI: Stochastic Ensemble Multi-Source Transfer Learning Using Statistical Invariant]] (80.1% similar)
- [[2025-09-23/Sample-Efficient Reinforcement Learning with Symmetry-Guided Demonstrations for Robotic Manipulation_20250923|Sample-Efficient Reinforcement Learning with Symmetry-Guided Demonstrations for Robotic Manipulation]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Self-Evolved Imitation Learning|Self-Evolved Imitation Learning]], [[keywords/Exponential Moving Average Model|Exponential Moving Average Model]], [[keywords/Simulator Interactions|Simulator Interactions]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19460v1 Announce Type: cross 
Abstract: Imitation learning has been a trend recently, yet training a generalist agent across multiple tasks still requires large-scale expert demonstrations, which are costly and labor-intensive to collect. To address the challenge of limited supervision, we propose Self-Evolved Imitation Learning (SEIL), a framework that progressively improves a few-shot model through simulator interactions. The model first attempts tasksin the simulator, from which successful trajectories are collected as new demonstrations for iterative refinement. To enhance the diversity of these demonstrations, SEIL employs dual-level augmentation: (i) Model-level, using an Exponential Moving Average (EMA) model to collaborate with the primary model, and (ii) Environment-level, introducing slight variations in initial object positions. We further introduce a lightweight selector that filters complementary and informative trajectories from the generated pool to ensure demonstration quality. These curated samples enable the model to achieve competitive performance with far fewer training examples. Extensive experiments on the LIBERO benchmark show that SEIL achieves a new state-of-the-art performance in few-shot imitation learning scenarios. Code is available at https://github.com/Jasper-aaa/SEIL.git.

## 📝 요약

이 논문은 제한된 감독 하에 모방 학습을 개선하기 위한 Self-Evolved Imitation Learning(SEIL) 프레임워크를 제안합니다. SEIL은 시뮬레이터 상호작용을 통해 소수의 샷 모델을 점진적으로 향상시키며, 성공적인 경로를 새로운 시연 자료로 수집하여 반복적으로 개선합니다. 시연의 다양성을 높이기 위해 모델 수준에서는 EMA 모델을 사용하고, 환경 수준에서는 초기 객체 위치에 변화를 주는 이중 수준 증강을 활용합니다. 또한, 보완적이고 유익한 경로를 선별하는 경량 선택기를 도입하여 시연 품질을 보장합니다. 이러한 방법으로 SEIL은 적은 훈련 예제로도 경쟁력 있는 성능을 달성하며, LIBERO 벤치마크에서 최첨단 성과를 기록했습니다.

## 🎯 주요 포인트

- 1. Self-Evolved Imitation Learning (SEIL)은 시뮬레이터 상호작용을 통해 소수의 예시로 모델을 점진적으로 개선하는 프레임워크입니다.
- 2. SEIL은 모델 수준과 환경 수준의 이중 증강을 통해 시뮬레이터에서 성공적인 경로를 새로운 시범으로 수집하여 다양성을 높입니다.
- 3. 경량 셀렉터를 도입하여 생성된 경로 중 보완적이고 정보가 풍부한 경로를 필터링하여 시범의 품질을 보장합니다.
- 4. LIBERO 벤치마크 실험에서 SEIL은 소수의 훈련 예시로도 경쟁력 있는 성능을 달성하며, 소수 샷 모방 학습 시나리오에서 새로운 최첨단 성능을 기록했습니다.


---

*Generated on 2025-09-25 15:36:12*