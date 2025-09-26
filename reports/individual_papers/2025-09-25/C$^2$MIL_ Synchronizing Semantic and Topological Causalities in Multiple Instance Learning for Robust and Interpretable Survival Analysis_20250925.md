---
keywords:
  - Multiple Instance Learning
  - Graph Neural Network
  - Causal Graph
  - Semantic Causal Intervention
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.20152
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:13:31.561710",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multiple Instance Learning",
    "Graph Neural Network",
    "Causal Graph",
    "Semantic Causal Intervention"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multiple Instance Learning": 0.78,
    "Graph Neural Network": 0.8,
    "Causal Graph": 0.77,
    "Semantic Causal Intervention": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multiple Instance Learning",
        "canonical": "Multiple Instance Learning",
        "aliases": [
          "MIL"
        ],
        "category": "specific_connectable",
        "rationale": "Multiple Instance Learning is a key technique in the paper, relevant for linking to other works in survival analysis and graph-based learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Graph-based MIL",
        "canonical": "Graph Neural Network",
        "aliases": [
          "Graph-based Multiple Instance Learning"
        ],
        "category": "specific_connectable",
        "rationale": "The use of graph structures in MIL aligns with Graph Neural Networks, facilitating connections to related graph-based methodologies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Causal Graph",
        "canonical": "Causal Graph",
        "aliases": [
          "Causal Graph Model"
        ],
        "category": "unique_technical",
        "rationale": "Causal Graphs are central to the proposed model, providing a unique perspective on causal discovery in MIL.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Semantic Causal Intervention",
        "canonical": "Semantic Causal Intervention",
        "aliases": [
          "Semantic Intervention"
        ],
        "category": "unique_technical",
        "rationale": "This concept is novel and specific to the paper's approach, offering a unique angle for linking to causal inference studies.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "survival analysis",
      "whole slide images"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multiple Instance Learning",
      "resolved_canonical": "Multiple Instance Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Graph-based MIL",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Causal Graph",
      "resolved_canonical": "Causal Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Semantic Causal Intervention",
      "resolved_canonical": "Semantic Causal Intervention",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# C$^2$MIL: Synchronizing Semantic and Topological Causalities in Multiple Instance Learning for Robust and Interpretable Survival Analysis

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20152.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.20152](https://arxiv.org/abs/2509.20152)

## 🔗 유사한 논문
- [[2025-09-23/WISE_ Weak-Supervision-Guided Step-by-Step Explanations for Multimodal LLMs in Image Classification_20250923|WISE: Weak-Supervision-Guided Step-by-Step Explanations for Multimodal LLMs in Image Classification]] (81.5% similar)
- [[2025-09-23/Revealing Multimodal Causality with Large Language Models_20250923|Revealing Multimodal Causality with Large Language Models]] (80.9% similar)
- [[2025-09-23/ME-Mamba_ Multi-Expert Mamba with Efficient Knowledge Capture and Fusion for Multimodal Survival Analysis_20250923|ME-Mamba: Multi-Expert Mamba with Efficient Knowledge Capture and Fusion for Multimodal Survival Analysis]] (80.7% similar)
- [[2025-09-23/Causal Representation Learning from Multimodal Clinical Records under Non-Random Modality Missingness_20250923|Causal Representation Learning from Multimodal Clinical Records under Non-Random Modality Missingness]] (80.6% similar)
- [[2025-09-23/Describe-to-Score_ Text-Guided Efficient Image Complexity Assessment_20250923|Describe-to-Score: Text-Guided Efficient Image Complexity Assessment]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multiple Instance Learning|Multiple Instance Learning]], [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Causal Graph|Causal Graph]], [[keywords/Semantic Causal Intervention|Semantic Causal Intervention]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20152v1 Announce Type: new 
Abstract: Graph-based Multiple Instance Learning (MIL) is widely used in survival analysis with Hematoxylin and Eosin (H\&amp;E)-stained whole slide images (WSIs) due to its ability to capture topological information. However, variations in staining and scanning can introduce semantic bias, while topological subgraphs that are not relevant to the causal relationships can create noise, resulting in biased slide-level representations. These issues can hinder both the interpretability and generalization of the analysis. To tackle this, we introduce a dual structural causal model as the theoretical foundation and propose a novel and interpretable dual causal graph-based MIL model, C$^2$MIL. C$^2$MIL incorporates a novel cross-scale adaptive feature disentangling module for semantic causal intervention and a new Bernoulli differentiable causal subgraph sampling method for topological causal discovery. A joint optimization strategy combining disentangling supervision and contrastive learning enables simultaneous refinement of both semantic and topological causalities. Experiments demonstrate that C$^2$MIL consistently improves generalization and interpretability over existing methods and can serve as a causal enhancement for diverse MIL baselines. The code is available at https://github.com/mimic0127/C2MIL.

## 📝 요약

이 논문은 Hematoxylin과 Eosin 염색된 전 슬라이드 이미지(WSI)를 활용한 생존 분석에서 그래프 기반 다중 인스턴스 학습(MIL)의 문제점을 해결하기 위해 새로운 모델 C$^2$MIL을 제안합니다. 기존 방법은 염색 및 스캔의 변동성과 관련 없는 위상적 서브그래프가 분석의 해석성과 일반화를 저해할 수 있습니다. 이를 해결하기 위해, 저자들은 이중 구조적 인과 모델을 이론적 기반으로 삼아, 의미론적 인과 개입을 위한 적응형 특징 분리 모듈과 위상적 인과 발견을 위한 베르누이 미분 가능한 인과 서브그래프 샘플링 방법을 도입했습니다. 실험 결과, C$^2$MIL은 기존 방법들보다 일반화와 해석성을 꾸준히 개선하며 다양한 MIL 기반 모델에 인과적 향상을 제공합니다.

## 🎯 주요 포인트

- 1. 그래프 기반 다중 인스턴스 학습(MIL)은 H&E 염색 전장 슬라이드 이미지의 생존 분석에서 위상 정보를 포착하는 데 사용된다.
- 2. 염색 및 스캔의 변동은 의미론적 편향을 초래할 수 있으며, 관련 없는 위상 하위 그래프는 노이즈를 발생시켜 슬라이드 수준의 표현에 편향을 줄 수 있다.
- 3. C$^2$MIL은 의미론적 인과 개입을 위한 적응형 특징 분리 모듈과 위상 인과 발견을 위한 새로운 베르누이 미분 가능한 인과 하위 그래프 샘플링 방법을 통합한다.
- 4. 실험 결과, C$^2$MIL은 기존 방법보다 일반화 및 해석 가능성을 지속적으로 개선하며, 다양한 MIL 기반에 대한 인과적 향상을 제공할 수 있다.
- 5. C$^2$MIL의 코드는 https://github.com/mimic0127/C2MIL에서 제공된다.


---

*Generated on 2025-09-26 09:13:31*