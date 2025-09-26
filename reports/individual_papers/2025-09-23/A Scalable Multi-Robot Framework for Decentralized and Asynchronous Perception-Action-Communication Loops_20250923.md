---
keywords:
  - Graph Neural Network
  - Perception-Action-Communication Loop
  - Asynchronous Perception-Action-Communication
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2309.10164
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:37:02.635168",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Perception-Action-Communication Loop",
    "Asynchronous Perception-Action-Communication"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Perception-Action-Communication Loop": 0.82,
    "Asynchronous Perception-Action-Communication": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN",
          "Graph NN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are central to the paper's framework and connect well with existing literature on decentralized systems.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Perception-Action-Communication loop",
        "canonical": "Perception-Action-Communication Loop",
        "aliases": [
          "PAC loop"
        ],
        "category": "unique_technical",
        "rationale": "The PAC loop is a unique concept in the paper, crucial for understanding the decentralized framework proposed.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "asynchronous PAC",
        "canonical": "Asynchronous Perception-Action-Communication",
        "aliases": [
          "asynchronous PAC loop"
        ],
        "category": "unique_technical",
        "rationale": "Asynchronous PAC is a novel approach in the paper, enabling robots to operate at different frequencies, enhancing the framework's flexibility.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.77,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "robot swarms",
      "communication capabilities"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Perception-Action-Communication loop",
      "resolved_canonical": "Perception-Action-Communication Loop",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "asynchronous PAC",
      "resolved_canonical": "Asynchronous Perception-Action-Communication",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.77,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# A Scalable Multi-Robot Framework for Decentralized and Asynchronous Perception-Action-Communication Loops

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2309.10164.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2309.10164](https://arxiv.org/abs/2309.10164)

## 🔗 유사한 논문
- [[2025-09-19/Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control_20250919|Local-Canonicalization Equivariant Graph Neural Networks for Sample-Efficient and Generalizable Swarm Robot Control]] (84.8% similar)
- [[2025-09-18/Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (82.9% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (82.6% similar)
- [[2025-09-19/GAF_ Gaussian Action Field as a Dynamic World Model for Robotic Manipulation_20250919|GAF: Gaussian Action Field as a Dynamic World Model for Robotic Manipulation]] (82.5% similar)
- [[2025-09-19/Multi-CAP_ A Multi-Robot Connectivity-Aware Hierarchical Coverage Path Planning Algorithm for Unknown Environments_20250919|Multi-CAP: A Multi-Robot Connectivity-Aware Hierarchical Coverage Path Planning Algorithm for Unknown Environments]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Perception-Action-Communication Loop|Perception-Action-Communication Loop]], [[keywords/Asynchronous Perception-Action-Communication|Asynchronous Perception-Action-Communication]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2309.10164v2 Announce Type: replace-cross 
Abstract: Collaboration in large robot swarms to achieve a common global objective is a challenging problem in large environments due to limited sensing and communication capabilities. The robots must execute a Perception-Action-Communication (PAC) loop -- they perceive their local environment, communicate with other robots, and take actions in real time. A fundamental challenge in decentralized PAC systems is to decide what information to communicate with the neighboring robots and how to take actions while utilizing the information shared by the neighbors. Recently, this has been addressed using Graph Neural Networks (GNNs) for applications such as flocking and coverage control. Although conceptually, GNN policies are fully decentralized, the evaluation and deployment of such policies have primarily remained centralized or restrictively decentralized. Furthermore, existing frameworks assume sequential execution of perception and action inference, which is very restrictive in real-world applications. This paper proposes a framework for asynchronous PAC in robot swarms, where decentralized GNNs are used to compute navigation actions and generate messages for communication. In particular, we use aggregated GNNs, which enable the exchange of hidden layer information between robots for computational efficiency and decentralized inference of actions. Furthermore, the modules in the framework are asynchronous, allowing robots to perform sensing, extracting information, communication, action inference, and control execution at different frequencies. We demonstrate the effectiveness of GNNs executed in the proposed framework in navigating large robot swarms for collaborative coverage of large environments.

## 📝 요약

이 논문은 대규모 로봇 군집이 제한된 센싱 및 통신 능력 하에서 공동 목표를 달성하는 문제를 다룹니다. 기존의 분산된 인식-행동-통신(PAC) 시스템의 한계를 극복하기 위해 그래프 신경망(GNN)을 활용한 비동기 PAC 프레임워크를 제안합니다. 이 프레임워크는 로봇들이 비동기적으로 센싱, 정보 추출, 통신, 행동 추론 및 제어를 수행할 수 있게 하며, GNN을 통해 로봇 간 숨겨진 계층 정보를 교환하여 효율적인 분산 행동 추론을 가능하게 합니다. 제안된 프레임워크의 유효성은 대규모 환경에서의 협력적 커버리지 문제를 해결하는 데 있어 GNN의 효과를 입증합니다.

## 🎯 주요 포인트

- 1. 대규모 로봇 군집의 협업을 위한 비동기적 인식-행동-통신(PAC) 프레임워크를 제안합니다.
- 2. 그래프 신경망(GNN)을 활용하여 로봇 간 숨겨진 계층 정보를 교환하고 분산된 행동 추론을 수행합니다.
- 3. 제안된 프레임워크는 로봇이 서로 다른 주파수로 감지, 정보 추출, 통신, 행동 추론 및 제어 실행을 수행할 수 있도록 합니다.
- 4. 제안된 프레임워크에서 실행되는 GNN의 효과를 대규모 환경에서의 협업적 커버리지 문제 해결을 통해 입증합니다.
- 5. 기존의 중앙 집중적 또는 제한적으로 분산된 GNN 정책 평가 및 배포의 한계를 극복합니다.


---

*Generated on 2025-09-24 00:37:02*