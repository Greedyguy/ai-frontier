<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:21:34.938757",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Linear Temporal Logic",
    "Large Language Model",
    "Embodied Agents",
    "Graph Traversal"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Linear Temporal Logic": 0.78,
    "Large Language Model": 0.8,
    "Embodied Agents": 0.75,
    "Graph Traversal": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Linear Temporal Logic",
        "canonical": "Linear Temporal Logic",
        "aliases": [
          "LTL"
        ],
        "category": "unique_technical",
        "rationale": "Linear Temporal Logic is central to the LogicGuard framework, offering a unique approach to guiding decision-making in LLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are foundational to the LogicGuard architecture, enabling advanced reasoning capabilities.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Embodied Agents",
        "canonical": "Embodied Agents",
        "aliases": [
          "Physical Agents"
        ],
        "category": "evolved_concepts",
        "rationale": "Embodied Agents represent a key application area for LogicGuard, enhancing decision-making in physical environments.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Graph Traversal",
        "canonical": "Graph Traversal",
        "aliases": [
          "Graph Search"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Traversal is a critical component in formalizing planning under symbolic constraints within LogicGuard.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "trajectory",
      "task completion",
      "safety rules"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Linear Temporal Logic",
      "resolved_canonical": "Linear Temporal Logic",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Embodied Agents",
      "resolved_canonical": "Embodied Agents",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Graph Traversal",
      "resolved_canonical": "Graph Traversal",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# LogicGuard: Improving Embodied LLM agents through Temporal Logic based Critics

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2507.03293.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2507.03293](https://arxiv.org/abs/2507.03293)

## 🔗 유사한 논문
- [[2025-09-24/Code Driven Planning with Domain-Adaptive Critic_20250924|Code Driven Planning with Domain-Adaptive Critic]] (84.2% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (83.3% similar)
- [[2025-09-19/ThinkAct_ Vision-Language-Action Reasoning via Reinforced Visual Latent Planning_20250919|ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (83.1% similar)
- [[2025-09-23/AdaptiveGuard_ Towards Adaptive Runtime Safety for LLM-Powered Software_20250923|AdaptiveGuard: Towards Adaptive Runtime Safety for LLM-Powered Software]] (83.1% similar)
- [[2025-09-23/Reasoning-to-Defend_ Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking_20250923|Reasoning-to-Defend: Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Graph Traversal|Graph Traversal]]
**⚡ Unique Technical**: [[keywords/Linear Temporal Logic|Linear Temporal Logic]]
**🚀 Evolved Concepts**: [[keywords/Embodied Agents|Embodied Agents]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.03293v2 Announce Type: replace 
Abstract: Large language models (LLMs) have shown promise in zero-shot and single step reasoning and decision making problems, but in long horizon sequential planning tasks, their errors compound, often leading to unreliable or inefficient behavior. We introduce LogicGuard, a modular actor-critic architecture in which an LLM actor is guided by a trajectory level LLM critic that communicates through Linear Temporal Logic (LTL). Our setup combines the reasoning strengths of language models with the guarantees of formal logic. The actor selects high-level actions from natural language observations, while the critic analyzes full trajectories and proposes new LTL constraints that shield the actor from future unsafe or inefficient behavior. LogicGuard supports both fixed safety rules and adaptive, learned constraints, and is model-agnostic: any LLM-based planner can serve as the actor, with LogicGuard acting as a logic-generating wrapper. We formalize planning as graph traversal under symbolic constraints, allowing LogicGuard to analyze failed or suboptimal trajectories and generate new temporal logic rules that improve future behavior. To demonstrate generality, we evaluate LogicGuard across two distinct settings: short-horizon general tasks and long-horizon specialist tasks. On the Behavior benchmark of 100 household tasks, LogicGuard increases task completion rates by 25% over a baseline InnerMonologue planner. On the Minecraft diamond-mining task, which is long-horizon and requires multiple interdependent subgoals, LogicGuard improves both efficiency and safety compared to SayCan and InnerMonologue. These results show that enabling LLMs to supervise each other through temporal logic yields more reliable, efficient and safe decision-making for both embodied agents.

## 📝 요약

LogicGuard는 장기 계획 작업에서 발생하는 오류를 줄이기 위해 설계된 모듈형 액터-크리틱 아키텍처입니다. LLM 액터가 자연어 관찰에서 고수준의 행동을 선택하면, LLM 크리틱이 전체 경로를 분석하고 Linear Temporal Logic(LTL)을 통해 새로운 제약 조건을 제안하여 안전하지 않거나 비효율적인 행동을 방지합니다. LogicGuard는 고정된 안전 규칙과 적응형 학습 제약을 지원하며, 다양한 LLM 기반 계획자에 적용 가능합니다. 두 가지 설정에서 LogicGuard를 평가한 결과, 가정 내 100개 작업에서 작업 완료율이 25% 증가했으며, Minecraft의 장기 목표 작업에서도 효율성과 안전성이 향상되었습니다. 이를 통해 LLM 간의 상호 감독을 통한 의사결정의 신뢰성과 효율성이 증대됨을 확인했습니다.

## 🎯 주요 포인트

- 1. LogicGuard는 LLM 기반의 actor-critic 아키텍처로, LLM actor가 LTL을 통해 통신하는 critic에 의해 안내됩니다.
- 2. LogicGuard는 고정된 안전 규칙과 적응 가능한 학습 제약을 지원하며, 모델에 구애받지 않고 다양한 LLM 기반 계획자에 적용 가능합니다.
- 3. LogicGuard는 실패하거나 최적이 아닌 경로를 분석하여 새로운 시간 논리 규칙을 생성함으로써 미래의 행동을 개선합니다.
- 4. Behavior 벤치마크에서 LogicGuard는 기본 InnerMonologue 계획자 대비 작업 완료율을 25% 향상시켰습니다.
- 5. Minecraft 다이아몬드 채굴 작업에서 LogicGuard는 SayCan 및 InnerMonologue에 비해 효율성과 안전성을 향상시켰습니다.


---

*Generated on 2025-09-24 14:21:34*