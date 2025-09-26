<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:38:21.203316",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Hierarchical Evaluation Function",
    "Demand Forecasting",
    "Grid Search",
    "Particle Swarm Optimization",
    "Optuna"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Hierarchical Evaluation Function": 0.78,
    "Demand Forecasting": 0.8,
    "Grid Search": 0.75,
    "Particle Swarm Optimization": 0.77,
    "Optuna": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hierarchical Evaluation Function",
        "canonical": "Hierarchical Evaluation Function",
        "aliases": [
          "HEF"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach for evaluating demand forecasting models, enhancing model selection and optimization.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Demand Forecasting",
        "canonical": "Demand Forecasting",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A central theme of the paper, relevant for linking to inventory management and optimization discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Grid Search",
        "canonical": "Grid Search",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A common optimization technique, linking to discussions on hyperparameter tuning in machine learning.",
        "novelty_score": 0.4,
        "connectivity_score": 0.78,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      },
      {
        "surface": "Particle Swarm Optimization",
        "canonical": "Particle Swarm Optimization",
        "aliases": [
          "PSO"
        ],
        "category": "specific_connectable",
        "rationale": "A specific optimization algorithm, providing a link to evolutionary computation methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Optuna",
        "canonical": "Optuna",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A modern hyperparameter optimization framework, relevant for linking to advanced optimization techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "Mean Absolute Error",
      "Root Mean Squared Error",
      "R2"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Hierarchical Evaluation Function",
      "resolved_canonical": "Hierarchical Evaluation Function",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Demand Forecasting",
      "resolved_canonical": "Demand Forecasting",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Grid Search",
      "resolved_canonical": "Grid Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.78,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Particle Swarm Optimization",
      "resolved_canonical": "Particle Swarm Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Optuna",
      "resolved_canonical": "Optuna",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Hierarchical Evaluation Function: A Multi-Metric Approach for Optimizing Demand Forecasting Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.13057.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2508.13057](https://arxiv.org/abs/2508.13057)

## 🔗 유사한 논문
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (80.6% similar)
- [[2025-09-22/Improving the forecast accuracy of wind power by leveraging multiple hierarchical structure_20250922|Improving the forecast accuracy of wind power by leveraging multiple hierarchical structure]] (80.6% similar)
- [[2025-09-22/Multi-modal Adaptive Estimation for Temporal Respiratory Disease Outbreak_20250922|Multi-modal Adaptive Estimation for Temporal Respiratory Disease Outbreak]] (79.4% similar)
- [[2025-09-23/MoEs Are Stronger than You Think_ Hyper-Parallel Inference Scaling with RoE_20250923|MoEs Are Stronger than You Think: Hyper-Parallel Inference Scaling with RoE]] (79.3% similar)
- [[2025-09-23/MIRA_ Medical Time Series Foundation Model for Real-World Health Data_20250923|MIRA: Medical Time Series Foundation Model for Real-World Health Data]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Demand Forecasting|Demand Forecasting]]
**🔗 Specific Connectable**: [[keywords/Grid Search|Grid Search]], [[keywords/Particle Swarm Optimization|Particle Swarm Optimization]], [[keywords/Optuna|Optuna]]
**⚡ Unique Technical**: [[keywords/Hierarchical Evaluation Function|Hierarchical Evaluation Function]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.13057v4 Announce Type: replace-cross 
Abstract: Accurate demand forecasting is crucial for effective inventory management in dynamic and competitive environments, where decisions are influenced by uncertainty, financial constraints, and logistical limitations. Traditional evaluation metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) provide complementary perspectives but may lead to biased assessments when applied individually. To address this limitation, we propose the Hierarchical Evaluation Function (HEF), a composite function that integrates R2, MAE, and RMSE within a hierarchical and adaptive framework. The function incorporates dynamic weights, tolerance thresholds derived from the statistical properties of the series, and progressive penalty mechanisms to ensure robustness against extreme errors and invalid predictions. HEF was implemented to optimize multiple forecasting models using Grid Search, Particle Swarm Optimization (PSO), and Optuna, and tested on benchmark datasets including Walmart, M3, M4, and M5. Experimental results, validated through statistical tests, demonstrate that HEF consistently outperforms MAE as an evaluation function in global metrics such as R2, Global Relative Accuracy (GRA), RMSE, and RMSSE, thereby providing greater explanatory power, adaptability, and stability. While MAE retains advantages in simplicity and efficiency, HEF proves more effective for long-term planning and complex contexts. Overall, HEF constitutes a robust and adaptive alternative for model selection and hyperparameter optimization in highly variable demand forecasting environments.

## 📝 요약

정확한 수요 예측은 동적이고 경쟁적인 환경에서 효과적인 재고 관리에 필수적입니다. 기존의 평가 지표인 MAE와 RMSE는 보완적이지만, 개별적으로 사용 시 편향된 평가를 초래할 수 있습니다. 이를 해결하기 위해, 본 연구는 R2, MAE, RMSE를 통합한 계층적 평가 함수(HEF)를 제안합니다. HEF는 동적 가중치와 통계적 속성에 기반한 허용 임계값, 점진적 페널티 메커니즘을 포함하여 극단적 오류와 잘못된 예측에 대한 강건성을 보장합니다. HEF는 다양한 예측 모델을 최적화하는 데 사용되었으며, 실험 결과 MAE보다 전반적으로 우수한 성능을 보였습니다. HEF는 장기 계획 및 복잡한 상황에서 더 효과적인 대안으로, 수요 예측 환경에서 모델 선택 및 하이퍼파라미터 최적화에 유용합니다.

## 🎯 주요 포인트

- 1. 정확한 수요 예측은 동적이고 경쟁적인 환경에서 효과적인 재고 관리에 필수적입니다.
- 2. 전통적인 평가 지표인 MAE와 RMSE는 보완적인 관점을 제공하지만 개별적으로 적용할 경우 편향된 평가로 이어질 수 있습니다.
- 3. 제안된 계층적 평가 함수(HEF)는 R2, MAE, RMSE를 통합하여 계층적이고 적응적인 프레임워크를 제공합니다.
- 4. HEF는 Walmart, M3, M4, M5와 같은 벤치마크 데이터셋에서 테스트되었으며, MAE보다 글로벌 지표에서 일관되게 우수한 성능을 보였습니다.
- 5. HEF는 복잡한 환경과 장기 계획에서 더 효과적이며, 모델 선택과 하이퍼파라미터 최적화에 강력하고 적응적인 대안을 제공합니다.


---

*Generated on 2025-09-24 14:38:21*