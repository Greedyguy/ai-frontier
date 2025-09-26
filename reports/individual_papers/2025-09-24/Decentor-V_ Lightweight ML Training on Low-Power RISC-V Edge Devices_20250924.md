<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:45:53.088200",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "RISC-V Architecture",
    "Lightweight Stochastic Gradient Descent",
    "Internet of Things"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.8,
    "RISC-V Architecture": 0.78,
    "Lightweight Stochastic Gradient Descent": 0.75,
    "Internet of Things": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Learning",
        "canonical": "Federated Learning",
        "aliases": [
          "FL"
        ],
        "category": "specific_connectable",
        "rationale": "Federated Learning is a key concept for decentralized training, linking to privacy and connectivity issues.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "RISC-V",
        "canonical": "RISC-V Architecture",
        "aliases": [
          "RISC-V"
        ],
        "category": "unique_technical",
        "rationale": "RISC-V is an emerging architecture relevant to the paper's focus on low-power edge devices.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "L-SGD",
        "canonical": "Lightweight Stochastic Gradient Descent",
        "aliases": [
          "L-SGD"
        ],
        "category": "unique_technical",
        "rationale": "L-SGD is a specific optimization algorithm variant crucial for the paper's proposed method.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "IoT devices",
        "canonical": "Internet of Things",
        "aliases": [
          "IoT"
        ],
        "category": "broad_technical",
        "rationale": "Internet of Things is central to the context of edge device applications discussed in the paper.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "on-device training",
      "cloud-based services",
      "memory usage"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "RISC-V",
      "resolved_canonical": "RISC-V Architecture",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "L-SGD",
      "resolved_canonical": "Lightweight Stochastic Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "IoT devices",
      "resolved_canonical": "Internet of Things",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Decentor-V: Lightweight ML Training on Low-Power RISC-V Edge Devices

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18118.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18118](https://arxiv.org/abs/2509.18118)

## 🔗 유사한 논문
- [[2025-09-19/MaRVIn_ A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration_20250919|MaRVIn: A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (85.7% similar)
- [[2025-09-19/Evolution of Kernels_ Automated RISC-V Kernel Optimization with Large Language Models_20250919|Evolution of Kernels: Automated RISC-V Kernel Optimization with Large Language Models]] (82.6% similar)
- [[2025-09-24/Chiplet-Based RISC-V SoC with Modular AI Acceleration_20250924|Chiplet-Based RISC-V SoC with Modular AI Acceleration]] (82.5% similar)
- [[2025-09-23/Federated Learning with Ad-hoc Adapter Insertions_ The Case of Soft-Embeddings for Training Classifier-as-Retriever_20250923|Federated Learning with Ad-hoc Adapter Insertions: The Case of Soft-Embeddings for Training Classifier-as-Retriever]] (81.8% similar)
- [[2025-09-23/MobiZO_ Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines_20250923|MobiZO: Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Internet of Things|Internet of Things]]
**🔗 Specific Connectable**: [[keywords/Federated Learning|Federated Learning]]
**⚡ Unique Technical**: [[keywords/RISC-V Architecture|RISC-V Architecture]], [[keywords/Lightweight Stochastic Gradient Descent|Lightweight Stochastic Gradient Descent]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18118v1 Announce Type: new 
Abstract: Modern IoT devices increasingly rely on machine learning solutions to process data locally. However, the lack of graphics processing units (GPUs) or dedicated accelerators on most platforms makes on-device training largely infeasible, often requiring cloud-based services to perform this task. This procedure often raises privacy-related concerns, and creates dependency on reliable and always-on connectivity. Federated Learning (FL) is a new trend that addresses these issues by enabling decentralized and collaborative training directly on devices, but it requires highly efficient optimization algorithms. L-SGD, a lightweight variant of stochastic gradient descent, has enabled neural network training on Arm Cortex-M Microcontroller Units (MCUs). This work extends L-SGD to RISC-V-based MCUs, an open and emerging architecture that still lacks robust support for on-device training. L-SGD was evaluated on both Arm and RISC-V platforms using 32-bit floating-point arithmetic, highlighting the performance impact of the absence of Floating-Point Units (FPUs) in RISC-V MCUs. To mitigate these limitations, we introduce an 8-bit quantized version of L-SGD for RISC-V, which achieves nearly 4x reduction in memory usage and a 2.2x speedup in training time, with negligible accuracy degradation.

## 📝 요약

이 논문은 IoT 기기에서의 데이터 처리를 위한 머신러닝 솔루션의 문제점을 해결하기 위해 연합 학습(Federated Learning, FL)을 활용하는 방법을 제안합니다. 기존의 Arm Cortex-M 마이크로컨트롤러 유닛(MCU)에서 사용되던 L-SGD 알고리즘을 RISC-V 기반 MCU에 확장하여 적용했습니다. RISC-V는 아직 온디바이스 학습 지원이 부족한 개방형 아키텍처입니다. 연구 결과, RISC-V MCU에서 부동소수점 유닛(FPU)의 부재로 인한 성능 저하를 극복하기 위해 8비트 양자화된 L-SGD 버전을 도입하여 메모리 사용량을 약 4배 줄이고 학습 시간을 2.2배 단축하면서도 정확도 저하를 최소화했습니다.

## 🎯 주요 포인트

- 1. 현대 IoT 기기들은 점점 더 기계 학습 솔루션에 의존하여 데이터를 로컬에서 처리하지만, 대부분의 플랫폼에서 GPU나 전용 가속기가 없어 기기 내 훈련이 어렵습니다.
- 2. 연합 학습(Federated Learning)은 기기에서 직접 분산 및 협업 훈련을 가능하게 하여 프라이버시 문제와 항상 연결된 상태의 의존성을 해결합니다.
- 3. L-SGD는 Arm Cortex-M MCU에서의 신경망 훈련을 가능하게 한 경량화된 확률적 경사 하강법의 변형입니다.
- 4. 본 연구는 RISC-V 기반 MCU로 L-SGD를 확장하여, RISC-V MCU에서 부동 소수점 유닛(FPU)의 부재가 성능에 미치는 영향을 강조합니다.
- 5. RISC-V를 위한 8비트 양자화된 L-SGD 버전을 도입하여 메모리 사용량을 약 4배 줄이고 훈련 시간을 2.2배 단축하면서 정확도 저하는 미미합니다.


---

*Generated on 2025-09-24 14:45:53*