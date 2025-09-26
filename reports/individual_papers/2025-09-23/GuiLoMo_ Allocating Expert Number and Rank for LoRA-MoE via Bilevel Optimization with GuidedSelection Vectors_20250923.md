---
keywords:
  - Low-Rank Adaptation
  - Mixture-of-Experts
  - GuidedSelection Vectors
  - Bilevel Optimization
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2506.14646
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:05:37.152540",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Low-Rank Adaptation",
    "Mixture-of-Experts",
    "GuidedSelection Vectors",
    "Bilevel Optimization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Low-Rank Adaptation": 0.75,
    "Mixture-of-Experts": 0.8,
    "GuidedSelection Vectors": 0.7,
    "Bilevel Optimization": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Low-Rank Adaptation",
        "canonical": "Low-Rank Adaptation",
        "aliases": [
          "LoRA"
        ],
        "category": "unique_technical",
        "rationale": "LoRA is a specific technique for parameter-efficient fine-tuning, crucial for adapting large language models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Mixture-of-Experts",
        "canonical": "Mixture-of-Experts",
        "aliases": [
          "MoE"
        ],
        "category": "specific_connectable",
        "rationale": "MoE is a significant concept in enhancing model capacity and is relevant for linking with other expert-based methods.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "GuidedSelection Vectors",
        "canonical": "GuidedSelection Vectors",
        "aliases": [
          "GSVs"
        ],
        "category": "unique_technical",
        "rationale": "GSVs are a novel mechanism proposed in the paper for optimizing expert allocation, offering a unique linking opportunity.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Bilevel Optimization",
        "canonical": "Bilevel Optimization",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Bilevel optimization is a key method used in the paper, relevant for linking with optimization techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "fine-tuning",
      "performance",
      "backbone models"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Low-Rank Adaptation",
      "resolved_canonical": "Low-Rank Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Mixture-of-Experts",
      "resolved_canonical": "Mixture-of-Experts",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "GuidedSelection Vectors",
      "resolved_canonical": "GuidedSelection Vectors",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Bilevel Optimization",
      "resolved_canonical": "Bilevel Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# GuiLoMo: Allocating Expert Number and Rank for LoRA-MoE via Bilevel Optimization with GuidedSelection Vectors

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.14646.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2506.14646](https://arxiv.org/abs/2506.14646)

## 🔗 유사한 논문
- [[2025-09-23/Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA_20250923|Robust Federated Finetuning of LLMs via Alternating Optimization of LoRA]] (86.1% similar)
- [[2025-09-23/MoEs Are Stronger than You Think_ Hyper-Parallel Inference Scaling with RoE_20250923|MoEs Are Stronger than You Think: Hyper-Parallel Inference Scaling with RoE]] (85.4% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box: Interpretable LLMs via Semantic Resonance Architecture]] (84.9% similar)
- [[2025-09-17/Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection_20250917|Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (84.3% similar)
- [[2025-09-23/SparseDoctor_ Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models_20250923|SparseDoctor: Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Mixture-of-Experts|Mixture-of-Experts]], [[keywords/Bilevel Optimization|Bilevel Optimization]]
**⚡ Unique Technical**: [[keywords/Low-Rank Adaptation|Low-Rank Adaptation]], [[keywords/GuidedSelection Vectors|GuidedSelection Vectors]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.14646v2 Announce Type: replace 
Abstract: Parameter-efficient fine-tuning (PEFT) methods, particularly Low-Rank Adaptation (LoRA), offer an efficient way to adapt large language models with reduced computational costs. However, their performance is limited by the small number of trainable parameters. Recent work combines LoRA with the Mixture-of-Experts (MoE), i.e., LoRA-MoE, to enhance capacity, but two limitations remain in hindering the full exploitation of its potential: 1) the influence of downstream tasks when assigning expert numbers, and 2) the uniform rank assignment across all LoRA experts, which restricts representational diversity. To mitigate these gaps, we propose GuiLoMo, a fine-grained layer-wise expert numbers and ranks allocation strategy with GuidedSelection Vectors (GSVs). GSVs are learned via a prior bilevel optimization process to capture both model- and task-specific needs, and are then used to allocate optimal expert numbers and ranks. Experiments on three backbone models across diverse benchmarks show that GuiLoMo consistently achieves superior or comparable performance to all baselines. Further analysis offers key insights into how expert numbers and ranks vary across layers and tasks, highlighting the benefits of adaptive expert configuration. Our code is available at https://github.com/Liar406/Gui-LoMo.git.

## 📝 요약

이 논문은 대규모 언어 모델을 효율적으로 적응시키기 위한 방법으로 Low-Rank Adaptation (LoRA)와 Mixture-of-Experts (MoE)를 결합한 LoRA-MoE의 한계를 극복하기 위해 GuiLoMo를 제안합니다. GuiLoMo는 GuidedSelection Vectors (GSVs)를 통해 세밀한 레이어별 전문가 수와 랭크를 할당하여 모델과 작업의 특수한 요구를 반영합니다. 실험 결과, GuiLoMo는 다양한 벤치마크에서 기존 방법들과 비교해 우수하거나 동등한 성능을 보였으며, 레이어와 작업에 따라 전문가 수와 랭크가 어떻게 변화하는지에 대한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. LoRA-MoE의 한계를 극복하기 위해 GuiLoMo를 제안하여 레이어별 전문가 수와 순위를 세밀하게 할당하는 전략을 도입했습니다.
- 2. GuidedSelection Vectors (GSVs)를 통해 모델 및 작업별 요구 사항을 반영하여 최적의 전문가 수와 순위를 할당합니다.
- 3. GuiLoMo는 다양한 벤치마크에서 기존 방법들과 비교하여 일관되게 우수하거나 유사한 성능을 보여줍니다.
- 4. 실험 분석을 통해 레이어와 작업에 따라 전문가 수와 순위가 어떻게 달라지는지에 대한 중요한 통찰을 제공합니다.


---

*Generated on 2025-09-24 04:05:37*