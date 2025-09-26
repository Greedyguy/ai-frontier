---
keywords:
  - Counterfactual Generation
  - Neural Causal Models
  - Domain Shift
  - Causal Graphs
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2502.12013
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:38:41.905143",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Counterfactual Generation",
    "Neural Causal Models",
    "Domain Shift",
    "Causal Graphs"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Counterfactual Generation": 0.78,
    "Neural Causal Models": 0.81,
    "Domain Shift": 0.77,
    "Causal Graphs": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "counterfactual generation",
        "canonical": "Counterfactual Generation",
        "aliases": [
          "counterfactual synthesis"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's methodology, providing a unique approach to generating counterfactuals under domain shift.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Neural Causal models",
        "canonical": "Neural Causal Models",
        "aliases": [
          "causal neural networks"
        ],
        "category": "specific_connectable",
        "rationale": "These models are crucial for integrating causal graphs and generating counterfactuals, linking to existing neural network concepts.",
        "novelty_score": 0.68,
        "connectivity_score": 0.82,
        "specificity_score": 0.79,
        "link_intent_score": 0.81
      },
      {
        "surface": "domain shift",
        "canonical": "Domain Shift",
        "aliases": [
          "domain adaptation"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding domain shift is essential for cross-domain learning, which is a key focus of the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "causal graphs",
        "canonical": "Causal Graphs",
        "aliases": [
          "causal diagrams"
        ],
        "category": "specific_connectable",
        "rationale": "Causal graphs are fundamental to the paper's approach, enabling the integration of domain-specific causal structures.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "cross-domain learning",
      "factual observations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "counterfactual generation",
      "resolved_canonical": "Counterfactual Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Neural Causal models",
      "resolved_canonical": "Neural Causal Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.82,
        "specificity": 0.79,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "domain shift",
      "resolved_canonical": "Domain Shift",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "causal graphs",
      "resolved_canonical": "Causal Graphs",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Unsupervised Structural-Counterfactual Generation under Domain Shift

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.12013.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2502.12013](https://arxiv.org/abs/2502.12013)

## 🔗 유사한 논문
- [[2025-09-22/Causal Fingerprints of AI Generative Models_20250922|Causal Fingerprints of AI Generative Models]] (84.1% similar)
- [[2025-09-19/Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (83.4% similar)
- [[2025-09-19/Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG: The Integration of Causal-Counterfactual Reasoning into RAG]] (82.9% similar)
- [[2025-09-23/Canonical Representations of Markovian Structural Causal Models_ A Framework for Counterfactual Reasoning_20250923|Canonical Representations of Markovian Structural Causal Models: A Framework for Counterfactual Reasoning]] (82.5% similar)
- [[2025-09-23/DoubleGen_ Debiased Generative Modeling of Counterfactuals_20250923|DoubleGen: Debiased Generative Modeling of Counterfactuals]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Neural Causal Models|Neural Causal Models]], [[keywords/Domain Shift|Domain Shift]], [[keywords/Causal Graphs|Causal Graphs]]
**⚡ Unique Technical**: [[keywords/Counterfactual Generation|Counterfactual Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.12013v3 Announce Type: replace 
Abstract: Motivated by the burgeoning interest in cross-domain learning, we present a novel generative modeling challenge: generating counterfactual samples in a target domain based on factual observations from a source domain. Our approach operates within an unsupervised paradigm devoid of parallel or joint datasets, relying exclusively on distinct observational samples and causal graphs for each domain. This setting presents challenges that surpass those of conventional counterfactual generation. Central to our methodology is the disambiguation of exogenous causes into effect-intrinsic and domain-intrinsic categories. This differentiation facilitates the integration of domain-specific causal graphs into a unified joint causal graph via shared effect-intrinsic exogenous variables. We propose leveraging Neural Causal models within this joint framework to enable accurate counterfactual generation under standard identifiability assumptions. Furthermore, we introduce a novel loss function that effectively segregates effect-intrinsic from domain-intrinsic variables during model training. Given a factual observation, our framework combines the posterior distribution of effect-intrinsic variables from the source domain with the prior distribution of domain-intrinsic variables from the target domain to synthesize the desired counterfactuals, adhering to Pearl's causal hierarchy. Intriguingly, when domain shifts are restricted to alterations in causal mechanisms without accompanying covariate shifts, our training regimen parallels the resolution of a conditional optimal transport problem. Empirical evaluations on a synthetic dataset show that our framework generates counterfactuals in the target domain that very closely resemble the ground truth.

## 📝 요약

이 논문은 서로 다른 도메인 간의 학습을 위한 새로운 생성 모델링 과제를 제안합니다. 소스 도메인의 사실적 관찰을 바탕으로 타겟 도메인에서 반사실적 샘플을 생성하는 방법론을 개발했습니다. 이 연구는 병렬 또는 공동 데이터셋 없이 각 도메인의 관찰 샘플과 인과 그래프만을 활용하는 비지도 학습 패러다임에서 작동합니다. 주요 기여는 외생적 원인을 효과 내재적 및 도메인 내재적으로 구분하여, 이를 통해 도메인별 인과 그래프를 통합된 공동 인과 그래프로 결합하는 것입니다. Neural Causal 모델을 활용하여 정확한 반사실적 생성이 가능하며, 새로운 손실 함수를 도입해 효과 내재적 변수와 도메인 내재적 변수를 효과적으로 분리합니다. 실험 결과, 제안된 프레임워크는 타겟 도메인에서 실제와 유사한 반사실적 샘플을 생성하는 데 성공했습니다.

## 🎯 주요 포인트

- 1. 본 연구는 소스 도메인의 사실적 관찰을 기반으로 타겟 도메인에서 반사실적 샘플을 생성하는 새로운 생성 모델링 과제를 제시합니다.
- 2. 제안된 방법은 병렬 또는 공동 데이터셋 없이 각 도메인의 개별 관찰 샘플과 인과 그래프만을 활용하는 비지도 학습 패러다임에서 작동합니다.
- 3. 효과 내재적 변수와 도메인 내재적 변수를 구분하여 도메인별 인과 그래프를 통합된 공동 인과 그래프로 결합합니다.
- 4. Neural Causal 모델을 활용하여 표준 식별 가능성 가정 하에 정확한 반사실적 생성이 가능하도록 합니다.
- 5. 제안된 손실 함수는 모델 훈련 중 효과 내재적 변수와 도메인 내재적 변수를 효과적으로 분리합니다.


---

*Generated on 2025-09-24 02:38:41*