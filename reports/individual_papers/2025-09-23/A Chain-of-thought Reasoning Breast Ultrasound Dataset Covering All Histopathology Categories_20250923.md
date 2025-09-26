---
keywords:
  - Breast Ultrasound
  - Chain-of-thought Reasoning
  - Histopathology Categories
  - AI Development
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17046
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:42:21.409795",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Breast Ultrasound",
    "Chain-of-thought Reasoning",
    "Histopathology Categories",
    "AI Development"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Breast Ultrasound": 0.8,
    "Chain-of-thought Reasoning": 0.85,
    "Histopathology Categories": 0.7,
    "AI Development": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Breast Ultrasound",
        "canonical": "Breast Ultrasound",
        "aliases": [
          "BUS"
        ],
        "category": "unique_technical",
        "rationale": "Breast Ultrasound is a specific imaging technique crucial for linking datasets and AI applications in medical imaging.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Chain-of-thought Reasoning",
        "canonical": "Chain-of-thought Reasoning",
        "aliases": [
          "CoT Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Chain-of-thought Reasoning is a novel approach in AI that enhances understanding and decision-making processes.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Histopathology Categories",
        "canonical": "Histopathology Categories",
        "aliases": [
          "Histopathology Types"
        ],
        "category": "unique_technical",
        "rationale": "Covering all histopathology categories is significant for comprehensive medical datasets and AI training.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "AI Development",
        "canonical": "AI Development",
        "aliases": [
          "Artificial Intelligence Development"
        ],
        "category": "broad_technical",
        "rationale": "AI Development is a broad technical area that connects various AI applications and advancements.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "images",
      "patients"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Breast Ultrasound",
      "resolved_canonical": "Breast Ultrasound",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Chain-of-thought Reasoning",
      "resolved_canonical": "Chain-of-thought Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Histopathology Categories",
      "resolved_canonical": "Histopathology Categories",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "AI Development",
      "resolved_canonical": "AI Development",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# A Chain-of-thought Reasoning Breast Ultrasound Dataset Covering All Histopathology Categories

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17046.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17046](https://arxiv.org/abs/2509.17046)

## 🔗 유사한 논문
- [[2025-09-22/From Data to Diagnosis_ A Large, Comprehensive Bone Marrow Dataset and AI Methods for Childhood Leukemia Prediction_20250922|From Data to Diagnosis: A Large, Comprehensive Bone Marrow Dataset and AI Methods for Childhood Leukemia Prediction]] (78.9% similar)
- [[2025-09-18/Uni-cot_ Towards Unified Chain-of-Thought Reasoning Across Text and Vision_20250918|Uni-cot: Towards Unified Chain-of-Thought Reasoning Across Text and Vision]] (78.4% similar)
- [[2025-09-22/Data-Efficient Learning for Generalizable Surgical Video Understanding_20250922|Data-Efficient Learning for Generalizable Surgical Video Understanding]] (78.1% similar)
- [[2025-09-22/Screener_ Self-supervised Pathology Segmentation in Medical CT Images_20250922|Screener: Self-supervised Pathology Segmentation in Medical CT Images]] (77.5% similar)
- [[2025-09-23/Breast Cancer Classification Using Gradient Boosting Algorithms Focusing on Reducing the False Negative and SHAP for Explainability_20250923|Breast Cancer Classification Using Gradient Boosting Algorithms Focusing on Reducing the False Negative and SHAP for Explainability]] (77.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/AI Development|AI Development]]
**⚡ Unique Technical**: [[keywords/Breast Ultrasound|Breast Ultrasound]], [[keywords/Chain-of-thought Reasoning|Chain-of-thought Reasoning]], [[keywords/Histopathology Categories|Histopathology Categories]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17046v1 Announce Type: cross 
Abstract: Breast ultrasound (BUS) is an essential tool for diagnosing breast lesions, with millions of examinations per year. However, publicly available high-quality BUS benchmarks for AI development are limited in data scale and annotation richness. In this work, we present BUS-CoT, a BUS dataset for chain-of-thought (CoT) reasoning analysis, which contains 11,439 images of 10,019 lesions from 4,838 patients and covers all 99 histopathology types. To facilitate research on incentivizing CoT reasoning, we construct the reasoning processes based on observation, feature, diagnosis and pathology labels, annotated and verified by experienced experts. Moreover, by covering lesions of all histopathology types, we aim to facilitate robust AI systems in rare cases, which can be error-prone in clinical practice.

## 📝 요약

이 논문은 유방 초음파(BUS) 영상 분석을 위한 데이터셋인 BUS-CoT를 소개합니다. 이 데이터셋은 4,838명의 환자로부터 수집된 10,019개의 병변을 포함한 11,439장의 이미지를 제공하며, 99가지 병리 유형을 모두 다룹니다. 저자들은 관찰, 특징, 진단 및 병리 레이블에 기반한 체계적인 추론 과정을 구축하여 체인 오브 쏘트(CoT) 추론 연구를 촉진하고자 합니다. 이 데이터셋은 드문 병리 유형을 포함하여 임상 실습에서 오류가 발생할 수 있는 경우에도 견고한 AI 시스템 개발을 지원하는 것을 목표로 합니다.

## 🎯 주요 포인트

- 1. BUS-CoT는 4,838명의 환자로부터 10,019개의 병변을 포함한 11,439개의 이미지를 제공하는 유방 초음파 데이터셋입니다.
- 2. 이 데이터셋은 관찰, 특징, 진단 및 병리학 레이블에 기반한 체계적인 사고 과정 분석을 위해 설계되었습니다.
- 3. 모든 99가지 병리학 유형의 병변을 포함하여 드문 경우에도 강력한 AI 시스템 개발을 목표로 합니다.
- 4. 데이터셋의 주석과 검증은 경험이 풍부한 전문가들에 의해 이루어졌습니다.
- 5. AI 개발을 위한 고품질의 유방 초음파 벤치마크 데이터셋의 부족 문제를 해결하고자 합니다.


---

*Generated on 2025-09-23 23:42:21*