---
keywords:
  - Graph Neural Network
  - Transformer
  - Self-supervised Learning
  - Oligopeptide-Infectious Disease Association
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20290
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:05:36.240869",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Transformer",
    "Self-supervised Learning",
    "Oligopeptide-Infectious Disease Association"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.82,
    "Transformer": 0.8,
    "Self-supervised Learning": 0.78,
    "Oligopeptide-Infectious Disease Association": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Convolutional Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GCN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Convolutional Networks are a subset of Graph Neural Networks, facilitating connections to broader graph-based learning discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are fundamental in modern machine learning, linking to various advanced architectures and applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Contrastive Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Contrastive learning is a key technique in self-supervised learning, enabling connections to unsupervised data representation methods.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      },
      {
        "surface": "Oligopeptide-Infectious Disease Association",
        "canonical": "Oligopeptide-Infectious Disease Association",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This specific association is central to the paper's focus, offering unique insights into niche biomedical applications.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "tripartite graph",
      "multilayer perceptron",
      "benchmark dataset"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Convolutional Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Contrastive Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Oligopeptide-Infectious Disease Association",
      "resolved_canonical": "Oligopeptide-Infectious Disease Association",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# PGCLODA: Prompt-Guided Graph Contrastive Learning for Oligopeptide-Infectious Disease Association Prediction

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20290.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20290](https://arxiv.org/abs/2509.20290)

## 🔗 유사한 논문
- [[2025-09-17/PhenoGnet_ A Graph-Based Contrastive Learning Framework for Disease Similarity Prediction_20250917|PhenoGnet: A Graph-Based Contrastive Learning Framework for Disease Similarity Prediction]] (84.1% similar)
- [[2025-09-23/Learning Massive-scale Partial Correlation Networks in Clinical Multi-omics Studies with HP-ACCORD_20250923|Learning Massive-scale Partial Correlation Networks in Clinical Multi-omics Studies with HP-ACCORD]] (80.4% similar)
- [[2025-09-22/Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation_20250922|Temperature-Driven Robust Disease Detection in Brain and Gastrointestinal Disorders via Context-Aware Adaptive Knowledge Distillation]] (80.3% similar)
- [[2025-09-23/DPASyn_ Mechanism-Aware Drug Synergy Prediction via Dual Attention and Precision-Aware Quantization_20250923|DPASyn: Mechanism-Aware Drug Synergy Prediction via Dual Attention and Precision-Aware Quantization]] (80.1% similar)
- [[2025-09-24/Learning Contrastive Multimodal Fusion with Improved Modality Dropout for Disease Detection and Prediction_20250924|Learning Contrastive Multimodal Fusion with Improved Modality Dropout for Disease Detection and Prediction]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Oligopeptide-Infectious Disease Association|Oligopeptide-Infectious Disease Association]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20290v1 Announce Type: cross 
Abstract: Infectious diseases continue to pose a serious threat to public health, underscoring the urgent need for effective computational approaches to screen novel anti-infective agents. Oligopeptides have emerged as promising candidates in antimicrobial research due to their structural simplicity, high bioavailability, and low susceptibility to resistance. Despite their potential, computational models specifically designed to predict associations between oligopeptides and infectious diseases remain scarce. This study introduces a prompt-guided graph-based contrastive learning framework (PGCLODA) to uncover potential associations. A tripartite graph is constructed with oligopeptides, microbes, and diseases as nodes, incorporating both structural and semantic information. To preserve critical regions during contrastive learning, a prompt-guided graph augmentation strategy is employed to generate meaningful paired views. A dual encoder architecture, integrating Graph Convolutional Network (GCN) and Transformer, is used to jointly capture local and global features. The fused embeddings are subsequently input into a multilayer perceptron (MLP) classifier for final prediction. Experimental results on a benchmark dataset indicate that PGCLODA consistently outperforms state-of-the-art models in AUROC, AUPRC, and accuracy. Ablation and hyperparameter studies confirm the contribution of each module. Case studies further validate the generalization ability of PGCLODA and its potential to uncover novel, biologically relevant associations. These findings offer valuable insights for mechanism-driven discovery and oligopeptide-based drug development. The source code of PGCLODA is available online at https://github.com/jjnlcode/PGCLODA.

## 📝 요약

이 연구는 감염병과 올리고펩타이드 간의 연관성을 예측하기 위한 컴퓨팅 모델의 부족을 해결하기 위해, PGCLODA라는 프롬프트 기반 그래프 대조 학습 프레임워크를 제안합니다. 이 모델은 올리고펩타이드, 미생물, 질병을 노드로 하는 삼중 그래프를 구축하고, 구조적 및 의미적 정보를 통합합니다. 그래프 컨볼루션 네트워크(GCN)와 트랜스포머를 결합한 이중 인코더 아키텍처를 사용하여 지역 및 전역 특징을 포착하며, 최종 예측을 위해 다층 퍼셉트론(MLP) 분류기에 입력됩니다. 실험 결과, PGCLODA는 AUROC, AUPRC, 정확도에서 기존 모델보다 우수한 성능을 보였으며, 모듈별 기여도도 확인되었습니다. 이 연구는 메커니즘 기반 발견과 올리고펩타이드 기반 약물 개발에 유용한 통찰을 제공합니다. PGCLODA의 소스 코드는 온라인에서 이용 가능합니다.

## 🎯 주요 포인트

- 1. 감염병에 대한 새로운 항감염제 후보로 올리고펩타이드가 주목받고 있으며, 이를 예측하는 컴퓨터 모델이 부족한 상황이다.
- 2. 본 연구는 올리고펩타이드, 미생물, 질병 간의 잠재적 연관성을 발견하기 위해 PGCLODA라는 프롬프트 기반 그래프 대조 학습 프레임워크를 도입하였다.
- 3. PGCLODA는 그래프 컨볼루션 네트워크(GCN)와 트랜스포머를 통합한 이중 인코더 아키텍처를 사용하여 지역 및 전역 특징을 포착한다.
- 4. 실험 결과, PGCLODA는 AUROC, AUPRC, 정확도에서 최신 모델들을 지속적으로 능가하는 성능을 보였다.
- 5. PGCLODA의 소스 코드는 온라인에서 제공되며, 새로운 생물학적 연관성을 발견하는 데 유용한 도구로 활용될 수 있다.


---

*Generated on 2025-09-25 16:05:36*