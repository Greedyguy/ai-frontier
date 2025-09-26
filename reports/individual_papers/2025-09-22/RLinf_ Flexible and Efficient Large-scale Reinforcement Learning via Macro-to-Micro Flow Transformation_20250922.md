---
keywords:
  - Reinforcement Learning
  - Macro-to-Micro Flow Transformation
  - Embodied Intelligence
  - Adaptive Communication
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15965
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:23:50.697709",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Macro-to-Micro Flow Transformation",
    "Embodied Intelligence",
    "Adaptive Communication"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning": 0.88,
    "Macro-to-Micro Flow Transformation": 0.78,
    "Embodied Intelligence": 0.82,
    "Adaptive Communication": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a foundational concept in AI and connects to various subfields and applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.6,
        "link_intent_score": 0.88
      },
      {
        "surface": "Macro-to-Micro Flow Transformation",
        "canonical": "Macro-to-Micro Flow Transformation",
        "aliases": [
          "M2Flow"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach introduced in the paper, offering a new perspective on RL system design.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Embodied Intelligence",
        "canonical": "Embodied Intelligence",
        "aliases": [],
        "category": "evolved_concepts",
        "rationale": "Embodied Intelligence is an emerging area linking physical systems with AI, relevant to the paper's focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Adaptive Communication",
        "canonical": "Adaptive Communication",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is key to the paper's system design, enabling efficient RL training workflows.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "system flexibility",
      "training throughput"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.6,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Macro-to-Micro Flow Transformation",
      "resolved_canonical": "Macro-to-Micro Flow Transformation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Embodied Intelligence",
      "resolved_canonical": "Embodied Intelligence",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Adaptive Communication",
      "resolved_canonical": "Adaptive Communication",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# RLinf: Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation

**Korean Title:** RLinf: 매크로-투-마이크로 흐름 변환을 통한 유연하고 효율적인 대규모 강화 학습

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15965.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15965](https://arxiv.org/abs/2509.15965)

## 🔗 유사한 논문
- [[2025-09-19/FlowRL_ Matching Reward Distributions for LLM Reasoning_20250919|FlowRL: Matching Reward Distributions for LLM Reasoning]] (85.3% similar)
- [[2025-09-22/DiffusionNFT_ Online Diffusion Reinforcement with Forward Process_20250922|DiffusionNFT: Online Diffusion Reinforcement with Forward Process]] (84.1% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (83.0% similar)
- [[2025-09-18/SHaRe-RL_ Structured, Interactive Reinforcement Learning for Contact-Rich Industrial Assembly Tasks_20250918|SHaRe-RL: Structured, Interactive Reinforcement Learning for Contact-Rich Industrial Assembly Tasks]] (82.4% similar)
- [[2025-09-22/Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control_20250922|Hierarchical Reinforcement Learning with Low-Level MPC for Multi-Agent Control]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Macro-to-Micro Flow Transformation|Macro-to-Micro Flow Transformation]], [[keywords/Adaptive Communication|Adaptive Communication]]
**🚀 Evolved Concepts**: [[keywords/Embodied Intelligence|Embodied Intelligence]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15965v1 Announce Type: cross 
Abstract: Reinforcement learning (RL) has demonstrated immense potential in advancing artificial general intelligence, agentic intelligence, and embodied intelligence. However, the inherent heterogeneity and dynamicity of RL workflows often lead to low hardware utilization and slow training on existing systems. In this paper, we present RLinf, a high-performance RL training system based on our key observation that the major roadblock to efficient RL training lies in system flexibility. To maximize flexibility and efficiency, RLinf is built atop a novel RL system design paradigm called macro-to-micro flow transformation (M2Flow), which automatically breaks down high-level, easy-to-compose RL workflows at both the temporal and spatial dimensions, and recomposes them into optimized execution flows. Supported by RLinf worker's adaptive communication capability, we devise context switching and elastic pipelining to realize M2Flow transformation, and a profiling-guided scheduling policy to generate optimal execution plans. Extensive evaluations on both reasoning RL and embodied RL tasks demonstrate that RLinf consistently outperforms state-of-the-art systems, achieving 1.1x-2.13x speedup in end-to-end training throughput.

## 🔍 Abstract (한글 번역)

arXiv:2509.15965v1 발표 유형: 교차  
초록: 강화 학습(RL)은 인공지능 일반화, 에이전트 지능, 그리고 구현된 지능을 발전시키는 데 엄청난 잠재력을 보여주었습니다. 그러나 RL 워크플로우의 내재된 이질성과 동적 특성은 기존 시스템에서 낮은 하드웨어 활용도와 느린 학습을 초래하는 경우가 많습니다. 이 논문에서는 효율적인 RL 학습의 주요 장애물이 시스템 유연성에 있다는 핵심 관찰을 바탕으로 한 고성능 RL 학습 시스템인 RLinf를 소개합니다. 유연성과 효율성을 극대화하기 위해, RLinf는 매크로-투-마이크로 흐름 변환(M2Flow)이라는 새로운 RL 시스템 설계 패러다임을 기반으로 구축되었습니다. 이는 시간적 및 공간적 차원에서 고수준의, 쉽게 구성할 수 있는 RL 워크플로우를 자동으로 분해하고 최적화된 실행 흐름으로 재구성합니다. RLinf 작업자의 적응형 통신 능력에 의해 지원되는 우리는 M2Flow 변환을 실현하기 위해 컨텍스트 전환과 탄력적 파이프라이닝을 고안하고, 최적의 실행 계획을 생성하기 위한 프로파일링 기반 스케줄링 정책을 개발했습니다. 추론 RL 및 구현된 RL 작업에 대한 광범위한 평가 결과, RLinf는 최첨단 시스템을 지속적으로 능가하여 종단 간 학습 처리량에서 1.1배에서 2.13배의 속도 향상을 달성했습니다.

## 📝 요약

이 논문에서는 강화 학습(RL)의 효율성을 높이기 위한 고성능 RL 훈련 시스템인 RLinf를 제안합니다. 주요 기여는 RL 훈련의 효율성을 저해하는 시스템 유연성 문제를 해결하는 것으로, 이를 위해 새로운 RL 시스템 설계 패러다임인 매크로-투-마이크로 흐름 변환(M2Flow)을 도입했습니다. M2Flow는 고수준의 RL 워크플로를 시간적, 공간적 차원에서 자동으로 분해하고 최적화된 실행 흐름으로 재구성합니다. RLinf는 적응형 통신 기능을 활용하여 컨텍스트 전환과 탄력적 파이프라이닝을 구현하며, 프로파일링 기반의 스케줄링 정책을 통해 최적의 실행 계획을 생성합니다. 평가 결과, RLinf는 기존 시스템보다 1.1배에서 2.13배 빠른 훈련 속도를 보여주며 우수한 성능을 입증했습니다.

## 🎯 주요 포인트

- 1. 강화 학습(RL)은 인공지능 발전에 큰 잠재력을 가지고 있지만, 기존 시스템에서는 낮은 하드웨어 활용도와 느린 학습 속도를 보인다.
- 2. RLinf는 시스템 유연성이 효율적인 RL 학습의 주요 장애물이라는 점을 관찰하여 개발된 고성능 RL 학습 시스템이다.
- 3. RLinf는 매크로-투-마이크로 흐름 변환(M2Flow)이라는 새로운 RL 시스템 설계 패러다임을 기반으로 하여, RL 워크플로우를 최적화된 실행 흐름으로 재구성한다.
- 4. RLinf는 컨텍스트 전환과 탄력적 파이프라이닝을 통해 M2Flow 변환을 실현하고, 프로파일링 기반 스케줄링 정책을 통해 최적의 실행 계획을 생성한다.
- 5. RLinf는 최신 시스템보다 1.1배에서 2.13배의 속도로 학습 처리량을 향상시키며, 추론 RL과 구현된 RL 작업 모두에서 우수한 성능을 보인다.


---

*Generated on 2025-09-23 09:23:50*