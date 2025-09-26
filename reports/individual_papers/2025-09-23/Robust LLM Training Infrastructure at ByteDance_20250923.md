---
keywords:
  - Large Language Model
  - GPU Infrastructure Management
  - Fault Tolerance
  - ByteRobust
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16293
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:12:50.682531",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "GPU Infrastructure Management",
    "Fault Tolerance",
    "ByteRobust"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "GPU Infrastructure Management": 0.78,
    "Fault Tolerance": 0.82,
    "ByteRobust": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large-Scale Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on training infrastructure, providing a strong link to existing LLM research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "GPU Infrastructure Management",
        "canonical": "GPU Infrastructure Management",
        "aliases": [
          "GPU Management",
          "GPU Infrastructure"
        ],
        "category": "unique_technical",
        "rationale": "Describes a unique system developed for managing large-scale GPU resources, crucial for LLM training.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Fault Tolerance",
        "canonical": "Fault Tolerance",
        "aliases": [
          "Failure Tolerance",
          "Error Tolerance"
        ],
        "category": "specific_connectable",
        "rationale": "Essential for linking to broader discussions on system reliability and robustness in AI infrastructure.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "ByteRobust",
        "canonical": "ByteRobust",
        "aliases": [
          "ByteRobust System"
        ],
        "category": "unique_technical",
        "rationale": "A specific system introduced in the paper, offering a unique contribution to LLM training solutions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "training scale",
      "resource scale",
      "training stability"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "GPU Infrastructure Management",
      "resolved_canonical": "GPU Infrastructure Management",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Fault Tolerance",
      "resolved_canonical": "Fault Tolerance",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "ByteRobust",
      "resolved_canonical": "ByteRobust",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Robust LLM Training Infrastructure at ByteDance

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16293.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16293](https://arxiv.org/abs/2509.16293)

## 🔗 유사한 논문
- [[2025-09-22/Characterizing the Efficiency of Distributed Training_ A Power, Performance, and Thermal Perspective_20250922|Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective]] (85.6% similar)
- [[2025-09-19/Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization_20250919|Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization]] (84.3% similar)
- [[2025-09-18/LNE-Blocking_ An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models_20250918|LNE-Blocking: An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models]] (83.4% similar)
- [[2025-09-22/Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning_20250922|Small LLMs with Expert Blocks Are Good Enough for Hyperparamter Tuning]] (82.3% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Fault Tolerance|Fault Tolerance]]
**⚡ Unique Technical**: [[keywords/GPU Infrastructure Management|GPU Infrastructure Management]], [[keywords/ByteRobust|ByteRobust]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16293v1 Announce Type: cross 
Abstract: The training scale of large language models (LLMs) has reached tens of thousands of GPUs and is still continuously expanding, enabling faster learning of larger models. Accompanying the expansion of the resource scale is the prevalence of failures (CUDA error, NaN values, job hang, etc.), which poses significant challenges to training stability. Any large-scale LLM training infrastructure should strive for minimal training interruption, efficient fault diagnosis, and effective failure tolerance to enable highly efficient continuous training. This paper presents ByteRobust, a large-scale GPU infrastructure management system tailored for robust and stable training of LLMs. It exploits the uniqueness of LLM training process and gives top priorities to detecting and recovering failures in a routine manner. Leveraging parallelisms and characteristics of LLM training, ByteRobust enables high-capacity fault tolerance, prompt fault demarcation, and localization with an effective data-driven approach, comprehensively ensuring continuous and efficient training of LLM tasks. ByteRobust is deployed on a production GPU platform with over 200,000 GPUs and achieves 97% ETTR for a three-month training job on 9,600 GPUs.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)의 안정적이고 효율적인 훈련을 지원하기 위한 GPU 인프라 관리 시스템인 ByteRobust를 소개합니다. LLM 훈련 과정의 특성을 활용하여, 실패 감지 및 복구를 우선시하며, 병렬 처리와 데이터 기반 접근 방식을 통해 높은 수준의 오류 내성 및 신속한 오류 진단을 제공합니다. ByteRobust는 20만 개 이상의 GPU가 있는 플랫폼에 배치되어, 9,600개의 GPU를 사용한 3개월간의 훈련 작업에서 97%의 ETTR을 달성했습니다. 주요 기여는 대규모 LLM 훈련의 연속성과 효율성을 보장하는 데 있습니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델(LLM)의 훈련 규모가 수만 개의 GPU에 이르며, 이는 훈련 안정성에 큰 도전을 제기합니다.
- 2. ByteRobust는 LLM의 견고하고 안정적인 훈련을 위해 설계된 대규모 GPU 인프라 관리 시스템입니다.
- 3. ByteRobust는 LLM 훈련의 병렬성과 특성을 활용하여 높은 수준의 장애 허용과 신속한 장애 진단 및 위치 파악을 가능하게 합니다.
- 4. 이 시스템은 200,000개 이상의 GPU가 있는 플랫폼에 배치되어 9,600개의 GPU로 수행된 3개월 훈련 작업에서 97%의 ETTR을 달성했습니다.


---

*Generated on 2025-09-23 23:12:50*