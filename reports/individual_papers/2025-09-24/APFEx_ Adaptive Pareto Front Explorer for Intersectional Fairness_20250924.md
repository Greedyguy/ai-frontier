<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:29:23.402535",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Intersectional Fairness",
    "Pareto Front",
    "Adaptive Multi-Objective Optimizer",
    "Differentiable Intersectional Fairness Metrics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Intersectional Fairness": 0.78,
    "Pareto Front": 0.75,
    "Adaptive Multi-Objective Optimizer": 0.72,
    "Differentiable Intersectional Fairness Metrics": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "intersectional fairness",
        "canonical": "Intersectional Fairness",
        "aliases": [
          "intersectional bias mitigation"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a novel approach to fairness in ML, focusing on multiple intersecting attributes.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Pareto Front",
        "canonical": "Pareto Front",
        "aliases": [
          "Pareto frontier"
        ],
        "category": "specific_connectable",
        "rationale": "Pareto Front is a key concept in optimization, relevant for linking with multi-objective optimization literature.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "adaptive multi-objective optimizer",
        "canonical": "Adaptive Multi-Objective Optimizer",
        "aliases": [
          "adaptive optimizer"
        ],
        "category": "unique_technical",
        "rationale": "This optimizer is central to the proposed method, highlighting its adaptability in fairness-accuracy trade-offs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "differentiable intersectional fairness metrics",
        "canonical": "Differentiable Intersectional Fairness Metrics",
        "aliases": [
          "differentiable fairness metrics"
        ],
        "category": "unique_technical",
        "rationale": "These metrics are crucial for enabling gradient-based optimization in the context of fairness.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "fairness violations",
      "real-world datasets"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "intersectional fairness",
      "resolved_canonical": "Intersectional Fairness",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Pareto Front",
      "resolved_canonical": "Pareto Front",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "adaptive multi-objective optimizer",
      "resolved_canonical": "Adaptive Multi-Objective Optimizer",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "differentiable intersectional fairness metrics",
      "resolved_canonical": "Differentiable Intersectional Fairness Metrics",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# APFEx: Adaptive Pareto Front Explorer for Intersectional Fairness

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.13908.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.13908](https://arxiv.org/abs/2509.13908)

## 🔗 유사한 논문
- [[2025-09-17/APFEx_ Adaptive Pareto Front Explorer for Intersectional Fairness_20250917|APFEx: Adaptive Pareto Front Explorer for Intersectional Fairness]] (98.4% similar)
- [[2025-09-19/CausalPre_ Scalable and Effective Data Pre-processing for Causal Fairness_20250919|CausalPre: Scalable and Effective Data Pre-processing for Causal Fairness]] (83.2% similar)
- [[2025-09-22/Algorithmic Fairness_ Not a Purely Technical but Socio-Technical Property_20250922|Algorithmic Fairness: Not a Purely Technical but Socio-Technical Property]] (83.2% similar)
- [[2025-09-17/ParaAegis_ Parallel Protection for Flexible Privacy-preserved Federated Learning_20250917|ParaAegis: Parallel Protection for Flexible Privacy-preserved Federated Learning]] (82.6% similar)
- [[2025-09-23/Regularizing Extrapolation in Causal Inference_20250923|Regularizing Extrapolation in Causal Inference]] (82.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Pareto Front|Pareto Front]]
**⚡ Unique Technical**: [[keywords/Intersectional Fairness|Intersectional Fairness]], [[keywords/Adaptive Multi-Objective Optimizer|Adaptive Multi-Objective Optimizer]], [[keywords/Differentiable Intersectional Fairness Metrics|Differentiable Intersectional Fairness Metrics]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13908v2 Announce Type: replace 
Abstract: Ensuring fairness in machine learning models is critical, especially when biases compound across intersecting protected attributes like race, gender, and age. While existing methods address fairness for single attributes, they fail to capture the nuanced, multiplicative biases faced by intersectional subgroups. We introduce Adaptive Pareto Front Explorer (APFEx), the first framework to explicitly model intersectional fairness as a joint optimization problem over the Cartesian product of sensitive attributes. APFEx combines three key innovations- (1) an adaptive multi-objective optimizer that dynamically switches between Pareto cone projection, gradient weighting, and exploration strategies to navigate fairness-accuracy trade-offs, (2) differentiable intersectional fairness metrics enabling gradient-based optimization of non-smooth subgroup disparities, and (3) theoretical guarantees of convergence to Pareto-optimal solutions. Experiments on four real-world datasets demonstrate APFEx's superiority, reducing fairness violations while maintaining competitive accuracy. Our work bridges a critical gap in fair ML, providing a scalable, model-agnostic solution for intersectional fairness.

## 📝 요약

이 논문은 머신러닝 모델에서 교차 보호 속성(예: 인종, 성별, 나이) 간의 복합적인 편향 문제를 해결하기 위해 APFEx라는 새로운 프레임워크를 제안합니다. APFEx는 교차공정성을 민감한 속성의 데카르트 곱에 대한 공동 최적화 문제로 모델링하며, 적응형 다중 목표 최적화 기법을 통해 공정성과 정확성 간의 균형을 동적으로 조절합니다. 또한, 미분 가능한 교차공정성 지표를 사용하여 비매끄러운 하위 그룹 불균형을 최적화하고, 이론적으로 파레토 최적 솔루션으로의 수렴을 보장합니다. 실험 결과, APFEx는 네 개의 실제 데이터셋에서 공정성 위반을 줄이면서도 경쟁력 있는 정확성을 유지하는 데 우수한 성능을 보였습니다. 이 연구는 교차공정성을 위한 확장 가능하고 모델에 구애받지 않는 솔루션을 제공하여 공정한 머신러닝 분야의 중요한 격차를 해소합니다.

## 🎯 주요 포인트

- 1. 기계 학습 모델에서 인종, 성별, 연령과 같은 교차 보호 속성에 대한 공정성을 보장하는 것이 중요합니다.
- 2. 기존 방법들은 단일 속성에 대한 공정성만을 다루며, 교차적 하위 그룹이 직면하는 복합적 편향을 포착하지 못합니다.
- 3. APFEx는 민감한 속성의 데카르트 곱에 대한 공동 최적화 문제로 교차적 공정성을 명시적으로 모델링하는 최초의 프레임워크입니다.
- 4. APFEx는 적응형 다목적 최적화 기법, 미분 가능한 교차적 공정성 지표, 그리고 파레토 최적 솔루션으로의 수렴에 대한 이론적 보장을 결합합니다.
- 5. 네 가지 실제 데이터셋에 대한 실험에서 APFEx는 공정성 위반을 줄이면서도 경쟁력 있는 정확성을 유지하는 우수성을 입증합니다.


---

*Generated on 2025-09-24 15:29:23*