---
keywords:
  - Quasi-Hyperbolic Momentum
  - Increasing Batch Size
  - Neural Network
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2506.23544
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:09:38.408680",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Quasi-Hyperbolic Momentum",
    "Increasing Batch Size",
    "Neural Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Quasi-Hyperbolic Momentum": 0.78,
    "Increasing Batch Size": 0.72,
    "Neural Network": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Quasi-Hyperbolic Momentum",
        "canonical": "Quasi-Hyperbolic Momentum",
        "aliases": [
          "QHM"
        ],
        "category": "unique_technical",
        "rationale": "Quasi-Hyperbolic Momentum is a specific algorithm that generalizes various momentum methods, providing a unique perspective on optimization strategies.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Increasing Batch Size",
        "canonical": "Increasing Batch Size",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Increasing batch size is a key strategy discussed in the paper for achieving convergence without decaying the learning rate.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "NN",
          "Deep Neural Networks"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are central to the discussion of optimization methods in the paper, linking to broader topics in machine learning.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "momentum methods",
      "stochastic gradient descent",
      "convex objective functions"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Quasi-Hyperbolic Momentum",
      "resolved_canonical": "Quasi-Hyperbolic Momentum",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Increasing Batch Size",
      "resolved_canonical": "Increasing Batch Size",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Both Asymptotic and Non-Asymptotic Convergence of Quasi-Hyperbolic Momentum using Increasing Batch Size

**Korean Title:** 점진적 배치 크기를 사용한 준-쌍곡선 모멘텀의 점근적 및 비점근적 수렴

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.23544.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2506.23544](https://arxiv.org/abs/2506.23544)

## 🔗 유사한 논문
- [[2025-09-22/Faster Convergence of Riemannian Stochastic Gradient Descent with Increasing Batch Size_20250922|Faster Convergence of Riemannian Stochastic Gradient Descent with Increasing Batch Size]] (84.1% similar)
- [[2025-09-22/DIVEBATCH_ Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation_20250922|DIVEBATCH: Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation]] (83.0% similar)
- [[2025-09-22/Flavors of Margin_ Implicit Bias of Steepest Descent in Homogeneous Neural Networks_20250922|Flavors of Margin: Implicit Bias of Steepest Descent in Homogeneous Neural Networks]] (82.2% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (81.5% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Quasi-Hyperbolic Momentum|Quasi-Hyperbolic Momentum]], [[keywords/Increasing Batch Size|Increasing Batch Size]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.23544v3 Announce Type: replace 
Abstract: Momentum methods were originally introduced for their superiority to stochastic gradient descent (SGD) in deterministic settings with convex objective functions. However, despite their widespread application to deep neural networks -- a representative case of stochastic nonconvex optimization -- the theoretical justification for their effectiveness in such settings remains limited. Quasi-hyperbolic momentum (QHM) is an algorithm that generalizes various momentum methods and has been studied to better understand the class of momentum-based algorithms as a whole. In this paper, we provide both asymptotic and non-asymptotic convergence results for mini-batch QHM with an increasing batch size. We show that achieving asymptotic convergence requires either a decaying learning rate or an increasing batch size. Since a decaying learning rate adversely affects non-asymptotic convergence, we demonstrate that using mini-batch QHM with an increasing batch size -- without decaying the learning rate -- can be a more effective strategy. Our experiments show that even a finite increase in batch size can provide benefits for training neural networks.

## 🔍 Abstract (한글 번역)

arXiv:2506.23544v3 발표 유형: 교체  
초록: 모멘텀 방법은 원래 볼록 목적 함수가 있는 결정론적 환경에서 확률적 경사 하강법(SGD)보다 우수하다는 이유로 도입되었습니다. 그러나 심층 신경망에 대한 광범위한 적용에도 불구하고, 이는 확률적 비볼록 최적화의 대표적인 사례로, 이러한 환경에서의 효과에 대한 이론적 정당성은 여전히 제한적입니다. 준-쌍곡선 모멘텀(QHM)은 다양한 모멘텀 방법을 일반화한 알고리즘으로, 모멘텀 기반 알고리즘 전체 클래스를 더 잘 이해하기 위해 연구되었습니다. 본 논문에서는 증가하는 배치 크기를 사용하는 미니배치 QHM에 대한 점근적 및 비점근적 수렴 결과를 제공합니다. 점근적 수렴을 달성하려면 학습률 감소 또는 배치 크기 증가가 필요하다는 것을 보여줍니다. 학습률 감소는 비점근적 수렴에 부정적인 영향을 미치기 때문에, 학습률을 감소시키지 않고 배치 크기를 증가시키는 미니배치 QHM을 사용하는 것이 더 효과적인 전략이 될 수 있음을 입증합니다. 우리의 실험은 배치 크기의 유한한 증가만으로도 신경망 훈련에 이점을 제공할 수 있음을 보여줍니다.

## 📝 요약

이 논문은 모멘텀 방법의 일반화된 알고리즘인 준-쌍곡선 모멘텀(QHM)을 연구하여 모멘텀 기반 알고리즘의 이해를 돕고자 합니다. 미니배치 QHM의 수렴 결과를 제시하며, 점진적인 배치 크기 증가가 비감소 학습률과 결합하여 비대칭 수렴을 달성할 수 있음을 보여줍니다. 이는 학습률 감소가 비대칭 수렴에 부정적 영향을 미치는 것을 고려할 때, 배치 크기 증가가 더 효과적인 전략임을 시사합니다. 실험 결과, 유한한 배치 크기 증가만으로도 신경망 훈련에 이점이 있음을 확인했습니다.

## 🎯 주요 포인트

- 1. 모멘텀 방법은 원래 확정적 환경에서의 우수성 때문에 도입되었으나, 비확정적 비볼록 최적화인 심층 신경망에서의 이론적 근거는 제한적이다.
- 2. 준-쌍곡선 모멘텀(QHM)은 다양한 모멘텀 방법을 일반화한 알고리즘으로, 모멘텀 기반 알고리즘 전체를 이해하기 위해 연구되었다.
- 3. 본 논문에서는 증가하는 배치 크기를 사용하는 미니배치 QHM의 점근적 및 비점근적 수렴 결과를 제시한다.
- 4. 점근적 수렴을 달성하기 위해서는 학습률 감소 또는 배치 크기 증가가 필요하며, 학습률 감소는 비점근적 수렴에 부정적 영향을 미친다.
- 5. 실험 결과, 배치 크기의 유한한 증가만으로도 신경망 훈련에 이점이 있음을 보여준다.


---

*Generated on 2025-09-23 11:09:38*