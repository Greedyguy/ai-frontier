---
keywords:
  - Black-Box Optimization
  - Probabilistic Bridge
  - Gaussian Processes
  - Distributional Translation
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16300
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:33:59.507409",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Black-Box Optimization",
    "Probabilistic Bridge",
    "Gaussian Processes",
    "Distributional Translation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Black-Box Optimization": 0.75,
    "Probabilistic Bridge": 0.78,
    "Gaussian Processes": 0.8,
    "Distributional Translation": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "black-box optimization",
        "canonical": "Black-Box Optimization",
        "aliases": [
          "BBO"
        ],
        "category": "unique_technical",
        "rationale": "Black-box optimization is a specific technique that can connect with various optimization methods and applications.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "probabilistic bridge",
        "canonical": "Probabilistic Bridge",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The concept of a probabilistic bridge is novel and central to the paper's approach, offering potential connections to probabilistic modeling.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Gaussian processes",
        "canonical": "Gaussian Processes",
        "aliases": [
          "GP"
        ],
        "category": "broad_technical",
        "rationale": "Gaussian processes are a fundamental technique in machine learning, relevant for linking with probabilistic models.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "distributional translation",
        "canonical": "Distributional Translation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This term represents a unique approach to optimization, facilitating connections with translation and transformation methodologies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.55,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "offline data",
      "surrogate function",
      "inverse modeling"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "black-box optimization",
      "resolved_canonical": "Black-Box Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "probabilistic bridge",
      "resolved_canonical": "Probabilistic Bridge",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Gaussian processes",
      "resolved_canonical": "Gaussian Processes",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "distributional translation",
      "resolved_canonical": "Distributional Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.55,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# ROOT: Rethinking Offline Optimization as Distributional Translation via Probabilistic Bridge

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16300.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16300](https://arxiv.org/abs/2509.16300)

## 🔗 유사한 논문
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (80.5% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (80.0% similar)
- [[2025-09-23/Dynamic Speculative Agent Planning_20250923|Dynamic Speculative Agent Planning]] (79.5% similar)
- [[2025-09-23/Adaptive Kernel Design for Bayesian Optimization Is a Piece of CAKE with LLMs_20250923|Adaptive Kernel Design for Bayesian Optimization Is a Piece of CAKE with LLMs]] (79.3% similar)
- [[2025-09-19/Online Multi-Robot Coordination and Cooperation with Task Precedence Relationships_20250919|Online Multi-Robot Coordination and Cooperation with Task Precedence Relationships]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Gaussian Processes|Gaussian Processes]]
**⚡ Unique Technical**: [[keywords/Black-Box Optimization|Black-Box Optimization]], [[keywords/Probabilistic Bridge|Probabilistic Bridge]], [[keywords/Distributional Translation|Distributional Translation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16300v1 Announce Type: new 
Abstract: This paper studies the black-box optimization task which aims to find the maxima of a black-box function using a static set of its observed input-output pairs. This is often achieved via learning and optimizing a surrogate function with that offline data. Alternatively, it can also be framed as an inverse modeling task that maps a desired performance to potential input candidates that achieve it. Both approaches are constrained by the limited amount of offline data. To mitigate this limitation, we introduce a new perspective that casts offline optimization as a distributional translation task. This is formulated as learning a probabilistic bridge transforming an implicit distribution of low-value inputs (i.e., offline data) into another distribution of high-value inputs (i.e., solution candidates). Such probabilistic bridge can be learned using low- and high-value inputs sampled from synthetic functions that resemble the target function. These synthetic functions are constructed as the mean posterior of multiple Gaussian processes fitted with different parameterizations on the offline data, alleviating the data bottleneck. The proposed approach is evaluated on an extensive benchmark comprising most recent methods, demonstrating significant improvement and establishing a new state-of-the-art performance.

## 📝 요약

이 논문은 블랙박스 함수의 최대값을 찾기 위한 블랙박스 최적화 문제를 다룹니다. 기존 방법은 관찰된 입력-출력 쌍을 사용하여 대리 함수를 학습하고 최적화하거나, 원하는 성능을 달성할 수 있는 입력 후보를 찾는 역모델링 방식으로 접근합니다. 그러나 이러한 방법들은 제한된 오프라인 데이터에 의해 제약을 받습니다. 이를 극복하기 위해 본 연구는 오프라인 최적화를 분포 변환 작업으로 재구성하는 새로운 관점을 제안합니다. 이는 낮은 값의 입력 분포를 높은 값의 입력 분포로 변환하는 확률적 다리를 학습하는 것으로, 목표 함수와 유사한 합성 함수를 사용하여 학습합니다. 합성 함수는 다양한 매개변수로 오프라인 데이터에 맞춘 다중 가우시안 프로세스의 평균 후행으로 구성됩니다. 제안된 방법은 최신 방법들을 포함한 광범위한 벤치마크에서 평가되었으며, 성능이 크게 향상되어 새로운 최첨단 성과를 달성했습니다.

## 🎯 주요 포인트

- 1. 본 논문은 블랙박스 함수의 최대값을 찾기 위한 블랙박스 최적화 작업을 연구하며, 관찰된 입력-출력 쌍의 정적 집합을 사용합니다.
- 2. 기존의 방법들은 제한된 오프라인 데이터로 인해 제약을 받으며, 이를 완화하기 위해 오프라인 최적화를 분포 번역 작업으로 재구성하는 새로운 관점을 제시합니다.
- 3. 제안된 방법은 낮은 가치의 입력 분포를 높은 가치의 입력 분포로 변환하는 확률적 다리를 학습하여 데이터 병목 현상을 완화합니다.
- 4. 여러 가우시안 프로세스의 평균 사후 확률로 구성된 합성 함수를 사용하여 목표 함수와 유사한 입력을 샘플링합니다.
- 5. 제안된 접근법은 최신 방법들을 포함한 광범위한 벤치마크에서 평가되었으며, 상당한 개선을 보여주며 새로운 최첨단 성능을 확립했습니다.


---

*Generated on 2025-09-24 01:33:59*