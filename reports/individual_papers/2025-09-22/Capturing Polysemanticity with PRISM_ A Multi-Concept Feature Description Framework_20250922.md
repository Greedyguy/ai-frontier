---
keywords:
  - PRISM
  - Large Language Model
  - Natural Language Processing
  - Polysemanticity
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2506.15538
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:04:40.881014",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "PRISM",
    "Large Language Model",
    "Natural Language Processing",
    "Polysemanticity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "PRISM": 0.78,
    "Large Language Model": 0.7,
    "Natural Language Processing": 0.65,
    "Polysemanticity": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Polysemantic FeatuRe Identification and Scoring Method",
        "canonical": "PRISM",
        "aliases": [
          "Polysemantic Feature Identification",
          "PRISM Framework"
        ],
        "category": "unique_technical",
        "rationale": "PRISM is a novel framework specifically designed to address polysemanticity in LLMs, making it a unique technical contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's focus on interpretability and polysemanticity, providing a broad technical context.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Natural Language Processing",
        "canonical": "Natural Language Processing",
        "aliases": [
          "NLP"
        ],
        "category": "broad_technical",
        "rationale": "NLP is a key domain where the discussed interpretability methods are applied, enhancing connectivity with related research.",
        "novelty_score": 0.2,
        "connectivity_score": 0.85,
        "specificity_score": 0.55,
        "link_intent_score": 0.65
      },
      {
        "surface": "polysemanticity",
        "canonical": "Polysemanticity",
        "aliases": [
          "multiple meanings",
          "multi-concept"
        ],
        "category": "evolved_concepts",
        "rationale": "Polysemanticity is a central concept in the paper, addressing the complexity of neuron behavior in LLMs.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "concept",
      "feature"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Polysemantic FeatuRe Identification and Scoring Method",
      "resolved_canonical": "PRISM",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Natural Language Processing",
      "resolved_canonical": "Natural Language Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.85,
        "specificity": 0.55,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "polysemanticity",
      "resolved_canonical": "Polysemanticity",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Capturing Polysemanticity with PRISM: A Multi-Concept Feature Description Framework

**Korean Title:** PRISM으로 다의성을 포착하기: 다중 개념 특징 설명 프레임워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.15538.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2506.15538](https://arxiv.org/abs/2506.15538)

## 🔗 유사한 논문
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box: Interpretable LLMs via Semantic Resonance Architecture]] (84.7% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (83.9% similar)
- [[2025-09-19/Large Multi-modal Models Can Interpret Features in Large Multi-modal Models_20250919|Large Multi-modal Models Can Interpret Features in Large Multi-modal Models]] (83.6% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (83.5% similar)
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Natural Language Processing|Natural Language Processing]]
**⚡ Unique Technical**: [[keywords/PRISM|PRISM]]
**🚀 Evolved Concepts**: [[keywords/Polysemanticity|Polysemanticity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.15538v3 Announce Type: replace-cross 
Abstract: Automated interpretability research aims to identify concepts encoded in neural network features to enhance human understanding of model behavior. Within the context of large language models (LLMs) for natural language processing (NLP), current automated neuron-level feature description methods face two key challenges: limited robustness and the assumption that each neuron encodes a single concept (monosemanticity), despite increasing evidence of polysemanticity. This assumption restricts the expressiveness of feature descriptions and limits their ability to capture the full range of behaviors encoded in model internals. To address this, we introduce Polysemantic FeatuRe Identification and Scoring Method (PRISM), a novel framework specifically designed to capture the complexity of features in LLMs. Unlike approaches that assign a single description per neuron, common in many automated interpretability methods in NLP, PRISM produces more nuanced descriptions that account for both monosemantic and polysemantic behavior. We apply PRISM to LLMs and, through extensive benchmarking against existing methods, demonstrate that our approach produces more accurate and faithful feature descriptions, improving both overall description quality (via a description score) and the ability to capture distinct concepts when polysemanticity is present (via a polysemanticity score).

## 🔍 Abstract (한글 번역)

arXiv:2506.15538v3 발표 유형: 교체-교차  
초록: 자동 해석 가능성 연구는 모델의 행동에 대한 인간의 이해를 향상시키기 위해 신경망 특징에 인코딩된 개념을 식별하는 것을 목표로 합니다. 자연어 처리(NLP)를 위한 대형 언어 모델(LLM)의 맥락에서, 현재의 자동화된 뉴런 수준의 특징 설명 방법은 두 가지 주요 과제에 직면해 있습니다: 제한된 견고성과 각 뉴런이 단일 개념(단일 의미성)을 인코딩한다고 가정하는 것, 이는 다의성에 대한 증가하는 증거에도 불구하고 그렇습니다. 이 가정은 특징 설명의 표현력을 제한하고 모델 내부에 인코딩된 행동의 전체 범위를 포착하는 능력을 제한합니다. 이를 해결하기 위해, 우리는 LLM의 특징 복잡성을 포착하기 위해 특별히 설계된 새로운 프레임워크인 다의성 특징 식별 및 점수화 방법(PRISM)을 소개합니다. NLP의 많은 자동 해석 가능성 방법에서 흔히 볼 수 있는 뉴런당 단일 설명을 할당하는 접근 방식과 달리, PRISM은 단일 의미성과 다의성 행동 모두를 고려한 보다 세밀한 설명을 제공합니다. 우리는 LLM에 PRISM을 적용하고 기존 방법과의 광범위한 벤치마킹을 통해 우리의 접근 방식이 더 정확하고 충실한 특징 설명을 생성하며, 전반적인 설명 품질(설명 점수를 통해)과 다의성이 존재할 때 독특한 개념을 포착하는 능력(다의성 점수를 통해)을 모두 개선함을 입증합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 신경망 특징을 해석하는 자동화된 방법론의 한계를 극복하기 위해 PRISM이라는 새로운 프레임워크를 제안합니다. 기존 방법들은 각 뉴런이 단일 개념만을 인코딩한다고 가정하여 표현력에 한계를 두었으나, PRISM은 다의적(Polysemantic) 특성을 고려하여 보다 복잡한 특징을 포착합니다. 이를 통해 PRISM은 기존 방법들보다 더욱 정확하고 신뢰할 수 있는 특징 설명을 제공하며, 특히 다의성이 존재할 때 다양한 개념을 포착하는 능력을 향상시킵니다.

## 🎯 주요 포인트

- 1. 자동 해석 가능성 연구는 신경망의 특징에 인코딩된 개념을 식별하여 모델 행동에 대한 인간의 이해를 증진시키는 것을 목표로 합니다.
- 2. 대형 언어 모델(LLM)의 자동화된 뉴런 수준의 특징 설명 방법은 제한된 견고성과 단일 개념 인코딩 가정으로 인해 도전에 직면해 있습니다.
- 3. PRISM은 LLM의 특징 복잡성을 포착하기 위해 설계된 새로운 프레임워크로, 단일 설명이 아닌 더 세밀한 설명을 제공합니다.
- 4. PRISM은 기존 방법과의 광범위한 벤치마킹을 통해 더 정확하고 충실한 특징 설명을 생성하며, 다의성을 고려한 설명 점수와 다의성 점수를 통해 설명 품질을 향상시킵니다.


---

*Generated on 2025-09-23 10:04:40*