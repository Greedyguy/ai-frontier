---
keywords:
  - Quantum Sensitivity Sampling
  - Coreset
  - Low-Rank Approximation
  - Quantum Sublinear-Time Algorithm
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16801
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:16:22.079613",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Quantum Sensitivity Sampling",
    "Coreset",
    "Low-Rank Approximation",
    "Quantum Sublinear-Time Algorithm"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Quantum Sensitivity Sampling": 0.78,
    "Coreset": 0.79,
    "Low-Rank Approximation": 0.8,
    "Quantum Sublinear-Time Algorithm": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "quantum sensitivity sampling",
        "canonical": "Quantum Sensitivity Sampling",
        "aliases": [
          "quantum sampling",
          "sensitivity sampling"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a novel framework extending quantum computing to classical problems, offering potential for unique connections in quantum computing research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "coreset",
        "canonical": "Coreset",
        "aliases": [
          "epsilon-coreset"
        ],
        "category": "specific_connectable",
        "rationale": "Coresets are crucial for efficient data summarization in clustering and regression, providing strong links to optimization and data reduction techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      },
      {
        "surface": "low-rank approximation",
        "canonical": "Low-Rank Approximation",
        "aliases": [
          "rank reduction"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is fundamental in numerical linear algebra and connects to various applications in data compression and machine learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "quantum sublinear-time algorithm",
        "canonical": "Quantum Sublinear-Time Algorithm",
        "aliases": [
          "quantum sublinear algorithm"
        ],
        "category": "unique_technical",
        "rationale": "This represents a cutting-edge advancement in quantum algorithms, offering potential for novel connections in computational complexity.",
        "novelty_score": 0.78,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "algorithm",
      "improvement",
      "approach"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "quantum sensitivity sampling",
      "resolved_canonical": "Quantum Sensitivity Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "coreset",
      "resolved_canonical": "Coreset",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "low-rank approximation",
      "resolved_canonical": "Low-Rank Approximation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "quantum sublinear-time algorithm",
      "resolved_canonical": "Quantum Sublinear-Time Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Sublinear Time Quantum Sensitivity Sampling

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16801.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16801](https://arxiv.org/abs/2509.16801)

## 🔗 유사한 논문
- [[2025-09-17/Learning quantum many-body data locally_ A provably scalable framework_20250917|Learning quantum many-body data locally: A provably scalable framework]] (82.8% similar)
- [[2025-09-22/Efficient Learning for Linear Properties of Bounded-Gate Quantum Circuits_20250922|Efficient Learning for Linear Properties of Bounded-Gate Quantum Circuits]] (82.3% similar)
- [[2025-09-22/Double descent in quantum kernel methods_20250922|Double descent in quantum kernel methods]] (80.6% similar)
- [[2025-09-22/Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization_20250922|Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization]] (80.4% similar)
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Coreset|Coreset]], [[keywords/Low-Rank Approximation|Low-Rank Approximation]]
**⚡ Unique Technical**: [[keywords/Quantum Sensitivity Sampling|Quantum Sensitivity Sampling]], [[keywords/Quantum Sublinear-Time Algorithm|Quantum Sublinear-Time Algorithm]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16801v1 Announce Type: cross 
Abstract: We present a unified framework for quantum sensitivity sampling, extending the advantages of quantum computing to a broad class of classical approximation problems. Our unified framework provides a streamlined approach for constructing coresets and offers significant runtime improvements in applications such as clustering, regression, and low-rank approximation. Our contributions include:
  * $k$-median and $k$-means clustering: For $n$ points in $d$-dimensional Euclidean space, we give an algorithm that constructs an $\epsilon$-coreset in time $\widetilde O(n^{0.5}dk^{2.5}~\mathrm{poly}(\epsilon^{-1}))$ for $k$-median and $k$-means clustering. Our approach achieves a better dependence on $d$ and constructs smaller coresets that only consist of points in the dataset, compared to recent results of [Xue, Chen, Li and Jiang, ICML'23].
  * $\ell_p$ regression: For $\ell_p$ regression problems, we construct an $\epsilon$-coreset of size $\widetilde O_p(d^{\max\{1, p/2\}}\epsilon^{-2})$ in time $\widetilde O_p(n^{0.5}d^{\max\{0.5, p/4\}+1}(\epsilon^{-3}+d^{0.5}))$, improving upon the prior best quantum sampling approach of [Apers and Gribling, QIP'24] for all $p\in (0, 2)\cup (2, 22]$, including the widely studied least absolute deviation regression ($\ell_1$ regression).
  * Low-rank approximation with Frobenius norm error: We introduce the first quantum sublinear-time algorithm for low-rank approximation that does not rely on data-dependent parameters, and runs in $\widetilde O(nd^{0.5}k^{0.5}\epsilon^{-1})$ time. Additionally, we present quantum sublinear algorithms for kernel low-rank approximation and tensor low-rank approximation, broadening the range of achievable sublinear time algorithms in randomized numerical linear algebra.

## 📝 요약

이 논문은 양자 민감도 샘플링을 위한 통합 프레임워크를 제시하여, 양자 컴퓨팅의 이점을 다양한 고전적 근사 문제에 확장합니다. 주요 기여는 다음과 같습니다. 첫째, $k$-중앙값 및 $k$-평균 군집화에서, $d$차원 유클리드 공간의 $n$개의 점에 대해 $\epsilon$-코어셋을 효율적으로 구성하는 알고리즘을 제안하여, 기존 연구보다 더 작은 코어셋을 생성합니다. 둘째, $\ell_p$ 회귀 문제에서, 모든 $p\in (0, 2)\cup (2, 22]$에 대해 이전보다 개선된 $\epsilon$-코어셋을 구성하는 방법을 제시합니다. 셋째, 프로베니우스 노름 오류를 사용하는 저랭크 근사 문제에 대해 데이터 의존 매개변수 없이 양자 서브선형 시간 알고리즘을 도입하여, 무작위 수치 선형 대수의 서브선형 시간 알고리즘 범위를 확장합니다.

## 🎯 주요 포인트

- 1. 본 연구는 양자 민감도 샘플링을 위한 통합 프레임워크를 제시하여, 양자 컴퓨팅의 이점을 다양한 고전적 근사 문제에 확장합니다.
- 2. $k$-중간값 및 $k$-평균 클러스터링에서, 제안된 알고리즘은 최근 연구보다 더 작은 코어셋을 구성하며, $d$에 대한 의존성을 개선합니다.
- 3. $\ell_p$ 회귀 문제에 대해, 제안된 방법은 모든 $p\in (0, 2)\cup (2, 22]$에 대해 이전의 양자 샘플링 접근법보다 개선된 성능을 보여줍니다.
- 4. Frobenius 노름 오류를 가진 저순위 근사 문제에 대해, 데이터 의존적 매개변수에 의존하지 않는 최초의 양자 서브선형 시간 알고리즘을 도입합니다.
- 5. 제안된 프레임워크는 커널 저순위 근사 및 텐서 저순위 근사에 대한 양자 서브선형 알고리즘을 제시하여, 무작위 수치 선형 대수에서 달성 가능한 서브선형 시간 알고리즘의 범위를 확장합니다.


---

*Generated on 2025-09-24 02:16:22*