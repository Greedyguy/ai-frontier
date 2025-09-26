---
keywords:
  - Phase Retrieval
  - Diffusion Model
  - Inline Holography
  - Nonlinear Inverse Problems
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.12728
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:24:45.359220",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Phase Retrieval",
    "Diffusion Model",
    "Inline Holography",
    "Nonlinear Inverse Problems"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Phase Retrieval": 0.75,
    "Diffusion Model": 0.78,
    "Inline Holography": 0.72,
    "Nonlinear Inverse Problems": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Phase Retrieval",
        "canonical": "Phase Retrieval",
        "aliases": [
          "Phase Reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "Phase retrieval is a specialized topic in computational imaging, crucial for linking discussions on inverse problems and holography.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Diffusion Model",
        "canonical": "Diffusion Model",
        "aliases": [
          "Diffusion Process"
        ],
        "category": "broad_technical",
        "rationale": "Diffusion models are increasingly relevant in machine learning, providing a bridge to discussions on generative models.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Inline Holography",
        "canonical": "Inline Holography",
        "aliases": [
          "Holographic Imaging"
        ],
        "category": "unique_technical",
        "rationale": "Inline holography is a distinct technique in imaging, offering specific connections to coherent imaging discussions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Nonlinear Inverse Problems",
        "canonical": "Nonlinear Inverse Problems",
        "aliases": [
          "Nonlinear Inversion"
        ],
        "category": "specific_connectable",
        "rationale": "Nonlinear inverse problems are central to computational imaging, linking to broader discussions on mathematical modeling.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
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
      "candidate_surface": "Phase Retrieval",
      "resolved_canonical": "Phase Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Diffusion Model",
      "resolved_canonical": "Diffusion Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Inline Holography",
      "resolved_canonical": "Inline Holography",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Nonlinear Inverse Problems",
      "resolved_canonical": "Nonlinear Inverse Problems",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Generalizable Holographic Reconstruction via Amplitude-Only Diffusion Priors

**Korean Title:** 일반화 가능한 홀로그램 재구성을 위한 진폭-전용 확산 우선순위

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.12728.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.12728](https://arxiv.org/abs/2509.12728)

## 🔗 유사한 논문
- [[2025-09-22/G2D2_ Gradient-Guided Discrete Diffusion for Inverse Problem Solving_20250922|G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving]] (84.6% similar)
- [[2025-09-17/Deconstructing Intraocular Pressure_ A Non-invasive Multi-Stage Probabilistic Inverse Framework_20250917|Deconstructing Intraocular Pressure: A Non-invasive Multi-Stage Probabilistic Inverse Framework]] (83.4% similar)
- [[2025-09-18/Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (82.4% similar)
- [[2025-09-22/Kuramoto Orientation Diffusion Models_20250922|Kuramoto Orientation Diffusion Models]] (82.2% similar)
- [[2025-09-22/Recovering Parametric Scenes from Very Few Time-of-Flight Pixels_20250922|Recovering Parametric Scenes from Very Few Time-of-Flight Pixels]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Diffusion Model|Diffusion Model]]
**🔗 Specific Connectable**: [[keywords/Nonlinear Inverse Problems|Nonlinear Inverse Problems]]
**⚡ Unique Technical**: [[keywords/Phase Retrieval|Phase Retrieval]], [[keywords/Inline Holography|Inline Holography]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12728v2 Announce Type: replace-cross 
Abstract: Phase retrieval in inline holography is a fundamental yet ill-posed inverse problem due to the nonlinear coupling between amplitude and phase in coherent imaging. We present a novel off-the-shelf solution that leverages a diffusion model trained solely on object amplitude to recover both amplitude and phase from diffraction intensities. Using a predictor-corrector sampling framework with separate likelihood gradients for amplitude and phase, our method enables complex field reconstruction without requiring ground-truth phase data for training. We validate the proposed approach through extensive simulations and experiments, demonstrating robust generalization across diverse object shapes, imaging system configurations, and modalities, including lensless setups. Notably, a diffusion prior trained on simple amplitude data (e.g., polystyrene beads) successfully reconstructs complex biological tissue structures, highlighting the method's adaptability. This framework provides a cost-effective, generalizable solution for nonlinear inverse problems in computational imaging, and establishes a foundation for broader coherent imaging applications beyond holography.

## 🔍 Abstract (한글 번역)

arXiv:2509.12728v2 발표 유형: 교차 대체  
초록: 인라인 홀로그래피에서의 위상 복원은 코히어런트 이미징에서 진폭과 위상 간의 비선형 결합으로 인해 근본적으로 잘못된 역문제입니다. 우리는 회절 강도로부터 진폭과 위상을 모두 복원하기 위해 객체 진폭에만 훈련된 확산 모델을 활용하는 새로운 기성 솔루션을 제시합니다. 진폭과 위상에 대한 개별적인 가능도 기울기를 사용하는 예측-보정 샘플링 프레임워크를 통해, 우리의 방법은 훈련을 위한 진실 위상 데이터 없이 복잡한 필드 복원을 가능하게 합니다. 우리는 다양한 객체 모양, 이미징 시스템 구성 및 모달리티(렌즈 없는 설정 포함)에 걸쳐 강력한 일반화를 입증하는 광범위한 시뮬레이션 및 실험을 통해 제안된 접근 방식을 검증합니다. 특히, 단순한 진폭 데이터(예: 폴리스티렌 비드)에 대해 훈련된 확산 사전이 복잡한 생물학적 조직 구조를 성공적으로 재구성하여 이 방법의 적응성을 강조합니다. 이 프레임워크는 계산 이미징의 비선형 역문제에 대한 비용 효율적이고 일반화 가능한 솔루션을 제공하며, 홀로그래피를 넘어선 더 넓은 코히어런트 이미징 응용을 위한 기초를 마련합니다.

## 📝 요약

이 논문은 비선형 결합으로 인해 잘못된 문제인 인라인 홀로그래피에서의 위상 복원 문제를 다룹니다. 저자들은 객체의 진폭만을 학습한 확산 모델을 활용하여 회절 강도로부터 진폭과 위상을 모두 복원하는 새로운 방법을 제안합니다. 이 방법은 진폭과 위상에 대한 개별적인 가능도 기울기를 사용하여 복잡한 필드 재구성을 가능하게 하며, 학습 시 실제 위상 데이터가 필요하지 않습니다. 다양한 객체 형태와 이미징 시스템 구성에서의 강력한 일반화 능력을 시뮬레이션과 실험을 통해 검증하였으며, 단순한 진폭 데이터로 학습된 확산 사전이 복잡한 생물학적 조직 구조를 성공적으로 재구성함을 보여줍니다. 이 프레임워크는 계산 이미징에서 비선형 역문제를 해결하는 비용 효율적이고 일반화 가능한 솔루션을 제공하며, 홀로그래피를 넘어선 광범위한 응용 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 본 연구는 비선형 결합 문제인 인라인 홀로그래피의 위상 복원을 위한 새로운 솔루션을 제안합니다.
- 2. 제안된 방법은 객체의 진폭만을 학습한 확산 모델을 활용하여 회절 강도로부터 진폭과 위상을 복원합니다.
- 3. 예측-보정 샘플링 프레임워크를 통해 진폭과 위상에 대한 개별적인 가능도 기울기를 사용하여 복잡한 필드 재구성을 가능하게 합니다.
- 4. 제안된 접근법은 다양한 객체 형태, 이미징 시스템 구성 및 모달리티에 걸쳐 강력한 일반화 능력을 입증합니다.
- 5. 간단한 진폭 데이터로 학습된 확산 사전이 복잡한 생물학적 조직 구조를 성공적으로 재구성하여 방법의 적응성을 강조합니다.


---

*Generated on 2025-09-23 11:24:45*