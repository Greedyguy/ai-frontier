---
keywords:
  - Few-Shot Learning
  - Large Language Model
  - Kernel Method
  - Optimal Design Regularization
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15676
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:10:08.131950",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Few-Shot Learning",
    "Large Language Model",
    "Kernel Method",
    "Optimal Design Regularization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Few-Shot Learning": 0.8,
    "Large Language Model": 0.85,
    "Kernel Method": 0.75,
    "Optimal Design Regularization": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "In-context learning",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "ICL"
        ],
        "category": "specific_connectable",
        "rationale": "In-context learning is closely related to Few-Shot Learning, which is a trending concept in adapting models with limited data.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the study and connect well with other concepts in the field.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Kernel trick",
        "canonical": "Kernel Method",
        "aliases": [
          "Kernelization"
        ],
        "category": "unique_technical",
        "rationale": "The kernel trick is a unique method used in the paper to handle high-dimensional spaces, offering a novel approach.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Optimal design-based regularizer",
        "canonical": "Optimal Design Regularization",
        "aliases": [
          "Design-based regularization"
        ],
        "category": "unique_technical",
        "rationale": "This concept introduces a novel regularization technique to enhance diversity in example selection.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.78,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "example selection",
      "query-specific optimization",
      "prediction error"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "In-context learning",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Kernel trick",
      "resolved_canonical": "Kernel Method",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Optimal design-based regularizer",
      "resolved_canonical": "Optimal Design Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.78,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# KITE: Kernelized and Information Theoretic Exemplars for In-Context Learning

