<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:14:45.435555",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Trusted Execution Environment",
    "Confidential Computing",
    "Intel SGX"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Trusted Execution Environment": 0.78,
    "Confidential Computing": 0.77,
    "Intel SGX": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's focus on confidential inference, providing a strong link to existing research on language models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Trusted Execution Environments",
        "canonical": "Trusted Execution Environment",
        "aliases": [
          "TEEs"
        ],
        "category": "unique_technical",
        "rationale": "TEEs are a novel solution proposed for securing LLM inference, making them a unique technical focus of the paper.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Confidential Compute GPUs",
        "canonical": "Confidential Computing",
        "aliases": [
          "Confidential GPUs"
        ],
        "category": "specific_connectable",
        "rationale": "Confidential computing is a key aspect of the paper's exploration of secure inference environments.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "Intel's TDX and SGX",
        "canonical": "Intel SGX",
        "aliases": [
          "Intel TDX"
        ],
        "category": "unique_technical",
        "rationale": "Intel's TEEs are specifically evaluated in the paper, highlighting their role in secure LLM inference.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "cost",
      "security trade-offs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Trusted Execution Environments",
      "resolved_canonical": "Trusted Execution Environment",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Confidential Compute GPUs",
      "resolved_canonical": "Confidential Computing",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Intel's TDX and SGX",
      "resolved_canonical": "Intel SGX",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Confidential LLM Inference: Performance and Cost Across CPU and GPU TEEs

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18886.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18886](https://arxiv.org/abs/2509.18886)

## 🔗 유사한 논문
- [[2025-09-22/Characterizing the Efficiency of Distributed Training_ A Power, Performance, and Thermal Perspective_20250922|Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective]] (84.1% similar)
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (83.7% similar)
- [[2025-09-23/TranSQL+_ Serving Large Language Models with SQL on Low-Resource Hardware_20250923|TranSQL+: Serving Large Language Models with SQL on Low-Resource Hardware]] (83.7% similar)
- [[2025-09-23/Large Language Models for Cyber Security_ A Systematic Literature Review_20250923|Large Language Models for Cyber Security: A Systematic Literature Review]] (83.4% similar)
- [[2025-09-23/Robust LLM Training Infrastructure at ByteDance_20250923|Robust LLM Training Infrastructure at ByteDance]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Confidential Computing|Confidential Computing]]
**⚡ Unique Technical**: [[keywords/Trusted Execution Environment|Trusted Execution Environment]], [[keywords/Intel SGX|Intel SGX]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18886v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) are increasingly deployed on converged Cloud and High-Performance Computing (HPC) infrastructure. However, as LLMs handle confidential inputs and are fine-tuned on costly, proprietary datasets, their heightened security requirements slow adoption in privacy-sensitive sectors such as healthcare and finance. We investigate methods to address this gap and propose Trusted Execution Environments (TEEs) as a solution for securing end-to-end LLM inference. We validate their practicality by evaluating these compute-intensive workloads entirely within CPU and GPU TEEs. On the CPU side, we conduct an in-depth study running full Llama2 inference pipelines (7B, 13B, 70B) inside Intel's TDX and SGX, accelerated by Advanced Matrix Extensions (AMX). We derive 12 insights, including that across various data types, batch sizes, and input lengths, CPU TEEs impose under 10% throughput and 20% latency overheads, further reduced by AMX. We run LLM inference on NVIDIA H100 Confidential Compute GPUs, contextualizing our CPU findings and observing throughput penalties of 4-8% that diminish as batch and input sizes grow. By comparing performance, cost, and security trade-offs, we show how CPU TEEs can be more cost-effective or secure than their GPU counterparts. To our knowledge, our work is the first to comprehensively demonstrate the performance and practicality of modern TEEs across both CPUs and GPUs for enabling confidential LLMs (cLLMs).

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 보안을 강화하기 위해 신뢰 실행 환경(TEE)을 제안합니다. 특히, 의료 및 금융 분야에서의 민감한 데이터 처리에 있어 LLM의 보안 요구 사항이 높은 점을 해결하고자 합니다. 연구에서는 CPU와 GPU TEE에서 LLM 추론을 수행하며, Intel의 TDX와 SGX를 사용하여 Llama2 모델을 실행하고, Advanced Matrix Extensions(AMX)로 성능을 향상시킵니다. CPU TEE는 다양한 데이터 유형, 배치 크기, 입력 길이에 대해 10% 미만의 처리량 및 20% 미만의 지연 오버헤드를 보이며, AMX로 이를 더욱 줄일 수 있음을 발견했습니다. 또한, NVIDIA H100 Confidential Compute GPU에서의 실행 결과, 배치 및 입력 크기가 증가함에 따라 4-8%의 처리량 패널티가 감소하는 것을 관찰했습니다. 이 연구는 CPU와 GPU TEE의 성능, 비용, 보안의 균형을 비교하며, CPU TEE가 더 비용 효율적이거나 보안적일 수 있음을 보여줍니다. 이는 현대 TEE를 사용하여 기밀 LLM을 구현한 최초의 포괄적 연구입니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 보안 문제를 해결하기 위해 신뢰 실행 환경(TEE)을 제안합니다.
- 2. CPU와 GPU TEE 내에서 LLM 추론 작업의 실용성을 검증하였습니다.
- 3. CPU TEE는 다양한 데이터 유형, 배치 크기, 입력 길이에 대해 10% 미만의 처리량 및 20%의 지연 오버헤드를 보입니다.
- 4. GPU TEE에서는 배치 및 입력 크기가 증가함에 따라 4-8%의 처리량 패널티가 감소합니다.
- 5. CPU TEE는 GPU TEE보다 비용 효율적이거나 보안성이 높을 수 있음을 보여줍니다.


---

*Generated on 2025-09-24 15:14:45*