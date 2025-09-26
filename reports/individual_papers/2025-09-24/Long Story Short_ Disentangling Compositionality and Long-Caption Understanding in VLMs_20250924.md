<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:18:42.504095",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Compositionality",
    "Long-Caption Understanding",
    "Object-Attribute Binding",
    "Data Quality"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Compositionality": 0.78,
    "Long-Caption Understanding": 0.8,
    "Object-Attribute Binding": 0.72,
    "Data Quality": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's exploration of compositionality and long-caption understanding, making them a key concept for linking.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Compositionality",
        "canonical": "Compositionality",
        "aliases": [
          "Compositional Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Compositionality is a unique technical focus of the paper, crucial for understanding the interaction with long-caption understanding.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Long-Caption Understanding",
        "canonical": "Long-Caption Understanding",
        "aliases": [
          "Dense Caption Understanding"
        ],
        "category": "unique_technical",
        "rationale": "Long-Caption Understanding is a specific challenge addressed in the paper, relevant for linking to related research in vision-language tasks.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Object-Attribute Binding",
        "canonical": "Object-Attribute Binding",
        "aliases": [
          "Attribute Binding"
        ],
        "category": "unique_technical",
        "rationale": "Object-Attribute Binding is a specific aspect of compositionality discussed in the paper, important for linking to related cognitive and computational models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Data Quality",
        "canonical": "Data Quality",
        "aliases": [
          "Dataset Quality"
        ],
        "category": "broad_technical",
        "rationale": "Data Quality is highlighted as a critical factor affecting model performance, relevant for linking to discussions on dataset curation and model training.",
        "novelty_score": 0.3,
        "connectivity_score": 0.82,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Compositionality",
      "resolved_canonical": "Compositionality",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Long-Caption Understanding",
      "resolved_canonical": "Long-Caption Understanding",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Object-Attribute Binding",
      "resolved_canonical": "Object-Attribute Binding",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Data Quality",
      "resolved_canonical": "Data Quality",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.82,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Long Story Short: Disentangling Compositionality and Long-Caption Understanding in VLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19207.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2509.19207](https://arxiv.org/abs/2509.19207)

## 🔗 유사한 논문
- [[2025-09-24/Reading Images Like Texts_ Sequential Image Understanding in Vision-Language Models_20250924|Reading Images Like Texts: Sequential Image Understanding in Vision-Language Models]] (86.5% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (83.9% similar)
- [[2025-09-22/Robust Vision-Language Models via Tensor Decomposition_ A Defense Against Adversarial Attacks_20250922|Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks]] (83.1% similar)
- [[2025-09-22/Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models_20250922|Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models]] (82.6% similar)
- [[2025-09-24/Vision-Free Retrieval_ Rethinking Multimodal Search with Textual Scene Descriptions_20250924|Vision-Free Retrieval: Rethinking Multimodal Search with Textual Scene Descriptions]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Data Quality|Data Quality]]
**⚡ Unique Technical**: [[keywords/Compositionality|Compositionality]], [[keywords/Long-Caption Understanding|Long-Caption Understanding]], [[keywords/Object-Attribute Binding|Object-Attribute Binding]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19207v1 Announce Type: new 
Abstract: Contrastive vision-language models (VLMs) have made significant progress in binding visual and textual information, but understanding long, dense captions remains an open challenge. We hypothesize that compositionality, the capacity to reason about object-attribute bindings and inter-object relationships, is key to understanding longer captions. In this paper, we investigate the interaction between compositionality and long-caption understanding, asking whether training for one property enhances the other. We train and evaluate a range of models that target each of these capabilities. Our results reveal a bidirectional relationship: compositional training improves performance on long-caption retrieval, and training on long captions promotes compositionality. However, these gains are sensitive to data quality and model design. We find that training on poorly structured captions, or with limited parameter updates, fails to support generalization. Likewise, strategies that aim at retaining general alignment, such as freezing positional embeddings, do not improve compositional understanding. Overall, we find that compositional understanding and long-caption understanding are intertwined capabilities that can be jointly learned through training on dense, grounded descriptions. Despite these challenges, we show that models trained on high-quality, long-caption data can achieve strong performance in both tasks, offering practical guidance for improving VLM generalization.

## 📝 요약

대조적 비전-언어 모델(VLM)은 시각적 및 텍스트 정보를 결합하는 데 진전을 이루었지만, 긴 캡션을 이해하는 데는 여전히 어려움이 있습니다. 본 연구는 객체 속성 결합 및 객체 간 관계를 추론하는 능력인 구성성이 긴 캡션 이해에 중요하다고 가정하고, 두 가지 능력 간의 상호작용을 조사했습니다. 연구 결과, 구성성 훈련이 긴 캡션 검색 성능을 향상시키고, 긴 캡션 훈련이 구성성을 촉진하는 상호 관계를 발견했습니다. 그러나 이러한 성과는 데이터 품질과 모델 설계에 민감하게 영향을 받습니다. 구조가 잘못된 캡션이나 제한된 매개변수 업데이트로 훈련할 경우 일반화에 실패하며, 위치 임베딩을 고정하는 전략도 구성성 이해를 개선하지 못했습니다. 고품질의 긴 캡션 데이터를 사용한 훈련은 두 가지 과제에서 강력한 성능을 달성할 수 있으며, VLM 일반화 개선을 위한 실질적인 지침을 제공합니다.

## 🎯 주요 포인트

- 1. 대조적 비전-언어 모델(VLMs)은 시각적 및 텍스트 정보를 결합하는 데 진전을 이루었지만, 긴 캡션을 이해하는 것은 여전히 도전 과제입니다.
- 2. 본 연구는 객체-속성 결합 및 객체 간 관계에 대한 추론 능력인 구성성이 긴 캡션 이해의 핵심이라고 가정합니다.
- 3. 구성성 훈련은 긴 캡션 검색 성능을 향상시키고, 긴 캡션 훈련은 구성성을 촉진하는 양방향 관계가 있음을 발견했습니다.
- 4. 데이터 품질과 모델 설계에 따라 이러한 성과가 민감하게 변하며, 구조가 잘못된 캡션이나 제한된 매개변수 업데이트로는 일반화가 어렵습니다.
- 5. 고품질의 긴 캡션 데이터를 사용한 모델은 두 작업에서 강력한 성능을 발휘할 수 있으며, 이는 VLM 일반화를 개선하기 위한 실질적인 지침을 제공합니다.


---

*Generated on 2025-09-24 16:18:42*