---
keywords:
  - Augmented Reality
  - Deep Learning
  - Power Allocation Policy
  - Quality of Service
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2501.16186
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:36:50.675591",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Augmented Reality",
    "Deep Learning",
    "Power Allocation Policy",
    "Quality of Service"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Augmented Reality": 0.85,
    "Deep Learning": 0.8,
    "Power Allocation Policy": 0.78,
    "Quality of Service": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "augmented reality",
        "canonical": "Augmented Reality",
        "aliases": [
          "AR"
        ],
        "category": "specific_connectable",
        "rationale": "Augmented Reality is a key application area that connects with various technologies like computer vision and neural networks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "deep neural network",
        "canonical": "Deep Learning",
        "aliases": [
          "DNN"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational technology that underpins the learning-based optimization approach discussed in the paper.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "power allocation policy",
        "canonical": "Power Allocation Policy",
        "aliases": [
          "power management",
          "resource allocation"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique technical concept central to the paper's focus on optimizing resource allocation under constraints.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "quality of service",
        "canonical": "Quality of Service",
        "aliases": [
          "QoS"
        ],
        "category": "specific_connectable",
        "rationale": "Quality of Service is a critical requirement that ties into network performance and reliability discussions.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "uplink",
      "downlink",
      "simulation results"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "augmented reality",
      "resolved_canonical": "Augmented Reality",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "deep neural network",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "power allocation policy",
      "resolved_canonical": "Power Allocation Policy",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "quality of service",
      "resolved_canonical": "Quality of Service",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Learn to Optimize Resource Allocation under QoS Constraint of AR

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2501.16186.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2501.16186](https://arxiv.org/abs/2501.16186)

## 🔗 유사한 논문
- [[2025-09-19/An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing_20250919|An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing]] (85.1% similar)
- [[2025-09-18/Joint Power and Spectrum Orchestration for D2D Semantic Communication Underlying Energy-Efficient Cellular Networks_20250918|Joint Power and Spectrum Orchestration for D2D Semantic Communication Underlying Energy-Efficient Cellular Networks]] (81.6% similar)
- [[2025-09-19/AI-Driven Multi-Agent Vehicular Planning for Battery Efficiency and QoS in 6G Smart Cities_20250919|AI-Driven Multi-Agent Vehicular Planning for Battery Efficiency and QoS in 6G Smart Cities]] (81.1% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (81.0% similar)
- [[2025-09-18/Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit_20250918|Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Augmented Reality|Augmented Reality]], [[keywords/Quality of Service|Quality of Service]]
**⚡ Unique Technical**: [[keywords/Power Allocation Policy|Power Allocation Policy]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.16186v2 Announce Type: replace 
Abstract: This paper studies the uplink and downlink power allocation for interactive augmented reality (AR) services, where the live video captured by an AR device is uploaded to the network edge, and then the augmented video is subsequently downloaded. By modeling the AR transmission process as a tandem queuing system, we derive an upper bound for the probabilistic quality of service (QoS) requirement concerning end-to-end latency and reliability. The resource allocation under the QoS requirement results in a functional optimization problem. To address it, we design a deep neural network to learn the power allocation policy, leveraging the optimal power allocation structure to enhance learning performance. Simulation results demonstrate that the proposed method effectively reduces transmit power while meeting the QoS requirement.

## 📝 요약

이 논문은 상호작용 증강 현실(AR) 서비스에서의 업링크 및 다운링크 전력 할당을 연구합니다. AR 장치가 촬영한 실시간 영상을 네트워크 엣지로 업로드하고, 증강된 영상을 다시 다운로드하는 과정을 탠덤 대기열 시스템으로 모델링하여, 종단 간 지연 및 신뢰성에 관한 확률적 서비스 품질(QoS) 요구 사항의 상한을 도출합니다. QoS 요구 사항 하에서의 자원 할당은 기능 최적화 문제로 이어지며, 이를 해결하기 위해 최적 전력 할당 구조를 활용하여 학습 성능을 향상시키는 심층 신경망을 설계했습니다. 시뮬레이션 결과, 제안된 방법이 QoS 요구 사항을 충족하면서 전송 전력을 효과적으로 줄임을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 논문은 대화형 증강 현실(AR) 서비스의 업링크 및 다운링크 전력 할당을 연구합니다.
- 2. AR 전송 과정을 직렬 대기 시스템으로 모델링하여, 종단 간 지연 및 신뢰성에 관한 확률적 서비스 품질(QoS) 요구 사항의 상한을 도출합니다.
- 3. QoS 요구 사항 하에서의 자원 할당은 함수 최적화 문제로 이어지며, 이를 해결하기 위해 전력 할당 정책을 학습하는 심층 신경망을 설계합니다.
- 4. 제안된 방법은 QoS 요구 사항을 충족하면서 전송 전력을 효과적으로 줄이는 것을 시뮬레이션 결과를 통해 입증합니다.


---

*Generated on 2025-09-24 02:36:50*