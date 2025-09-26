---
keywords:
  - Neural Network
  - Gaussian Mixture Model
  - Wide Width Limit
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2507.22095
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:07:31.781351",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Gaussian Mixture Model",
    "Wide Width Limit"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.72,
    "Gaussian Mixture Model": 0.75,
    "Wide Width Limit": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Bayesian Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "BNN"
        ],
        "category": "broad_technical",
        "rationale": "Bayesian Neural Networks are a subset of Neural Networks, which can be linked to broader discussions in Deep Learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Gaussian Mixture",
        "canonical": "Gaussian Mixture Model",
        "aliases": [
          "GMM"
        ],
        "category": "specific_connectable",
        "rationale": "Gaussian Mixture Models are a specific statistical method relevant to the paper's discussion on distributions.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "Wide Width Limit",
        "canonical": "Wide Width Limit",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The concept of Wide Width Limit is unique to this paper's approach to neural networks.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "posterior",
      "likelihood",
      "algorithm"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Bayesian Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Gaussian Mixture",
      "resolved_canonical": "Gaussian Mixture Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Wide Width Limit",
      "resolved_canonical": "Wide Width Limit",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Simulating Posterior Bayesian Neural Networks with Dependent Weights

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.22095.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2507.22095](https://arxiv.org/abs/2507.22095)

## 🔗 유사한 논문
- [[2025-09-23/Addressing the Inconsistency in Bayesian Deep Learning via Generalized Laplace Approximation_20250923|Addressing the Inconsistency in Bayesian Deep Learning via Generalized Laplace Approximation]] (83.4% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (79.1% similar)
- [[2025-09-23/Bio-Inspired Adaptive Neurons for Dynamic Weighting in Artificial Neural Networks_20250923|Bio-Inspired Adaptive Neurons for Dynamic Weighting in Artificial Neural Networks]] (79.0% similar)
- [[2025-09-22/Geometric Integration for Neural Control Variates_20250922|Geometric Integration for Neural Control Variates]] (79.0% similar)
- [[2025-09-22/Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows_20250922|Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Gaussian Mixture Model|Gaussian Mixture Model]]
**⚡ Unique Technical**: [[keywords/Wide Width Limit|Wide Width Limit]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.22095v2 Announce Type: replace-cross 
Abstract: In this paper we consider posterior Bayesian fully connected and feedforward deep neural networks with dependent weights. Particularly, if the likelihood is Gaussian, we identify the distribution of the wide width limit and provide an algorithm to sample from the network. In the shallow case we explicitly compute the distribution of the conditional output, proving that it is a Gaussian mixture. All the theoretical results are numerically validated.

## 📝 요약

이 논문에서는 의존적인 가중치를 가진 베이지안 후방 연결 및 피드포워드 심층 신경망을 다룹니다. 특히, 가능도가 가우시안일 경우, 넓은 폭의 한계 분포를 식별하고 네트워크에서 샘플링할 수 있는 알고리즘을 제공합니다. 얕은 신경망의 경우, 조건부 출력의 분포를 명시적으로 계산하여 가우시안 혼합임을 증명합니다. 모든 이론적 결과는 수치적으로 검증되었습니다.

## 🎯 주요 포인트

- 1. 후행 베이지안 완전 연결 및 순방향 심층 신경망에서 종속 가중치를 고려합니다.
- 2. 가능도가 가우시안일 경우, 넓은 폭 한계의 분포를 식별하고 네트워크에서 샘플링하는 알고리즘을 제공합니다.
- 3. 얕은 경우 조건부 출력의 분포를 명시적으로 계산하여 가우시안 혼합임을 증명합니다.
- 4. 모든 이론적 결과는 수치적으로 검증되었습니다.


---

*Generated on 2025-09-24 03:07:31*