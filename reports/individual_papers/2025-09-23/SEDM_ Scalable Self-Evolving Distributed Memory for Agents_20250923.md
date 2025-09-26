---
keywords:
  - Self-Evolving Distributed Memory
  - Multi-Agent Systems
  - Cross-Domain Knowledge Diffusion
  - Verifiable Write Admission
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.09498
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:33:42.329196",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-Evolving Distributed Memory",
    "Multi-Agent Systems",
    "Cross-Domain Knowledge Diffusion",
    "Verifiable Write Admission"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-Evolving Distributed Memory": 0.8,
    "Multi-Agent Systems": 0.75,
    "Cross-Domain Knowledge Diffusion": 0.78,
    "Verifiable Write Admission": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-Evolving Distributed Memory",
        "canonical": "Self-Evolving Distributed Memory",
        "aliases": [
          "SEDM"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a novel approach to memory management in multi-agent systems.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "multi-agent systems",
        "canonical": "Multi-Agent Systems",
        "aliases": [
          "MAS"
        ],
        "category": "broad_technical",
        "rationale": "Multi-agent systems are a foundational concept in the paper, providing context for the application of SEDM.",
        "novelty_score": 0.4,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "cross-domain knowledge diffusion",
        "canonical": "Cross-Domain Knowledge Diffusion",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This mechanism is crucial for enabling knowledge transfer across different tasks, enhancing the system's adaptability.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "verifiable write admission",
        "canonical": "Verifiable Write Admission",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This feature ensures the reliability of memory updates, a key innovation in the proposed framework.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.7
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
      "candidate_surface": "Self-Evolving Distributed Memory",
      "resolved_canonical": "Self-Evolving Distributed Memory",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "multi-agent systems",
      "resolved_canonical": "Multi-Agent Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "cross-domain knowledge diffusion",
      "resolved_canonical": "Cross-Domain Knowledge Diffusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "verifiable write admission",
      "resolved_canonical": "Verifiable Write Admission",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# SEDM: Scalable Self-Evolving Distributed Memory for Agents

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.09498.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.09498](https://arxiv.org/abs/2509.09498)

## 🔗 유사한 논문
- [[2025-09-23/Synthetic POMDPs to Challenge Memory-Augmented RL_ Memory Demand Structure Modeling_20250923|Synthetic POMDPs to Challenge Memory-Augmented RL: Memory Demand Structure Modeling]] (84.0% similar)
- [[2025-09-19/MemEvo_ Memory-Evolving Incremental Multi-view Clustering_20250919|MemEvo: Memory-Evolving Incremental Multi-view Clustering]] (82.9% similar)
- [[2025-09-19/Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems_20250919|Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems]] (81.1% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (81.0% similar)
- [[2025-09-23/SPICED_ A Synaptic Homeostasis-Inspired Framework for Unsupervised Continual EEG Decoding_20250923|SPICED: A Synaptic Homeostasis-Inspired Framework for Unsupervised Continual EEG Decoding]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Multi-Agent Systems|Multi-Agent Systems]]
**🔗 Specific Connectable**: [[keywords/Cross-Domain Knowledge Diffusion|Cross-Domain Knowledge Diffusion]]
**⚡ Unique Technical**: [[keywords/Self-Evolving Distributed Memory|Self-Evolving Distributed Memory]], [[keywords/Verifiable Write Admission|Verifiable Write Admission]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.09498v2 Announce Type: replace 
Abstract: Long-term multi-agent systems inevitably generate vast amounts of trajectories and historical interactions, which makes efficient memory management essential for both performance and scalability. Existing methods typically depend on vector retrieval and hierarchical storage, yet they are prone to noise accumulation, uncontrolled memory expansion, and limited generalization across domains. To address these challenges, we present SEDM, Self-Evolving Distributed Memory, a verifiable and adaptive framework that transforms memory from a passive repository into an active, self-optimizing component. SEDM integrates verifiable write admission based on reproducible replay, a self-scheduling memory controller that dynamically ranks and consolidates entries according to empirical utility, and cross-domain knowledge diffusion that abstracts reusable insights to support transfer across heterogeneous tasks. Evaluations on benchmark datasets demonstrate that SEDM improves reasoning accuracy while reducing token overhead compared with strong memory baselines, and further enables knowledge distilled from fact verification to enhance multi-hop reasoning. The results highlight SEDM as a scalable and sustainable memory mechanism for open-ended multi-agent collaboration. The code will be released in the later stage of this project.

## 📝 요약

이 논문은 장기적인 다중 에이전트 시스템에서 발생하는 방대한 양의 경로와 상호작용 데이터를 효율적으로 관리하기 위한 메모리 관리 기법을 제안합니다. 기존 방법들이 노이즈 축적, 메모리 확장, 도메인 일반화의 한계를 가지는 반면, 제안된 SEDM(Self-Evolving Distributed Memory)은 메모리를 능동적이고 최적화된 요소로 변환합니다. SEDM은 재현 가능한 재생 기반의 검증 가능한 쓰기 허가, 경험적 유틸리티에 따라 항목을 동적으로 정렬 및 통합하는 자가 스케줄링 메모리 컨트롤러, 이질적인 작업 간 전이를 지원하는 교차 도메인 지식 확산을 통합합니다. 벤치마크 데이터셋 평가 결과, SEDM은 기존 메모리 기법 대비 추론 정확도를 향상시키고 토큰 오버헤드를 줄이며, 다중 단계 추론을 강화하는 데 기여함을 보여줍니다. 이 연구는 개방형 다중 에이전트 협업을 위한 확장 가능하고 지속 가능한 메모리 메커니즘을 제시합니다. 코드 공개는 프로젝트 후반에 예정되어 있습니다.

## 🎯 주요 포인트

- 1. SEDM(Self-Evolving Distributed Memory)은 메모리를 수동 저장소에서 능동적이고 자기 최적화하는 구성 요소로 변환하는 프레임워크입니다.
- 2. SEDM은 재생 가능한 재생에 기반한 검증 가능한 쓰기 허가, 경험적 유틸리티에 따라 항목을 동적으로 정렬 및 통합하는 자기 스케줄링 메모리 컨트롤러를 통합합니다.
- 3. SEDM은 이종 작업 간 전이를 지원하기 위해 재사용 가능한 통찰력을 추상화하는 교차 도메인 지식 확산을 제공합니다.
- 4. 벤치마크 데이터셋 평가 결과, SEDM은 강력한 메모리 기준선과 비교하여 추론 정확도를 향상시키면서 토큰 오버헤드를 줄이는 것으로 나타났습니다.
- 5. SEDM은 개방형 다중 에이전트 협업을 위한 확장 가능하고 지속 가능한 메모리 메커니즘으로 강조됩니다.


---

*Generated on 2025-09-24 00:33:42*