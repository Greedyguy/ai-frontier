---
keywords:
  - Multimodal Learning
  - Data Contamination
  - Vision-Language Model
  - Unimodal Pre-training
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2411.03823
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:41:30.429656",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Data Contamination",
    "Vision-Language Model",
    "Unimodal Pre-training"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.88,
    "Data Contamination": 0.79,
    "Vision-Language Model": 0.83,
    "Unimodal Pre-training": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Large Language Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs",
          "Multimodal LLMs"
        ],
        "category": "specific_connectable",
        "rationale": "This term is central to the paper's focus on multimodal data contamination and aligns with the trending concept of Multimodal Learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.88
      },
      {
        "surface": "Data Contamination",
        "canonical": "Data Contamination",
        "aliases": [
          "Contamination",
          "Data Leakage"
        ],
        "category": "unique_technical",
        "rationale": "The concept of data contamination is unique to this study's analysis of model training and evaluation, offering a new perspective on model reliability.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "Visual Question Answering",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VQA"
        ],
        "category": "evolved_concepts",
        "rationale": "Visual Question Answering is a specific application of Vision-Language Models, which are relevant to the paper's analysis of multimodal benchmarks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.8,
        "link_intent_score": 0.83
      },
      {
        "surface": "Unimodal Pre-training",
        "canonical": "Unimodal Pre-training",
        "aliases": [
          "Single-modal Pre-training"
        ],
        "category": "unique_technical",
        "rationale": "This term highlights a specific phase in model training that contributes to data contamination, providing insights into model development processes.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.77,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "model training",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Data Contamination",
      "resolved_canonical": "Data Contamination",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Visual Question Answering",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.8,
        "link_intent": 0.83
      }
    },
    {
      "candidate_surface": "Unimodal Pre-training",
      "resolved_canonical": "Unimodal Pre-training",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.77,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Both Text and Images Leaked! A Systematic Analysis of Data Contamination in Multimodal LLM

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2411.03823.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2411.03823](https://arxiv.org/abs/2411.03823)

## 🔗 유사한 논문
- [[2025-09-18/LNE-Blocking_ An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models_20250918|LNE-Blocking: An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models]] (87.5% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (86.4% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals: Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (85.5% similar)
- [[2025-09-17/Simulating a Bias Mitigation Scenario in Large Language Models_20250917|Simulating a Bias Mitigation Scenario in Large Language Models]] (85.2% similar)
- [[2025-09-19/DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM: Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (85.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Data Contamination|Data Contamination]], [[keywords/Unimodal Pre-training|Unimodal Pre-training]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2411.03823v3 Announce Type: replace-cross 
Abstract: The rapid advancement of multimodal large language models (MLLMs) has significantly enhanced performance across benchmarks. However, data contamination-unintentional memorization of benchmark data during model training-poses critical challenges for fair evaluation. Existing detection methods for unimodal large language models (LLMs) are inadequate for MLLMs due to multimodal data complexity and multi-phase training. We systematically analyze multimodal data contamination using our analytical framework, MM-Detect, which defines two contamination categories-unimodal and cross-modal-and effectively quantifies contamination severity across multiple-choice and caption-based Visual Question Answering tasks. Evaluations on twelve MLLMs and five benchmarks reveal significant contamination, particularly in proprietary models and older benchmarks. Crucially, contamination sometimes originates during unimodal pre-training rather than solely from multimodal fine-tuning. Our insights refine contamination understanding, guiding evaluation practices and improving multimodal model reliability.

## 📝 요약

이 논문은 멀티모달 대형 언어 모델(MLLM)의 데이터 오염 문제를 다룹니다. 데이터 오염은 모델 훈련 중 벤치마크 데이터를 의도치 않게 암기하는 현상을 말하며, 이는 공정한 평가에 큰 문제를 초래합니다. 기존의 단일 모달 언어 모델(LLM) 탐지 방법은 멀티모달 데이터의 복잡성과 다단계 훈련 과정 때문에 MLLM에 적합하지 않습니다. 저자들은 MM-Detect라는 분석 프레임워크를 통해 멀티모달 데이터 오염을 체계적으로 분석하고, 오염을 단일 모달과 교차 모달로 분류하여 다양한 시각적 질문 응답 과제에서 오염의 심각성을 정량화했습니다. 12개의 MLLM과 5개의 벤치마크를 평가한 결과, 특히 독점 모델과 오래된 벤치마크에서 상당한 오염이 발견되었습니다. 중요한 점은 오염이 멀티모달 세부 조정뿐만 아니라 단일 모달 사전 훈련 중에도 발생할 수 있다는 것입니다. 이러한 통찰은 오염 이해를 개선하고 평가 관행을 안내하며 멀티모달 모델의 신뢰성을 향상시킵니다.

## 🎯 주요 포인트

- 1. 멀티모달 대형 언어 모델(MLLMs)의 발전은 성능을 크게 향상시켰으나, 데이터 오염 문제가 공정한 평가에 도전 과제를 제기한다.
- 2. 기존의 단일 모달 언어 모델(LLMs) 탐지 방법은 멀티모달 데이터의 복잡성과 다단계 훈련 때문에 MLLMs에 적합하지 않다.
- 3. MM-Detect라는 분석 프레임워크를 통해 멀티모달 데이터 오염을 체계적으로 분석하고, 오염의 심각성을 효과적으로 정량화한다.
- 4. 열두 개의 MLLMs과 다섯 개의 벤치마크 평가에서, 특히 독점 모델과 오래된 벤치마크에서 상당한 오염이 발견되었다.
- 5. 오염은 멀티모달 미세 조정뿐만 아니라 단일 모달 사전 훈련에서도 발생할 수 있으며, 이는 평가 관행을 개선하고 모델 신뢰성을 높이는 데 기여한다.


---

*Generated on 2025-09-24 00:41:30*