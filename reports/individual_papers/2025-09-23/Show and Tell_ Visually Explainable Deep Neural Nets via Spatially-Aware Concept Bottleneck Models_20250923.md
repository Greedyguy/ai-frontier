---
keywords:
  - Neural Network
  - Concept Bottleneck Model
  - Spatially-Aware Concept Bottleneck Model
  - Zero-Shot Learning
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2502.20134
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:18:06.408771",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Concept Bottleneck Model",
    "Spatially-Aware Concept Bottleneck Model",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Concept Bottleneck Model": 0.8,
    "Spatially-Aware Concept Bottleneck Model": 0.78,
    "Zero-Shot Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "DNN",
          "Deep Learning Models"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are central to the paper's methodology and connect to a wide range of related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Concept Bottleneck Models",
        "canonical": "Concept Bottleneck Model",
        "aliases": [
          "CBM",
          "Concept Bottleneck"
        ],
        "category": "unique_technical",
        "rationale": "This is a core innovation of the paper, offering a new approach to model interpretability.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Spatially-Aware Concept Bottleneck Model",
        "canonical": "Spatially-Aware Concept Bottleneck Model",
        "aliases": [
          "SALF-CBM"
        ],
        "category": "unique_technical",
        "rationale": "This specific model is a novel contribution that enhances interpretability in neural networks.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Zero-Shot Segmentation",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot Segmentation Task"
        ],
        "category": "specific_connectable",
        "rationale": "The paper demonstrates improved performance in zero-shot tasks, linking to broader zero-shot learning research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "task",
      "model"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Concept Bottleneck Models",
      "resolved_canonical": "Concept Bottleneck Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Spatially-Aware Concept Bottleneck Model",
      "resolved_canonical": "Spatially-Aware Concept Bottleneck Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Zero-Shot Segmentation",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Show and Tell: Visually Explainable Deep Neural Nets via Spatially-Aware Concept Bottleneck Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2502.20134.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2502.20134](https://arxiv.org/abs/2502.20134)

## 🔗 유사한 논문
- [[2025-09-23/Chat-CBM_ Towards Interactive Concept Bottleneck Models with Frozen Large Language Models_20250923|Chat-CBM: Towards Interactive Concept Bottleneck Models with Frozen Large Language Models]] (85.0% similar)
- [[2025-09-22/Bayesian Concept Bottleneck Models with LLM Priors_20250922|Bayesian Concept Bottleneck Models with LLM Priors]] (84.4% similar)
- [[2025-09-23/V-CECE_ Visual Counterfactual Explanations via Conceptual Edits_20250923|V-CECE: Visual Counterfactual Explanations via Conceptual Edits]] (83.1% similar)
- [[2025-09-22/Multi-Modal Interpretability for Enhanced Localization in Vision-Language Models_20250922|Multi-Modal Interpretability for Enhanced Localization in Vision-Language Models]] (82.7% similar)
- [[2025-09-23/WISE_ Weak-Supervision-Guided Step-by-Step Explanations for Multimodal LLMs in Image Classification_20250923|WISE: Weak-Supervision-Guided Step-by-Step Explanations for Multimodal LLMs in Image Classification]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Concept Bottleneck Model|Concept Bottleneck Model]], [[keywords/Spatially-Aware Concept Bottleneck Model|Spatially-Aware Concept Bottleneck Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.20134v4 Announce Type: replace 
Abstract: Modern deep neural networks have now reached human-level performance across a variety of tasks. However, unlike humans they lack the ability to explain their decisions by showing where and telling what concepts guided them. In this work, we present a unified framework for transforming any vision neural network into a spatially and conceptually interpretable model. We introduce a spatially-aware concept bottleneck layer that projects "black-box" features of pre-trained backbone models into interpretable concept maps, without requiring human labels. By training a classification layer over this bottleneck, we obtain a self-explaining model that articulates which concepts most influenced its prediction, along with heatmaps that ground them in the input image. Accordingly, we name this method "Spatially-Aware and Label-Free Concept Bottleneck Model" (SALF-CBM). Our results show that the proposed SALF-CBM: (1) Outperforms non-spatial CBM methods, as well as the original backbone, on a variety of classification tasks; (2) Produces high-quality spatial explanations, outperforming widely used heatmap-based methods on a zero-shot segmentation task; (3) Facilitates model exploration and debugging, enabling users to query specific image regions and refine the model's decisions by locally editing its concept maps.

## 📝 요약

이 연구는 모든 비전 신경망을 공간적 및 개념적으로 해석 가능한 모델로 변환하는 통합 프레임워크를 제안합니다. 연구에서는 인간의 레이블 없이도 사전 학습된 모델의 "블랙박스" 특징을 해석 가능한 개념 맵으로 변환하는 공간 인식 개념 병목층을 도입했습니다. 이를 통해 예측에 가장 큰 영향을 미친 개념을 설명하고 입력 이미지에 이를 시각적으로 표현하는 자기 설명 모델을 구축했습니다. 제안된 방법인 SALF-CBM은 다양한 분류 작업에서 기존 방법보다 우수한 성능을 보였으며, 고품질의 공간적 설명을 제공하여 모델 탐색 및 디버깅을 용이하게 합니다.

## 🎯 주요 포인트

- 1. SALF-CBM은 사전 학습된 모델의 "블랙박스" 특징을 해석 가능한 개념 지도에 투영하여 공간적 및 개념적으로 해석 가능한 모델을 제공합니다.
- 2. 이 모델은 인간의 레이블 없이도 공간적으로 인식 가능한 개념 병목 레이어를 도입하여 모델의 예측에 가장 큰 영향을 미친 개념을 설명할 수 있습니다.
- 3. SALF-CBM은 다양한 분류 작업에서 비공간적 CBM 방법 및 원래 백본 모델보다 우수한 성능을 보입니다.
- 4. 제안된 모델은 제로샷 분할 작업에서 널리 사용되는 히트맵 기반 방법보다 뛰어난 고품질의 공간적 설명을 생성합니다.
- 5. 사용자는 특정 이미지 영역을 쿼리하고 개념 지도를 로컬로 편집하여 모델의 결정을 개선할 수 있어 모델 탐색 및 디버깅을 용이하게 합니다.


---

*Generated on 2025-09-24 05:18:06*