---
keywords:
  - Neural Network
  - Dynamic Voltage and Frequency Scaling
  - Energy-efficient Inference
  - Task Offloading
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17970
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:14:16.974560",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Dynamic Voltage and Frequency Scaling",
    "Energy-efficient Inference",
    "Task Offloading"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Dynamic Voltage and Frequency Scaling": 0.8,
    "Energy-efficient Inference": 0.78,
    "Task Offloading": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "DNN",
          "Deep Learning Models"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are foundational to the paper's discussion on optimizing inference, linking well with existing literature on machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Dynamic Voltage and Frequency Scaling",
        "canonical": "Dynamic Voltage and Frequency Scaling",
        "aliases": [
          "DVFS"
        ],
        "category": "unique_technical",
        "rationale": "DVFS is a specific technique central to the paper's optimization strategy, offering a unique angle for linking energy efficiency discussions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Energy-efficient DNN Inference",
        "canonical": "Energy-efficient Inference",
        "aliases": [
          "Efficient Inference",
          "Low-power Inference"
        ],
        "category": "unique_technical",
        "rationale": "This concept is crucial for understanding the paper's contribution to reducing energy consumption in neural network operations.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Task Offloading",
        "canonical": "Task Offloading",
        "aliases": [
          "Computation Offloading"
        ],
        "category": "specific_connectable",
        "rationale": "Task Offloading is a key strategy in distributed computing, relevant for linking discussions on resource management.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "memory frequency",
      "computing frequency",
      "transmission power"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Dynamic Voltage and Frequency Scaling",
      "resolved_canonical": "Dynamic Voltage and Frequency Scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Energy-efficient DNN Inference",
      "resolved_canonical": "Energy-efficient Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Task Offloading",
      "resolved_canonical": "Task Offloading",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Joint Optimization of Memory Frequency, Computing Frequency, Transmission Power and Task Offloading for Energy-efficient DNN Inference

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17970.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17970](https://arxiv.org/abs/2509.17970)

## 🔗 유사한 논문
- [[2025-09-19/MaRVIn_ A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration_20250919|MaRVIn: A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (83.7% similar)
- [[2025-09-23/Evaluating the Energy Efficiency of NPU-Accelerated Machine Learning Inference on Embedded Microcontrollers_20250923|Evaluating the Energy Efficiency of NPU-Accelerated Machine Learning Inference on Embedded Microcontrollers]] (83.6% similar)
- [[2025-09-18/The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning_20250918|The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning]] (81.6% similar)
- [[2025-09-22/Learning to Optimize Capacity Planning in Semiconductor Manufacturing_20250922|Learning to Optimize Capacity Planning in Semiconductor Manufacturing]] (81.0% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Task Offloading|Task Offloading]]
**⚡ Unique Technical**: [[keywords/Dynamic Voltage and Frequency Scaling|Dynamic Voltage and Frequency Scaling]], [[keywords/Energy-efficient Inference|Energy-efficient Inference]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17970v1 Announce Type: cross 
Abstract: Deep neural networks (DNNs) have been widely applied in diverse applications, but the problems of high latency and energy overhead are inevitable on resource-constrained devices. To address this challenge, most researchers focus on the dynamic voltage and frequency scaling (DVFS) technique to balance the latency and energy consumption by changing the computing frequency of processors. However, the adjustment of memory frequency is usually ignored and not fully utilized to achieve efficient DNN inference, which also plays a significant role in the inference time and energy consumption. In this paper, we first investigate the impact of joint memory frequency and computing frequency scaling on the inference time and energy consumption with a model-based and data-driven method. Then by combining with the fitting parameters of different DNN models, we give a preliminary analysis for the proposed model to see the effects of adjusting memory frequency and computing frequency simultaneously. Finally, simulation results in local inference and cooperative inference cases further validate the effectiveness of jointly scaling the memory frequency and computing frequency to reduce the energy consumption of devices.

## 📝 요약

이 논문은 자원 제약이 있는 장치에서 딥러닝 모델의 추론 시 발생하는 높은 지연 시간과 에너지 소모 문제를 해결하기 위해 메모리 주파수와 컴퓨팅 주파수를 동시에 조정하는 방법을 제안합니다. 기존에는 주로 컴퓨팅 주파수 조정에 중점을 두었으나, 메모리 주파수의 조정도 추론 시간과 에너지 소비에 중요한 영향을 미친다는 점을 강조합니다. 모델 기반 및 데이터 기반 방법을 통해 메모리와 컴퓨팅 주파수의 공동 조정이 장치의 에너지 소비를 줄이는 데 효과적임을 시뮬레이션 결과로 입증합니다.

## 🎯 주요 포인트

- 1. 자원 제약이 있는 장치에서 높은 지연 시간과 에너지 오버헤드를 해결하기 위해 동적 전압 및 주파수 스케일링(DVFS) 기술이 주로 사용됩니다.
- 2. 메모리 주파수 조정은 종종 간과되지만, 이는 추론 시간과 에너지 소비에 중요한 역할을 합니다.
- 3. 본 논문에서는 메모리 주파수와 컴퓨팅 주파수의 공동 조정이 추론 시간과 에너지 소비에 미치는 영향을 모델 기반 및 데이터 기반 방법으로 조사합니다.
- 4. 다양한 DNN 모델의 피팅 파라미터를 결합하여 메모리 주파수와 컴퓨팅 주파수를 동시에 조정하는 효과를 분석합니다.
- 5. 시뮬레이션 결과는 메모리 주파수와 컴퓨팅 주파수를 공동으로 조정함으로써 장치의 에너지 소비를 줄이는 데 효과적임을 입증합니다.


---

*Generated on 2025-09-24 00:14:16*