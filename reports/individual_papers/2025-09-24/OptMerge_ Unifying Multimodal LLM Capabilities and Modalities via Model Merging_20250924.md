<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:20:50.746535",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Model Merging",
    "Vision-Language Model",
    "Omni-language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Model Merging": 0.79,
    "Vision-Language Model": 0.82,
    "Omni-language Model": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal LLMs",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs",
          "Multimodal Large Language Models"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is a trending concept that connects various modalities, enhancing the understanding of complex data interactions.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Model Merging",
        "canonical": "Model Merging",
        "aliases": [
          "Merging Models"
        ],
        "category": "unique_technical",
        "rationale": "Model Merging is a novel approach to combine expert models, which is crucial for advancing multimodal capabilities.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.81,
        "link_intent_score": 0.79
      },
      {
        "surface": "Vision-Language",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language Models"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are essential for integrating visual and textual data, a key aspect of multimodal systems.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Omni-language model",
        "canonical": "Omni-language Model",
        "aliases": [
          "Universal Language Model"
        ],
        "category": "unique_technical",
        "rationale": "The Omni-language Model represents a comprehensive approach to unify multiple language modalities, pushing the boundaries of language understanding.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.83,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "tasks",
      "performance gain"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal LLMs",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Model Merging",
      "resolved_canonical": "Model Merging",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.81,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Vision-Language",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Omni-language model",
      "resolved_canonical": "Omni-language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.83,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# OptMerge: Unifying Multimodal LLM Capabilities and Modalities via Model Merging

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.19892.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2505.19892](https://arxiv.org/abs/2505.19892)

## 🔗 유사한 논문
- [[2025-09-23/AIMMerging_ Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning_20250923|AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning]] (88.1% similar)
- [[2025-09-23/Both Text and Images Leaked! A Systematic Analysis of Data Contamination in Multimodal LLM_20250923|Both Text and Images Leaked! A Systematic Analysis of Data Contamination in Multimodal LLM]] (86.9% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (86.6% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (86.6% similar)
- [[2025-09-23/LEO-MINI_ An Efficient Multimodal Large Language Model using Conditional Token Reduction and Mixture of Multi-Modal Experts_20250923|LEO-MINI: An Efficient Multimodal Large Language Model using Conditional Token Reduction and Mixture of Multi-Modal Experts]] (86.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Model Merging|Model Merging]], [[keywords/Omni-language Model|Omni-language Model]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.19892v2 Announce Type: replace 
Abstract: Foundation models update slowly due to resource-intensive training, whereas domain-specific models evolve rapidly between releases. Model merging seeks to combine multiple expert models into a single, more capable model, reducing storage and serving costs while supporting decentralized development. Despite its potential, previous studies have primarily focused on merging visual classification models or Large Language Models (LLMs) for code and math tasks. Recently, Multimodal LLMs (MLLMs) that extend LLMs through large-scale multimodal training have gained traction. However, there lacks a benchmark for model merging research that clearly divides the tasks for MLLM training and evaluation. In this paper, $\textbf{(i)}$ we introduce a model merging benchmark for MLLMs, which includes multiple tasks such as VQA, Geometry, Chart, OCR, and Grounding, studying both LoRA and full fine-tuning models. Moreover, we explore how model merging can combine different modalities (e.g., vision-language, audio-language, and video-language models), moving toward the Omni-language model. $\textbf{(ii)}$ We implement 10 model merging algorithms on the benchmark. Furthermore, we propose a novel method that removes noise from task vectors and robustly optimizes the merged vector based on a loss defined over task vector interactions, achieving an average performance gain of 2.48%. $\textbf{(iii)}$ We find that model merging offers a promising way for building improved MLLMs without requiring training data. Our results also demonstrate that the complementarity among multiple modalities outperforms individual modalities.

## 📝 요약

이 논문은 멀티모달 대형 언어 모델(MMLM)의 모델 병합 연구를 위한 벤치마크를 제안하며, VQA, 기하학, 차트, OCR, 그라운딩 등의 다양한 과제를 포함합니다. 연구에서는 LoRA 및 전체 미세 조정 모델을 사용하여 모델 병합이 어떻게 다양한 모달리티를 결합할 수 있는지 탐구합니다. 10개의 모델 병합 알고리즘을 벤치마크에 구현하고, 잡음을 제거하고 과제 벡터 상호작용에 기반한 손실을 통해 병합 벡터를 최적화하는 새로운 방법을 제안하여 평균 2.48%의 성능 향상을 달성했습니다. 이 연구는 훈련 데이터 없이도 향상된 MMLM을 구축할 수 있는 가능성을 보여주며, 여러 모달리티의 상호보완성이 개별 모달리티를 능가함을 입증합니다.

## 🎯 주요 포인트

- 1. 모델 병합은 여러 전문가 모델을 결합하여 저장 및 서비스 비용을 줄이고 분산 개발을 지원하는 방법이다.
- 2. MLLM(멀티모달 대형 언어 모델) 병합 연구를 위한 벤치마크를 소개하며, VQA, 기하학, 차트, OCR, 그라운딩 등의 다양한 작업을 포함한다.
- 3. 모델 병합은 비전-언어, 오디오-언어, 비디오-언어 모델 등 다양한 모달리티를 결합하여 옴니-언어 모델로 발전할 수 있다.
- 4. 10개의 모델 병합 알고리즘을 구현하고, 잡음 제거 및 작업 벡터 상호작용 기반 최적화 방법을 제안하여 평균 성능을 2.48% 향상시켰다.
- 5. 모델 병합은 훈련 데이터 없이도 개선된 MLLM을 구축할 수 있는 유망한 방법이며, 여러 모달리티의 상호보완성이 개별 모달리티보다 우수하다.


---

*Generated on 2025-09-24 14:20:50*