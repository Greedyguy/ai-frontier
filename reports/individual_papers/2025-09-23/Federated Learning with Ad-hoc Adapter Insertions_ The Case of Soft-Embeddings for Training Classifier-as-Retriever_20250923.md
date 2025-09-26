---
keywords:
  - Federated Learning
  - Differential Privacy
  - Soft Embeddings
  - Classifier-as-Retriever
  - Retrieval Augmented Generation
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16508
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:38:43.791060",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Differential Privacy",
    "Soft Embeddings",
    "Classifier-as-Retriever",
    "Retrieval Augmented Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.85,
    "Differential Privacy": 0.8,
    "Soft Embeddings": 0.78,
    "Classifier-as-Retriever": 0.77,
    "Retrieval Augmented Generation": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Learning",
        "canonical": "Federated Learning",
        "aliases": [
          "FL"
        ],
        "category": "specific_connectable",
        "rationale": "Federated Learning is crucial for enabling privacy-preserving and efficient training across distributed devices, making it a key concept for linking.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Differential Privacy",
        "canonical": "Differential Privacy",
        "aliases": [
          "DP"
        ],
        "category": "specific_connectable",
        "rationale": "Differential Privacy is essential for ensuring privacy in federated learning, providing strong connectivity to privacy-preserving techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Soft Embeddings",
        "canonical": "Soft Embeddings",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Soft Embeddings represent a novel approach to enhance encoder capabilities, offering a unique technical link.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Classifier-as-Retriever",
        "canonical": "Classifier-as-Retriever",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This novel retrieval mechanism enhances the retrieval process, providing a unique technical concept for linking.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Retrieval Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending concept that integrates retrieval with generation, offering strong connectivity to current research trends.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "solution",
      "analysis"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Differential Privacy",
      "resolved_canonical": "Differential Privacy",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Soft Embeddings",
      "resolved_canonical": "Soft Embeddings",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Classifier-as-Retriever",
      "resolved_canonical": "Classifier-as-Retriever",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Retrieval Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Federated Learning with Ad-hoc Adapter Insertions: The Case of Soft-Embeddings for Training Classifier-as-Retriever

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16508.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16508](https://arxiv.org/abs/2509.16508)

## 🔗 유사한 논문
- [[2025-09-23/Large Language Models as End-to-end Combinatorial Optimization Solvers_20250923|Large Language Models as End-to-end Combinatorial Optimization Solvers]] (83.7% similar)
- [[2025-09-23/LightRetriever_ A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference_20250923|LightRetriever: A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference]] (83.5% similar)
- [[2025-09-23/DeepInsert_ Early Layer Bypass for Efficient and Performant Multimodal Understanding_20250923|DeepInsert: Early Layer Bypass for Efficient and Performant Multimodal Understanding]] (83.5% similar)
- [[2025-09-23/PDTrim_ Targeted Pruning for Prefill-Decode Disaggregation in Inference_20250923|PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference]] (83.4% similar)
- [[2025-09-23/Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning_20250923|Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Federated Learning|Federated Learning]], [[keywords/Differential Privacy|Differential Privacy]], [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Soft Embeddings|Soft Embeddings]], [[keywords/Classifier-as-Retriever|Classifier-as-Retriever]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16508v1 Announce Type: new 
Abstract: When existing retrieval-augmented generation (RAG) solutions are intended to be used for new knowledge domains, it is necessary to update their encoders, which are taken to be pretrained large language models (LLMs). However, fully finetuning these large models is compute- and memory-intensive, and even infeasible when deployed on resource-constrained edge devices. We propose a novel encoder architecture in this work that addresses this limitation by using a frozen small language model (SLM), which satisfies the memory constraints of edge devices, and inserting a small adapter network before the transformer blocks of the SLM. The trainable adapter takes the token embeddings of the new corpus and learns to produce enhanced soft embeddings for it, while requiring significantly less compute power to update than full fine-tuning. We further propose a novel retrieval mechanism by attaching a classifier head to the SLM encoder, which is trained to learn a similarity mapping of the input embeddings to their corresponding documents. Finally, to enable the online fine-tuning of both (i) the encoder soft embeddings and (ii) the classifier-as-retriever on edge devices, we adopt federated learning (FL) and differential privacy (DP) to achieve an efficient, privacy-preserving, and product-grade training solution. We conduct a theoretical analysis of our methodology, establishing convergence guarantees under mild assumptions on gradient variance when deployed for general smooth nonconvex loss functions. Through extensive numerical experiments, we demonstrate (i) the efficacy of obtaining soft embeddings to enhance the encoder, (ii) training a classifier to improve the retriever, and (iii) the role of FL in achieving speedup.

## 📝 요약

이 논문은 새로운 지식 도메인에 적용할 때 대규모 언어 모델(LLM)의 완전한 미세 조정이 어려운 문제를 해결하기 위해, 소형 언어 모델(SLM)과 어댑터 네트워크를 활용한 새로운 인코더 아키텍처를 제안합니다. 이 방법은 엣지 디바이스의 메모리 제약을 만족시키며, 새로운 코퍼스의 토큰 임베딩을 개선된 소프트 임베딩으로 변환합니다. 또한, SLM 인코더에 분류기 헤드를 부착하여 입력 임베딩과 문서 간의 유사성을 학습하는 새로운 검색 메커니즘을 제안합니다. 엣지 디바이스에서의 온라인 미세 조정을 위해 연합 학습(FL)과 차등 프라이버시(DP)를 도입하여 효율적이고 프라이버시를 보장하는 학습 솔루션을 제공합니다. 이 방법론의 수렴성을 이론적으로 분석하고, 수치 실험을 통해 소프트 임베딩의 효과, 검색기 성능 향상, FL의 속도 향상 역할을 입증합니다.

## 🎯 주요 포인트

- 1. 새로운 지식 도메인에 적용하기 위해 기존의 RAG 솔루션의 인코더 업데이트가 필요하지만, 대형 언어 모델의 전체 미세 조정은 자원 제약이 있는 엣지 디바이스에서는 비현실적입니다.
- 2. 본 연구에서는 작은 언어 모델(SLM)을 고정하고, SLM의 트랜스포머 블록 앞에 작은 어댑터 네트워크를 삽입하는 새로운 인코더 아키텍처를 제안합니다.
- 3. 제안된 어댑터는 새로운 코퍼스의 토큰 임베딩을 받아 강화된 소프트 임베딩을 생성하며, 전체 미세 조정보다 적은 계산 자원을 필요로 합니다.
- 4. SLM 인코더에 분류기 헤드를 부착하여 입력 임베딩과 해당 문서 간의 유사성 매핑을 학습하는 새로운 검색 메커니즘을 제안합니다.
- 5. 엣지 디바이스에서 인코더 소프트 임베딩과 분류기를 온라인 미세 조정하기 위해 연합 학습과 차등 프라이버시를 채택하여 효율적이고 프라이버시를 보장하는 학습 솔루션을 구현합니다.


---

*Generated on 2025-09-24 01:38:43*