---
keywords:
  - LVADNet3D
  - Left Ventricular Assist Devices
  - Computational Fluid Dynamics
  - 3D Convolutional Autoencoder
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16860
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:43:48.751490",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "LVADNet3D",
    "Left Ventricular Assist Devices",
    "Computational Fluid Dynamics",
    "3D Convolutional Autoencoder"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "LVADNet3D": 0.88,
    "Left Ventricular Assist Devices": 0.82,
    "Computational Fluid Dynamics": 0.78,
    "3D Convolutional Autoencoder": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LVADNet3D",
        "canonical": "LVADNet3D",
        "aliases": [
          "3D convolutional autoencoder for LVAD",
          "LVADNet"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel model specifically designed for reconstructing intraventricular flow, which is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Left Ventricular Assist Devices",
        "canonical": "Left Ventricular Assist Devices",
        "aliases": [
          "LVADs"
        ],
        "category": "specific_connectable",
        "rationale": "LVADs are critical to the study's context and are a key medical device linked to the paper's focus.",
        "novelty_score": 0.45,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Computational Fluid Dynamics",
        "canonical": "Computational Fluid Dynamics",
        "aliases": [
          "CFD"
        ],
        "category": "broad_technical",
        "rationale": "CFD is a fundamental technique used in the study to generate synthetic datasets, linking it to broader computational methods.",
        "novelty_score": 0.3,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "3D convolutional autoencoder",
        "canonical": "3D Convolutional Autoencoder",
        "aliases": [
          "3D autoencoder"
        ],
        "category": "specific_connectable",
        "rationale": "This architecture is central to the paper's methodology and connects to broader deep learning techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.77,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "hemodynamic data",
      "velocity fields"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LVADNet3D",
      "resolved_canonical": "LVADNet3D",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Left Ventricular Assist Devices",
      "resolved_canonical": "Left Ventricular Assist Devices",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Computational Fluid Dynamics",
      "resolved_canonical": "Computational Fluid Dynamics",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "3D convolutional autoencoder",
      "resolved_canonical": "3D Convolutional Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.77,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# LVADNet3D: A Deep Autoencoder for Reconstructing 3D Intraventricular Flow from Sparse Hemodynamic Data

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16860.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16860](https://arxiv.org/abs/2509.16860)

## 🔗 유사한 논문
- [[2025-09-23/An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation_20250923|An Efficient Dual-Line Decoder Network with Multi-Scale Convolutional Attention for Multi-organ Segmentation]] (82.8% similar)
- [[2025-09-18/Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (82.0% similar)
- [[2025-09-22/A Flow-rate-conserving CNN-based Domain Decomposition Method for Blood Flow Simulations_20250922|A Flow-rate-conserving CNN-based Domain Decomposition Method for Blood Flow Simulations]] (81.9% similar)
- [[2025-09-23/MRN_ Harnessing 2D Vision Foundation Models for Diagnosing Parkinson's Disease with Limited 3D MR Data_20250923|MRN: Harnessing 2D Vision Foundation Models for Diagnosing Parkinson's Disease with Limited 3D MR Data]] (80.4% similar)
- [[2025-09-18/HD3C_ Efficient Medical Data Classification for Embedded Devices_20250918|HD3C: Efficient Medical Data Classification for Embedded Devices]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Computational Fluid Dynamics|Computational Fluid Dynamics]]
**🔗 Specific Connectable**: [[keywords/Left Ventricular Assist Devices|Left Ventricular Assist Devices]], [[keywords/3D Convolutional Autoencoder|3D Convolutional Autoencoder]]
**⚡ Unique Technical**: [[keywords/LVADNet3D|LVADNet3D]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16860v1 Announce Type: new 
Abstract: Accurate assessment of intraventricular blood flow is essential for evaluating hemodynamic conditions in patients supported by Left Ventricular Assist Devices (LVADs). However, clinical imaging is either incompatible with LVADs or yields sparse, low-quality velocity data. While Computational Fluid Dynamics (CFD) simulations provide high-fidelity data, they are computationally intensive and impractical for routine clinical use. To address this, we propose LVADNet3D, a 3D convolutional autoencoder that reconstructs full-resolution intraventricular velocity fields from sparse velocity vector inputs. In contrast to a standard UNet3D model, LVADNet3D incorporates hybrid downsampling and a deeper encoder-decoder architecture with increased channel capacity to better capture spatial flow patterns. To train and evaluate the models, we generate a high-resolution synthetic dataset of intraventricular blood flow in LVAD-supported hearts using CFD simulations. We also investigate the effect of conditioning the models on anatomical and physiological priors. Across various input configurations, LVADNet3D outperforms the baseline UNet3D model, yielding lower reconstruction error and higher PSNR results.

## 📝 요약

이 논문은 LVAD(좌심실 보조 장치) 지원 환자의 혈류 역학 상태 평가를 위한 새로운 방법론을 제안합니다. 기존의 임상 이미징은 LVAD와 호환되지 않거나 낮은 품질의 데이터를 제공하며, CFD 시뮬레이션은 고품질 데이터를 제공하지만 계산 비용이 높아 실용적이지 않습니다. 이를 해결하기 위해, 연구진은 LVADNet3D라는 3D 컨볼루션 오토인코더를 개발하여 희박한 속도 벡터 입력으로부터 고해상도의 심실 내 속도장을 재구성합니다. LVADNet3D는 하이브리드 다운샘플링과 깊은 인코더-디코더 구조를 통해 공간적 흐름 패턴을 더 잘 포착합니다. 모델 훈련 및 평가를 위해 CFD 시뮬레이션을 사용하여 고해상도 합성 데이터를 생성하였으며, 해부학적 및 생리학적 조건을 모델에 적용하는 효과도 조사했습니다. LVADNet3D는 다양한 입력 구성에서 UNet3D 모델보다 낮은 재구성 오류와 높은 PSNR 결과를 보여줍니다.

## 🎯 주요 포인트

- 1. LVADNet3D는 3D 컨볼루셔널 오토인코더로, 희소한 속도 벡터 입력으로부터 고해상도의 심실 내 속도장을 재구성합니다.
- 2. LVADNet3D는 하이브리드 다운샘플링과 더 깊은 인코더-디코더 아키텍처를 통해 공간적 흐름 패턴을 효과적으로 포착합니다.
- 3. 고해상도 합성 데이터셋을 사용하여 모델을 훈련 및 평가하며, 해부학적 및 생리학적 조건을 모델에 반영하는 효과를 조사합니다.
- 4. LVADNet3D는 다양한 입력 구성에서 UNet3D 모델보다 낮은 재구성 오류와 높은 PSNR 결과를 보여줍니다.


---

*Generated on 2025-09-24 01:43:48*