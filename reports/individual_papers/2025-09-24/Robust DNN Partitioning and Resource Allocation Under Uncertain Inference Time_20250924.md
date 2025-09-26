<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:32:30.447735",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network Partitioning",
    "Resource Allocation",
    "Chance-Constrained Programming",
    "Penalty Convex-Concave Procedure"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network Partitioning": 0.82,
    "Resource Allocation": 0.79,
    "Chance-Constrained Programming": 0.75,
    "Penalty Convex-Concave Procedure": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "DNN Partitioning",
        "canonical": "Neural Network Partitioning",
        "aliases": [
          "Deep Neural Network Partitioning"
        ],
        "category": "specific_connectable",
        "rationale": "Partitioning is a critical aspect of optimizing neural networks for edge computing, enhancing connectivity with resource allocation studies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Resource Allocation",
        "canonical": "Resource Allocation",
        "aliases": [
          "Resource Management"
        ],
        "category": "broad_technical",
        "rationale": "Resource allocation is a fundamental concept in optimizing computational tasks, linking well with studies on system optimization.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.79
      },
      {
        "surface": "Chance-Constrained Programming",
        "canonical": "Chance-Constrained Programming",
        "aliases": [
          "CCP"
        ],
        "category": "unique_technical",
        "rationale": "This method is uniquely applied to handle uncertainty in optimization problems, offering novel insights into probabilistic constraints.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Penalty Convex-Concave Procedure",
        "canonical": "Penalty Convex-Concave Procedure",
        "aliases": [
          "PCCP"
        ],
        "category": "unique_technical",
        "rationale": "PCCP is a specialized optimization technique relevant for solving non-linear programming problems, enhancing specificity in optimization discussions.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "inference time",
      "task processing",
      "energy consumption"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "DNN Partitioning",
      "resolved_canonical": "Neural Network Partitioning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Resource Allocation",
      "resolved_canonical": "Resource Allocation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Chance-Constrained Programming",
      "resolved_canonical": "Chance-Constrained Programming",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Penalty Convex-Concave Procedure",
      "resolved_canonical": "Penalty Convex-Concave Procedure",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Robust DNN Partitioning and Resource Allocation Under Uncertain Inference Time

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2503.21476.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2503.21476](https://arxiv.org/abs/2503.21476)

## 🔗 유사한 논문
- [[2025-09-23/Joint Optimization of Memory Frequency, Computing Frequency, Transmission Power and Task Offloading for Energy-efficient DNN Inference_20250923|Joint Optimization of Memory Frequency, Computing Frequency, Transmission Power and Task Offloading for Energy-efficient DNN Inference]] (87.4% similar)
- [[2025-09-24/Intra-DP_ A High Performance Collaborative Inference System for Mobile Edge Computing_20250924|Intra-DP: A High Performance Collaborative Inference System for Mobile Edge Computing]] (86.3% similar)
- [[2025-09-23/Evaluating the Energy Efficiency of NPU-Accelerated Machine Learning Inference on Embedded Microcontrollers_20250923|Evaluating the Energy Efficiency of NPU-Accelerated Machine Learning Inference on Embedded Microcontrollers]] (83.3% similar)
- [[2025-09-23/Unified Framework for Pre-trained Neural Network Compression via Decomposition and Optimized Rank Selection_20250923|Unified Framework for Pre-trained Neural Network Compression via Decomposition and Optimized Rank Selection]] (82.7% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Resource Allocation|Resource Allocation]]
**🔗 Specific Connectable**: [[keywords/Neural Network Partitioning|Neural Network Partitioning]]
**⚡ Unique Technical**: [[keywords/Chance-Constrained Programming|Chance-Constrained Programming]], [[keywords/Penalty Convex-Concave Procedure|Penalty Convex-Concave Procedure]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.21476v2 Announce Type: replace-cross 
Abstract: In edge intelligence systems, deep neural network (DNN) partitioning and data offloading can provide real-time task inference for resource-constrained mobile devices. However, the inference time of DNNs is typically uncertain and cannot be precisely determined in advance, presenting significant challenges in ensuring timely task processing within deadlines. To address the uncertain inference time, we propose a robust optimization scheme to minimize the total energy consumption of mobile devices while meeting task probabilistic deadlines. The scheme only requires the mean and variance information of the inference time, without any prediction methods or distribution functions. The problem is formulated as a mixed-integer nonlinear programming (MINLP) that involves jointly optimizing the DNN model partitioning and the allocation of local CPU/GPU frequencies and uplink bandwidth. To tackle the problem, we first decompose the original problem into two subproblems: resource allocation and DNN model partitioning. Subsequently, the two subproblems with probability constraints are equivalently transformed into deterministic optimization problems using the chance-constrained programming (CCP) method. Finally, the convex optimization technique and the penalty convex-concave procedure (PCCP) technique are employed to obtain the optimal solution of the resource allocation subproblem and a stationary point of the DNN model partitioning subproblem, respectively. The proposed algorithm leverages real-world data from popular hardware platforms and is evaluated on widely used DNN models. Extensive simulations show that our proposed algorithm effectively addresses the inference time uncertainty with probabilistic deadline guarantees while minimizing the energy consumption of mobile devices.

## 📝 요약

이 논문은 엣지 인텔리전스 시스템에서 자원 제약이 있는 모바일 기기를 위한 DNN 분할 및 데이터 오프로딩을 통해 실시간 작업 추론을 제공하는 방법을 제안합니다. DNN의 추론 시간이 불확실하여 작업 기한을 맞추는 데 어려움이 있는데, 이를 해결하기 위해 평균 및 분산 정보만으로 모바일 기기의 에너지 소비를 최소화하면서 작업의 확률적 기한을 충족시키는 강건 최적화 방안을 제시합니다. 문제는 혼합 정수 비선형 프로그래밍(MINLP)으로 공식화되며, DNN 모델 분할과 로컬 CPU/GPU 주파수 및 업링크 대역폭 할당을 공동 최적화합니다. 이를 해결하기 위해 자원 할당과 DNN 모델 분할의 두 하위 문제로 분해하고, 확률 제약 프로그래밍(CCP) 방법을 사용해 결정론적 최적화 문제로 변환합니다. 최종적으로 볼록 최적화 기법과 페널티 볼록-오목 절차(PCCP)를 활용해 최적 해를 도출합니다. 제안된 알고리즘은 실제 하드웨어 플랫폼의 데이터를 활용하며, 다양한 DNN 모델에서 평가되어 에너지 소비를 최소화하면서 추론 시간의 불확실성을 효과적으로 해결함을 입증합니다.

## 🎯 주요 포인트

- 1. 엣지 인텔리전스 시스템에서 DNN 분할 및 데이터 오프로딩은 자원 제약이 있는 모바일 장치에 실시간 작업 추론을 제공할 수 있습니다.
- 2. DNN의 추론 시간은 불확실하며 사전에 정확히 결정할 수 없어 기한 내에 작업을 처리하는 데 어려움이 있습니다.
- 3. 우리는 작업의 확률적 기한을 충족하면서 모바일 장치의 총 에너지 소비를 최소화하는 강건 최적화 방안을 제안합니다.
- 4. 문제는 DNN 모델 분할과 로컬 CPU/GPU 주파수 및 업링크 대역폭 할당을 공동으로 최적화하는 혼합 정수 비선형 프로그래밍(MINLP)으로 공식화됩니다.
- 5. 제안된 알고리즘은 실제 하드웨어 플랫폼의 데이터를 활용하며, 광범위한 시뮬레이션을 통해 에너지 소비를 최소화하면서 추론 시간 불확실성을 효과적으로 해결합니다.


---

*Generated on 2025-09-24 15:32:30*