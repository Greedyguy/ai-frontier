---
keywords:
  - Distributed Prefix Caching
  - Key-Value Cache
  - Smart Network Interface Card
  - Large Language Model Serving
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16857
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:35:50.155996",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Distributed Prefix Caching",
    "Key-Value Cache",
    "Smart Network Interface Card",
    "Large Language Model Serving"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Distributed Prefix Caching": 0.78,
    "Key-Value Cache": 0.8,
    "Smart Network Interface Card": 0.77,
    "Large Language Model Serving": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Distributed prefix caching",
        "canonical": "Distributed Prefix Caching",
        "aliases": [
          "Prefix Caching",
          "Distributed Caching"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's contribution and represents a unique approach to optimizing LLM serving.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "KV cache",
        "canonical": "Key-Value Cache",
        "aliases": [
          "KV Cache",
          "Key-Value Store"
        ],
        "category": "specific_connectable",
        "rationale": "Key-Value caching is a specific technique that can be linked to broader caching strategies in distributed systems.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "SmartNIC",
        "canonical": "Smart Network Interface Card",
        "aliases": [
          "SmartNIC",
          "Programmable NIC"
        ],
        "category": "specific_connectable",
        "rationale": "SmartNICs are increasingly relevant in optimizing data plane operations, providing strong connectivity to network optimization topics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "LLM serving",
        "canonical": "Large Language Model Serving",
        "aliases": [
          "LLM Deployment",
          "Language Model Serving"
        ],
        "category": "broad_technical",
        "rationale": "Serving large language models is a broad technical concept that connects to various deployment strategies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "compression",
      "decompression",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Distributed prefix caching",
      "resolved_canonical": "Distributed Prefix Caching",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "KV cache",
      "resolved_canonical": "Key-Value Cache",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "SmartNIC",
      "resolved_canonical": "Smart Network Interface Card",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "LLM serving",
      "resolved_canonical": "Large Language Model Serving",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# ShadowServe: Interference-Free KV Cache Fetching for Distributed Prefix Caching

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16857.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16857](https://arxiv.org/abs/2509.16857)

## 🔗 유사한 논문
- [[2025-09-19/Taming Serverless Cold Starts Through OS Co-Design_20250919|Taming Serverless Cold Starts Through OS Co-Design]] (80.3% similar)
- [[2025-09-19/{\lambda}Scale_ Enabling Fast Scaling for Serverless Large Language Model Inference_20250919|{\lambda}Scale: Enabling Fast Scaling for Serverless Large Language Model Inference]] (79.4% similar)
- [[2025-09-22/KVCompose_ Efficient Structured KV Cache Compression with Composite Tokens_20250922|KVCompose: Efficient Structured KV Cache Compression with Composite Tokens]] (79.1% similar)
- [[2025-09-22/ForestColl_ Throughput-Optimal Collective Communications on Heterogeneous Network Fabrics_20250922|ForestColl: Throughput-Optimal Collective Communications on Heterogeneous Network Fabrics]] (78.9% similar)
- [[2025-09-19/MaRVIn_ A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration_20250919|MaRVIn: A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (78.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model Serving|Large Language Model Serving]]
**🔗 Specific Connectable**: [[keywords/Key-Value Cache|Key-Value Cache]], [[keywords/Smart Network Interface Card|Smart Network Interface Card]]
**⚡ Unique Technical**: [[keywords/Distributed Prefix Caching|Distributed Prefix Caching]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16857v1 Announce Type: cross 
Abstract: Distributed prefix caching accelerates long-context LLM serving by reusing KV cache entries for common context prefixes. However, KV cache fetches can become a bottleneck when network bandwidth is limited. Compression mitigates the bandwidth issue, but can degrade overall performance when decompression interferes with model computation.
  We present ShadowServe, the first SmartNIC-accelerated, interference-free prefix caching system for LLM serving. ShadowServe separates a control plane on the host and a data plane fully offloaded to the SmartNIC, which eliminates interference to both host GPU and CPU. To overcome the SmartNIC's limited compute and memory resources, we design a chunked pipeline that parallelizes data plane operations across the SmartNIC's compute resources, and a minimal-copy memory management scheme that reduces memory pressure on the SmartNIC. Compared to state-of-the-art solutions, ShadowServe achieves up to 2.2x lower loaded time-per-output-token (TPOT), and reduces time-to-first-token (TTFT) by up to 1.38x in low-bandwidth scenarios (<= 20 Gbps), translating to up to 1.35x higher throughput.

## 📝 요약

ShadowServe는 LLM 서비스에서 긴 맥락을 가속화하기 위한 SmartNIC 기반의 간섭 없는 접두사 캐싱 시스템입니다. 기존의 분산 접두사 캐싱은 네트워크 대역폭이 제한될 때 병목 현상이 발생할 수 있으며, 압축은 대역폭 문제를 완화하지만 모델 계산에 간섭을 줄 수 있습니다. ShadowServe는 호스트의 제어 평면과 SmartNIC에 완전히 오프로드된 데이터 평면을 분리하여 이러한 간섭을 제거합니다. SmartNIC의 제한된 자원을 극복하기 위해 데이터 평면 작업을 병렬화하는 청크 파이프라인과 메모리 압박을 줄이는 최소 복사 메모리 관리 방식을 설계했습니다. ShadowServe는 최신 솔루션 대비 출력 토큰당 시간(TPOT)을 최대 2.2배, 첫 번째 토큰까지의 시간(TTFT)을 최대 1.38배 단축하여 최대 1.35배 높은 처리량을 제공합니다.

## 🎯 주요 포인트

- 1. ShadowServe는 SmartNIC을 활용하여 LLM 서비스에서 간섭 없는 접두사 캐싱 시스템을 구현합니다.
- 2. ShadowServe는 호스트의 제어 평면과 SmartNIC에 완전히 오프로드된 데이터 평면을 분리하여 GPU 및 CPU 간섭을 제거합니다.
- 3. 제한된 SmartNIC의 계산 및 메모리 자원을 극복하기 위해 데이터 평면 작업을 병렬화하는 청크 파이프라인과 최소 복사 메모리 관리 방식을 설계했습니다.
- 4. ShadowServe는 최신 솔루션과 비교하여 최대 2.2배 낮은 출력 토큰당 로드 시간을 달성하고, 저대역폭 시나리오에서 첫 번째 토큰까지의 시간을 최대 1.38배 단축합니다.
- 5. 이러한 개선은 최대 1.35배 높은 처리량으로 이어집니다.


---

*Generated on 2025-09-23 23:35:50*