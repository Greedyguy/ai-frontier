<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:08:29.439304",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Diffusion-based Inverse Problem Solvers",
    "Compressed-Sensing MRI Reconstruction",
    "Coil Sensitivity Maps"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.8,
    "Diffusion-based Inverse Problem Solvers": 0.7,
    "Compressed-Sensing MRI Reconstruction": 0.75,
    "Coil Sensitivity Maps": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-supervision"
        ],
        "category": "specific_connectable",
        "rationale": "Links to existing work on self-supervised techniques, connecting to broader machine learning contexts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Diffusion-based inverse problem solvers",
        "canonical": "Diffusion-based Inverse Problem Solvers",
        "aliases": [
          "DIS"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specialized approach in MRI reconstruction, offering unique insights into diffusion models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Compressed-sensing parallel MRI reconstruction",
        "canonical": "Compressed-Sensing MRI Reconstruction",
        "aliases": [
          "CS-MRI"
        ],
        "category": "unique_technical",
        "rationale": "A specific application of compressed sensing in MRI, relevant for connecting to medical imaging research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Coil sensitivity maps",
        "canonical": "Coil Sensitivity Maps",
        "aliases": [
          "CSMs"
        ],
        "category": "unique_technical",
        "rationale": "Essential for understanding the technical challenges in MRI, linking to hardware-specific studies.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
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
      "candidate_surface": "Self-supervised learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Diffusion-based inverse problem solvers",
      "resolved_canonical": "Diffusion-based Inverse Problem Solvers",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Compressed-sensing parallel MRI reconstruction",
      "resolved_canonical": "Compressed-Sensing MRI Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Coil sensitivity maps",
      "resolved_canonical": "Coil Sensitivity Maps",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Measurement Score-Based MRI Reconstruction with Automatic Coil Sensitivity Estimation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18402.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18402](https://arxiv.org/abs/2509.18402)

## 🔗 유사한 논문
- [[2025-09-19/DICE_ Diffusion Consensus Equilibrium for Sparse-view CT Reconstruction_20250919|DICE: Diffusion Consensus Equilibrium for Sparse-view CT Reconstruction]] (84.1% similar)
- [[2025-09-22/SLaM-DiMM_ Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI_20250922|SLaM-DiMM: Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI]] (83.5% similar)
- [[2025-09-23/A Novel Metric for Detecting Memorization in Generative Models for Brain MRI Synthesis_20250923|A Novel Metric for Detecting Memorization in Generative Models for Brain MRI Synthesis]] (82.0% similar)
- [[2025-09-22/PRISM_ Probabilistic and Robust Inverse Solver with Measurement-Conditioned Diffusion Prior for Blind Inverse Problems_20250922|PRISM: Probabilistic and Robust Inverse Solver with Measurement-Conditioned Diffusion Prior for Blind Inverse Problems]] (81.9% similar)
- [[2025-09-18/Scattering approach to diffusion quantifies axonal damage in brain injury_20250918|Scattering approach to diffusion quantifies axonal damage in brain injury]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Diffusion-based Inverse Problem Solvers|Diffusion-based Inverse Problem Solvers]], [[keywords/Compressed-Sensing MRI Reconstruction|Compressed-Sensing MRI Reconstruction]], [[keywords/Coil Sensitivity Maps|Coil Sensitivity Maps]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18402v1 Announce Type: cross 
Abstract: Diffusion-based inverse problem solvers (DIS) have recently shown outstanding performance in compressed-sensing parallel MRI reconstruction by combining diffusion priors with physical measurement models. However, they typically rely on pre-calibrated coil sensitivity maps (CSMs) and ground truth images, making them often impractical: CSMs are difficult to estimate accurately under heavy undersampling and ground-truth images are often unavailable. We propose Calibration-free Measurement Score-based diffusion Model (C-MSM), a new method that eliminates these dependencies by jointly performing automatic CSM estimation and self-supervised learning of measurement scores directly from k-space data. C-MSM reconstructs images by approximating the full posterior distribution through stochastic sampling over partial measurement posterior scores, while simultaneously estimating CSMs. Experiments on the multi-coil brain fastMRI dataset show that C-MSM achieves reconstruction performance close to DIS with clean diffusion priors -- even without access to clean training data and pre-calibrated CSMs.

## 📝 요약

이 논문은 확산 기반 역문제 해결법(DIS)의 한계를 극복하기 위해 새로운 방법인 C-MSM을 제안합니다. 기존 DIS는 사전 보정된 코일 감도 맵(CSM)과 실제 이미지에 의존하지만, C-MSM은 k-공간 데이터로부터 자동으로 CSM을 추정하고 측정 점수를 자기 지도 학습하여 이러한 의존성을 제거합니다. C-MSM은 부분 측정 후방 점수에 대한 확률적 샘플링을 통해 전체 후방 분포를 근사하며 이미지를 재구성하고, 동시에 CSM을 추정합니다. 실험 결과, C-MSM은 깨끗한 훈련 데이터와 사전 보정된 CSM 없이도 기존 DIS와 유사한 수준의 재구성 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 확산 기반 역문제 해결기(Diffusion-based inverse problem solvers, DIS)는 압축 센싱 병렬 MRI 재구성에서 뛰어난 성능을 보였으나, 사전 보정된 코일 감도 맵(CSM)과 실제 이미지에 의존하여 실용성이 떨어진다.
- 2. CSM은 심한 언더샘플링 상황에서 정확하게 추정하기 어려우며, 실제 이미지는 종종 구할 수 없다.
- 3. 제안된 C-MSM(Calibration-free Measurement Score-based diffusion Model)은 k-공간 데이터로부터 자동 CSM 추정과 측정 점수의 자가 지도 학습을 통해 이러한 의존성을 제거한다.
- 4. C-MSM은 부분 측정 후방 점수에 대한 확률적 샘플링을 통해 전체 후방 분포를 근사하면서 이미지를 재구성하고 동시에 CSM을 추정한다.
- 5. 실험 결과, C-MSM은 깨끗한 학습 데이터와 사전 보정된 CSM 없이도 다중 코일 뇌 fastMRI 데이터셋에서 DIS와 유사한 재구성 성능을 달성했다.


---

*Generated on 2025-09-24 15:08:29*