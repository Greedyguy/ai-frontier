<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:38:49.293172",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Pseudo-Sample Matching",
    "Randomized Controlled Trials",
    "Observational Data Fusion",
    "Uplift Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Pseudo-Sample Matching": 0.78,
    "Randomized Controlled Trials": 0.72,
    "Observational Data Fusion": 0.75,
    "Uplift Models": 0.73
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Pseudo-Sample Matching",
        "canonical": "Pseudo-Sample Matching",
        "aliases": [
          "Pseudo Sample Matching",
          "PSM"
        ],
        "category": "unique_technical",
        "rationale": "This method is central to the paper's contribution and offers a novel approach to data fusion, enhancing connectivity with related data fusion techniques.",
        "novelty_score": 0.85,
        "connectivity_score": 0.67,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "Randomized Controlled Trials",
        "canonical": "Randomized Controlled Trials",
        "aliases": [
          "RCTs"
        ],
        "category": "broad_technical",
        "rationale": "RCTs are a fundamental concept in the paper and are widely used in experimental design, providing a strong link to related studies in experimental methodologies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Observational Data Fusion",
        "canonical": "Observational Data Fusion",
        "aliases": [
          "Data Fusion",
          "Observational Data Integration"
        ],
        "category": "specific_connectable",
        "rationale": "This concept is key to the paper's methodology, linking to broader data integration and fusion techniques in industrial applications.",
        "novelty_score": 0.68,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      },
      {
        "surface": "Uplift Models",
        "canonical": "Uplift Models",
        "aliases": [
          "Uplift Modeling"
        ],
        "category": "specific_connectable",
        "rationale": "Uplift models are crucial for assessing treatment effects, providing a connection to predictive modeling techniques in marketing and economics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.84,
        "specificity_score": 0.7,
        "link_intent_score": 0.73
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "data quality",
      "improvement"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Pseudo-Sample Matching",
      "resolved_canonical": "Pseudo-Sample Matching",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.67,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Randomized Controlled Trials",
      "resolved_canonical": "Randomized Controlled Trials",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Observational Data Fusion",
      "resolved_canonical": "Observational Data Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Uplift Models",
      "resolved_canonical": "Uplift Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.84,
        "specificity": 0.7,
        "link_intent": 0.73
      }
    }
  ]
}
-->

# Augmenting Limited and Biased RCTs through Pseudo-Sample Matching-Based Observational Data Fusion Method

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18148.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18148](https://arxiv.org/abs/2509.18148)

## 🔗 유사한 논문
- [[2025-09-22/TSCAN_ Context-Aware Uplift Modeling via Two-Stage Training for Online Merchant Business Diagnosis_20250922|TSCAN: Context-Aware Uplift Modeling via Two-Stage Training for Online Merchant Business Diagnosis]] (81.5% similar)
- [[2025-09-23/RIFT_ Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation_20250923|RIFT: Group-Relative RL Fine-Tuning for Realistic and Controllable Traffic Simulation]] (80.7% similar)
- [[2025-09-19/MetaTrading_ An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services_20250919|MetaTrading: An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services]] (79.8% similar)
- [[2025-09-23/CEBench_ A Benchmarking Toolkit for the Cost-Effectiveness of LLM Pipelines_20250923|CEBench: A Benchmarking Toolkit for the Cost-Effectiveness of LLM Pipelines]] (79.6% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Randomized Controlled Trials|Randomized Controlled Trials]]
**🔗 Specific Connectable**: [[keywords/Observational Data Fusion|Observational Data Fusion]], [[keywords/Uplift Models|Uplift Models]]
**⚡ Unique Technical**: [[keywords/Pseudo-Sample Matching|Pseudo-Sample Matching]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18148v1 Announce Type: cross 
Abstract: In the online ride-hailing pricing context, companies often conduct randomized controlled trials (RCTs) and utilize uplift models to assess the effect of discounts on customer orders, which substantially influences competitive market outcomes. However, due to the high cost of RCTs, the proportion of trial data relative to observational data is small, which only accounts for 0.65\% of total traffic in our context, resulting in significant bias when generalizing to the broader user base. Additionally, the complexity of industrial processes reduces the quality of RCT data, which is often subject to heterogeneity from potential interference and selection bias, making it difficult to correct. Moreover, existing data fusion methods are challenging to implement effectively in complex industrial settings due to the high dimensionality of features and the strict assumptions that are hard to verify with real-world data. To address these issues, we propose an empirical data fusion method called pseudo-sample matching. By generating pseudo-samples from biased, low-quality RCT data and matching them with the most similar samples from large-scale observational data, the method expands the RCT dataset while mitigating its heterogeneity. We validated the method through simulation experiments, conducted offline and online tests using real-world data. In a week-long online experiment, we achieved a 0.41\% improvement in profit, which is a considerable gain when scaled to industrial scenarios with hundreds of millions in revenue. In addition, we discuss the harm to model training, offline evaluation, and online economic benefits when the RCT data quality is not high, and emphasize the importance of improving RCT data quality in industrial scenarios. Further details of the simulation experiments can be found in the GitHub repository https://github.com/Kairong-Han/Pseudo-Matching.

## 📝 요약

이 논문은 온라인 승차 호출 서비스의 가격 책정에서 할인 효과를 평가하기 위해 사용되는 무작위 대조 실험(RCT)의 한계를 극복하기 위한 새로운 데이터 융합 방법론을 제안합니다. 기존 RCT 데이터는 비용 문제로 전체 데이터의 0.65%에 불과해 일반화에 편향이 발생하며, 산업적 복잡성으로 인해 데이터 품질이 저하됩니다. 이를 해결하기 위해 저자는 편향된 RCT 데이터를 기반으로 유사한 대규모 관찰 데이터를 매칭하는 '가상 샘플 매칭' 방법을 제안했습니다. 이 방법은 RCT 데이터의 이질성을 줄이고 데이터셋을 확장합니다. 시뮬레이션 실험과 실제 데이터를 통한 테스트 결과, 일주일간의 온라인 실험에서 0.41%의 수익 개선을 달성했습니다. 이는 대규모 산업 환경에서 상당한 이익을 의미합니다. 연구는 RCT 데이터 품질 향상의 중요성을 강조하며, 관련 실험 세부사항은 GitHub에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. 온라인 승차 호출 서비스에서 할인 효과를 평가하기 위해 무작위 대조 실험(RCT)과 업리프트 모델이 사용되지만, RCT의 높은 비용으로 인해 실험 데이터의 비율이 낮아 일반화에 편향이 발생합니다.
- 2. 산업적 프로세스의 복잡성으로 인해 RCT 데이터의 품질이 저하되며, 이로 인한 이질성과 선택 편향을 수정하기 어렵습니다.
- 3. 기존 데이터 융합 방법은 높은 차원의 특징과 엄격한 가정 때문에 복잡한 산업 환경에서 효과적으로 구현하기 어렵습니다.
- 4. 제안된 경험적 데이터 융합 방법인 가상 샘플 매칭은 편향된 저품질 RCT 데이터로부터 가상 샘플을 생성하고 대규모 관찰 데이터와 매칭하여 RCT 데이터셋을 확장하고 이질성을 완화합니다.
- 5. 실제 데이터로 진행한 온라인 실험에서 수익이 0.41% 개선되었으며, 이는 수백만 달러의 수익이 발생하는 산업 시나리오에서 상당한 이익입니다.


---

*Generated on 2025-09-24 13:38:49*