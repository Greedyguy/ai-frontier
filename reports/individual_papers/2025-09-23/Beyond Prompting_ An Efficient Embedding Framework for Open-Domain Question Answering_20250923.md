---
keywords:
  - Large Language Model
  - Open-Domain Question Answering
  - Self-supervised Learning
  - Embedding Framework
  - Entropy-based Selection
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2503.01606
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:49:16.468930",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Open-Domain Question Answering",
    "Self-supervised Learning",
    "Embedding Framework",
    "Entropy-based Selection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Open-Domain Question Answering": 0.88,
    "Self-supervised Learning": 0.8,
    "Embedding Framework": 0.78,
    "Entropy-based Selection": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "language models"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are foundational to the field and connect with numerous related concepts in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Open Domain Question Answering",
        "canonical": "Open-Domain Question Answering",
        "aliases": [
          "ODQA",
          "open-domain QA"
        ],
        "category": "specific_connectable",
        "rationale": "Open-Domain Question Answering is a specific task that connects with various retrieval and reading strategies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.88
      },
      {
        "surface": "Contrastive Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "contrastive objective"
        ],
        "category": "specific_connectable",
        "rationale": "Contrastive Learning is a self-supervised approach that enhances model training, linking to broader self-supervised methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Embedding Framework",
        "canonical": "Embedding Framework",
        "aliases": [
          "embedding model",
          "embedding approach"
        ],
        "category": "unique_technical",
        "rationale": "The Embedding Framework is a novel approach proposed in the paper, offering unique insights into embedding-based QA.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Entropy-based Selection",
        "canonical": "Entropy-based Selection",
        "aliases": [
          "entropy selection",
          "entropy mechanism"
        ],
        "category": "unique_technical",
        "rationale": "Entropy-based Selection is a unique mechanism introduced in the paper, enhancing answer selection processes.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "retriever-reader pipelines",
      "retrieval coverage",
      "exploratory embedding"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Open Domain Question Answering",
      "resolved_canonical": "Open-Domain Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Embedding Framework",
      "resolved_canonical": "Embedding Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Entropy-based Selection",
      "resolved_canonical": "Entropy-based Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Beyond Prompting: An Efficient Embedding Framework for Open-Domain Question Answering

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2503.01606.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2503.01606](https://arxiv.org/abs/2503.01606)

## 🔗 유사한 논문
- [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know: An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (84.3% similar)
- [[2025-09-22/MMAPG_ A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs_20250922|MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs]] (83.9% similar)
- [[2025-09-22/Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models_20250922|Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models]] (83.5% similar)
- [[2025-09-19/SWE-QA_ Can Language Models Answer Repository-level Code Questions?_20250919|SWE-QA: Can Language Models Answer Repository-level Code Questions?]] (83.2% similar)
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Open-Domain Question Answering|Open-Domain Question Answering]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Embedding Framework|Embedding Framework]], [[keywords/Entropy-based Selection|Entropy-based Selection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.01606v3 Announce Type: replace-cross 
Abstract: Large language models have recently pushed open domain question answering (ODQA) to new frontiers. However, prevailing retriever-reader pipelines often depend on multiple rounds of prompt level instructions, leading to high computational overhead, instability, and suboptimal retrieval coverage. In this paper, we propose EmbQA, an embedding-level framework that alleviates these shortcomings by enhancing both the retriever and the reader. Specifically, we refine query representations via lightweight linear layers under an unsupervised contrastive learning objective, thereby reordering retrieved passages to highlight those most likely to contain correct answers. Additionally, we introduce an exploratory embedding that broadens the model's latent semantic space to diversify candidate generation and employs an entropy-based selection mechanism to choose the most confident answer automatically. Extensive experiments across three open-source LLMs, three retrieval methods, and four ODQA benchmarks demonstrate that EmbQA substantially outperforms recent baselines in both accuracy and efficiency.

## 📝 요약

최근 대형 언어 모델은 개방형 도메인 질문 응답(ODQA) 분야에서 새로운 가능성을 열었습니다. 그러나 기존의 검색기-리더 파이프라인은 여러 번의 프롬프트 수준 지침에 의존하여 높은 계산 비용과 불안정성, 비효율적인 검색 범위를 초래합니다. 본 논문에서는 이러한 문제를 해결하기 위해 EmbQA라는 임베딩 수준의 프레임워크를 제안합니다. 이 프레임워크는 검색기와 리더를 개선하여 쿼리 표현을 경량화된 선형 계층과 비지도 대조 학습 목표를 통해 개선하고, 검색된 문서의 순서를 재조정하여 올바른 답변을 포함할 가능성이 높은 문서를 강조합니다. 또한, 모델의 잠재 의미 공간을 확장하는 탐색 임베딩을 도입하고, 엔트로피 기반 선택 메커니즘을 통해 가장 신뢰할 수 있는 답변을 자동으로 선택합니다. 세 가지 오픈 소스 LLM, 세 가지 검색 방법, 네 가지 ODQA 벤치마크를 대상으로 한 광범위한 실험 결과, EmbQA는 정확성과 효율성 면에서 최근의 기준선을 크게 능가하는 성과를 보였습니다.

## 🎯 주요 포인트

- 1. EmbQA는 ODQA에서 발생하는 높은 계산 비용, 불안정성, 비효율적인 검색 범위 문제를 해결하기 위해 제안된 임베딩 수준의 프레임워크입니다.
- 2. EmbQA는 비지도 대조 학습 목표 하에 경량의 선형 레이어를 통해 쿼리 표현을 개선하여, 올바른 답변을 포함할 가능성이 높은 검색된 문서를 재정렬합니다.
- 3. 탐색적 임베딩을 도입하여 모델의 잠재 의미 공간을 확장하고, 엔트로피 기반 선택 메커니즘을 통해 가장 신뢰할 수 있는 답변을 자동으로 선택합니다.
- 4. 세 가지 오픈 소스 LLM, 세 가지 검색 방법, 네 가지 ODQA 벤치마크에서의 광범위한 실험을 통해 EmbQA가 최근의 기준 모델들보다 정확성과 효율성에서 크게 우수함을 입증했습니다.


---

*Generated on 2025-09-24 00:49:16*