---
keywords:
  - Deep Learning
  - Neural Network
  - Direction of Arrival Estimation
  - Spatial Spectrum
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15475
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:49:27.660341",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Neural Network",
    "Direction of Arrival Estimation",
    "Spatial Spectrum"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Neural Network": 0.82,
    "Direction of Arrival Estimation": 0.78,
    "Spatial Spectrum": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep Learning is a fundamental technique underlying the proposed method, facilitating connections with other neural network-based approaches.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Neural Network",
        "canonical": "Neural Network",
        "aliases": [
          "NN"
        ],
        "category": "broad_technical",
        "rationale": "The use of a neural network is central to the proposed architecture, enabling links to other neural network methodologies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.55,
        "link_intent_score": 0.82
      },
      {
        "surface": "Direction of Arrival Estimation",
        "canonical": "Direction of Arrival Estimation",
        "aliases": [
          "DOA Estimation"
        ],
        "category": "unique_technical",
        "rationale": "This is the specific problem addressed by the paper, providing a unique technical focus for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Spatial Spectrum",
        "canonical": "Spatial Spectrum",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The concept of spatial spectrum is central to the method, offering a unique technical term for linking.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "Bartlett beamformer",
      "single snapshot",
      "antenna array"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Neural Network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.55,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Direction of Arrival Estimation",
      "resolved_canonical": "Direction of Arrival Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Spatial Spectrum",
      "resolved_canonical": "Spatial Spectrum",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# (SP)$^2$-Net: A Neural Spatial Spectrum Method for DOA Estimation

**Korean Title:** (SP)$^2$-Net: DOA 추정을 위한 신경망 공간 스펙트럼 방법

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15475.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15475](https://arxiv.org/abs/2509.15475)

## 🔗 유사한 논문
- [[2025-09-17/Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations_20250917|Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations]] (79.3% similar)
- [[2025-09-22/DSDNet_ Raw Domain Demoir\'eing via Dual Color-Space Synergy_20250922|DSDNet: Raw Domain Demoir\'eing via Dual Color-Space Synergy]] (79.1% similar)
- [[2025-09-17/DSpAST_ Disentangled Representations for Spatial Audio Reasoning with Large Language Models_20250917|DSpAST: Disentangled Representations for Spatial Audio Reasoning with Large Language Models]] (79.0% similar)
- [[2025-09-22/Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising_20250922|Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising]] (78.5% similar)
- [[2025-09-22/SGMAGNet_ A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark_20250922|SGMAGNet: A Baseline Model for 3D Cloud Phase Structure Reconstruction on a New Passive Active Satellite Benchmark]] (78.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]], [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Direction of Arrival Estimation|Direction of Arrival Estimation]], [[keywords/Spatial Spectrum|Spatial Spectrum]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15475v1 Announce Type: cross 
Abstract: We consider the problem of estimating the directions of arrival (DOAs) of multiple sources from a single snapshot of an antenna array, a task with many practical applications. In such settings, the classical Bartlett beamformer is commonly used, as maximum likelihood estimation becomes impractical when the number of sources is unknown or large, and spectral methods based on the sample covariance are not applicable due to the lack of multiple snapshots. However, the accuracy and resolution of the Bartlett beamformer are fundamentally limited by the array aperture. In this paper, we propose a deep learning technique, comprising a novel architecture and training strategy, for generating a high-resolution spatial spectrum from a single snapshot. Specifically, we train a deep neural network that takes the measurements and a hypothesis angle as input and learns to output a score consistent with the capabilities of a much wider array. At inference time, a heatmap can be produced by scanning an arbitrary set of angles. We demonstrate the advantages of our trained model, named (SP)$^2$-Net, over the Bartlett beamformer and sparsity-based DOA estimation methods.

## 🔍 Abstract (한글 번역)

arXiv:2509.15475v1 발표 유형: 교차  
초록: 우리는 안테나 배열의 단일 스냅샷으로부터 여러 소스의 도래 방향(DOAs)을 추정하는 문제를 고려하며, 이는 다양한 실용적인 응용 분야를 가지고 있는 과제입니다. 이러한 상황에서는, 소스의 수가 알려지지 않았거나 많을 때 최대 우도 추정이 비실용적이기 때문에, 고전적인 Bartlett 빔포머가 일반적으로 사용됩니다. 또한, 샘플 공분산에 기반한 스펙트럼 방법은 여러 스냅샷의 부재로 인해 적용할 수 없습니다. 그러나 Bartlett 빔포머의 정확도와 해상도는 근본적으로 배열 개구에 의해 제한됩니다. 본 논문에서는 단일 스냅샷으로부터 고해상도 공간 스펙트럼을 생성하기 위한 새로운 아키텍처와 학습 전략을 포함한 딥러닝 기법을 제안합니다. 구체적으로, 우리는 측정값과 가설 각도를 입력으로 받아 훨씬 더 넓은 배열의 능력과 일치하는 점수를 출력하도록 학습하는 심층 신경망을 훈련합니다. 추론 시에는 임의의 각도 집합을 스캔하여 히트맵을 생성할 수 있습니다. 우리는 Bartlett 빔포머와 희소성 기반의 DOA 추정 방법에 비해 (SP)$^2$-Net이라는 이름의 훈련된 모델의 장점을 입증합니다.

## 📝 요약

이 논문은 안테나 배열의 단일 스냅샷에서 다중 신호의 도착 방향(DOA)을 추정하는 문제를 다룹니다. 기존의 Bartlett 빔포머는 배열 개구에 의해 정확도와 해상도가 제한되며, 최대 우도 추정법은 실용적이지 않습니다. 이를 해결하기 위해, 본 연구에서는 새로운 아키텍처와 학습 전략을 갖춘 딥러닝 기법을 제안합니다. 제안된 모델 (SP)$^2$-Net은 측정값과 가설 각도를 입력으로 받아 넓은 배열의 성능에 부합하는 점수를 출력하도록 학습됩니다. 실험 결과, 제안된 모델은 Bartlett 빔포머 및 희소성 기반 DOA 추정 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 본 연구는 안테나 배열의 단일 스냅샷에서 다중 소스의 도착 방향(DOAs)을 추정하는 문제를 다룹니다.
- 2. 기존의 Bartlett 빔포머는 배열 개구에 의해 정확도와 해상도가 제한됩니다.
- 3. 본 논문에서는 단일 스냅샷에서 고해상도 공간 스펙트럼을 생성하기 위한 새로운 딥러닝 기법을 제안합니다.
- 4. 제안된 모델 (SP)$^2$-Net은 Bartlett 빔포머 및 희소성 기반 DOA 추정 방법보다 우수한 성능을 보입니다.
- 5. 학습된 심층 신경망은 측정값과 가설 각도를 입력으로 받아 더 넓은 배열의 성능과 일치하는 점수를 출력하도록 학습됩니다.


---

*Generated on 2025-09-23 10:49:27*