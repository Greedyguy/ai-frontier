---
keywords:
  - Hypothesis Selection
  - Local Differential Privacy
  - Scheffé Graph
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.16180
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:57:44.515113",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hypothesis Selection",
    "Local Differential Privacy",
    "Scheffé Graph"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hypothesis Selection": 0.75,
    "Local Differential Privacy": 0.82,
    "Scheffé Graph": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "hypothesis selection",
        "canonical": "Hypothesis Selection",
        "aliases": [
          "model selection",
          "distribution selection"
        ],
        "category": "specific_connectable",
        "rationale": "Hypothesis selection is a key concept in statistical learning and connects with various selection and optimization techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "local differential privacy",
        "canonical": "Local Differential Privacy",
        "aliases": [
          "LDP",
          "differential privacy"
        ],
        "category": "broad_technical",
        "rationale": "Local differential privacy is a crucial concept in privacy-preserving data analysis, linking to privacy and security domains.",
        "novelty_score": 0.48,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Scheffé graph",
        "canonical": "Scheffé Graph",
        "aliases": [
          "Scheffe graph",
          "difference graph"
        ],
        "category": "unique_technical",
        "rationale": "The Scheffé graph is a novel concept introduced in the paper, offering a new perspective on distribution differences.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "algorithm",
      "probability distribution",
      "query-complexity"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "hypothesis selection",
      "resolved_canonical": "Hypothesis Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "local differential privacy",
      "resolved_canonical": "Local Differential Privacy",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Scheffé graph",
      "resolved_canonical": "Scheffé Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Query-Efficient Locally Private Hypothesis Selection via the Scheffe Graph

**Korean Title:** Scheffe 그래프를 통한 쿼리 효율적인 로컬 프라이빗 가설 선택

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16180.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.16180](https://arxiv.org/abs/2509.16180)

## 🔗 유사한 논문
- [[2025-09-22/Personalized Prediction By Learning Halfspace Reference Classes Under Well-Behaved Distribution_20250922|Personalized Prediction By Learning Halfspace Reference Classes Under Well-Behaved Distribution]] (78.8% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (78.2% similar)
- [[2025-09-19/Federated Hypergraph Learning with Local Differential Privacy_ Toward Privacy-Aware Hypergraph Structure Completion_20250919|Federated Hypergraph Learning with Local Differential Privacy: Toward Privacy-Aware Hypergraph Structure Completion]] (77.3% similar)
- [[2025-09-19/Preference Isolation Forest for Structure-based Anomaly Detection_20250919|Preference Isolation Forest for Structure-based Anomaly Detection]] (77.3% similar)
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (77.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Local Differential Privacy|Local Differential Privacy]]
**🔗 Specific Connectable**: [[keywords/Hypothesis Selection|Hypothesis Selection]]
**⚡ Unique Technical**: [[keywords/Scheffé Graph|Scheffé Graph]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16180v1 Announce Type: cross 
Abstract: We propose an algorithm with improved query-complexity for the problem of hypothesis selection under local differential privacy constraints. Given a set of $k$ probability distributions $Q$, we describe an algorithm that satisfies local differential privacy, performs $\tilde{O}(k^{3/2})$ non-adaptive queries to individuals who each have samples from a probability distribution $p$, and outputs a probability distribution from the set $Q$ which is nearly the closest to $p$. Previous algorithms required either $\Omega(k^2)$ queries or many rounds of interactive queries.
  Technically, we introduce a new object we dub the Scheff\'e graph, which captures structure of the differences between distributions in $Q$, and may be of more broad interest for hypothesis selection tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.16180v1 발표 유형: 교차  
초록: 우리는 지역 차등 프라이버시 제약 하에서 가설 선택 문제에 대한 개선된 쿼리 복잡성을 갖는 알고리즘을 제안합니다. $k$개의 확률 분포 집합 $Q$가 주어졌을 때, 우리는 지역 차등 프라이버시를 만족하고, 확률 분포 $p$로부터 샘플을 가진 개인에게 $\tilde{O}(k^{3/2})$의 비적응적 쿼리를 수행하며, $Q$ 집합에서 $p$에 거의 가장 가까운 확률 분포를 출력하는 알고리즘을 설명합니다. 이전 알고리즘은 $\Omega(k^2)$ 쿼리 또는 여러 번의 상호작용 쿼리 라운드를 필요로 했습니다. 기술적으로, 우리는 $Q$ 내의 분포 간 차이의 구조를 포착하는 Scheffé 그래프라는 새로운 객체를 도입하며, 이는 가설 선택 작업에 대해 더 넓은 관심을 받을 수 있습니다.

## 📝 요약

이 논문은 지역적 차등 프라이버시 제약 하에서 가설 선택 문제를 위한 쿼리 복잡도를 개선한 알고리즘을 제안합니다. $k$개의 확률 분포 집합 $Q$가 주어졌을 때, 각 개인이 확률 분포 $p$의 샘플을 가지고 있는 상황에서, 이 알고리즘은 지역적 차등 프라이버시를 만족하면서 $\tilde{O}(k^{3/2})$개의 비적응적 쿼리를 수행하여 $Q$에서 $p$에 가장 가까운 확률 분포를 출력합니다. 기존 알고리즘은 $\Omega(k^2)$개의 쿼리나 여러 라운드의 상호작용 쿼리가 필요했습니다. 기술적으로, 우리는 분포 간의 차이를 구조적으로 포착하는 새로운 개념인 Scheffé 그래프를 도입하였으며, 이는 가설 선택 작업에 더 널리 활용될 수 있습니다.

## 🎯 주요 포인트

- 1. 제안된 알고리즘은 지역적 차등 프라이버시 제약 하에서 가설 선택 문제의 쿼리 복잡성을 개선합니다.
- 2. 알고리즘은 $\tilde{O}(k^{3/2})$의 비적응적 쿼리를 수행하여, $p$와 거의 가장 가까운 확률 분포를 집합 $Q$에서 출력합니다.
- 3. 이전 알고리즘은 $\Omega(k^2)$의 쿼리 또는 여러 라운드의 상호작용 쿼리를 필요로 했습니다.
- 4. 새로운 개념인 Scheffé 그래프를 도입하여 $Q$ 내 분포 간의 차이 구조를 포착합니다.
- 5. Scheffé 그래프는 가설 선택 작업에 더 넓은 관심을 받을 수 있습니다.


---

*Generated on 2025-09-23 10:57:44*