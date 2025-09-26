<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:32:17.123820",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Domain-Adaptive Critic",
    "High-Level Planning Programs",
    "Sequential Decision-Making"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Domain-Adaptive Critic": 0.8,
    "High-Level Planning Programs": 0.78,
    "Sequential Decision-Making": 0.77
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
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Key technology in AI planning, connecting with broader AI research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Domain-Adaptive Critic",
        "canonical": "Domain-Adaptive Critic",
        "aliases": [
          "Adaptive Critic"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept specific to the paper's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "High-Level Planning Programs",
        "canonical": "High-Level Planning Programs",
        "aliases": [
          "Planning Programs"
        ],
        "category": "unique_technical",
        "rationale": "Central to the proposed method, offering a unique approach to planning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sequential Decision-Making",
        "canonical": "Sequential Decision-Making",
        "aliases": [
          "Decision-Making"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to broader AI decision-making contexts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "task planners",
      "environmental feedback",
      "query costs"
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
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Domain-Adaptive Critic",
      "resolved_canonical": "Domain-Adaptive Critic",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "High-Level Planning Programs",
      "resolved_canonical": "High-Level Planning Programs",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sequential Decision-Making",
      "resolved_canonical": "Sequential Decision-Making",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Code Driven Planning with Domain-Adaptive Critic

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19077.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19077](https://arxiv.org/abs/2509.19077)

## 🔗 유사한 논문
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (85.1% similar)
- [[2025-09-23/Large Language Models as End-to-end Combinatorial Optimization Solvers_20250923|Large Language Models as End-to-end Combinatorial Optimization Solvers]] (84.0% similar)
- [[2025-09-22/World Modelling Improves Language Model Agents_20250922|World Modelling Improves Language Model Agents]] (82.8% similar)
- [[2025-09-23/Generalizable End-to-End Tool-Use RL with Synthetic CodeGym_20250923|Generalizable End-to-End Tool-Use RL with Synthetic CodeGym]] (82.8% similar)
- [[2025-09-23/MCTS-EP_ Empowering Embodied Planning with Online Preference Optimization_20250923|MCTS-EP: Empowering Embodied Planning with Online Preference Optimization]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Sequential Decision-Making|Sequential Decision-Making]]
**⚡ Unique Technical**: [[keywords/Domain-Adaptive Critic|Domain-Adaptive Critic]], [[keywords/High-Level Planning Programs|High-Level Planning Programs]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19077v1 Announce Type: new 
Abstract: Large Language Models (LLMs) have been widely adopted as task planners for AI agents in sequential decision-making problems, leveraging their extensive world knowledge. However, the gap between their general knowledge and environment-specific requirements often leads to inaccurate plans. To address this, existing approaches rely on frequent LLM queries to iteratively refine plans based on immediate environmental feedback, which incurs substantial query costs. However, this refinement is typically guided by short-term environmental feedback, limiting LLMs from developing plans aligned with long-term rewards. We propose Code Driven Planning with Domain-Adaptive Critic (CoPiC). Instead of relying on frequent queries, CoPiC employs LLMs to generate a diverse set of high-level planning programs, which iteratively produce and refine candidate plans. A trained domain-adaptive critic then evaluates these candidates and selects the one most aligned with long-term rewards for execution. Using high-level planning programs as planner and domain-adaptive critic as estimator, CoPiC improves planning while significantly reducing query costs. Results in ALFWorld, NetHack, and StarCraft II Unit Building show that CoPiC outperforms advanced LLM-based baselines, AdaPlanner and Reflexion, achieving an average (1) 23.33% improvement in success rate and (2) 91.27% reduction in query costs.

## 📝 요약

이 논문은 AI 에이전트의 순차적 의사결정 문제에서 대형 언어 모델(LLM)의 계획 수립 한계를 극복하기 위해 CoPiC(Code Driven Planning with Domain-Adaptive Critic)를 제안합니다. 기존 방법은 환경 피드백에 의존해 빈번한 LLM 쿼리를 사용하지만, 이는 단기적 피드백에 국한되어 장기적 보상에 부합하는 계획 수립에 한계가 있습니다. CoPiC는 LLM을 활용해 다양한 고수준 계획 프로그램을 생성하고, 훈련된 도메인 적응 비평가가 이를 평가하여 장기적 보상에 가장 부합하는 계획을 선택합니다. ALFWorld, NetHack, StarCraft II Unit Building 실험에서 CoPiC는 성공률 23.33% 향상과 쿼리 비용 91.27% 절감을 달성하며 기존 방법인 AdaPlanner와 Reflexion을 능가했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 순차적 의사결정 문제에서 AI 에이전트의 작업 계획자로 널리 사용되지만, 일반 지식과 환경 특수 요구 사항 간의 차이로 인해 부정확한 계획이 생성될 수 있다.
- 2. 기존 접근 방식은 환경 피드백을 기반으로 계획을 반복적으로 수정하기 위해 빈번한 LLM 쿼리에 의존하지만, 이는 상당한 쿼리 비용을 초래한다.
- 3. CoPiC는 LLM을 사용하여 다양한 고수준 계획 프로그램을 생성하고, 훈련된 도메인 적응 비평가가 장기 보상에 가장 부합하는 후보를 선택하여 실행함으로써 쿼리 비용을 크게 줄인다.
- 4. ALFWorld, NetHack, StarCraft II Unit Building에서 CoPiC는 AdaPlanner 및 Reflexion과 같은 고급 LLM 기반 기준보다 성공률에서 평균 23.33% 향상, 쿼리 비용에서 91.27% 감소를 달성했다.


---

*Generated on 2025-09-24 13:32:17*