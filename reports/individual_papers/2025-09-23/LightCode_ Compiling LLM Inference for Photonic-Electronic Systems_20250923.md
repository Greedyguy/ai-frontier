---
keywords:
  - Large Language Model
  - Photonic Tensor Units
  - Hybrid Photonic-Electronic Systems
  - Stacked Graph
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16443
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:19:53.131252",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Photonic Tensor Units",
    "Hybrid Photonic-Electronic Systems",
    "Stacked Graph"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Photonic Tensor Units": 0.78,
    "Hybrid Photonic-Electronic Systems": 0.77,
    "Stacked Graph": 0.79
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
        "rationale": "Large Language Models are central to the paper's focus on inference optimization, providing a strong link to existing research in NLP and machine learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Photonic Tensor Units",
        "canonical": "Photonic Tensor Units",
        "aliases": [
          "PTUs"
        ],
        "category": "unique_technical",
        "rationale": "Photonic Tensor Units represent a novel hardware component discussed in the paper, crucial for linking to emerging photonic computing research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hybrid Photonic-Electronic Systems",
        "canonical": "Hybrid Photonic-Electronic Systems",
        "aliases": [
          "Photonic-Electronic Systems"
        ],
        "category": "unique_technical",
        "rationale": "The hybrid systems are a unique focus of the paper, offering a new perspective on integrating different computational paradigms.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Stacked Graph",
        "canonical": "Stacked Graph",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The Stacked Graph is a novel intermediate representation introduced in the paper, essential for understanding the compilation strategy.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
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
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Photonic Tensor Units",
      "resolved_canonical": "Photonic Tensor Units",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hybrid Photonic-Electronic Systems",
      "resolved_canonical": "Hybrid Photonic-Electronic Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Stacked Graph",
      "resolved_canonical": "Stacked Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# LightCode: Compiling LLM Inference for Photonic-Electronic Systems

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16443.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16443](https://arxiv.org/abs/2509.16443)

## 🔗 유사한 논문
- [[2025-09-22/Characterizing the Efficiency of Distributed Training_ A Power, Performance, and Thermal Perspective_20250922|Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective]] (84.6% similar)
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (83.4% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (82.1% similar)
- [[2025-09-22/MigGPT_ Harnessing Large Language Models for Automated Migration of Out-of-Tree Linux Kernel Patches Across Versions_20250922|MigGPT: Harnessing Large Language Models for Automated Migration of Out-of-Tree Linux Kernel Patches Across Versions]] (82.0% similar)
- [[2025-09-18/The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning_20250918|The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Photonic Tensor Units|Photonic Tensor Units]], [[keywords/Hybrid Photonic-Electronic Systems|Hybrid Photonic-Electronic Systems]], [[keywords/Stacked Graph|Stacked Graph]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16443v1 Announce Type: cross 
Abstract: The growing demand for low-latency, energy-efficient inference in large language models (LLMs) has catalyzed interest in heterogeneous architectures. While GPUs remain dominant, they are poorly suited for integration with emerging domain-specific accelerators like the Photonic Tensor Units (PTUs), which offer low-power, high-throughput linear computation. This motivates hybrid compilation strategies that combine photonic and electronic resources. We present LightCode, a compiler framework and simulator for mapping LLM inference workloads across hybrid photonic-electronic systems. LightCode introduces the Stacked Graph, an intermediate representation that encodes multiple hardware-specific realizations of each tensor operation. Hardware assignment is formulated as a constrained subgraph selection problem optimized for latency or energy under parametric cost models. We evaluate LightCode on the prefill stage of GPT-2 and Llama-7B showing that under our workload and hardware assumptions, (i) Photonic hardware reduced energy by up to 50% in our simulated workloads at maximum sequence length; (ii) multiplexing and assignment strategy yielded latency improvements exceeding 10x; and (iii) Optimizing for latency or energy resulted in distinct hardware mappings in our simulations. LightCode offers a module, foundational framework and simulator for compiling LLMs to emerging photonic accelerators.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 추론 작업에서 낮은 지연 시간과 에너지 효율성을 달성하기 위한 이종 아키텍처에 대한 연구를 다룹니다. 주로 GPU가 사용되지만, 저전력 고처리량을 제공하는 포토닉 텐서 유닛(PTU)과의 통합에는 적합하지 않습니다. 이를 해결하기 위해 포토닉 및 전자 자원을 결합한 하이브리드 컴파일 전략을 제안합니다. LightCode는 이러한 하이브리드 시스템에서 LLM 추론 작업을 매핑하는 컴파일러 프레임워크 및 시뮬레이터로, 각 텐서 연산의 하드웨어별 구현을 인코딩하는 중간 표현인 Stacked Graph를 도입합니다. 하드웨어 할당은 지연 시간이나 에너지를 최적화하는 제약된 서브그래프 선택 문제로 공식화됩니다. GPT-2와 Llama-7B의 프리필 단계 평가 결과, 포토닉 하드웨어가 에너지를 최대 50% 절감하고, 멀티플렉싱 및 할당 전략이 지연 시간을 10배 이상 개선했으며, 지연 시간 또는 에너지 최적화에 따라 하드웨어 매핑이 달라짐을 보였습니다. LightCode는 포토닉 가속기에 LLM을 컴파일하기 위한 기본 프레임워크와 시뮬레이터를 제공합니다.

## 🎯 주요 포인트

- 1. LightCode는 대형 언어 모델의 추론 작업을 하이브리드 광전자 시스템에 매핑하는 컴파일러 프레임워크 및 시뮬레이터입니다.
- 2. Stacked Graph는 각 텐서 연산의 여러 하드웨어 특정 실현을 인코딩하는 중간 표현을 제공합니다.
- 3. LightCode는 GPT-2 및 Llama-7B의 prefill 단계에서 광자 하드웨어가 최대 시퀀스 길이에서 에너지를 최대 50%까지 절감할 수 있음을 보여줍니다.
- 4. 다중화 및 할당 전략을 통해 지연 시간이 10배 이상 개선되었습니다.
- 5. 지연 시간 또는 에너지 최적화는 시뮬레이션에서 서로 다른 하드웨어 매핑을 초래했습니다.


---

*Generated on 2025-09-23 23:19:53*