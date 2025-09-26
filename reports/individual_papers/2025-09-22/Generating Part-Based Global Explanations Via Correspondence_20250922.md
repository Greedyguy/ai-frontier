---
keywords:
  - Deep Learning
  - Concept-based Explanations
  - Symbolic Explanations
  - Computer Vision
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15393
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:55:16.594853",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Concept-based Explanations",
    "Symbolic Explanations",
    "Computer Vision"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Concept-based Explanations": 0.78,
    "Symbolic Explanations": 0.77,
    "Computer Vision": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is central to the paper's approach and connects with many related concepts.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Concept-based explanations",
        "canonical": "Concept-based Explanations",
        "aliases": [
          "Concept Explanations"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique approach discussed in the paper, offering a global perspective on model explanations.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Symbolic explanations",
        "canonical": "Symbolic Explanations",
        "aliases": [
          "Symbolic Interpretations"
        ],
        "category": "unique_technical",
        "rationale": "Symbolic explanations are a novel aspect of the paper, providing a human-understandable format.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "Computer Vision",
        "canonical": "Computer Vision",
        "aliases": [
          "CV"
        ],
        "category": "broad_technical",
        "rationale": "The paper's focus on visual explanations aligns with the field of Computer Vision.",
        "novelty_score": 0.25,
        "connectivity_score": 0.85,
        "specificity_score": 0.55,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "approach",
      "images",
      "dataset"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Concept-based explanations",
      "resolved_canonical": "Concept-based Explanations",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Symbolic explanations",
      "resolved_canonical": "Symbolic Explanations",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Computer Vision",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.25,
        "connectivity": 0.85,
        "specificity": 0.55,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Generating Part-Based Global Explanations Via Correspondence

**Korean Title:** 부분 기반 글로벌 설명 생성: 상관관계를 통한 접근

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15393.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15393](https://arxiv.org/abs/2509.15393)

## 🔗 유사한 논문
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (83.6% similar)
- [[2025-09-22/Multi-Modal Interpretability for Enhanced Localization in Vision-Language Models_20250922|Multi-Modal Interpretability for Enhanced Localization in Vision-Language Models]] (82.4% similar)
- [[2025-09-22/GIN-Graph_ A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks_20250922|GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks]] (81.7% similar)
- [[2025-09-22/Shedding Light on Depth_ Explainability Assessment in Monocular Depth Estimation_20250922|Shedding Light on Depth: Explainability Assessment in Monocular Depth Estimation]] (81.5% similar)
- [[2025-09-19/SMARTER_ A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models_20250919|SMARTER: A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]], [[keywords/Computer Vision|Computer Vision]]
**⚡ Unique Technical**: [[keywords/Concept-based Explanations|Concept-based Explanations]], [[keywords/Symbolic Explanations|Symbolic Explanations]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15393v1 Announce Type: cross 
Abstract: Deep learning models are notoriously opaque. Existing explanation methods often focus on localized visual explanations for individual images. Concept-based explanations, while offering global insights, require extensive annotations, incurring significant labeling cost. We propose an approach that leverages user-defined part labels from a limited set of images and efficiently transfers them to a larger dataset. This enables the generation of global symbolic explanations by aggregating part-based local explanations, ultimately providing human-understandable explanations for model decisions on a large scale.

## 🔍 Abstract (한글 번역)

arXiv:2509.15393v1 발표 유형: 교차  
초록: 딥러닝 모델은 대체로 불투명합니다. 기존의 설명 방법은 종종 개별 이미지에 대한 국지적인 시각적 설명에 초점을 맞춥니다. 개념 기반 설명은 전반적인 통찰력을 제공하지만, 광범위한 주석이 필요하여 상당한 라벨링 비용이 발생합니다. 우리는 제한된 수의 이미지에서 사용자 정의 부위 라벨을 활용하고 이를 더 큰 데이터셋으로 효율적으로 전이하는 접근 방식을 제안합니다. 이는 부위 기반의 국지적 설명을 집계하여 전역적인 상징적 설명을 생성할 수 있게 하며, 궁극적으로 대규모로 모델 결정에 대한 인간이 이해할 수 있는 설명을 제공합니다.

## 📝 요약

이 논문은 딥러닝 모델의 불투명성을 해결하기 위해 사용자 정의 부위 레이블을 소수의 이미지에서 대규모 데이터셋으로 효율적으로 전이하는 방법을 제안합니다. 기존의 설명 방법은 개별 이미지에 대한 국소적 시각 설명에 집중하거나, 개념 기반 설명은 광범위한 주석이 필요하여 비용이 많이 듭니다. 제안된 방법은 부위 기반의 국소적 설명을 집계하여 전반적인 상징적 설명을 생성함으로써, 대규모 데이터셋에 대한 모델 결정의 인간 이해 가능한 설명을 제공합니다.

## 🎯 주요 포인트

- 1. 딥러닝 모델의 불투명성을 해결하기 위해 사용자 정의 부위 레이블을 활용하는 접근법을 제안합니다.
- 2. 제한된 이미지 세트에서 사용자 정의 부위 레이블을 대규모 데이터셋으로 효율적으로 전이합니다.
- 3. 부위 기반의 지역적 설명을 집계하여 전역적인 상징적 설명을 생성합니다.
- 4. 제안된 방법은 모델 결정에 대한 인간이 이해할 수 있는 설명을 대규모로 제공합니다.


---

*Generated on 2025-09-23 08:55:16*