<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:50:23.211524",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "In-Context Reinforcement Learning",
    "Transformer",
    "Temporal Difference Learning",
    "Neural Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "In-Context Reinforcement Learning": 0.78,
    "Transformer": 0.85,
    "Temporal Difference Learning": 0.7,
    "Neural Network": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "in-context reinforcement learning",
        "canonical": "In-Context Reinforcement Learning",
        "aliases": [
          "ICRL"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a novel approach to reinforcement learning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a key component in the study and have broad applicability across machine learning tasks.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "temporal difference learning",
        "canonical": "Temporal Difference Learning",
        "aliases": [
          "TD Learning"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specific learning method discussed in the paper that connects to reinforcement learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "neural network parameters",
        "canonical": "Neural Network",
        "aliases": [
          "NN Parameters"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are fundamental to the study and are widely applicable in machine learning.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "task",
      "performance",
      "parameter updates"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "in-context reinforcement learning",
      "resolved_canonical": "In-Context Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "temporal difference learning",
      "resolved_canonical": "Temporal Difference Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "neural network parameters",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Towards Provable Emergence of In-Context Reinforcement Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18389.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18389](https://arxiv.org/abs/2509.18389)

## 🔗 유사한 논문
- [[2025-09-18/Asymptotic Study of In-context Learning with Random Transformers through Equivalent Models_20250918|Asymptotic Study of In-context Learning with Random Transformers through Equivalent Models]] (83.8% similar)
- [[2025-09-22/RLinf_ Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation_20250922|RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation]] (83.2% similar)
- [[2025-09-22/Automated Cyber Defense with Generalizable Graph-based Reinforcement Learning Agents_20250922|Automated Cyber Defense with Generalizable Graph-based Reinforcement Learning Agents]] (82.8% similar)
- [[2025-09-24/Reinforcement Learning on Pre-Training Data_20250924|Reinforcement Learning on Pre-Training Data]] (82.7% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]], [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Temporal Difference Learning|Temporal Difference Learning]]
**⚡ Unique Technical**: [[keywords/In-Context Reinforcement Learning|In-Context Reinforcement Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18389v1 Announce Type: new 
Abstract: Typically, a modern reinforcement learning (RL) agent solves a task by updating its neural network parameters to adapt its policy to the task. Recently, it has been observed that some RL agents can solve a wide range of new out-of-distribution tasks without parameter updates after pretraining on some task distribution. When evaluated in a new task, instead of making parameter updates, the pretrained agent conditions its policy on additional input called the context, e.g., the agent's interaction history in the new task. The agent's performance increases as the information in the context increases, with the agent's parameters fixed. This phenomenon is typically called in-context RL (ICRL). The pretrained parameters of the agent network enable the remarkable ICRL phenomenon. However, many ICRL works perform the pretraining with standard RL algorithms. This raises the central question this paper aims to address: Why can the RL pretraining algorithm generate network parameters that enable ICRL? We hypothesize that the parameters capable of ICRL are minimizers of the pretraining loss. This work provides initial support for this hypothesis through a case study. In particular, we prove that when a Transformer is pretrained for policy evaluation, one of the global minimizers of the pretraining loss can enable in-context temporal difference learning.

## 📝 요약

이 논문은 현대 강화 학습(RL) 에이전트가 사전 학습 후 매개변수 업데이트 없이 새로운 과제를 해결할 수 있는 '맥락 내 강화 학습(ICRL)' 현상을 탐구합니다. 연구는 사전 학습된 에이전트가 새로운 과제에서 추가 입력인 '맥락'을 활용하여 성능을 향상시킬 수 있음을 보여줍니다. 저자들은 ICRL을 가능하게 하는 네트워크 매개변수가 사전 학습 손실의 최소화 결과라고 가정하고, 이를 사례 연구를 통해 초기적으로 입증합니다. 특히, 트랜스포머가 정책 평가를 위해 사전 학습될 때, 사전 학습 손실의 전역 최소화가 ICRL을 가능하게 할 수 있음을 증명합니다.

## 🎯 주요 포인트

- 1. 현대 강화 학습 에이전트는 신경망 파라미터를 업데이트하여 정책을 적응시킴으로써 과제를 해결한다.
- 2. 사전 훈련된 에이전트는 파라미터 업데이트 없이 새로운 과제에서 맥락 정보를 활용하여 정책을 조정할 수 있다.
- 3. 맥락 정보가 증가할수록 에이전트의 성능이 향상되며, 이를 맥락 내 강화 학습(ICRL)이라고 한다.
- 4. ICRL 현상은 에이전트 네트워크의 사전 훈련된 파라미터에 의해 가능해진다.
- 5. 본 연구는 사전 훈련 손실의 최소화가 ICRL을 가능케 하는 파라미터를 생성할 수 있음을 사례 연구를 통해 입증한다.


---

*Generated on 2025-09-24 14:50:23*