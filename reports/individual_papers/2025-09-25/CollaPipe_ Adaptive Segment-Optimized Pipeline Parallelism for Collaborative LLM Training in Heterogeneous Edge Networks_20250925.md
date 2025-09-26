---
keywords:
  - Large Language Model
  - Pipeline Parallelism
  - Federated Learning
  - Dynamic Resource Allocation
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19855
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:51:42.443876",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Pipeline Parallelism",
    "Federated Learning",
    "Dynamic Resource Allocation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Pipeline Parallelism": 0.78,
    "Federated Learning": 0.8,
    "Dynamic Resource Allocation": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer-based large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Transformer LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus on collaborative training in edge networks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "pipeline parallelism",
        "canonical": "Pipeline Parallelism",
        "aliases": [
          "pipeline training",
          "parallel training"
        ],
        "category": "specific_connectable",
        "rationale": "Pipeline parallelism is a key technique discussed for optimizing model training in distributed environments.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "federated aggregation",
        "canonical": "Federated Learning",
        "aliases": [
          "federated model aggregation"
        ],
        "category": "specific_connectable",
        "rationale": "Federated aggregation is crucial for the collaborative aspect of the training framework described.",
        "novelty_score": 0.7,
        "connectivity_score": 0.82,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Dynamic Segment Scheduling and Resource Allocation",
        "canonical": "Dynamic Resource Allocation",
        "aliases": [
          "DSSDA algorithm"
        ],
        "category": "unique_technical",
        "rationale": "The DSSDA algorithm is a novel contribution of the paper, optimizing resource allocation for training.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "mobile edge computing",
      "self-evolving intelligent networks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer-based large language models",
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
      "candidate_surface": "pipeline parallelism",
      "resolved_canonical": "Pipeline Parallelism",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "federated aggregation",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.82,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Dynamic Segment Scheduling and Resource Allocation",
      "resolved_canonical": "Dynamic Resource Allocation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# CollaPipe: Adaptive Segment-Optimized Pipeline Parallelism for Collaborative LLM Training in Heterogeneous Edge Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19855.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19855](https://arxiv.org/abs/2509.19855)

## 🔗 유사한 논문
- [[2025-09-24/PipelineRL_ Faster On-policy Reinforcement Learning for Long Sequence Generatio_20250924|PipelineRL: Faster On-policy Reinforcement Learning for Long Sequence Generatio]] (83.9% similar)
- [[2025-09-22/Characterizing the Efficiency of Distributed Training_ A Power, Performance, and Thermal Perspective_20250922|Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective]] (83.8% similar)
- [[2025-09-19/{\lambda}Scale_ Enabling Fast Scaling for Serverless Large Language Model Inference_20250919|{\lambda}Scale: Enabling Fast Scaling for Serverless Large Language Model Inference]] (83.7% similar)
- [[2025-09-18/The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning_20250918|The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning]] (83.2% similar)
- [[2025-09-23/MobiZO_ Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines_20250923|MobiZO: Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Pipeline Parallelism|Pipeline Parallelism]], [[keywords/Federated Learning|Federated Learning]]
**⚡ Unique Technical**: [[keywords/Dynamic Resource Allocation|Dynamic Resource Allocation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19855v1 Announce Type: cross 
Abstract: The increasing demand for intelligent mobile applications has made multi-agent collaboration with Transformer-based large language models (LLMs) essential in mobile edge computing (MEC) networks. However, training LLMs in such environments remains challenging due to heavy computation, high end-to-end latency, and limited model generalization. We introduce CollaPipe, a hybrid distributed learning framework that integrates collaborative pipeline parallelism with federated aggregation to support self-evolving intelligent networks. In CollaPipe, the encoder part is adaptively partitioned into variable-sized segments and deployed across mobile devices for pipeline-parallel training, while the decoder is deployed on edge servers to handle generative tasks. Then we perform global model update via federated aggregation. To enhance training efficiency, we formulate a joint optimization problem that adaptively allocates model segments, micro-batches, bandwidth, and transmission power. We derive and use a closed-form convergence bound to design an Dynamic Segment Scheduling and Resource Allocation (DSSDA) algorithm based on Lyapunov optimization, ensuring system stability under long-term constraints. Extensive experiments on downstream tasks with Transformer and BERT models show that CollaPipe improves computation efficiency by up to 15.09%, reduces end-to-end latency by at least 48.98%, and cuts single device memory usage by more than half, enabling online learning in heterogeneous and dynamic communication environments.

## 📝 요약

이 논문에서는 모바일 엣지 컴퓨팅 네트워크에서 대규모 언어 모델(LLM)의 다중 에이전트 협업을 지원하기 위한 하이브리드 분산 학습 프레임워크인 CollaPipe를 제안합니다. CollaPipe는 협업 파이프라인 병렬 처리와 연합 집계를 결합하여 모델의 자가 진화를 돕습니다. 인코더는 가변 크기의 세그먼트로 나뉘어 모바일 장치에 배포되고, 디코더는 엣지 서버에 배포되어 생성 작업을 처리합니다. 효율적인 학습을 위해 모델 세그먼트, 마이크로 배치, 대역폭, 전송 전력을 최적화하는 문제를 설정하고, Lyapunov 최적화를 기반으로 한 동적 세그먼트 스케줄링 및 자원 할당 알고리즘(DSSDA)을 설계합니다. 실험 결과, CollaPipe는 계산 효율성을 최대 15.09% 향상시키고, 지연 시간을 최소 48.98% 줄이며, 단일 장치 메모리 사용량을 절반 이상 감소시켜 이기종 및 동적 통신 환경에서의 온라인 학습을 가능하게 합니다.

## 🎯 주요 포인트

- 1. CollaPipe는 협업 파이프라인 병렬 처리와 연합 집계를 통합한 하이브리드 분산 학습 프레임워크입니다.
- 2. 인코더는 가변 크기의 세그먼트로 분할되어 모바일 장치에 배포되고, 디코더는 엣지 서버에 배포되어 생성 작업을 처리합니다.
- 3. 모델 세그먼트, 마이크로 배치, 대역폭 및 전송 전력을 적응적으로 할당하는 공동 최적화 문제를 공식화하여 학습 효율성을 향상시킵니다.
- 4. Lyapunov 최적화에 기반한 동적 세그먼트 스케줄링 및 자원 할당 알고리즘(DSSDA)을 설계하여 장기 제약 조건 하에서 시스템 안정성을 보장합니다.
- 5. 실험 결과, CollaPipe는 계산 효율성을 최대 15.09% 향상시키고, 종단 간 지연을 최소 48.98% 줄이며, 단일 장치 메모리 사용량을 절반 이상 감소시킵니다.


---

*Generated on 2025-09-25 15:51:42*