<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:46:05.140467",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Prototype Embeddings",
    "Conceptual Spaces",
    "Explainable AI"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Prototype Embeddings": 0.78,
    "Conceptual Spaces": 0.82,
    "Explainable AI": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's methodology and connect to a wide range of AI topics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Prototype Embeddings",
        "canonical": "Prototype Embeddings",
        "aliases": [
          "Prototype-based Embeddings"
        ],
        "category": "unique_technical",
        "rationale": "Prototype Embeddings are a novel approach introduced in the paper, crucial for linking conceptual spaces.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Conceptual Spaces",
        "canonical": "Conceptual Spaces",
        "aliases": [
          "Concept Spaces"
        ],
        "category": "unique_technical",
        "rationale": "Conceptual Spaces are a key theoretical framework in the paper, essential for understanding the proposed method.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Explainable AI",
        "canonical": "Explainable AI",
        "aliases": [
          "XAI"
        ],
        "category": "specific_connectable",
        "rationale": "Explainable AI is a significant application area for the research, providing a bridge to broader AI discussions.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "perceptual features",
      "cognitive science"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Prototype Embeddings",
      "resolved_canonical": "Prototype Embeddings",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Conceptual Spaces",
      "resolved_canonical": "Conceptual Spaces",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Explainable AI",
      "resolved_canonical": "Explainable AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Extracting Conceptual Spaces from LLMs Using Prototype Embeddings

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19269.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.19269](https://arxiv.org/abs/2509.19269)

## 🔗 유사한 논문
- [[2025-09-22/Capturing Polysemanticity with PRISM_ A Multi-Concept Feature Description Framework_20250922|Capturing Polysemanticity with PRISM: A Multi-Concept Feature Description Framework]] (83.8% similar)
- [[2025-09-23/LLMs as Layout Designers_ A Spatial Reasoning Perspective_20250923|LLMs as Layout Designers: A Spatial Reasoning Perspective]] (82.4% similar)
- [[2025-09-19/Large Multi-modal Models Can Interpret Features in Large Multi-modal Models_20250919|Large Multi-modal Models Can Interpret Features in Large Multi-modal Models]] (81.6% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (81.5% similar)
- [[2025-09-23/Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning_20250923|Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Explainable AI|Explainable AI]]
**⚡ Unique Technical**: [[keywords/Prototype Embeddings|Prototype Embeddings]], [[keywords/Conceptual Spaces|Conceptual Spaces]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19269v1 Announce Type: new 
Abstract: Conceptual spaces represent entities and concepts using cognitively meaningful dimensions, typically referring to perceptual features. Such representations are widely used in cognitive science and have the potential to serve as a cornerstone for explainable AI. Unfortunately, they have proven notoriously difficult to learn, although recent LLMs appear to capture the required perceptual features to a remarkable extent. Nonetheless, practical methods for extracting the corresponding conceptual spaces are currently still lacking. While various methods exist for extracting embeddings from LLMs, extracting conceptual spaces also requires us to encode the underlying features. In this paper, we propose a strategy in which features (e.g. sweetness) are encoded by embedding the description of a corresponding prototype (e.g. a very sweet food). To improve this strategy, we fine-tune the LLM to align the prototype embeddings with the corresponding conceptual space dimensions. Our empirical analysis finds this approach to be highly effective.

## 📝 요약

이 논문은 개념적 공간을 설명 가능한 AI의 기초로 활용할 수 있는 가능성을 탐구합니다. 개념적 공간은 인지적으로 의미 있는 차원을 사용하여 개체와 개념을 표현하지만, 학습하기 어려운 것으로 알려져 있습니다. 최근 대형 언어 모델(LLM)이 이러한 지각적 특징을 잘 포착하지만, 실제로 개념적 공간을 추출하는 방법은 부족합니다. 이 논문에서는 특징(예: 단맛)을 설명하는 프로토타입(예: 매우 단 음식)의 설명을 임베딩하여 인코딩하는 전략을 제안합니다. 또한, 프로토타입 임베딩을 개념적 공간 차원과 정렬하기 위해 LLM을 미세 조정합니다. 실증 분석 결과, 이 접근 방식이 매우 효과적임을 발견했습니다.

## 🎯 주요 포인트

- 1. 개념적 공간은 인지적으로 의미 있는 차원을 사용하여 개체와 개념을 표현하며, 이는 주로 지각적 특징을 참조한다.
- 2. 최근의 대형 언어 모델(LLM)은 요구되는 지각적 특징을 상당한 정도로 포착하는 것으로 보인다.
- 3. 개념적 공간을 추출하기 위한 실질적인 방법은 아직 부족하다.
- 4. 본 논문에서는 프로토타입의 설명을 임베딩하여 특징을 인코딩하는 전략을 제안한다.
- 5. 제안된 방법은 프로토타입 임베딩을 개념적 공간 차원과 정렬하도록 LLM을 미세 조정하여 효과적임을 실증적으로 분석하였다.


---

*Generated on 2025-09-24 15:46:05*