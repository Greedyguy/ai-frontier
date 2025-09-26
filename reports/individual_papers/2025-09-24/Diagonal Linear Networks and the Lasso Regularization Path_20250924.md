<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:55:24.857950",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diagonal Linear Networks",
    "Lasso Regularization Path",
    "Neural Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diagonal Linear Networks": 0.78,
    "Lasso Regularization Path": 0.81,
    "Neural Network": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diagonal Linear Networks",
        "canonical": "Diagonal Linear Networks",
        "aliases": [
          "Diagonal Networks",
          "DLN"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a specific type of neural network architecture with unique properties, crucial for understanding the paper's focus.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Lasso Regularization Path",
        "canonical": "Lasso Regularization Path",
        "aliases": [
          "Lasso Path",
          "Regularization Path"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is central to the paper's analysis and connects to broader discussions on regularization techniques in machine learning.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.81
      },
      {
        "surface": "Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "Neural Nets"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental concept in the paper, linking it to the broader field of deep learning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "training",
      "simulations",
      "monotonicity assumption"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diagonal Linear Networks",
      "resolved_canonical": "Diagonal Linear Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Lasso Regularization Path",
      "resolved_canonical": "Lasso Regularization Path",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Diagonal Linear Networks and the Lasso Regularization Path

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18766.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18766](https://arxiv.org/abs/2509.18766)

## 🔗 유사한 논문
- [[2025-09-22/Flavors of Margin_ Implicit Bias of Steepest Descent in Homogeneous Neural Networks_20250922|Flavors of Margin: Implicit Bias of Steepest Descent in Homogeneous Neural Networks]] (81.0% similar)
- [[2025-09-22/Computing Linear Regions in Neural Networks with Skip Connections_20250922|Computing Linear Regions in Neural Networks with Skip Connections]] (80.5% similar)
- [[2025-09-23/Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks_20250923|Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks]] (80.4% similar)
- [[2025-09-17/Circuit realization and hardware linearization of monotone operator equilibrium networks_20250917|Circuit realization and hardware linearization of monotone operator equilibrium networks]] (80.4% similar)
- [[2025-09-22/Adversarial generalization of unfolding (model-based) networks_20250922|Adversarial generalization of unfolding (model-based) networks]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Lasso Regularization Path|Lasso Regularization Path]]
**⚡ Unique Technical**: [[keywords/Diagonal Linear Networks|Diagonal Linear Networks]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18766v1 Announce Type: new 
Abstract: Diagonal linear networks are neural networks with linear activation and diagonal weight matrices. Their theoretical interest is that their implicit regularization can be rigorously analyzed: from a small initialization, the training of diagonal linear networks converges to the linear predictor with minimal 1-norm among minimizers of the training loss. In this paper, we deepen this analysis showing that the full training trajectory of diagonal linear networks is closely related to the lasso regularization path. In this connection, the training time plays the role of an inverse regularization parameter. Both rigorous results and simulations are provided to illustrate this conclusion. Under a monotonicity assumption on the lasso regularization path, the connection is exact while in the general case, we show an approximate connection.

## 📝 요약

이 논문은 대각선 선형 네트워크의 훈련 경로가 라쏘 정규화 경로와 밀접하게 관련되어 있음을 분석합니다. 대각선 선형 네트워크는 선형 활성화 함수와 대각선 가중치 행렬을 사용하는 신경망으로, 작은 초기값에서 시작하여 훈련 시 최소 1-노름을 갖는 선형 예측기로 수렴합니다. 이 연구는 훈련 시간이 역정규화 매개변수 역할을 한다는 점을 강조하며, 엄밀한 결과와 시뮬레이션을 통해 이를 입증합니다. 라쏘 경로의 단조성 가정 하에서는 정확한 연결이, 일반적인 경우에는 근사적인 연결이 성립함을 보여줍니다.

## 🎯 주요 포인트

- 1. 대각선 선형 네트워크는 선형 활성화 함수와 대각선 가중치 행렬을 가진 신경망이다.
- 2. 대각선 선형 네트워크의 훈련은 최소 1-노름을 가진 선형 예측기로 수렴한다.
- 3. 대각선 선형 네트워크의 훈련 경로는 라쏘 정규화 경로와 밀접한 관련이 있다.
- 4. 훈련 시간은 역정규화 매개변수의 역할을 한다.
- 5. 라쏘 정규화 경로의 단조성 가정 하에 대각선 선형 네트워크와의 연결은 정확하다.


---

*Generated on 2025-09-24 14:55:24*