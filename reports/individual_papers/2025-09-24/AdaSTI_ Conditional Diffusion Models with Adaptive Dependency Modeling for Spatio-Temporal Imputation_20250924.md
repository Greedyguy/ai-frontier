<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:38:01.919116",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Spatio-Temporal Imputation",
    "BiS4PI Network",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Models": 0.78,
    "Spatio-Temporal Imputation": 0.82,
    "BiS4PI Network": 0.75,
    "Attention Mechanism": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Models",
        "canonical": "Diffusion Models",
        "aliases": [
          "Diffusion-based Methods"
        ],
        "category": "broad_technical",
        "rationale": "Diffusion models are increasingly used in machine learning tasks and can link to various related concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Spatio-Temporal Imputation",
        "canonical": "Spatio-Temporal Imputation",
        "aliases": [
          "Spatio-Temporal Data Imputation"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task addressed by the paper, connecting to broader themes in data imputation.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "BiS4PI network",
        "canonical": "BiS4PI Network",
        "aliases": [
          "Bi-directional S4 Model"
        ],
        "category": "unique_technical",
        "rationale": "A novel network architecture introduced in the paper, relevant for linking to network design topics.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Gated Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Gated Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are key in modern neural networks, and this variation can link to broader attention studies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "sensor malfunctions",
      "transmission failures"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Models",
      "resolved_canonical": "Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Spatio-Temporal Imputation",
      "resolved_canonical": "Spatio-Temporal Imputation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "BiS4PI network",
      "resolved_canonical": "BiS4PI Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Gated Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# AdaSTI: Conditional Diffusion Models with Adaptive Dependency Modeling for Spatio-Temporal Imputation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18144.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18144](https://arxiv.org/abs/2509.18144)

## 🔗 유사한 논문
- [[2025-09-23/MH-GIN_ Multi-scale Heterogeneous Graph-based Imputation Network for AIS Data (Extended Version)_20250923|MH-GIN: Multi-scale Heterogeneous Graph-based Imputation Network for AIS Data (Extended Version)]] (81.4% similar)
- [[2025-09-17/SpecDiff_ Accelerating Diffusion Model Inference with Self-Speculation_20250917|SpecDiff: Accelerating Diffusion Model Inference with Self-Speculation]] (81.3% similar)
- [[2025-09-23/Diff-GNSS_ Diffusion-based Pseudorange Error Estimation_20250923|Diff-GNSS: Diffusion-based Pseudorange Error Estimation]] (80.9% similar)
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (80.7% similar)
- [[2025-09-22/Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising_20250922|Blind-Spot Guided Diffusion for Self-supervised Real-World Denoising]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Models|Diffusion Models]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Spatio-Temporal Imputation|Spatio-Temporal Imputation]], [[keywords/BiS4PI Network|BiS4PI Network]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18144v1 Announce Type: cross 
Abstract: Spatio-temporal data abounds in domain like traffic and environmental monitoring. However, it often suffers from missing values due to sensor malfunctions, transmission failures, etc. Recent years have seen continued efforts to improve spatio-temporal data imputation performance. Recently diffusion models have outperformed other approaches in various tasks, including spatio-temporal imputation, showing competitive performance. Extracting and utilizing spatio-temporal dependencies as conditional information is vital in diffusion-based methods. However, previous methods introduce error accumulation in this process and ignore the variability of the dependencies in the noisy data at different diffusion steps. In this paper, we propose AdaSTI (Adaptive Dependency Model in Diffusion-based Spatio-Temporal Imputation), a novel spatio-temporal imputation approach based on conditional diffusion model. Inside AdaSTI, we propose a BiS4PI network based on a bi-directional S4 model for pre-imputation with the imputed result used to extract conditional information by our designed Spatio-Temporal Conditionalizer (STC)network. We also propose a Noise-Aware Spatio-Temporal (NAST) network with a gated attention mechanism to capture the variant dependencies across diffusion steps. Extensive experiments on three real-world datasets show that AdaSTI outperforms existing methods in all the settings, with up to 46.4% reduction in imputation error.

## 📝 요약

이 논문은 결측치가 발생하는 시공간 데이터의 보완을 위한 새로운 방법론인 AdaSTI를 제안합니다. AdaSTI는 조건부 확산 모델을 기반으로 하며, BiS4PI 네트워크와 Spatio-Temporal Conditionalizer(STC) 네트워크를 통해 사전 보완된 데이터를 조건부 정보로 활용합니다. 또한, Noise-Aware Spatio-Temporal(NAST) 네트워크를 도입하여 확산 단계별로 변하는 의존성을 효과적으로 포착합니다. 세 가지 실제 데이터셋을 활용한 실험 결과, AdaSTI는 기존 방법들보다 최대 46.4% 낮은 보완 오류율을 기록하며 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 스페이시오-템포럴 데이터는 센서 오작동 및 전송 실패로 인해 종종 결측값 문제를 겪습니다.
- 2. 최근 확산 모델은 다양한 작업에서 경쟁력 있는 성능을 보이며 스페이시오-템포럴 보완에서 다른 접근 방식을 능가했습니다.
- 3. AdaSTI는 조건부 확산 모델을 기반으로 한 새로운 스페이시오-템포럴 보완 접근법으로, BiS4PI 네트워크와 STC 네트워크를 활용합니다.
- 4. NAST 네트워크는 게이트 주의 메커니즘을 통해 확산 단계별로 다양한 종속성을 포착합니다.
- 5. 세 가지 실제 데이터셋에 대한 실험 결과, AdaSTI는 최대 46.4%의 보완 오류 감소를 달성하며 기존 방법을 능가했습니다.


---

*Generated on 2025-09-24 13:38:01*