---
keywords:
  - Text Complexity
  - Language Model Pretraining
  - Zero-Shot Learning
  - Simplified Texts
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16551
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:25:32.254480",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Text Complexity",
    "Language Model Pretraining",
    "Zero-Shot Learning",
    "Simplified Texts"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Text Complexity": 0.75,
    "Language Model Pretraining": 0.8,
    "Zero-Shot Learning": 0.78,
    "Simplified Texts": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "text complexity",
        "canonical": "Text Complexity",
        "aliases": [
          "complexity of text",
          "reading difficulty"
        ],
        "category": "unique_technical",
        "rationale": "Text complexity is central to the study and impacts language model performance, making it a unique technical concept.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "language model pretraining",
        "canonical": "Language Model Pretraining",
        "aliases": [
          "pretraining of language models"
        ],
        "category": "broad_technical",
        "rationale": "Pretraining is a foundational process in NLP, crucial for understanding model development and performance.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "zero-shot evaluations",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "zero-shot tasks"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot learning is a trending concept that connects to broader discussions on model evaluation and adaptation.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "simplified texts",
        "canonical": "Simplified Texts",
        "aliases": [
          "text simplification",
          "simpler text"
        ],
        "category": "unique_technical",
        "rationale": "The use of simplified texts in pretraining is a unique approach that could influence model performance and understanding.",
        "novelty_score": 0.65,
        "connectivity_score": 0.5,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "downstream performance",
      "sentence structure"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "text complexity",
      "resolved_canonical": "Text Complexity",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "language model pretraining",
      "resolved_canonical": "Language Model Pretraining",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "zero-shot evaluations",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "simplified texts",
      "resolved_canonical": "Simplified Texts",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.5,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Rethinking the Role of Text Complexity in Language Model Pretraining

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16551.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16551](https://arxiv.org/abs/2509.16551)

## 🔗 유사한 논문
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (83.5% similar)
- [[2025-09-22/Once Upon a Time_ Interactive Learning for Storytelling with Small Language Models_20250922|Once Upon a Time: Interactive Learning for Storytelling with Small Language Models]] (80.7% similar)
- [[2025-09-22/Measuring Lexical Diversity of Synthetic Data Generated through Fine-Grained Persona Prompting_20250922|Measuring Lexical Diversity of Synthetic Data Generated through Fine-Grained Persona Prompting]] (80.3% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text?_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text?]] (80.1% similar)
- [[2025-09-22/Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training_20250922|Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Language Model Pretraining|Language Model Pretraining]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Text Complexity|Text Complexity]], [[keywords/Simplified Texts|Simplified Texts]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16551v1 Announce Type: cross 
Abstract: Improving pretraining data quality and size is known to boost downstream performance, but the role of text complexity is less explored. Text complexity refers to how hard a text is to read, and is typically estimated from surface cues such as sentence length, word choice, and sentence structure. We reduce surface-level complexity--shorter sentences, simpler words, simpler structure--while keeping core text content close to constant, and ask: (1) How does complexity affect language modeling across model sizes? (2) Can useful representations be learned from simpler text alone? (3) How does pretraining text complexity influence downstream language understanding? To answer these questions, we simplify human-written texts using a large language model, then pretrain causal models (28M-500M) from scratch on both original and simplified data, and evaluate them in finetuning and zero-shot setups. We find that perplexity is sensitive to the interaction between model capacity and text complexity--smaller models degrade far less on simpler texts--while text complexity has little impact on finetuning evaluations, with zero-shot evaluations indicating that simpler texts benefit performance on linguistic knowledge tasks, whereas more complex texts favor tasks requiring world knowledge and entity tracking.

## 📝 요약

이 논문은 텍스트 복잡성이 사전 학습과 후속 작업 성능에 미치는 영향을 조사합니다. 연구에서는 문장 길이, 단어 선택, 문장 구조 등을 단순화하여 텍스트 복잡성을 줄이고, 다양한 크기의 모델(28M-500M)을 사용해 원본 및 단순화된 데이터를 기반으로 사전 학습을 수행했습니다. 그 결과, 모델의 용량과 텍스트 복잡성 간의 상호작용에 따라 당혹도가 달라지며, 작은 모델은 단순한 텍스트에서 성능 저하가 덜하다는 것을 발견했습니다. 또한, 단순한 텍스트는 언어 지식 과제에서 성능을 향상시키는 반면, 복잡한 텍스트는 세계 지식 및 엔티티 추적이 필요한 과제에서 유리하다는 것을 확인했습니다.

## 🎯 주요 포인트

- 1. 텍스트 복잡성은 문장 길이, 단어 선택, 문장 구조와 같은 표면적 요소로 추정되며, 이를 단순화하여 핵심 내용을 유지하면서 언어 모델링에 미치는 영향을 연구한다.
- 2. 모델 크기와 텍스트 복잡성 간의 상호작용에 따라 퍼플렉시티가 민감하게 반응하며, 작은 모델은 단순한 텍스트에서 성능 저하가 적다.
- 3. 텍스트 복잡성은 파인튜닝 평가에 큰 영향을 미치지 않지만, 제로샷 평가에서는 단순한 텍스트가 언어 지식 과제에 유리하고 복잡한 텍스트가 세계 지식 및 엔티티 추적 과제에 유리하다.
- 4. 인간이 작성한 텍스트를 대형 언어 모델로 단순화하여 원본과 단순화된 데이터를 사용해 인과 모델을 사전 학습하고 평가한다.
- 5. 단순한 텍스트만으로도 유용한 표현을 학습할 수 있는지를 탐구한다.


---

*Generated on 2025-09-23 23:25:32*