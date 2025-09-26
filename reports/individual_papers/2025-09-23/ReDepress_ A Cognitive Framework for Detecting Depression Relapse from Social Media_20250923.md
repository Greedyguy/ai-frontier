---
keywords:
  - Transformer
  - Cognitive Theories of Depression
  - Attention Mechanism
  - Depression Relapse Detection
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17991
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:14:55.349766",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Cognitive Theories of Depression",
    "Attention Mechanism",
    "Depression Relapse Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.78,
    "Cognitive Theories of Depression": 0.79,
    "Attention Mechanism": 0.81,
    "Depression Relapse Detection": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer-based temporal models",
        "canonical": "Transformer",
        "aliases": [
          "Transformer models",
          "Transformer architecture"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a key technology in the paper's methodology, linking to broader technical discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Cognitive theories of depression",
        "canonical": "Cognitive Theories of Depression",
        "aliases": [
          "Cognitive depression models",
          "Depression cognitive framework"
        ],
        "category": "unique_technical",
        "rationale": "This represents a unique integration of cognitive psychology with computational methods, enhancing interdisciplinary links.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Attention bias",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention bias in depression",
          "Cognitive attention bias"
        ],
        "category": "specific_connectable",
        "rationale": "Attention bias is a specific cognitive construct relevant to both depression studies and machine learning models.",
        "novelty_score": 0.58,
        "connectivity_score": 0.84,
        "specificity_score": 0.77,
        "link_intent_score": 0.81
      },
      {
        "surface": "Depression relapse detection",
        "canonical": "Depression Relapse Detection",
        "aliases": [
          "Relapse detection",
          "Depression recurrence detection"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel application area within mental health analytics, offering new research and intervention pathways.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer-based temporal models",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Cognitive theories of depression",
      "resolved_canonical": "Cognitive Theories of Depression",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Attention bias",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.84,
        "specificity": 0.77,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Depression relapse detection",
      "resolved_canonical": "Depression Relapse Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# ReDepress: A Cognitive Framework for Detecting Depression Relapse from Social Media

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17991.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17991](https://arxiv.org/abs/2509.17991)

## 🔗 유사한 논문
- [[2025-09-22/A Weak Supervision Approach for Monitoring Recreational Drug Use Effects in Social Media_20250922|A Weak Supervision Approach for Monitoring Recreational Drug Use Effects in Social Media]] (79.4% similar)
- [[2025-09-23/Multi-View Attention Multiple-Instance Learning Enhanced by LLM Reasoning for Cognitive Distortion Detection_20250923|Multi-View Attention Multiple-Instance Learning Enhanced by LLM Reasoning for Cognitive Distortion Detection]] (78.3% similar)
- [[2025-09-22/A Layered Multi-Expert Framework for Long-Context Mental Health Assessments_20250922|A Layered Multi-Expert Framework for Long-Context Mental Health Assessments]] (78.3% similar)
- [[2025-09-22/Predicting the descent into extremism and terrorism_20250922|Predicting the descent into extremism and terrorism]] (77.6% similar)
- [[2025-09-22/RAVE_ Retrieval and Scoring Aware Verifiable Claim Detection_20250922|RAVE: Retrieval and Scoring Aware Verifiable Claim Detection]] (77.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Cognitive Theories of Depression|Cognitive Theories of Depression]], [[keywords/Depression Relapse Detection|Depression Relapse Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17991v1 Announce Type: cross 
Abstract: Almost 50% depression patients face the risk of going into relapse. The risk increases to 80% after the second episode of depression. Although, depression detection from social media has attained considerable attention, depression relapse detection has remained largely unexplored due to the lack of curated datasets and the difficulty of distinguishing relapse and non-relapse users. In this work, we present ReDepress, the first clinically validated social media dataset focused on relapse, comprising 204 Reddit users annotated by mental health professionals. Unlike prior approaches, our framework draws on cognitive theories of depression, incorporating constructs such as attention bias, interpretation bias, memory bias and rumination into both annotation and modeling. Through statistical analyses and machine learning experiments, we demonstrate that cognitive markers significantly differentiate relapse and non-relapse groups, and that models enriched with these features achieve competitive performance, with transformer-based temporal models attaining an F1 of 0.86. Our findings validate psychological theories in real-world textual data and underscore the potential of cognitive-informed computational methods for early relapse detection, paving the way for scalable, low-cost interventions in mental healthcare.

## 📝 요약

이 연구는 우울증 재발 탐지를 위한 첫 번째 임상 검증 소셜 미디어 데이터셋인 ReDepress를 소개합니다. 204명의 Reddit 사용자가 정신 건강 전문가에 의해 주석 처리되었으며, 인지 이론을 활용하여 주의 편향, 해석 편향, 기억 편향 및 반추와 같은 개념을 주석 및 모델링에 통합했습니다. 통계 분석과 기계 학습 실험을 통해 인지적 지표가 재발 및 비재발 그룹을 유의미하게 구분하며, 이러한 특징을 포함한 모델이 F1 점수 0.86을 달성하는 경쟁력 있는 성능을 보임을 확인했습니다. 이 연구는 심리학 이론을 실제 텍스트 데이터에 검증하고, 인지 기반 계산 방법이 초기 재발 탐지에 유용함을 강조하여 정신 건강 관리의 저비용 개입 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 우울증 재발 위험은 첫 번째 에피소드 후 50%에서 두 번째 에피소드 후 80%로 증가합니다.
- 2. ReDepress는 재발에 초점을 맞춘 최초의 임상적으로 검증된 소셜 미디어 데이터셋으로, 정신 건강 전문가가 주석을 단 204명의 Reddit 사용자로 구성되어 있습니다.
- 3. 이 연구는 주의 편향, 해석 편향, 기억 편향 및 반추와 같은 인지적 이론을 주석 및 모델링에 통합하여 재발과 비재발 그룹을 구분하는 데 유의미한 인지적 마커를 발견했습니다.
- 4. 인지적 특징을 포함한 모델은 경쟁력 있는 성능을 보였으며, 특히 트랜스포머 기반의 시간적 모델은 F1 점수 0.86을 달성했습니다.
- 5. 이 연구는 심리학 이론을 실제 텍스트 데이터에서 검증하고, 인지적 정보를 활용한 컴퓨팅 방법이 조기 재발 탐지에 유망하다는 것을 강조합니다.


---

*Generated on 2025-09-24 00:14:55*