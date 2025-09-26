---
keywords:
  - Multimodal Learning
  - Retrieval Augmented Generation
  - Position-Independent Caching
  - Multimodal Information Management
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2502.01960
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:37:29.277929",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Retrieval Augmented Generation",
    "Position-Independent Caching",
    "Multimodal Information Management"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.8,
    "Retrieval Augmented Generation": 0.79,
    "Position-Independent Caching": 0.72,
    "Multimodal Information Management": 0.71
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Large Language Model",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLM"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the growing field of integrating multiple data types in language models.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "Links to methods that enhance model outputs with external data retrieval.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Position-Independent Caching",
        "canonical": "Position-Independent Caching",
        "aliases": [
          "PIC"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel caching approach specific to this paper's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Multimodal Information Management",
        "canonical": "Multimodal Information Management",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Describes a specific technique for handling diverse data types efficiently.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.71
      }
    ],
    "ban_list_suggestions": [
      "context caching",
      "system-level challenges",
      "algorithm-level challenges"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Model",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Position-Independent Caching",
      "resolved_canonical": "Position-Independent Caching",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Multimodal Information Management",
      "resolved_canonical": "Multimodal Information Management",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.71
      }
    }
  ]
}
-->

# MPIC: Position-Independent Multimodal Context Caching System for Efficient MLLM Serving

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.01960.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2502.01960](https://arxiv.org/abs/2502.01960)

## 🔗 유사한 논문
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (85.8% similar)
- [[2025-09-23/PDTrim_ Targeted Pruning for Prefill-Decode Disaggregation in Inference_20250923|PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference]] (83.7% similar)
- [[2025-09-22/M-PACE_ Mother Child Framework for Multimodal Compliance_20250922|M-PACE: Mother Child Framework for Multimodal Compliance]] (83.5% similar)
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (83.2% similar)
- [[2025-09-22/MMAPG_ A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs_20250922|MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/Position-Independent Caching|Position-Independent Caching]], [[keywords/Multimodal Information Management|Multimodal Information Management]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.01960v2 Announce Type: replace 
Abstract: The context caching technique is employed to accelerate the Multimodal Large Language Model (MLLM) inference by prevailing serving platforms currently. However, this approach merely reuses the Key-Value (KV) cache of the initial sequence of prompt, resulting in full KV cache recomputation even if the prefix differs slightly. This becomes particularly inefficient in the context of interleaved text and images, as well as multimodal retrieval-augmented generation. This paper proposes position-independent caching as a more effective approach for multimodal information management. We have designed and implemented a caching system, named MPIC, to address both system-level and algorithm-level challenges. MPIC stores the KV cache on local disks when receiving multimodal data, and calculates and loads the KV cache in parallel during inference. To mitigate accuracy degradation, we have incorporated the integrated reuse and recompute mechanism within the system. The experimental results demonstrate that MPIC can achieve up to 54\% reduction in response time and 2$\times$ improvement in throughput compared to existing context caching systems, while maintaining negligible or no accuracy loss.

## 📝 요약

이 논문은 멀티모달 대형 언어 모델(MLLM) 추론을 가속화하기 위한 새로운 캐싱 시스템인 MPIC를 제안합니다. 기존의 문맥 캐싱 기법은 프롬프트의 초기 시퀀스의 키-값(KV) 캐시만 재사용하여, 프리픽스가 약간만 달라도 전체 KV 캐시를 다시 계산해야 하는 비효율성이 있었습니다. 특히 텍스트와 이미지가 섞인 경우나 멀티모달 검색-증강 생성에서 비효율적입니다. MPIC는 위치에 독립적인 캐싱 방식을 통해 이러한 문제를 해결하며, 시스템 및 알고리즘 수준의 도전 과제를 해결합니다. MPIC는 멀티모달 데이터를 받을 때 로컬 디스크에 KV 캐시를 저장하고, 추론 중 병렬로 계산 및 로드를 수행합니다. 실험 결과, MPIC는 기존 시스템 대비 응답 시간을 최대 54% 단축하고 처리량을 2배 향상시키면서도 정확도 손실이 거의 없음을 보여줍니다.

## 🎯 주요 포인트

- 1. 기존의 문맥 캐싱 기법은 초기 프롬프트의 키-값(KV) 캐시만 재사용하여 프리픽스가 약간만 달라도 전체 KV 캐시를 다시 계산해야 하는 비효율성을 초래합니다.
- 2. 본 논문은 위치 독립적인 캐싱을 제안하여 다중 모드 정보 관리의 효율성을 높입니다.
- 3. 제안된 MPIC 시스템은 멀티모달 데이터를 받을 때 로컬 디스크에 KV 캐시를 저장하고, 추론 시 병렬로 KV 캐시를 계산 및 로드합니다.
- 4. MPIC는 기존 문맥 캐싱 시스템 대비 최대 54%의 응답 시간 감소와 2배의 처리량 향상을 이루며, 정확도 손실은 거의 없습니다.
- 5. 시스템 내 통합 재사용 및 재계산 메커니즘을 도입하여 정확도 저하를 완화합니다.


---

*Generated on 2025-09-24 02:37:29*