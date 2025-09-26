---
keywords:
  - Hyperspectral Image Reconstruction
  - Mixture-of-Codebooks
  - Attention Mechanism
  - Test-time Adaptation
  - Photometric Consistency
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2507.09885
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:38:26.463992",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hyperspectral Image Reconstruction",
    "Mixture-of-Codebooks",
    "Attention Mechanism",
    "Test-time Adaptation",
    "Photometric Consistency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hyperspectral Image Reconstruction": 0.8,
    "Mixture-of-Codebooks": 0.75,
    "Attention Mechanism": 0.78,
    "Test-time Adaptation": 0.77,
    "Photometric Consistency": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hyperspectral Image Reconstruction",
        "canonical": "Hyperspectral Image Reconstruction",
        "aliases": [
          "HSI Reconstruction"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on reconstructing hyperspectral images from RGB inputs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Mixture-of-Codebooks",
        "canonical": "Mixture-of-Codebooks",
        "aliases": [
          "MoC"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework proposed in the paper, crucial for understanding the method's innovation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      },
      {
        "surface": "Grayscale-aware Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "GANet"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specific type of attention mechanism that enhances connectivity with existing attention-based methods.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Test-time Adaptation",
        "canonical": "Test-time Adaptation",
        "aliases": [
          "TTA"
        ],
        "category": "unique_technical",
        "rationale": "This technique is highlighted for improving efficiency and robustness, making it a key concept in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Photometric Consistency",
        "canonical": "Photometric Consistency",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is essential for understanding the method's approach to aligning RGB features with spectral priors.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "RGB inputs",
      "large attention networks",
      "state-of-the-art accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Hyperspectral Image Reconstruction",
      "resolved_canonical": "Hyperspectral Image Reconstruction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Mixture-of-Codebooks",
      "resolved_canonical": "Mixture-of-Codebooks",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Grayscale-aware Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Test-time Adaptation",
      "resolved_canonical": "Test-time Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Photometric Consistency",
      "resolved_canonical": "Photometric Consistency",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# MCGA: Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention

**Korean Title:** MCGA: 그레이스케일 인식 주의 메커니즘을 통한 코드북 혼합 기반의 고해상도 스펙트럼 재구성

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2507.09885.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2507.09885](https://arxiv.org/abs/2507.09885)

## 🔗 유사한 논문
- [[2025-09-22/USCTNet_ A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction_20250922|USCTNet: A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction]] (83.5% similar)
- [[2025-09-18/MCGS-SLAM_ A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (82.5% similar)
- [[2025-09-19/HPGN_ Hybrid Priors-Guided Network for Compressed Low-Light Image Enhancement_20250919|HPGN: Hybrid Priors-Guided Network for Compressed Low-Light Image Enhancement]] (82.0% similar)
- [[2025-09-22/MS-GS_ Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild_20250922|MS-GS: Multi-Appearance Sparse-View 3D Gaussian Splatting in the Wild]] (80.9% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Hyperspectral Image Reconstruction|Hyperspectral Image Reconstruction]], [[keywords/Mixture-of-Codebooks|Mixture-of-Codebooks]], [[keywords/Test-time Adaptation|Test-time Adaptation]], [[keywords/Photometric Consistency|Photometric Consistency]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.09885v2 Announce Type: replace 
Abstract: Reconstructing hyperspectral images (HSIs) from RGB inputs provides a cost-effective alternative to hyperspectral cameras, but reconstructing high-dimensional spectra from three channels is inherently ill-posed. Existing methods typically directly regress RGB-to-HSI mappings using large attention networks, which are computationally expensive and handle ill-posedness only implicitly. We propose MCGA, a Mixture-of-Codebooks with Grayscale-aware Attention framework that explicitly addresses these challenges using spectral priors and photometric consistency. MCGA first learns transferable spectral priors via a mixture-of-codebooks (MoC) from heterogeneous HSI datasets, then aligns RGB features with these priors through grayscale-aware photometric attention (GANet). Efficiency and robustness are further improved via top-K attention design and test-time adaptation (TTA). Experiments on benchmarks and real-world data demonstrate the state-of-the-art accuracy, strong cross-dataset generalization, and 4-5x faster inference. Codes will be available once acceptance at https://github.com/Fibonaccirabbit/MCGA.

## 🔍 Abstract (한글 번역)

arXiv:2507.09885v2 발표 유형: 교체  
초록: RGB 입력으로부터 고광대역 이미지를 재구성하는 것은 고광대역 카메라에 대한 비용 효율적인 대안을 제공하지만, 세 개의 채널로부터 고차원의 스펙트럼을 재구성하는 것은 본질적으로 잘못된 문제입니다. 기존 방법들은 일반적으로 대형 주의 네트워크를 사용하여 RGB에서 HSI로의 매핑을 직접 회귀하는데, 이는 계산 비용이 많이 들고 잘못된 문제를 암묵적으로만 처리합니다. 우리는 이러한 문제를 스펙트럼 사전과 광도 일관성을 사용하여 명시적으로 해결하는 그레이스케일 인식 주의 프레임워크인 MCGA(Mixture-of-Codebooks with Grayscale-aware Attention)를 제안합니다. MCGA는 먼저 이질적인 HSI 데이터셋으로부터 코드북 혼합(MoC)을 통해 전이 가능한 스펙트럼 사전을 학습하고, 그런 다음 그레이스케일 인식 광도 주의(GANet)를 통해 RGB 특징을 이 사전과 정렬합니다. 효율성과 견고성은 top-K 주의 설계와 테스트 시간 적응(TTA)을 통해 더욱 향상됩니다. 벤치마크 및 실제 데이터에 대한 실험은 최첨단 정확도, 강력한 데이터셋 간 일반화 및 4-5배 빠른 추론을 입증합니다. 코드는 승인 후 https://github.com/Fibonaccirabbit/MCGA에서 제공될 예정입니다.

## 📝 요약

이 논문은 RGB 입력으로부터 고차원 스펙트럼을 재구성하는 문제를 다룹니다. 기존 방법들은 주로 대규모 주의 메커니즘을 사용하여 RGB에서 HSI로의 매핑을 직접 회귀하지만, 이는 계산 비용이 크고 문제의 본질적인 불완전성을 명시적으로 해결하지 않습니다. 이를 해결하기 위해, 저자들은 MCGA라는 새로운 프레임워크를 제안합니다. 이 프레임워크는 이질적인 HSI 데이터셋에서 혼합 코드북을 통해 전이 가능한 스펙트럼 사전 지식을 학습하고, 그레이스케일 인식 포토메트릭 주의를 통해 RGB 특징을 정렬합니다. 또한, 효율성과 강건성을 향상시키기 위해 top-K 주의 설계와 테스트 시점 적응을 도입했습니다. 실험 결과, 제안된 방법은 최신 기술 수준의 정확도와 강력한 데이터셋 간 일반화 능력을 보여주며, 추론 속도도 4-5배 빠릅니다.

## 🎯 주요 포인트

- 1. MCGA는 RGB 입력에서 고차원 스펙트럼을 재구성하는 문제를 해결하기 위해 혼합 코드북과 그레이스케일 인식 주의 메커니즘을 사용합니다.
- 2. MCGA는 다양한 HSI 데이터셋에서 혼합 코드북을 통해 전이 가능한 스펙트럼 사전 지식을 학습하고, 이를 RGB 특징과 정렬합니다.
- 3. 효율성과 강건성을 개선하기 위해 top-K 주의 설계와 테스트 시 적응(TTA)을 도입하였습니다.
- 4. 벤치마크와 실제 데이터 실험에서 최첨단 정확도와 강력한 데이터셋 간 일반화 능력을 보여주며, 4-5배 빠른 추론 속도를 달성했습니다.


---

*Generated on 2025-09-23 12:38:26*