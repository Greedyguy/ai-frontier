---
keywords:
  - Quantization-Aware Training
  - Maximum Entropy Coding Quantization
  - Mixture Of Experts
  - Computer Vision
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15514
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:59:25.768393",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Quantization-Aware Training",
    "Maximum Entropy Coding Quantization",
    "Mixture Of Experts",
    "Computer Vision"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Quantization-Aware Training": 0.8,
    "Maximum Entropy Coding Quantization": 0.82,
    "Mixture Of Experts": 0.77,
    "Computer Vision": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Quantization-Aware Training",
        "canonical": "Quantization-Aware Training",
        "aliases": [
          "QAT"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific method central to the paper's contribution, offering a unique approach to neural network optimization.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Maximum Entropy Coding Quantization",
        "canonical": "Maximum Entropy Coding Quantization",
        "aliases": [
          "MEC-Quant"
        ],
        "category": "unique_technical",
        "rationale": "Represents the novel technique introduced in the paper, crucial for understanding the proposed advancements.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Mixture Of Experts",
        "canonical": "Mixture Of Experts",
        "aliases": [
          "MOE"
        ],
        "category": "specific_connectable",
        "rationale": "A well-known model architecture that enhances understanding of the computational strategies used.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Computer Vision",
        "canonical": "Computer Vision",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "The application domain of the proposed technique, relevant for contextualizing its impact.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.5,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "Full Precision",
      "in-distribution samples"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Quantization-Aware Training",
      "resolved_canonical": "Quantization-Aware Training",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Maximum Entropy Coding Quantization",
      "resolved_canonical": "Maximum Entropy Coding Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Mixture Of Experts",
      "resolved_canonical": "Mixture Of Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Computer Vision",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.5,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# MEC-Quant: Maximum Entropy Coding for Extremely Low Bit Quantization-Aware Training

**Korean Title:** MEC-Quant: 극저비트 양자화 인식 훈련을 위한 최대 엔트로피 코딩

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15514.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15514](https://arxiv.org/abs/2509.15514)

## 🔗 유사한 논문
- [[2025-09-22/Quantum Enhanced Anomaly Detection for ADS-B Data using Hybrid Deep Learning_20250922|Quantum Enhanced Anomaly Detection for ADS-B Data using Hybrid Deep Learning]] (81.5% similar)
- [[2025-09-17/Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks_20250917|Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks]] (81.2% similar)
- [[2025-09-22/IMPQ_ Interaction-Aware Layerwise Mixed Precision Quantization for LLMs_20250922|IMPQ: Interaction-Aware Layerwise Mixed Precision Quantization for LLMs]] (81.0% similar)
- [[2025-09-22/Quantum Generative Adversarial Autoencoders_ Learning latent representations for quantum data generation_20250922|Quantum Generative Adversarial Autoencoders: Learning latent representations for quantum data generation]] (80.8% similar)
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Computer Vision|Computer Vision]]
**🔗 Specific Connectable**: [[keywords/Mixture Of Experts|Mixture Of Experts]]
**⚡ Unique Technical**: [[keywords/Quantization-Aware Training|Quantization-Aware Training]], [[keywords/Maximum Entropy Coding Quantization|Maximum Entropy Coding Quantization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15514v1 Announce Type: new 
Abstract: Quantization-Aware Training (QAT) has driven much attention to produce efficient neural networks. Current QAT still obtains inferior performances compared with the Full Precision (FP) counterpart. In this work, we argue that quantization inevitably introduce biases into the learned representation, especially under the extremely low-bit setting. To cope with this issue, we propose Maximum Entropy Coding Quantization (MEC-Quant), a more principled objective that explicitly optimizes on the structure of the representation, so that the learned representation is less biased and thus generalizes better to unseen in-distribution samples. To make the objective end-to-end trainable, we propose to leverage the minimal coding length in lossy data coding as a computationally tractable surrogate for the entropy, and further derive a scalable reformulation of the objective based on Mixture Of Experts (MOE) that not only allows fast computation but also handles the long-tailed distribution for weights or activation values. Extensive experiments on various tasks on computer vision tasks prove its superiority. With MEC-Qaunt, the limit of QAT is pushed to the x-bit activation for the first time and the accuracy of MEC-Quant is comparable to or even surpass the FP counterpart. Without bells and whistles, MEC-Qaunt establishes a new state of the art for QAT.

## 🔍 Abstract (한글 번역)

arXiv:2509.15514v1 발표 유형: 신규  
초록: 양자화 인식 훈련(Quantization-Aware Training, QAT)은 효율적인 신경망을 생성하기 위해 많은 주목을 받고 있습니다. 현재의 QAT는 여전히 완전 정밀도(Full Precision, FP)와 비교하여 성능이 열등합니다. 이 연구에서는 양자화가 학습된 표현에 필연적으로 편향을 도입한다고 주장하며, 특히 극도로 낮은 비트 설정에서 그러합니다. 이 문제를 해결하기 위해 우리는 학습된 표현이 덜 편향되고 따라서 보지 못한 분포 내 샘플에 더 잘 일반화되도록 표현의 구조를 명시적으로 최적화하는 보다 원칙적인 목표인 최대 엔트로피 코딩 양자화(Maximum Entropy Coding Quantization, MEC-Quant)를 제안합니다. 목표를 종단 간 학습 가능하게 만들기 위해, 우리는 손실 데이터 코딩에서 최소 코딩 길이를 엔트로피의 계산적으로 실행 가능한 대리로 활용하고, 가중치 또는 활성화 값의 긴 꼬리 분포를 처리할 뿐만 아니라 빠른 계산을 가능하게 하는 전문가 혼합(Mixture Of Experts, MOE)에 기반한 목표의 확장 가능한 재구성을 추가로 도출합니다. 다양한 컴퓨터 비전 작업에 대한 광범위한 실험은 그 우수성을 입증합니다. MEC-Quant를 통해 QAT의 한계는 처음으로 x-비트 활성화로 확장되었으며, MEC-Quant의 정확도는 FP와 비교할 만하거나 심지어 능가합니다. 추가적인 장치 없이도 MEC-Quant는 QAT의 새로운 최첨단을 확립합니다.

## 📝 요약

이 논문에서는 양자화 인식 훈련(QAT)의 성능 한계를 극복하기 위해 최대 엔트로피 코딩 양자화(MEC-Quant)를 제안합니다. 기존 QAT는 완전 정밀(FP) 네트워크에 비해 성능이 떨어지는데, 이는 양자화가 학습된 표현에 편향을 초래하기 때문입니다. MEC-Quant는 표현 구조를 명시적으로 최적화하여 이러한 편향을 줄이고, 새로운 데이터에 대한 일반화 성능을 향상시킵니다. 이를 위해 손실 데이터 코딩의 최소 코딩 길이를 엔트로피의 근사치로 사용하고, 전문가 혼합(MOE) 기반의 확장 가능한 재구성을 통해 빠른 계산과 긴 꼬리 분포 처리를 가능하게 합니다. 다양한 컴퓨터 비전 과제 실험에서 MEC-Quant는 QAT의 한계를 극복하고, FP와 동등하거나 더 나은 정확도를 달성하여 새로운 표준을 세웠습니다.

## 🎯 주요 포인트

- 1. 양자화 인식 훈련(QAT)은 효율적인 신경망을 생성하기 위해 주목받고 있지만, 여전히 완전 정밀(FP) 모델에 비해 성능이 떨어진다.
- 2. 양자화는 특히 극단적으로 낮은 비트 설정에서 학습된 표현에 편향을 도입할 수 있다.
- 3. Maximum Entropy Coding Quantization(MEC-Quant)은 표현의 구조를 명시적으로 최적화하여 편향을 줄이고 일반화 성능을 향상시키는 방법을 제안한다.
- 4. MEC-Quant는 손실 데이터 코딩의 최소 코딩 길이를 엔트로피의 대체물로 사용하여 목표를 엔드 투 엔드로 학습 가능하게 만든다.
- 5. 다양한 컴퓨터 비전 작업에서 MEC-Quant는 QAT의 한계를 극복하고, FP 모델과 비교할 때 동등하거나 더 나은 정확도를 보여준다.


---

*Generated on 2025-09-23 11:59:25*