<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:38:33.165515",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "ConceptFlow",
    "Attention Mechanism",
    "Conceptual Pathways"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.78,
    "ConceptFlow": 0.82,
    "Attention Mechanism": 0.8,
    "Conceptual Pathways": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Convolutional Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "CNN",
          "ConvNet"
        ],
        "category": "broad_technical",
        "rationale": "Convolutional Neural Networks are a foundational concept in deep learning, linking to broader neural network research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "ConceptFlow",
        "canonical": "ConceptFlow",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "ConceptFlow is a novel framework introduced in the paper, providing a unique perspective on model interpretability.",
        "novelty_score": 0.92,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "concept attentions",
        "canonical": "Attention Mechanism",
        "aliases": [
          "conceptual attention"
        ],
        "category": "specific_connectable",
        "rationale": "Concept attentions relate to the attention mechanism, a key concept in understanding neural network interpretability.",
        "novelty_score": 0.58,
        "connectivity_score": 0.87,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "conceptual pathways",
        "canonical": "Conceptual Pathways",
        "aliases": [
          "concept pathways"
        ],
        "category": "unique_technical",
        "rationale": "Conceptual pathways are a unique element of the proposed framework, crucial for tracing concept propagation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "internal model reasoning",
      "semantic interpretation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Convolutional Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "ConceptFlow",
      "resolved_canonical": "ConceptFlow",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "concept attentions",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.87,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "conceptual pathways",
      "resolved_canonical": "Conceptual Pathways",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# ConceptFlow: Hierarchical and Fine-grained Concept-Based Explanation for Convolutional Neural Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18147.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18147](https://arxiv.org/abs/2509.18147)

## 🔗 유사한 논문
- [[2025-09-23/Show and Tell_ Visually Explainable Deep Neural Nets via Spatially-Aware Concept Bottleneck Models_20250923|Show and Tell: Visually Explainable Deep Neural Nets via Spatially-Aware Concept Bottleneck Models]] (85.4% similar)
- [[2025-09-23/Unsupervised Interpretable Basis Extraction for Concept-Based Visual Explanations_20250923|Unsupervised Interpretable Basis Extraction for Concept-Based Visual Explanations]] (83.7% similar)
- [[2025-09-23/Chat-CBM_ Towards Interactive Concept Bottleneck Models with Frozen Large Language Models_20250923|Chat-CBM: Towards Interactive Concept Bottleneck Models with Frozen Large Language Models]] (82.4% similar)
- [[2025-09-22/Incorporating Visual Cortical Lateral Connection Properties into CNN_ Recurrent Activation and Excitatory-Inhibitory Separation_20250922|Incorporating Visual Cortical Lateral Connection Properties into CNN: Recurrent Activation and Excitatory-Inhibitory Separation]] (81.7% similar)
- [[2025-09-23/WISE_ Weak-Supervision-Guided Step-by-Step Explanations for Multimodal LLMs in Image Classification_20250923|WISE: Weak-Supervision-Guided Step-by-Step Explanations for Multimodal LLMs in Image Classification]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/ConceptFlow|ConceptFlow]], [[keywords/Conceptual Pathways|Conceptual Pathways]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18147v1 Announce Type: cross 
Abstract: Concept-based interpretability for Convolutional Neural Networks (CNNs) aims to align internal model representations with high-level semantic concepts, but existing approaches largely overlook the semantic roles of individual filters and the dynamic propagation of concepts across layers. To address these limitations, we propose ConceptFlow, a concept-based interpretability framework that simulates the internal "thinking path" of a model by tracing how concepts emerge and evolve across layers. ConceptFlow comprises two key components: (i) concept attentions, which associate each filter with relevant high-level concepts to enable localized semantic interpretation, and (ii) conceptual pathways, derived from a concept transition matrix that quantifies how concepts propagate and transform between filters. Together, these components offer a unified and structured view of internal model reasoning. Experimental results demonstrate that ConceptFlow yields semantically meaningful insights into model reasoning, validating the effectiveness of concept attentions and conceptual pathways in explaining decision behavior. By modeling hierarchical conceptual pathways, ConceptFlow provides deeper insight into the internal logic of CNNs and supports the generation of more faithful and human-aligned explanations.

## 📝 요약

이 논문은 합성곱 신경망(CNN)의 개념 기반 해석 가능성을 향상시키기 위해 ConceptFlow라는 프레임워크를 제안합니다. 기존 방법들이 개별 필터의 의미적 역할과 계층 간 개념의 동적 전파를 간과하는 문제를 해결하고자, ConceptFlow는 모델의 내부 "사고 경로"를 시뮬레이션하여 개념이 계층을 통해 어떻게 나타나고 진화하는지를 추적합니다. 이 프레임워크는 두 가지 주요 구성 요소로 이루어져 있습니다: (i) 각 필터를 관련 고수준 개념과 연결하여 국소적 의미 해석을 가능하게 하는 개념 주의(concept attentions)와 (ii) 개념 전이 행렬을 통해 필터 간 개념의 전파와 변형을 정량화하는 개념 경로(conceptual pathways)입니다. 실험 결과, ConceptFlow는 모델의 추론에 대한 의미 있는 통찰을 제공하며, 개념 주의와 개념 경로의 효과성을 입증합니다. 이를 통해 CNN의 내부 논리에 대한 깊은 이해를 제공하고, 보다 신뢰할 수 있고 인간 친화적인 설명을 생성하는 데 기여합니다.

## 🎯 주요 포인트

- 1. ConceptFlow는 CNN의 내부 "사고 경로"를 시뮬레이션하여 개념이 레이어를 통해 어떻게 나타나고 발전하는지를 추적합니다.
- 2. ConceptFlow는 필터와 관련된 고수준 개념을 연관시켜 국지적 의미 해석을 가능하게 하는 개념 주의와 개념 전이 행렬을 기반으로 한 개념적 경로를 포함합니다.
- 3. 실험 결과, ConceptFlow는 모델 추론에 대한 의미 있는 통찰을 제공하며, 개념 주의와 개념적 경로의 효과성을 입증합니다.
- 4. ConceptFlow는 계층적 개념 경로를 모델링하여 CNN의 내부 논리에 대한 깊은 통찰을 제공하고, 보다 신뢰할 수 있고 인간 친화적인 설명을 지원합니다.


---

*Generated on 2025-09-24 13:38:33*