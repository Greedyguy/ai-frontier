---
keywords:
  - Diff-GNSS
  - GNSS
  - Conditional Diffusion Model
  - Pseudorange Error Estimation
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17397
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:50:09.112858",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diff-GNSS",
    "GNSS",
    "Conditional Diffusion Model",
    "Pseudorange Error Estimation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diff-GNSS": 0.8,
    "GNSS": 0.78,
    "Conditional Diffusion Model": 0.75,
    "Pseudorange Error Estimation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diff-GNSS",
        "canonical": "Diff-GNSS",
        "aliases": [
          "Diffusion-based GNSS",
          "Diffusion GNSS"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework for GNSS error estimation using diffusion models, enhancing connectivity with GNSS and diffusion model research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Global Navigation Satellite Systems",
        "canonical": "GNSS",
        "aliases": [
          "Global Navigation Satellite Systems"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus, linking it to broader GNSS research and applications.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "conditional diffusion model",
        "canonical": "Conditional Diffusion Model",
        "aliases": [
          "diffusion model",
          "conditional model"
        ],
        "category": "broad_technical",
        "rationale": "Highlights the use of diffusion models, a trending approach in machine learning, enhancing connectivity with diffusion-based research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "pseudorange error estimation",
        "canonical": "Pseudorange Error Estimation",
        "aliases": [
          "pseudorange estimation",
          "error estimation"
        ],
        "category": "unique_technical",
        "rationale": "A specific technical focus of the paper, linking it to GNSS error correction research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diff-GNSS",
      "resolved_canonical": "Diff-GNSS",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Global Navigation Satellite Systems",
      "resolved_canonical": "GNSS",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "conditional diffusion model",
      "resolved_canonical": "Conditional Diffusion Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "pseudorange error estimation",
      "resolved_canonical": "Pseudorange Error Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Diff-GNSS: Diffusion-based Pseudorange Error Estimation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17397.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17397](https://arxiv.org/abs/2509.17397)

## 🔗 유사한 논문
- [[2025-09-17/Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations_20250917|Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations]] (84.0% similar)
- [[2025-09-22/Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising_20250922|Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising]] (82.4% similar)
- [[2025-09-22/Communications to Circulations_ 3D Wind Field Retrieval and Real-Time Prediction Using 5G GNSS Signals and Deep Learning_20250922|Communications to Circulations: 3D Wind Field Retrieval and Real-Time Prediction Using 5G GNSS Signals and Deep Learning]] (81.6% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (81.5% similar)
- [[2025-09-23/DiffEye_ Diffusion-Based Continuous Eye-Tracking Data Generation Conditioned on Natural Images_20250923|DiffEye: Diffusion-Based Continuous Eye-Tracking Data Generation Conditioned on Natural Images]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Conditional Diffusion Model|Conditional Diffusion Model]]
**🔗 Specific Connectable**: [[keywords/GNSS|GNSS]]
**⚡ Unique Technical**: [[keywords/Diff-GNSS|Diff-GNSS]], [[keywords/Pseudorange Error Estimation|Pseudorange Error Estimation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17397v1 Announce Type: new 
Abstract: Global Navigation Satellite Systems (GNSS) are vital for reliable urban positioning. However, multipath and non-line-of-sight reception often introduce large measurement errors that degrade accuracy. Learning-based methods for predicting and compensating pseudorange errors have gained traction, but their performance is limited by complex error distributions. To address this challenge, we propose Diff-GNSS, a coarse-to-fine GNSS measurement (pseudorange) error estimation framework that leverages a conditional diffusion model to capture such complex distributions. Firstly, a Mamba-based module performs coarse estimation to provide an initial prediction with appropriate scale and trend. Then, a conditional denoising diffusion layer refines the estimate, enabling fine-grained modeling of pseudorange errors. To suppress uncontrolled generative diversity and achieve controllable synthesis, three key features related to GNSS measurement quality are used as conditions to precisely guide the reverse denoising process. We further incorporate per-satellite uncertainty modeling within the diffusion stage to assess the reliability of the predicted errors. We have collected and publicly released a real-world dataset covering various scenes. Experiments on public and self-collected datasets show that DiffGNSS consistently outperforms state-of-the-art baselines across multiple metrics. To the best of our knowledge, this is the first application of diffusion models to pseudorange error estimation. The proposed diffusion-based refinement module is plug-and-play and can be readily integrated into existing networks to markedly improve estimation accuracy.

## 📝 요약

Diff-GNSS는 도시 환경에서 GNSS의 위치 정확도를 저하시키는 다중 경로 및 비가시선 수신 문제를 해결하기 위해 제안된 프레임워크입니다. 이 연구는 조건부 확산 모델을 활용하여 복잡한 오차 분포를 효과적으로 모델링합니다. 먼저, Mamba 기반 모듈로 초기 예측을 수행한 후, 조건부 디노이징 확산 레이어로 세밀한 오차 모델링을 진행합니다. GNSS 측정 품질과 관련된 세 가지 주요 특징을 조건으로 사용하여 예측 오차의 신뢰성을 평가하고, 다양한 데이터셋 실험을 통해 기존 방법들보다 우수한 성능을 입증했습니다. 이 연구는 확산 모델을 위성 측정 오차 추정에 처음으로 적용한 사례로, 기존 네트워크에 쉽게 통합할 수 있는 모듈을 제공합니다.

## 🎯 주요 포인트

- 1. GNSS는 도시 환경에서 신뢰할 수 있는 위치 측정을 위해 필수적이지만, 다중 경로 및 비직접 경로 수신으로 인해 큰 측정 오류가 발생할 수 있습니다.
- 2. Diff-GNSS는 조건부 확산 모델을 활용하여 복잡한 오류 분포를 포착하는 GNSS 측정 오류 추정 프레임워크입니다.
- 3. Mamba 기반 모듈을 통해 초기 예측을 수행한 후, 조건부 디노이징 확산 레이어가 세밀한 오류 모델링을 가능하게 합니다.
- 4. GNSS 측정 품질과 관련된 세 가지 주요 특징을 조건으로 사용하여 제어 가능한 합성을 달성합니다.
- 5. Diff-GNSS는 여러 데이터셋 실험에서 최신 기법보다 우수한 성능을 보이며, 확산 모델을 오차 추정에 적용한 최초의 사례입니다.


---

*Generated on 2025-09-24 04:50:09*