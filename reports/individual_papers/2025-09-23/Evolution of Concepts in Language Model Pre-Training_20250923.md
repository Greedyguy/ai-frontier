---
keywords:
  - Large Language Model
  - Transformer
  - Crosscoders
  - Feature Evolution
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17196
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:48:05.944934",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Transformer",
    "Crosscoders",
    "Feature Evolution"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Transformer": 0.8,
    "Crosscoders": 0.7,
    "Feature Evolution": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LM",
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on pre-training and feature evolution.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Key architecture discussed in relation to feature learning phases.",
        "novelty_score": 0.3,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "crosscoders",
        "canonical": "Crosscoders",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Specific method introduced for tracking feature evolution.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "feature evolution",
        "canonical": "Feature Evolution",
        "aliases": [
          "feature dynamics"
        ],
        "category": "unique_technical",
        "rationale": "Describes the process observed and analyzed in the study.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "pre-training",
      "snapshot",
      "black box"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "crosscoders",
      "resolved_canonical": "Crosscoders",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "feature evolution",
      "resolved_canonical": "Feature Evolution",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Evolution of Concepts in Language Model Pre-Training

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17196.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17196](https://arxiv.org/abs/2509.17196)

## 🔗 유사한 논문
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (82.0% similar)
- [[2025-09-17/Language models' activations linearly encode training-order recency_20250917|Language models' activations linearly encode training-order recency]] (81.9% similar)
- [[2025-09-23/Rethinking the Role of Text Complexity in Language Model Pretraining_20250923|Rethinking the Role of Text Complexity in Language Model Pretraining]] (81.2% similar)
- [[2025-09-22/Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation_20250922|Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation]] (81.1% similar)
- [[2025-09-22/Modeling Transformers as complex networks to analyze learning dynamics_20250922|Modeling Transformers as complex networks to analyze learning dynamics]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/Crosscoders|Crosscoders]], [[keywords/Feature Evolution|Feature Evolution]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17196v1 Announce Type: cross 
Abstract: Language models obtain extensive capabilities through pre-training. However, the pre-training process remains a black box. In this work, we track linear interpretable feature evolution across pre-training snapshots using a sparse dictionary learning method called crosscoders. We find that most features begin to form around a specific point, while more complex patterns emerge in later training stages. Feature attribution analyses reveal causal connections between feature evolution and downstream performance. Our feature-level observations are highly consistent with previous findings on Transformer's two-stage learning process, which we term a statistical learning phase and a feature learning phase. Our work opens up the possibility to track fine-grained representation progress during language model learning dynamics.

## 📝 요약

이 논문은 언어 모델의 사전 훈련 과정을 분석하기 위해 희소 사전 학습 방법인 crosscoders를 사용하여 선형 해석 가능한 특징의 진화를 추적합니다. 연구 결과, 대부분의 특징은 특정 시점에서 형성되기 시작하며, 복잡한 패턴은 훈련 후반부에 나타납니다. 특징 귀속 분석을 통해 특징 진화와 다운스트림 성능 간의 인과 관계를 밝혀냈습니다. 이러한 특징 수준의 관찰은 Transformer의 두 단계 학습 과정인 통계적 학습 단계와 특징 학습 단계와 일치합니다. 이 연구는 언어 모델 학습의 세밀한 표현 진행을 추적할 수 있는 가능성을 열어줍니다.

## 🎯 주요 포인트

- 1. 언어 모델은 사전 훈련을 통해 광범위한 능력을 얻지만, 그 과정은 여전히 블랙박스로 남아 있다.
- 2. 본 연구에서는 crosscoders라는 희소 사전 학습 방법을 사용하여 사전 훈련 스냅샷 간의 선형 해석 가능한 특징 진화를 추적한다.
- 3. 대부분의 특징은 특정 시점에서 형성되기 시작하며, 더 복잡한 패턴은 훈련 후반 단계에서 나타난다.
- 4. 특징 귀속 분석을 통해 특징 진화와 다운스트림 성능 간의 인과 관계를 밝혀낸다.
- 5. 본 연구는 언어 모델 학습 과정에서 세밀한 표현의 발전을 추적할 수 있는 가능성을 열어준다.


---

*Generated on 2025-09-23 23:48:05*