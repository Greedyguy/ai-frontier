---
keywords:
  - Large Language Model
  - Microservice Trace Generation
  - Synthetic Workload Traces
  - Instruction Tuning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2502.17439
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:48:37.618560",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Microservice Trace Generation",
    "Synthetic Workload Traces",
    "Instruction Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Microservice Trace Generation": 0.78,
    "Synthetic Workload Traces": 0.77,
    "Instruction Tuning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's methodology and connect with other AI and NLP research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Microservice Trace Generation",
        "canonical": "Microservice Trace Generation",
        "aliases": [
          "Trace Generation"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique approach introduced in the paper, crucial for understanding the application of LLMs in system traces.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Synthetic Workload Traces",
        "canonical": "Synthetic Workload Traces",
        "aliases": [
          "Synthetic Traces"
        ],
        "category": "unique_technical",
        "rationale": "The generation of synthetic traces is a key innovation in the paper, linking to resource management in computing.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "Instruction Tuning",
        "canonical": "Instruction Tuning",
        "aliases": [
          "Tuning"
        ],
        "category": "specific_connectable",
        "rationale": "Instruction tuning is critical for aligning LLM outputs with desired features, relevant to model adaptation techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "workload",
      "traces",
      "model",
      "data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
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
      "candidate_surface": "Microservice Trace Generation",
      "resolved_canonical": "Microservice Trace Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Synthetic Workload Traces",
      "resolved_canonical": "Synthetic Workload Traces",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Instruction Tuning",
      "resolved_canonical": "Instruction Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Large Language Models as Realistic Microservice Trace Generators

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.17439.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2502.17439](https://arxiv.org/abs/2502.17439)

## 🔗 유사한 논문
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (84.7% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (83.3% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (83.1% similar)
- [[2025-09-22/SyGra_ A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data_20250922|SyGra: A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data]] (82.6% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (82.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Instruction Tuning|Instruction Tuning]]
**⚡ Unique Technical**: [[keywords/Microservice Trace Generation|Microservice Trace Generation]], [[keywords/Synthetic Workload Traces|Synthetic Workload Traces]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.17439v3 Announce Type: replace-cross 
Abstract: Workload traces are essential to understand complex computer systems' behavior and manage processing and memory resources. Since real-world traces are hard to obtain, synthetic trace generation is a promising alternative. This paper proposes a first-of-a-kind approach that relies on training a large language model (LLM) to generate synthetic workload traces, specifically microservice call graphs. To capture complex and arbitrary hierarchical structures and implicit constraints in such traces, we propose to train LLMs to generate recursively, making call graph generation a sequence of more manageable steps. To further enforce learning constraints on the traces and generate uncommon situations, we apply additional instruction tuning steps to align our model with the desired trace features. With this method, we train TraceLLM, an LLM for microservice trace generation, and demonstrate that it produces diverse, realistic traces under varied conditions, outperforming existing approaches in both accuracy and validity. The synthetically generated traces can effectively replace real data to optimize important microservice management tasks. Additionally, TraceLLM adapts to downstream trace-related tasks, such as predicting key trace features and infilling missing data.

## 📝 요약

이 논문은 복잡한 컴퓨터 시스템의 동작을 이해하고 자원 관리를 돕기 위해 합성 워크로드 추적을 생성하는 새로운 접근법을 제안합니다. 실제 추적 데이터를 얻기 어려운 문제를 해결하기 위해, 대형 언어 모델(LLM)을 훈련시켜 합성 워크로드 추적, 특히 마이크로서비스 호출 그래프를 생성합니다. 복잡한 계층 구조와 암묵적 제약을 포착하기 위해 LLM을 재귀적으로 훈련하여 호출 그래프 생성을 더 관리하기 쉬운 단계로 나눕니다. 또한, 모델이 원하는 추적 특성과 일치하도록 추가적인 지시 조정을 통해 학습 제약을 강화하고 드문 상황을 생성합니다. 이 방법을 통해 개발된 TraceLLM은 다양한 조건에서 현실적이고 다양한 추적을 생성하며, 기존 방법보다 정확성과 유효성에서 우수한 성능을 보입니다. 생성된 합성 추적은 실제 데이터를 대체하여 중요한 마이크로서비스 관리 작업을 최적화할 수 있으며, 추적 관련 작업에도 적응할 수 있습니다.

## 🎯 주요 포인트

- 1. 실세계의 워크로드 트레이스를 얻기 어려운 문제를 해결하기 위해 대규모 언어 모델(LLM)을 활용한 합성 트레이스 생성 방법을 제안합니다.
- 2. 마이크로서비스 호출 그래프와 같은 복잡한 계층 구조와 암묵적 제약을 포착하기 위해 LLM을 순차적으로 학습시켜 트레이스를 생성합니다.
- 3. 트레이스의 학습 제약을 강화하고 드문 상황을 생성하기 위해 추가적인 명령어 조정 단계를 적용합니다.
- 4. 제안된 TraceLLM은 다양한 조건에서 현실적이고 다양한 트레이스를 생성하며, 기존 방법보다 정확성과 유효성 면에서 우수한 성능을 보입니다.
- 5. TraceLLM은 주요 트레이스 특징 예측 및 누락 데이터 보완과 같은 후속 트레이스 관련 작업에도 적응합니다.


---

*Generated on 2025-09-24 00:48:37*