---
keywords:
  - Transformer
  - FairTune
  - Group Distributionally Robust Optimization
  - Adversarial Debiasing
  - Photoplethysmography
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16491
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:37:26.090478",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "FairTune",
    "Group Distributionally Robust Optimization",
    "Adversarial Debiasing",
    "Photoplethysmography"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "FairTune": 0.8,
    "Group Distributionally Robust Optimization": 0.78,
    "Adversarial Debiasing": 0.77,
    "Photoplethysmography": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Transformer-based foundation model",
        "canonical": "Transformer",
        "aliases": [
          "Transformer model"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are a fundamental architecture in deep learning, crucial for linking with other models and techniques.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "FairTune",
        "canonical": "FairTune",
        "aliases": [
          "bias-aware fine-tuning framework"
        ],
        "category": "unique_technical",
        "rationale": "FairTune is a novel framework specifically designed for bias mitigation in heart rate prediction models.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Group Distributionally Robust Optimization",
        "canonical": "Group Distributionally Robust Optimization",
        "aliases": [
          "GroupDRO"
        ],
        "category": "specific_connectable",
        "rationale": "GroupDRO is a specific technique for fairness optimization, linking to broader discussions on robust optimization methods.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Adversarial debiasing",
        "canonical": "Adversarial Debiasing",
        "aliases": [
          "ADV"
        ],
        "category": "specific_connectable",
        "rationale": "Adversarial debiasing is a key method for reducing bias in models, connecting to adversarial learning techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "Photoplethysmography signals",
        "canonical": "Photoplethysmography",
        "aliases": [
          "PPG signals"
        ],
        "category": "specific_connectable",
        "rationale": "Photoplethysmography is central to the study, linking to other physiological signal processing research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "fine-tuning",
      "mean absolute error",
      "demographic fairness"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Transformer-based foundation model",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "FairTune",
      "resolved_canonical": "FairTune",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Group Distributionally Robust Optimization",
      "resolved_canonical": "Group Distributionally Robust Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Adversarial debiasing",
      "resolved_canonical": "Adversarial Debiasing",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Photoplethysmography signals",
      "resolved_canonical": "Photoplethysmography",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# FairTune: A Bias-Aware Fine-Tuning Framework Towards Fair Heart Rate Prediction from PPG

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16491.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16491](https://arxiv.org/abs/2509.16491)

## 🔗 유사한 논문
- [[2025-09-23/Estimating Clinical Lab Test Result Trajectories from PPG using Physiological Foundation Model and Patient-Aware State Space Model -- a UNIPHY+ Approach_20250923|Estimating Clinical Lab Test Result Trajectories from PPG using Physiological Foundation Model and Patient-Aware State Space Model -- a UNIPHY+ Approach]] (82.3% similar)
- [[2025-09-17/APFEx_ Adaptive Pareto Front Explorer for Intersectional Fairness_20250917|APFEx: Adaptive Pareto Front Explorer for Intersectional Fairness]] (81.4% similar)
- [[2025-09-22/Deep learning and abstractive summarisation for radiological reports_ an empirical study for adapting the PEGASUS models' family with scarce data_20250922|Deep learning and abstractive summarisation for radiological reports: an empirical study for adapting the PEGASUS models' family with scarce data]] (81.3% similar)
- [[2025-09-22/Where Fact Ends and Fairness Begins_ Redefining AI Bias Evaluation through Cognitive Biases_20250922|Where Fact Ends and Fairness Begins: Redefining AI Bias Evaluation through Cognitive Biases]] (81.1% similar)
- [[2025-09-22/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250922|Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Group Distributionally Robust Optimization|Group Distributionally Robust Optimization]], [[keywords/Adversarial Debiasing|Adversarial Debiasing]], [[keywords/Photoplethysmography|Photoplethysmography]]
**⚡ Unique Technical**: [[keywords/FairTune|FairTune]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16491v1 Announce Type: new 
Abstract: Foundation models pretrained on physiological data such as photoplethysmography (PPG) signals are increasingly used to improve heart rate (HR) prediction across diverse settings. Fine-tuning these models for local deployment is often seen as a practical and scalable strategy. However, its impact on demographic fairness particularly under domain shifts remains underexplored. We fine-tune PPG-GPT a transformer-based foundation model pretrained on intensive care unit (ICU) data across three heterogeneous datasets (ICU, wearable, smartphone) and systematically evaluate the effects on HR prediction accuracy and gender fairness. While fine-tuning substantially reduces mean absolute error (up to 80%), it can simultaneously widen fairness gaps, especially in larger models and under significant distributional characteristics shifts. To address this, we introduce FairTune, a bias-aware fine-tuning framework in which we benchmark three mitigation strategies: class weighting based on inverse group frequency (IF), Group Distributionally Robust Optimization (GroupDRO), and adversarial debiasing (ADV). We find that IF and GroupDRO significantly reduce fairness gaps without compromising accuracy, with effectiveness varying by deployment domain. Representation analyses further reveal that mitigation techniques reshape internal embeddings to reduce demographic clustering. Our findings highlight that fairness does not emerge as a natural byproduct of fine-tuning and that explicit mitigation is essential for equitable deployment of physiological foundation models.

## 📝 요약

이 논문은 광혈류측정(PPG) 신호를 기반으로 심박수 예측을 개선하기 위해 사전 학습된 기초 모델의 미세 조정이 인구통계학적 공정성에 미치는 영향을 탐구합니다. 연구에서는 ICU, 웨어러블, 스마트폰 데이터셋에서 PPG-GPT 모델을 미세 조정하여 심박수 예측 정확도와 성별 공정성을 평가했습니다. 미세 조정은 평균 절대 오차를 최대 80%까지 줄였지만, 공정성 격차를 확대할 수 있음을 발견했습니다. 이를 해결하기 위해 FairTune이라는 편향 인식 미세 조정 프레임워크를 제안하고, 역 그룹 빈도 기반 클래스 가중치(IF), 그룹 분포적 강건 최적화(GroupDRO), 적대적 디바이싱(ADV) 등 세 가지 완화 전략을 비교했습니다. IF와 GroupDRO는 정확성을 유지하면서 공정성 격차를 줄이는 데 효과적이었으며, 배포 도메인에 따라 효과가 달라졌습니다. 연구 결과는 공정성이 미세 조정의 자연스러운 결과로 나타나지 않으며, 명시적인 완화가 필요함을 강조합니다.

## 🎯 주요 포인트

- 1. PPG 신호와 같은 생리학적 데이터로 사전 학습된 기초 모델은 다양한 환경에서 심박수 예측을 개선하는 데 사용된다.
- 2. 세 가지 이질적인 데이터셋에서 PPG-GPT 모델을 미세 조정하여 심박수 예측 정확성과 성별 공정성에 미치는 영향을 평가하였다.
- 3. 미세 조정은 평균 절대 오차를 최대 80%까지 줄일 수 있지만, 공정성 격차를 확대할 수 있다.
- 4. FairTune이라는 편향 인식 미세 조정 프레임워크를 도입하여 세 가지 완화 전략을 벤치마킹하였다.
- 5. IF와 GroupDRO는 정확성을 유지하면서 공정성 격차를 크게 줄이는 것으로 나타났다.


---

*Generated on 2025-09-24 01:37:26*