---
keywords:
  - BiPrompt-SAM
  - Segment Anything Model
  - Intersection over Union
  - Zero-Shot Learning
  - Multimodal Learning
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2503.19769
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:03:19.266790",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "BiPrompt-SAM",
    "Segment Anything Model",
    "Intersection over Union",
    "Zero-Shot Learning",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "BiPrompt-SAM": 0.88,
    "Segment Anything Model": 0.82,
    "Intersection over Union": 0.79,
    "Zero-Shot Learning": 0.8,
    "Multimodal Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "BiPrompt-SAM",
        "canonical": "BiPrompt-SAM",
        "aliases": [
          "BiPrompt SAM",
          "BiPrompt"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel dual-modal prompt segmentation framework introduced in the paper.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Segment Anything Model",
        "canonical": "Segment Anything Model",
        "aliases": [
          "SAM"
        ],
        "category": "unique_technical",
        "rationale": "A key model discussed in the paper, central to the segmentation task.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Intersection over Union",
        "canonical": "Intersection over Union",
        "aliases": [
          "IoU"
        ],
        "category": "specific_connectable",
        "rationale": "A critical metric for evaluating spatial alignment in segmentation tasks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Zero-Shot Performance",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the model's ability to perform without domain-specific training, linking to broader zero-shot learning concepts.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multimodal Encoders",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "Emphasizes the integration of multiple data types, relevant to the paper's dual-modal approach.",
        "novelty_score": 0.58,
        "connectivity_score": 0.84,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
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
      "candidate_surface": "BiPrompt-SAM",
      "resolved_canonical": "BiPrompt-SAM",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Segment Anything Model",
      "resolved_canonical": "Segment Anything Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Intersection over Union",
      "resolved_canonical": "Intersection over Union",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Zero-Shot Performance",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multimodal Encoders",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.84,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# BiPrompt-SAM: Enhancing Image Segmentation via Explicit Selection between Point and Text Prompts

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2503.19769.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2503.19769](https://arxiv.org/abs/2503.19769)

## 🔗 유사한 논문
- [[2025-09-23/DescriptorMedSAM_ Language-Image Fusion with Multi-Aspect Text Guidance for Medical Image Segmentation_20250923|DescriptorMedSAM: Language-Image Fusion with Multi-Aspect Text Guidance for Medical Image Segmentation]] (86.8% similar)
- [[2025-09-22/ENSAM_ an efficient foundation model for interactive segmentation of 3D medical images_20250922|ENSAM: an efficient foundation model for interactive segmentation of 3D medical images]] (83.8% similar)
- [[2025-09-22/pFedSAM_ Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation_20250922|pFedSAM: Personalized Federated Learning of Segment Anything Model for Medical Image Segmentation]] (83.2% similar)
- [[2025-09-22/SAMPO_Scale-wise Autoregression with Motion PrOmpt for generative world models_20250922|SAMPO:Scale-wise Autoregression with Motion PrOmpt for generative world models]] (82.8% similar)
- [[2025-09-22/TASAM_ Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation_20250922|TASAM: Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Intersection over Union|Intersection over Union]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/BiPrompt-SAM|BiPrompt-SAM]], [[keywords/Segment Anything Model|Segment Anything Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.19769v3 Announce Type: replace-cross 
Abstract: Segmentation is a fundamental task in computer vision, with prompt-driven methods gaining prominence due to their flexibility. The Segment Anything Model (SAM) excels at point-prompted segmentation, while text-based models, often leveraging powerful multimodal encoders like BEIT-3, provide rich semantic understanding. However, effectively combining these complementary modalities remains a challenge. This paper introduces BiPrompt-SAM, a novel dual-modal prompt segmentation framework employing an explicit selection mechanism. We leverage SAM's ability to generate multiple mask candidates from a single point prompt and use a text-guided mask (generated via EVF-SAM with BEIT-3) to select the point-generated mask that best aligns spatially, measured by Intersection over Union (IoU). This approach, interpretable as a simplified Mixture of Experts (MoE), effectively fuses spatial precision and semantic context without complex model modifications. Notably, our method achieves strong zero-shot performance on the Endovis17 medical dataset (89.55% mDice, 81.46% mIoU) using only a single point prompt per instance. This significantly reduces annotation burden compared to bounding boxes and aligns better with practical clinical workflows, demonstrating the method's effectiveness without domain-specific training. On the RefCOCO series, BiPrompt-SAM attained 87.1%, 86.5%, and 85.8% IoU, significantly outperforming existing approaches. Experiments show BiPrompt-SAM excels in scenarios requiring both spatial accuracy and semantic disambiguation, offering a simple, effective, and interpretable perspective on multi-modal prompt fusion.

## 📝 요약

이 논문은 컴퓨터 비전에서 세그멘테이션을 위한 새로운 이중 모달 프롬프트 세그멘테이션 프레임워크인 BiPrompt-SAM을 제안합니다. 이 방법은 SAM의 포인트 프롬프트 기반 마스크 생성 능력과 BEIT-3를 활용한 텍스트 기반 마스크를 결합하여, IoU를 기준으로 가장 잘 맞는 마스크를 선택합니다. 이 접근법은 복잡한 모델 수정 없이 공간적 정밀도와 의미적 맥락을 효과적으로 융합합니다. BiPrompt-SAM은 Endovis17 의료 데이터셋에서 89.55% mDice와 81.46% mIoU를 기록하며, 도메인 특화 훈련 없이도 높은 성능을 보였습니다. 또한 RefCOCO 시리즈에서도 기존 방법들을 능가하는 성과를 보였습니다. 이 연구는 공간적 정확성과 의미적 구분이 필요한 상황에서 효과적이고 해석 가능한 다중 모달 프롬프트 융합을 제공합니다.

## 🎯 주요 포인트

- 1. BiPrompt-SAM은 듀얼 모달 프롬프트 세분화 프레임워크로, 명시적 선택 메커니즘을 사용하여 공간적 정밀성과 의미적 맥락을 효과적으로 결합합니다.
- 2. SAM의 단일 포인트 프롬프트에서 생성된 여러 마스크 후보 중 텍스트 기반 마스크를 이용해 최적의 마스크를 선택하는 방식을 채택합니다.
- 3. BiPrompt-SAM은 Endovis17 의료 데이터셋에서 강력한 제로샷 성능을 보이며, 실질적인 임상 워크플로우와 잘 맞아 도메인 특화 훈련 없이도 효과적입니다.
- 4. RefCOCO 시리즈에서 BiPrompt-SAM은 기존 방법들을 크게 능가하는 IoU 성능을 기록했습니다.
- 5. 이 방법은 공간적 정확성과 의미적 명확성이 요구되는 시나리오에서 뛰어난 성능을 발휘하며, 복잡한 모델 수정 없이 간단하고 효과적인 멀티모달 프롬프트 융합을 제공합니다.


---

*Generated on 2025-09-24 03:03:19*