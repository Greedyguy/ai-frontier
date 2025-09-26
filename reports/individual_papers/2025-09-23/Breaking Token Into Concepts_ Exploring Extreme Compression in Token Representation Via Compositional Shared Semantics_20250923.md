---
keywords:
  - Aggregate Semantic Grouping
  - Product Quantization
  - Transformer
  - Cross-Lingual Transfer
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17737
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:32:15.666416",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Aggregate Semantic Grouping",
    "Product Quantization",
    "Transformer",
    "Cross-Lingual Transfer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Aggregate Semantic Grouping": 0.78,
    "Product Quantization": 0.7,
    "Transformer": 0.8,
    "Cross-Lingual Transfer": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Aggregate Semantic Grouping",
        "canonical": "Aggregate Semantic Grouping",
        "aliases": [
          "ASG"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for token representation that could be pivotal for future research in token compression.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Product Quantization",
        "canonical": "Product Quantization",
        "aliases": [
          "PQ"
        ],
        "category": "specific_connectable",
        "rationale": "A known technique in vector quantization, relevant for linking to compression and representation methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Transformer Architectures",
        "canonical": "Transformer",
        "aliases": [
          "mBERT",
          "XLM-R",
          "mT5"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are foundational in NLP, and connecting different architectures helps in understanding model variations.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Cross Lingual Transfer",
        "canonical": "Cross-Lingual Transfer",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Important for linking multilingual capabilities and transfer learning in NLP models.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "embedding parameters",
      "task performance",
      "base model"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Aggregate Semantic Grouping",
      "resolved_canonical": "Aggregate Semantic Grouping",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Product Quantization",
      "resolved_canonical": "Product Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Transformer Architectures",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Cross Lingual Transfer",
      "resolved_canonical": "Cross-Lingual Transfer",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Breaking Token Into Concepts: Exploring Extreme Compression in Token Representation Via Compositional Shared Semantics

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17737.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17737](https://arxiv.org/abs/2509.17737)

## 🔗 유사한 논문
- [[2025-09-23/Language Modeling with Learned Meta-Tokens_20250923|Language Modeling with Learned Meta-Tokens]] (83.2% similar)
- [[2025-09-23/EG-MLA_ Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs_20250923|EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs]] (83.0% similar)
- [[2025-09-23/VQToken_ Neural Discrete Token Representation Learning for Extreme Token Reduction in Video Large Language Models_20250923|VQToken: Neural Discrete Token Representation Learning for Extreme Token Reduction in Video Large Language Models]] (83.0% similar)
- [[2025-09-23/Search-Optimized Quantization in Biomedical Ontology Alignment_20250923|Search-Optimized Quantization in Biomedical Ontology Alignment]] (82.7% similar)
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Product Quantization|Product Quantization]], [[keywords/Cross-Lingual Transfer|Cross-Lingual Transfer]]
**⚡ Unique Technical**: [[keywords/Aggregate Semantic Grouping|Aggregate Semantic Grouping]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17737v1 Announce Type: new 
Abstract: Standard language models employ unique, monolithic embeddings for each token, potentially limiting their ability to capture the multifaceted nature of word meanings. We investigate whether tokens can be more effectively represented through a compositional structure that accumulates diverse semantic facets. To explore this, we propose Aggregate Semantic Grouping (ASG), a novel approach leveraging Product Quantization (PQ). We apply ASG to standard transformer architectures (mBERT, XLM-R, mT5) and evaluate this representational scheme across diverse tasks (NLI, NER, QA), as well as a biomedical domain-specific benchmark (BC5CDR) using BioBERT. Our findings demonstrate that representing tokens compositionally via ASG achieves extreme compression in embedding parameters (0.4--0.5\%) while maintaining $>$95\% task performance relative to the base model, even in generative tasks and extends to both cross lingual transfer and domain-specific settings. These results validate the principle that tokens can be effectively modeled as combinations of shared semantic building blocks. ASG offers a simple yet concrete method for achieving this, showcasing how compositional representations can capture linguistic richness while enabling compact yet semantically rich models.

## 📝 요약

이 논문은 언어 모델에서 각 토큰을 단일 임베딩으로 표현하는 기존 방식의 한계를 극복하기 위해, 토큰을 다양한 의미적 측면으로 구성된 구조로 표현하는 방법을 제안합니다. 이를 위해 Product Quantization(PQ)을 활용한 Aggregate Semantic Grouping(ASG) 접근법을 소개하고, 이를 mBERT, XLM-R, mT5 등의 변형 모델에 적용하여 다양한 과제(NLI, NER, QA) 및 생의학 분야(BioBERT)에서 평가했습니다. 연구 결과, ASG를 통해 임베딩 파라미터를 극도로 압축(0.4-0.5%)하면서도 기본 모델 대비 95% 이상의 성능을 유지할 수 있음을 확인했습니다. 이는 토큰을 공유된 의미적 구성 요소의 조합으로 효과적으로 모델링할 수 있음을 입증하며, ASG가 언어의 풍부함을 포착하면서도 컴팩트한 모델을 가능하게 하는 방법임을 보여줍니다.

## 🎯 주요 포인트

- 1. 기존 언어 모델의 단일 임베딩 방식은 단어의 다면적 의미를 포착하는 데 한계가 있을 수 있다.
- 2. Aggregate Semantic Grouping (ASG)은 Product Quantization (PQ)을 활용하여 토큰을 조합적으로 표현하는 새로운 접근법이다.
- 3. ASG는 다양한 작업(NLI, NER, QA) 및 생물의학 분야(BioBERT)를 포함한 벤치마크에서 높은 성능을 유지하면서 임베딩 파라미터를 극도로 압축한다.
- 4. ASG는 기본 모델 대비 95% 이상의 작업 성능을 유지하면서도 임베딩 파라미터를 0.4-0.5% 수준으로 압축할 수 있다.
- 5. ASG는 언어의 풍부함을 포착하면서도 컴팩트하고 의미적으로 풍부한 모델을 가능하게 한다.


---

*Generated on 2025-09-24 03:32:15*