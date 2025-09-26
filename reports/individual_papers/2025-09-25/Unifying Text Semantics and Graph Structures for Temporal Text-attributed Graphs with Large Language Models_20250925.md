---
keywords:
  - Graph Neural Network
  - Temporal Text-attributed Graphs
  - Large Language Model
  - Semantic-structural Co-encoder
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2503.14411
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:21:34.269851",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Temporal Text-attributed Graphs",
    "Large Language Model",
    "Semantic-structural Co-encoder"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.8,
    "Temporal Text-attributed Graphs": 0.78,
    "Large Language Model": 0.85,
    "Semantic-structural Co-encoder": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Temporal Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "TGNN",
          "Temporal GNN"
        ],
        "category": "specific_connectable",
        "rationale": "This term directly connects to existing Graph Neural Network concepts, enhancing temporal modeling discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Temporal Text-attributed Graphs",
        "canonical": "Temporal Text-attributed Graphs",
        "aliases": [
          "TTAGs"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique concept introduced in the paper, essential for discussions on text and graph integration.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "This term is crucial for linking discussions on advanced language processing techniques.",
        "novelty_score": 0.3,
        "connectivity_score": 0.92,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Semantic-structural Co-encoder",
        "canonical": "Semantic-structural Co-encoder",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This is a novel framework component that integrates semantics and structure, pivotal for the paper's methodology.",
        "novelty_score": 0.78,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "temporal semantics extraction",
      "semantic dynamics",
      "cohesive representations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Temporal Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Temporal Text-attributed Graphs",
      "resolved_canonical": "Temporal Text-attributed Graphs",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.92,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Semantic-structural Co-encoder",
      "resolved_canonical": "Semantic-structural Co-encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Unifying Text Semantics and Graph Structures for Temporal Text-attributed Graphs with Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2503.14411.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2503.14411](https://arxiv.org/abs/2503.14411)

## 🔗 유사한 논문
- [[2025-09-24/Global-Recent Semantic Reasoning on Dynamic Text-Attributed Graphs with Large Language Models_20250924|Global-Recent Semantic Reasoning on Dynamic Text-Attributed Graphs with Large Language Models]] (84.7% similar)
- [[2025-09-23/Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning_20250923|Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning]] (81.7% similar)
- [[2025-09-23/CGTGait_ Collaborative Graph and Transformer for Gait Emotion Recognition_20250923|CGTGait: Collaborative Graph and Transformer for Gait Emotion Recognition]] (81.4% similar)
- [[2025-09-23/LTA-thinker_ Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning_20250923|LTA-thinker: Latent Thought-Augmented Training Framework for Large Language Models on Complex Reasoning]] (81.4% similar)
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Temporal Text-attributed Graphs|Temporal Text-attributed Graphs]], [[keywords/Semantic-structural Co-encoder|Semantic-structural Co-encoder]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.14411v3 Announce Type: replace-cross 
Abstract: Temporal graph neural networks (TGNNs) have shown remarkable performance in temporal graph modeling. However, real-world temporal graphs often possess rich textual information, giving rise to temporal text-attributed graphs (TTAGs). Such combination of dynamic text semantics and evolving graph structures introduces heightened complexity. Existing TGNNs embed texts statically and rely heavily on encoding mechanisms that biasedly prioritize structural information, overlooking the temporal evolution of text semantics and the essential interplay between semantics and structures for synergistic reinforcement. To tackle these issues, we present \textbf{CROSS}, a flexible framework that seamlessly extends existing TGNNs for TTAG modeling. CROSS is designed by decomposing the TTAG modeling process into two phases: (i) temporal semantics extraction; and (ii) semantic-structural information unification. The key idea is to advance the large language models (LLMs) to dynamically extract the temporal semantics in text space and then generate cohesive representations unifying both semantics and structures. Specifically, we propose a Temporal Semantics Extractor in the CROSS framework, which empowers LLMs to offer the temporal semantic understanding of node's evolving contexts of textual neighborhoods, facilitating semantic dynamics. Subsequently, we introduce the Semantic-structural Co-encoder, which collaborates with the above Extractor for synthesizing illuminating representations by jointly considering both semantic and structural information while encouraging their mutual reinforcement. Extensive experiments show that CROSS achieves state-of-the-art results on four public datasets and one industrial dataset, with 24.7% absolute MRR gain on average in temporal link prediction and 3.7% AUC gain in node classification of industrial application.

## 📝 요약

이 논문은 시간적 텍스트 속성 그래프(TTAG)를 효과적으로 모델링하기 위한 프레임워크인 CROSS를 제안합니다. 기존의 시간적 그래프 신경망(TGNN)은 텍스트 정보를 정적으로 처리하고 구조적 정보에 치우치는 한계를 가집니다. CROSS는 이러한 문제를 해결하기 위해 TTAG 모델링을 두 단계로 나눕니다: (i) 시간적 의미 추출, (ii) 의미-구조 정보 통합. CROSS는 대형 언어 모델(LLM)을 활용하여 텍스트의 시간적 의미를 동적으로 추출하고, 의미와 구조를 통합한 표현을 생성합니다. 제안된 Temporal Semantics Extractor는 노드의 텍스트적 맥락을 이해하고, Semantic-structural Co-encoder는 의미와 구조 정보를 결합하여 시너지 효과를 높입니다. 실험 결과, CROSS는 여러 데이터셋에서 최첨단 성능을 보였으며, 시간적 링크 예측에서 평균 24.7% MRR 향상, 산업 응용의 노드 분류에서 3.7% AUC 향상을 달성했습니다.

## 🎯 주요 포인트

- 1. CROSS는 기존의 TGNNs를 TTAG 모델링으로 확장하는 유연한 프레임워크로, 두 단계로 TTAG 모델링을 수행합니다: (i) 시간적 의미 추출, (ii) 의미-구조 정보 통합.
- 2. CROSS는 대형 언어 모델(LLMs)을 활용하여 텍스트 공간에서 시간적 의미를 동적으로 추출하고, 의미와 구조를 통합한 일관된 표현을 생성합니다.
- 3. Temporal Semantics Extractor는 LLMs가 텍스트 주변의 노드의 변화하는 맥락에 대한 시간적 의미 이해를 제공하여 의미 역학을 촉진합니다.
- 4. Semantic-structural Co-encoder는 의미와 구조 정보를 공동으로 고려하여 통합된 표현을 합성하고, 상호 강화 효과를 장려합니다.
- 5. CROSS는 네 개의 공개 데이터셋과 하나의 산업 데이터셋에서 최첨단 결과를 달성하며, 시간적 링크 예측에서 평균 24.7%의 MRR 절대 증가 및 산업 응용의 노드 분류에서 3.7%의 AUC 증가를 보였습니다.


---

*Generated on 2025-09-25 16:21:34*