---
keywords:
  - Attention Mechanism
  - Precision-Aware Quantization
  - Drug Synergy Prediction
  - Graph Neural Network
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2505.19144
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:44:34.335040",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Attention Mechanism",
    "Precision-Aware Quantization",
    "Drug Synergy Prediction",
    "Graph Neural Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Attention Mechanism": 0.82,
    "Precision-Aware Quantization": 0.79,
    "Drug Synergy Prediction": 0.81,
    "Graph Neural Network": 0.83
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "dual-attention mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "dual-attention"
        ],
        "category": "specific_connectable",
        "rationale": "The dual-attention mechanism is a specific application of the broader attention mechanism, enhancing connectivity with related models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Precision-Aware Quantization",
        "canonical": "Precision-Aware Quantization",
        "aliases": [
          "PAQ"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel technique introduced in the paper, providing a unique approach to optimizing computational efficiency.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      },
      {
        "surface": "drug synergy prediction",
        "canonical": "Drug Synergy Prediction",
        "aliases": [
          "synergy prediction"
        ],
        "category": "unique_technical",
        "rationale": "The paper focuses on predicting drug synergies, a specific and novel application in computational biology.",
        "novelty_score": 0.78,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.81
      },
      {
        "surface": "graph-based approaches",
        "canonical": "Graph Neural Network",
        "aliases": [
          "graph-based methods"
        ],
        "category": "specific_connectable",
        "rationale": "Graph-based approaches are integral to the model's architecture, linking well with existing graph neural network research.",
        "novelty_score": 0.48,
        "connectivity_score": 0.88,
        "specificity_score": 0.76,
        "link_intent_score": 0.83
      }
    ],
    "ban_list_suggestions": [
      "drug combinations",
      "experimental screening",
      "computational models"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "dual-attention mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Precision-Aware Quantization",
      "resolved_canonical": "Precision-Aware Quantization",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "drug synergy prediction",
      "resolved_canonical": "Drug Synergy Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "graph-based approaches",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.88,
        "specificity": 0.76,
        "link_intent": 0.83
      }
    }
  ]
}
-->

# DPASyn: Mechanism-Aware Drug Synergy Prediction via Dual Attention and Precision-Aware Quantization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.19144.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2505.19144](https://arxiv.org/abs/2505.19144)

## 🔗 유사한 논문
- [[2025-09-22/A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction_20250922|A Multi-Scale Graph Neural Process with Cross-Drug Co-Attention for Drug-Drug Interactions Prediction]] (87.0% similar)
- [[2025-09-18/Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (83.2% similar)
- [[2025-09-22/Rethinking Molecule Synthesizability with Chain-of-Reaction_20250922|Rethinking Molecule Synthesizability with Chain-of-Reaction]] (80.0% similar)
- [[2025-09-23/TF-DWGNet_ A Directed Weighted Graph Neural Network with Tensor Fusion for Multi-Omics Cancer Subtype Classification_20250923|TF-DWGNet: A Directed Weighted Graph Neural Network with Tensor Fusion for Multi-Omics Cancer Subtype Classification]] (79.8% similar)
- [[2025-09-23/Medical priority fusion_ achieving dual optimization of sensitivity and interpretability in nipt anomaly detection_20250923|Medical priority fusion: achieving dual optimization of sensitivity and interpretability in nipt anomaly detection]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Precision-Aware Quantization|Precision-Aware Quantization]], [[keywords/Drug Synergy Prediction|Drug Synergy Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.19144v2 Announce Type: replace 
Abstract: Drug combinations are essential in cancer therapy, leveraging synergistic drug-drug interactions (DDI) to enhance efficacy and combat resistance. However, the vast combinatorial space makes experimental screening impractical, and existing computational models struggle to capture the complex, bidirectional nature of DDIs, often relying on independent drug encoding or simplistic fusion strategies that miss fine-grained inter-molecular dynamics. Moreover, state-of-the-art graph-based approaches suffer from high computational costs, limiting scalability for real-world drug discovery. To address this, we propose DPASyn, a novel drug synergy prediction framework featuring a dual-attention mechanism and Precision-Aware Quantization (PAQ). The dual-attention architecture jointly models intra-drug structures and inter-drug interactions via shared projections and cross-drug attention, enabling fine-grained, biologically plausible synergy modeling. While this enhanced expressiveness brings increased computational resource consumption, our proposed PAQ strategy complements it by dynamically optimizing numerical precision during training based on feature sensitivity-reducing memory usage by 40% and accelerating training threefold without sacrificing accuracy. With LayerNorm-stabilized residual connections for training stability, DPASyn outperforms seven state-of-the-art methods on the O'Neil dataset (13,243 combinations) and supports full-batch processing of up to 256 graphs on a single GPU, setting a new standard for efficient and expressive drug synergy prediction.

## 📝 요약

이 논문은 암 치료에서 약물 병합의 시너지 효과를 예측하는 새로운 프레임워크인 DPASyn을 제안합니다. 기존 모델들이 복잡한 약물 간 상호작용을 제대로 포착하지 못하는 문제를 해결하기 위해, DPASyn은 이중 주의 메커니즘과 정밀도 인식 양자화(PAQ)를 도입합니다. 이중 주의 구조는 약물 내 구조와 약물 간 상호작용을 정밀하게 모델링하며, PAQ는 메모리 사용량을 40% 줄이고 학습 속도를 세 배로 증가시킵니다. DPASyn은 O'Neil 데이터셋에서 기존 7가지 최첨단 방법을 능가하며, 단일 GPU에서 최대 256개의 그래프를 처리할 수 있는 효율성과 표현력을 제공합니다.

## 🎯 주요 포인트

- 1. DPASyn은 이중 주의 메커니즘과 정밀도 인식 양자화를 특징으로 하는 새로운 약물 시너지 예측 프레임워크입니다.
- 2. 이중 주의 아키텍처는 약물 내 구조와 약물 간 상호작용을 공동으로 모델링하여 세밀하고 생물학적으로 타당한 시너지 모델링을 가능하게 합니다.
- 3. 정밀도 인식 양자화 전략은 메모리 사용량을 40% 줄이고 학습 속도를 3배 향상시키면서도 정확도를 유지합니다.
- 4. DPASyn은 O'Neil 데이터셋에서 13,243개의 조합을 대상으로 7개의 최신 방법을 능가하며, 단일 GPU에서 최대 256개의 그래프를 전체 배치로 처리할 수 있습니다.
- 5. LayerNorm으로 안정성을 확보한 잔차 연결을 통해 DPASyn은 효율적이고 표현력 있는 약물 시너지 예측의 새로운 기준을 제시합니다.


---

*Generated on 2025-09-24 02:44:34*