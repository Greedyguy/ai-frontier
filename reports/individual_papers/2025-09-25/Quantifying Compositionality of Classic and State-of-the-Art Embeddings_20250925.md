---
keywords:
  - Transformer
  - Word Embeddings
  - Compositionality
  - Canonical Correlation Analysis
  - Graph Neural Network
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19332
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:25:16.601499",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Word Embeddings",
    "Compositionality",
    "Canonical Correlation Analysis",
    "Graph Neural Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Word Embeddings": 0.8,
    "Compositionality": 0.78,
    "Canonical Correlation Analysis": 0.75,
    "Graph Neural Network": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer models",
        "canonical": "Transformer",
        "aliases": [
          "Transformer models"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational model architecture in NLP, crucial for linking to related works.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Word embeddings",
        "canonical": "Word Embeddings",
        "aliases": [
          "static word embeddings",
          "Word2vec"
        ],
        "category": "specific_connectable",
        "rationale": "Word embeddings are key to understanding compositionality in language models.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Compositionality",
        "canonical": "Compositionality",
        "aliases": [
          "additive compositionality"
        ],
        "category": "unique_technical",
        "rationale": "Compositionality is a unique concept central to the paper's evaluation of language models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Canonical correlation analysis",
        "canonical": "Canonical Correlation Analysis",
        "aliases": [
          "CCA"
        ],
        "category": "unique_technical",
        "rationale": "This statistical method is critical for evaluating the linearity of embeddings.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Graph models",
        "canonical": "Graph Neural Network",
        "aliases": [
          "graph models"
        ],
        "category": "specific_connectable",
        "rationale": "Graph models are significant for understanding shifts in meaning within embeddings.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "evaluation",
      "metrics",
      "stages"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer models",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Word embeddings",
      "resolved_canonical": "Word Embeddings",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.8
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
      "candidate_surface": "Canonical correlation analysis",
      "resolved_canonical": "Canonical Correlation Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Graph models",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Quantifying Compositionality of Classic and State-of-the-Art Embeddings

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19332.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19332](https://arxiv.org/abs/2509.19332)

## 🔗 유사한 논문
- [[2025-09-23/Breaking Token Into Concepts_ Exploring Extreme Compression in Token Representation Via Compositional Shared Semantics_20250923|Breaking Token Into Concepts: Exploring Extreme Compression in Token Representation Via Compositional Shared Semantics]] (83.3% similar)
- [[2025-09-25/Magnitude Matters_ a Superior Class of Similarity Metrics for Holistic Semantic Understanding_20250925|Magnitude Matters: a Superior Class of Similarity Metrics for Holistic Semantic Understanding]] (82.3% similar)
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (82.3% similar)
- [[2025-09-22/BBScoreV2_ Learning Time-Evolution and Latent Alignment from Stochastic Representation_20250922|BBScoreV2: Learning Time-Evolution and Latent Alignment from Stochastic Representation]] (82.2% similar)
- [[2025-09-24/Long Story Short_ Disentangling Compositionality and Long-Caption Understanding in VLMs_20250924|Long Story Short: Disentangling Compositionality and Long-Caption Understanding in VLMs]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Word Embeddings|Word Embeddings]], [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Compositionality|Compositionality]], [[keywords/Canonical Correlation Analysis|Canonical Correlation Analysis]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19332v1 Announce Type: cross 
Abstract: For language models to generalize correctly to novel expressions, it is critical that they exploit access compositional meanings when this is justified. Even if we don't know what a "pelp" is, we can use our knowledge of numbers to understand that "ten pelps" makes more pelps than "two pelps". Static word embeddings such as Word2vec made strong, indeed excessive, claims about compositionality. The SOTA generative, transformer models and graph models, however, go too far in the other direction by providing no real limits on shifts in meaning due to context. To quantify the additive compositionality, we formalize a two-step, generalized evaluation that (i) measures the linearity between known entity attributes and their embeddings via canonical correlation analysis, and (ii) evaluates additive generalization by reconstructing embeddings for unseen attribute combinations and checking reconstruction metrics such as L2 loss, cosine similarity, and retrieval accuracy. These metrics also capture failure cases where linear composition breaks down. Sentences, knowledge graphs, and word embeddings are evaluated and tracked the compositionality across all layers and training stages. Stronger compositional signals are observed in later training stages across data modalities, and in deeper layers of the transformer-based model before a decline at the top layer. Code is available at https://github.com/Zhijin-Guo1/quantifying-compositionality.

## 📝 요약

이 논문은 언어 모델이 새로운 표현에 대해 올바르게 일반화하기 위해 조합적 의미를 활용하는 방법을 탐구합니다. 기존의 Word2vec 같은 정적 단어 임베딩은 조합성을 과도하게 주장했으나, 최신 생성적 트랜스포머 모델과 그래프 모델은 문맥에 따른 의미 변화에 제한을 두지 않습니다. 이를 해결하기 위해, 저자들은 두 단계의 평가 방법을 제안합니다. 첫째, 정준 상관 분석을 통해 알려진 엔티티 속성과 임베딩 간의 선형성을 측정합니다. 둘째, 보지 못한 속성 조합에 대한 임베딩을 재구성하여 L2 손실, 코사인 유사도, 검색 정확도 등의 지표로 평가합니다. 이 방법은 조합적 실패 사례도 포착합니다. 실험 결과, 트랜스포머 모델의 깊은 층과 학습 후반 단계에서 강한 조합 신호가 관찰되었습니다. 코드와 데이터는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. 언어 모델이 새로운 표현에 일반화하기 위해서는 조합적 의미를 활용하는 것이 중요합니다.
- 2. 기존의 정적 단어 임베딩은 조합성에 대해 과도한 주장을 했으나, 최신 생성적 트랜스포머 모델과 그래프 모델은 문맥에 따른 의미 변화에 제한이 없습니다.
- 3. 우리는 두 단계의 일반화된 평가를 통해 추가적 조합성을 정량화하며, 이는 알려진 엔티티 속성과 임베딩 간의 선형성을 측정하고, 보이지 않는 속성 조합에 대한 임베딩을 재구성하여 평가합니다.
- 4. 평가 지표는 L2 손실, 코사인 유사도, 검색 정확도 등을 포함하며, 선형 조합이 실패하는 경우도 포착합니다.
- 5. 데이터 모달리티 전반에 걸쳐 훈련 후반 단계에서 더 강한 조합 신호가 관찰되며, 트랜스포머 기반 모델의 깊은 층에서 이러한 신호가 두드러집니다.


---

*Generated on 2025-09-25 15:25:16*