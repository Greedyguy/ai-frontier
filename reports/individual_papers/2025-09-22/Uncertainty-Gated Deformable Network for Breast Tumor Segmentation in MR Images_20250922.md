---
keywords:
  - Transformer
  - Uncertainty-Gated Enhancing Module
  - Deformable Network
  - Boundary-sensitive Deep Supervision Loss
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15758
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:24:35.502821",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Uncertainty-Gated Enhancing Module",
    "Deformable Network",
    "Boundary-sensitive Deep Supervision Loss"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Uncertainty-Gated Enhancing Module": 0.8,
    "Deformable Network": 0.78,
    "Boundary-sensitive Deep Supervision Loss": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [
          "Attention Mechanism"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are central to the proposed method, enabling integration of local and global features.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Uncertainty-Gated Enhancing Module",
        "canonical": "Uncertainty-Gated Enhancing Module",
        "aliases": [
          "U-GEM"
        ],
        "category": "unique_technical",
        "rationale": "This module is a novel contribution that enhances feature exchange based on uncertainty, crucial for the method's performance.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Deformable Network",
        "canonical": "Deformable Network",
        "aliases": [
          "Deformable Feature Modeling"
        ],
        "category": "unique_technical",
        "rationale": "The deformable network is a key innovation for adapting to irregular tumor shapes.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Boundary-sensitive Deep Supervision Loss",
        "canonical": "Boundary-sensitive Deep Supervision Loss",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This loss function is specifically designed to improve tumor boundary delineation, a critical aspect of the study.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "breast tumor",
      "MRI",
      "segmentation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Uncertainty-Gated Enhancing Module",
      "resolved_canonical": "Uncertainty-Gated Enhancing Module",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Deformable Network",
      "resolved_canonical": "Deformable Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Boundary-sensitive Deep Supervision Loss",
      "resolved_canonical": "Boundary-sensitive Deep Supervision Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images

**Korean Title:** 불확실성 게이트 변형 네트워크를 이용한 MR 영상에서의 유방 종양 분할

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15758.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15758](https://arxiv.org/abs/2509.15758)

## 🔗 유사한 논문
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (84.6% similar)
- [[2025-09-22/FMD-TransUNet_ Abdominal Multi-Organ Segmentation Based on Frequency Domain Multi-Axis Representation Learning and Dual Attention Mechanisms_20250922|FMD-TransUNet: Abdominal Multi-Organ Segmentation Based on Frequency Domain Multi-Axis Representation Learning and Dual Attention Mechanisms]] (84.4% similar)
- [[2025-09-22/UniMRSeg_ Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation_20250922|UniMRSeg: Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation]] (83.5% similar)
- [[2025-09-22/Prostate Capsule Segmentation from Micro-Ultrasound Images using Adaptive Focal Loss_20250922|Prostate Capsule Segmentation from Micro-Ultrasound Images using Adaptive Focal Loss]] (82.7% similar)
- [[2025-09-18/Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification_20250918|Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/Uncertainty-Gated Enhancing Module|Uncertainty-Gated Enhancing Module]], [[keywords/Deformable Network|Deformable Network]], [[keywords/Boundary-sensitive Deep Supervision Loss|Boundary-sensitive Deep Supervision Loss]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15758v1 Announce Type: cross 
Abstract: Accurate segmentation of breast tumors in magnetic resonance images (MRI) is essential for breast cancer diagnosis, yet existing methods face challenges in capturing irregular tumor shapes and effectively integrating local and global features. To address these limitations, we propose an uncertainty-gated deformable network to leverage the complementary information from CNN and Transformers. Specifically, we incorporates deformable feature modeling into both convolution and attention modules, enabling adaptive receptive fields for irregular tumor contours. We also design an Uncertainty-Gated Enhancing Module (U-GEM) to selectively exchange complementary features between CNN and Transformer based on pixel-wise uncertainty, enhancing both local and global representations. Additionally, a Boundary-sensitive Deep Supervision Loss is introduced to further improve tumor boundary delineation. Comprehensive experiments on two clinical breast MRI datasets demonstrate that our method achieves superior segmentation performance compared with state-of-the-art methods, highlighting its clinical potential for accurate breast tumor delineation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15758v1 발표 유형: 교차  
초록: 자기공명영상(MRI)에서 유방 종양의 정확한 분할은 유방암 진단에 필수적이지만, 기존 방법들은 불규칙한 종양 형태를 포착하고 지역 및 전역 특징을 효과적으로 통합하는 데 어려움을 겪고 있습니다. 이러한 한계를 해결하기 위해, 우리는 CNN과 트랜스포머의 보완적 정보를 활용하기 위한 불확실성 게이트 변형 네트워크를 제안합니다. 구체적으로, 우리는 컨볼루션 및 어텐션 모듈 모두에 변형 가능한 특징 모델링을 통합하여 불규칙한 종양 윤곽에 대한 적응형 수용 영역을 가능하게 합니다. 또한, 픽셀 단위의 불확실성에 기반하여 CNN과 트랜스포머 간의 보완적 특징을 선택적으로 교환하는 불확실성 게이트 강화 모듈(U-GEM)을 설계하여 지역 및 전역 표현을 모두 강화합니다. 추가적으로, 종양 경계 구분을 더욱 개선하기 위해 경계 민감 심층 감독 손실을 도입합니다. 두 개의 임상 유방 MRI 데이터셋에 대한 포괄적인 실험은 우리의 방법이 최첨단 방법들과 비교하여 우수한 분할 성능을 달성함을 보여주며, 정확한 유방 종양 구분을 위한 임상적 잠재력을 강조합니다.

## 📝 요약

이 논문은 유방암 진단을 위한 MRI 영상에서의 유방 종양 분할을 개선하기 위해 불확실성 게이트 변형 네트워크를 제안합니다. 기존 방법들이 불규칙한 종양 형태를 포착하고 지역 및 전역 특징을 효과적으로 통합하는 데 어려움을 겪는 문제를 해결하고자 합니다. 제안된 네트워크는 CNN과 트랜스포머의 보완적 정보를 활용하며, 변형 가능한 특징 모델링을 통해 불규칙한 종양 윤곽에 적응하는 수용 영역을 제공합니다. 또한, 픽셀 단위의 불확실성을 기반으로 CNN과 트랜스포머 간의 보완적 특징을 선택적으로 교환하는 불확실성 게이트 강화 모듈(U-GEM)을 설계하여 지역 및 전역 표현을 강화합니다. 종양 경계 구분을 개선하기 위해 경계 민감 심층 감독 손실도 도입되었습니다. 두 개의 임상 유방 MRI 데이터셋에 대한 실험 결과, 제안된 방법이 최첨단 방법들보다 우수한 분할 성능을 보이며, 정확한 유방 종양 구분을 위한 임상적 잠재력을 강조합니다.

## 🎯 주요 포인트

- 1. 기존 방법들이 직면한 불규칙한 종양 형태와 지역 및 전역 특징 통합의 어려움을 해결하기 위해 불확실성 게이트 변형 네트워크를 제안합니다.
- 2. CNN과 트랜스포머의 상호 보완적 정보를 활용하기 위해 변형 가능한 특징 모델링을 컨볼루션 및 주의 모듈에 통합하여 적응형 수용 영역을 제공합니다.
- 3. 픽셀 단위 불확실성에 기반한 CNN과 트랜스포머 간의 보완적 특징 교환을 위해 불확실성 게이트 강화 모듈(U-GEM)을 설계하였습니다.
- 4. 종양 경계 구분을 개선하기 위해 경계 민감형 심층 감독 손실을 도입하였습니다.
- 5. 두 개의 임상 유방 MRI 데이터셋에서의 포괄적인 실험 결과, 제안된 방법이 최첨단 기법들보다 우수한 분할 성능을 보여 임상적 잠재력을 강조합니다.


---

*Generated on 2025-09-23 12:24:35*