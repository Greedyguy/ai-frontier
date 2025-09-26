---
keywords:
  - Analog In-memory Computing
  - Non-ideal Response Functions
  - Residual Learning
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2502.06309
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:04:18.572800",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Analog In-memory Computing",
    "Non-ideal Response Functions",
    "Residual Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Analog In-memory Computing": 0.78,
    "Non-ideal Response Functions": 0.72,
    "Residual Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Analog In-memory Computing",
        "canonical": "Analog In-memory Computing",
        "aliases": [
          "AIMC"
        ],
        "category": "unique_technical",
        "rationale": "Analog In-memory Computing is central to the paper's focus on energy-efficient solutions and training dynamics, offering a novel perspective on hardware-based learning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Non-ideal Response Functions",
        "canonical": "Non-ideal Response Functions",
        "aliases": [
          "asymmetric response functions"
        ],
        "category": "unique_technical",
        "rationale": "The paper's investigation of non-ideal response functions is crucial for understanding the limitations and potential of AIMC hardware.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Residual Learning Algorithm",
        "canonical": "Residual Learning",
        "aliases": [
          "Residual Learning Algorithm"
        ],
        "category": "specific_connectable",
        "rationale": "Residual Learning is proposed as a solution to overcome the challenges posed by non-ideal response functions, linking to broader machine learning optimization techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "training dynamic",
      "objective",
      "simulations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Analog In-memory Computing",
      "resolved_canonical": "Analog In-memory Computing",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Non-ideal Response Functions",
      "resolved_canonical": "Non-ideal Response Functions",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Residual Learning Algorithm",
      "resolved_canonical": "Residual Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Analog In-memory Training on General Non-ideal Resistive Elements: The Impact of Response Functions

