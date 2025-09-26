---
keywords:
  - Conditional Diffusion Models
  - Compositional Generalization
  - Local Conditional Scores
  - Feature-Space Compositionality
  - CLEVR Dataset
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16447
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:36:16.016594",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Conditional Diffusion Models",
    "Compositional Generalization",
    "Local Conditional Scores",
    "Feature-Space Compositionality",
    "CLEVR Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Conditional Diffusion Models": 0.78,
    "Compositional Generalization": 0.81,
    "Local Conditional Scores": 0.77,
    "Feature-Space Compositionality": 0.74,
    "CLEVR Dataset": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Conditional Diffusion Models",
        "canonical": "Conditional Diffusion Models",
        "aliases": [
          "Conditional Diffusion"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on compositional generalization in diffusion models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Compositional Generalization",
        "canonical": "Compositional Generalization",
        "aliases": [
          "Compositionality"
        ],
        "category": "specific_connectable",
        "rationale": "Key concept for linking studies on generalization capabilities in machine learning models.",
        "novelty_score": 0.68,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.81
      },
      {
        "surface": "Local Conditional Scores",
        "canonical": "Local Conditional Scores",
        "aliases": [
          "Local Scores"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel mechanism for understanding compositional generalization in diffusion models.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      },
      {
        "surface": "Feature-Space Compositionality",
        "canonical": "Feature-Space Compositionality",
        "aliases": [
          "Feature Compositionality"
        ],
        "category": "unique_technical",
        "rationale": "Explores a new dimension of compositionality, relevant for linking to feature analysis in models.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.74
      },
      {
        "surface": "CLEVR Setting",
        "canonical": "CLEVR Dataset",
        "aliases": [
          "CLEVR"
        ],
        "category": "specific_connectable",
        "rationale": "Frequently used benchmark for testing generalization in visual models, aiding in dataset-related links.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "length generalization",
      "causal intervention"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Conditional Diffusion Models",
      "resolved_canonical": "Conditional Diffusion Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Compositional Generalization",
      "resolved_canonical": "Compositional Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Local Conditional Scores",
      "resolved_canonical": "Local Conditional Scores",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Feature-Space Compositionality",
      "resolved_canonical": "Feature-Space Compositionality",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "CLEVR Setting",
      "resolved_canonical": "CLEVR Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Local Mechanisms of Compositional Generalization in Conditional Diffusion

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16447.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16447](https://arxiv.org/abs/2509.16447)

## 🔗 유사한 논문
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (80.1% similar)
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (79.6% similar)
- [[2025-09-23/Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements_20250923|Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements]] (79.5% similar)
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (79.3% similar)
- [[2025-09-17/Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures_20250917|Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Compositional Generalization|Compositional Generalization]], [[keywords/CLEVR Dataset|CLEVR Dataset]]
**⚡ Unique Technical**: [[keywords/Conditional Diffusion Models|Conditional Diffusion Models]], [[keywords/Local Conditional Scores|Local Conditional Scores]], [[keywords/Feature-Space Compositionality|Feature-Space Compositionality]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16447v1 Announce Type: new 
Abstract: Conditional diffusion models appear capable of compositional generalization, i.e., generating convincing samples for out-of-distribution combinations of conditioners, but the mechanisms underlying this ability remain unclear. To make this concrete, we study length generalization, the ability to generate images with more objects than seen during training. In a controlled CLEVR setting (Johnson et al., 2017), we find that length generalization is achievable in some cases but not others, suggesting that models only sometimes learn the underlying compositional structure. We then investigate locality as a structural mechanism for compositional generalization. Prior works proposed score locality as a mechanism for creativity in unconditional diffusion models (Kamb & Ganguli, 2024; Niedoba et al., 2024), but did not address flexible conditioning or compositional generalization. In this paper, we prove an exact equivalence between a specific compositional structure ("conditional projective composition") (Bradley et al., 2025) and scores with sparse dependencies on both pixels and conditioners ("local conditional scores"). This theory also extends to feature-space compositionality. We validate our theory empirically: CLEVR models that succeed at length generalization exhibit local conditional scores, while those that fail do not. Furthermore, we show that a causal intervention explicitly enforcing local conditional scores restores length generalization in a previously failing model. Finally, we investigate feature-space compositionality in color-conditioned CLEVR, and find preliminary evidence of compositional structure in SDXL.

## 📝 요약

이 논문은 조건부 확산 모델의 조합적 일반화 능력, 특히 훈련 중 보지 못한 객체 수를 생성하는 능력인 '길이 일반화'를 연구합니다. CLEVR 환경에서 실험한 결과, 일부 모델은 길이 일반화를 성공적으로 수행했으나, 다른 모델은 그렇지 못했습니다. 이는 모델이 조합적 구조를 항상 학습하는 것은 아님을 시사합니다. 논문은 '지역적 조건 점수'라는 구조적 메커니즘이 조합적 일반화에 기여할 수 있음을 증명하고, 이를 통해 길이 일반화에 성공한 모델은 이러한 점수를 보유하고 있음을 실험적으로 검증했습니다. 또한, 인과적 개입을 통해 실패한 모델에서도 길이 일반화를 복원할 수 있음을 보여주었습니다. 마지막으로, 색상 조건이 있는 CLEVR에서의 특징 공간 조합성을 조사하여 초기 증거를 발견했습니다.

## 🎯 주요 포인트

- 1. 조건부 확산 모델은 조합적 일반화 능력을 보이며, 훈련 시 보지 못한 조합의 샘플을 생성할 수 있지만, 그 메커니즘은 명확하지 않다.
- 2. CLEVR 환경에서 길이 일반화를 연구한 결과, 모델이 조합적 구조를 학습하는 경우와 그렇지 않은 경우가 있음을 발견했다.
- 3. 본 연구는 조합적 일반화를 위한 구조적 메커니즘으로서의 지역성을 조사하고, 특정 조합적 구조와 지역적 조건 점수 간의 정확한 등가성을 증명했다.
- 4. 길이 일반화에 성공한 CLEVR 모델은 지역적 조건 점수를 보였으며, 실패한 모델은 그렇지 않았다.
- 5. 색상 조건이 있는 CLEVR에서의 특징 공간 조합성을 조사한 결과, SDXL에서 조합적 구조의 초기 증거를 발견했다.


---

*Generated on 2025-09-24 01:36:16*