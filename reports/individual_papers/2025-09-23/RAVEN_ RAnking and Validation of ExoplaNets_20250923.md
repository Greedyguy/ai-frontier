---
keywords:
  - RAVEN Pipeline
  - Transiting Exoplanet Survey Satellite
  - Bayesian Framework
  - Gradient Boosted Decision Tree
  - Gaussian Process Classifier
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17645
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:25:09.203331",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "RAVEN Pipeline",
    "Transiting Exoplanet Survey Satellite",
    "Bayesian Framework",
    "Gradient Boosted Decision Tree",
    "Gaussian Process Classifier"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "RAVEN Pipeline": 0.88,
    "Transiting Exoplanet Survey Satellite": 0.85,
    "Bayesian Framework": 0.82,
    "Gradient Boosted Decision Tree": 0.8,
    "Gaussian Process Classifier": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "RAVEN",
        "canonical": "RAVEN Pipeline",
        "aliases": [
          "RAVEN"
        ],
        "category": "unique_technical",
        "rationale": "RAVEN is a unique pipeline specifically developed for TESS exoplanet candidate validation, offering a distinct contribution to exoplanet research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "TESS",
        "canonical": "Transiting Exoplanet Survey Satellite",
        "aliases": [
          "TESS"
        ],
        "category": "specific_connectable",
        "rationale": "TESS is a significant mission in exoplanet discovery, providing a common ground for linking related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.92,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Bayesian framework",
        "canonical": "Bayesian Framework",
        "aliases": [
          "Bayesian method"
        ],
        "category": "broad_technical",
        "rationale": "The Bayesian framework is a widely used statistical approach, connecting various applications in data analysis.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Gradient Boosted Decision Tree",
        "canonical": "Gradient Boosted Decision Tree",
        "aliases": [
          "GBDT"
        ],
        "category": "specific_connectable",
        "rationale": "This machine learning model is crucial for the classification tasks in the pipeline, linking to broader ML applications.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Gaussian Process classifier",
        "canonical": "Gaussian Process Classifier",
        "aliases": [
          "GP classifier"
        ],
        "category": "specific_connectable",
        "rationale": "The Gaussian Process classifier is a sophisticated model for probabilistic classification, relevant to advanced ML techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.83,
        "specificity_score": 0.78,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "vetting",
      "validation",
      "performance",
      "candidates"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "RAVEN",
      "resolved_canonical": "RAVEN Pipeline",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "TESS",
      "resolved_canonical": "Transiting Exoplanet Survey Satellite",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.92,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Bayesian framework",
      "resolved_canonical": "Bayesian Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Gradient Boosted Decision Tree",
      "resolved_canonical": "Gradient Boosted Decision Tree",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Gaussian Process classifier",
      "resolved_canonical": "Gaussian Process Classifier",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.83,
        "specificity": 0.78,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# RAVEN: RAnking and Validation of ExoplaNets

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17645.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17645](https://arxiv.org/abs/2509.17645)

## 🔗 유사한 논문
- [[2025-09-22/TESSERA_ Precomputed FAIR Global Pixel Embeddings for Earth Representation and Analysis_20250922|TESSERA: Precomputed FAIR Global Pixel Embeddings for Earth Representation and Analysis]] (76.6% similar)
- [[2025-09-22/RAVE_ Retrieval and Scoring Aware Verifiable Claim Detection_20250922|RAVE: Retrieval and Scoring Aware Verifiable Claim Detection]] (75.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Bayesian Framework|Bayesian Framework]]
**🔗 Specific Connectable**: [[keywords/Transiting Exoplanet Survey Satellite|Transiting Exoplanet Survey Satellite]], [[keywords/Gradient Boosted Decision Tree|Gradient Boosted Decision Tree]], [[keywords/Gaussian Process Classifier|Gaussian Process Classifier]]
**⚡ Unique Technical**: [[keywords/RAVEN Pipeline|RAVEN Pipeline]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17645v1 Announce Type: cross 
Abstract: We present RAVEN, a newly developed vetting and validation pipeline for TESS exoplanet candidates. The pipeline employs a Bayesian framework to derive the posterior probability of a candidate being a planet against a set of False Positive (FP) scenarios, through the use of a Gradient Boosted Decision Tree and a Gaussian Process classifier, trained on comprehensive synthetic training sets of simulated planets and 8 astrophysical FP scenarios injected into TESS lightcurves. These training sets allow large scale candidate vetting and performance verification against individual FP scenarios. A Non-Simulated FP training set consisting of real TESS candidates caused primarily by stellar variability and systematic noise is also included. The machine learning derived probabilities are combined with scenario specific prior probabilities, including the candidates' positional probabilities, to compute the final posterior probabilities. Candidates with a planetary posterior probability greater than 99% against each FP scenario and whose implied planetary radius is less than 8$R_{\oplus}$ are considered to be statistically validated by the pipeline. In this first version, the pipeline has been developed for candidates with a lightcurve released from the TESS Science Processing Operations Centre, an orbital period between 0.5 and 16 days and a transit depth greater than 300ppm. The pipeline obtained area-under-curve (AUC) scores > 97% on all FP scenarios and > 99% on all but one. Testing on an independent external sample of 1361 pre-classified TOIs, the pipeline achieved an overall accuracy of 91%, demonstrating its effectiveness for automated ranking of TESS candidates. For a probability threshold of 0.9 the pipeline reached a precision of 97% with a recall score of 66% on these TOIs. The RAVEN pipeline is publicly released as a cloud-hosted app, making it easily accessible to the community.

## 📝 요약

RAVEN은 TESS 외계행성 후보를 검증하고 확인하기 위한 새로운 파이프라인으로, 베이지안 프레임워크를 사용하여 후보가 행성일 확률을 계산합니다. 이 과정에서 Gradient Boosted Decision Tree와 Gaussian Process 분류기를 활용하며, 이는 TESS 광도곡선에 주입된 가상의 행성과 8가지 천체 물리학적 오탐지(FP) 시나리오로 훈련됩니다. 또한, 실제 TESS 후보로 구성된 비모의 FP 훈련 세트도 포함됩니다. RAVEN은 후보의 위치 확률 등 시나리오별 사전 확률을 결합하여 최종 확률을 산출하며, 특정 기준을 충족하는 후보를 통계적으로 검증합니다. 첫 버전은 특정 궤도 주기와 통과 깊이를 가진 후보에 적용되며, 모든 FP 시나리오에서 97% 이상의 AUC 점수를 기록했습니다. 독립적인 샘플에서 91%의 정확도를 보였으며, 0.9의 확률 임계값에서 97%의 정밀도와 66%의 재현율을 달성했습니다. RAVEN은 클라우드 기반 앱으로 공개되어 쉽게 접근 가능합니다.

## 🎯 주요 포인트

- 1. RAVEN은 TESS 외계행성 후보를 검증하고 확인하기 위한 새로운 파이프라인으로, 베이지안 프레임워크를 사용하여 후보가 행성일 확률을 계산합니다.
- 2. 이 파이프라인은 Gradient Boosted Decision Tree와 Gaussian Process 분류기를 활용하여 TESS 광도곡선에 주입된 8가지 천체물리학적 거짓 양성(FP) 시나리오와 모의 행성으로 구성된 종합적인 합성 훈련 세트로 훈련됩니다.
- 3. RAVEN은 행성 후광 확률이 99% 이상이고 행성 반경이 8지구 반경 이하인 후보를 통계적으로 검증된 것으로 간주합니다.
- 4. 이 파이프라인은 TESS Science Processing Operations Centre에서 제공하는 광도곡선, 궤도 주기 0.5~16일, 통과 깊이 300ppm 이상인 후보에 대해 개발되었습니다.
- 5. RAVEN은 독립적인 외부 샘플에서 91%의 정확도를 달성했으며, 클라우드 기반 앱으로 공개되어 커뮤니티에서 쉽게 접근할 수 있습니다.


---

*Generated on 2025-09-24 02:25:09*