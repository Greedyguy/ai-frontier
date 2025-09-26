<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:37:05.708820",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Low-Rank Adaptation",
    "Mixture of Experts",
    "LoRA-MoE Methods",
    "OpenCompass Testing Tool"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Low-Rank Adaptation": 0.8,
    "Mixture of Experts": 0.78,
    "LoRA-MoE Methods": 0.82,
    "OpenCompass Testing Tool": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LoRA",
        "canonical": "Low-Rank Adaptation",
        "aliases": [
          "LoRA"
        ],
        "category": "unique_technical",
        "rationale": "LoRA is a key method discussed in the paper, offering a unique approach to parameter-efficient fine-tuning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "MoE",
        "canonical": "Mixture of Experts",
        "aliases": [
          "MoE"
        ],
        "category": "specific_connectable",
        "rationale": "MoE is a significant concept that enhances model adaptability, making it a strong candidate for linking.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "LoRA-MoE",
        "canonical": "LoRA-MoE Methods",
        "aliases": [
          "LoRA-MoE"
        ],
        "category": "unique_technical",
        "rationale": "Combining LoRA with MoE represents a novel approach that the paper focuses on, warranting a unique technical category.",
        "novelty_score": 0.88,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "OpenCompass",
        "canonical": "OpenCompass Testing Tool",
        "aliases": [
          "OpenCompass"
        ],
        "category": "unique_technical",
        "rationale": "OpenCompass is a specific tool used in the paper's experiments, relevant for linking technical implementations.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "datasets",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LoRA",
      "resolved_canonical": "Low-Rank Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "MoE",
      "resolved_canonical": "Mixture of Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "LoRA-MoE",
      "resolved_canonical": "LoRA-MoE Methods",
      "decision": "linked",
      "scores": {
        "novelty": 0.88,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "OpenCompass",
      "resolved_canonical": "OpenCompass Testing Tool",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# LoRALib: A Standardized Benchmark for Evaluating LoRA-MoE Methods

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18137.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18137](https://arxiv.org/abs/2509.18137)

## 🔗 유사한 논문
- [[2025-09-23/Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA_20250923|Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA]] (89.0% similar)
- [[2025-09-23/GuiLoMo_ Allocating Expert Number and Rank for LoRA-MoE via Bilevel Optimization with GuidedSelection Vectors_20250923|GuiLoMo: Allocating Expert Number and Rank for LoRA-MoE via Bilevel Optimization with GuidedSelection Vectors]] (87.1% similar)
- [[2025-09-23/TASO_ Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation_20250923|TASO: Task-Aligned Sparse Optimization for Parameter-Efficient Model Adaptation]] (85.7% similar)
- [[2025-09-23/RefLoRA_ Refactored Low-Rank Adaptation for Efficient Fine-Tuning of Large Models_20250923|RefLoRA: Refactored Low-Rank Adaptation for Efficient Fine-Tuning of Large Models]] (85.5% similar)
- [[2025-09-22/Sparsity May Be All You Need_ Sparse Random Parameter Adaptation_20250922|Sparsity May Be All You Need: Sparse Random Parameter Adaptation]] (84.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Mixture of Experts|Mixture of Experts]]
**⚡ Unique Technical**: [[keywords/Low-Rank Adaptation|Low-Rank Adaptation]], [[keywords/LoRA-MoE Methods|LoRA-MoE Methods]], [[keywords/OpenCompass Testing Tool|OpenCompass Testing Tool]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18137v1 Announce Type: cross 
Abstract: As a parameter efficient fine-tuning (PEFT) method, low-rank adaptation (LoRA) can save significant costs in storage and computing, but its strong adaptability to a single task is often accompanied by insufficient cross-task generalization capabilities. To improve this, existing work combines LoRA with mixture-of-experts (MoE) to enhance the model's adaptability through expert modules and routing mechanisms. However, existing LoRA-MoE methods lack unified standards in models, datasets, hyperparameters, and evaluation methods, making it difficult to conduct fair comparisons between different methods. To this end, we proposed a unified benchmark named LoRALib. Specifically, we standardized datasets from $40$ downstream tasks into a unified format, fine-tuned them using the same hyperparameters and obtained $680$ LoRA modules across $17$ model architectures. Based on this LoRA library, we conduct large-scale experiments on $3$ representative LoRA-MoE methods and different LoRA selection mechanisms using the open-sourced testing tool OpenCompass. Extensive experiments show that LoRAMoE performs best, and that prioritizing LoRAs relevant to the target task can further improve the performance of MoE. We hope these findings will inspire future work. Our datasets and LoRA library are available at https://huggingface.co/datasets/YaoLuzjut/LoRAOcean_dataset and https://huggingface.co/YaoLuzjut/models.

## 📝 요약

이 논문은 파라미터 효율적 미세 조정(PEFT) 방법인 저순위 적응(LoRA)의 단일 작업 적응력은 높지만, 작업 간 일반화 능력이 부족하다는 문제를 해결하기 위해 LoRA와 전문가 혼합(MoE)을 결합한 방법을 제안합니다. 이를 위해 LoRALib라는 통합 벤치마크를 개발하여, 40개의 다운스트림 작업을 표준화된 형식으로 정리하고, 동일한 하이퍼파라미터로 미세 조정하여 17개 모델 아키텍처에서 680개의 LoRA 모듈을 생성했습니다. 대규모 실험 결과, LoRAMoE가 가장 우수한 성능을 보였으며, 목표 작업과 관련된 LoRA를 우선시할 때 MoE의 성능이 더욱 향상됨을 발견했습니다. 이러한 결과는 향후 연구에 영감을 줄 것으로 기대됩니다. 데이터셋과 LoRA 라이브러리는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. LoRA는 저장 및 계산 비용을 절감하는 파라미터 효율적 미세 조정(PEFT) 방법이지만, 단일 작업에 대한 적응력이 강한 반면, 작업 간 일반화 능력이 부족하다.
- 2. 기존 연구는 LoRA와 전문가 모듈 및 라우팅 메커니즘을 활용한 mixture-of-experts (MoE)를 결합하여 모델의 적응력을 향상시키고자 한다.
- 3. 다양한 LoRA-MoE 방법 간의 공정한 비교를 위해 모델, 데이터셋, 하이퍼파라미터 및 평가 방법에 대한 통일된 기준이 필요하다.
- 4. 이를 해결하기 위해, 우리는 40개의 다운스트림 작업을 표준화하고, 동일한 하이퍼파라미터로 미세 조정하여 17개의 모델 아키텍처에서 680개의 LoRA 모듈을 얻는 LoRALib 벤치마크를 제안했다.
- 5. 대규모 실험 결과, LoRAMoE가 가장 우수한 성능을 보였으며, 목표 작업과 관련된 LoRA를 우선적으로 선택하면 MoE의 성능이 더욱 향상될 수 있음을 발견했다.


---

*Generated on 2025-09-24 13:37:05*