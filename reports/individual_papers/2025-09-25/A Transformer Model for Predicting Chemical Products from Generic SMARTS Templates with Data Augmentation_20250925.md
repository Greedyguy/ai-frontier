---
keywords:
  - Transformer
  - ProPreT5
  - SMARTS Templates
  - Data Augmentation
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2503.05810
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:20:29.884616",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "ProPreT5",
    "SMARTS Templates",
    "Data Augmentation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "ProPreT5": 0.8,
    "SMARTS Templates": 0.78,
    "Data Augmentation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer Model",
        "canonical": "Transformer",
        "aliases": [
          "Transformer Architecture"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are foundational in modern machine learning, linking to a wide range of applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "ProPreT5",
        "canonical": "ProPreT5",
        "aliases": [
          "ProPreT5 Model"
        ],
        "category": "unique_technical",
        "rationale": "ProPreT5 is a novel adaptation of T5 for chemistry, offering unique insights into template-based reaction prediction.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "SMARTS Templates",
        "canonical": "SMARTS Templates",
        "aliases": [
          "SMARTS Pattern"
        ],
        "category": "specific_connectable",
        "rationale": "SMARTS templates are critical for describing chemical substructures, facilitating connections in computational chemistry.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Data Augmentation",
        "canonical": "Data Augmentation",
        "aliases": [
          "Augmentation Strategy"
        ],
        "category": "specific_connectable",
        "rationale": "Data augmentation enhances model generalization, a key concept in improving predictive performance.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "chemical reaction outcomes",
      "reaction prediction",
      "computational chemistry"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer Model",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "ProPreT5",
      "resolved_canonical": "ProPreT5",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "SMARTS Templates",
      "resolved_canonical": "SMARTS Templates",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Data Augmentation",
      "resolved_canonical": "Data Augmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# A Transformer Model for Predicting Chemical Products from Generic SMARTS Templates with Data Augmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2503.05810.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2503.05810](https://arxiv.org/abs/2503.05810)

## 🔗 유사한 논문
- [[2025-09-22/DeepMech_ A Machine Learning Framework for Chemical Reaction Mechanism Prediction_20250922|DeepMech: A Machine Learning Framework for Chemical Reaction Mechanism Prediction]] (81.0% similar)
- [[2025-09-23/Test-Time Training Scaling Laws for Chemical Exploration in Drug Design_20250923|Test-Time Training Scaling Laws for Chemical Exploration in Drug Design]] (79.5% similar)
- [[2025-09-19/SMART_ Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction_20250919|SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction]] (78.6% similar)
- [[2025-09-23/Efficient Transition State Searches by Freezing String Method with Graph Neural Network Potentials_20250923|Efficient Transition State Searches by Freezing String Method with Graph Neural Network Potentials]] (78.5% similar)
- [[2025-09-22/FragmentRetro_ A Quadratic Retrosynthetic Method Based on Fragmentation Algorithms_20250922|FragmentRetro: A Quadratic Retrosynthetic Method Based on Fragmentation Algorithms]] (78.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/SMARTS Templates|SMARTS Templates]], [[keywords/Data Augmentation|Data Augmentation]]
**⚡ Unique Technical**: [[keywords/ProPreT5|ProPreT5]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.05810v3 Announce Type: replace-cross 
Abstract: The accurate prediction of chemical reaction outcomes is a major challenge in computational chemistry. Current models rely heavily on either highly specific reaction templates or template-free methods, both of which present limitations. To address these, this work proposes the Broad Reaction Set (BRS), a set featuring 20 generic reaction templates written in SMARTS, a pattern-based notation designed to describe substructures and reactivity. Additionally, we introduce ProPreT5, a T5-based model specifically adapted for chemistry and, to the best of our knowledge, the first language model capable of directly handling and applying SMARTS reaction templates. To further improve generalization, we propose the first augmentation strategy for SMARTS, which injects structural diversity at the pattern level. Trained on augmented templates, ProPreT5 demonstrates strong predictive performance and generalization to unseen reactions. Together, these contributions provide a novel and practical alternative to current methods, advancing the field of template-based reaction prediction.

## 📝 요약

이 연구는 화학 반응 결과 예측의 정확성을 높이기 위해 Broad Reaction Set (BRS)와 ProPreT5 모델을 제안합니다. BRS는 20개의 일반적인 반응 템플릿으로 구성되어 있으며, SMARTS 표기법을 사용하여 반응성을 설명합니다. ProPreT5는 화학에 특화된 T5 기반 모델로, SMARTS 반응 템플릿을 직접 처리할 수 있는 최초의 언어 모델입니다. 또한, SMARTS의 구조적 다양성을 높이기 위한 첫 번째 증강 전략을 제안하여 모델의 일반화 능력을 향상시켰습니다. 증강된 템플릿으로 학습된 ProPreT5는 뛰어난 예측 성능과 미지의 반응에 대한 일반화 능력을 보여주며, 이는 기존 방법에 대한 실용적인 대안을 제공합니다.

## 🎯 주요 포인트

- 1. Broad Reaction Set (BRS)는 20개의 일반적인 반응 템플릿을 포함하며, SMARTS 표기법을 사용하여 반응성을 설명합니다.
- 2. ProPreT5는 화학에 특화된 T5 기반 모델로, SMARTS 반응 템플릿을 직접 처리하고 적용할 수 있는 최초의 언어 모델입니다.
- 3. SMARTS의 일반화를 위해 패턴 수준에서 구조적 다양성을 추가하는 첫 번째 증강 전략을 제안합니다.
- 4. 증강된 템플릿으로 학습된 ProPreT5는 보지 못한 반응에 대한 예측 성능과 일반화 능력이 뛰어납니다.
- 5. 이 연구는 템플릿 기반 반응 예측 분야에 새로운 실용적 대안을 제공하며, 현재 방법을 발전시킵니다.


---

*Generated on 2025-09-25 16:20:29*