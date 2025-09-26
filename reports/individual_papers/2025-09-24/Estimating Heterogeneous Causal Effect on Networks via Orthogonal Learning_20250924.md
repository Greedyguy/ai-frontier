<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:10:23.595068",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Attention Mechanism",
    "Neyman Orthogonalization",
    "Spillover Effects"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Attention Mechanism": 0.82,
    "Neyman Orthogonalization": 0.79,
    "Spillover Effects": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are central to the method proposed in the paper, offering strong connectivity with existing research on network topology.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Attention-based Interference Model",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Attention Model"
        ],
        "category": "specific_connectable",
        "rationale": "The attention-based interference model is a novel application of attention mechanisms, linking to broader research on attention in neural networks.",
        "novelty_score": 0.58,
        "connectivity_score": 0.87,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Neyman Orthogonalization",
        "canonical": "Neyman Orthogonalization",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Neyman Orthogonalization is a unique statistical technique used to ensure robustness in causal effect estimation, providing a novel link to statistical methods.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.83,
        "link_intent_score": 0.79
      },
      {
        "surface": "Spillover Effects",
        "canonical": "Spillover Effects",
        "aliases": [
          "Indirect Effects"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding spillover effects is crucial for causal inference in networks, connecting to various fields like epidemiology and economics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.81,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "causal effects",
      "networks",
      "interference"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Attention-based Interference Model",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.87,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Neyman Orthogonalization",
      "resolved_canonical": "Neyman Orthogonalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.83,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Spillover Effects",
      "resolved_canonical": "Spillover Effects",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.81,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Estimating Heterogeneous Causal Effect on Networks via Orthogonal Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18484.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18484](https://arxiv.org/abs/2509.18484)

## 🔗 유사한 논문
- [[2025-09-23/Entropic Causal Inference_ Graph Identifiability_20250923|Entropic Causal Inference: Graph Identifiability]] (82.0% similar)
- [[2025-09-22/Interpretable Network-assisted Random Forest+_20250922|Interpretable Network-assisted Random Forest+]] (81.4% similar)
- [[2025-09-22/Decomposing Interventional Causality into Synergistic, Redundant, and Unique Components_20250922|Decomposing Interventional Causality into Synergistic, Redundant, and Unique Components]] (81.2% similar)
- [[2025-09-22/Adversarial generalization of unfolding (model-based) networks_20250922|Adversarial generalization of unfolding (model-based) networks]] (80.4% similar)
- [[2025-09-22/Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data_20250922|Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Spillover Effects|Spillover Effects]]
**⚡ Unique Technical**: [[keywords/Neyman Orthogonalization|Neyman Orthogonalization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18484v1 Announce Type: cross 
Abstract: Estimating causal effects on networks is important for both scientific research and practical applications. Unlike traditional settings that assume the Stable Unit Treatment Value Assumption (SUTVA), interference allows an intervention/treatment on one unit to affect the outcomes of others. Understanding both direct and spillover effects is critical in fields such as epidemiology, political science, and economics. Causal inference on networks faces two main challenges. First, causal effects are typically heterogeneous, varying with unit features and local network structure. Second, connected units often exhibit dependence due to network homophily, creating confounding between structural correlations and causal effects. In this paper, we propose a two-stage method to estimate heterogeneous direct and spillover effects on networks. The first stage uses graph neural networks to estimate nuisance components that depend on the complex network topology. In the second stage, we adjust for network confounding using these estimates and infer causal effects through a novel attention-based interference model. Our approach balances expressiveness and interpretability, enabling downstream tasks such as identifying influential neighborhoods and recovering the sign of spillover effects. We integrate the two stages using Neyman orthogonalization and cross-fitting, which ensures that errors from nuisance estimation contribute only at higher order. As a result, our causal effect estimates are robust to bias and misspecification in modeling causal effects under network dependencies.

## 📝 요약

이 논문은 네트워크 상에서의 인과 효과 추정을 다루며, 전통적인 SUTVA 가정 대신 간섭을 고려합니다. 이는 역학, 정치학, 경제학 등에서 직접 및 파급 효과를 이해하는 데 중요합니다. 네트워크 인과 추론의 주요 도전은 이질적인 인과 효과와 네트워크 동질성으로 인한 의존성입니다. 저자들은 두 단계 방법론을 제안하여, 첫 번째 단계에서 그래프 신경망을 사용해 복잡한 네트워크 구조에 의존하는 성분을 추정하고, 두 번째 단계에서 네트워크 혼란을 조정하여 인과 효과를 추론합니다. 이 방법은 표현력과 해석 가능성을 균형 있게 유지하며, 영향력 있는 이웃 식별 및 파급 효과의 부호 복구 등의 작업을 지원합니다. Neyman 직교화와 교차 적합을 통해 추정 오류를 최소화하여 네트워크 의존성 하에서도 편향에 강한 인과 효과 추정을 제공합니다.

## 🎯 주요 포인트

- 1. 네트워크에서의 인과 효과 추정은 과학 연구와 실용적 응용 모두에서 중요하다.
- 2. 네트워크에서의 인과 추론은 단위의 특성과 지역 네트워크 구조에 따라 이질적인 인과 효과를 보이는 것이 주요 도전 과제 중 하나이다.
- 3. 제안된 방법은 그래프 신경망을 사용하여 복잡한 네트워크 구조에 의존하는 불필요한 요소를 추정하고, 주의 기반 간섭 모델을 통해 인과 효과를 추론한다.
- 4. 네트워크 상의 인과 효과 추정에서 편향과 잘못된 명세에 강건한 결과를 제공하기 위해 Neyman 직교화와 교차 적합을 통합하였다.
- 5. 제안된 접근법은 표현력과 해석 가능성을 균형 있게 유지하여, 영향력 있는 이웃 식별 및 스필오버 효과의 부호 복구와 같은 후속 작업을 가능하게 한다.


---

*Generated on 2025-09-24 15:10:23*