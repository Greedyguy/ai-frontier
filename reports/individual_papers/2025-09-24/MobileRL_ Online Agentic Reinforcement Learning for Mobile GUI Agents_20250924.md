<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:34:22.754689",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mobile GUI Agents",
    "Reinforcement Learning",
    "Vision-Language Model",
    "Difficulty-Adaptive GRPO",
    "Shortest Path Reward Adjustment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mobile GUI Agents": 0.78,
    "Reinforcement Learning": 0.85,
    "Vision-Language Model": 0.8,
    "Difficulty-Adaptive GRPO": 0.77,
    "Shortest Path Reward Adjustment": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Mobile GUI Agents",
        "canonical": "Mobile GUI Agents",
        "aliases": [
          "Mobile Graphical User Interface Agents"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specialized application of reinforcement learning in mobile environments, which is central to the paper's contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "A foundational technique used in the framework, connecting to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Vision Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision Language Models"
        ],
        "category": "evolved_concepts",
        "rationale": "Highlights the integration of visual and linguistic data, a key aspect of modern AI systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Difficulty-Adaptive GRPO",
        "canonical": "Difficulty-Adaptive GRPO",
        "aliases": [
          "ADAGRPO"
        ],
        "category": "unique_technical",
        "rationale": "A novel algorithm introduced in the paper, crucial for adapting to task difficulty in RL.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.77
      },
      {
        "surface": "Shortest Path Reward Adjustment",
        "canonical": "Shortest Path Reward Adjustment",
        "aliases": [
          "Reward Adjustment Strategy"
        ],
        "category": "unique_technical",
        "rationale": "A specific strategy for reward shaping in multi-turn tasks, enhancing RL performance.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "framework",
      "environment sampling"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Mobile GUI Agents",
      "resolved_canonical": "Mobile GUI Agents",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Vision Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Difficulty-Adaptive GRPO",
      "resolved_canonical": "Difficulty-Adaptive GRPO",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Shortest Path Reward Adjustment",
      "resolved_canonical": "Shortest Path Reward Adjustment",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18119.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18119](https://arxiv.org/abs/2509.18119)

## 🔗 유사한 논문
- [[2025-09-18/AppAgent v2_ Advanced Agent for Flexible Mobile Interactions_20250918|AppAgent v2: Advanced Agent for Flexible Mobile Interactions]] (83.8% similar)
- [[2025-09-23/Mano Report_20250923|Mano Report]] (83.6% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (83.1% similar)
- [[2025-09-23/Generalizable End-to-End Tool-Use RL with Synthetic CodeGym_20250923|Generalizable End-to-End Tool-Use RL with Synthetic CodeGym]] (82.9% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Mobile GUI Agents|Mobile GUI Agents]], [[keywords/Difficulty-Adaptive GRPO|Difficulty-Adaptive GRPO]], [[keywords/Shortest Path Reward Adjustment|Shortest Path Reward Adjustment]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18119v1 Announce Type: cross 
Abstract: Building general-purpose graphical user interface (GUI) agents has become increasingly promising with the progress in vision language models. However, developing effective mobile GUI agents with reinforcement learning (RL) remains challenging due to the heavy-tailed distribution of task difficulty and the inefficiency of large-scale environment sampling. We present an online agentic reinforcement learning framework MOBILERL to enhance GUI agents in mobile environments. Its core component is the Difficulty-Adaptive GRPO (ADAGRPO) algorithm. In ADAGRPO, we design difficulty-adaptive positive replay and failure curriculum filtering to adapt the model to different task difficulties. We introduce the shortest path reward adjustment strategy to reshape rewards concerning the task length in multi-turn agentic tasks. Those strategies jointly stabilize RL training, improve sample efficiency, and generate strong performance across diverse mobile apps and tasks. We apply MOBILERL to two open models (Qwen2.5-VL-7B-Instruct and GLM-4.1V-9B-Base). The resultant MOBILERL-9B model achieves state-of-the-art results in terms of success rates on both AndroidWorld (75.8%) and AndroidLab (46.8%). The MOBILERL framework is adopted in the AutoGLM products, and also open-sourced at https://github.com/THUDM/MobileRL.

## 📝 요약

이 논문은 모바일 환경에서 GUI 에이전트를 강화하기 위한 온라인 강화 학습 프레임워크인 MOBILERL을 제안합니다. 핵심 알고리즘인 ADAGRPO는 난이도 적응형 긍정적 재생과 실패 커리큘럼 필터링을 통해 다양한 과제 난이도에 모델을 적응시킵니다. 또한, 다중 턴 과제에서 보상을 재구성하는 최단 경로 보상 조정 전략을 도입하여 강화 학습의 안정성과 샘플 효율성을 개선합니다. MOBILERL은 Qwen2.5-VL-7B-Instruct와 GLM-4.1V-9B-Base 모델에 적용되어 AndroidWorld와 AndroidLab에서 각각 75.8%와 46.8%의 성공률을 기록하며 최첨단 성능을 달성했습니다. 이 프레임워크는 AutoGLM 제품에 채택되었으며, 오픈 소스로 공개되었습니다.

## 🎯 주요 포인트

- 1. MOBILERL은 모바일 환경에서 GUI 에이전트를 강화하기 위한 온라인 에이전트 강화 학습 프레임워크입니다.
- 2. ADAGRPO 알고리즘은 난이도 적응형 긍정적 재생 및 실패 커리큘럼 필터링을 통해 다양한 작업 난이도에 모델을 적응시킵니다.
- 3. 최단 경로 보상 조정 전략을 도입하여 다중 턴 에이전트 작업에서 작업 길이에 따른 보상을 재구성합니다.
- 4. MOBILERL-9B 모델은 AndroidWorld와 AndroidLab에서 각각 75.8%와 46.8%의 성공률로 최첨단 성능을 달성했습니다.
- 5. MOBILERL 프레임워크는 AutoGLM 제품에 채택되었으며, 오픈 소스로 제공됩니다.


---

*Generated on 2025-09-24 13:34:22*