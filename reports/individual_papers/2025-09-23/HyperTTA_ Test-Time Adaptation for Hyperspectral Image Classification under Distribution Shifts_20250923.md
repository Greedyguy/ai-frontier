---
keywords:
  - Hyperspectral Image Classification
  - Transformer
  - Spectral-Spatial Transformer Classifier
  - Test-Time Adaptation
  - Confidence-aware Entropy-minimized LayerNorm Adapter
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.08436
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:31:45.933509",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hyperspectral Image Classification",
    "Transformer",
    "Spectral-Spatial Transformer Classifier",
    "Test-Time Adaptation",
    "Confidence-aware Entropy-minimized LayerNorm Adapter"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hyperspectral Image Classification": 0.78,
    "Transformer": 0.85,
    "Spectral-Spatial Transformer Classifier": 0.72,
    "Test-Time Adaptation": 0.8,
    "Confidence-aware Entropy-minimized LayerNorm Adapter": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hyperspectral Image Classification",
        "canonical": "Hyperspectral Image Classification",
        "aliases": [
          "HSI Classification"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area that connects to both hyperspectral imaging and classification techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model architecture that connects to various deep learning applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Spectral--Spatial Transformer Classifier",
        "canonical": "Spectral-Spatial Transformer Classifier",
        "aliases": [
          "SSTC"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel model introduced in the paper, combining spectral and spatial analysis for classification.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "Test-Time Adaptation",
        "canonical": "Test-Time Adaptation",
        "aliases": [
          "TTA"
        ],
        "category": "specific_connectable",
        "rationale": "Test-time adaptation is a technique relevant to improving model robustness under distribution shifts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Confidence-aware Entropy-minimized LayerNorm Adapter",
        "canonical": "Confidence-aware Entropy-minimized LayerNorm Adapter",
        "aliases": [
          "CELA"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific adaptation strategy introduced in the paper, enhancing model robustness.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "degradation",
      "benchmark",
      "dataset"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Hyperspectral Image Classification",
      "resolved_canonical": "Hyperspectral Image Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Spectral--Spatial Transformer Classifier",
      "resolved_canonical": "Spectral-Spatial Transformer Classifier",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Test-Time Adaptation",
      "resolved_canonical": "Test-Time Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Confidence-aware Entropy-minimized LayerNorm Adapter",
      "resolved_canonical": "Confidence-aware Entropy-minimized LayerNorm Adapter",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# HyperTTA: Test-Time Adaptation for Hyperspectral Image Classification under Distribution Shifts

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.08436.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.08436](https://arxiv.org/abs/2509.08436)

## 🔗 유사한 논문
- [[2025-09-23/A Cross-Hierarchical Multi-Feature Fusion Network Based on Multiscale Encoder-Decoder for Hyperspectral Change Detection_20250923|A Cross-Hierarchical Multi-Feature Fusion Network Based on Multiscale Encoder-Decoder for Hyperspectral Change Detection]] (82.7% similar)
- [[2025-09-22/CLIPTTA_ Robust Contrastive Vision-Language Test-Time Adaptation_20250922|CLIPTTA: Robust Contrastive Vision-Language Test-Time Adaptation]] (81.9% similar)
- [[2025-09-23/Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding_20250923|Degradation-Aware All-in-One Image Restoration via Latent Prior Encoding]] (81.8% similar)
- [[2025-09-23/MTM_ A Multi-Scale Token Mixing Transformer for Irregular Multivariate Time Series Classification_20250923|MTM: A Multi-Scale Token Mixing Transformer for Irregular Multivariate Time Series Classification]] (81.8% similar)
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Test-Time Adaptation|Test-Time Adaptation]]
**⚡ Unique Technical**: [[keywords/Hyperspectral Image Classification|Hyperspectral Image Classification]], [[keywords/Spectral-Spatial Transformer Classifier|Spectral-Spatial Transformer Classifier]], [[keywords/Confidence-aware Entropy-minimized LayerNorm Adapter|Confidence-aware Entropy-minimized LayerNorm Adapter]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.08436v2 Announce Type: replace 
Abstract: Hyperspectral image (HSI) classification models are highly sensitive to distribution shifts caused by real-world degradations such as noise, blur, compression, and atmospheric effects. To address this challenge, we propose HyperTTA (Test-Time Adaptable Transformer for Hyperspectral Degradation), a unified framework that enhances model robustness under diverse degradation conditions. First, we construct a multi-degradation hyperspectral benchmark that systematically simulates nine representative degradations, enabling comprehensive evaluation of robust classification. Based on this benchmark, we develop a Spectral--Spatial Transformer Classifier (SSTC) with a multi-level receptive field mechanism and label smoothing regularization to capture multi-scale spatial context and improve generalization. Furthermore, we introduce a lightweight test-time adaptation strategy, the Confidence-aware Entropy-minimized LayerNorm Adapter (CELA), which dynamically updates only the affine parameters of LayerNorm layers by minimizing prediction entropy on high-confidence unlabeled target samples. This strategy ensures reliable adaptation without access to source data or target labels. Experiments on two benchmark datasets demonstrate that HyperTTA outperforms state-of-the-art baselines across a wide range of degradation scenarios. Code will be made available publicly.

## 📝 요약

이 논문은 실제 환경에서 발생하는 다양한 열화 조건(노이즈, 블러, 압축, 대기 효과 등)에 민감한 고광대역 이미지(HSI) 분류 모델의 강건성을 향상시키기 위해 HyperTTA라는 통합 프레임워크를 제안합니다. 이를 위해 아홉 가지 대표적인 열화를 체계적으로 시뮬레이션하는 다중 열화 고광대역 벤치마크를 구축하여 포괄적인 평가를 가능하게 합니다. 또한, 다중 수준 수용 필드 메커니즘과 레이블 스무딩 정규화를 사용하는 Spectral-Spatial Transformer Classifier(SSTC)를 개발하여 다중 스케일 공간 컨텍스트를 포착하고 일반화를 개선합니다. 더불어, Confidence-aware Entropy-minimized LayerNorm Adapter(CELA)라는 경량의 테스트 시 적응 전략을 도입하여, 소스 데이터나 타겟 레이블 없이도 신뢰성 있는 적응을 보장합니다. 실험 결과, HyperTTA는 다양한 열화 시나리오에서 최신 기법들을 능가하는 성능을 보였습니다. 코드는 공개될 예정입니다.

## 🎯 주요 포인트

- 1. HyperTTA는 다양한 열화 조건에서 모델의 강인성을 향상시키기 위한 통합 프레임워크로 제안되었습니다.
- 2. 다중 열화 하이퍼스펙트럼 벤치마크를 구축하여 9개의 대표적인 열화를 체계적으로 시뮬레이션하고, 강인한 분류의 포괄적인 평가를 가능하게 합니다.
- 3. Spectral--Spatial Transformer Classifier (SSTC)는 다중 수준 수용 영역 메커니즘과 라벨 스무딩 정규화를 통해 다중 스케일 공간 컨텍스트를 포착하고 일반화를 개선합니다.
- 4. Confidence-aware Entropy-minimized LayerNorm Adapter (CELA)는 고신뢰도 비라벨 대상 샘플의 예측 엔트로피를 최소화하여 LayerNorm 계층의 어파인 매개변수를 동적으로 업데이트하는 경량 테스트 시간 적응 전략입니다.
- 5. HyperTTA는 두 개의 벤치마크 데이터셋 실험에서 다양한 열화 시나리오에 걸쳐 최신 기준을 능가하는 성능을 보였습니다.


---

*Generated on 2025-09-24 05:31:45*