<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:59:39.741740",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Gaussian Processes",
    "Diffusion Bridge Variational Inference",
    "Denoising Diffusion Variational Inference",
    "Neural Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Gaussian Processes": 0.78,
    "Diffusion Bridge Variational Inference": 0.82,
    "Denoising Diffusion Variational Inference": 0.77,
    "Neural Network": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Gaussian Processes",
        "canonical": "Deep Gaussian Processes",
        "aliases": [
          "DGPs"
        ],
        "category": "unique_technical",
        "rationale": "Deep Gaussian Processes are central to the paper's methodology and provide a unique hierarchical Bayesian modeling approach.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Diffusion Bridge Variational Inference",
        "canonical": "Diffusion Bridge Variational Inference",
        "aliases": [
          "DBVI"
        ],
        "category": "unique_technical",
        "rationale": "DBVI is the novel method proposed in the paper, offering a significant improvement over existing techniques.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Denoising Diffusion Variational Inference",
        "canonical": "Denoising Diffusion Variational Inference",
        "aliases": [
          "DDVI"
        ],
        "category": "unique_technical",
        "rationale": "DDVI is a foundational method that DBVI extends, making it crucial for understanding the paper's contributions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Neural Network",
        "canonical": "Neural Network",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Neural Networks are used for parameterizing the initial distribution, linking to broader machine learning concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "posterior inference",
      "inducing variables",
      "ELBO objective"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Gaussian Processes",
      "resolved_canonical": "Deep Gaussian Processes",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Diffusion Bridge Variational Inference",
      "resolved_canonical": "Diffusion Bridge Variational Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Denoising Diffusion Variational Inference",
      "resolved_canonical": "Denoising Diffusion Variational Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Diffusion Bridge Variational Inference for Deep Gaussian Processes

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19078.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.19078](https://arxiv.org/abs/2509.19078)

## 🔗 유사한 논문
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (83.9% similar)
- [[2025-09-22/Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising_20250922|Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising]] (82.2% similar)
- [[2025-09-23/DiffQ_ Unified Parameter Initialization for Variational Quantum Algorithms via Diffusion Models_20250923|DiffQ: Unified Parameter Initialization for Variational Quantum Algorithms via Diffusion Models]] (81.9% similar)
- [[2025-09-23/Robust, Online, and Adaptive Decentralized Gaussian Processes_20250923|Robust, Online, and Adaptive Decentralized Gaussian Processes]] (81.6% similar)
- [[2025-09-22/DiffusionNFT_ Online Diffusion Reinforcement with Forward Process_20250922|DiffusionNFT: Online Diffusion Reinforcement with Forward Process]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Deep Gaussian Processes|Deep Gaussian Processes]], [[keywords/Diffusion Bridge Variational Inference|Diffusion Bridge Variational Inference]], [[keywords/Denoising Diffusion Variational Inference|Denoising Diffusion Variational Inference]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19078v1 Announce Type: new 
Abstract: Deep Gaussian processes (DGPs) enable expressive hierarchical Bayesian modeling but pose substantial challenges for posterior inference, especially over inducing variables. Denoising diffusion variational inference (DDVI) addresses this by modeling the posterior as a time-reversed diffusion from a simple Gaussian prior. However, DDVI's fixed unconditional starting distribution remains far from the complex true posterior, resulting in inefficient inference trajectories and slow convergence. In this work, we propose Diffusion Bridge Variational Inference (DBVI), a principled extension of DDVI that initiates the reverse diffusion from a learnable, data-dependent initial distribution. This initialization is parameterized via an amortized neural network and progressively adapted using gradients from the ELBO objective, reducing the posterior gap and improving sample efficiency. To enable scalable amortization, we design the network to operate on the inducing inputs, which serve as structured, low-dimensional summaries of the dataset and naturally align with the inducing variables' shape. DBVI retains the mathematical elegance of DDVI, including Girsanov-based ELBOs and reverse-time SDEs,while reinterpreting the prior via a Doob-bridged diffusion process. We derive a tractable training objective under this formulation and implement DBVI for scalable inference in large-scale DGPs. Across regression, classification, and image reconstruction tasks, DBVI consistently outperforms DDVI and other variational baselines in predictive accuracy, convergence speed, and posterior quality.

## 📝 요약

이 논문은 딥 가우시안 프로세스(DGP)의 후방 추론 문제를 해결하기 위해 새로운 방법론인 Diffusion Bridge Variational Inference(DBVI)를 제안합니다. 기존의 Denoising Diffusion Variational Inference(DDVI)는 고정된 시작 분포로 인해 비효율적인 추론 경로와 느린 수렴 속도를 보였으나, DBVI는 학습 가능한 데이터 의존적 초기 분포를 도입하여 이러한 문제를 개선합니다. 이 초기화는 신경망을 통해 매개변수화되며, ELBO 목표의 그래디언트를 사용해 점진적으로 조정됩니다. DBVI는 DDVI의 수학적 우아함을 유지하면서도 Doob-브릿지 확산 과정을 통해 사전 분포를 재해석합니다. 이를 통해 대규모 DGP에서의 확장 가능한 추론을 가능하게 하며, 회귀, 분류, 이미지 복원 작업에서 DDVI 및 다른 변분 기법보다 예측 정확도, 수렴 속도, 후방 분포 품질에서 우수한 성능을 보입니다.

## 🎯 주요 포인트

- 1. DBVI는 DDVI의 확장으로, 데이터에 의존하는 초기 분포를 통해 역확산을 시작하여 후방 분포와의 차이를 줄이고 샘플 효율성을 향상시킵니다.
- 2. DBVI는 유도 입력에 작동하는 네트워크를 설계하여 대규모 데이터셋에서 확장 가능한 추론을 가능하게 합니다.
- 3. DBVI는 Girsanov 기반 ELBO와 역시간 SDE를 포함한 DDVI의 수학적 우아함을 유지하면서, Doob-브리지 확산 과정을 통해 사전 분포를 재해석합니다.
- 4. DBVI는 회귀, 분류, 이미지 재구성 작업에서 예측 정확도, 수렴 속도, 후방 분포 품질 측면에서 DDVI 및 기타 변분 기준선을 일관되게 능가합니다.


---

*Generated on 2025-09-24 14:59:39*