---
keywords:
  - Retrieval Augmented Generation
  - Process Supervision
  - Large Language Model
  - Open-Domain Question-Answering
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15577
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:05:38.218793",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "Process Supervision",
    "Large Language Model",
    "Open-Domain Question-Answering"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.85,
    "Process Supervision": 0.72,
    "Large Language Model": 0.8,
    "Open-Domain Question-Answering": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending concept in NLP that bridges retrieval and generation, enhancing connectivity with related research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Process Supervision",
        "canonical": "Process Supervision",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This novel approach directly optimizes generative models, offering a unique technical perspective.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are foundational in modern NLP, providing broad connectivity across various studies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Open-Domain Question-Answering",
        "canonical": "Open-Domain Question-Answering",
        "aliases": [
          "ODQA"
        ],
        "category": "specific_connectable",
        "rationale": "ODQA is a key application area for RAG systems, linking to numerous datasets and benchmarks.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "bridge modules",
      "empirical results",
      "retrieved documents"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Process Supervision",
      "resolved_canonical": "Process Supervision",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Open-Domain Question-Answering",
      "resolved_canonical": "Open-Domain Question-Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Relevance to Utility: Process-Supervised Rewrite for RAG

**Korean Title:** 유용성 관련성: RAG를 위한 프로세스 감독 재작성

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15577.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15577](https://arxiv.org/abs/2509.15577)

## 🔗 유사한 논문
- [[2025-09-19/Enhancing Retrieval Augmentation via Adversarial Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (86.1% similar)
- [[2025-09-22/CORE-RAG_ Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning_20250922|CORE-RAG: Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning]] (85.8% similar)
- [[2025-09-19/ImpRAG_ Retrieval-Augmented Generation with Implicit Queries_20250919|ImpRAG: Retrieval-Augmented Generation with Implicit Queries]] (85.7% similar)
- [[2025-09-19/AIP_ Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt_20250919|AIP: Subverting Retrieval-Augmented Generation via Adversarial Instructional Prompt]] (85.5% similar)
- [[2025-09-22/Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models_20250922|Query Optimization for Parametric Knowledge Refinement in Retrieval-Augmented Large Language Models]] (85.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]], [[keywords/Open-Domain Question-Answering|Open-Domain Question-Answering]]
**⚡ Unique Technical**: [[keywords/Process Supervision|Process Supervision]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15577v1 Announce Type: cross 
Abstract: Retrieval-Augmented Generation systems often suffer from a gap between optimizing retrieval relevance and generative utility: retrieved documents may be topically relevant but still lack the content needed for effective reasoning during generation. While existing "bridge" modules attempt to rewrite the retrieved text for better generation, we show how they fail to capture true document utility. In this work, we propose R2U, with a key distinction of directly optimizing to maximize the probability of generating a correct answer through process supervision. As such direct observation is expensive, we also propose approximating an efficient distillation pipeline by scaling the supervision from LLMs, which helps the smaller rewriter model generalize better. We evaluate our method across multiple open-domain question-answering benchmarks. The empirical results demonstrate consistent improvements over strong bridging baselines.

## 🔍 Abstract (한글 번역)

arXiv:2509.15577v1 발표 유형: 교차  
초록: 검색 증강 생성 시스템은 종종 검색 관련성 최적화와 생성적 유용성 사이의 격차로 고통받습니다. 검색된 문서는 주제적으로 관련이 있을 수 있지만, 생성 중 효과적인 추론에 필요한 내용을 여전히 결여할 수 있습니다. 기존의 "브리지" 모듈은 더 나은 생성을 위해 검색된 텍스트를 재작성하려고 시도하지만, 우리는 이들이 진정한 문서 유용성을 포착하지 못하는 방법을 보여줍니다. 이 연구에서는 R2U를 제안하며, 올바른 답변을 생성할 확률을 최대화하기 위해 직접 최적화하는 프로세스 감독을 통해 차별화된 접근 방식을 제시합니다. 이러한 직접 관찰은 비용이 많이 들기 때문에, 우리는 LLMs로부터의 감독을 확장하여 더 작은 재작성 모델이 더 잘 일반화할 수 있도록 돕는 효율적인 증류 파이프라인을 근사화하는 방법도 제안합니다. 우리는 다양한 오픈 도메인 질문-응답 벤치마크에서 우리의 방법을 평가합니다. 실험 결과는 강력한 브리지 기준선에 비해 일관된 개선을 보여줍니다.

## 📝 요약

이 논문은 검색 기반 생성 시스템에서 검색된 문서의 주제적 관련성과 생성 유용성 간의 차이를 해결하기 위한 새로운 접근법을 제안합니다. 기존의 "브리지" 모듈은 검색된 텍스트를 재작성하여 생성 품질을 향상시키려 하지만, 문서의 실제 유용성을 포착하지 못합니다. 이를 해결하기 위해, 우리는 R2U라는 방법을 제안하며, 올바른 답변을 생성할 확률을 최대화하도록 직접 최적화하는 프로세스 감독을 사용합니다. 이러한 직접 관찰이 비용이 많이 들기 때문에, 우리는 대규모 언어 모델(LLM)에서 감독을 확장하여 작은 재작성 모델이 더 잘 일반화할 수 있도록 효율적인 증류 파이프라인을 제안합니다. 여러 오픈 도메인 질문-응답 벤치마크에서 우리의 방법을 평가한 결과, 강력한 브리지 기준선보다 일관된 성능 향상을 보였습니다.

## 🎯 주요 포인트

- 1. Retrieval-Augmented Generation 시스템은 검색 관련성과 생성 유용성 간의 격차 문제를 겪습니다.
- 2. 기존의 "bridge" 모듈은 검색된 텍스트를 재작성하지만, 문서의 진정한 유용성을 포착하지 못합니다.
- 3. R2U는 정답 생성 확률을 최대화하기 위해 프로세스 감독을 통해 직접 최적화하는 방법을 제안합니다.
- 4. LLMs로부터 감독을 확장하여 효율적인 증류 파이프라인을 근사화함으로써 작은 재작성 모델이 더 잘 일반화할 수 있도록 돕습니다.
- 5. 다양한 오픈 도메인 질문-응답 벤치마크에서 평가한 결과, 강력한 브리징 기준선보다 일관된 개선을 보였습니다.


---

*Generated on 2025-09-23 09:05:38*