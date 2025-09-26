---
keywords:
  - Federated Learning
  - Adaptive Moment Estimation
  - Sparse Federated Adam
  - Convergence Rate
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2405.17932
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:00:32.512361",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Adaptive Moment Estimation",
    "Sparse Federated Adam",
    "Convergence Rate"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Learning": 0.85,
    "Adaptive Moment Estimation": 0.78,
    "Sparse Federated Adam": 0.82,
    "Convergence Rate": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Learning",
        "canonical": "Federated Learning",
        "aliases": [
          "FL"
        ],
        "category": "broad_technical",
        "rationale": "Federated Learning is a central theme of the paper and connects with various distributed machine learning discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.89,
        "specificity_score": 0.68,
        "link_intent_score": 0.85
      },
      {
        "surface": "Adaptive Moment Estimation",
        "canonical": "Adaptive Moment Estimation",
        "aliases": [
          "Adam"
        ],
        "category": "unique_technical",
        "rationale": "Adaptive Moment Estimation is a key optimization technique discussed in the paper, relevant to optimization strategies in machine learning.",
        "novelty_score": 0.62,
        "connectivity_score": 0.76,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sparse FedAdam",
        "canonical": "Sparse Federated Adam",
        "aliases": [
          "FedAdam-SSM"
        ],
        "category": "unique_technical",
        "rationale": "Sparse FedAdam is a novel algorithm introduced in the paper, enhancing federated learning efficiency.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Convergence Rate",
        "canonical": "Convergence Rate",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Convergence Rate is a critical metric for evaluating the performance of optimization algorithms in federated learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "uplink communication",
      "local model updates",
      "test accuracy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Learning",
      "resolved_canonical": "Federated Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.89,
        "specificity": 0.68,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Adaptive Moment Estimation",
      "resolved_canonical": "Adaptive Moment Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.62,
        "connectivity": 0.76,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sparse FedAdam",
      "resolved_canonical": "Sparse Federated Adam",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Convergence Rate",
      "resolved_canonical": "Convergence Rate",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Towards Communication-efficient Federated Learning via Sparse and Aligned Adaptive Optimization

**Korean Title:** 의사소통 효율적인 연합 학습을 위한 희소하고 정렬된 적응 최적화 방안

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2405.17932.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2405.17932](https://arxiv.org/abs/2405.17932)

## 🔗 유사한 논문
- [[2025-09-19/FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT: Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (83.8% similar)
- [[2025-09-17/FedSSG_ Expectation-Gated and History-Aware Drift Alignment for Federated Learning_20250917|FedSSG: Expectation-Gated and History-Aware Drift Alignment for Federated Learning]] (83.5% similar)
- [[2025-09-19/Hierarchical Federated Learning for Social Network with Mobility_20250919|Hierarchical Federated Learning for Social Network with Mobility]] (82.3% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (80.2% similar)
- [[2025-09-19/Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Federated Learning|Federated Learning]]
**🔗 Specific Connectable**: [[keywords/Convergence Rate|Convergence Rate]]
**⚡ Unique Technical**: [[keywords/Adaptive Moment Estimation|Adaptive Moment Estimation]], [[keywords/Sparse Federated Adam|Sparse Federated Adam]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2405.17932v2 Announce Type: replace 
Abstract: Adaptive moment estimation (Adam), as a Stochastic Gradient Descent (SGD) variant, has gained widespread popularity in federated learning (FL) due to its fast convergence. However, federated Adam (FedAdam) algorithms suffer from a threefold increase in uplink communication overhead compared to federated SGD (FedSGD) algorithms, which arises from the necessity to transmit both local model updates and first and second moment estimates from distributed devices to the centralized server for aggregation. Driven by this issue, we propose a novel sparse FedAdam algorithm called FedAdam-SSM, wherein distributed devices sparsify the updates of local model parameters and moment estimates and subsequently upload the sparse representations to the centralized server. To further reduce the communication overhead, the updates of local model parameters and moment estimates incorporate a shared sparse mask (SSM) into the sparsification process, eliminating the need for three separate sparse masks. Theoretically, we develop an upper bound on the divergence between the local model trained by FedAdam-SSM and the desired model trained by centralized Adam, which is related to sparsification error and imbalanced data distribution. By minimizing the divergence bound between the model trained by FedAdam-SSM and centralized Adam, we optimize the SSM to mitigate the learning performance degradation caused by sparsification error. Additionally, we provide convergence bounds for FedAdam-SSM in both convex and non-convex objective function settings, and investigate the impact of local epoch, learning rate and sparsification ratio on the convergence rate of FedAdam-SSM. Experimental results show that FedAdam-SSM outperforms baselines in terms of convergence rate (over 1.1$\times$ faster than the sparse FedAdam baselines) and test accuracy (over 14.5\% ahead of the quantized FedAdam baselines).

## 🔍 Abstract (한글 번역)

arXiv:2405.17932v2 발표 유형: 교체

초록: 적응적 모멘트 추정(Adam)은 확률적 경사 하강법(SGD)의 변형으로, 빠른 수렴 속도로 인해 연합 학습(FL)에서 널리 인기를 얻고 있습니다. 그러나 연합 Adam(FedAdam) 알고리즘은 연합 SGD(FedSGD) 알고리즘에 비해 업링크 통신 오버헤드가 세 배 증가하는 문제를 겪고 있습니다. 이는 분산된 장치에서 중앙 서버로 로컬 모델 업데이트와 1차 및 2차 모멘트 추정을 모두 전송해야 하기 때문입니다. 이 문제를 해결하기 위해, 우리는 FedAdam-SSM이라는 새로운 희소 FedAdam 알고리즘을 제안합니다. 이 알고리즘에서는 분산된 장치가 로컬 모델 파라미터와 모멘트 추정의 업데이트를 희소화하여 희소 표현을 중앙 서버로 업로드합니다. 통신 오버헤드를 더욱 줄이기 위해, 로컬 모델 파라미터와 모멘트 추정의 업데이트는 희소화 과정에 공유 희소 마스크(SSM)를 포함시켜 세 개의 별도 희소 마스크가 필요하지 않도록 합니다. 이론적으로, 우리는 FedAdam-SSM에 의해 훈련된 로컬 모델과 중앙 집중식 Adam에 의해 훈련된 목표 모델 간의 발산에 대한 상한을 개발하였으며, 이는 희소화 오류와 불균형한 데이터 분포와 관련이 있습니다. FedAdam-SSM에 의해 훈련된 모델과 중앙 집중식 Adam 간의 발산 경계를 최소화함으로써, 우리는 희소화 오류로 인한 학습 성능 저하를 완화하기 위해 SSM을 최적화합니다. 또한, 우리는 볼록 및 비볼록 목적 함수 설정에서 FedAdam-SSM의 수렴 경계를 제공하고, 로컬 에폭, 학습률 및 희소화 비율이 FedAdam-SSM의 수렴 속도에 미치는 영향을 조사합니다. 실험 결과, FedAdam-SSM은 수렴 속도(희소 FedAdam 기준선보다 1.1배 이상 빠름)와 테스트 정확도(양자화된 FedAdam 기준선보다 14.5% 이상 앞섬) 측면에서 기준선을 능가하는 것으로 나타났습니다.

## 📝 요약

이 논문은 연합 학습에서의 적응 모멘트 추정(Adam) 알고리즘의 통신 오버헤드를 줄이기 위해 새로운 희소 FedAdam 알고리즘인 FedAdam-SSM을 제안합니다. FedAdam-SSM은 로컬 모델 업데이트와 모멘트 추정치를 희소화하여 중앙 서버로 전송하며, 공유 희소 마스크(SSM)를 사용해 통신 오버헤드를 줄입니다. 이 방법론은 희소화 오류와 불균형 데이터 분포로 인한 모델 간의 발산을 이론적으로 분석하고, FedAdam-SSM의 수렴 경계를 제시합니다. 실험 결과, FedAdam-SSM은 수렴 속도와 테스트 정확도에서 기존 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. FedAdam 알고리즘은 FedSGD에 비해 3배의 업링크 통신 오버헤드가 발생합니다.
- 2. FedAdam-SSM 알고리즘은 로컬 모델 파라미터와 모멘트 추정치를 희소화하여 통신 오버헤드를 줄입니다.
- 3. 공유 희소 마스크(SSM)를 사용하여 세 개의 별도 희소 마스크 필요성을 제거합니다.
- 4. FedAdam-SSM의 수렴 경계는 볼록 및 비볼록 목적 함수 설정에서 제공됩니다.
- 5. 실험 결과, FedAdam-SSM은 수렴 속도와 테스트 정확도에서 기존 방법보다 우수한 성능을 보입니다.


---

*Generated on 2025-09-23 11:00:32*