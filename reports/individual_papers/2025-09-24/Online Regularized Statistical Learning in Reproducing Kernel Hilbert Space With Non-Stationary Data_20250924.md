<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:20:44.483138",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reproducing Kernel Hilbert Space",
    "Tikhonov Regularization",
    "Operator Theory",
    "Persistence of Excitation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reproducing Kernel Hilbert Space": 0.78,
    "Tikhonov Regularization": 0.77,
    "Operator Theory": 0.7,
    "Persistence of Excitation": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Reproducing Kernel Hilbert Space",
        "canonical": "Reproducing Kernel Hilbert Space",
        "aliases": [
          "RKHS"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's methodology, linking to advanced mathematical frameworks.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Tikhonov regularization",
        "canonical": "Tikhonov Regularization",
        "aliases": [
          "Tikhonov path"
        ],
        "category": "specific_connectable",
        "rationale": "A specific regularization technique that connects to broader statistical learning methods.",
        "novelty_score": 0.58,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "operator theory",
        "canonical": "Operator Theory",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Provides a mathematical foundation for analyzing algorithms in the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.68,
        "specificity_score": 0.72,
        "link_intent_score": 0.7
      },
      {
        "surface": "persistence of excitation",
        "canonical": "Persistence of Excitation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A unique condition introduced in the paper, crucial for algorithm stability.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "non-stationary data",
      "mean square consistency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Reproducing Kernel Hilbert Space",
      "resolved_canonical": "Reproducing Kernel Hilbert Space",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Tikhonov regularization",
      "resolved_canonical": "Tikhonov Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "operator theory",
      "resolved_canonical": "Operator Theory",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.68,
        "specificity": 0.72,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "persistence of excitation",
      "resolved_canonical": "Persistence of Excitation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Online Regularized Statistical Learning in Reproducing Kernel Hilbert Space With Non-Stationary Data

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2404.03211.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2404.03211](https://arxiv.org/abs/2404.03211)

## 🔗 유사한 논문
- [[2025-09-23/A non-smooth regularization framework for learning over multitask graphs_20250923|A non-smooth regularization framework for learning over multitask graphs]] (83.2% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (81.0% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (80.8% similar)
- [[2025-09-24/Diagonal Linear Networks and the Lasso Regularization Path_20250924|Diagonal Linear Networks and the Lasso Regularization Path]] (80.5% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Operator Theory|Operator Theory]]
**🔗 Specific Connectable**: [[keywords/Tikhonov Regularization|Tikhonov Regularization]]
**⚡ Unique Technical**: [[keywords/Reproducing Kernel Hilbert Space|Reproducing Kernel Hilbert Space]], [[keywords/Persistence of Excitation|Persistence of Excitation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2404.03211v5 Announce Type: replace 
Abstract: We study the convergence of recursive regularized learning algorithms in the reproducing kernel Hilbert space (RKHS) with dependent and non-stationary online data streams. Firstly, we introduce the concept of random Tikhonov regularization path and decompose the tracking error of the algorithm's output for the regularization path into random difference equations in RKHS, whose non-homogeneous terms are martingale difference sequences. Investigating the mean square asymptotic stability of the equations, we show that if the regularization path is slowly time-varying, then the algorithm's output achieves mean square consistency with the regularization path. Leveraging operator theory, particularly the monotonicity of the inverses of operators and the spectral decomposition of compact operators, we introduce the RKHS persistence of excitation condition (i.e. there exists a fixed-length time period, such that the conditional expectation of the operators induced by the input data accumulated over every period has a uniformly strictly positive compact lower bound) and develop a dominated convergence method to prove the mean square consistency between the algorithm's output and an unknown function. Finally, for independent and non-identically distributed data streams, the algorithm achieves the mean square consistency if the input data's marginal probability measures are slowly time-varying and the average measure over each fixed-length time period has a uniformly strictly positive lower bound.

## 📝 요약

이 논문은 종속적이고 비정상적인 온라인 데이터 스트림에서 재귀적 정규화 학습 알고리즘의 수렴성을 연구합니다. 주요 기여는 랜덤 티호노프 정규화 경로 개념을 도입하고, 알고리즘 출력의 추적 오차를 RKHS에서 랜덤 차분 방정식으로 분해한 것입니다. 비균질 항은 마팅게일 차분 시퀀스로 구성됩니다. 평균 제곱 비대칭 안정성을 조사하여 정규화 경로가 천천히 변할 경우 알고리즘 출력이 평균 제곱 일관성을 달성함을 보였습니다. 또한, 연산자 이론과 RKHS 자극 지속 조건을 활용하여 알고리즘 출력과 미지 함수 간의 평균 제곱 일관성을 증명했습니다. 독립적이고 비동일 분포 데이터 스트림의 경우, 입력 데이터의 주변 확률 측정이 천천히 변하고, 각 고정 길이 기간 동안의 평균 측정이 양의 하한을 가지면 알고리즘은 평균 제곱 일관성을 달성합니다.

## 🎯 주요 포인트

- 1. 재생 커널 힐베르트 공간(RKHS)에서 의존적이고 비정상적인 온라인 데이터 스트림을 대상으로 한 재귀적 정규화 학습 알고리즘의 수렴성을 연구합니다.
- 2. 랜덤 티호노프 정규화 경로의 개념을 도입하고, 알고리즘 출력의 추적 오류를 RKHS의 랜덤 차분 방정식으로 분해합니다.
- 3. 연산자 이론을 활용하여 RKHS 자극 지속 조건을 도입하고, 알고리즘 출력과 미지 함수 간의 평균 제곱 일관성을 증명합니다.
- 4. 독립적이고 비동일 분포 데이터 스트림의 경우, 입력 데이터의 주변 확률 측정이 천천히 시간에 따라 변화하면 알고리즘은 평균 제곱 일관성을 달성합니다.


---

*Generated on 2025-09-24 15:20:44*