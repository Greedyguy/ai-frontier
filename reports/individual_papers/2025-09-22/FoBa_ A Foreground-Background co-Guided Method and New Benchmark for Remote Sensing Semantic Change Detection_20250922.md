---
keywords:
  - Semantic Change Detection
  - Foreground-Background co-guided method
  - Gated Interaction Fusion
  - Remote Sensing
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15788
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:10:38.361868",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Semantic Change Detection",
    "Foreground-Background co-guided method",
    "Gated Interaction Fusion",
    "Remote Sensing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Semantic Change Detection": 0.8,
    "Foreground-Background co-guided method": 0.75,
    "Gated Interaction Fusion": 0.78,
    "Remote Sensing": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Semantic Change Detection",
        "canonical": "Semantic Change Detection",
        "aliases": [
          "SCD"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus, enabling connections to change detection methodologies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Foreground-Background co-guided method",
        "canonical": "Foreground-Background co-guided method",
        "aliases": [
          "FoBa"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach specific to the paper, enhancing understanding of the methodology.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      },
      {
        "surface": "Gated Interaction Fusion",
        "canonical": "Gated Interaction Fusion",
        "aliases": [
          "GIF"
        ],
        "category": "unique_technical",
        "rationale": "A specific module introduced in the paper, crucial for linking to interaction techniques.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Remote Sensing",
        "canonical": "Remote Sensing",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Broad technical term that connects to a wide range of sensing technologies and applications.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
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
      "candidate_surface": "Semantic Change Detection",
      "resolved_canonical": "Semantic Change Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Foreground-Background co-guided method",
      "resolved_canonical": "Foreground-Background co-guided method",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Gated Interaction Fusion",
      "resolved_canonical": "Gated Interaction Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Remote Sensing",
      "resolved_canonical": "Remote Sensing",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# FoBa: A Foreground-Background co-Guided Method and New Benchmark for Remote Sensing Semantic Change Detection

**Korean Title:** 포바(FoBa): 원격 감지 의미 변화 탐지를 위한 전경-배경 공동 안내 방법 및 새로운 벤치마크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15788.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15788](https://arxiv.org/abs/2509.15788)

## 🔗 유사한 논문
- [[2025-09-22/Semantic Change Detection of Roads and Bridges_ A Fine-grained Dataset and Multimodal Frequency-driven Detector_20250922|Semantic Change Detection of Roads and Bridges: A Fine-grained Dataset and Multimodal Frequency-driven Detector]] (85.1% similar)
- [[2025-09-22/DC-Mamba_ Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection_20250922|DC-Mamba: Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection]] (84.9% similar)
- [[2025-09-22/RSCC_ A Large-Scale Remote Sensing Change Caption Dataset for Disaster Events_20250922|RSCC: A Large-Scale Remote Sensing Change Caption Dataset for Disaster Events]] (80.5% similar)
- [[2025-09-22/FOVAL_ Calibration-Free and Subject-Invariant Fixation Depth Estimation Across Diverse Eye-Tracking Datasets_20250922|FOVAL: Calibration-Free and Subject-Invariant Fixation Depth Estimation Across Diverse Eye-Tracking Datasets]] (79.9% similar)
- [[2025-09-18/FishBEV_ Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras_20250918|FishBEV: Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Remote Sensing|Remote Sensing]]
**⚡ Unique Technical**: [[keywords/Semantic Change Detection|Semantic Change Detection]], [[keywords/Foreground-Background co-guided method|Foreground-Background co-guided method]], [[keywords/Gated Interaction Fusion|Gated Interaction Fusion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15788v1 Announce Type: new 
Abstract: Despite the remarkable progress achieved in remote sensing semantic change detection (SCD), two major challenges remain. At the data level, existing SCD datasets suffer from limited change categories, insufficient change types, and a lack of fine-grained class definitions, making them inadequate to fully support practical applications. At the methodological level, most current approaches underutilize change information, typically treating it as a post-processing step to enhance spatial consistency, which constrains further improvements in model performance. To address these issues, we construct a new benchmark for remote sensing SCD, LevirSCD. Focused on the Beijing area, the dataset covers 16 change categories and 210 specific change types, with more fine-grained class definitions (e.g., roads are divided into unpaved and paved roads). Furthermore, we propose a foreground-background co-guided SCD (FoBa) method, which leverages foregrounds that focus on regions of interest and backgrounds enriched with contextual information to guide the model collaboratively, thereby alleviating semantic ambiguity while enhancing its ability to detect subtle changes. Considering the requirements of bi-temporal interaction and spatial consistency in SCD, we introduce a Gated Interaction Fusion (GIF) module along with a simple consistency loss to further enhance the model's detection performance. Extensive experiments on three datasets (SECOND, JL1, and the proposed LevirSCD) demonstrate that FoBa achieves competitive results compared to current SOTA methods, with improvements of 1.48%, 3.61%, and 2.81% in the SeK metric, respectively. Our code and dataset are available at https://github.com/zmoka-zht/FoBa.

## 🔍 Abstract (한글 번역)

arXiv:2509.15788v1 발표 유형: 신규  
초록: 원격 감지 의미론적 변화 탐지(SCD)에서 상당한 진전이 있었음에도 불구하고 두 가지 주요 과제가 남아 있습니다. 데이터 수준에서는 기존 SCD 데이터셋이 제한된 변화 범주, 불충분한 변화 유형, 세분화된 클래스 정의의 부족으로 인해 실질적인 응용을 완전히 지원하기에 부적합합니다. 방법론적 수준에서는 대부분의 현재 접근 방식이 변화 정보를 충분히 활용하지 못하고, 일반적으로 공간적 일관성을 향상시키기 위한 후처리 단계로 취급하여 모델 성능의 추가 개선을 제한합니다. 이러한 문제를 해결하기 위해, 우리는 원격 감지 SCD를 위한 새로운 벤치마크인 LevirSCD를 구축했습니다. 베이징 지역에 초점을 맞춘 이 데이터셋은 16개의 변화 범주와 210개의 특정 변화 유형을 포함하며, 더 세분화된 클래스 정의(예: 도로는 비포장 도로와 포장 도로로 나뉨)를 가지고 있습니다. 또한, 우리는 관심 영역에 초점을 맞춘 전경과 맥락 정보를 풍부하게 포함한 배경을 활용하여 모델을 협력적으로 안내하는 전경-배경 공동 안내 SCD(FoBa) 방법을 제안합니다. 이를 통해 의미적 모호성을 완화하면서 미세한 변화를 감지하는 능력을 향상시킵니다. SCD에서의 이중 시간 상호작용과 공간적 일관성의 요구 사항을 고려하여, 우리는 모델의 탐지 성능을 더욱 향상시키기 위해 Gated Interaction Fusion (GIF) 모듈과 간단한 일관성 손실을 도입합니다. 세 가지 데이터셋(SECOND, JL1, 제안된 LevirSCD)에서의 광범위한 실험은 FoBa가 현재 SOTA 방법과 비교하여 경쟁력 있는 결과를 달성하며, SeK 지표에서 각각 1.48%, 3.61%, 2.81%의 개선을 보여줍니다. 우리의 코드와 데이터셋은 https://github.com/zmoka-zht/FoBa에서 사용할 수 있습니다.

## 📝 요약

이 논문은 원격 감지 의미 변화 탐지(SCD)에서 데이터와 방법론의 한계를 극복하기 위해 새로운 벤치마크 LevirSCD를 제안합니다. LevirSCD는 베이징 지역을 중심으로 16개의 변화 카테고리와 210개의 세부 변화 유형을 포함하며, 도로를 포장도로와 비포장도로로 세분화하는 등 더 정교한 클래스 정의를 제공합니다. 또한, 전경-배경 공동 안내 SCD(FoBa) 방법을 제안하여 관심 영역과 배경의 맥락 정보를 활용하여 모델의 성능을 향상시킵니다. 이와 함께, 양시점 상호작용과 공간적 일관성을 고려한 Gated Interaction Fusion(GIF) 모듈과 간단한 일관성 손실을 도입하여 탐지 성능을 강화합니다. 세 가지 데이터셋(SECOND, JL1, LevirSCD)에서의 실험 결과, FoBa는 최신 방법 대비 SeK 지표에서 각각 1.48%, 3.61%, 2.81%의 성능 향상을 보였습니다. 코드와 데이터셋은 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. 기존 원격 감지 의미 변화 탐지(SCD) 데이터셋은 변화 카테고리와 유형이 제한적이고 세분화된 클래스 정의가 부족하여 실용적 응용을 충분히 지원하지 못한다.
- 2. 대부분의 기존 방법론은 변화 정보를 충분히 활용하지 못하고, 공간 일관성을 높이기 위한 후처리 단계로 취급하여 모델 성능 향상을 제한한다.
- 3. 새로운 벤치마크 데이터셋 LevirSCD는 베이징 지역을 중심으로 16개의 변화 카테고리와 210개의 구체적인 변화 유형을 포함하며, 더 세분화된 클래스 정의를 제공한다.
- 4. 제안된 FoBa 방법은 관심 영역에 초점을 맞춘 전경과 맥락 정보를 풍부하게 포함한 배경을 활용하여 모델의 의미적 모호성을 줄이고 미세한 변화를 감지하는 능력을 향상시킨다.
- 5. Gated Interaction Fusion (GIF) 모듈과 간단한 일관성 손실을 도입하여 모델의 탐지 성능을 더욱 향상시켰으며, 세 가지 데이터셋에서 경쟁력 있는 결과를 달성했다.


---

*Generated on 2025-09-23 12:10:38*