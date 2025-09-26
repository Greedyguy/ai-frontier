---
keywords:
  - Multimodal Learning
  - Adaptive Planning Graph
  - Vision-Language Model
  - Retrieval Augmented Generation
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2508.16051
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:40:27.668038",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Adaptive Planning Graph",
    "Vision-Language Model",
    "Retrieval Augmented Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.8,
    "Adaptive Planning Graph": 0.82,
    "Vision-Language Model": 0.78,
    "Retrieval Augmented Generation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Multi-hop question answering",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal QA",
          "Multimodal Question Answering"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the broader concept of integrating multiple data types, enhancing links to multimodal research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Adaptive Planning Graph",
        "canonical": "Adaptive Planning Graph",
        "aliases": [
          "APG"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework that is central to the paper's methodology, offering unique linking potential.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Vision-Language",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language Integration"
        ],
        "category": "evolved_concepts",
        "rationale": "Represents a trending concept in combining visual and textual data, crucial for multimodal applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "retrieval and reasoning modules",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG Modules"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the concept of enhancing reasoning with retrieval, relevant for improving QA systems.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.68,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "training-free framework",
      "task-specific training",
      "current state"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Multi-hop question answering",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Adaptive Planning Graph",
      "resolved_canonical": "Adaptive Planning Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Vision-Language",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "retrieval and reasoning modules",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.68,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs

**Korean Title:** MMAPG: 적응형 계획 그래프를 통한 다중 모달 다중 홉 질문 응답을 위한 훈련 불필요 프레임워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.16051.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2508.16051](https://arxiv.org/abs/2508.16051)

## 🔗 유사한 논문
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (84.0% similar)
- [[2025-09-22/Advances in Multimodal Adaptation and Generalization_ From Traditional Approaches to Foundation Models_20250922|Advances in Multimodal Adaptation and Generalization: From Traditional Approaches to Foundation Models]] (83.7% similar)
- [[2025-09-19/Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (82.7% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals: Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (82.4% similar)
- [[2025-09-22/Multi-Modal Interpretability for Enhanced Localization in Vision-Language Models_20250922|Multi-Modal Interpretability for Enhanced Localization in Vision-Language Models]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Adaptive Planning Graph|Adaptive Planning Graph]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.16051v2 Announce Type: replace 
Abstract: Multimodal Multi-hop question answering requires integrating information from diverse sources, such as images and texts, to derive answers. Existing methods typically rely on sequential retrieval and reasoning, where each step builds on the previous output. However, this single-path paradigm makes them vulnerable to errors due to misleading intermediate steps. Moreover, developing multimodal models can be computationally expensive, often requiring extensive training. To address these limitations, we propose a training-free framework guided by an Adaptive Planning Graph, which consists of planning, retrieval and reasoning modules. The planning module analyzes the current state of the Adaptive Planning Graph, determines the next action and where to expand the graph, which enables dynamic and flexible exploration of reasoning paths. To handle retrieval of text to unspecified target modalities, we devise modality-specific strategies that dynamically adapt to distinct data types. Our approach preserves the characteristics of multimodal information without costly task-specific training, enabling seamless integration with up-to-date models. Finally, the experiments on MultimodalQA and WebQA show that our approach matches or outperforms existing models that rely on training.

## 🔍 Abstract (한글 번역)

arXiv:2508.16051v2 발표 유형: 교체  
초록: 다중모달 다중단계 질문 응답은 이미지와 텍스트와 같은 다양한 출처의 정보를 통합하여 답을 도출해야 합니다. 기존 방법들은 일반적으로 순차적 검색 및 추론에 의존하며, 각 단계는 이전 출력에 기반하여 진행됩니다. 그러나 이러한 단일 경로 패러다임은 중간 단계에서의 오류로 인해 오답에 취약합니다. 게다가, 다중모달 모델 개발은 종종 광범위한 훈련이 필요하여 계산 비용이 많이 듭니다. 이러한 한계를 극복하기 위해, 우리는 계획, 검색 및 추론 모듈로 구성된 적응형 계획 그래프에 의해 안내되는 훈련이 필요 없는 프레임워크를 제안합니다. 계획 모듈은 적응형 계획 그래프의 현재 상태를 분석하고, 다음 행동과 그래프 확장 위치를 결정하여 추론 경로의 동적이고 유연한 탐색을 가능하게 합니다. 명시되지 않은 대상 모달리티로의 텍스트 검색을 처리하기 위해, 우리는 서로 다른 데이터 유형에 동적으로 적응하는 모달리티별 전략을 고안했습니다. 우리의 접근 방식은 비용이 많이 드는 작업별 훈련 없이 다중모달 정보의 특성을 보존하며, 최신 모델과의 원활한 통합을 가능하게 합니다. 마지막으로, MultimodalQA 및 WebQA에 대한 실험은 우리의 접근 방식이 훈련에 의존하는 기존 모델과 동등하거나 더 나은 성능을 보임을 보여줍니다.

## 📝 요약

이 논문은 다양한 소스(이미지와 텍스트)에서 정보를 통합하여 답을 도출하는 멀티모달 멀티홉 질문 응답 시스템을 다룹니다. 기존 방법은 순차적 검색과 추론에 의존하여 중간 단계의 오류에 취약하고, 멀티모달 모델 개발에 많은 비용이 듭니다. 이를 해결하기 위해, 저자들은 Adaptive Planning Graph를 활용한 훈련이 필요 없는 프레임워크를 제안합니다. 이 프레임워크는 계획, 검색, 추론 모듈로 구성되어 있으며, 동적이고 유연한 추론 경로 탐색을 가능하게 합니다. 또한, 텍스트 검색을 위한 모달리티별 전략을 통해 다양한 데이터 유형에 적응합니다. 제안된 방법은 비싼 훈련 없이 최신 모델과의 통합을 가능하게 하며, 실험 결과 MultimodalQA와 WebQA에서 기존 모델과 동등하거나 더 나은 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 멀티모달 멀티홉 질문 응답은 이미지와 텍스트 등 다양한 소스에서 정보를 통합하여 답을 도출해야 한다.
- 2. 기존 방법은 순차적 검색과 추론에 의존하여 중간 단계의 오류에 취약하다.
- 3. 제안된 프레임워크는 Adaptive Planning Graph를 활용하여 동적이고 유연한 추론 경로 탐색을 가능하게 한다.
- 4. 텍스트 검색을 위한 모달리티별 전략을 통해 데이터 유형에 맞게 동적으로 적응한다.
- 5. MultimodalQA와 WebQA 실험에서 제안된 방법이 기존 모델과 동등하거나 더 나은 성능을 보였다.


---

*Generated on 2025-09-23 09:40:27*