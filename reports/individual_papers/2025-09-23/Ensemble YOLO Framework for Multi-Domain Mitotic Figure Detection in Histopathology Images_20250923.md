---
keywords:
  - YOLO
  - Mitosis Detection
  - Digital Pathology
  - Ensemble Learning
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.02957
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:36:44.046325",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "YOLO",
    "Mitosis Detection",
    "Digital Pathology",
    "Ensemble Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "YOLO": 0.85,
    "Mitosis Detection": 0.78,
    "Digital Pathology": 0.8,
    "Ensemble Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "YOLOv5",
        "canonical": "YOLO",
        "aliases": [
          "YOLOv5",
          "YOLOv8"
        ],
        "category": "specific_connectable",
        "rationale": "YOLO is a widely used object detection framework, and its variants are relevant for linking advancements in object detection.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "mitotic figure detection",
        "canonical": "Mitosis Detection",
        "aliases": [
          "mitotic figure detection"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application in digital pathology, providing a unique link to specialized research in histopathology.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "histopathology images",
        "canonical": "Digital Pathology",
        "aliases": [
          "histopathological images"
        ],
        "category": "broad_technical",
        "rationale": "Digital Pathology is a broad field encompassing the analysis of histopathology images, relevant for linking to medical imaging research.",
        "novelty_score": 0.48,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "ensemble",
        "canonical": "Ensemble Learning",
        "aliases": [
          "ensemble"
        ],
        "category": "broad_technical",
        "rationale": "Ensemble Learning is a fundamental concept in machine learning that enhances model performance by combining multiple models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.65,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "whole-slide",
      "internal validation",
      "preliminary test leaderboard"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "YOLOv5",
      "resolved_canonical": "YOLO",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "mitotic figure detection",
      "resolved_canonical": "Mitosis Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "histopathology images",
      "resolved_canonical": "Digital Pathology",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "ensemble",
      "resolved_canonical": "Ensemble Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.65,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Ensemble YOLO Framework for Multi-Domain Mitotic Figure Detection in Histopathology Images

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.02957.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.02957](https://arxiv.org/abs/2509.02957)

## 🔗 유사한 논문
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (88.3% similar)
- [[2025-09-23/Parameter-efficient fine-tuning (PEFT) of Vision Foundation Models for Atypical Mitotic Figure Classification_20250923|Parameter-efficient fine-tuning (PEFT) of Vision Foundation Models for Atypical Mitotic Figure Classification]] (87.1% similar)
- [[2025-09-23/MS-YOLO_ A Multi-Scale Model for Accurate and Efficient Blood Cell Detection_20250923|MS-YOLO: A Multi-Scale Model for Accurate and Efficient Blood Cell Detection]] (87.0% similar)
- [[2025-09-22/MIDOG 2025_ Mitotic Figure Detection with Attention-Guided False Positive Correction_20250922|MIDOG 2025: Mitotic Figure Detection with Attention-Guided False Positive Correction]] (86.3% similar)
- [[2025-09-23/Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology_20250923|Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology]] (85.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Digital Pathology|Digital Pathology]], [[keywords/Ensemble Learning|Ensemble Learning]]
**🔗 Specific Connectable**: [[keywords/YOLO|YOLO]]
**⚡ Unique Technical**: [[keywords/Mitosis Detection|Mitosis Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.02957v2 Announce Type: replace-cross 
Abstract: The reliable identification of mitotic figures in whole-slide histopathological images remains difficult, owing to their low prevalence, substantial morphological heterogeneity, and the inconsistencies introduced by tissue processing and staining procedures. The MIDOG competition series provides standardized benchmarks for evaluating detection approaches across diverse domains, thus motivating the development of generalizable deep learning models. In this work, we investigate the performance of two modern one-stage detectors, YOLOv5 and YOLOv8, trained on MIDOG++, CMC, and CCMCT datasets. To enhance robustness, training incorporated stain-invariant color perturbations and texture-preserving augmentations. Ininternal validation, YOLOv5 achieved higher precision (84.3%), while YOLOv8 offered improved recall (82.6%), reflecting architectural trade-offs between anchor-based and anchor-free detections. To capitalize on their complementary strengths, weemployed an ensemble of the two models, which improved sensitivity (85.3%) while maintaining competitive precision, yielding the best F1 score of 83.1%. On the preliminary MIDOG 2025 test leaderboard, our ensemble ranked 5th with an F1 score of 79.2%, precision of 73.6%, and recall of 85.8%, confirming that the proposed strategy generalizes effectively across unseen test data. These findings highlight the effectiveness of combining anchor-based and anchor-free object detectors to advance automated mitosis detection in digital pathology.

## 📝 요약

이 논문은 전체 슬라이드 병리 이미지에서 유사분열 형상을 신뢰성 있게 식별하는 문제를 다룹니다. 연구에서는 MIDOG++ 등 다양한 데이터셋을 활용하여 YOLOv5와 YOLOv8 두 가지 최신 탐지기를 평가했습니다. 색상 및 질감 변형을 통한 데이터 증강을 적용하여 모델의 강건성을 높였습니다. YOLOv5는 높은 정밀도(84.3%)를, YOLOv8은 높은 재현율(82.6%)을 보여 각각의 탐지 방식의 장단점을 확인했습니다. 두 모델을 앙상블하여 민감도를 85.3%로 개선하고, F1 점수 83.1%를 달성했습니다. MIDOG 2025 테스트에서 앙상블 모델은 F1 점수 79.2%로 5위를 기록하며, 제안된 전략이 새로운 데이터에서도 효과적임을 입증했습니다. 연구는 앵커 기반 및 앵커 프리 탐지기의 결합이 디지털 병리학에서 자동 유사분열 탐지를 향상시킬 수 있음을 강조합니다.

## 🎯 주요 포인트

- 1. 전 슬라이드 병리 이미지에서 유사분열 형상의 신뢰할 수 있는 식별은 여전히 어려운 과제입니다.
- 2. MIDOG 대회는 다양한 도메인에서 검출 접근 방식을 평가하기 위한 표준화된 벤치마크를 제공합니다.
- 3. YOLOv5는 높은 정밀도(84.3%)를, YOLOv8은 향상된 재현율(82.6%)을 보여주며, 두 모델의 상호 보완적인 강점을 활용한 앙상블이 최상의 F1 점수(83.1%)를 기록했습니다.
- 4. 제안된 전략은 미도그 2025 테스트 리더보드에서 5위를 차지하며, 보지 않은 테스트 데이터에서도 효과적으로 일반화됨을 확인했습니다.
- 5. 앵커 기반 및 앵커 프리 객체 검출기를 결합하는 것이 디지털 병리학에서 자동화된 유사분열 검출을 발전시키는 데 효과적임을 강조합니다.


---

*Generated on 2025-09-24 05:36:44*