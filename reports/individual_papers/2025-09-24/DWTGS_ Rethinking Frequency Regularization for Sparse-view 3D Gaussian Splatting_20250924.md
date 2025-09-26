<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:31:45.335517",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sparse-view 3D Gaussian Splatting",
    "Frequency Regularization",
    "Wavelet Transform",
    "Self-supervised Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sparse-view 3D Gaussian Splatting": 0.78,
    "Frequency Regularization": 0.8,
    "Wavelet Transform": 0.79,
    "Self-supervised Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sparse-view 3D Gaussian Splatting",
        "canonical": "Sparse-view 3D Gaussian Splatting",
        "aliases": [
          "3DGS"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus and represents a specific technique in 3D reconstruction.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Frequency Regularization",
        "canonical": "Frequency Regularization",
        "aliases": [
          "Frequency Control"
        ],
        "category": "specific_connectable",
        "rationale": "Frequency regularization is a key concept in the paper, linking to broader discussions on signal processing.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Wavelet-space losses",
        "canonical": "Wavelet Transform",
        "aliases": [
          "Wavelet Losses"
        ],
        "category": "specific_connectable",
        "rationale": "Wavelet transforms are a specific method used for frequency analysis, connecting to broader mathematical frameworks.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.76,
        "link_intent_score": 0.79
      },
      {
        "surface": "Self-supervised manner",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Self-supervision"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised learning is a growing area of interest, providing a link to machine learning techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "high-frequency",
      "low-frequency",
      "Fourier-based"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Sparse-view 3D Gaussian Splatting",
      "resolved_canonical": "Sparse-view 3D Gaussian Splatting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Frequency Regularization",
      "resolved_canonical": "Frequency Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Wavelet-space losses",
      "resolved_canonical": "Wavelet Transform",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.76,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Self-supervised manner",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# DWTGS: Rethinking Frequency Regularization for Sparse-view 3D Gaussian Splatting

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2507.15690.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2507.15690](https://arxiv.org/abs/2507.15690)

## 🔗 유사한 논문
- [[2025-09-24/WaveletGaussian_ Wavelet-domain Diffusion for Sparse-view 3D Gaussian Object Reconstruction_20250924|WaveletGaussian: Wavelet-domain Diffusion for Sparse-view 3D Gaussian Object Reconstruction]] (87.3% similar)
- [[2025-09-23/AD-GS_ Alternating Densification for Sparse-Input 3D Gaussian Splatting_20250923|AD-GS: Alternating Densification for Sparse-Input 3D Gaussian Splatting]] (86.1% similar)
- [[2025-09-23/Accurate and Complete Surface Reconstruction from 3D Gaussians via Direct SDF Learning_20250923|Accurate and Complete Surface Reconstruction from 3D Gaussians via Direct SDF Learning]] (86.0% similar)
- [[2025-09-24/Gaussian Herding across Pens_ An Optimal Transport Perspective on Global Gaussian Reduction for 3DGS_20250924|Gaussian Herding across Pens: An Optimal Transport Perspective on Global Gaussian Reduction for 3DGS]] (84.9% similar)
- [[2025-09-24/VolSplat_ Rethinking Feed-Forward 3D Gaussian Splatting with Voxel-Aligned Prediction_20250924|VolSplat: Rethinking Feed-Forward 3D Gaussian Splatting with Voxel-Aligned Prediction]] (84.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Frequency Regularization|Frequency Regularization]], [[keywords/Wavelet Transform|Wavelet Transform]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Sparse-view 3D Gaussian Splatting|Sparse-view 3D Gaussian Splatting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.15690v2 Announce Type: replace 
Abstract: Sparse-view 3D Gaussian Splatting (3DGS) presents significant challenges in reconstructing high-quality novel views, as it often overfits to the widely-varying high-frequency (HF) details of the sparse training views. While frequency regularization can be a promising approach, its typical reliance on Fourier transforms causes difficult parameter tuning and biases towards detrimental HF learning. We propose DWTGS, a framework that rethinks frequency regularization by leveraging wavelet-space losses that provide additional spatial supervision. Specifically, we supervise only the low-frequency (LF) LL subbands at multiple DWT levels, while enforcing sparsity on the HF HH subband in a self-supervised manner. Experiments across benchmarks show that DWTGS consistently outperforms Fourier-based counterparts, as this LF-centric strategy improves generalization and reduces HF hallucinations.

## 📝 요약

Sparse-view 3D Gaussian Splatting(3DGS)의 주요 문제는 고주파(HF) 세부사항에 과적합되어 새로운 시각을 고품질로 재구성하기 어렵다는 점입니다. 기존의 주파수 정규화는 Fourier 변환에 의존하여 매개변수 조정이 어렵고 HF 학습에 편향될 수 있습니다. 이를 해결하기 위해 우리는 DWTGS라는 프레임워크를 제안합니다. 이 방법은 파형 변환(DWT)을 활용하여 공간적 감독을 제공하며, 저주파(LF) LL 서브밴드만 감독하고 HF HH 서브밴드에는 자가 감독을 통해 희소성을 부여합니다. 실험 결과, DWTGS는 Fourier 기반 방법보다 일관되게 우수한 성능을 보였으며, LF 중심 전략이 일반화 성능을 향상시키고 HF 환각을 줄이는 데 효과적임을 확인했습니다.

## 🎯 주요 포인트

- 1. Sparse-view 3D Gaussian Splatting은 고주파 세부사항에 과적합되어 새로운 시각을 재구성하는 데 어려움을 겪습니다.
- 2. 기존의 주파수 정규화는 푸리에 변환에 의존하여 매개변수 조정이 어렵고 고주파 학습에 편향될 수 있습니다.
- 3. DWTGS는 웨이블릿 공간 손실을 활용하여 주파수 정규화를 재고하는 프레임워크로, 추가적인 공간적 감독을 제공합니다.
- 4. DWTGS는 저주파 LL 서브밴드만 감독하고, 고주파 HH 서브밴드에는 자기지도 학습으로 희소성을 부과합니다.
- 5. 실험 결과, DWTGS는 푸리에 기반 방법보다 일관되게 우수한 성능을 보이며, 일반화 능력을 향상시키고 고주파 환각을 줄입니다.


---

*Generated on 2025-09-24 16:31:45*