**Korean Title:** KITE: 문맥 학습을 위한 커널화 및 정보 이론적 예제들

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15676.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15676](https://arxiv.org/abs/2509.15676)

## 🔗 유사한 논문
- [[2025-09-22/Disentangling Latent Shifts of In-Context Learning with Weak Supervision_20250922|Disentangling Latent Shifts of In-Context Learning with Weak Supervision]] (85.6% similar)
- [[2025-09-18/TICL_ Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models_20250918|TICL: Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (84.4% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (83.4% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (82.5% similar)
- [[2025-09-22/Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training_20250922|Enhancing LLM Language Adaption through Cross-lingual In-Context Pre-training]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Kernel Method|Kernel Method]], [[keywords/Optimal Design Regularization|Optimal Design Regularization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15676v1 Announce Type: cross 
Abstract: In-context learning (ICL) has emerged as a powerful paradigm for adapting large language models (LLMs) to new and data-scarce tasks using only a few carefully selected task-specific examples presented in the prompt. However, given the limited context size of LLMs, a fundamental question arises: Which examples should be selected to maximize performance on a given user query? While nearest-neighbor-based methods like KATE have been widely adopted for this purpose, they suffer from well-known drawbacks in high-dimensional embedding spaces, including poor generalization and a lack of diversity. In this work, we study this problem of example selection in ICL from a principled, information theory-driven perspective. We first model an LLM as a linear function over input embeddings and frame the example selection task as a query-specific optimization problem: selecting a subset of exemplars from a larger example bank that minimizes the prediction error on a specific query. This formulation departs from traditional generalization-focused learning theoretic approaches by targeting accurate prediction for a specific query instance. We derive a principled surrogate objective that is approximately submodular, enabling the use of a greedy algorithm with an approximation guarantee. We further enhance our method by (i) incorporating the kernel trick to operate in high-dimensional feature spaces without explicit mappings, and (ii) introducing an optimal design-based regularizer to encourage diversity in the selected examples. Empirically, we demonstrate significant improvements over standard retrieval methods across a suite of classification tasks, highlighting the benefits of structure-aware, diverse example selection for ICL in real-world, label-scarce scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2509.15676v1 발표 유형: 교차  
초록: 맥락 내 학습(ICL)은 대형 언어 모델(LLM)을 새로운 데이터가 부족한 작업에 적응시키기 위한 강력한 패러다임으로 부상하고 있으며, 이는 프롬프트에 제시된 몇 가지 신중하게 선택된 작업별 예제를 사용하는 것만으로 가능합니다. 그러나 LLM의 제한된 컨텍스트 크기를 고려할 때, 근본적인 질문이 제기됩니다: 주어진 사용자 쿼리에 대한 성능을 극대화하기 위해 어떤 예제를 선택해야 할까요? KATE와 같은 최근접 이웃 기반 방법이 이 목적을 위해 널리 채택되었지만, 이들은 고차원 임베딩 공간에서의 일반화 부족과 다양성 결여와 같은 잘 알려진 단점이 있습니다. 본 연구에서는 정보 이론에 기반한 원칙적인 관점에서 ICL에서의 예제 선택 문제를 연구합니다. 우리는 먼저 LLM을 입력 임베딩에 대한 선형 함수로 모델링하고, 예제 선택 작업을 특정 쿼리에 대한 최적화 문제로 구성합니다: 특정 쿼리에 대한 예측 오류를 최소화하는 더 큰 예제 은행에서 예제의 하위 집합을 선택하는 것입니다. 이 공식은 특정 쿼리 인스턴스에 대한 정확한 예측을 목표로 함으로써 전통적인 일반화 중심의 학습 이론적 접근 방식에서 벗어납니다. 우리는 근사적으로 부분 모듈러인 원칙적인 대리 목표를 도출하여 근사 보장이 있는 탐욕 알고리즘을 사용할 수 있게 합니다. 우리는 또한 (i) 명시적 매핑 없이 고차원 특징 공간에서 작동하기 위해 커널 트릭을 통합하고, (ii) 선택된 예제의 다양성을 장려하기 위해 최적 설계 기반 정규화를 도입하여 방법을 더욱 향상시킵니다. 실증적으로, 우리는 다양한 분류 작업에서 표준 검색 방법에 비해 상당한 개선을 보여주며, 실제 세계의 레이블이 부족한 시나리오에서 ICL을 위한 구조 인식, 다양한 예제 선택의 이점을 강조합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 새로운 데이터 부족 과제에 적응시키기 위한 강력한 패러다임인 문맥 내 학습(ICL)에서 최적의 예제 선택 문제를 정보 이론적 관점에서 다룹니다. 기존의 최근접 이웃 기반 방법들이 고차원 임베딩 공간에서 일반화 부족과 다양성 결여 문제를 겪는다는 점을 지적하고, 이를 해결하기 위해 LLM을 입력 임베딩에 대한 선형 함수로 모델링하여 특정 쿼리에 대한 예측 오류를 최소화하는 예제 선택 최적화 문제로 정의합니다. 이 과정에서 근사적으로 부분 모듈러인 대리 목적을 도출하여 탐욕 알고리즘을 사용하고, 커널 트릭과 최적 설계 기반 정규화를 도입하여 다양성을 촉진합니다. 실험 결과, 다양한 분류 작업에서 기존 방법보다 성능이 크게 향상됨을 보여주며, 구조 인식과 다양한 예제 선택의 중요성을 강조합니다.

## 🎯 주요 포인트

- 1. In-context learning(ICL)은 대형 언어 모델(LLM)을 새로운 데이터가 부족한 작업에 적응시키기 위한 강력한 패러다임으로 부상했습니다.
- 2. LLM의 제한된 컨텍스트 크기 때문에, 주어진 사용자 쿼리에 대한 성능을 극대화하기 위해 어떤 예제를 선택해야 하는지가 중요한 문제로 대두됩니다.
- 3. 본 연구는 정보 이론에 기반한 접근법을 통해 ICL에서의 예제 선택 문제를 다루며, 쿼리별 최적화 문제로 예제 선택을 모델링합니다.
- 4. 대용량 예제 은행에서 특정 쿼리에 대한 예측 오류를 최소화하는 예제를 선택하는 문제를 해결하기 위해 근사적으로 부분 모듈러인 대리 목표를 도출하고, 탐욕 알고리즘을 사용합니다.
- 5. 실험적으로, 구조 인식 및 다양한 예제 선택이 실제 세계의 레이블이 부족한 시나리오에서 ICL의 성능을 크게 향상시킴을 입증했습니다.


---

*Generated on 2025-09-23 09:10:08*