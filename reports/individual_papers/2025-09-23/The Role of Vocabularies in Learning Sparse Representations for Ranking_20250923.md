---
keywords:
  - Learned Sparse Retrieval
  - SPLADE
  - Transformer
  - Vocabulary Granularity
  - ESPLADE
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16621
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:39:06.295133",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Learned Sparse Retrieval",
    "SPLADE",
    "Transformer",
    "Vocabulary Granularity",
    "ESPLADE"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Learned Sparse Retrieval": 0.85,
    "SPLADE": 0.8,
    "Transformer": 0.75,
    "Vocabulary Granularity": 0.7,
    "ESPLADE": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Learned Sparse Retrieval",
        "canonical": "Learned Sparse Retrieval",
        "aliases": [
          "LSR"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on retrieval efficiency and effectiveness, offering unique insights into sparse representation learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "SPLADE",
        "canonical": "SPLADE",
        "aliases": [
          "Sparse Lattice"
        ],
        "category": "unique_technical",
        "rationale": "SPLADE is a specific model discussed extensively in the paper, critical for understanding the proposed improvements.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "BERT",
        "canonical": "Transformer",
        "aliases": [
          "Bidirectional Encoder Representations from Transformers"
        ],
        "category": "broad_technical",
        "rationale": "BERT is a well-known Transformer model used in the study, linking to broader discussions on Transformer-based architectures.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "vocabularic granularity",
        "canonical": "Vocabulary Granularity",
        "aliases": [
          "vocabularic detail"
        ],
        "category": "unique_technical",
        "rationale": "This concept is crucial for understanding the paper's exploration of vocabulary roles in retrieval models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      },
      {
        "surface": "ESPLADE",
        "canonical": "ESPLADE",
        "aliases": [
          "Expanded SPLADE"
        ],
        "category": "unique_technical",
        "rationale": "ESPLADE represents a key advancement in the paper, focusing on expanded vocabularies for improved retrieval.",
        "novelty_score": 0.68,
        "connectivity_score": 0.58,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
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
      "candidate_surface": "Learned Sparse Retrieval",
      "resolved_canonical": "Learned Sparse Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "SPLADE",
      "resolved_canonical": "SPLADE",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "BERT",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "vocabularic granularity",
      "resolved_canonical": "Vocabulary Granularity",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "ESPLADE",
      "resolved_canonical": "ESPLADE",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.58,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# The Role of Vocabularies in Learning Sparse Representations for Ranking

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16621.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16621](https://arxiv.org/abs/2509.16621)

## 🔗 유사한 논문
- [[2025-09-23/Evaluating the Effectiveness and Scalability of LLM-Based Data Augmentation for Retrieval_20250923|Evaluating the Effectiveness and Scalability of LLM-Based Data Augmentation for Retrieval]] (80.8% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box: Interpretable LLMs via Semantic Resonance Architecture]] (78.9% similar)
- [[2025-09-22/Distribution-Aligned Decoding for Efficient LLM Task Adaptation_20250922|Distribution-Aligned Decoding for Efficient LLM Task Adaptation]] (78.9% similar)
- [[2025-09-23/Federated Learning with Ad-hoc Adapter Insertions_ The Case of Soft-Embeddings for Training Classifier-as-Retriever_20250923|Federated Learning with Ad-hoc Adapter Insertions: The Case of Soft-Embeddings for Training Classifier-as-Retriever]] (78.8% similar)
- [[2025-09-23/LCES_ Zero-shot Automated Essay Scoring via Pairwise Comparisons Using Large Language Models_20250923|LCES: Zero-shot Automated Essay Scoring via Pairwise Comparisons Using Large Language Models]] (78.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/Learned Sparse Retrieval|Learned Sparse Retrieval]], [[keywords/SPLADE|SPLADE]], [[keywords/Vocabulary Granularity|Vocabulary Granularity]], [[keywords/ESPLADE|ESPLADE]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16621v1 Announce Type: cross 
Abstract: Learned Sparse Retrieval (LSR) such as SPLADE has growing interest for effective semantic 1st stage matching while enjoying the efficiency of inverted indices. A recent work on learning SPLADE models with expanded vocabularies (ESPLADE) was proposed to represent queries and documents into a sparse space of custom vocabulary which have different levels of vocabularic granularity. Within this effort, however, there have not been many studies on the role of vocabulary in SPLADE models and their relationship to retrieval efficiency and effectiveness.
  To study this, we construct BERT models with 100K-sized output vocabularies, one initialized with the ESPLADE pretraining method and one initialized randomly. After finetune on real-world search click logs, we applied logit score-based queries and documents pruning to max size for further balancing efficiency. The experimental result in our evaluation set shows that, when pruning is applied, the two models are effective compared to the 32K-sized normal SPLADE model in the computational budget under the BM25. And the ESPLADE models are more effective than the random vocab model, while having a similar retrieval cost.
  The result indicates that the size and pretrained weight of output vocabularies play the role of configuring the representational specification for queries, documents, and their interactions in the retrieval engine, beyond their original meaning and purposes in NLP. These findings can provide a new room for improvement for LSR by identifying the importance of representational specification from vocabulary configuration for efficient and effective retrieval.

## 📝 요약

이 논문은 SPLADE 모델의 어휘 확장을 통한 학습 희소 검색(LSR)의 효율성과 효과성을 연구합니다. ESPLADE라는 확장된 어휘를 사용하여 쿼리와 문서를 희소 공간에 표현하는 방법을 제안합니다. BERT 모델을 사용하여 10만 개의 출력 어휘를 가진 모델을 구축하고, ESPLADE 사전 학습 방법과 무작위 초기화를 비교합니다. 실제 검색 클릭 로그로 미세 조정 후, 효율성을 위해 쿼리와 문서를 정리합니다. 실험 결과, 두 모델 모두 3.2만 개 어휘의 일반 SPLADE 모델보다 효율적이며, ESPLADE 모델이 무작위 어휘 모델보다 더 효과적임을 보여줍니다. 이는 어휘의 크기와 사전 학습 가중치가 검색 엔진에서 쿼리와 문서의 표현 사양을 구성하는 데 중요한 역할을 한다는 것을 시사합니다. 이러한 발견은 LSR의 효율성과 효과성을 개선할 수 있는 새로운 가능성을 제공합니다.

## 🎯 주요 포인트

- 1. ESPLADE는 확장된 어휘를 사용하여 쿼리와 문서를 희소 공간에 표현하는 방법으로, 어휘의 역할과 검색 효율성 및 효과성의 관계에 대한 연구는 부족했다.
- 2. 100K 크기의 출력 어휘를 가진 BERT 모델을 구축하여, ESPLADE 사전 학습 방법과 랜덤 초기화를 비교하고 실제 검색 클릭 로그로 미세 조정했다.
- 3. 실험 결과, 로그 점수 기반의 쿼리 및 문서 가지치기를 적용하면 두 모델 모두 32K 크기의 일반 SPLADE 모델보다 효율적이며, ESPLADE 모델이 랜덤 어휘 모델보다 더 효과적이었다.
- 4. 출력 어휘의 크기와 사전 학습 가중치는 검색 엔진에서 쿼리와 문서의 표현 사양을 구성하는 데 중요한 역할을 한다.
- 5. 어휘 구성에서의 표현 사양의 중요성을 인식함으로써 LSR의 효율성과 효과성을 개선할 수 있는 새로운 가능성을 제공한다.


---

*Generated on 2025-09-24 03:39:06*