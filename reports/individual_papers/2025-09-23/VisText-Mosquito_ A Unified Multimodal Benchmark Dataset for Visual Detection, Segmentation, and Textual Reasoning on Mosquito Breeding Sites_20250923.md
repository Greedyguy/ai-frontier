---
keywords:
  - Multimodal Learning
  - YOLO Model
  - Vision-Language Model
  - Few-Shot Learning
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2506.14629
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:17:12.922151",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "YOLO Model",
    "Vision-Language Model",
    "Few-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "YOLO Model": 0.78,
    "Vision-Language Model": 0.82,
    "Few-Shot Learning": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal dataset",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal data",
          "Multimodal integration"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the integration of visual and textual data, a key aspect of the study.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "YOLOv9s model",
        "canonical": "YOLO Model",
        "aliases": [
          "YOLOv9s",
          "YOLO"
        ],
        "category": "unique_technical",
        "rationale": "Specific model used for object detection, relevant for technical discussions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-language models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-language",
          "LVLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Represents the integration of vision and language processing, central to the paper's methodology.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Few-shot settings",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-shot",
          "Few-shot learning"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the learning approach tested in the study, relevant for linking learning paradigms.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "object detection",
      "segmentation precision",
      "BLEU score"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal dataset",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "YOLOv9s model",
      "resolved_canonical": "YOLO Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-language models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Few-shot settings",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# VisText-Mosquito: A Unified Multimodal Benchmark Dataset for Visual Detection, Segmentation, and Textual Reasoning on Mosquito Breeding Sites

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.14629.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2506.14629](https://arxiv.org/abs/2506.14629)

## 🔗 유사한 논문
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets]] (81.6% similar)
- [[2025-09-22/Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models_20250922|Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models]] (81.4% similar)
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL: Toward Expert-Level Medical Text Validation with Language Models]] (80.8% similar)
- [[2025-09-18/Iterative Prompt Refinement for Safer Text-to-Image Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (80.8% similar)
- [[2025-09-22/SAR-TEXT_ A Large-Scale SAR Image-Text Dataset Built with SAR-Narrator and Progressive Transfer Learning_20250922|SAR-TEXT: A Large-Scale SAR Image-Text Dataset Built with SAR-Narrator and Progressive Transfer Learning]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/YOLO Model|YOLO Model]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.14629v2 Announce Type: replace-cross 
Abstract: Mosquito-borne diseases pose a major global health risk, requiring early detection and proactive control of breeding sites to prevent outbreaks. In this paper, we present VisText-Mosquito, a multimodal dataset that integrates visual and textual data to support automated detection, segmentation, and reasoning for mosquito breeding site analysis. The dataset includes 1,828 annotated images for object detection, 142 images for water surface segmentation, and natural language reasoning texts linked to each image. The YOLOv9s model achieves the highest precision of 0.92926 and mAP@50 of 0.92891 for object detection, while YOLOv11n-Seg reaches a segmentation precision of 0.91587 and mAP@50 of 0.79795. For reasoning generation, we tested a range of large vision-language models (LVLMs) in both zero-shot and few-shot settings. Our fine-tuned Mosquito-LLaMA3-8B model achieved the best results, with a final loss of 0.0028, a BLEU score of 54.7, BERTScore of 0.91, and ROUGE-L of 0.85. This dataset and model framework emphasize the theme "Prevention is Better than Cure", showcasing how AI-based detection can proactively address mosquito-borne disease risks. The dataset and implementation code are publicly available at GitHub: https://github.com/adnanul-islam-jisun/VisText-Mosquito

## 📝 요약

이 논문은 모기 매개 질병의 조기 탐지와 번식지 통제를 위한 VisText-Mosquito라는 멀티모달 데이터셋을 소개합니다. 이 데이터셋은 시각 및 텍스트 데이터를 통합하여 모기 번식지 분석을 위한 자동 탐지, 분할, 추론을 지원합니다. YOLOv9s 모델은 객체 탐지에서 높은 정밀도와 mAP를 기록하였으며, YOLOv11n-Seg는 분할에서 우수한 성능을 보였습니다. 추론 생성에서는 Mosquito-LLaMA3-8B 모델이 최상의 결과를 달성했습니다. 이 연구는 "예방이 치료보다 낫다"는 주제를 강조하며, AI 기반 탐지가 모기 매개 질병의 위험을 사전에 해결할 수 있음을 보여줍니다. 데이터셋과 구현 코드는 GitHub에서 공개됩니다.

## 🎯 주요 포인트

- 1. VisText-Mosquito는 모기 서식지 분석을 위한 시각 및 텍스트 데이터를 통합한 멀티모달 데이터셋을 제공합니다.
- 2. YOLOv9s 모델은 객체 탐지에서 0.92926의 높은 정밀도와 0.92891의 mAP@50을 달성했습니다.
- 3. YOLOv11n-Seg 모델은 수면 분할에서 0.91587의 정밀도와 0.79795의 mAP@50을 기록했습니다.
- 4. Mosquito-LLaMA3-8B 모델은 추론 생성에서 BLEU 점수 54.7, BERTScore 0.91, ROUGE-L 0.85로 최고의 성능을 보였습니다.
- 5. 이 데이터셋과 모델은 "예방이 치료보다 낫다"는 주제를 강조하며, AI 기반 탐지가 모기 매개 질병 위험을 사전에 해결할 수 있음을 보여줍니다.


---

*Generated on 2025-09-24 04:17:12*