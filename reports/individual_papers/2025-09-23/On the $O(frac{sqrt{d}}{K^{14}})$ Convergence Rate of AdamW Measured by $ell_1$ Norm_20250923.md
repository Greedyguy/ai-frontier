---
keywords:
  - AdamW Optimizer
  - Convergence Rate
  - Large Language Model
  - Stochastic Gradient Descent
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2505.11840
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:43:34.441659",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "AdamW Optimizer",
    "Convergence Rate",
    "Large Language Model",
    "Stochastic Gradient Descent"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "AdamW Optimizer": 0.78,
    "Convergence Rate": 0.7,
    "Large Language Model": 0.72,
    "Stochastic Gradient Descent": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "AdamW",
        "canonical": "AdamW Optimizer",
        "aliases": [
          "AdamW"
        ],
        "category": "unique_technical",
        "rationale": "AdamW is a specific optimization algorithm crucial for linking discussions on convergence rates in deep learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "convergence rate",
        "canonical": "Convergence Rate",
        "aliases": [
          "rate of convergence"
        ],
        "category": "broad_technical",
        "rationale": "Convergence rate is a fundamental concept in optimization and machine learning, linking to performance analysis.",
        "novelty_score": 0.45,
        "connectivity_score": 0.8,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large language models are central to modern AI research, facilitating links to various applications and studies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "SGD",
        "canonical": "Stochastic Gradient Descent",
        "aliases": [
          "SGD"
        ],
        "category": "specific_connectable",
        "rationale": "SGD is a widely used optimization method, providing a basis for comparing convergence rates with AdamW.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "iteration number",
      "model dimension",
      "Gaussian distribution"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "AdamW",
      "resolved_canonical": "AdamW Optimizer",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "convergence rate",
      "resolved_canonical": "Convergence Rate",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.8,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "large language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "SGD",
      "resolved_canonical": "Stochastic Gradient Descent",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# On the $O(\frac{\sqrt{d}}{K^{1/4}})$ Convergence Rate of AdamW Measured by $\ell_1$ Norm

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.11840.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2505.11840](https://arxiv.org/abs/2505.11840)

## 🔗 유사한 논문
- [[2025-09-22/Towards Communication-efficient Federated Learning via Sparse and Aligned Adaptive Optimization_20250922|Towards Communication-efficient Federated Learning via Sparse and Aligned Adaptive Optimization]] (81.2% similar)
- [[2025-09-22/DIVEBATCH_ Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation_20250922|DIVEBATCH: Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation]] (80.0% similar)
- [[2025-09-22/Faster Convergence of Riemannian Stochastic Gradient Descent with Increasing Batch Size_20250922|Faster Convergence of Riemannian Stochastic Gradient Descent with Increasing Batch Size]] (79.9% similar)
- [[2025-09-22/Flavors of Margin_ Implicit Bias of Steepest Descent in Homogeneous Neural Networks_20250922|Flavors of Margin: Implicit Bias of Steepest Descent in Homogeneous Neural Networks]] (79.8% similar)
- [[2025-09-17/On the Rate of Gaussian Approximation for Linear Regression Problems_20250917|On the Rate of Gaussian Approximation for Linear Regression Problems]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Convergence Rate|Convergence Rate]], [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Stochastic Gradient Descent|Stochastic Gradient Descent]]
**⚡ Unique Technical**: [[keywords/AdamW Optimizer|AdamW Optimizer]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.11840v2 Announce Type: replace 
Abstract: As the default optimizer for training large language models, AdamW has achieved remarkable success in deep learning. However, its convergence behavior is not theoretically well-understood. This paper establishes the convergence rate $\frac{1}{K}\sum_{k=1}^KE\left[||\nabla f(x^k)||_1\right]\leq O(\frac{\sqrt{d}C}{K^{1/4}})$ for AdamW measured by $\ell_1$ norm, where $K$ represents the iteration number, $d$ denotes the model dimension, and $C$ matches the constant in the optimal convergence rate of SGD. Theoretically, we have $||\nabla f(x)||_2\ll ||\nabla f(x)||_1\leq \sqrt{d}||\nabla f(x)||_2$ for any high-dimensional vector $x$ and $E\left[||\nabla f(x)||_1\right]\geq\sqrt{\frac{2d}{\pi}}E\left[||\nabla f(x)||_2\right]$ when each element of $\nabla f(x)$ is generated from Gaussian distribution $\mathcal N(0,1)$. Empirically, our experimental results on real-world deep learning tasks reveal $||\nabla f(x)||_1=\varTheta(\sqrt{d})||\nabla f(x)||_2$. Both support that our convergence rate can be considered to be analogous to the optimal $\frac{1}{K}\sum_{k=1}^KE\left[||\nabla f(x^k)||_2\right]\leq O(\frac{C}{K^{1/4}})$ convergence rate of SGD.

## 📝 요약

이 논문은 대형 언어 모델 학습에 널리 사용되는 AdamW 옵티마이저의 수렴 속도를 이론적으로 분석합니다. AdamW의 수렴 속도가 $\ell_1$ 노름으로 측정될 때 $\frac{1}{K}\sum_{k=1}^KE\left[||\nabla f(x^k)||_1\right]\leq O(\frac{\sqrt{d}C}{K^{1/4}})$임을 증명하였으며, 이는 SGD의 최적 수렴 속도와 유사합니다. 이론적으로 $\ell_2$ 노름보다 $\ell_1$ 노름이 더 크며, 실험적으로도 실제 딥러닝 작업에서 이 결과가 확인되었습니다. 이러한 분석은 AdamW의 수렴 속도가 SGD의 최적 수렴 속도와 유사하다는 것을 시사합니다.

## 🎯 주요 포인트

- 1. AdamW는 대형 언어 모델 학습의 기본 최적화 도구로서 깊이 있는 학습에서 큰 성공을 거두었지만, 그 수렴 행동은 이론적으로 잘 이해되지 않았다.
- 2. 본 논문은 AdamW의 수렴 속도를 $\ell_1$ 노름으로 측정하여 $\frac{1}{K}\sum_{k=1}^KE\left[||\nabla f(x^k)||_1\right]\leq O(\frac{\sqrt{d}C}{K^{1/4}})$로 설정하였다.
- 3. 이론적으로 고차원 벡터 $x$에 대해 $||\nabla f(x)||_2\ll ||\nabla f(x)||_1\leq \sqrt{d}||\nabla f(x)||_2$이며, $\nabla f(x)$의 각 요소가 Gaussian 분포 $\mathcal N(0,1)$에서 생성될 때 $E\left[||\nabla f(x)||_1\right]\geq\sqrt{\frac{2d}{\pi}}E\left[||\nabla f(x)||_2\right]$임을 보였다.
- 4. 실험적으로, 실제 심층 학습 작업에서 $||\nabla f(x)||_1=\varTheta(\sqrt{d})||\nabla f(x)||_2$임을 확인하였다.
- 5. 이러한 결과들은 AdamW의 수렴 속도가 SGD의 최적 수렴 속도와 유사하다는 것을 뒷받침한다.


---

*Generated on 2025-09-24 02:43:34*