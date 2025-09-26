<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:09:11.936428",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Reward Machines",
    "Deep Learning",
    "Linear Temporal Logic",
    "Symbol Grounding"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Reward Machines": 0.8,
    "Deep Learning": 0.85,
    "Linear Temporal Logic": 0.78,
    "Symbol Grounding": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Reward Machines",
        "canonical": "Neural Reward Machines",
        "aliases": [
          "NRM"
        ],
        "category": "unique_technical",
        "rationale": "Neural Reward Machines represent a novel approach in reinforcement learning that integrates symbolic reasoning with neural networks.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Deep Reinforcement Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DRL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Reinforcement Learning is a key area of deep learning that enhances the connectivity with other machine learning concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Linear Temporal Logic",
        "canonical": "Linear Temporal Logic",
        "aliases": [
          "LTL"
        ],
        "category": "specific_connectable",
        "rationale": "Linear Temporal Logic is crucial for expressing temporally extended objectives in reinforcement learning, linking to formal methods.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Symbol Grounding",
        "canonical": "Symbol Grounding",
        "aliases": [
          "SG"
        ],
        "category": "specific_connectable",
        "rationale": "Symbol Grounding is essential for mapping raw observations to symbolic representations, connecting to cognitive science and AI.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "state-action pairs",
      "prior knowledge",
      "finite and compact nature"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Reward Machines",
      "resolved_canonical": "Neural Reward Machines",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Deep Reinforcement Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Linear Temporal Logic",
      "resolved_canonical": "Linear Temporal Logic",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Symbol Grounding",
      "resolved_canonical": "Symbol Grounding",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Fully Learnable Neural Reward Machines

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19017.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19017](https://arxiv.org/abs/2509.19017)

## 🔗 유사한 논문
- [[2025-09-23/ConfClip_ Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs_20250923|ConfClip: Confidence-Weighted and Clipped Reward for Reinforcement Learning in LLMs]] (85.9% similar)
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL: Replacing Human Feedback for Reward Shaping]] (85.0% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (84.8% similar)
- [[2025-09-23/Reinforcement Learning Meets Large Language Models_ A Survey of Advancements and Applications Across the LLM Lifecycle_20250923|Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle]] (84.6% similar)
- [[2025-09-24/Tackling GNARLy Problems_ Graph Neural Algorithmic Reasoning Reimagined through Reinforcement Learning_20250924|Tackling GNARLy Problems: Graph Neural Algorithmic Reasoning Reimagined through Reinforcement Learning]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Linear Temporal Logic|Linear Temporal Logic]], [[keywords/Symbol Grounding|Symbol Grounding]]
**⚡ Unique Technical**: [[keywords/Neural Reward Machines|Neural Reward Machines]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19017v1 Announce Type: cross 
Abstract: Non-Markovian Reinforcement Learning (RL) tasks present significant challenges, as agents must reason over entire trajectories of state-action pairs to make optimal decisions. A common strategy to address this is through symbolic formalisms, such as Linear Temporal Logic (LTL) or automata, which provide a structured way to express temporally extended objectives. However, these approaches often rely on restrictive assumptions -- such as the availability of a predefined Symbol Grounding (SG) function mapping raw observations to high-level symbolic representations, or prior knowledge of the temporal task. In this work, we propose a fully learnable version of Neural Reward Machines (NRM), which can learn both the SG function and the automaton end-to-end, removing any reliance on prior knowledge. Our approach is therefore as easily applicable as classic deep RL (DRL) approaches, while being far more explainable, because of the finite and compact nature of automata. Furthermore, we show that by integrating Fully Learnable Reward Machines (FLNRM) with DRL, our method outperforms previous approaches based on Recurrent Neural Networks (RNNs).

## 📝 요약

비마르코프 강화 학습(RL) 과제는 최적의 결정을 위해 상태-행동 쌍의 전체 경로를 고려해야 하므로 어려움이 있습니다. 이를 해결하기 위해 선형 시간 논리(LTL)나 오토마타와 같은 상징적 형식을 사용하지만, 이는 사전 정의된 상징적 표현으로의 매핑이나 시간적 과제에 대한 사전 지식에 의존합니다. 본 연구에서는 이러한 사전 지식 없이 상징적 표현과 오토마타를 학습할 수 있는 완전 학습 가능한 신경 보상 기계(NRM)를 제안합니다. 이 방법은 고전적 심층 강화 학습(DRL)만큼 쉽게 적용 가능하면서도 오토마타의 유한하고 간결한 특성 덕분에 설명 가능성이 높습니다. 또한, 완전 학습 가능한 보상 기계(FLNRM)를 DRL과 통합함으로써, 순환 신경망(RNN) 기반의 기존 방법보다 우수한 성능을 보임을 입증했습니다.

## 🎯 주요 포인트

- 1. 비마르코프 강화 학습(RL) 과제는 최적의 결정을 위해 상태-행동 쌍의 전체 궤적을 고려해야 하는 도전 과제를 포함합니다.
- 2. 기존 접근법은 선형 시간 논리(LTL)나 오토마타와 같은 상징적 형식을 사용하여 시간적으로 확장된 목표를 표현하지만, 이는 사전 정의된 상징적 표현 매핑이나 시간적 과제에 대한 사전 지식에 의존하는 제한적인 가정을 필요로 합니다.
- 3. 본 연구에서는 사전 지식에 의존하지 않고 상징적 표현 매핑과 오토마타를 학습할 수 있는 완전 학습 가능한 신경 보상 기계(NRM)를 제안합니다.
- 4. 제안된 방법은 고전적인 심층 강화 학습(DRL) 접근법만큼 쉽게 적용 가능하며, 오토마타의 유한하고 간결한 특성 덕분에 더 설명 가능합니다.
- 5. 완전 학습 가능한 보상 기계(FLNRM)를 DRL과 통합함으로써, 제안된 방법이 순환 신경망(RNN) 기반의 이전 접근법보다 뛰어난 성능을 보임을 입증합니다.


---

*Generated on 2025-09-24 14:09:11*