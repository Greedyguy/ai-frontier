---
keywords:
  - Large Language Model
  - SWE-Effi
  - Token Snowball Effect
  - Expensive Failures
  - Reinforcement Learning
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.09853
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:12:57.722293",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "SWE-Effi",
    "Token Snowball Effect",
    "Expensive Failures",
    "Reinforcement Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "SWE-Effi": 0.8,
    "Token Snowball Effect": 0.7,
    "Expensive Failures": 0.72,
    "Reinforcement Learning": 0.78
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
        "rationale": "LLMs are central to the paper's discussion on AI systems in software engineering, providing a strong link to broader AI topics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "SWE-Effi",
        "canonical": "SWE-Effi",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "SWE-Effi is a unique metric introduced in the paper, crucial for evaluating AI effectiveness in resource-constrained environments.",
        "novelty_score": 0.9,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Token Snowball Effect",
        "canonical": "Token Snowball Effect",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This effect is a novel challenge identified in the paper, relevant for understanding inefficiencies in AI resource usage.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Expensive Failures",
        "canonical": "Expensive Failures",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The concept of 'Expensive Failures' highlights a critical inefficiency in AI systems, offering a unique perspective on cost management.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "specific_connectable",
        "rationale": "Reinforcement Learning is a key technique discussed in the context of managing project budgets and scalability.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "issue resolution",
      "project budgets",
      "fast responses"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "SWE-Effi",
      "resolved_canonical": "SWE-Effi",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Token Snowball Effect",
      "resolved_canonical": "Token Snowball Effect",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Expensive Failures",
      "resolved_canonical": "Expensive Failures",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# SWE-Effi: Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints

