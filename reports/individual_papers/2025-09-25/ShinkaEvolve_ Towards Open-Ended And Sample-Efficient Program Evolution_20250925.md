---
keywords:
  - Large Language Model
  - ShinkaEvolve
  - Evolutionary Agentic Harness
  - Bandit-based LLM Ensemble Selection
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19349
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:51:06.739456",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "ShinkaEvolve",
    "Evolutionary Agentic Harness",
    "Bandit-based LLM Ensemble Selection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "ShinkaEvolve": 0.8,
    "Evolutionary Agentic Harness": 0.78,
    "Bandit-based LLM Ensemble Selection": 0.77
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
        "rationale": "Large Language Models are central to the framework's functionality and connect with existing research in AI and machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "ShinkaEvolve",
        "canonical": "ShinkaEvolve",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "ShinkaEvolve is the main subject of the paper, representing a unique framework that offers novel contributions to program evolution.",
        "novelty_score": 0.9,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Evolutionary Agentic Harnesses",
        "canonical": "Evolutionary Agentic Harness",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is crucial for understanding how the framework leverages LLMs for program evolution, offering a unique approach.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Bandit-based LLM Ensemble Selection",
        "canonical": "Bandit-based LLM Ensemble Selection",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is a novel contribution to improving LLM efficiency and is a specific method that can be linked to optimization strategies.",
        "novelty_score": 0.82,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "state-of-the-art",
      "open-source"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "ShinkaEvolve",
      "resolved_canonical": "ShinkaEvolve",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Evolutionary Agentic Harnesses",
      "resolved_canonical": "Evolutionary Agentic Harness",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Bandit-based LLM Ensemble Selection",
      "resolved_canonical": "Bandit-based LLM Ensemble Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.82,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# ShinkaEvolve: Towards Open-Ended And Sample-Efficient Program Evolution

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19349.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19349](https://arxiv.org/abs/2509.19349)

## 🔗 유사한 논문
- [[2025-09-24/Solve it with EASE_20250924|Solve it with EASE]] (84.2% similar)
- [[2025-09-24/EvoAgentX_ An Automated Framework for Evolving Agentic Workflows_20250924|EvoAgentX: An Automated Framework for Evolving Agentic Workflows]] (83.3% similar)
- [[2025-09-23/Large Language Models as End-to-end Combinatorial Optimization Solvers_20250923|Large Language Models as End-to-end Combinatorial Optimization Solvers]] (81.7% similar)
- [[2025-09-23/Generalizable End-to-End Tool-Use RL with Synthetic CodeGym_20250923|Generalizable End-to-End Tool-Use RL with Synthetic CodeGym]] (81.6% similar)
- [[2025-09-23/Reinforced Generation of Combinatorial Structures_ Applications to Complexity Theory_20250923|Reinforced Generation of Combinatorial Structures: Applications to Complexity Theory]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/ShinkaEvolve|ShinkaEvolve]], [[keywords/Evolutionary Agentic Harness|Evolutionary Agentic Harness]], [[keywords/Bandit-based LLM Ensemble Selection|Bandit-based LLM Ensemble Selection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19349v1 Announce Type: cross 
Abstract: We introduce ShinkaEvolve: a new open-source framework leveraging large language models (LLMs) to advance scientific discovery with state-of-the-art performance and unprecedented efficiency. Recent advances in scaling inference time compute of LLMs have enabled significant progress in generalized scientific discovery. These approaches rely on evolutionary agentic harnesses that leverage LLMs as mutation operators to generate candidate solutions. However, current code evolution methods suffer from critical limitations: they are sample inefficient, requiring thousands of samples to identify effective solutions, and remain closed-source, hindering broad adoption and extension. ShinkaEvolve addresses these limitations, introducing three key innovations: a parent sampling technique balancing exploration and exploitation, code novelty rejection-sampling for efficient search space exploration, and a bandit-based LLM ensemble selection strategy. We evaluate ShinkaEvolve across diverse tasks, demonstrating consistent improvements in sample efficiency and solution quality. ShinkaEvolve discovers a new state-of-the-art circle packing solution using only 150 samples, designs high-performing agentic harnesses for AIME mathematical reasoning tasks, identifies improvements to ALE-Bench competitive programming solutions, and discovers novel mixture-of-expert load balancing loss functions that illuminate the space of optimization strategies. Our results demonstrate that ShinkaEvolve achieves broad applicability with exceptional sample efficiency. By providing open-source accessibility and cost-efficiency, this work democratizes open-ended discovery across diverse computational problems.

## 📝 요약

ShinkaEvolve는 대형 언어 모델(LLM)을 활용하여 과학적 발견을 촉진하는 새로운 오픈 소스 프레임워크입니다. 기존 코드 진화 방법의 샘플 비효율성과 폐쇄성 문제를 해결하기 위해, ShinkaEvolve는 탐색과 활용을 균형 있게 조절하는 부모 샘플링 기법, 코드 참신성 거부 샘플링, 그리고 밴딧 기반 LLM 앙상블 선택 전략을 도입했습니다. 이를 통해 다양한 과제에서 샘플 효율성과 솔루션 품질을 개선했으며, 특히 150개의 샘플만으로 최첨단 원형 패킹 솔루션을 발견하는 등 뛰어난 성과를 보였습니다. ShinkaEvolve는 오픈 소스 접근성과 비용 효율성을 제공하여 다양한 계산 문제에서의 발견을 민주화합니다.

## 🎯 주요 포인트

- 1. ShinkaEvolve는 대형 언어 모델(LLMs)을 활용하여 과학적 발견을 촉진하는 새로운 오픈 소스 프레임워크입니다.
- 2. 기존 코드 진화 방법의 샘플 비효율성과 비공개 소스 문제를 해결하기 위해 세 가지 혁신적인 기법을 도입했습니다.
- 3. ShinkaEvolve는 다양한 작업에서 샘플 효율성과 솔루션 품질을 지속적으로 개선하며, 150개의 샘플만으로 최첨단 원형 패킹 솔루션을 발견했습니다.
- 4. 이 프레임워크는 AIME 수학적 추론 작업을 위한 고성능 에이전트 하네스를 설계하고, ALE-Bench 경쟁 프로그래밍 솔루션을 개선했습니다.
- 5. ShinkaEvolve는 오픈 소스 접근성과 비용 효율성을 제공하여 다양한 계산 문제에 대한 개방형 발견을 민주화합니다.


---

*Generated on 2025-09-25 16:51:06*