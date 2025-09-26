---
keywords:
  - Scene Graph Representation
  - Graph Neural Network
  - Vision-Language Model
  - Diffusion-based Imitation Learning
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.16053
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:27:31.822965",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Scene Graph Representation",
    "Graph Neural Network",
    "Vision-Language Model",
    "Diffusion-based Imitation Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Scene Graph Representation": 0.78,
    "Graph Neural Network": 0.8,
    "Vision-Language Model": 0.79,
    "Diffusion-based Imitation Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "scene graph-based representation",
        "canonical": "Scene Graph Representation",
        "aliases": [
          "scene graph",
          "graph-based scene"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's approach and offers a unique method for task-relevant object and relation focus.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "GNNs are integral to the proposed skill learning framework, enhancing connectivity with existing research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "vision-language model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM"
        ],
        "category": "evolved_concepts",
        "rationale": "The integration of VLMs with scene-graph skills highlights a novel approach to task planning.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      },
      {
        "surface": "diffusion-based imitation learning",
        "canonical": "Diffusion-based Imitation Learning",
        "aliases": [
          "diffusion imitation"
        ],
        "category": "unique_technical",
        "rationale": "This represents a novel learning approach within the framework, offering new avenues for exploration.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "planner",
      "task"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "scene graph-based representation",
      "resolved_canonical": "Scene Graph Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "vision-language model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "diffusion-based imitation learning",
      "resolved_canonical": "Diffusion-based Imitation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Compose by Focus: Scene Graph-based Atomic Skills

**Korean Title:** 포커스를 통한 구성: 장면 그래프 기반의 원자적 기술

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16053.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.16053](https://arxiv.org/abs/2509.16053)

## 🔗 유사한 논문
- [[2025-09-19/Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (82.5% similar)
- [[2025-09-19/CRAFT_ Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks_20250919|CRAFT: Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks]] (82.2% similar)
- [[2025-09-19/Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control_20250919|Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control]] (81.9% similar)
- [[2025-09-22/SCENEFORGE_ Enhancing 3D-text alignment with Structured Scene Compositions_20250922|SCENEFORGE: Enhancing 3D-text alignment with Structured Scene Compositions]] (81.6% similar)
- [[2025-09-18/\textsc{Gen2Real}_ Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Scene Graph Representation|Scene Graph Representation]], [[keywords/Diffusion-based Imitation Learning|Diffusion-based Imitation Learning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16053v1 Announce Type: cross 
Abstract: A key requirement for generalist robots is compositional generalization - the ability to combine atomic skills to solve complex, long-horizon tasks. While prior work has primarily focused on synthesizing a planner that sequences pre-learned skills, robust execution of the individual skills themselves remains challenging, as visuomotor policies often fail under distribution shifts induced by scene composition. To address this, we introduce a scene graph-based representation that focuses on task-relevant objects and relations, thereby mitigating sensitivity to irrelevant variation. Building on this idea, we develop a scene-graph skill learning framework that integrates graph neural networks with diffusion-based imitation learning, and further combine "focused" scene-graph skills with a vision-language model (VLM) based task planner. Experiments in both simulation and real-world manipulation tasks demonstrate substantially higher success rates than state-of-the-art baselines, highlighting improved robustness and compositional generalization in long-horizon tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.16053v1 발표 유형: 교차  
초록: 일반적인 로봇에게 중요한 요구 사항 중 하나는 조합적 일반화입니다. 이는 원자적 기술을 결합하여 복잡하고 장기적인 과제를 해결하는 능력을 의미합니다. 이전 연구는 주로 사전 학습된 기술을 순서대로 배열하는 계획자를 합성하는 데 중점을 두었지만, 개별 기술의 견고한 실행 자체는 여전히 도전 과제로 남아 있습니다. 이는 장면 구성에 의해 유도된 분포 변화로 인해 시각-운동 정책이 종종 실패하기 때문입니다. 이를 해결하기 위해, 우리는 과제와 관련된 객체와 관계에 중점을 둔 장면 그래프 기반 표현을 도입하여 불필요한 변동에 대한 민감성을 완화합니다. 이 아이디어를 바탕으로, 우리는 그래프 신경망과 확산 기반 모방 학습을 통합한 장면 그래프 기술 학습 프레임워크를 개발하고, "집중된" 장면 그래프 기술을 비전-언어 모델(VLM) 기반 과제 계획자와 결합합니다. 시뮬레이션과 실제 조작 작업 모두에서의 실험은 최첨단 기준선보다 상당히 높은 성공률을 보여주며, 장기 과제에서의 향상된 견고성과 조합적 일반화를 강조합니다.

## 📝 요약

이 논문은 일반적인 로봇이 복잡한 작업을 해결하기 위해 개별 기술을 조합하는 능력인 구성적 일반화를 달성하는 방법을 제안합니다. 기존 연구는 주로 사전에 학습된 기술을 순서대로 배치하는 계획에 초점을 맞췄으나, 개별 기술의 실행이 장면 구성 변화에 민감하여 어려움이 있었습니다. 이를 해결하기 위해, 이 연구는 작업 관련 객체와 관계에 집중하는 장면 그래프 기반 표현을 도입하여 불필요한 변동에 대한 민감성을 줄였습니다. 이 아이디어를 바탕으로 그래프 신경망과 확산 기반 모방 학습을 통합한 장면 그래프 기술 학습 프레임워크를 개발하고, 이를 비전-언어 모델 기반의 작업 계획자와 결합했습니다. 시뮬레이션과 실제 조작 작업 실험에서, 제안된 방법은 최신 기법보다 높은 성공률을 보여주며, 장기 작업에서의 향상된 강건성과 구성적 일반화를 입증했습니다.

## 🎯 주요 포인트

- 1. 일반 로봇의 핵심 요구사항은 원자적 기술을 결합하여 복잡한 장기 과제를 해결하는 조합적 일반화 능력이다.
- 2. 기존 연구는 주로 사전 학습된 기술을 순차적으로 사용하는 계획자 합성에 집중했으나, 개별 기술의 실행은 여전히 도전 과제이다.
- 3. 장면 그래프 기반 표현을 도입하여 과제 관련 객체와 관계에 집중함으로써 불필요한 변동에 대한 민감성을 줄였다.
- 4. 그래프 신경망과 확산 기반 모방 학습을 통합한 장면 그래프 기술 학습 프레임워크를 개발했다.
- 5. 실험 결과, 시뮬레이션 및 실제 조작 작업에서 기존 최첨단 기준보다 높은 성공률을 보여주며, 장기 과제에서의 향상된 강건성과 조합적 일반화를 강조한다.


---

*Generated on 2025-09-23 09:27:31*