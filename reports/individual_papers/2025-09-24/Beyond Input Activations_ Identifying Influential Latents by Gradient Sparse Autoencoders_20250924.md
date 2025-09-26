<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:33:43.139831",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Sparse Autoencoder",
    "Gradient Sparse Autoencoder",
    "Large Language Model",
    "Causal Influence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Sparse Autoencoder": 0.75,
    "Gradient Sparse Autoencoder": 0.8,
    "Large Language Model": 0.7,
    "Causal Influence": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Sparse Autoencoders",
        "canonical": "Sparse Autoencoder",
        "aliases": [
          "SAE"
        ],
        "category": "unique_technical",
        "rationale": "Sparse Autoencoders are central to the paper's methodology and offer a unique perspective on model interpretation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Gradient Sparse Autoencoder",
        "canonical": "Gradient Sparse Autoencoder",
        "aliases": [
          "GradSAE"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method for identifying influential latents, crucial for understanding the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are the primary context in which the paper's methods are applied.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Causal Influence",
        "canonical": "Causal Influence",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Understanding causal influence is key to the paper's exploration of latent feature impact.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
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
      "candidate_surface": "Sparse Autoencoders",
      "resolved_canonical": "Sparse Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Gradient Sparse Autoencoder",
      "resolved_canonical": "Gradient Sparse Autoencoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Causal Influence",
      "resolved_canonical": "Causal Influence",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Beyond Input Activations: Identifying Influential Latents by Gradient Sparse Autoencoders

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.08080.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2505.08080](https://arxiv.org/abs/2505.08080)

## 🔗 유사한 논문
- [[2025-09-24/A Survey on Sparse Autoencoders_ Interpreting the Internal Mechanisms of Large Language Models_20250924|A Survey on Sparse Autoencoders: Interpreting the Internal Mechanisms of Large Language Models]] (88.4% similar)
- [[2025-09-23/Group-SAE_ Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups_20250923|Group-SAE: Efficient Training of Sparse Autoencoders for Large Language Models via Layer Groups]] (85.0% similar)
- [[2025-09-24/Safe-SAIL_ Towards a Fine-grained Safety Landscape of Large Language Models via Sparse Autoencoder Interpretation Framework_20250924|Safe-SAIL: Towards a Fine-grained Safety Landscape of Large Language Models via Sparse Autoencoder Interpretation Framework]] (84.1% similar)
- [[2025-09-24/Amortized Latent Steering_ Low-Cost Alternative to Test-Time Optimization_20250924|Amortized Latent Steering: Low-Cost Alternative to Test-Time Optimization]] (80.8% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box: Interpretable LLMs via Semantic Resonance Architecture]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Causal Influence|Causal Influence]]
**⚡ Unique Technical**: [[keywords/Sparse Autoencoder|Sparse Autoencoder]], [[keywords/Gradient Sparse Autoencoder|Gradient Sparse Autoencoder]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.08080v2 Announce Type: replace-cross 
Abstract: Sparse Autoencoders (SAEs) have recently emerged as powerful tools for interpreting and steering the internal representations of large language models (LLMs). However, conventional approaches to analyzing SAEs typically rely solely on input-side activations, without considering the causal influence between each latent feature and the model's output. This work is built on two key hypotheses: (1) activated latents do not contribute equally to the construction of the model's output, and (2) only latents with high causal influence are effective for model steering. To validate these hypotheses, we propose Gradient Sparse Autoencoder (GradSAE), a simple yet effective method that identifies the most influential latents by incorporating output-side gradient information.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 내부 표현을 해석하고 조정하는 데 사용되는 희소 오토인코더(SAE)의 한계를 극복하기 위해 Gradient Sparse Autoencoder(GradSAE)를 제안합니다. 기존 SAE 분석은 입력 활성화에만 의존했지만, 이 연구는 잠재 특징과 모델 출력 간의 인과적 영향을 고려합니다. 주요 기여는 (1) 활성화된 잠재 특징들이 모델 출력에 동일하게 기여하지 않으며, (2) 높은 인과적 영향을 가진 잠재 특징만이 모델 조정에 효과적이라는 가설을 검증한 것입니다. GradSAE는 출력 측의 그래디언트 정보를 활용하여 가장 영향력 있는 잠재 특징을 식별하는 간단하면서도 효과적인 방법론을 제공합니다.

## 🎯 주요 포인트

- 1. 희소 오토인코더(SAE)는 대형 언어 모델(LLM)의 내부 표현을 해석하고 조정하는 데 유용한 도구로 부상하고 있다.
- 2. 기존 SAE 분석 방법은 입력 측 활성화에만 의존하며, 각 잠재 특징과 모델 출력 간의 인과적 영향을 고려하지 않는다.
- 3. 본 연구는 활성화된 잠재 변수들이 모델 출력 구성에 동일하게 기여하지 않는다는 가설을 제시한다.
- 4. 높은 인과적 영향을 가진 잠재 변수만이 모델 조정에 효과적이라는 가설을 제시한다.
- 5. GradSAE는 출력 측 기울기 정보를 통합하여 가장 영향력 있는 잠재 변수를 식별하는 간단하면서도 효과적인 방법이다.


---

*Generated on 2025-09-24 14:33:43*