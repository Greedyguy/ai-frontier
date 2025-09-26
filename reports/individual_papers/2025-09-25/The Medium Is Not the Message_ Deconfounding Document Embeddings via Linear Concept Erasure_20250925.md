---
keywords:
  - Document Embeddings
  - Debiasing Algorithm
  - Document Similarity
  - Clustering Metrics
  - Out-of-Distribution Benchmarks
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2507.01234
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:56:32.799924",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Document Embeddings",
    "Debiasing Algorithm",
    "Document Similarity",
    "Clustering Metrics",
    "Out-of-Distribution Benchmarks"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Document Embeddings": 0.78,
    "Debiasing Algorithm": 0.77,
    "Document Similarity": 0.8,
    "Clustering Metrics": 0.79,
    "Out-of-Distribution Benchmarks": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "document embeddings",
        "canonical": "Document Embeddings",
        "aliases": [
          "text embeddings",
          "sequence embeddings"
        ],
        "category": "unique_technical",
        "rationale": "Document embeddings are central to the paper's focus on improving similarity metrics by removing biases.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "debiasing algorithm",
        "canonical": "Debiasing Algorithm",
        "aliases": [
          "bias removal algorithm"
        ],
        "category": "unique_technical",
        "rationale": "The debiasing algorithm is a novel approach proposed in the paper to enhance document embeddings.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "document similarity",
        "canonical": "Document Similarity",
        "aliases": [
          "text similarity",
          "sequence similarity"
        ],
        "category": "specific_connectable",
        "rationale": "Document similarity is a key application area for the improved embeddings discussed in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "clustering metrics",
        "canonical": "Clustering Metrics",
        "aliases": [
          "clustering evaluation",
          "cluster analysis"
        ],
        "category": "specific_connectable",
        "rationale": "Clustering metrics are used to evaluate the effectiveness of the debiased embeddings.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "out-of-distribution benchmarks",
        "canonical": "Out-of-Distribution Benchmarks",
        "aliases": [
          "OOD benchmarks",
          "generalization benchmarks"
        ],
        "category": "unique_technical",
        "rationale": "Out-of-distribution benchmarks are crucial for assessing the generalization of the embeddings.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "document embeddings",
      "resolved_canonical": "Document Embeddings",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "debiasing algorithm",
      "resolved_canonical": "Debiasing Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "document similarity",
      "resolved_canonical": "Document Similarity",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "clustering metrics",
      "resolved_canonical": "Clustering Metrics",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "out-of-distribution benchmarks",
      "resolved_canonical": "Out-of-Distribution Benchmarks",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# The Medium Is Not the Message: Deconfounding Document Embeddings via Linear Concept Erasure

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2507.01234.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2507.01234](https://arxiv.org/abs/2507.01234)

## 🔗 유사한 논문
- [[2025-09-25/Magnitude Matters_ a Superior Class of Similarity Metrics for Holistic Semantic Understanding_20250925|Magnitude Matters: a Superior Class of Similarity Metrics for Holistic Semantic Understanding]] (81.1% similar)
- [[2025-09-18/BiasMap_ Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation_20250918|BiasMap: Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation]] (80.6% similar)
- [[2025-09-23/AdvSumm_ Adversarial Training for Bias Mitigation in Text Summarization_20250923|AdvSumm: Adversarial Training for Bias Mitigation in Text Summarization]] (79.9% similar)
- [[2025-09-23/Rethinking the Role of Text Complexity in Language Model Pretraining_20250923|Rethinking the Role of Text Complexity in Language Model Pretraining]] (79.7% similar)
- [[2025-09-25/Quantifying Compositionality of Classic and State-of-the-Art Embeddings_20250925|Quantifying Compositionality of Classic and State-of-the-Art Embeddings]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Document Similarity|Document Similarity]], [[keywords/Clustering Metrics|Clustering Metrics]]
**⚡ Unique Technical**: [[keywords/Document Embeddings|Document Embeddings]], [[keywords/Debiasing Algorithm|Debiasing Algorithm]], [[keywords/Out-of-Distribution Benchmarks|Out-of-Distribution Benchmarks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.01234v3 Announce Type: replace 
Abstract: Embedding-based similarity metrics between text sequences can be influenced not just by the content dimensions we most care about, but can also be biased by spurious attributes like the text's source or language. These document confounders cause problems for many applications, but especially those that need to pool texts from different corpora. This paper shows that a debiasing algorithm that removes information about observed confounders from the encoder representations substantially reduces these biases at a minimal computational cost. Document similarity and clustering metrics improve across every embedding variant and task we evaluate -- often dramatically. Interestingly, performance on out-of-distribution benchmarks is not impacted, indicating that the embeddings are not otherwise degraded.

## 📝 요약

이 논문은 텍스트 시퀀스 간 유사성을 측정하는 임베딩 기반 메트릭이 텍스트의 출처나 언어와 같은 불필요한 속성에 의해 편향될 수 있음을 지적합니다. 이를 해결하기 위해 관찰된 혼란 변수를 인코더 표현에서 제거하는 디바이어싱 알고리즘을 제안합니다. 이 알고리즘은 최소한의 계산 비용으로 이러한 편향을 크게 줄이며, 모든 임베딩 변형과 평가 과제에서 문서 유사성과 클러스터링 메트릭이 개선됩니다. 또한, 분포 외 벤치마크에서 성능이 저하되지 않아 임베딩의 품질이 유지됨을 확인했습니다.

## 🎯 주요 포인트

- 1. 텍스트 시퀀스 간 유사성 측정은 텍스트의 출처나 언어와 같은 부수적인 속성에 의해 편향될 수 있다.
- 2. 문서 혼란 요소는 다양한 응용 분야, 특히 여러 코퍼스에서 텍스트를 모아야 하는 경우에 문제를 일으킨다.
- 3. 관찰된 혼란 요소에 대한 정보를 인코더 표현에서 제거하는 디바이어싱 알고리즘은 이러한 편향을 최소한의 계산 비용으로 크게 줄인다.
- 4. 모든 임베딩 변형 및 평가된 작업에서 문서 유사성과 클러스터링 지표가 개선되었다.
- 5. 분포 외 벤치마크에서의 성능은 영향을 받지 않아 임베딩이 다른 방식으로 저하되지 않음을 나타낸다.


---

*Generated on 2025-09-26 08:56:32*