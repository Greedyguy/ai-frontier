<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:33:08.788044",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Phantora",
    "Hybrid Simulation",
    "GPU Cluster",
    "Containerized Environment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Phantora": 0.78,
    "Hybrid Simulation": 0.82,
    "GPU Cluster": 0.75,
    "Containerized Environment": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Phantora",
        "canonical": "Phantora",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Phantora is a novel hybrid GPU cluster simulator, providing a unique approach to ML performance estimation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "hybrid simulation",
        "canonical": "Hybrid Simulation",
        "aliases": [
          "hybrid GPU simulation"
        ],
        "category": "specific_connectable",
        "rationale": "Hybrid simulation offers a new method for performance estimation by reusing existing ML frameworks.",
        "novelty_score": 0.72,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "GPU cluster",
        "canonical": "GPU Cluster",
        "aliases": [
          "GPU server cluster"
        ],
        "category": "broad_technical",
        "rationale": "GPU clusters are essential for understanding the infrastructure used in ML training workloads.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      },
      {
        "surface": "containerized environment",
        "canonical": "Containerized Environment",
        "aliases": [
          "container environment"
        ],
        "category": "specific_connectable",
        "rationale": "Containerized environments are critical for simulating distributed ML frameworks effectively.",
        "novelty_score": 0.68,
        "connectivity_score": 0.77,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "performance estimation",
      "ML training workloads"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Phantora",
      "resolved_canonical": "Phantora",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "hybrid simulation",
      "resolved_canonical": "Hybrid Simulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "GPU cluster",
      "resolved_canonical": "GPU Cluster",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "containerized environment",
      "resolved_canonical": "Containerized Environment",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.77,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Phantora: Maximizing Code Reuse in Simulation-based Machine Learning System Performance Estimation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.01616.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2505.01616](https://arxiv.org/abs/2505.01616)

## 🔗 유사한 논문
- [[2025-09-23/Machine learning-driven conservative-to-primitive conversion in hybrid piecewise polytropic and tabulated equations of state_20250923|Machine learning-driven conservative-to-primitive conversion in hybrid piecewise polytropic and tabulated equations of state]] (82.3% similar)
- [[2025-09-22/Characterizing the Efficiency of Distributed Training_ A Power, Performance, and Thermal Perspective_20250922|Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective]] (81.7% similar)
- [[2025-09-23/LightCode_ Compiling LLM Inference for Photonic-Electronic Systems_20250923|LightCode: Compiling LLM Inference for Photonic-Electronic Systems]] (81.2% similar)
- [[2025-09-23/Robust LLM Training Infrastructure at ByteDance_20250923|Robust LLM Training Infrastructure at ByteDance]] (81.1% similar)
- [[2025-09-18/Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/GPU Cluster|GPU Cluster]]
**🔗 Specific Connectable**: [[keywords/Hybrid Simulation|Hybrid Simulation]], [[keywords/Containerized Environment|Containerized Environment]]
**⚡ Unique Technical**: [[keywords/Phantora|Phantora]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.01616v2 Announce Type: replace-cross 
Abstract: Modern machine learning (ML) training workloads place substantial demands on both computational and communication resources. Consequently, accurate performance estimation has become increasingly critical for guiding system design decisions, such as the selection of parallelization strategies, cluster configurations, and hardware provisioning. Existing simulation-based performance estimation requires reimplementing the ML framework in a simulator, which demands significant manual effort and is hard to maintain as ML frameworks evolve rapidly.
  This paper introduces Phantora, a hybrid GPU cluster simulator designed for performance estimation of ML training workloads. Phantora executes unmodified ML frameworks as is within a distributed, containerized environment. Each container emulates the behavior of a GPU server in a large-scale cluster, while Phantora intercepts and simulates GPU- and communication-related operations to provide high-fidelity performance estimation. We call this approach hybrid simulation of ML systems, in contrast to traditional methods that simulate static workloads. The primary advantage of hybrid simulation is that it allows direct reuse of ML framework source code in simulation, avoiding the need for reimplementation. Our evaluation shows that Phantora provides accuracy comparable to static workload simulation while supporting three state-of-the-art LLM training frameworks out-of-the-box. In addition, Phantora operates on a single GPU, eliminating the need for the resource-intensive trace collection and workload extraction steps required by traditional trace-based simulators. Phantora is open-sourced at https://github.com/QDelta/Phantora.

## 📝 요약

현대 머신러닝(ML) 훈련 작업은 계산 및 통신 자원에 대한 높은 요구를 제기하며, 이에 따라 성능 추정의 중요성이 커지고 있습니다. 기존 시뮬레이션 기반 성능 추정은 ML 프레임워크를 시뮬레이터에 재구현해야 하며, 이는 많은 수작업과 유지보수의 어려움을 수반합니다. 본 논문은 ML 훈련 작업의 성능 추정을 위한 하이브리드 GPU 클러스터 시뮬레이터인 Phantora를 소개합니다. Phantora는 수정되지 않은 ML 프레임워크를 분산된 컨테이너 환경에서 실행하며, 각 컨테이너는 대규모 클러스터의 GPU 서버 동작을 에뮬레이트합니다. Phantora는 GPU 및 통신 관련 작업을 가로채고 시뮬레이션하여 높은 정확도의 성능 추정을 제공합니다. 하이브리드 시뮬레이션은 ML 프레임워크 소스 코드를 직접 재사용할 수 있어 재구현의 필요성을 없애는 것이 주요 장점입니다. 평가 결과, Phantora는 정적 작업 시뮬레이션과 유사한 정확성을 제공하며, 최신 LLM 훈련 프레임워크를 지원합니다. 또한, Phantora는 단일 GPU에서 작동하여 전통적인 추적 기반 시뮬레이터가 요구하는 리소스 집약적인 단계가 필요하지 않습니다. Phantora는 오픈 소스로 제공됩니다.

## 🎯 주요 포인트

- 1. Phantora는 ML 훈련 작업의 성능 추정을 위한 하이브리드 GPU 클러스터 시뮬레이터로, 수정되지 않은 ML 프레임워크를 분산된 컨테이너 환경에서 실행합니다.
- 2. 하이브리드 시뮬레이션 접근법은 ML 시스템의 소스 코드를 직접 재사용할 수 있게 하여 재구현의 필요성을 없앱니다.
- 3. Phantora는 단일 GPU에서 작동하여 전통적인 추적 기반 시뮬레이터가 요구하는 리소스 집약적인 추적 수집 및 작업 추출 단계를 제거합니다.
- 4. Phantora는 최신 LLM 훈련 프레임워크 세 가지를 기본적으로 지원하며, 정적 작업 시뮬레이션과 유사한 정확도를 제공합니다.
- 5. Phantora는 오픈 소스로 제공되며, 성능 추정을 위한 혁신적인 방법을 제시합니다.


---

*Generated on 2025-09-24 15:33:08*