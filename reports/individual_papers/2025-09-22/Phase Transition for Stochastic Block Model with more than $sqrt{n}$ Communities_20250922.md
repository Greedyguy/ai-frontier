---
keywords:
  - Stochastic Block Model
  - Kesten-Stigum threshold
  - Community Detection
  - Non-backtracking Paths
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15822
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:53:26.477785",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Stochastic Block Model",
    "Kesten-Stigum threshold",
    "Community Detection",
    "Non-backtracking Paths"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Stochastic Block Model": 0.8,
    "Kesten-Stigum threshold": 0.75,
    "Community Detection": 0.72,
    "Non-backtracking Paths": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Stochastic Block Model",
        "canonical": "Stochastic Block Model",
        "aliases": [
          "SBM"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's discussion on community recovery and phase transitions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Kesten-Stigum threshold",
        "canonical": "Kesten-Stigum threshold",
        "aliases": [
          "KS threshold"
        ],
        "category": "unique_technical",
        "rationale": "Key threshold discussed for community recovery in the SBM context.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.88,
        "link_intent_score": 0.75
      },
      {
        "surface": "community recovery",
        "canonical": "Community Detection",
        "aliases": [
          "community recovery"
        ],
        "category": "broad_technical",
        "rationale": "Essential concept for understanding the implications of the SBM phase transition.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      },
      {
        "surface": "non-backtracking paths",
        "canonical": "Non-backtracking Paths",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Method used for community recovery below the KS threshold.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "polynomial time",
      "sparse regime"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Stochastic Block Model",
      "resolved_canonical": "Stochastic Block Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Kesten-Stigum threshold",
      "resolved_canonical": "Kesten-Stigum threshold",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.88,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "community recovery",
      "resolved_canonical": "Community Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "non-backtracking paths",
      "resolved_canonical": "Non-backtracking Paths",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Phase Transition for Stochastic Block Model with more than $\sqrt{n}$ Communities

**Korean Title:** 확률적 블록 모델에서 $\sqrt{n}$ 이상의 커뮤니티를 가진 경우의 상전이

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15822.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15822](https://arxiv.org/abs/2509.15822)

## 🔗 유사한 논문
- [[2025-09-22/Model-free algorithms for fast node clustering in SBM type graphs and application to social role inference in animals_20250922|Model-free algorithms for fast node clustering in SBM type graphs and application to social role inference in animals]] (81.7% similar)
- [[2025-09-19/How Bad Is Forming Your Own Multidimensional Opinion?_20250919|How Bad Is Forming Your Own Multidimensional Opinion?]] (76.7% similar)
- [[2025-09-22/Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows_20250922|Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows]] (76.5% similar)
- [[2025-09-18/Asymptotic Boundedness of Distributed Set-Membership Filtering_20250918|Asymptotic Boundedness of Distributed Set-Membership Filtering]] (76.5% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (76.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Community Detection|Community Detection]]
**🔗 Specific Connectable**: [[keywords/Non-backtracking Paths|Non-backtracking Paths]]
**⚡ Unique Technical**: [[keywords/Stochastic Block Model|Stochastic Block Model]], [[keywords/Kesten-Stigum threshold|Kesten-Stigum threshold]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15822v1 Announce Type: cross 
Abstract: Predictions from statistical physics postulate that recovery of the communities in Stochastic Block Model (SBM) is possible in polynomial time above, and only above, the Kesten-Stigum (KS) threshold. This conjecture has given rise to a rich literature, proving that non-trivial community recovery is indeed possible in SBM above the KS threshold, as long as the number $K$ of communities remains smaller than $\sqrt{n}$, where $n$ is the number of nodes in the observed graph. Failure of low-degree polynomials below the KS threshold was also proven when $K=o(\sqrt{n})$.
  When $K\geq \sqrt{n}$, Chin et al.(2025) recently prove that, in a sparse regime, community recovery in polynomial time is possible below the KS threshold by counting non-backtracking paths. This breakthrough result lead them to postulate a new threshold for the many communities regime $K\geq \sqrt{n}$. In this work, we provide evidences that confirm their conjecture for $K\geq \sqrt{n}$:
  1- We prove that, for any density of the graph, low-degree polynomials fail to recover communities below the threshold postulated by Chin et al.(2025);
  2- We prove that community recovery is possible in polynomial time above the postulated threshold, not only in the sparse regime of~Chin et al., but also in some (but not all) moderately sparse regimes by essentially counting clique occurence in the observed graph.

## 🔍 Abstract (한글 번역)

arXiv:2509.15822v1 발표 유형: 교차  
초록: 통계 물리학의 예측에 따르면, 확률적 블록 모델(SBM)에서 공동체 복구는 Kesten-Stigum(KS) 임계값 이상에서, 그리고 오직 그 이상에서 다항 시간 내에 가능하다고 가정된다. 이 가설은 풍부한 문헌을 낳았으며, 관찰된 그래프의 노드 수를 $n$이라고 할 때, 공동체의 수 $K$가 $\sqrt{n}$보다 작은 경우 KS 임계값 이상에서 비자명한 공동체 복구가 실제로 가능하다는 것을 증명했다. $K=o(\sqrt{n})$인 경우 KS 임계값 이하에서 저차 다항식의 실패도 증명되었다.  
$K\geq \sqrt{n}$인 경우, Chin 등(2025)은 최근 희소한 상태에서 비반복 경로를 세어 KS 임계값 이하에서 다항 시간 내에 공동체 복구가 가능하다고 증명했다. 이 획기적인 결과는 그들이 다수의 공동체 상태 $K\geq \sqrt{n}$에 대한 새로운 임계값을 제안하도록 이끌었다. 본 연구에서는 $K\geq \sqrt{n}$에 대한 그들의 가설을 확인하는 증거를 제공한다:  
1- 우리는 Chin 등(2025)이 제안한 임계값 이하에서, 그래프의 어떤 밀도에서도 저차 다항식이 공동체를 복구하는 데 실패한다는 것을 증명한다;  
2- 우리는 Chin 등의 희소한 상태뿐만 아니라 일부(하지만 모두는 아닌) 중간 희소 상태에서도 본질적으로 관찰된 그래프에서 클리크 발생을 세어 제안된 임계값 이상에서 다항 시간 내에 공동체 복구가 가능하다는 것을 증명한다.

## 📝 요약

이 논문은 확률적 블록 모델(SBM)에서 커뮤니티 복구가 Kesten-Stigum(KS) 임계값 이상에서만 다항 시간 내에 가능하다는 기존 이론을 확장합니다. Chin et al.(2025)은 K가 노드 수 n의 제곱근 이상일 때, KS 임계값 이하에서도 희소한 조건에서 비회귀 경로를 세어 커뮤니티 복구가 가능하다고 주장했습니다. 본 연구는 이 주장을 확인하며, K가 n의 제곱근 이상일 때, Chin et al.이 제안한 새로운 임계값 아래에서는 저차 다항식이 커뮤니티 복구에 실패함을 증명하고, 제안된 임계값 이상에서는 희소 및 중간 희소 조건에서도 다항 시간 내에 커뮤니티 복구가 가능함을 입증합니다.

## 🎯 주요 포인트

- 1. 확률적 블록 모델(SBM)에서 Kesten-Stigum(KS) 임계값 이상에서는 다항 시간 내에 비자명한 커뮤니티 복구가 가능하다.
- 2. 커뮤니티 수 $K$가 $\sqrt{n}$보다 작을 때, KS 임계값 이하에서는 저차 다항식이 커뮤니티 복구에 실패한다.
- 3. $K \geq \sqrt{n}$인 경우, Chin et al.(2025)은 희소한 조건에서 비회귀 경로를 세어 KS 임계값 이하에서도 다항 시간 내에 커뮤니티 복구가 가능함을 증명했다.
- 4. 본 연구는 $K \geq \sqrt{n}$인 경우, Chin et al.(2025)이 제안한 새로운 임계값 아래에서 저차 다항식이 커뮤니티 복구에 실패함을 증명한다.
- 5. 제안된 임계값 이상에서는 희소한 조건뿐만 아니라 일부 중간 희소 조건에서도 다항 시간 내에 커뮤니티 복구가 가능함을 증명한다.


---

*Generated on 2025-09-23 10:53:26*