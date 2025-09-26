---
keywords:
  - Hierarchical Retrieval
  - Dual Encoder
  - Pretrain-Finetune Strategy
  - WordNet
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16411
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:08:14.932959",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hierarchical Retrieval",
    "Dual Encoder",
    "Pretrain-Finetune Strategy",
    "WordNet"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hierarchical Retrieval": 0.8,
    "Dual Encoder": 0.7,
    "Pretrain-Finetune Strategy": 0.78,
    "WordNet": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hierarchical Retrieval",
        "canonical": "Hierarchical Retrieval",
        "aliases": [
          "HR"
        ],
        "category": "unique_technical",
        "rationale": "Hierarchical Retrieval is a central concept in the paper, focusing on document retrieval within a hierarchy, which is not covered by existing canonical terms.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Dual Encoder",
        "canonical": "Dual Encoder",
        "aliases": [
          "DE"
        ],
        "category": "specific_connectable",
        "rationale": "Dual Encoder models are pivotal in the paper's methodology for embedding queries and documents, offering strong connectivity to retrieval methods.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      },
      {
        "surface": "Pretrain-Finetune Recipe",
        "canonical": "Pretrain-Finetune Strategy",
        "aliases": [
          "Pretrain-Finetune"
        ],
        "category": "specific_connectable",
        "rationale": "The pretrain-finetune approach is a key innovation in the paper, enhancing retrieval performance and linking to broader training strategies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "WordNet",
        "canonical": "WordNet",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "WordNet is used as a realistic hierarchy for experiments, providing a strong link to lexical databases and semantic hierarchies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "embedding space",
      "retrieval accuracy",
      "document set"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Hierarchical Retrieval",
      "resolved_canonical": "Hierarchical Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Dual Encoder",
      "resolved_canonical": "Dual Encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Pretrain-Finetune Recipe",
      "resolved_canonical": "Pretrain-Finetune Strategy",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "WordNet",
      "resolved_canonical": "WordNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Hierarchical Retrieval: The Geometry and a Pretrain-Finetune Recipe

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16411.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16411](https://arxiv.org/abs/2509.16411)

## 🔗 유사한 논문
- [[2025-09-23/Federated Learning with Ad-hoc Adapter Insertions_ The Case of Soft-Embeddings for Training Classifier-as-Retriever_20250923|Federated Learning with Ad-hoc Adapter Insertions: The Case of Soft-Embeddings for Training Classifier-as-Retriever]] (80.6% similar)
- [[2025-09-22/Database-Augmented Query Representation for Information Retrieval_20250922|Database-Augmented Query Representation for Information Retrieval]] (80.5% similar)
- [[2025-09-23/MindRef_ Mimicking Human Memory for Hierarchical Reference Retrieval with Fine-Grained Location Awareness_20250923|MindRef: Mimicking Human Memory for Hierarchical Reference Retrieval with Fine-Grained Location Awareness]] (80.4% similar)
- [[2025-09-23/LightRetriever_ A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference_20250923|LightRetriever: A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference]] (79.5% similar)
- [[2025-09-23/DETACH_ Cross-domain Learning for Long-Horizon Tasks via Mixture of Disentangled Experts_20250923|DETACH: Cross-domain Learning for Long-Horizon Tasks via Mixture of Disentangled Experts]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Dual Encoder|Dual Encoder]], [[keywords/Pretrain-Finetune Strategy|Pretrain-Finetune Strategy]], [[keywords/WordNet|WordNet]]
**⚡ Unique Technical**: [[keywords/Hierarchical Retrieval|Hierarchical Retrieval]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16411v1 Announce Type: cross 
Abstract: Dual encoder (DE) models, where a pair of matching query and document are embedded into similar vector representations, are widely used in information retrieval due to their simplicity and scalability. However, the Euclidean geometry of the embedding space limits the expressive power of DEs, which may compromise their quality. This paper investigates such limitations in the context of hierarchical retrieval (HR), where the document set has a hierarchical structure and the matching documents for a query are all of its ancestors. We first prove that DEs are feasible for HR as long as the embedding dimension is linear in the depth of the hierarchy and logarithmic in the number of documents. Then we study the problem of learning such embeddings in a standard retrieval setup where DEs are trained on samples of matching query and document pairs. Our experiments reveal a lost-in-the-long-distance phenomenon, where retrieval accuracy degrades for documents further away in the hierarchy. To address this, we introduce a pretrain-finetune recipe that significantly improves long-distance retrieval without sacrificing performance on closer documents. We experiment on a realistic hierarchy from WordNet for retrieving documents at various levels of abstraction, and show that pretrain-finetune boosts the recall on long-distance pairs from 19% to 76%. Finally, we demonstrate that our method improves retrieval of relevant products on a shopping queries dataset.

## 📝 요약

이 논문은 정보 검색에서 사용되는 듀얼 인코더(DE) 모델의 한계를 계층적 검색(HR) 맥락에서 조사합니다. DE 모델은 쿼리와 문서를 유사한 벡터로 임베딩하지만, 임베딩 공간의 유클리드 기하학이 표현력을 제한할 수 있습니다. 연구는 DE가 계층의 깊이에 선형적이고 문서 수에 로그적일 때 HR에 적합함을 증명합니다. 실험 결과, 계층 구조에서 멀리 떨어진 문서의 검색 정확도가 떨어지는 현상을 발견했습니다. 이를 해결하기 위해 사전 학습 및 미세 조정 방법을 도입하여 장거리 검색 성능을 크게 향상시켰습니다. WordNet의 계층 구조 실험에서 장거리 쌍의 재현율이 19%에서 76%로 증가했으며, 쇼핑 쿼리 데이터셋에서도 관련 제품 검색이 개선됨을 보였습니다.

## 🎯 주요 포인트

- 1. 이중 인코더 모델(DE)은 정보 검색에서 간단하고 확장성이 뛰어나지만, 임베딩 공간의 유클리드 기하학이 표현력을 제한하여 품질에 영향을 미칠 수 있다.
- 2. 문서 집합이 계층 구조를 가지는 계층적 검색(HR)에서 DE의 한계를 조사하고, 임베딩 차원이 계층의 깊이에 선형이고 문서 수에 대해 로그형일 때 DE가 HR에 적합하다는 것을 증명했다.
- 3. 실험 결과, 계층 구조에서 멀리 떨어진 문서에 대한 검색 정확도가 저하되는 '장거리 손실' 현상이 나타났다.
- 4. 이를 해결하기 위해, 사전 학습-미세 조정 방법을 도입하여 가까운 문서의 성능을 희생하지 않으면서 장거리 검색 성능을 크게 향상시켰다.
- 5. WordNet의 현실적인 계층 구조에서 실험한 결과, 사전 학습-미세 조정 방법이 장거리 쌍에 대한 재현율을 19%에서 76%로 증가시켰다.


---

*Generated on 2025-09-24 02:08:14*