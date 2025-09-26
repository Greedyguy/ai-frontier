---
keywords:
  - Neural Network
  - Quantization
  - Sparsification
  - Straight-Through Estimator
  - Denoising Dequantization Transform
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2409.09245
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:16:28.558791",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Quantization",
    "Sparsification",
    "Straight-Through Estimator",
    "Denoising Dequantization Transform"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Quantization": 0.8,
    "Sparsification": 0.78,
    "Straight-Through Estimator": 0.7,
    "Denoising Dequantization Transform": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "Neural Nets"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on training methods, providing a strong link to existing neural network research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Quantization",
        "canonical": "Quantization",
        "aliases": [
          "Quantizing"
        ],
        "category": "unique_technical",
        "rationale": "A key technical process discussed in the paper, crucial for understanding precision in neural networks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Sparsification",
        "canonical": "Sparsification",
        "aliases": [
          "Sparse Training"
        ],
        "category": "unique_technical",
        "rationale": "Essential for linking research on reducing neural network complexity and enhancing efficiency.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Straight-Through Estimator",
        "canonical": "Straight-Through Estimator",
        "aliases": [
          "STE"
        ],
        "category": "unique_technical",
        "rationale": "A specific technique addressed in the paper, relevant for understanding the proposed improvements.",
        "novelty_score": 0.6,
        "connectivity_score": 0.5,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Denoising Dequantization Transform",
        "canonical": "Denoising Dequantization Transform",
        "aliases": [
          "DDT"
        ],
        "category": "unique_technical",
        "rationale": "Introduced as a novel solution in the paper, critical for linking to new methods in neural network training.",
        "novelty_score": 0.8,
        "connectivity_score": 0.4,
        "specificity_score": 0.9,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "method",
      "process",
      "approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Networks",
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
      "candidate_surface": "Quantization",
      "resolved_canonical": "Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Sparsification",
      "resolved_canonical": "Sparsification",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Straight-Through Estimator",
      "resolved_canonical": "Straight-Through Estimator",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.5,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Denoising Dequantization Transform",
      "resolved_canonical": "Denoising Dequantization Transform",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.4,
        "specificity": 0.9,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Robust Training of Neural Networks at Arbitrary Precision and Sparsity

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2409.09245.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2409.09245](https://arxiv.org/abs/2409.09245)

## 🔗 유사한 논문
- [[2025-09-23/Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks_20250923|Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks]] (84.0% similar)
- [[2025-09-22/MEC-Quant_ Maximum Entropy Coding for Extremely Low Bit Quantization-Aware Training_20250922|MEC-Quant: Maximum Entropy Coding for Extremely Low Bit Quantization-Aware Training]] (82.7% similar)
- [[2025-09-23/Machine Learning for Quantum Noise Reduction_20250923|Machine Learning for Quantum Noise Reduction]] (82.3% similar)
- [[2025-09-22/Flavors of Margin_ Implicit Bias of Steepest Descent in Homogeneous Neural Networks_20250922|Flavors of Margin: Implicit Bias of Steepest Descent in Homogeneous Neural Networks]] (82.3% similar)
- [[2025-09-24/Energy-convergence trade off for the training of neural networks on bio-inspired hardware_20250924|Energy-convergence trade off for the training of neural networks on bio-inspired hardware]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Quantization|Quantization]], [[keywords/Sparsification|Sparsification]], [[keywords/Straight-Through Estimator|Straight-Through Estimator]], [[keywords/Denoising Dequantization Transform|Denoising Dequantization Transform]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.09245v2 Announce Type: replace-cross 
Abstract: The discontinuous operations inherent in quantization and sparsification introduce a long-standing obstacle to backpropagation, particularly in ultra-low precision and sparse regimes. The standard Straight-Through Estimator (STE) is widely used to address this, but the well-understood mismatch between its quantization-aware forward pass and quantization-oblivious backward pass leads to unmanaged error that can corrupt the learning process. We solve this by introducing a denoising dequantization transform derived from a principled ridge regression objective. This transform makes the entire learning process aware of and robust to the quantization error that STE's surrogate gradient bypasses, by creating an explicit, corrective gradient path. We extend this principle to sparsification by viewing it as a special form of quantization that maps insignificant values to zero. Our unified framework allows existing models to be trained at a wide spectrum of precisions and sparsity levels with off-the-shelf recipes, achieving stable training of fully binary (A1W1) and sparse sub-1-bit networks where other methods falter. This approach yields state-of-the-art results and provides a theoretically-grounded path to hyper-efficient neural networks.

## 📝 요약

이 논문은 양자화와 희소화 과정에서 발생하는 불연속적 연산이 역전파에 미치는 문제를 해결하기 위해 새로운 방법론을 제안합니다. 기존의 Straight-Through Estimator(STE)는 양자화 인식 전방 패스와 양자화 무시 후방 패스 간의 불일치로 인해 학습 과정에 오류를 초래할 수 있습니다. 이를 해결하기 위해, 저자들은 원칙적인 릿지 회귀 목표에서 파생된 디노이징 디퀀타이제이션 변환을 도입하여, 양자화 오류를 명시적으로 보정하는 경로를 제공합니다. 또한, 희소화를 양자화의 특별한 형태로 보고 이를 통합하여 다양한 정밀도와 희소성 수준에서 안정적인 학습을 가능하게 합니다. 이 접근법은 완전 이진 및 희소 서브 1비트 네트워크에서 최첨단 결과를 달성하며, 이론적으로 효율적인 신경망 설계의 길을 제시합니다.

## 🎯 주요 포인트

- 1. 양자화 및 희소화의 불연속적 연산은 초저정밀 및 희소 환경에서 역전파에 장애를 초래한다.
- 2. 표준 직선 추정기(STE)는 양자화 인식 전방 패스와 양자화 비인식 후방 패스 간의 불일치로 인해 학습 과정에 오류를 유발할 수 있다.
- 3. 본 연구는 원칙적인 능선 회귀 목표에서 파생된 잡음 제거 디양자화 변환을 도입하여 이 문제를 해결한다.
- 4. 제안된 변환은 STE의 대체 경사가 우회하는 양자화 오류에 대해 학습 과정을 인식하고 견고하게 만든다.
- 5. 본 접근법은 완전 이진 및 희소 서브 1비트 네트워크의 안정적인 학습을 가능하게 하며, 이론적으로 근거 있는 초효율 신경망으로의 경로를 제공한다.


---

*Generated on 2025-09-25 16:16:28*