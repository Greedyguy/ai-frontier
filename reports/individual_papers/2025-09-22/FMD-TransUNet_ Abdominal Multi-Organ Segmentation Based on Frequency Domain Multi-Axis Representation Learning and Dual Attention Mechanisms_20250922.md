---
keywords:
  - FMD-TransUNet
  - Multi-axis External Weight Block
  - Attention Mechanism
  - Frequency-domain representation
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.16044
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:26:54.068312",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "FMD-TransUNet",
    "Multi-axis External Weight Block",
    "Attention Mechanism",
    "Frequency-domain representation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "FMD-TransUNet": 0.78,
    "Multi-axis External Weight Block": 0.72,
    "Attention Mechanism": 0.8,
    "Frequency-domain representation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "FMD-TransUNet",
        "canonical": "FMD-TransUNet",
        "aliases": [
          "Frequency Domain Multi-Axis TransUNet"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework specifically designed for abdominal multi-organ segmentation, offering unique technical insights.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multi-axis External Weight Block",
        "canonical": "Multi-axis External Weight Block",
        "aliases": [
          "MEWB"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a new method for extracting frequency-domain features, enhancing the framework's capability.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Dual Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "DA+",
          "Dual Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Enhances feature fusion and is a key component in many advanced neural network architectures.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Frequency-domain representation",
        "canonical": "Frequency-domain representation",
        "aliases": [
          "Frequency-domain analysis"
        ],
        "category": "specific_connectable",
        "rationale": "Provides a complementary perspective to spatial-domain analysis, crucial for comprehensive segmentation tasks.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
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
      "candidate_surface": "FMD-TransUNet",
      "resolved_canonical": "FMD-TransUNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multi-axis External Weight Block",
      "resolved_canonical": "Multi-axis External Weight Block",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Dual Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Frequency-domain representation",
      "resolved_canonical": "Frequency-domain representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# FMD-TransUNet: Abdominal Multi-Organ Segmentation Based on Frequency Domain Multi-Axis Representation Learning and Dual Attention Mechanisms

**Korean Title:** FMD-TransUNet: 주파수 도메인 다축 표현 학습과 이중 주의 메커니즘을 기반으로 한 복부 다기관 분할

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16044.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.16044](https://arxiv.org/abs/2509.16044)

## 🔗 유사한 논문
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (84.4% similar)
- [[2025-09-22/UniMRSeg_ Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation_20250922|UniMRSeg: Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation]] (83.6% similar)
- [[2025-09-22/ENSAM_ an efficient foundation model for interactive segmentation of 3D medical images_20250922|ENSAM: an efficient foundation model for interactive segmentation of 3D medical images]] (82.0% similar)
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (81.8% similar)
- [[2025-09-19/DiffCut_ Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut_20250919|DiffCut: Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Frequency-domain representation|Frequency-domain representation]]
**⚡ Unique Technical**: [[keywords/FMD-TransUNet|FMD-TransUNet]], [[keywords/Multi-axis External Weight Block|Multi-axis External Weight Block]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16044v1 Announce Type: cross 
Abstract: Accurate abdominal multi-organ segmentation is critical for clinical applications. Although numerous deep learning-based automatic segmentation methods have been developed, they still struggle to segment small, irregular, or anatomically complex organs. Moreover, most current methods focus on spatial-domain analysis, often overlooking the synergistic potential of frequency-domain representations. To address these limitations, we propose a novel framework named FMD-TransUNet for precise abdominal multi-organ segmentation. It innovatively integrates the Multi-axis External Weight Block (MEWB) and the improved dual attention module (DA+) into the TransUNet framework. The MEWB extracts multi-axis frequency-domain features to capture both global anatomical structures and local boundary details, providing complementary information to spatial-domain representations. The DA+ block utilizes depthwise separable convolutions and incorporates spatial and channel attention mechanisms to enhance feature fusion, reduce redundant information, and narrow the semantic gap between the encoder and decoder. Experimental validation on the Synapse dataset shows that FMD-TransUNet outperforms other recent state-of-the-art methods, achieving an average DSC of 81.32\% and a HD of 16.35 mm across eight abdominal organs. Compared to the baseline model, the average DSC increased by 3.84\%, and the average HD decreased by 15.34 mm. These results demonstrate the effectiveness of FMD-TransUNet in improving the accuracy of abdominal multi-organ segmentation.

## 🔍 Abstract (한글 번역)

arXiv:2509.16044v1 발표 유형: 교차  
초록: 정확한 복부 다기관 분할은 임상 응용에 매우 중요합니다. 수많은 딥러닝 기반 자동 분할 방법이 개발되었지만, 여전히 작고 불규칙하거나 해부학적으로 복잡한 기관을 분할하는 데 어려움을 겪고 있습니다. 게다가 대부분의 현재 방법은 공간 도메인 분석에 중점을 두고 있으며, 주파수 도메인 표현의 시너지 잠재력을 종종 간과합니다. 이러한 한계를 해결하기 위해, 우리는 정밀한 복부 다기관 분할을 위한 새로운 프레임워크인 FMD-TransUNet을 제안합니다. 이 프레임워크는 혁신적으로 다축 외부 가중치 블록(MEWB)과 개선된 이중 주의 모듈(DA+)을 TransUNet 프레임워크에 통합합니다. MEWB는 다축 주파수 도메인 특징을 추출하여 전역 해부학적 구조와 국부 경계 세부 사항을 포착하여 공간 도메인 표현에 보완적인 정보를 제공합니다. DA+ 블록은 깊이별 분리 합성곱을 활용하고 공간 및 채널 주의 메커니즘을 통합하여 특징 융합을 향상시키고, 중복 정보를 줄이며, 인코더와 디코더 간의 의미적 차이를 좁힙니다. Synapse 데이터셋에 대한 실험적 검증 결과, FMD-TransUNet은 최근의 다른 최첨단 방법들을 능가하여 8개의 복부 기관에서 평균 DSC 81.32%와 HD 16.35 mm를 달성했습니다. 기준 모델과 비교하여, 평균 DSC는 3.84% 증가하였고, 평균 HD는 15.34 mm 감소하였습니다. 이러한 결과는 복부 다기관 분할의 정확성을 향상시키는 데 있어 FMD-TransUNet의 효과성을 입증합니다.

## 📝 요약

이 논문은 정확한 복부 다중 장기 분할을 위한 새로운 프레임워크인 FMD-TransUNet을 제안합니다. 기존 방법들이 작은 장기나 복잡한 해부학적 구조의 분할에 어려움을 겪고, 주로 공간 영역 분석에 치중하는 문제를 해결하기 위해, FMD-TransUNet은 TransUNet 프레임워크에 다축 외부 가중치 블록(MEWB)과 개선된 이중 주의 모듈(DA+)을 통합합니다. MEWB는 다축 주파수 영역 특징을 추출하여 공간 영역 표현에 보완적인 정보를 제공하고, DA+는 깊이별 분리 합성곱과 주의 메커니즘을 활용하여 특징 융합을 강화합니다. 실험 결과, FMD-TransUNet은 Synapse 데이터셋에서 평균 DSC 81.32%와 HD 16.35 mm를 기록하며, 기존 최첨단 방법들보다 우수한 성능을 보였습니다. 이는 복부 다중 장기 분할의 정확성을 향상시켰음을 입증합니다.

## 🎯 주요 포인트

- 1. FMD-TransUNet는 복부 다기관 분할의 정확성을 높이기 위해 제안된 새로운 프레임워크입니다.
- 2. 이 프레임워크는 다축 주파수 도메인 특징을 추출하는 MEWB와 개선된 이중 주의 모듈(DA+)을 통합하여 공간 도메인 표현을 보완합니다.
- 3. 실험 결과, FMD-TransUNet는 Synapse 데이터셋에서 평균 DSC 81.32%와 HD 16.35mm를 기록하며 최신 방법들보다 우수한 성능을 보였습니다.
- 4. FMD-TransUNet는 기본 모델에 비해 평균 DSC가 3.84% 증가하고 평균 HD가 15.34mm 감소하여 성능 향상을 입증했습니다.


---

*Generated on 2025-09-23 12:26:54*