---
keywords:
  - Active Learning
  - Table Detection
  - CascadeTabNet
  - YOLO
  - Diversity-based Sampling
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20003
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:56:12.022243",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Active Learning",
    "Table Detection",
    "CascadeTabNet",
    "YOLO",
    "Diversity-based Sampling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Active Learning": 0.85,
    "Table Detection": 0.78,
    "CascadeTabNet": 0.8,
    "YOLO": 0.77,
    "Diversity-based Sampling": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Active Learning",
        "canonical": "Active Learning",
        "aliases": [
          "AL"
        ],
        "category": "specific_connectable",
        "rationale": "Active Learning is a key strategy in reducing annotation costs, making it a crucial concept for linking in machine learning contexts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Table Detection",
        "canonical": "Table Detection",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Table Detection is a specific task within computer vision that is central to the paper's contributions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "CascadeTabNet",
        "canonical": "CascadeTabNet",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "CascadeTabNet is a specific architecture used in the evaluation, providing a direct link to related research in table detection.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "YOLOv9",
        "canonical": "YOLO",
        "aliases": [
          "YOLOv9"
        ],
        "category": "unique_technical",
        "rationale": "YOLOv9 is a state-of-the-art model in object detection, offering strong connectivity to broader discussions in computer vision.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Diversity-based Strategies",
        "canonical": "Diversity-based Sampling",
        "aliases": [
          "Diversity-based Strategies"
        ],
        "category": "specific_connectable",
        "rationale": "Diversity-based Sampling enhances active learning by improving sampling efficiency, making it a valuable concept for linking.",
        "novelty_score": 0.58,
        "connectivity_score": 0.82,
        "specificity_score": 0.76,
        "link_intent_score": 0.79
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
      "candidate_surface": "Active Learning",
      "resolved_canonical": "Active Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Table Detection",
      "resolved_canonical": "Table Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "CascadeTabNet",
      "resolved_canonical": "CascadeTabNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "YOLOv9",
      "resolved_canonical": "YOLO",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Diversity-based Strategies",
      "resolved_canonical": "Diversity-based Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.82,
        "specificity": 0.76,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Table Detection with Active Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20003.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20003](https://arxiv.org/abs/2509.20003)

## 🔗 유사한 논문
- [[2025-09-22/Boosting Active Learning with Knowledge Transfer_20250922|Boosting Active Learning with Knowledge Transfer]] (81.5% similar)
- [[2025-09-23/DCoM_ Active Learning for All Learners_20250923|DCoM: Active Learning for All Learners]] (80.9% similar)
- [[2025-09-19/TableDART_ Dynamic Adaptive Multi-Modal Routing for Table Understanding_20250919|TableDART: Dynamic Adaptive Multi-Modal Routing for Table Understanding]] (80.2% similar)
- [[2025-09-18/Synthetic-to-Real Object Detection using YOLOv11 and Domain Randomization Strategies_20250918|Synthetic-to-Real Object Detection using YOLOv11 and Domain Randomization Strategies]] (80.2% similar)
- [[2025-09-23/LASER_ Stratified Selective Sampling for Instruction Tuning with Dedicated Scoring Strategy_20250923|LASER: Stratified Selective Sampling for Instruction Tuning with Dedicated Scoring Strategy]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Active Learning|Active Learning]], [[keywords/Diversity-based Sampling|Diversity-based Sampling]]
**⚡ Unique Technical**: [[keywords/Table Detection|Table Detection]], [[keywords/CascadeTabNet|CascadeTabNet]], [[keywords/YOLO|YOLO]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20003v1 Announce Type: cross 
Abstract: Efficient data annotation remains a critical challenge in machine learning, particularly for object detection tasks requiring extensive labeled data. Active learning (AL) has emerged as a promising solution to minimize annotation costs by selecting the most informative samples. While traditional AL approaches primarily rely on uncertainty-based selection, recent advances suggest that incorporating diversity-based strategies can enhance sampling efficiency in object detection tasks. Our approach ensures the selection of representative examples that improve model generalization. We evaluate our method on two benchmark datasets (TableBank-LaTeX, TableBank-Word) using state-of-the-art table detection architectures, CascadeTabNet and YOLOv9. Our results demonstrate that AL-based example selection significantly outperforms random sampling, reducing annotation effort given a limited budget while maintaining comparable performance to fully supervised models. Our method achieves higher mAP scores within the same annotation budget.

## 📝 요약

이 논문은 객체 탐지 작업에서 효율적인 데이터 주석의 중요성을 다루며, 주석 비용을 최소화하기 위한 해결책으로 능동 학습(AL)을 제안합니다. 전통적인 AL 방법은 주로 불확실성 기반의 샘플 선택에 의존하지만, 본 연구는 다양성 기반 전략을 통합하여 샘플링 효율성을 높이는 방법을 제안합니다. 이 접근법은 모델의 일반화를 향상시키는 대표적인 예제를 선택합니다. TableBank-LaTeX와 TableBank-Word라는 두 개의 벤치마크 데이터셋을 사용하여 CascadeTabNet과 YOLOv9 아키텍처로 평가한 결과, AL 기반의 예제 선택이 무작위 샘플링보다 주석 노력을 줄이면서도 완전 지도 학습 모델과 유사한 성능을 유지함을 보여주었습니다. 제한된 예산 내에서 더 높은 mAP 점수를 달성했습니다.

## 🎯 주요 포인트

- 1. 효율적인 데이터 주석은 객체 탐지 작업에서 여전히 중요한 도전 과제입니다.
- 2. 능동 학습(AL)은 가장 정보가 많은 샘플을 선택하여 주석 비용을 최소화하는 유망한 솔루션으로 부상하고 있습니다.
- 3. 전통적인 AL 접근법은 주로 불확실성 기반 선택에 의존하지만, 다양성 기반 전략을 통합하면 샘플링 효율성을 향상시킬 수 있습니다.
- 4. 우리의 방법은 모델 일반화를 개선하는 대표적인 예제를 선택하도록 보장합니다.
- 5. AL 기반 예제 선택은 제한된 예산 내에서 주석 노력을 줄이면서 완전 지도 학습 모델과 유사한 성능을 유지합니다.


---

*Generated on 2025-09-25 15:56:12*