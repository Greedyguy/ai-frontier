---
keywords:
  - Self-supervised Learning
  - Unsupervised Visual Anomaly Segmentation
  - Dense Self-supervised Learning
  - Pathology Segmentation
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2502.08321
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:30:47.609524",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Unsupervised Visual Anomaly Segmentation",
    "Dense Self-supervised Learning",
    "Pathology Segmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.9,
    "Unsupervised Visual Anomaly Segmentation": 0.78,
    "Dense Self-supervised Learning": 0.77,
    "Pathology Segmentation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-supervised training"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key technique used in the paper and is already a recognized concept in the field, facilitating connections with related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.9
      },
      {
        "surface": "Unsupervised Visual Anomaly Segmentation",
        "canonical": "Unsupervised Visual Anomaly Segmentation",
        "aliases": [
          "UVAS"
        ],
        "category": "unique_technical",
        "rationale": "This represents a novel approach to pathology detection, enhancing the paper's unique contribution to the field.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Dense Self-supervised Learning",
        "canonical": "Dense Self-supervised Learning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a specific innovation introduced in the paper, offering a new method for feature extraction without supervised pretraining.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Pathology Segmentation",
        "canonical": "Pathology Segmentation",
        "aliases": [
          "medical image segmentation"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental application area of the research, linking it to a broad range of medical imaging studies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Unsupervised Visual Anomaly Segmentation",
      "resolved_canonical": "Unsupervised Visual Anomaly Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Dense Self-supervised Learning",
      "resolved_canonical": "Dense Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Pathology Segmentation",
      "resolved_canonical": "Pathology Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Screener: Self-supervised Pathology Segmentation in Medical CT Images

**Korean Title:** 화면: 의료 CT 이미지에서의 자가 지도 병리 분할

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2502.08321.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2502.08321](https://arxiv.org/abs/2502.08321)

## 🔗 유사한 논문
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (81.7% similar)
- [[2025-09-22/ENSAM_ an efficient foundation model for interactive segmentation of 3D medical images_20250922|ENSAM: an efficient foundation model for interactive segmentation of 3D medical images]] (81.5% similar)
- [[2025-09-22/Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images_20250922|Uncertainty-Gated Deformable Network for Breast Tumor Segmentation in MR Images]] (81.3% similar)
- [[2025-09-22/The Missing Piece_ A Case for Pre-Training in 3D Medical Object Detection_20250922|The Missing Piece: A Case for Pre-Training in 3D Medical Object Detection]] (81.3% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Pathology Segmentation|Pathology Segmentation]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Unsupervised Visual Anomaly Segmentation|Unsupervised Visual Anomaly Segmentation]], [[keywords/Dense Self-supervised Learning|Dense Self-supervised Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.08321v2 Announce Type: replace 
Abstract: Accurate detection of all pathological findings in 3D medical images remains a significant challenge, as supervised models are limited to detecting only the few pathology classes annotated in existing datasets. To address this, we frame pathology detection as an unsupervised visual anomaly segmentation (UVAS) problem, leveraging the inherent rarity of pathological patterns compared to healthy ones. We enhance the existing density-based UVAS framework with two key innovations: (1) dense self-supervised learning for feature extraction, eliminating the need for supervised pretraining, and (2) learned, masking-invariant dense features as conditioning variables, replacing hand-crafted positional encodings. Trained on over 30,000 unlabeled 3D CT volumes, our fully self-supervised model, Screener, outperforms existing UVAS methods on four large-scale test datasets comprising 1,820 scans with diverse pathologies. Furthermore, in a supervised fine-tuning setting, Screener surpasses existing self-supervised pretraining methods, establishing it as a state-of-the-art foundation for pathology segmentation. The code and pretrained models will be made publicly available.

## 🔍 Abstract (한글 번역)

arXiv:2502.08321v2 발표 유형: 교체  
초록: 3D 의료 영상에서 모든 병리학적 소견을 정확하게 감지하는 것은 여전히 중요한 도전 과제입니다. 이는 감독 학습 모델이 기존 데이터셋에 주석이 달린 소수의 병리학적 클래스만 감지할 수 있기 때문입니다. 이를 해결하기 위해 우리는 병리학적 감지를 비지도 시각적 이상 분할(UVAS) 문제로 설정하고, 건강한 패턴에 비해 병리학적 패턴의 고유한 희소성을 활용합니다. 우리는 기존의 밀도 기반 UVAS 프레임워크를 두 가지 주요 혁신으로 강화합니다: (1) 특징 추출을 위한 밀집 자가 지도 학습을 통해 감독 사전 학습의 필요성을 제거하고, (2) 수작업으로 제작된 위치 인코딩을 대체하여 학습된 마스킹 불변 밀집 특징을 조건 변수로 사용합니다. 30,000개 이상의 라벨이 없는 3D CT 볼륨으로 훈련된 우리의 완전 자가 지도 모델인 Screener는 다양한 병리를 포함한 1,820개의 스캔으로 구성된 네 개의 대규모 테스트 데이터셋에서 기존 UVAS 방법을 능가합니다. 더욱이, 감독 미세 조정 설정에서 Screener는 기존의 자가 지도 사전 학습 방법을 능가하여 병리학적 분할을 위한 최첨단 기반으로 자리 잡았습니다. 코드와 사전 학습된 모델은 공개적으로 제공될 예정입니다.

## 📝 요약

이 논문은 3D 의료 영상에서 병리학적 소견을 정확하게 탐지하는 문제를 다룹니다. 기존의 지도 학습 모델은 주석된 병리 클래스만 탐지할 수 있는 한계가 있어, 이를 해결하기 위해 병리 탐지를 비지도 시각적 이상 분할(UVAS) 문제로 정의했습니다. 제안된 방법은 (1) 밀집 자가 지도 학습을 통해 특징을 추출하여 지도 사전 학습의 필요성을 없애고, (2) 학습된 마스킹 불변 밀집 특징을 조건 변수로 사용하여 기존의 수작업 위치 인코딩을 대체합니다. 30,000개 이상의 라벨 없는 3D CT 볼륨으로 학습된 자가 지도 모델인 Screener는 다양한 병리를 포함한 1,820개의 스캔을 가진 네 개의 대규모 테스트 데이터셋에서 기존 UVAS 방법을 능가했습니다. 또한, 지도 학습 미세 조정 설정에서도 기존의 자가 지도 사전 학습 방법을 뛰어넘어 병리 분할의 최첨단 기초로 자리 잡았습니다. 코드와 사전 학습된 모델은 공개될 예정입니다.

## 🎯 주요 포인트

- 1. 3D 의료 영상에서 병리학적 소견을 정확하게 탐지하는 것은 여전히 중요한 도전 과제입니다.
- 2. 병리 탐지를 비지도 시각적 이상 분할 문제로 설정하여 병리 패턴의 희소성을 활용합니다.
- 3. 밀도 기반 UVAS 프레임워크를 개선하기 위해 자가 지도 학습과 학습된 마스킹 불변 밀집 특징을 도입했습니다.
- 4. 30,000개 이상의 라벨 없는 3D CT 볼륨으로 학습된 모델 Screener는 기존 UVAS 방법을 능가합니다.
- 5. Screener는 지도 학습 미세 조정 설정에서도 기존 자가 지도 사전 학습 방법을 능가하여 병리 분할의 최첨단 기초로 자리 잡았습니다.


---

*Generated on 2025-09-23 12:30:47*