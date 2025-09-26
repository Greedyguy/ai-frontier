<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:27:27.313997",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Machine Learning Model Description",
    "Semantics Preservation",
    "European Union Aviation Safety Agency"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.9,
    "Machine Learning Model Description": 0.7,
    "Semantics Preservation": 0.72,
    "European Union Aviation Safety Agency": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "ML"
        ],
        "category": "broad_technical",
        "rationale": "Machine Learning is a fundamental concept in the paper and links to a wide range of related topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.95,
        "specificity_score": 0.5,
        "link_intent_score": 0.9
      },
      {
        "surface": "Machine Learning Model Description",
        "canonical": "Machine Learning Model Description",
        "aliases": [
          "MLMD"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique concept introduced in the paper to differentiate between models and their descriptions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Semantics Preservation",
        "canonical": "Semantics Preservation",
        "aliases": [
          "Semantic Integrity"
        ],
        "category": "unique_technical",
        "rationale": "Semantics Preservation is crucial for ensuring model accuracy and is a key focus of the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      },
      {
        "surface": "European Union Aviation Safety Agency",
        "canonical": "European Union Aviation Safety Agency",
        "aliases": [
          "EASA"
        ],
        "category": "specific_connectable",
        "rationale": "EASA is a regulatory body relevant to the compliance aspects discussed in the paper.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "airborne systems",
      "training performance",
      "target environment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.95,
        "specificity": 0.5,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Machine Learning Model Description",
      "resolved_canonical": "Machine Learning Model Description",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Semantics Preservation",
      "resolved_canonical": "Semantics Preservation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "European Union Aviation Safety Agency",
      "resolved_canonical": "European Union Aviation Safety Agency",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Implementation of airborne ML models with semantics preservation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18681.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18681](https://arxiv.org/abs/2509.18681)

## 🔗 유사한 논문
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (82.0% similar)
- [[2025-09-23/SafeEraser_ Enhancing Safety in Multimodal Large Language Models through Multimodal Machine Unlearning_20250923|SafeEraser: Enhancing Safety in Multimodal Large Language Models through Multimodal Machine Unlearning]] (81.9% similar)
- [[2025-09-23/System-Level Uncertainty Quantification with Multiple Machine Learning Models_ A Theoretical Framework_20250923|System-Level Uncertainty Quantification with Multiple Machine Learning Models: A Theoretical Framework]] (81.8% similar)
- [[2025-09-22/Activation Space Interventions Can Be Transferred Between Large Language Models_20250922|Activation Space Interventions Can Be Transferred Between Large Language Models]] (81.0% similar)
- [[2025-09-23/Automating Steering for Safe Multimodal Large Language Models_20250923|Automating Steering for Safe Multimodal Large Language Models]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]]
**🔗 Specific Connectable**: [[keywords/European Union Aviation Safety Agency|European Union Aviation Safety Agency]]
**⚡ Unique Technical**: [[keywords/Machine Learning Model Description|Machine Learning Model Description]], [[keywords/Semantics Preservation|Semantics Preservation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18681v1 Announce Type: new 
Abstract: Machine Learning (ML) may offer new capabilities in airborne systems. However, as any piece of airborne systems, ML-based systems will be required to guarantee their safe operation. Thus, their development will have to be demonstrated to be compliant with the adequate guidance. So far, the European Union Aviation Safety Agency (EASA) has published a concept paper and an EUROCAE/SAE group is preparing ED-324. Both approaches delineate high-level objectives to confirm the ML model achieves its intended function and maintains training performance in the target environment. The paper aims to clarify the difference between an ML model and its corresponding unambiguous description, referred to as the Machine Learning Model Description (MLMD). It then refines the essential notion of semantics preservation to ensure the accurate replication of the model. We apply our contributions to several industrial use cases to build and compare several target models.

## 📝 요약

이 논문은 항공 시스템에서 머신 러닝(ML)의 안전한 운영을 보장하기 위한 개발 기준을 다룹니다. 유럽연합항공안전청(EASA)와 EUROCAE/SAE 그룹의 지침을 바탕으로 ML 모델이 의도된 기능을 수행하고 목표 환경에서의 성능을 유지하는지 확인하는 목표를 설정합니다. 논문은 ML 모델과 그에 대한 명확한 설명인 머신 러닝 모델 설명(MLMD)의 차이를 명확히 하고, 모델의 정확한 복제를 위한 의미 보존의 개념을 세분화합니다. 이러한 기여를 여러 산업 사례에 적용하여 다양한 목표 모델을 구축하고 비교합니다.

## 🎯 주요 포인트

- 1. 기계 학습(ML)은 항공 시스템에서 새로운 기능을 제공할 수 있지만, 안전한 운영을 보장하기 위해 적절한 지침을 준수해야 한다.
- 2. 유럽연합항공안전청(EASA)은 ML 기반 시스템의 안전성을 위한 개념 문서를 발표했으며, EUROCAE/SAE 그룹은 ED-324를 준비 중이다.
- 3. 논문은 ML 모델과 그에 상응하는 명확한 설명인 기계 학습 모델 설명(MLMD)의 차이를 명확히 하고자 한다.
- 4. 모델의 정확한 복제를 보장하기 위해 의미 보존의 필수 개념을 정제한다.
- 5. 여러 산업적 사용 사례에 우리의 기여를 적용하여 여러 목표 모델을 구축하고 비교한다.


---

*Generated on 2025-09-24 13:27:27*