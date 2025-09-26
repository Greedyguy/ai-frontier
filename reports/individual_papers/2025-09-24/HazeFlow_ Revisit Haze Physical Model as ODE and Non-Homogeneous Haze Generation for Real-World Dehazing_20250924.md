<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:42:02.801709",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "HazeFlow",
    "Atmospheric Scattering Model",
    "Markov Chain Brownian Motion",
    "Real-world Dehazing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "HazeFlow": 0.8,
    "Atmospheric Scattering Model": 0.82,
    "Markov Chain Brownian Motion": 0.75,
    "Real-world Dehazing": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "HazeFlow",
        "canonical": "HazeFlow",
        "aliases": [
          "ODE-based Dehazing"
        ],
        "category": "unique_technical",
        "rationale": "HazeFlow introduces a novel approach to dehazing using ODEs, which is a unique contribution to the field.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Atmospheric Scattering Model",
        "canonical": "Atmospheric Scattering Model",
        "aliases": [
          "ASM"
        ],
        "category": "specific_connectable",
        "rationale": "ASM is a foundational concept in dehazing, providing a basis for linking related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Markov Chain Brownian Motion",
        "canonical": "Markov Chain Brownian Motion",
        "aliases": [
          "MCBM"
        ],
        "category": "unique_technical",
        "rationale": "MCBM is a novel method for generating non-homogeneous haze, enhancing the adaptability of dehazing models.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Real-world Dehazing",
        "canonical": "Real-world Dehazing",
        "aliases": [
          "Dehazing in Real Scenarios"
        ],
        "category": "broad_technical",
        "rationale": "Real-world dehazing is a critical application area connecting various dehazing techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
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
      "candidate_surface": "HazeFlow",
      "resolved_canonical": "HazeFlow",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Atmospheric Scattering Model",
      "resolved_canonical": "Atmospheric Scattering Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Markov Chain Brownian Motion",
      "resolved_canonical": "Markov Chain Brownian Motion",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Real-world Dehazing",
      "resolved_canonical": "Real-world Dehazing",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# HazeFlow: Revisit Haze Physical Model as ODE and Non-Homogeneous Haze Generation for Real-World Dehazing

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18190.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18190](https://arxiv.org/abs/2509.18190)

## 🔗 유사한 논문
- [[2025-09-18/FlowCast-ODE_ Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration_20250918|FlowCast-ODE: Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration]] (81.3% similar)
- [[2025-09-19/Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models_20250919|Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models]] (81.1% similar)
- [[2025-09-23/Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding_20250923|Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding]] (81.1% similar)
- [[2025-09-22/Generalizable Holographic Reconstruction via Amplitude-Only Diffusion Priors_20250922|Generalizable Holographic Reconstruction via Amplitude-Only Diffusion Priors]] (80.8% similar)
- [[2025-09-23/Efficient Rectified Flow for Image Fusion_20250923|Efficient Rectified Flow for Image Fusion]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Real-world Dehazing|Real-world Dehazing]]
**🔗 Specific Connectable**: [[keywords/Atmospheric Scattering Model|Atmospheric Scattering Model]]
**⚡ Unique Technical**: [[keywords/HazeFlow|HazeFlow]], [[keywords/Markov Chain Brownian Motion|Markov Chain Brownian Motion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18190v1 Announce Type: cross 
Abstract: Dehazing involves removing haze or fog from images to restore clarity and improve visibility by estimating atmospheric scattering effects. While deep learning methods show promise, the lack of paired real-world training data and the resulting domain gap hinder generalization to real-world scenarios. In this context, physics-grounded learning becomes crucial; however, traditional methods based on the Atmospheric Scattering Model (ASM) often fall short in handling real-world complexities and diverse haze patterns. To solve this problem, we propose HazeFlow, a novel ODE-based framework that reformulates ASM as an ordinary differential equation (ODE). Inspired by Rectified Flow (RF), HazeFlow learns an optimal ODE trajectory to map hazy images to clean ones, enhancing real-world dehazing performance with only a single inference step. Additionally, we introduce a non-homogeneous haze generation method using Markov Chain Brownian Motion (MCBM) to address the scarcity of paired real-world data. By simulating realistic haze patterns through MCBM, we enhance the adaptability of HazeFlow to diverse real-world scenarios. Through extensive experiments, we demonstrate that HazeFlow achieves state-of-the-art performance across various real-world dehazing benchmark datasets.

## 📝 요약

이 논문은 이미지에서 안개를 제거하여 선명도를 높이는 문제를 다룹니다. 기존의 심층 학습 방법은 실제 데이터 부족으로 인해 일반화에 한계가 있습니다. 이를 해결하기 위해, 저자들은 새로운 ODE 기반 프레임워크인 HazeFlow를 제안합니다. HazeFlow는 대기 산란 모델(ASM)을 보통 미분 방정식(ODE)으로 재구성하여 안개 낀 이미지를 깨끗한 이미지로 변환하는 최적의 경로를 학습합니다. 또한, 마르코프 체인 브라운 운동(MCBM)을 사용하여 다양한 안개 패턴을 생성함으로써 실제 데이터 부족 문제를 해결합니다. 실험 결과, HazeFlow는 다양한 실제 안개 제거 벤치마크 데이터셋에서 최첨단 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. HazeFlow는 대기 산란 모델(ASM)을 상미분 방정식(ODE)으로 재구성하여 안개 제거 성능을 향상시킵니다.
- 2. HazeFlow는 Rectified Flow(RF)에서 영감을 받아 단일 추론 단계로 흐릿한 이미지를 선명하게 변환합니다.
- 3. Markov Chain Brownian Motion(MCBM)을 활용한 비균질 안개 생성 방법을 도입하여 실제 데이터 부족 문제를 해결합니다.
- 4. HazeFlow는 다양한 실제 안개 제거 벤치마크 데이터셋에서 최첨단 성능을 입증합니다.


---

*Generated on 2025-09-24 13:42:02*