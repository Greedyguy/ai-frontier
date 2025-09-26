---
keywords:
  - Reinforcement Learning
  - Low-Dose CT Denoising
  - Encoder-Decoder
  - Proximal Policy Optimization
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.03185
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:31:00.581281",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Low-Dose CT Denoising",
    "Encoder-Decoder",
    "Proximal Policy Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning": 0.78,
    "Low-Dose CT Denoising": 0.81,
    "Encoder-Decoder": 0.75,
    "Proximal Policy Optimization": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is a foundational concept that connects to various machine learning techniques and applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Low-Dose CT Denoising",
        "canonical": "Low-Dose CT Denoising",
        "aliases": [
          "LDCT Denoising"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area that highlights the unique focus of the paper on medical imaging.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.81
      },
      {
        "surface": "Encoder-Decoder",
        "canonical": "Encoder-Decoder",
        "aliases": [
          "ED"
        ],
        "category": "specific_connectable",
        "rationale": "Encoder-Decoder architectures are widely used in various deep learning models, facilitating connections to related research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.79,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Proximal Policy Optimization",
        "canonical": "Proximal Policy Optimization",
        "aliases": [
          "PPO"
        ],
        "category": "specific_connectable",
        "rationale": "PPO is a popular reinforcement learning algorithm, making it relevant for linking to other RL-based research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.84,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Low-Dose CT Denoising",
      "resolved_canonical": "Low-Dose CT Denoising",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Encoder-Decoder",
      "resolved_canonical": "Encoder-Decoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.79,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Proximal Policy Optimization",
      "resolved_canonical": "Proximal Policy Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.84,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# PPORLD-EDNetLDCT: A Proximal Policy Optimization-Based Reinforcement Learning Framework for Adaptive Low-Dose CT Denoising

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.03185.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.03185](https://arxiv.org/abs/2509.03185)

## 🔗 유사한 논문
- [[2025-09-23/An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation_20250923|An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation]] (84.5% similar)
- [[2025-09-22/DPC-QA Net_ A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images_20250922|DPC-QA Net: A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images]] (82.1% similar)
- [[2025-09-22/Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising_20250922|Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising]] (81.3% similar)
- [[2025-09-23/Catching the Details_ Self-Distilled RoI Predictors for Fine-Grained MLLM Perception_20250923|Catching the Details: Self-Distilled RoI Predictors for Fine-Grained MLLM Perception]] (81.2% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Encoder-Decoder|Encoder-Decoder]], [[keywords/Proximal Policy Optimization|Proximal Policy Optimization]]
**⚡ Unique Technical**: [[keywords/Low-Dose CT Denoising|Low-Dose CT Denoising]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.03185v2 Announce Type: replace 
Abstract: Low-dose computed tomography (LDCT) is critical for minimizing radiation exposure, but it often leads to increased noise and reduced image quality. Traditional denoising methods, such as iterative optimization or supervised learning, often fail to preserve image quality. To address these challenges, we introduce PPORLD-EDNetLDCT, a reinforcement learning-based (RL) approach with Encoder-Decoder for LDCT. Our method utilizes a dynamic RL-based approach in which an advanced posterior policy optimization (PPO) algorithm is used to optimize denoising policies in real time, based on image quality feedback, trained via a custom gym environment. The experimental results on the low dose CT image and projection dataset demonstrate that the proposed PPORLD-EDNetLDCT model outperforms traditional denoising techniques and other DL-based methods, achieving a peak signal-to-noise ratio of 41.87, a structural similarity index measure of 0.9814 and a root mean squared error of 0.00236. Moreover, in NIH-AAPM-Mayo Clinic Low Dose CT Challenge dataset our method achieved a PSNR of 41.52, SSIM of 0.9723 and RMSE of 0.0051. Furthermore, we validated the quality of denoising using a classification task in the COVID-19 LDCT dataset, where the images processed by our method improved the classification accuracy to 94%, achieving 4% higher accuracy compared to denoising without RL-based denoising.

## 📝 요약

이 논문은 저선량 컴퓨터 단층촬영(LDCT)에서 발생하는 노이즈와 이미지 품질 저하 문제를 해결하기 위해 강화 학습 기반의 PPORLD-EDNetLDCT를 제안합니다. 이 방법은 이미지 품질 피드백을 기반으로 실시간으로 최적화된 노이즈 제거 정책을 적용하며, 실험 결과 기존의 전통적 및 딥러닝 기반 방법들보다 우수한 성능을 보였습니다. 특히, 피크 신호 대 잡음비(PSNR) 41.87, 구조적 유사성 지수(SSIM) 0.9814, 평균 제곱근 오차(RMSE) 0.00236을 기록했습니다. 또한, COVID-19 LDCT 데이터셋에서 94%의 분류 정확도를 달성하며, RL 기반이 아닌 방법보다 4% 높은 정확도를 보였습니다.

## 🎯 주요 포인트

- 1. 저선량 CT(LDCT)의 방사선 노출을 최소화하면서 이미지 품질을 개선하기 위해 강화 학습 기반의 PPORLD-EDNetLDCT를 제안했습니다.
- 2. 제안된 모델은 이미지 품질 피드백을 기반으로 실시간으로 최적화된 비지도 학습을 수행하며, PPO 알고리즘을 활용해 잡음 제거 정책을 최적화합니다.
- 3. 실험 결과, PPORLD-EDNetLDCT는 기존의 잡음 제거 기법과 다른 딥러닝 기반 방법들보다 우수한 성능을 보였으며, PSNR 41.87, SSIM 0.9814, RMSE 0.00236의 성능을 달성했습니다.
- 4. NIH-AAPM-Mayo Clinic Low Dose CT Challenge 데이터셋에서도 PSNR 41.52, SSIM 0.9723, RMSE 0.0051의 성능을 기록했습니다.
- 5. COVID-19 LDCT 데이터셋의 분류 작업에서 제안된 방법으로 처리된 이미지는 분류 정확도를 94%로 향상시켜, 강화 학습 기반 잡음 제거 없이 처리된 경우보다 4% 높은 정확도를 달성했습니다.


---

*Generated on 2025-09-24 05:31:00*