**Korean Title:** SWE-Effi: 자원 제약 하에서 소프트웨어 AI 에이전트 시스템의 효과성을 재평가하기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.09853.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.09853](https://arxiv.org/abs/2509.09853)

## 🔗 유사한 논문
- [[2025-09-17/An Empirical Study on Failures in Automated Issue Solving_20250917|An Empirical Study on Failures in Automated Issue Solving]] (84.7% similar)
- [[2025-09-18/Designing AI-Agents with Personalities_ A Psychometric Approach_20250918|Designing AI-Agents with Personalities: A Psychometric Approach]] (81.3% similar)
- [[2025-09-22/Watson_ A Cognitive Observability Framework for the Reasoning of LLM-Powered Agents_20250922|Watson: A Cognitive Observability Framework for the Reasoning of LLM-Powered Agents]] (81.2% similar)
- [[2025-09-19/(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low: A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (81.2% similar)
- [[2025-09-19/An LLM-based multi-agent framework for agile effort estimation_20250919|An LLM-based multi-agent framework for agile effort estimation]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/SWE-Effi|SWE-Effi]], [[keywords/Token Snowball Effect|Token Snowball Effect]], [[keywords/Expensive Failures|Expensive Failures]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.09853v2 Announce Type: replace-cross 
Abstract: The advancement of large language models (LLMs) and code agents has demonstrated significant potential to assist software engineering (SWE) tasks, such as autonomous issue resolution and feature addition. Existing AI for software engineering leaderboards (e.g., SWE-bench) focus solely on solution accuracy, ignoring the crucial factor of effectiveness in a resource-constrained world. This is a universal problem that also exists beyond software engineering tasks: any AI system should be more than correct - it must also be cost-effective. To address this gap, we introduce SWE-Effi, a set of new metrics to re-evaluate AI systems in terms of holistic effectiveness scores. We define effectiveness as the balance between the accuracy of outcome (e.g., issue resolve rate) and the resources consumed (e.g., token and time). In this paper, we specifically focus on the software engineering scenario by re-ranking popular AI systems for issue resolution on a subset of the SWE-bench benchmark using our new multi-dimensional metrics. We found that AI system's effectiveness depends not just on the scaffold itself, but on how well it integrates with the base model, which is key to achieving strong performance in a resource-efficient manner. We also identified systematic challenges such as the "token snowball" effect and, more significantly, a pattern of "expensive failures". In these cases, agents consume excessive resources while stuck on unsolvable tasks - an issue that not only limits practical deployment but also drives up the cost of failed rollouts during RL training. Lastly, we observed a clear trade-off between effectiveness under the token budget and effectiveness under the time budget, which plays a crucial role in managing project budgets and enabling scalable reinforcement learning, where fast responses are essential.

## 🔍 Abstract (한글 번역)

arXiv:2509.09853v2 발표 유형: 교체-교차  
초록: 대형 언어 모델(LLMs)과 코드 에이전트의 발전은 자율적인 문제 해결 및 기능 추가와 같은 소프트웨어 공학(SWE) 작업을 지원하는 데 상당한 잠재력을 보여주었습니다. 기존의 소프트웨어 공학을 위한 AI 리더보드(예: SWE-bench)는 솔루션의 정확성에만 초점을 맞추고, 자원이 제한된 환경에서의 효과성이라는 중요한 요소를 간과하고 있습니다. 이는 소프트웨어 공학 작업을 넘어 존재하는 보편적인 문제로, 모든 AI 시스템은 단순히 정확한 것 이상이어야 하며, 비용 효율적이어야 합니다. 이러한 격차를 해소하기 위해, 우리는 AI 시스템을 총체적 효과성 점수 측면에서 재평가하기 위한 새로운 지표 세트인 SWE-Effi를 소개합니다. 우리는 효과성을 결과의 정확성(예: 문제 해결 비율)과 소비된 자원(예: 토큰 및 시간) 간의 균형으로 정의합니다. 이 논문에서는 특히 소프트웨어 공학 시나리오에 초점을 맞추어, SWE-bench 벤치마크의 하위 집합에서 문제 해결을 위한 인기 있는 AI 시스템을 우리의 새로운 다차원 지표를 사용하여 재순위화합니다. 우리는 AI 시스템의 효과성이 단순히 구조 자체에 의존하는 것이 아니라, 자원 효율적인 방식으로 강력한 성능을 달성하기 위해 기본 모델과 얼마나 잘 통합되는지에 달려 있음을 발견했습니다. 또한 "토큰 눈덩이" 효과와 더 중요한 "비용이 많이 드는 실패" 패턴과 같은 체계적인 문제를 확인했습니다. 이러한 경우, 에이전트는 해결할 수 없는 작업에 갇혀 과도한 자원을 소비하여 실용적인 배포를 제한할 뿐만 아니라 RL 훈련 중 실패한 롤아웃의 비용을 증가시킵니다. 마지막으로, 토큰 예산 하의 효과성과 시간 예산 하의 효과성 간의 명확한 상충 관계를 관찰했으며, 이는 프로젝트 예산 관리와 빠른 응답이 필수적인 확장 가능한 강화 학습을 가능하게 하는 데 중요한 역할을 합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)과 코드 에이전트가 소프트웨어 엔지니어링(SWE) 작업을 지원하는 데 있어 잠재력을 보여주었지만, 기존의 AI 리더보드는 솔루션의 정확성만을 평가하고 자원 효율성을 간과하고 있음을 지적합니다. 이를 해결하기 위해, 저자들은 SWE-Effi라는 새로운 지표를 도입하여 AI 시스템의 전반적인 효과성을 재평가합니다. 효과성은 결과의 정확성과 소비된 자원의 균형으로 정의됩니다. 연구는 SWE-bench 벤치마크의 일부를 사용하여 AI 시스템의 이슈 해결 능력을 새로운 다차원 지표로 재평가하였으며, 시스템의 효과성은 기본 모델과의 통합 능력에 달려 있음을 발견했습니다. 또한, "토큰 스노우볼" 효과와 "비용이 많이 드는 실패" 패턴 같은 체계적인 문제를 확인했습니다. 마지막으로, 토큰 예산과 시간 예산 간의 효과성 트레이드오프가 프로젝트 예산 관리와 확장 가능한 강화 학습에서 중요한 역할을 한다고 결론지었습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델과 코드 에이전트는 소프트웨어 엔지니어링 작업에서 자율적 문제 해결 및 기능 추가를 돕는 데 큰 잠재력을 보여주고 있습니다.
- 2. 기존의 소프트웨어 엔지니어링 AI 리더보드는 솔루션의 정확성에만 초점을 맞추고 있으며, 자원 제약 환경에서의 효과성을 간과하고 있습니다.
- 3. SWE-Effi는 AI 시스템의 효과성을 총체적으로 평가하기 위한 새로운 지표 세트를 도입하여, 정확성과 자원 소비 간의 균형을 중시합니다.
- 4. AI 시스템의 효과성은 기본 모델과의 통합 능력에 따라 달라지며, 이는 자원 효율적인 강력한 성능을 달성하는 데 중요합니다.
- 5. "토큰 스노우볼" 효과와 "비용이 많이 드는 실패" 패턴은 실질적인 배포를 제한하고 RL 훈련 중 실패 비용을 증가시키는 문제로 확인되었습니다.


---

*Generated on 2025-09-23 10:12:57*