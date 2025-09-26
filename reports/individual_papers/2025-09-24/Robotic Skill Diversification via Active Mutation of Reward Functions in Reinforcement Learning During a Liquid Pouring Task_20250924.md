<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:09:50.244734",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Proximal Policy Optimization",
    "Reward Function Mutation",
    "Robotic Skill Diversification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Proximal Policy Optimization": 0.8,
    "Reward Function Mutation": 0.75,
    "Robotic Skill Diversification": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a key method used in the study, linking it to the broader field of Machine Learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Proximal Policy Optimization",
        "canonical": "Proximal Policy Optimization",
        "aliases": [
          "PPO"
        ],
        "category": "specific_connectable",
        "rationale": "PPO is a specific algorithm used in the study, which can connect to other works using similar reinforcement learning techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Reward Function Mutation",
        "canonical": "Reward Function Mutation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is central to the study's methodology and represents a novel approach within reinforcement learning.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      },
      {
        "surface": "Robotic Skill Diversification",
        "canonical": "Robotic Skill Diversification",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The study's main contribution is the diversification of robotic skills, which is a unique aspect of the research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "simulation environment",
      "Franka Emika Panda",
      "Gaussian noise"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Proximal Policy Optimization",
      "resolved_canonical": "Proximal Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Reward Function Mutation",
      "resolved_canonical": "Reward Function Mutation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Robotic Skill Diversification",
      "resolved_canonical": "Robotic Skill Diversification",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Robotic Skill Diversification via Active Mutation of Reward Functions in Reinforcement Learning During a Liquid Pouring Task

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18463.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18463](https://arxiv.org/abs/2509.18463)

## 🔗 유사한 논문
- [[2025-09-22/reWordBench_ Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs_20250922|reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs]] (82.3% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (82.1% similar)
- [[2025-09-22/Dynamic Neural Curiosity Enhances Learning Flexibility for Autonomous Goal Discovery_20250922|Dynamic Neural Curiosity Enhances Learning Flexibility for Autonomous Goal Discovery]] (82.0% similar)
- [[2025-09-23/The Sound of Simulation_ Learning Multimodal Sim-to-Real Robot Policies with Generative Audio_20250923|The Sound of Simulation: Learning Multimodal Sim-to-Real Robot Policies with Generative Audio]] (81.7% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Proximal Policy Optimization|Proximal Policy Optimization]]
**⚡ Unique Technical**: [[keywords/Reward Function Mutation|Reward Function Mutation]], [[keywords/Robotic Skill Diversification|Robotic Skill Diversification]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18463v1 Announce Type: cross 
Abstract: This paper explores how deliberate mutations of reward function in reinforcement learning can produce diversified skill variations in robotic manipulation tasks, examined with a liquid pouring use case. To this end, we developed a new reward function mutation framework that is based on applying Gaussian noise to the weights of the different terms in the reward function. Inspired by the cost-benefit tradeoff model from human motor control, we designed the reward function with the following key terms: accuracy, time, and effort. The study was performed in a simulation environment created in NVIDIA Isaac Sim, and the setup included Franka Emika Panda robotic arm holding a glass with a liquid that needed to be poured into a container. The reinforcement learning algorithm was based on Proximal Policy Optimization. We systematically explored how different configurations of mutated weights in the rewards function would affect the learned policy. The resulting policies exhibit a wide range of behaviours: from variations in execution of the originally intended pouring task to novel skills useful for unexpected tasks, such as container rim cleaning, liquid mixing, and watering. This approach offers promising directions for robotic systems to perform diversified learning of specific tasks, while also potentially deriving meaningful skills for future tasks.

## 📝 요약

이 논문은 강화 학습에서 보상 함수의 의도적인 변이를 통해 로봇 조작 작업에서 다양한 기술 변화를 유도하는 방법을 탐구합니다. 이를 위해 보상 함수의 다양한 항목 가중치에 가우시안 노이즈를 적용하는 새로운 보상 함수 변이 프레임워크를 개발했습니다. 인간 운동 제어의 비용-편익 모델에서 영감을 받아 정확성, 시간, 노력이라는 핵심 항목으로 보상 함수를 설계했습니다. NVIDIA Isaac Sim의 시뮬레이션 환경에서 프랑카 에미카 판다 로봇 팔을 사용하여 액체를 용기에 붓는 작업을 수행했습니다. Proximal Policy Optimization 알고리즘을 기반으로, 변이된 가중치 구성에 따라 학습된 정책이 어떻게 달라지는지를 체계적으로 탐구했습니다. 결과적으로, 원래 의도된 붓기 작업의 실행 변형부터 용기 가장자리 청소, 액체 혼합, 물주기와 같은 새로운 기술까지 다양한 행동이 나타났습니다. 이 접근법은 로봇 시스템이 특정 작업에 대한 다양화된 학습을 수행하고, 미래 작업에 유용한 의미 있는 기술을 도출할 수 있는 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 강화 학습에서 보상 함수의 의도적인 변이가 로봇 조작 작업에서 다양한 기술 변화를 생성할 수 있음을 탐구했습니다.
- 2. 보상 함수의 가중치에 가우시안 노이즈를 적용하는 새로운 보상 함수 변이 프레임워크를 개발했습니다.
- 3. 보상 함수는 인간 운동 제어의 비용-이익 모델에서 영감을 받아 정확성, 시간, 노력의 주요 항목으로 설계되었습니다.
- 4. 연구는 NVIDIA Isaac Sim의 시뮬레이션 환경에서 수행되었으며, Franka Emika Panda 로봇 팔이 액체를 용기에 붓는 작업을 포함했습니다.
- 5. 변형된 보상 함수의 가중치 구성이 학습된 정책에 어떻게 영향을 미치는지를 체계적으로 탐구하여, 다양한 새로운 기술을 개발할 수 있는 가능성을 제시했습니다.


---

*Generated on 2025-09-24 15:09:50*