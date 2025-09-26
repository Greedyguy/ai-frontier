---
keywords:
  - 3D Semantic Scene Graph
  - Embodied Question Answering
  - Vision-Language Model
  - Hierarchical Planning
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2412.14480
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:37:32.270112",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "3D Semantic Scene Graph",
    "Embodied Question Answering",
    "Vision-Language Model",
    "Hierarchical Planning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "3D Semantic Scene Graph": 0.8,
    "Embodied Question Answering": 0.78,
    "Vision-Language Model": 0.85,
    "Hierarchical Planning": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "3D Semantic Scene Graphs",
        "canonical": "3D Semantic Scene Graph",
        "aliases": [
          "3DSG",
          "3D Scene Graph"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's approach and is not commonly found in existing vocabularies, offering a unique link opportunity.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Embodied Question Answering",
        "canonical": "Embodied Question Answering",
        "aliases": [
          "EQA"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task within AI that connects to embodied AI and robotics, providing a focused link.",
        "novelty_score": 0.78,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "This represents a trending intersection of vision and language processing, crucial for linking multimodal AI research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Hierarchical Planning",
        "canonical": "Hierarchical Planning",
        "aliases": [
          "Structured Planning"
        ],
        "category": "specific_connectable",
        "rationale": "Hierarchical planning is a key strategy in AI planning, linking to structured decision-making processes.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "real-time",
      "simulation",
      "benchmark datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "3D Semantic Scene Graphs",
      "resolved_canonical": "3D Semantic Scene Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Embodied Question Answering",
      "resolved_canonical": "Embodied Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Hierarchical Planning",
      "resolved_canonical": "Hierarchical Planning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# GraphEQA: Using 3D Semantic Scene Graphs for Real-time Embodied Question Answering

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2412.14480.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2412.14480](https://arxiv.org/abs/2412.14480)

## 🔗 유사한 논문
- [[2025-09-23/Beyond Prompting_ An Efficient Embedding Framework for Open-Domain Question Answering_20250923|Beyond Prompting: An Efficient Embedding Framework for Open-Domain Question Answering]] (83.9% similar)
- [[2025-09-23/Large Language Models Meet Knowledge Graphs for Question Answering_ Synthesis and Opportunities_20250923|Large Language Models Meet Knowledge Graphs for Question Answering: Synthesis and Opportunities]] (81.8% similar)
- [[2025-09-23/GeoPQA_ Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning_20250923|GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning]] (81.7% similar)
- [[2025-09-19/Graph-Enhanced Retrieval-Augmented Question Answering for E-Commerce Customer Support_20250919|Graph-Enhanced Retrieval-Augmented Question Answering for E-Commerce Customer Support]] (81.7% similar)
- [[2025-09-22/Spatial Understanding from Videos_ Structured Prompts Meet Simulation Data_20250922|Spatial Understanding from Videos: Structured Prompts Meet Simulation Data]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Hierarchical Planning|Hierarchical Planning]]
**⚡ Unique Technical**: [[keywords/3D Semantic Scene Graph|3D Semantic Scene Graph]], [[keywords/Embodied Question Answering|Embodied Question Answering]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.14480v2 Announce Type: replace-cross 
Abstract: In Embodied Question Answering (EQA), agents must explore and develop a semantic understanding of an unseen environment to answer a situated question with confidence. This problem remains challenging in robotics, due to the difficulties in obtaining useful semantic representations, updating these representations online, and leveraging prior world knowledge for efficient planning and exploration. To address these limitations, we propose GraphEQA, a novel approach that utilizes real-time 3D metric-semantic scene graphs (3DSGs) and task relevant images as multi-modal memory for grounding Vision-Language Models (VLMs) to perform EQA tasks in unseen environments. We employ a hierarchical planning approach that exploits the hierarchical nature of 3DSGs for structured planning and semantics-guided exploration. We evaluate GraphEQA in simulation on two benchmark datasets, HM-EQA and OpenEQA, and demonstrate that it outperforms key baselines by completing EQA tasks with higher success rates and fewer planning steps. We further demonstrate GraphEQA in multiple real-world home and office environments.

## 📝 요약

Embodied Question Answering(EQA)에서 에이전트는 미지의 환경을 탐색하고 이해하여 질문에 답해야 합니다. 그러나 로봇 공학에서는 유용한 의미 표현을 얻고 이를 실시간으로 업데이트하며, 기존의 세계 지식을 활용한 효율적인 계획과 탐색이 어렵습니다. 이를 해결하기 위해, 우리는 GraphEQA라는 새로운 접근법을 제안합니다. GraphEQA는 실시간 3D 메트릭-의미 장면 그래프(3DSGs)와 관련 이미지를 다중 모달 메모리로 활용하여 Vision-Language Models(VLMs)을 기반으로 EQA 작업을 수행합니다. 계층적 계획 접근법을 사용하여 3DSGs의 계층적 특성을 활용한 구조적 계획과 의미 기반 탐색을 가능하게 합니다. HM-EQA와 OpenEQA라는 두 개의 벤치마크 데이터셋에서 시뮬레이션 평가를 통해 GraphEQA가 주요 기준을 초과하여 더 높은 성공률과 적은 계획 단계로 EQA 작업을 완료함을 입증했습니다. 또한, 여러 실제 가정 및 사무실 환경에서도 GraphEQA의 성능을 시연했습니다.

## 🎯 주요 포인트

- 1. Embodied Question Answering(EQA) 문제는 새로운 환경에서의 의미적 이해를 요구하며, 로봇공학에서 여전히 도전적인 과제로 남아있다.
- 2. GraphEQA는 실시간 3D 메트릭-시맨틱 장면 그래프와 과제 관련 이미지를 멀티모달 메모리로 활용하여 EQA 작업을 수행하는 새로운 접근법이다.
- 3. GraphEQA는 3DSG의 계층적 특성을 활용하여 구조화된 계획 및 의미 기반 탐색을 수행한다.
- 4. 시뮬레이션 환경에서 GraphEQA는 HM-EQA 및 OpenEQA 데이터셋을 통해 주요 기준보다 높은 성공률과 적은 계획 단계로 EQA 작업을 완료함을 보여준다.
- 5. GraphEQA는 실제 가정 및 사무실 환경에서도 성공적으로 구현되었다.


---

*Generated on 2025-09-26 08:37:32*