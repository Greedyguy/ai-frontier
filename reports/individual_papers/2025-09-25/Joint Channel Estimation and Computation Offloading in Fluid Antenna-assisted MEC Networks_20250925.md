---
keywords:
  - Fluid Antenna
  - Mobile Edge Computing
  - IBM-CCS
  - HiTDMA
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19340
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:26:56.263352",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Fluid Antenna",
    "Mobile Edge Computing",
    "IBM-CCS",
    "HiTDMA"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Fluid Antenna": 0.78,
    "Mobile Edge Computing": 0.81,
    "IBM-CCS": 0.77,
    "HiTDMA": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Fluid Antenna",
        "canonical": "Fluid Antenna",
        "aliases": [
          "FA"
        ],
        "category": "unique_technical",
        "rationale": "Fluid Antenna is a novel concept in wireless communications, providing dynamic spatial diversity and spectrum efficiency, crucial for MEC systems.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Mobile Edge Computing",
        "canonical": "Mobile Edge Computing",
        "aliases": [
          "MEC"
        ],
        "category": "broad_technical",
        "rationale": "Mobile Edge Computing is a key framework in the paper, essential for understanding the context of computation offloading and system delay minimization.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.81
      },
      {
        "surface": "Information Bottleneck Metric-enhanced Channel Compressed Sensing",
        "canonical": "IBM-CCS",
        "aliases": [
          "Information Bottleneck Metric-enhanced CCS"
        ],
        "category": "unique_technical",
        "rationale": "IBM-CCS is a specialized technique proposed in the paper for improving channel estimation, making it a unique technical contribution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Hierarchical Twin-Dueling Multi-agent Algorithm",
        "canonical": "HiTDMA",
        "aliases": [
          "Hierarchical Twin-Dueling Multi-agent"
        ],
        "category": "unique_technical",
        "rationale": "HiTDMA is a novel algorithm proposed for optimizing MEC systems, highlighting its unique contribution to the field.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "system delay",
      "optimization problem",
      "numerical results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Fluid Antenna",
      "resolved_canonical": "Fluid Antenna",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Mobile Edge Computing",
      "resolved_canonical": "Mobile Edge Computing",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Information Bottleneck Metric-enhanced Channel Compressed Sensing",
      "resolved_canonical": "IBM-CCS",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Hierarchical Twin-Dueling Multi-agent Algorithm",
      "resolved_canonical": "HiTDMA",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Joint Channel Estimation and Computation Offloading in Fluid Antenna-assisted MEC Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19340.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19340](https://arxiv.org/abs/2509.19340)

## 🔗 유사한 논문
- [[2025-09-25/E2E Learning Massive MIMO for Multimodal Semantic Non-Orthogonal Transmission and Fusion_20250925|E2E Learning Massive MIMO for Multimodal Semantic Non-Orthogonal Transmission and Fusion]] (82.5% similar)
- [[2025-09-25/A Federated Fine-Tuning Paradigm of Foundation Models in Heterogenous Wireless Networks_20250925|A Federated Fine-Tuning Paradigm of Foundation Models in Heterogenous Wireless Networks]] (82.3% similar)
- [[2025-09-24/Integrating Stacked Intelligent Metasurfaces and Power Control for Dynamic Edge Inference via Over-The-Air Neural Networks_20250924|Integrating Stacked Intelligent Metasurfaces and Power Control for Dynamic Edge Inference via Over-The-Air Neural Networks]] (82.1% similar)
- [[2025-09-23/Learn to Optimize Resource Allocation under QoS Constraint of AR_20250923|Learn to Optimize Resource Allocation under QoS Constraint of AR]] (81.5% similar)
- [[2025-09-25/Federation of Agents_ A Semantics-Aware Communication Fabric for Large-Scale Agentic AI_20250925|Federation of Agents: A Semantics-Aware Communication Fabric for Large-Scale Agentic AI]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Mobile Edge Computing|Mobile Edge Computing]]
**⚡ Unique Technical**: [[keywords/Fluid Antenna|Fluid Antenna]], [[keywords/IBM-CCS|IBM-CCS]], [[keywords/HiTDMA|HiTDMA]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19340v1 Announce Type: cross 
Abstract: With the emergence of fluid antenna (FA) in wireless communications, the capability to dynamically adjust port positions offers substantial benefits in spatial diversity and spectrum efficiency, which are particularly valuable for mobile edge computing (MEC) systems. Therefore, we propose an FA-assisted MEC offloading framework to minimize system delay. This framework faces two severe challenges, which are the complexity of channel estimation due to dynamic port configuration and the inherent non-convexity of the joint optimization problem. Firstly, we propose Information Bottleneck Metric-enhanced Channel Compressed Sensing (IBM-CCS), which advances FA channel estimation by integrating information relevance into the sensing process and capturing key features of FA channels effectively. Secondly, to address the non-convex and high-dimensional optimization problem in FA-assisted MEC systems, which includes FA port selection, beamforming, power control, and resource allocation, we propose a game theory-assisted Hierarchical Twin-Dueling Multi-agent Algorithm (HiTDMA) based offloading scheme, where the hierarchical structure effectively decouples and coordinates the optimization tasks between the user side and the base station side. Crucially, the game theory effectively reduces the dimensionality of power control variables, allowing deep reinforcement learning (DRL) agents to achieve improved optimization efficiency. Numerical results confirm that the proposed scheme significantly reduces system delay and enhances offloading performance, outperforming benchmarks. Additionally, the IBM-CCS channel estimation demonstrates superior accuracy and robustness under varying port densities, contributing to efficient communication under imperfect CSI.

## 📝 요약

이 논문은 유동 안테나(FA)를 활용한 모바일 엣지 컴퓨팅(MEC) 시스템의 지연을 최소화하기 위한 FA 지원 MEC 오프로드 프레임워크를 제안합니다. 주요 기여는 두 가지 문제를 해결하는 데 있습니다: 동적 포트 구성으로 인한 채널 추정의 복잡성과 비볼록 최적화 문제입니다. 첫째, 정보 병목 메트릭을 활용한 채널 압축 센싱(IBM-CCS)을 제안하여 FA 채널 추정의 정확성과 효율성을 높였습니다. 둘째, 비볼록 및 고차원 최적화 문제를 해결하기 위해 게임 이론을 활용한 계층적 쌍대-듀얼링 다중 에이전트 알고리즘(HiTDMA)을 제안하여 사용자와 기지국 간의 최적화 작업을 효과적으로 분리하고 조정합니다. 이 방법은 전력 제어 변수의 차원을 줄여 심층 강화 학습(DRL) 에이전트의 최적화 효율성을 향상시킵니다. 수치 결과는 제안된 프레임워크가 시스템 지연을 크게 줄이고 오프로드 성능을 향상시킴을 보여주며, IBM-CCS 채널 추정은 다양한 포트 밀도에서 높은 정확성과 강건성을 입증합니다.

## 🎯 주요 포인트

- 1. 유동 안테나(FA)를 활용한 MEC 오프로드 프레임워크는 시스템 지연을 최소화하는 것을 목표로 한다.
- 2. FA 채널 추정의 복잡성을 해결하기 위해 정보 병목 메트릭을 활용한 채널 압축 감지(IBM-CCS)를 제안한다.
- 3. 비볼록 및 고차원 최적화 문제를 해결하기 위해 게임 이론을 활용한 계층적 쌍대 대결 다중 에이전트 알고리즘(HiTDMA)을 제안한다.
- 4. 제안된 HiTDMA 기반 오프로드 방식은 사용자 측과 기지국 측의 최적화 작업을 효과적으로 분리 및 조정한다.
- 5. 수치 결과는 제안된 방식이 시스템 지연을 크게 줄이고 오프로드 성능을 향상시킴을 보여준다.


---

*Generated on 2025-09-25 15:26:56*