---
keywords:
  - Self-supervised Learning
  - Contrastive Learning
  - Consistency Regularization
  - Multimodal Learning
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.16170
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:23:10.478617",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Contrastive Learning",
    "Consistency Regularization",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.8,
    "Contrastive Learning": 0.75,
    "Consistency Regularization": 0.7,
    "Multimodal Learning": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised compensation",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "HSSC"
        ],
        "category": "specific_connectable",
        "rationale": "The concept of self-supervised compensation aligns closely with self-supervised learning techniques, enhancing connectivity with existing research in this area.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Modality-invariant contrastive learning",
        "canonical": "Contrastive Learning",
        "aliases": [
          "contrastive modality learning"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is a specific application of contrastive learning, which is a well-connected concept in machine learning literature.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      },
      {
        "surface": "Hybrid consistency constraint",
        "canonical": "Consistency Regularization",
        "aliases": [
          "hybrid constraint"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a novel approach to ensuring model stability across modalities, making it a unique contribution to the field.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      },
      {
        "surface": "Cross-modal fusion",
        "canonical": "Multimodal Learning",
        "aliases": [
          "cross-modal integration"
        ],
        "category": "specific_connectable",
        "rationale": "Cross-modal fusion is a key aspect of multimodal learning, facilitating connections with other research in integrating multiple data modalities.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.68,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "modality reconstruction",
      "reverse attention adapter"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-supervised compensation",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Modality-invariant contrastive learning",
      "resolved_canonical": "Contrastive Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Hybrid consistency constraint",
      "resolved_canonical": "Consistency Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Cross-modal fusion",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.68,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# UniMRSeg: Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation

**Korean Title:** UniMRSeg: 계층적 자가 지도 보상을 통한 통합 모달리티-릴랙스 세분화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16170.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.16170](https://arxiv.org/abs/2509.16170)

## 🔗 유사한 논문
- [[2025-09-22/SLaM-DiMM_ Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI_20250922|SLaM-DiMM: Shared Latent Modeling for Diffusion Based Missing Modality Synthesis in MRI]] (83.8% similar)
- [[2025-09-22/FMD-TransUNet_ Abdominal Multi-Organ Segmentation Based on Frequency Domain Multi-Axis Representation Learning and Dual Attention Mechanisms_20250922|FMD-TransUNet: Abdominal Multi-Organ Segmentation Based on Frequency Domain Multi-Axis Representation Learning and Dual Attention Mechanisms]] (83.6% similar)
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (83.5% similar)
- [[2025-09-22/UNIV_ Unified Foundation Model for Infrared and Visible Modalities_20250922|UNIV: Unified Foundation Model for Infrared and Visible Modalities]] (83.2% similar)
- [[2025-09-18/Semi-MoE_ Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation_20250918|Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]], [[keywords/Contrastive Learning|Contrastive Learning]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Consistency Regularization|Consistency Regularization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16170v1 Announce Type: new 
Abstract: Multi-modal image segmentation faces real-world deployment challenges from incomplete/corrupted modalities degrading performance. While existing methods address training-inference modality gaps via specialized per-combination models, they introduce high deployment costs by requiring exhaustive model subsets and model-modality matching. In this work, we propose a unified modality-relax segmentation network (UniMRSeg) through hierarchical self-supervised compensation (HSSC). Our approach hierarchically bridges representation gaps between complete and incomplete modalities across input, feature and output levels. %
First, we adopt modality reconstruction with the hybrid shuffled-masking augmentation, encouraging the model to learn the intrinsic modality characteristics and generate meaningful representations for missing modalities through cross-modal fusion. %
Next, modality-invariant contrastive learning implicitly compensates the feature space distance among incomplete-complete modality pairs. Furthermore, the proposed lightweight reverse attention adapter explicitly compensates for the weak perceptual semantics in the frozen encoder. Last, UniMRSeg is fine-tuned under the hybrid consistency constraint to ensure stable prediction under all modality combinations without large performance fluctuations. Without bells and whistles, UniMRSeg significantly outperforms the state-of-the-art methods under diverse missing modality scenarios on MRI-based brain tumor segmentation, RGB-D semantic segmentation, RGB-D/T salient object segmentation. The code will be released at https://github.com/Xiaoqi-Zhao-DLUT/UniMRSeg.

## 🔍 Abstract (한글 번역)

arXiv:2509.16170v1 발표 유형: 신규  
초록: 다중 모달 이미지 분할은 불완전하거나 손상된 모달리티로 인해 성능이 저하되는 실제 환경에서의 배포 문제에 직면하고 있습니다. 기존 방법들은 조합별 특화 모델을 통해 훈련-추론 모달리티 간의 차이를 해결하지만, 이는 모델 하위 집합과 모델-모달리티 매칭을 필요로 하여 높은 배포 비용을 초래합니다. 본 연구에서는 계층적 자기 지도 보상을 통한 통합 모달리티 완화 분할 네트워크(UniMRSeg)를 제안합니다. 우리의 접근법은 입력, 특징, 출력 수준에서 완전한 모달리티와 불완전한 모달리티 간의 표현 격차를 계층적으로 연결합니다.  
우선, 하이브리드 셔플 마스킹 증강을 사용한 모달리티 재구성을 채택하여 모델이 본질적인 모달리티 특성을 학습하고 교차 모달 융합을 통해 누락된 모달리티에 대한 의미 있는 표현을 생성하도록 유도합니다.  
다음으로, 모달리티 불변 대조 학습은 불완전-완전 모달리티 쌍 간의 특징 공간 거리를 암묵적으로 보상합니다. 또한, 제안된 경량 역 주의 어댑터는 고정된 인코더에서 약한 지각적 의미를 명시적으로 보상합니다. 마지막으로, UniMRSeg는 모든 모달리티 조합에서 큰 성능 변동 없이 안정적인 예측을 보장하기 위해 하이브리드 일관성 제약 하에 미세 조정됩니다. 특별한 기교 없이 UniMRSeg는 MRI 기반 뇌종양 분할, RGB-D 의미 분할, RGB-D/T 주목 객체 분할에서 다양한 누락 모달리티 시나리오 하에서 최첨단 방법들을 크게 능가합니다. 코드는 https://github.com/Xiaoqi-Zhao-DLUT/UniMRSeg에서 공개될 예정입니다.

## 📝 요약

이 논문은 다중 모달 이미지 분할의 실제 적용에서 발생하는 불완전하거나 손상된 모달리티로 인한 성능 저하 문제를 해결하기 위해 UniMRSeg라는 통합 모달리티 완화 분할 네트워크를 제안합니다. 제안된 방법론은 계층적 자기 지도 보상을 통해 입력, 특징, 출력 수준에서 완전한 모달리티와 불완전한 모달리티 간의 표현 격차를 줄입니다. 하이브리드 셔플 마스킹 증강을 사용하여 모달리티 재구성을 수행하고, 모달리티 불변 대조 학습과 경량 역 주의 어댑터를 통해 특징 공간의 거리를 보상합니다. 또한, 하이브리드 일관성 제약을 통해 모든 모달리티 조합에서 안정적인 예측을 보장합니다. 이 방법은 MRI 기반 뇌종양 분할, RGB-D 의미론적 분할, RGB-D/T 주목 객체 분할에서 최신 방법들을 능가하는 성과를 보였습니다.

## 🎯 주요 포인트

- 1. UniMRSeg는 불완전하거나 손상된 모달리티로 인한 성능 저하 문제를 해결하기 위해 계층적 자가 지도 보상을 활용한 통합 모달리티 릴랙스 세분화 네트워크를 제안합니다.
- 2. 하이브리드 셔플 마스킹 증강을 통한 모달리티 재구성을 통해 모델이 모달리티의 본질적 특성을 학습하고 교차 모달 융합을 통해 의미 있는 표현을 생성하도록 유도합니다.
- 3. 모달리티 불변 대조 학습은 불완전-완전 모달리티 쌍 간의 특징 공간 거리를 암묵적으로 보상합니다.
- 4. 경량의 역 주의 어댑터는 고정된 인코더에서 약한 지각 의미를 명시적으로 보상합니다.
- 5. UniMRSeg는 모든 모달리티 조합에서 안정적인 예측을 보장하기 위해 하이브리드 일관성 제약 하에 미세 조정되며, 다양한 누락 모달리티 시나리오에서 최첨단 방법보다 뛰어난 성능을 보입니다.


---

*Generated on 2025-09-23 12:23:10*