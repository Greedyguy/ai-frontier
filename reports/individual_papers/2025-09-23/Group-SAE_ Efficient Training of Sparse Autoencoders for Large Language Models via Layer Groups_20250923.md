---
keywords:
  - Large Language Model
  - Sparse Autoencoder
  - Group-SAE
  - AMAD
  - Pythia Model Family
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2410.21508
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:41:09.209350",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Sparse Autoencoder",
    "Group-SAE",
    "AMAD",
    "Pythia Model Family"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.9,
    "Sparse Autoencoder": 0.88,
    "Group-SAE": 0.85,
    "AMAD": 0.8,
    "Pythia Model Family": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on improving training efficiency for these models.",
        "novelty_score": 0.2,
        "connectivity_score": 0.95,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Sparse Autoencoders",
        "canonical": "Sparse Autoencoder",
        "aliases": [
          "SAE",
          "Sparse Autoencoders"
        ],
        "category": "unique_technical",
        "rationale": "Key method discussed for improving layer representation understanding.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Group-SAE",
        "canonical": "Group-SAE",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Novel strategy introduced in the paper for efficient training.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Average Maximum Angular Distance",
        "canonical": "AMAD",
        "aliases": [
          "Average Maximum Angular Distance"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a new metric for optimizing layer grouping.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      },
      {
        "surface": "Pythia family",
        "canonical": "Pythia Model Family",
        "aliases": [
          "Pythia family"
        ],
        "category": "specific_connectable",
        "rationale": "Specific model family used in experiments, relevant for contextual linking.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.95,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Sparse Autoencoders",
      "resolved_canonical": "Sparse Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Group-SAE",
      "resolved_canonical": "Group-SAE",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Average Maximum Angular Distance",
      "resolved_canonical": "AMAD",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Pythia family",
      "resolved_canonical": "Pythia Model Family",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2410.21508.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2410.21508](https://arxiv.org/abs/2410.21508)

## 🔗 유사한 논문
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box: Interpretable LLMs via Semantic Resonance Architecture]] (82.0% similar)
- [[2025-09-23/LLMs as Layout Designers_ A Spatial Reasoning Perspective_20250923|LLMs as Layout Designers: A Spatial Reasoning Perspective]] (80.9% similar)
- [[2025-09-23/GALLa_ Graph Aligned Large Language Models for Improved Source Code Understanding_20250923|GALLa: Graph Aligned Large Language Models for Improved Source Code Understanding]] (80.6% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (80.4% similar)
- [[2025-09-23/Probabilistic Token Alignment for Large Language Model Fusion_20250923|Probabilistic Token Alignment for Large Language Model Fusion]] (80.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Pythia Model Family|Pythia Model Family]]
**⚡ Unique Technical**: [[keywords/Sparse Autoencoder|Sparse Autoencoder]], [[keywords/Group-SAE|Group-SAE]], [[keywords/AMAD|AMAD]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.21508v2 Announce Type: replace-cross 
Abstract: SAEs have recently been employed as a promising unsupervised approach for understanding the representations of layers of Large Language Models (LLMs). However, with the growth in model size and complexity, training SAEs is computationally intensive, as typically one SAE is trained for each model layer. To address such limitation, we propose \textit{Group-SAE}, a novel strategy to train SAEs. Our method considers the similarity of the residual stream representations between contiguous layers to group similar layers and train a single SAE per group. To balance the trade-off between efficiency and performance, we further introduce \textit{AMAD} (Average Maximum Angular Distance), an empirical metric that guides the selection of an optimal number of groups based on representational similarity across layers. Experiments on models from the Pythia family show that our approach significantly accelerates training with minimal impact on reconstruction quality and comparable downstream task performance and interpretability over baseline SAEs trained layer by layer. This method provides an efficient and scalable strategy for training SAEs in modern LLMs.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 각 층의 표현을 이해하기 위한 비지도 학습 접근법으로 사용되는 SAE의 효율성을 개선하기 위해 \textit{Group-SAE}라는 새로운 전략을 제안합니다. 기존에는 각 층마다 SAE를 훈련해야 했지만, 제안된 방법은 인접한 층 간의 잔여 스트림 표현의 유사성을 고려하여 유사한 층을 그룹화하고 그룹당 하나의 SAE를 훈련합니다. 또한, \textit{AMAD}라는 경험적 지표를 도입하여 층 간 표현 유사성을 기반으로 최적의 그룹 수를 선택합니다. Pythia 모델 실험 결과, 이 방법은 훈련 속도를 크게 향상시키면서도 재구성 품질과 다운스트림 작업 성능 및 해석 가능성에서 기존 SAE와 유사한 결과를 보였습니다. 이 방법은 현대 LLM에서 SAE 훈련의 효율적이고 확장 가능한 전략을 제공합니다.

## 🎯 주요 포인트

- 1. SAEs는 대규모 언어 모델(LLMs)의 층 표현을 이해하기 위한 유망한 비지도 학습 접근법으로 사용되고 있습니다.
- 2. 모델 크기와 복잡성이 증가함에 따라 각 층마다 SAE를 훈련하는 것은 계산적으로 부담이 큽니다.
- 3. Group-SAE는 유사한 층을 그룹화하여 그룹당 하나의 SAE를 훈련시키는 새로운 전략을 제안합니다.
- 4. AMAD(평균 최대 각도 거리)는 층 간 표현 유사성을 기반으로 최적의 그룹 수를 선택하는 경험적 지표입니다.
- 5. Pythia 모델군에 대한 실험 결과, 제안된 방법은 훈련 속도를 크게 높이면서도 재구성 품질과 다운스트림 작업 성능에 최소한의 영향을 미칩니다.


---

*Generated on 2025-09-24 00:41:09*