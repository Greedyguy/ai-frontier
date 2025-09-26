<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:57:59.093050",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Simulation-Grounded Neural Networks",
    "Bayesian Inference",
    "Mechanistic Interpretability",
    "Model Misspecification"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Simulation-Grounded Neural Networks": 0.8,
    "Bayesian Inference": 0.75,
    "Mechanistic Interpretability": 0.78,
    "Model Misspecification": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Simulation-Grounded Neural Networks",
        "canonical": "Simulation-Grounded Neural Networks",
        "aliases": [
          "SGNNs"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to neural networks that is central to the paper's contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Bayesian Inference",
        "canonical": "Bayesian Inference",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A foundational statistical method that underpins the theoretical framework discussed.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Mechanistic Interpretability",
        "canonical": "Mechanistic Interpretability",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a novel interpretability approach enabled by SGNNs, crucial for scientific explanations.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Model Misspecification",
        "canonical": "Model Misspecification",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Addresses a common issue in predictive modeling, relevant to the paper's generalization bounds.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Simulation-Grounded Neural Networks",
      "resolved_canonical": "Simulation-Grounded Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Bayesian Inference",
      "resolved_canonical": "Bayesian Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Mechanistic Interpretability",
      "resolved_canonical": "Mechanistic Interpretability",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Model Misspecification",
      "resolved_canonical": "Model Misspecification",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Learning From Simulators: A Theory of Simulation-Grounded Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18990.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18990](https://arxiv.org/abs/2509.18990)

## 🔗 유사한 논문
- [[2025-09-23/Self-Supervised Discovery of Neural Circuits in Spatially Patterned Neural Responses with Graph Neural Networks_20250923|Self-Supervised Discovery of Neural Circuits in Spatially Patterned Neural Responses with Graph Neural Networks]] (80.7% similar)
- [[2025-09-22/GIN-Graph_ A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks_20250922|GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks]] (80.6% similar)
- [[2025-09-22/Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows_20250922|Universal Learning of Stochastic Dynamics for Exact Belief Propagation using Bernstein Normalizing Flows]] (80.6% similar)
- [[2025-09-23/Informed, but Not Always Improved_ Challenging the Benefit of Background Knowledge in GNNs_20250923|Informed, but Not Always Improved: Challenging the Benefit of Background Knowledge in GNNs]] (80.4% similar)
- [[2025-09-23/From Prediction to Understanding_ Will AI Foundation Models Transform Brain Science?_20250923|From Prediction to Understanding: Will AI Foundation Models Transform Brain Science?]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Bayesian Inference|Bayesian Inference]]
**🔗 Specific Connectable**: [[keywords/Model Misspecification|Model Misspecification]]
**⚡ Unique Technical**: [[keywords/Simulation-Grounded Neural Networks|Simulation-Grounded Neural Networks]], [[keywords/Mechanistic Interpretability|Mechanistic Interpretability]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18990v1 Announce Type: new 
Abstract: Simulation-Grounded Neural Networks (SGNNs) are predictive models trained entirely on synthetic data from mechanistic simulations. They have achieved state-of-the-art performance in domains where real-world labels are limited or unobserved, but lack a formal underpinning.
  We present the foundational theory of simulation-grounded learning. We show that SGNNs implement amortized Bayesian inference under a simulation prior and converge to the Bayes-optimal predictor. We derive generalization bounds under model misspecification and prove that SGNNs can learn unobservable scientific quantities that empirical methods provably cannot. We also formalize a novel form of mechanistic interpretability uniquely enabled by SGNNs: by attributing predictions to the simulated mechanisms that generated them, SGNNs yield posterior-consistent, scientifically grounded explanations.
  We provide numerical experiments to validate all theoretical predictions. SGNNs recover latent parameters, remain robust under mismatch, and outperform classical tools: in a model selection task, SGNNs achieve half the error of AIC in distinguishing mechanistic dynamics. These results establish SGNNs as a principled and practical framework for scientific prediction in data-limited regimes.

## 📝 요약

이 논문은 시뮬레이션 기반 신경망(SGNNs)의 이론적 기초를 제시하며, 이 모델이 시뮬레이션 사전 확률 하에서 베이지안 추론을 수행하고 베이즈 최적 예측기에 수렴함을 보입니다. SGNNs는 모델 불일치 상황에서도 일반화 경계를 유지하며, 실증적 방법으로는 학습할 수 없는 비가시적 과학적 양을 학습할 수 있음을 증명합니다. 또한, SGNNs는 시뮬레이션 메커니즘을 통해 예측을 설명하는 새로운 형태의 메커니즘 해석 가능성을 제공합니다. 실험 결과, SGNNs는 잠재 매개변수를 회복하고, 모델 선택 작업에서 AIC보다 절반의 오류율로 뛰어난 성능을 보였습니다. 이는 데이터가 제한된 환경에서 과학적 예측을 위한 유용한 프레임워크로 SGNNs의 가능성을 입증합니다.

## 🎯 주요 포인트

- 1. Simulation-Grounded Neural Networks(SGNNs)는 전적으로 기계적 시뮬레이션의 합성 데이터로 훈련된 예측 모델로, 제한된 실제 데이터 환경에서 최첨단 성능을 달성합니다.
- 2. SGNNs는 시뮬레이션 사전 하에서의 암시적 베이지안 추론을 구현하며, 베이즈 최적 예측기로 수렴합니다.
- 3. SGNNs는 경험적 방법으로는 학습할 수 없는 관찰 불가능한 과학적 양을 학습할 수 있으며, 모델의 해석 가능성을 기계적 시뮬레이션을 통해 과학적으로 설명할 수 있습니다.
- 4. SGNNs는 모델 선택 작업에서 AIC의 오류를 절반으로 줄이며, 데이터가 제한된 환경에서 과학적 예측을 위한 실용적 프레임워크로 자리 잡았습니다.


---

*Generated on 2025-09-24 14:57:59*