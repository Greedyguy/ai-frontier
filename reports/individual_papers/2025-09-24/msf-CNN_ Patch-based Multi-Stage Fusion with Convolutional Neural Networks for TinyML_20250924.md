<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:24:18.488680",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "msf-CNN",
    "Neural Network",
    "Microcontrollers",
    "Directed Acyclic Graph"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "msf-CNN": 0.78,
    "Neural Network": 0.85,
    "Microcontrollers": 0.7,
    "Directed Acyclic Graph": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "msf-CNN",
        "canonical": "msf-CNN",
        "aliases": [
          "Multi-Stage Fusion CNN",
          "Patch-based CNN"
        ],
        "category": "unique_technical",
        "rationale": "msf-CNN is a novel technique specific to this paper, offering unique insights into CNN optimization for microcontrollers.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Convolutional Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "CNN",
          "ConvNet"
        ],
        "category": "broad_technical",
        "rationale": "Convolutional Neural Networks are a fundamental concept in deep learning, essential for linking with related neural network topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Microcontrollers",
        "canonical": "Microcontrollers",
        "aliases": [
          "MCU",
          "Embedded Systems"
        ],
        "category": "specific_connectable",
        "rationale": "Microcontrollers are crucial for understanding the hardware constraints discussed in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Directed Acyclic Graph",
        "canonical": "Directed Acyclic Graph",
        "aliases": [
          "DAG"
        ],
        "category": "specific_connectable",
        "rationale": "Directed Acyclic Graphs are key to understanding the fusion solution space described in the paper.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "TinyML",
      "real-time constraints"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "msf-CNN",
      "resolved_canonical": "msf-CNN",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Convolutional Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Microcontrollers",
      "resolved_canonical": "Microcontrollers",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Directed Acyclic Graph",
      "resolved_canonical": "Directed Acyclic Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# msf-CNN: Patch-based Multi-Stage Fusion with Convolutional Neural Networks for TinyML

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.11483.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2505.11483](https://arxiv.org/abs/2505.11483)

## 🔗 유사한 논문
- [[2025-09-23/Evaluating the Energy Efficiency of NPU-Accelerated Machine Learning Inference on Embedded Microcontrollers_20250923|Evaluating the Energy Efficiency of NPU-Accelerated Machine Learning Inference on Embedded Microcontrollers]] (84.9% similar)
- [[2025-09-23/MO R-CNN_ Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image_20250923|MO R-CNN: Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image]] (83.7% similar)
- [[2025-09-19/MaRVIn_ A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration_20250919|MaRVIn: A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (82.3% similar)
- [[2025-09-23/MPIC_ Position-Independent Multimodal Context Caching System for Efficient MLLM Serving_20250923|MPIC: Position-Independent Multimodal Context Caching System for Efficient MLLM Serving]] (81.3% similar)
- [[2025-09-22/Automating Versatile Time-Series Analysis with Tiny Transformers on Embedded FPGAs_20250922|Automating Versatile Time-Series Analysis with Tiny Transformers on Embedded FPGAs]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Microcontrollers|Microcontrollers]], [[keywords/Directed Acyclic Graph|Directed Acyclic Graph]]
**⚡ Unique Technical**: [[keywords/msf-CNN|msf-CNN]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.11483v2 Announce Type: replace 
Abstract: AI spans from large language models to tiny models running on microcontrollers (MCUs). Extremely memory-efficient model architectures are decisive to fit within an MCU's tiny memory budget e.g., 128kB of RAM. However, inference latency must remain small to fit real-time constraints. An approach to tackle this is patch-based fusion, which aims to optimize data flows across neural network layers. In this paper, we introduce msf-CNN, a novel technique that efficiently finds optimal fusion settings for convolutional neural networks (CNNs) by walking through the fusion solution space represented as a directed acyclic graph. Compared to previous work on CNN fusion for MCUs, msf-CNN identifies a wider set of solutions. We published an implementation of msf-CNN running on various microcontrollers (ARM Cortex-M, RISC-V, ESP32). We show that msf-CNN can achieve inference using 50% less RAM compared to the prior art (MCUNetV2 and StreamNet). We thus demonstrate how msf-CNN offers additional flexibility for system designers.

## 📝 요약

이 논문은 마이크로컨트롤러(MCU)에서 실행되는 메모리 효율적인 AI 모델 아키텍처를 제안합니다. 제안된 msf-CNN 기법은 패치 기반 융합을 통해 신경망 레이어 간 데이터 흐름을 최적화하여 실시간 제약을 충족시키면서도 메모리 사용을 최소화합니다. msf-CNN은 융합 솔루션 공간을 유향 비순환 그래프로 표현하여 최적의 융합 설정을 찾습니다. 기존의 MCU용 CNN 융합 연구보다 더 다양한 솔루션을 식별하며, ARM Cortex-M, RISC-V, ESP32 등의 다양한 마이크로컨트롤러에서 구현되었습니다. msf-CNN은 이전 기술 대비 최대 50% 적은 RAM으로 추론을 수행할 수 있어 시스템 설계자에게 추가적인 유연성을 제공합니다.

## 🎯 주요 포인트

- 1. msf-CNN은 마이크로컨트롤러의 제한된 메모리 환경에서 최적의 CNN 융합 설정을 효율적으로 찾는 새로운 기술입니다.
- 2. msf-CNN은 기존의 CNN 융합 연구보다 더 넓은 솔루션 세트를 식별할 수 있습니다.
- 3. msf-CNN은 이전 기술 대비 50% 적은 RAM을 사용하여 추론을 수행할 수 있습니다.
- 4. 다양한 마이크로컨트롤러(ARM Cortex-M, RISC-V, ESP32)에서 msf-CNN의 구현을 공개했습니다.
- 5. msf-CNN은 시스템 설계자에게 추가적인 유연성을 제공합니다.


---

*Generated on 2025-09-24 15:24:18*