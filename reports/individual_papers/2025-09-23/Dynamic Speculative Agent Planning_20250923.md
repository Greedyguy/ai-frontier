---
keywords:
  - Dynamic Speculative Planning
  - Large Language Model
  - Asynchronous Online Reinforcement Learning
  - Lossless Acceleration
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.01920
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:32:23.307434",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dynamic Speculative Planning",
    "Large Language Model",
    "Asynchronous Online Reinforcement Learning",
    "Lossless Acceleration"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dynamic Speculative Planning": 0.8,
    "Large Language Model": 0.85,
    "Asynchronous Online Reinforcement Learning": 0.78,
    "Lossless Acceleration": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Dynamic Speculative Planning",
        "canonical": "Dynamic Speculative Planning",
        "aliases": [
          "DSP"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework for lossless acceleration in language model-based agents, crucial for linking recent advancements in reinforcement learning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's discussion on improving inference efficiency and cost-effectiveness.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Asynchronous Online Reinforcement Learning",
        "canonical": "Asynchronous Online Reinforcement Learning",
        "aliases": [
          "AORL"
        ],
        "category": "unique_technical",
        "rationale": "Describes the specific learning approach used in DSP, enabling connections to reinforcement learning techniques.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Lossless Acceleration",
        "canonical": "Lossless Acceleration",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Key concept in the paper's framework, relevant for discussions on efficient computation in AI systems.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "cost",
      "system"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Dynamic Speculative Planning",
      "resolved_canonical": "Dynamic Speculative Planning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Asynchronous Online Reinforcement Learning",
      "resolved_canonical": "Asynchronous Online Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Lossless Acceleration",
      "resolved_canonical": "Lossless Acceleration",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Dynamic Speculative Agent Planning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.01920.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.01920](https://arxiv.org/abs/2509.01920)

## 🔗 유사한 논문
- [[2025-09-19/(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low: A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (82.7% similar)
- [[2025-09-19/Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (82.2% similar)
- [[2025-09-23/Spiffy_ Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding_20250923|Spiffy: Multiplying Diffusion LLM Acceleration via Lossless Speculative Decoding]] (82.0% similar)
- [[2025-09-22/Online Robust Planning under Model Uncertainty_ A Sample-Based Approach_20250922|Online Robust Planning under Model Uncertainty: A Sample-Based Approach]] (81.9% similar)
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Lossless Acceleration|Lossless Acceleration]]
**⚡ Unique Technical**: [[keywords/Dynamic Speculative Planning|Dynamic Speculative Planning]], [[keywords/Asynchronous Online Reinforcement Learning|Asynchronous Online Reinforcement Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.01920v3 Announce Type: replace 
Abstract: Despite their remarkable success in complex tasks propelling widespread adoption, large language-model-based agents still face critical deployment challenges due to prohibitive latency and inference costs. While recent work has explored various methods to accelerate inference, existing approaches suffer from significant limitations: they either fail to preserve performance fidelity, require extensive offline training of router modules, or incur excessive operational costs. Moreover, they provide minimal user control over the tradeoff between acceleration and other performance metrics. To address these gaps, we introduce Dynamic Speculative Planning (DSP), an asynchronous online reinforcement learning framework that provides lossless acceleration with substantially reduced costs without requiring additional pre-deployment preparation. DSP explicitly optimizes a joint objective balancing end-to-end latency against dollar cost, allowing practitioners to adjust a single parameter that steers the system toward faster responses, cheaper operation, or any point along this continuum. Experiments on two standard agent benchmarks demonstrate that DSP achieves comparable efficiency to the fastest lossless acceleration method while reducing total cost by 30% and unnecessary cost up to 60%. Our code and data are available through https://github.com/guanyilin428/Dynamic-Speculative-Planning.

## 📝 요약

이 논문은 대형 언어 모델 기반 에이전트의 배포 시 발생하는 지연 및 추론 비용 문제를 해결하기 위해 Dynamic Speculative Planning (DSP)이라는 비동기 온라인 강화 학습 프레임워크를 제안합니다. DSP는 성능 손실 없이 비용을 크게 줄이며, 사전 준비가 필요 없습니다. 이 방법은 지연 시간과 비용 간의 균형을 최적화하며, 사용자가 단일 매개변수를 조정하여 응답 속도와 비용 효율성을 조절할 수 있도록 합니다. 실험 결과, DSP는 가장 빠른 손실 없는 가속 방법과 유사한 효율성을 보이며, 총 비용을 30%, 불필요한 비용을 최대 60% 절감합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델 기반 에이전트는 높은 지연 시간과 추론 비용으로 인해 배포에 어려움을 겪고 있습니다.
- 2. 기존 가속화 방법은 성능 충실도를 유지하지 못하거나, 오프라인 라우터 모듈 훈련이 필요하거나, 운영 비용이 과도하게 듭니다.
- 3. Dynamic Speculative Planning(DSP)은 추가 사전 준비 없이 비용을 크게 줄이면서 손실 없는 가속화를 제공하는 비동기 온라인 강화 학습 프레임워크입니다.
- 4. DSP는 응답 속도와 비용 간의 균형을 최적화하며, 사용자가 단일 매개변수를 조정하여 시스템 성능을 제어할 수 있게 합니다.
- 5. 실험 결과, DSP는 가장 빠른 손실 없는 가속화 방법과 유사한 효율성을 유지하면서 총 비용을 30%, 불필요한 비용을 최대 60%까지 절감합니다.


---

*Generated on 2025-09-24 00:32:23*