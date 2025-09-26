---
keywords:
  - Foundation Models
  - Zero-Shot Learning
  - Vision-Language Model
  - Sparse-Reward Settings
  - Multi-Armed Bandits
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19924
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:53:25.987141",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Foundation Models",
    "Zero-Shot Learning",
    "Vision-Language Model",
    "Sparse-Reward Settings",
    "Multi-Armed Bandits"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Foundation Models": 0.85,
    "Zero-Shot Learning": 0.9,
    "Vision-Language Model": 0.88,
    "Sparse-Reward Settings": 0.78,
    "Multi-Armed Bandits": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "foundation models",
        "canonical": "Foundation Models",
        "aliases": [
          "foundation model"
        ],
        "category": "broad_technical",
        "rationale": "Foundation models are central to the paper's exploration of capabilities and limitations in reinforcement learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "zero-shot exploration",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "zero-shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot exploration is a key concept tested in the paper, linking to broader zero-shot learning discussions.",
        "novelty_score": 0.6,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "vision-language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are crucial for understanding the 'knowing-doing gap' discussed in the paper.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.88
      },
      {
        "surface": "sparse-reward settings",
        "canonical": "Sparse-Reward Settings",
        "aliases": [
          "sparse reward"
        ],
        "category": "unique_technical",
        "rationale": "Sparse-reward settings are a unique challenge in reinforcement learning, directly addressed in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "multi-armed bandits",
        "canonical": "Multi-Armed Bandits",
        "aliases": [
          "bandits"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-armed bandits are a classic RL benchmark used in the paper's experiments.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "exploration",
      "control"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "foundation models",
      "resolved_canonical": "Foundation Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "zero-shot exploration",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "sparse-reward settings",
      "resolved_canonical": "Sparse-Reward Settings",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "multi-armed bandits",
      "resolved_canonical": "Multi-Armed Bandits",
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

# Exploration with Foundation Models: Capabilities, Limitations, and Hybrid Approaches

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19924.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19924](https://arxiv.org/abs/2509.19924)

## 🔗 유사한 논문
- [[2025-09-22/Foundation Models as World Models_ A Foundational Study in Text-Based GridWorlds_20250922|Foundation Models as World Models: A Foundational Study in Text-Based GridWorlds]] (86.6% similar)
- [[2025-09-22/A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning_20250922|A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning]] (85.6% similar)
- [[2025-09-23/Are VLMs Ready for Lane Topology Awareness in Autonomous Driving?_20250923|Are VLMs Ready for Lane Topology Awareness in Autonomous Driving?]] (84.4% similar)
- [[2025-09-23/ConfClip_ Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs_20250923|ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs]] (84.0% similar)
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL: Replacing Human Feedback for Reward Shaping]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Foundation Models|Foundation Models]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Multi-Armed Bandits|Multi-Armed Bandits]]
**⚡ Unique Technical**: [[keywords/Sparse-Reward Settings|Sparse-Reward Settings]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19924v1 Announce Type: cross 
Abstract: Exploration in reinforcement learning (RL) remains challenging, particularly in sparse-reward settings. While foundation models possess strong semantic priors, their capabilities as zero-shot exploration agents in classic RL benchmarks are not well understood. We benchmark LLMs and VLMs on multi-armed bandits, Gridworlds, and sparse-reward Atari to test zero-shot exploration. Our investigation reveals a key limitation: while VLMs can infer high-level objectives from visual input, they consistently fail at precise low-level control: the "knowing-doing gap". To analyze a potential bridge for this gap, we investigate a simple on-policy hybrid framework in a controlled, best-case scenario. Our results in this idealized setting show that VLM guidance can significantly improve early-stage sample efficiency, providing a clear analysis of the potential and constraints of using foundation models to guide exploration rather than for end-to-end control.

## 📝 요약

이 논문은 강화 학습에서 탐색의 어려움을 다루며, 특히 보상이 드문 환경에서의 문제를 집중적으로 탐구합니다. 대형 언어 모델(LLM)과 비전 언어 모델(VLM)을 다양한 RL 벤치마크에서 제로샷 탐색 능력으로 평가한 결과, VLM이 시각적 입력에서 고수준 목표를 추론할 수 있지만, 세부적인 저수준 제어에는 실패하는 "지식-실행 간극"이 존재함을 발견했습니다. 이를 해결하기 위해 간단한 온-정책 하이브리드 프레임워크를 제안하고, 이상적인 상황에서 VLM의 지도가 초기 샘플 효율성을 크게 향상시킬 수 있음을 보였습니다. 이 연구는 기초 모델을 탐색 가이드로 활용할 때의 잠재력과 한계를 명확히 분석합니다.

## 🎯 주요 포인트

- 1. 강화 학습에서 탐색은 특히 보상이 희박한 환경에서 여전히 도전적이다.
- 2. 기초 모델들은 강력한 의미적 선험 지식을 가지고 있지만, 고전적인 강화 학습 벤치마크에서 제로샷 탐색 에이전트로서의 능력은 잘 이해되지 않았다.
- 3. VLM은 시각적 입력에서 고수준의 목표를 추론할 수 있지만, 정확한 저수준 제어에서는 일관되게 실패하는 "알고 행하는 간극"이 존재한다.
- 4. 간극을 해소하기 위해 단순한 온-정책 하이브리드 프레임워크를 이상적인 시나리오에서 조사한 결과, VLM의 지침이 초기 단계 샘플 효율성을 크게 향상시킬 수 있음을 보여준다.
- 5. 기초 모델을 탐색을 안내하는 데 사용하는 것의 잠재력과 제약을 명확히 분석하였다.


---

*Generated on 2025-09-25 15:53:25*