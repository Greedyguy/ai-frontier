---
keywords:
  - Transformer
  - Continual Learning
  - Low-Rank Adaptation
  - Dynamic Memory
  - Parameter-Efficient Fine-Tuning
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2411.00623
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:36:42.578642",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Continual Learning",
    "Low-Rank Adaptation",
    "Dynamic Memory",
    "Parameter-Efficient Fine-Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Continual Learning": 0.88,
    "Low-Rank Adaptation": 0.82,
    "Dynamic Memory": 0.8,
    "Parameter-Efficient Fine-Tuning": 0.84
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision Transformer",
        "canonical": "Transformer",
        "aliases": [
          "ViT"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are central to the discussed continual learning approach, linking to broader transformer-based research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Continual Learning",
        "canonical": "Continual Learning",
        "aliases": [
          "CL"
        ],
        "category": "specific_connectable",
        "rationale": "Continual learning is the core focus of the paper, connecting to ongoing research in adaptive learning systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Low-Rank Adaptation",
        "canonical": "Low-Rank Adaptation",
        "aliases": [
          "LoRA"
        ],
        "category": "unique_technical",
        "rationale": "Low-Rank Adaptation is a key technique explored in the paper, offering a unique approach to parameter-efficient tuning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Dynamic Memory",
        "canonical": "Dynamic Memory",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Dynamic memory is crucial for balancing stability and plasticity in the proposed method, linking to memory mechanisms in AI.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Parameter-Efficient Fine-Tuning",
        "canonical": "Parameter-Efficient Fine-Tuning",
        "aliases": [
          "PEFT"
        ],
        "category": "specific_connectable",
        "rationale": "PEFT is a significant aspect of the paper's approach, connecting to broader discussions on efficient model adaptation.",
        "novelty_score": 0.6,
        "connectivity_score": 0.83,
        "specificity_score": 0.77,
        "link_intent_score": 0.84
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
      "candidate_surface": "Vision Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Continual Learning",
      "resolved_canonical": "Continual Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Low-Rank Adaptation",
      "resolved_canonical": "Low-Rank Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Dynamic Memory",
      "resolved_canonical": "Dynamic Memory",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Parameter-Efficient Fine-Tuning",
      "resolved_canonical": "Parameter-Efficient Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.83,
        "specificity": 0.77,
        "link_intent": 0.84
      }
    }
  ]
}
-->

# Replay-Free Continual Low-Rank Adaptation with Dynamic Memory

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2411.00623.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2411.00623](https://arxiv.org/abs/2411.00623)

## 🔗 유사한 논문
- [[2025-09-18/HAM_ Hierarchical Adapter Merging for Scalable Continual Learning_20250918|HAM: Hierarchical Adapter Merging for Scalable Continual Learning]] (86.2% similar)
- [[2025-09-23/Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA_20250923|Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA]] (85.8% similar)
- [[2025-09-25/Faster Than SVD, Smarter Than SGD_ The OPLoRA Alternating Update_20250925|Faster Than SVD, Smarter Than SGD: The OPLoRA Alternating Update]] (85.8% similar)
- [[2025-09-25/Localized LoRA_ A Structured Low-Rank Approximation for Efficient Fine-Tuning_20250925|Localized LoRA: A Structured Low-Rank Approximation for Efficient Fine-Tuning]] (85.6% similar)
- [[2025-09-25/TensLoRA_ Tensor Alternatives for Low-Rank Adaptation_20250925|TensLoRA: Tensor Alternatives for Low-Rank Adaptation]] (85.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Continual Learning|Continual Learning]], [[keywords/Parameter-Efficient Fine-Tuning|Parameter-Efficient Fine-Tuning]]
**⚡ Unique Technical**: [[keywords/Low-Rank Adaptation|Low-Rank Adaptation]], [[keywords/Dynamic Memory|Dynamic Memory]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2411.00623v3 Announce Type: replace-cross 
Abstract: We revisit continual learning~(CL), which enables pre-trained vision transformers (ViTs) to sequentially fine-tune on new downstream tasks over time. However, as the scale of these models increases, catastrophic forgetting remains a more serious challenge. Recent studies highlight a crossover between CL techniques and parameter-efficient fine-tuning (PEFT), which focuses on fine-tuning only a small set of trainable parameters to adapt to downstream tasks, such as low-rank adaptation (LoRA). While LoRA achieves faster convergence and requires fewer trainable parameters, it has seldom been explored in the context of continual learning. To address this gap, we propose a novel PEFT-CL method called Dual Low-Rank Adaptation (DualLoRA), which introduces both an orthogonal LoRA adapter and a residual LoRA adapter parallel to pre-trained weights in each layer. These components are orchestrated by a dynamic memory mechanism to strike a balance between stability and plasticity. Additionally, we propose a scheme to predict task identity with confidence and calibrate the model's outputs accordingly. On ViT-based models, we demonstrate that DualLoRA offers significant advantages in accuracy, inference speed, and computation efficiency in training over existing CL methods across multiple benchmarks.

## 📝 요약

이 논문은 사전 학습된 비전 트랜스포머(ViTs)의 연속 학습(CL) 문제를 다루며, 특히 파라미터 효율적 미세 조정(PEFT) 기법과의 교차점을 강조합니다. 저자들은 새로운 PEFT-CL 방법인 Dual Low-Rank Adaptation(DualLoRA)을 제안하여, 각 층에 직교 LoRA 어댑터와 잔여 LoRA 어댑터를 병렬로 도입합니다. 이는 동적 메모리 메커니즘을 통해 안정성과 가변성의 균형을 맞춥니다. 또한, 작업 식별을 예측하고 모델 출력을 보정하는 방식을 제안합니다. 실험 결과, DualLoRA는 다양한 벤치마크에서 기존 CL 방법들보다 정확성, 추론 속도, 계산 효율성에서 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 비전 트랜스포머(ViTs)의 연속 학습(CL)에서 파라미터 효율적 미세 조정(PEFT) 기법과의 교차가 중요해지고 있습니다.
- 2. DualLoRA는 정규 LoRA 어댑터와 잔여 LoRA 어댑터를 도입하여 각 층의 사전 학습된 가중치와 병렬로 작동합니다.
- 3. 동적 메모리 메커니즘을 통해 안정성과 가소성 간의 균형을 맞추는 DualLoRA 방법을 제안합니다.
- 4. DualLoRA는 작업 정체성을 예측하고 모델의 출력을 보정하는 방식을 제안합니다.
- 5. ViT 기반 모델에서 DualLoRA는 기존 CL 방법에 비해 정확도, 추론 속도, 훈련 시 계산 효율성에서 큰 이점을 제공합니다.


---

*Generated on 2025-09-26 08:36:42*