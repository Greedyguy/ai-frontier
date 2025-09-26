<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:40:31.228414",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Multimodal Learning",
    "Low-Rank Adaptation",
    "Modality Incompleteness"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.78,
    "Multimodal Learning": 0.82,
    "Low-Rank Adaptation": 0.79,
    "Modality Incompleteness": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Learning",
        "canonical": "Federated Learning",
        "aliases": [
          "FL"
        ],
        "category": "broad_technical",
        "rationale": "Federated Learning is a key concept in the paper, connecting it to decentralized model training.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multimodal Data",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is central to the paper's focus on handling multiple data types.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Low-Rank Adaptation",
        "canonical": "Low-Rank Adaptation",
        "aliases": [
          "LoRA"
        ],
        "category": "unique_technical",
        "rationale": "LoRA is a unique adaptation method crucial for the paper's approach to fine-tuning.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      },
      {
        "surface": "Missing Modalities",
        "canonical": "Modality Incompleteness",
        "aliases": [
          "Incomplete Modalities"
        ],
        "category": "unique_technical",
        "rationale": "Addressing missing modalities is a unique challenge tackled by the proposed framework.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multimodal Data",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Low-Rank Adaptation",
      "resolved_canonical": "Low-Rank Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Missing Modalities",
      "resolved_canonical": "Modality Incompleteness",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# FediLoRA: Heterogeneous LoRA for Federated Multimodal Fine-tuning under Missing Modalities

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.06984.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.06984](https://arxiv.org/abs/2509.06984)

## 🔗 유사한 논문
- [[2025-09-23/Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA_20250923|Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA]] (91.3% similar)
- [[2025-09-18/Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning_20250918|Adaptive LoRA Experts Allocation and Selection for Federated Fine-Tuning]] (89.5% similar)
- [[2025-09-24/LoRALib_ A Standardized Benchmark for Evaluating LoRA-MoE Methods_20250924|LoRALib: A Standardized Benchmark for Evaluating LoRA-MoE Methods]] (88.0% similar)
- [[2025-09-23/RefLoRA_ Refactored Low-Rank Adaptation for Efficient Fine-Tuning of Large Models_20250923|RefLoRA: Refactored Low-Rank Adaptation for Efficient Fine-Tuning of Large Models]] (85.8% similar)
- [[2025-09-22/Sparsity May Be All You Need_ Sparse Random Parameter Adaptation_20250922|Sparsity May Be All You Need: Sparse Random Parameter Adaptation]] (84.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Low-Rank Adaptation|Low-Rank Adaptation]], [[keywords/Modality Incompleteness|Modality Incompleteness]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.06984v2 Announce Type: replace-cross 
Abstract: Foundation models have demonstrated remarkable performance across a wide range of tasks, yet their large parameter sizes pose challenges for practical deployment, especially in decentralized environments. Parameter-efficient fine-tuning (PEFT), such as Low-Rank Adaptation (LoRA), reduces local computing and memory overhead, making it attractive for federated learning. However, existing federated LoRA methods typically assume uniform rank configurations and unimodal inputs, overlooking two key real-world challenges: (1) heterogeneous client resources have different LoRA ranks, and (2) multimodal data settings with potentially missing modalities. In this work, we propose FediLoRA, a simple yet effective framework for federated multimodal fine-tuning under heterogeneous LoRA ranks and missing modalities. FediLoRA introduces a dimension-wise aggregation strategy that reweights LoRA updates without information dilution during aggregation. It also includes a lightweight layer-wise model editing method that selectively incorporates global parameters to repair local components which improves both client and global model performances. Experimental results on three multimodal benchmark datasets demonstrate that FediLoRA achieves superior performance over competitive baselines in both global and personalized settings, particularly in the presence of modality incompleteness.

## 📝 요약

이 논문은 대규모 파라미터 크기로 인해 실용적인 배포에 어려움을 겪는 기초 모델을 위한 파라미터 효율적 미세 조정(PEFT) 방법론을 제안합니다. 특히, FediLoRA라는 프레임워크를 통해 이종 클라이언트 자원과 다중 모달 데이터 환경에서의 문제를 해결합니다. FediLoRA는 LoRA 업데이트를 정보 손실 없이 재조정하는 차원별 집계 전략과, 글로벌 파라미터를 선택적으로 통합하여 성능을 향상시키는 경량 레이어 편집 방법을 도입합니다. 실험 결과, FediLoRA는 세 가지 다중 모달 벤치마크 데이터셋에서 기존 방법들보다 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. FediLoRA는 이질적인 LoRA 랭크와 누락된 모달리티가 있는 환경에서 연합 멀티모달 미세 조정을 위한 효과적인 프레임워크를 제안합니다.
- 2. FediLoRA는 정보 희석 없이 LoRA 업데이트를 재가중하는 차원별 집계 전략을 도입합니다.
- 3. FediLoRA는 경량의 레이어별 모델 편집 방법을 통해 글로벌 파라미터를 선택적으로 통합하여 로컬 구성 요소를 수정하고, 클라이언트 및 글로벌 모델 성능을 향상시킵니다.
- 4. 세 가지 멀티모달 벤치마크 데이터셋에 대한 실험 결과, FediLoRA는 모달리티 불완전성이 있는 상황에서도 글로벌 및 개인화 설정에서 경쟁력 있는 기준선보다 우수한 성능을 보여줍니다.


---

*Generated on 2025-09-24 14:40:31*