---
keywords:
  - Preference Distillation
  - Value-based Reinforcement Learning
  - Teacher Value-based Knowledge Distillation
  - Reward Modeling
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16965
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:21:01.537035",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Preference Distillation",
    "Value-based Reinforcement Learning",
    "Teacher Value-based Knowledge Distillation",
    "Reward Modeling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Preference Distillation": 0.85,
    "Value-based Reinforcement Learning": 0.8,
    "Teacher Value-based Knowledge Distillation": 0.9,
    "Reward Modeling": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Preference Distillation",
        "canonical": "Preference Distillation",
        "aliases": [
          "Preference Optimization"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's novel approach and offers a unique concept for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Value-based Reinforcement Learning",
        "canonical": "Value-based Reinforcement Learning",
        "aliases": [
          "Value Function Learning"
        ],
        "category": "broad_technical",
        "rationale": "This is a foundational concept in reinforcement learning, relevant for connecting to broader technical discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Teacher Value-based Knowledge Distillation",
        "canonical": "Teacher Value-based Knowledge Distillation",
        "aliases": [
          "TVKD"
        ],
        "category": "unique_technical",
        "rationale": "This is the core method proposed in the paper, offering a unique linking opportunity for specific discussions.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.9
      },
      {
        "surface": "Reward Modeling",
        "canonical": "Reward Modeling",
        "aliases": [
          "Reward Shaping"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is crucial for understanding the paper's approach to reinforcement learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
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
      "candidate_surface": "Preference Distillation",
      "resolved_canonical": "Preference Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Value-based Reinforcement Learning",
      "resolved_canonical": "Value-based Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Teacher Value-based Knowledge Distillation",
      "resolved_canonical": "Teacher Value-based Knowledge Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Reward Modeling",
      "resolved_canonical": "Reward Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Preference Distillation via Value based Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16965.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16965](https://arxiv.org/abs/2509.16965)

## 🔗 유사한 논문
- [[2025-09-19/Delta Knowledge Distillation for Large Language Models_20250919|Delta Knowledge Distillation for Large Language Models]] (86.1% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (83.0% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (82.8% similar)
- [[2025-09-23/From Uniform to Heterogeneous_ Tailoring Policy Optimization to Every Token's Nature_20250923|From Uniform to Heterogeneous: Tailoring Policy Optimization to Every Token's Nature]] (82.3% similar)
- [[2025-09-22/Distribution-Aligned Decoding for Efficient LLM Task Adaptation_20250922|Distribution-Aligned Decoding for Efficient LLM Task Adaptation]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Value-based Reinforcement Learning|Value-based Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Reward Modeling|Reward Modeling]]
**⚡ Unique Technical**: [[keywords/Preference Distillation|Preference Distillation]], [[keywords/Teacher Value-based Knowledge Distillation|Teacher Value-based Knowledge Distillation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16965v1 Announce Type: new 
Abstract: Direct Preference Optimization (DPO) is a powerful paradigm to align language models with human preferences using pairwise comparisons. However, its binary win-or-loss supervision often proves insufficient for training small models with limited capacity. Prior works attempt to distill information from large teacher models using behavior cloning or KL divergence. These methods often focus on mimicking current behavior and overlook distilling reward modeling. To address this issue, we propose \textit{Teacher Value-based Knowledge Distillation} (TVKD), which introduces an auxiliary reward from the value function of the teacher model to provide a soft guide. This auxiliary reward is formulated to satisfy potential-based reward shaping, ensuring that the global reward structure and optimal policy of DPO are preserved. TVKD can be integrated into the standard DPO training framework and does not require additional rollouts. Our experimental results show that TVKD consistently improves performance across various benchmarks and model sizes.

## 📝 요약

Direct Preference Optimization (DPO)는 언어 모델을 인간의 선호에 맞추기 위해 쌍별 비교를 사용하는 강력한 방법입니다. 하지만 작은 모델에서는 이진 승패 감독이 충분하지 않을 수 있습니다. 기존 연구는 대형 모델에서 행동 복제나 KL 발산을 통해 정보를 추출하려 했으나, 보상 모델링의 증류를 간과했습니다. 이를 해결하기 위해 우리는 교사 모델의 가치 함수에서 보조 보상을 도입하는 '교사 가치 기반 지식 증류(TVKD)'를 제안합니다. 이 보조 보상은 잠재 기반 보상 형성을 만족시켜 DPO의 글로벌 보상 구조와 최적 정책을 유지합니다. TVKD는 표준 DPO 훈련 프레임워크에 통합될 수 있으며 추가적인 롤아웃이 필요하지 않습니다. 실험 결과, TVKD는 다양한 벤치마크와 모델 크기에서 성능을 지속적으로 향상시켰습니다.

## 🎯 주요 포인트

- 1. Direct Preference Optimization(DPO)는 언어 모델을 인간의 선호에 맞추기 위한 강력한 패러다임이지만, 작은 모델에서는 이진 승패 감독이 충분하지 않을 수 있습니다.
- 2. 기존 연구들은 대형 교사 모델로부터 행동 복제나 KL 발산을 통해 정보를 추출하려고 시도했으나, 보상 모델링을 간과하는 경우가 많았습니다.
- 3. Teacher Value-based Knowledge Distillation(TVKD)은 교사 모델의 가치 함수에서 보조 보상을 도입하여 부드러운 지침을 제공하는 방법을 제안합니다.
- 4. TVKD는 잠재 기반 보상 형성을 만족하도록 설계되어 DPO의 전반적인 보상 구조와 최적 정책을 보존합니다.
- 5. 실험 결과, TVKD는 다양한 벤치마크와 모델 크기에서 일관되게 성능을 향상시켰습니다.


---

*Generated on 2025-09-24 03:21:01*