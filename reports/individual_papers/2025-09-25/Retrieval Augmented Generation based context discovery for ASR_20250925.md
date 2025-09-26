---
keywords:
  - Retrieval Augmented Generation
  - Automatic Speech Recognition
  - Large Language Model
  - Context Discovery
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2509.19567
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:42:58.807708",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Retrieval Augmented Generation",
    "Automatic Speech Recognition",
    "Large Language Model",
    "Context Discovery"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Retrieval Augmented Generation": 0.82,
    "Automatic Speech Recognition": 0.78,
    "Large Language Model": 0.8,
    "Context Discovery": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Retrieval Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "RAG is a trending approach in ASR and connects well with retrieval and generation techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Automatic Speech Recognition",
        "canonical": "Automatic Speech Recognition",
        "aliases": [
          "ASR"
        ],
        "category": "broad_technical",
        "rationale": "ASR is a fundamental technology in the field of speech processing and connects to various speech-related research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are crucial for context generation and correction in ASR, linking to broader NLP advancements.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Context Discovery",
        "canonical": "Context Discovery",
        "aliases": [
          "Contextual Discovery"
        ],
        "category": "unique_technical",
        "rationale": "Context discovery is a unique challenge in ASR, enhancing the system's ability to handle rare terms.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "transcription accuracy",
      "post-recognition transcript correction"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Retrieval Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Automatic Speech Recognition",
      "resolved_canonical": "Automatic Speech Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Context Discovery",
      "resolved_canonical": "Context Discovery",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Retrieval Augmented Generation based context discovery for ASR

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19567.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2509.19567](https://arxiv.org/abs/2509.19567)

## 🔗 유사한 논문
- [[2025-09-23/AttnComp_ Attention-Guided Adaptive Context Compression for Retrieval-Augmented Generation_20250923|AttnComp: Attention-Guided Adaptive Context Compression for Retrieval-Augmented Generation]] (87.2% similar)
- [[2025-09-25/Enhancing RAG Efficiency with Adaptive Context Compression_20250925|Enhancing RAG Efficiency with Adaptive Context Compression]] (85.4% similar)
- [[2025-09-22/Relevance to Utility_ Process-Supervised Rewrite for RAG_20250922|Relevance to Utility: Process-Supervised Rewrite for RAG]] (84.9% similar)
- [[2025-09-22/CORE-RAG_ Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning_20250922|CORE-RAG: Lossless Compression for Retrieval-Augmented LLMs via Reinforcement Learning]] (84.5% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Automatic Speech Recognition|Automatic Speech Recognition]], [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Context Discovery|Context Discovery]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19567v1 Announce Type: new 
Abstract: This work investigates retrieval augmented generation as an efficient strategy for automatic context discovery in context-aware Automatic Speech Recognition (ASR) system, in order to improve transcription accuracy in the presence of rare or out-of-vocabulary terms. However, identifying the right context automatically remains an open challenge. This work proposes an efficient embedding-based retrieval approach for automatic context discovery in ASR. To contextualize its effectiveness, two alternatives based on large language models (LLMs) are also evaluated: (1) large language model (LLM)-based context generation via prompting, and (2) post-recognition transcript correction using LLMs. Experiments on the TED-LIUMv3, Earnings21 and SPGISpeech demonstrate that the proposed approach reduces WER by up to 17% (percentage difference) relative to using no-context, while the oracle context results in a reduction of up to 24.1%.

## 📝 요약

이 연구는 희귀하거나 어휘에 없는 용어가 있을 때 전사 정확도를 향상시키기 위해 문맥 인식 자동 음성 인식(ASR) 시스템에서 자동 문맥 발견을 위한 효율적인 전략으로 검색 증강 생성을 조사합니다. 제안된 방법은 효율적인 임베딩 기반 검색 접근법으로, 대형 언어 모델(LLM)을 활용한 문맥 생성 및 후처리 전사 수정과 비교됩니다. TED-LIUMv3, Earnings21, SPGISpeech 데이터셋 실험 결과, 제안된 방법은 문맥을 사용하지 않은 경우에 비해 단어 오류율(WER)을 최대 17%까지 감소시켰으며, 최적의 문맥 사용 시 최대 24.1%까지 감소시켰습니다.

## 🎯 주요 포인트

- 1. 이 연구는 희귀하거나 사전에 없는 용어가 있을 때 전사 정확도를 향상시키기 위해 문맥 인식 자동 음성 인식(ASR) 시스템에서 자동 문맥 발견을 위한 효율적인 전략으로 검색 증강 생성을 조사합니다.
- 2. 자동 문맥 발견을 위한 효율적인 임베딩 기반 검색 접근법을 제안합니다.
- 3. 대형 언어 모델(LLM)을 기반으로 한 두 가지 대안, 즉 프롬프트를 통한 문맥 생성과 인식 후 전사 수정이 평가됩니다.
- 4. TED-LIUMv3, Earnings21, SPGISpeech 실험에서 제안된 접근법은 문맥을 사용하지 않은 경우에 비해 최대 17%의 WER 감소를 보여줍니다.
- 5. 오라클 문맥의 경우 최대 24.1%의 WER 감소가 관찰됩니다.


---

*Generated on 2025-09-26 08:42:58*