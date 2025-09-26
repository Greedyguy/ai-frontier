---
keywords:
  - GraphMend
  - FX Graph
  - Dynamic Control Flow
  - TorchDynamo
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16248
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:04:43.929498",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "GraphMend",
    "FX Graph",
    "Dynamic Control Flow",
    "TorchDynamo"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "GraphMend": 0.8,
    "FX Graph": 0.79,
    "Dynamic Control Flow": 0.77,
    "TorchDynamo": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "GraphMend",
        "canonical": "GraphMend",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "GraphMend is a novel tool specifically designed to address graph breaks in PyTorch 2, making it a unique technical contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "FX graph",
        "canonical": "FX Graph",
        "aliases": [
          "FX graphs"
        ],
        "category": "specific_connectable",
        "rationale": "FX Graphs are central to PyTorch's graph-based execution model, providing a specific point of connection for discussions on dynamic control flow.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "dynamic control flow",
        "canonical": "Dynamic Control Flow",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Dynamic control flow is a critical aspect of program execution that affects graph compilation, making it a key linkable concept.",
        "novelty_score": 0.6,
        "connectivity_score": 0.84,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "TorchDynamo",
        "canonical": "TorchDynamo",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "TorchDynamo is a specific component of PyTorch 2's JIT compilation pipeline, relevant for understanding the context of GraphMend's improvements.",
        "novelty_score": 0.7,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "compiler",
      "evaluation",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "GraphMend",
      "resolved_canonical": "GraphMend",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "FX graph",
      "resolved_canonical": "FX Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "dynamic control flow",
      "resolved_canonical": "Dynamic Control Flow",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.84,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "TorchDynamo",
      "resolved_canonical": "TorchDynamo",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# GraphMend: Code Transformations for Fixing Graph Breaks in PyTorch 2

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16248.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16248](https://arxiv.org/abs/2509.16248)

## 🔗 유사한 논문
- [[2025-09-19/Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization_20250919|Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization]] (80.1% similar)
- [[2025-09-19/Evaluating the Effectiveness of Coverage-Guided Fuzzing for Testing Deep Learning Library APIs_20250919|Evaluating the Effectiveness of Coverage-Guided Fuzzing for Testing Deep Learning Library APIs]] (80.1% similar)
- [[2025-09-22/ForestColl_ Throughput-Optimal Collective Communications on Heterogeneous Network Fabrics_20250922|ForestColl: Throughput-Optimal Collective Communications on Heterogeneous Network Fabrics]] (79.8% similar)
- [[2025-09-23/Machine learning-driven conservative-to-primitive conversion in hybrid piecewise polytropic and tabulated equations of state_20250923|Machine learning-driven conservative-to-primitive conversion in hybrid piecewise polytropic and tabulated equations of state]] (79.6% similar)
- [[2025-09-23/Tempo_ Compiled Dynamic Deep Learning with Symbolic Dependence Graphs_20250923|Tempo: Compiled Dynamic Deep Learning with Symbolic Dependence Graphs]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/FX Graph|FX Graph]], [[keywords/Dynamic Control Flow|Dynamic Control Flow]]
**⚡ Unique Technical**: [[keywords/GraphMend|GraphMend]], [[keywords/TorchDynamo|TorchDynamo]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16248v1 Announce Type: cross 
Abstract: This paper presents GraphMend, a high-level compiler that eliminates FX graph breaks in PyTorch 2 programs. Although PyTorch 2 introduced TorchDynamo and TorchInductor to enable just-in-time graph compilation, unresolved dynamic control flow and unsupported Python constructs often fragment models into multiple FX graphs. These fragments force frequent fallbacks to eager mode, incur costly CPU-to-GPU synchronizations, and reduce optimization opportunities. GraphMend addresses this limitation by analyzing and transforming source code before execution. Built on the Jac compilation framework, GraphMend introduces two code transformations that remove graph breaks due to dynamic control flow and Python I/O functions. This design allows PyTorch's compilation pipeline to capture larger, uninterrupted FX graphs without requiring manual refactoring by developers. Evaluation across eight Hugging Face models shows that GraphMend removes all fixable graph breaks due to dynamic control flow and Python I/O functions, driving the break count to 0 in 6 models and reducing it from 5 to 2 in another model. On NVIDIA RTX 3090 and A40 GPUs, GraphMend achieves up to 75% latency reductions and up to 8% higher end-to-end throughput. These results demonstrate that high-level code transformation is an effective complement to PyTorch's dynamic JIT compilation pipeline, substantially improving both usability and performance.

## 📝 요약

이 논문은 PyTorch 2 프로그램에서 FX 그래프 단절을 제거하는 고급 컴파일러인 GraphMend를 소개합니다. PyTorch 2의 TorchDynamo와 TorchInductor는 그래프 컴파일을 지원하지만, 동적 제어 흐름과 지원되지 않는 Python 구조로 인해 모델이 여러 FX 그래프로 분할되는 문제가 있습니다. GraphMend는 실행 전 소스 코드를 분석하고 변환하여 이러한 문제를 해결합니다. Jac 컴파일 프레임워크를 기반으로, GraphMend는 동적 제어 흐름과 Python I/O 함수로 인한 그래프 단절을 제거하는 두 가지 코드 변환을 도입합니다. 이를 통해 PyTorch의 컴파일 파이프라인이 더 큰 FX 그래프를 캡처할 수 있게 하여 개발자가 수동으로 리팩토링할 필요가 없습니다. 8개의 Hugging Face 모델 평가 결과, GraphMend는 모든 수정 가능한 그래프 단절을 제거하여 6개 모델에서 단절 수를 0으로 줄였고, 다른 모델에서는 5에서 2로 감소시켰습니다. NVIDIA RTX 3090 및 A40 GPU에서 최대 75%의 지연 시간 감소와 최대 8%의 처리량 증가를 달성했습니다. 이는 고급 코드 변환이 PyTorch의 동적 JIT 컴파일 파이프라인을 효과적으로 보완하여 사용성과 성능을 크게 향상시킴을 보여줍니다.

## 🎯 주요 포인트

- 1. GraphMend는 PyTorch 2 프로그램에서 FX 그래프 분할을 제거하는 고급 컴파일러입니다.
- 2. GraphMend는 동적 제어 흐름과 Python I/O 함수로 인한 그래프 분할을 제거하는 두 가지 코드 변환을 도입합니다.
- 3. GraphMend는 수동 리팩토링 없이도 PyTorch의 컴파일 파이프라인이 더 큰 FX 그래프를 캡처할 수 있도록 합니다.
- 4. GraphMend는 8개의 Hugging Face 모델 평가에서 모든 수정 가능한 그래프 분할을 제거하여 성능을 향상시킵니다.
- 5. NVIDIA RTX 3090 및 A40 GPU에서 GraphMend는 최대 75%의 지연 시간 감소와 최대 8%의 처리량 증가를 달성합니다.


---

*Generated on 2025-09-24 02:04:43*