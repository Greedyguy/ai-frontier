---
keywords:
  - Chromaticity-Intensity Decomposition
  - CASSI
  - Transformer
  - Hyperspectral Imaging
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16690
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:32:02.742910",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Chromaticity-Intensity Decomposition",
    "CASSI",
    "Transformer",
    "Hyperspectral Imaging"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Chromaticity-Intensity Decomposition": 0.8,
    "CASSI": 0.78,
    "Transformer": 0.82,
    "Hyperspectral Imaging": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Chromaticity-Intensity Decomposition",
        "canonical": "Chromaticity-Intensity Decomposition",
        "aliases": [
          "CID"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework proposed in the paper, crucial for understanding the decomposition of hyperspectral images.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Coded Aperture Snapshot Spectral Imaging",
        "canonical": "CASSI",
        "aliases": [
          "Coded Aperture Snapshot Spectral Imaging"
        ],
        "category": "unique_technical",
        "rationale": "CASSI is central to the paper's methodology and connects to broader imaging techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a key component in the proposed CIDNet, linking to a broad range of machine learning applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.82
      },
      {
        "surface": "Hyperspectral Images",
        "canonical": "Hyperspectral Imaging",
        "aliases": [
          "HSI"
        ],
        "category": "specific_connectable",
        "rationale": "Hyperspectral imaging is the primary focus of the paper, connecting to numerous imaging and analysis techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
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
      "candidate_surface": "Chromaticity-Intensity Decomposition",
      "resolved_canonical": "Chromaticity-Intensity Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Coded Aperture Snapshot Spectral Imaging",
      "resolved_canonical": "CASSI",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
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
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Hyperspectral Images",
      "resolved_canonical": "Hyperspectral Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Spectral Compressive Imaging via Chromaticity-Intensity Decomposition

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16690.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16690](https://arxiv.org/abs/2509.16690)

## 🔗 유사한 논문
- [[2025-09-22/USCTNet_ A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction_20250922|USCTNet: A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction]] (86.1% similar)
- [[2025-09-22/MCGA_ Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention_20250922|MCGA: Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention]] (83.5% similar)
- [[2025-09-22/DSDNet_ Raw Domain Demoir\'eing via Dual Color-Space Synergy_20250922|DSDNet: Raw Domain Demoir\'eing via Dual Color-Space Synergy]] (81.4% similar)
- [[2025-09-22/DPC-QA Net_ A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images_20250922|DPC-QA Net: A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images]] (80.6% similar)
- [[2025-09-22/scSplit_ Bringing Severity Cognizance to Image Decomposition in Fluorescence Microscopy_20250922|scSplit: Bringing Severity Cognizance to Image Decomposition in Fluorescence Microscopy]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Hyperspectral Imaging|Hyperspectral Imaging]]
**⚡ Unique Technical**: [[keywords/Chromaticity-Intensity Decomposition|Chromaticity-Intensity Decomposition]], [[keywords/CASSI|CASSI]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16690v1 Announce Type: new 
Abstract: In coded aperture snapshot spectral imaging (CASSI), the captured measurement entangles spatial and spectral information, posing a severely ill-posed inverse problem for hyperspectral images (HSIs) reconstruction. Moreover, the captured radiance inherently depends on scene illumination, making it difficult to recover the intrinsic spectral reflectance that remains invariant to lighting conditions. To address these challenges, we propose a chromaticity-intensity decomposition framework, which disentangles an HSI into a spatially smooth intensity map and a spectrally variant chromaticity cube. The chromaticity encodes lighting-invariant reflectance, enriched with high-frequency spatial details and local spectral sparsity. Building on this decomposition, we develop CIDNet, a Chromaticity-Intensity Decomposition unfolding network within a dual-camera CASSI system. CIDNet integrates a hybrid spatial-spectral Transformer tailored to reconstruct fine-grained and sparse spectral chromaticity and a degradation-aware, spatially-adaptive noise estimation module that captures anisotropic noise across iterative stages. Extensive experiments on both synthetic and real-world CASSI datasets demonstrate that our method achieves superior performance in both spectral and chromaticity fidelity. Code and models will be publicly available.

## 📝 요약

이 논문에서는 CASSI 시스템에서의 고질적인 문제인 공간적 및 스펙트럼 정보의 얽힘과 조명 조건에 따른 스펙트럼 반사율 복원 문제를 해결하기 위해 색도-강도 분해 프레임워크를 제안합니다. 이 프레임워크는 HSI를 공간적으로 매끄러운 강도 지도와 스펙트럼적으로 변하는 색도 큐브로 분리합니다. 색도는 조명에 불변한 반사율을 인코딩하며, 고주파 공간 세부 정보와 국부적 스펙트럼 희소성을 포함합니다. 이를 기반으로, 이중 카메라 CASSI 시스템 내에서 CIDNet이라는 네트워크를 개발하였으며, 이는 세밀하고 희소한 스펙트럼 색도를 재구성하기 위한 하이브리드 공간-스펙트럼 트랜스포머와 비등방성 노이즈를 포착하는 공간 적응형 노이즈 추정 모듈을 통합합니다. 실험 결과, 제안된 방법이 스펙트럼 및 색도 충실도에서 우수한 성능을 보임을 입증하였습니다. 코드와 모델은 공개될 예정입니다.

## 🎯 주요 포인트

- 1. CASSI 시스템에서 공간 및 스펙트럼 정보를 얽힌 상태로 캡처하여 HSI 재구성 문제를 해결하기 위해 색도-강도 분해 프레임워크를 제안합니다.
- 2. 제안된 프레임워크는 HSI를 공간적으로 부드러운 강도 맵과 스펙트럼적으로 변하는 색도 큐브로 분리하여 조명 불변 반사율을 인코딩합니다.
- 3. CIDNet은 하이브리드 공간-스펙트럼 트랜스포머를 통합하여 세밀하고 희소한 스펙트럼 색도를 재구성하며, 이방성 노이즈를 포착하는 공간 적응형 노이즈 추정 모듈을 포함합니다.
- 4. 제안된 방법은 합성 및 실제 CASSI 데이터셋에서 스펙트럼 및 색도 충실도 측면에서 우수한 성능을 보입니다.
- 5. 코드와 모델은 공개될 예정입니다.


---

*Generated on 2025-09-24 04:32:02*