**Korean Title:** 비이상적 저항 소자를 이용한 아날로그 인-메모리 학습: 응답 함수의 영향

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.06309.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2502.06309](https://arxiv.org/abs/2502.06309)

## 🔗 유사한 논문
- [[2025-09-22/Training thermodynamic computers by gradient descent_20250922|Training thermodynamic computers by gradient descent]] (81.9% similar)
- [[2025-09-18/Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (81.1% similar)
- [[2025-09-22/Both Asymptotic and Non-Asymptotic Convergence of Quasi-Hyperbolic Momentum using Increasing Batch Size_20250922|Both Asymptotic and Non-Asymptotic Convergence of Quasi-Hyperbolic Momentum using Increasing Batch Size]] (80.7% similar)
- [[2025-09-18/The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning_20250918|The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning]] (80.0% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Residual Learning|Residual Learning]]
**⚡ Unique Technical**: [[keywords/Analog In-memory Computing|Analog In-memory Computing]], [[keywords/Non-ideal Response Functions|Non-ideal Response Functions]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.06309v3 Announce Type: replace 
Abstract: As the economic and environmental costs of training and deploying large vision or language models increase dramatically, analog in-memory computing (AIMC) emerges as a promising energy-efficient solution. However, the training perspective, especially its training dynamic, is underexplored. In AIMC hardware, the trainable weights are represented by the conductance of resistive elements and updated using consecutive electrical pulses. While the conductance changes by a constant in response to each pulse, in reality, the change is scaled by asymmetric and non-linear \textit{response functions}, leading to a non-ideal training dynamic. This paper provides a theoretical foundation for gradient-based training on AIMC hardware with non-ideal response functions. We demonstrate that asymmetric response functions negatively impact Analog SGD by imposing an implicit penalty on the objective. To overcome the issue, we propose Residual Learning algorithm, which provably converges exactly to a critical point by solving a bilevel optimization problem. We demonstrate that the proposed method can be extended to address other hardware imperfections, such as limited response granularity. As we know, it is the first paper to investigate the impact of a class of generic non-ideal response functions. The conclusion is supported by simulations validating our theoretical insights.

## 🔍 Abstract (한글 번역)

arXiv:2502.06309v3 발표 유형: 교체  
초록: 대규모 비전 또는 언어 모델의 훈련 및 배포와 관련된 경제적 및 환경적 비용이 급격히 증가함에 따라, 아날로그 인-메모리 컴퓨팅(AIMC)은 유망한 에너지 효율적 솔루션으로 부상하고 있습니다. 그러나 훈련 관점, 특히 훈련 역학은 충분히 탐구되지 않았습니다. AIMC 하드웨어에서는 학습 가능한 가중치가 저항성 요소의 컨덕턴스로 표현되며, 연속적인 전기 펄스를 사용하여 업데이트됩니다. 각 펄스에 대한 응답으로 컨덕턴스가 일정하게 변화하지만, 실제로는 비대칭적이고 비선형적인 \textit{응답 함수}에 의해 변화가 조정되어 비이상적인 훈련 역학이 발생합니다. 본 논문은 비이상적인 응답 함수를 가진 AIMC 하드웨어에서의 기울기 기반 훈련을 위한 이론적 기초를 제공합니다. 우리는 비대칭 응답 함수가 목표에 암묵적인 페널티를 부과하여 아날로그 SGD에 부정적인 영향을 미친다는 것을 입증합니다. 이 문제를 해결하기 위해, 우리는 이중 최적화 문제를 해결하여 임계점에 정확히 수렴하는 것으로 입증된 잔차 학습 알고리즘을 제안합니다. 제안된 방법은 제한된 응답 세분화와 같은 다른 하드웨어 결함을 해결하기 위해 확장될 수 있음을 보여줍니다. 우리가 아는 한, 이는 일반적인 비이상적 응답 함수의 영향을 조사한 첫 번째 논문입니다. 결론은 우리의 이론적 통찰을 검증하는 시뮬레이션에 의해 뒷받침됩니다.

## 📝 요약

이 논문은 아날로그 인-메모리 컴퓨팅(AIMC) 하드웨어에서의 비이상적인 응답 함수가 훈련 동역학에 미치는 영향을 이론적으로 분석합니다. AIMC 하드웨어에서는 저항성 요소의 전도도로 가중치를 표현하고, 전기 펄스를 통해 이를 업데이트합니다. 그러나 비대칭적이고 비선형적인 응답 함수로 인해 훈련 동역학이 이상적이지 않게 됩니다. 이러한 문제를 해결하기 위해, 저자는 잔여 학습 알고리즘을 제안하여 이중 최적화 문제를 해결함으로써 정확한 수렴을 보장합니다. 이 방법은 응답의 세분화 제한과 같은 다른 하드웨어 결함에도 적용 가능합니다. 이는 비이상적인 응답 함수가 AIMC 훈련에 미치는 영향을 처음으로 조사한 연구로, 시뮬레이션을 통해 이론적 통찰을 검증했습니다.

## 🎯 주요 포인트

- 1. 아날로그 인메모리 컴퓨팅(AIMC)은 대규모 비전 및 언어 모델의 경제적, 환경적 비용을 줄이기 위한 에너지 효율적인 솔루션으로 주목받고 있습니다.
- 2. AIMC 하드웨어에서 비대칭적이고 비선형적인 응답 함수는 아날로그 SGD에 부정적인 영향을 미치며, 이는 목표에 암묵적인 페널티를 부과합니다.
- 3. 본 논문은 비이상적인 응답 함수가 있는 AIMC 하드웨어에서의 경사 기반 학습을 위한 이론적 기초를 제공합니다.
- 4. 제안된 Residual Learning 알고리즘은 이중 최적화 문제를 해결하여 임계점에 정확히 수렴할 수 있음을 증명합니다.
- 5. 시뮬레이션을 통해 제안된 방법이 이론적 통찰을 뒷받침하며, 다른 하드웨어 결함에도 확장 가능함을 보여줍니다.


---

*Generated on 2025-09-23 11:04:18*