---
keywords:
  - Neural Network
  - Influence Function
  - Instruction Fine-Tuning
  - Subset Selection
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2502.09969
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:50:55.848536",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Influence Function",
    "Instruction Fine-Tuning",
    "Subset Selection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Influence Function": 0.8,
    "Instruction Fine-Tuning": 0.82,
    "Subset Selection": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "NN",
          "Neural Nets"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are fundamental to the paper's methodology and connect to a wide range of related concepts.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Influence Functions",
        "canonical": "Influence Function",
        "aliases": [
          "Influence Estimation"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's contribution, providing a unique perspective on model training insights.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.8
      },
      {
        "surface": "Instruction Fine-Tuning",
        "canonical": "Instruction Fine-Tuning",
        "aliases": [
          "Instruction Tuning"
        ],
        "category": "specific_connectable",
        "rationale": "A specific technique relevant to the paper's application and broader trends in model training.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Subset Selection",
        "canonical": "Subset Selection",
        "aliases": [
          "Data Subset Selection"
        ],
        "category": "unique_technical",
        "rationale": "A key application of the proposed method, relevant for optimizing training data usage.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.72,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "model training",
      "large models",
      "hyperparameter analyses"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Influence Functions",
      "resolved_canonical": "Influence Function",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Instruction Fine-Tuning",
      "resolved_canonical": "Instruction Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Subset Selection",
      "resolved_canonical": "Subset Selection",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.72,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data

**Korean Title:** 명령 세분화 데이터의 학습 가능하고 확장 가능한 영향 추정을 위한 신경망

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.09969.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2502.09969](https://arxiv.org/abs/2502.09969)

## 🔗 유사한 논문
- [[2025-09-22/Toward Efficient Influence Function_ Dropout as a Compression Tool_20250922|Toward Efficient Influence Function: Dropout as a Compression Tool]] (83.8% similar)
- [[2025-09-22/Targeted Fine-Tuning of DNN-Based Receivers via Influence Functions_20250922|Targeted Fine-Tuning of DNN-Based Receivers via Influence Functions]] (82.5% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (80.6% similar)
- [[2025-09-22/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250922|Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (80.5% similar)
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Instruction Fine-Tuning|Instruction Fine-Tuning]]
**⚡ Unique Technical**: [[keywords/Influence Function|Influence Function]], [[keywords/Subset Selection|Subset Selection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.09969v3 Announce Type: replace-cross 
Abstract: Influence functions provide crucial insights into model training, but existing methods suffer from large computational costs and limited generalization. Particularly, recent works have proposed various metrics and algorithms to calculate the influence of data using language models, which do not scale well with large models and datasets. This is because of the expensive forward and backward passes required for computation, substantial memory requirements to store large models, and poor generalization of influence estimates to new data. In this paper, we explore the use of small neural networks -- which we refer to as the InfluenceNetwork -- to estimate influence values, achieving up to 99% cost reduction. Our evaluation demonstrates that influence values can be estimated with models just 0.0027% the size of full language models (we use 7B and 8B versions). We apply our algorithm of estimating influence values (called NN-CIFT: Neural Networks for effiCient Instruction Fine-Tuning) to the downstream task of subset selection for general instruction fine-tuning. In our study, we include four state-of-the-art influence functions and show no compromise in performance, despite large speedups, between NN-CIFT and the original influence functions. We provide an in-depth hyperparameter analyses of NN-CIFT. The code for our method can be found here: https://github.com/agarwalishika/NN-CIFT.

## 🔍 Abstract (한글 번역)

arXiv:2502.09969v3 발표 유형: 교차 대체  
초록: 영향 함수는 모델 학습에 중요한 통찰을 제공하지만, 기존 방법은 큰 계산 비용과 제한된 일반화 문제를 겪고 있습니다. 특히, 최근 연구들은 언어 모델을 사용하여 데이터의 영향을 계산하기 위한 다양한 지표와 알고리즘을 제안했지만, 이는 대규모 모델과 데이터셋에 잘 확장되지 않습니다. 이는 계산을 위한 비싼 순방향 및 역방향 패스, 대규모 모델을 저장하기 위한 상당한 메모리 요구사항, 새로운 데이터에 대한 영향 추정의 낮은 일반화 때문입니다. 본 논문에서는 영향 값을 추정하기 위해 작은 신경망(InfluenceNetwork라 부름)을 사용하는 방법을 탐구하여 최대 99%의 비용 절감을 달성합니다. 우리의 평가에서는 전체 언어 모델 크기의 단 0.0027%에 불과한 모델로도 영향 값을 추정할 수 있음을 보여줍니다(7B 및 8B 버전을 사용). 우리는 일반적인 지시 세부 조정을 위한 하위 집합 선택의 다운스트림 작업에 영향 값 추정 알고리즘(NN-CIFT: Neural Networks for effiCient Instruction Fine-Tuning)을 적용합니다. 우리의 연구에서는 네 가지 최신 영향 함수를 포함하여 NN-CIFT와 원래 영향 함수 간의 성능 저하 없이 큰 속도 향상을 보여줍니다. 우리는 NN-CIFT의 하이퍼파라미터에 대한 심층 분석을 제공합니다. 우리의 방법에 대한 코드는 다음에서 찾을 수 있습니다: https://github.com/agarwalishika/NN-CIFT.

## 📝 요약

이 논문은 대규모 언어 모델에서 데이터의 영향을 효율적으로 추정하기 위해 작은 신경망인 InfluenceNetwork를 사용하는 방법을 제안합니다. 기존 방법들은 계산 비용이 크고 일반화가 제한적이었으나, 제안된 방법은 모델 크기의 0.0027%만으로도 영향을 추정할 수 있어 최대 99%의 비용 절감을 달성합니다. NN-CIFT 알고리즘을 통해 일반적인 지시 미세 조정을 위한 하위 집합 선택 작업에 적용했으며, 성능 저하 없이 속도를 크게 향상시켰습니다. 논문은 NN-CIFT의 하이퍼파라미터 분석을 포함하고 있으며, 관련 코드는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. 기존의 데이터 영향력 계산 방법은 큰 계산 비용과 일반화의 한계를 가지고 있다.
- 2. InfluenceNetwork라는 작은 신경망을 사용하여 영향력 값을 추정하면 최대 99%의 비용 절감이 가능하다.
- 3. 전체 언어 모델 크기의 0.0027%에 불과한 모델로도 영향력 값을 정확하게 추정할 수 있다.
- 4. NN-CIFT 알고리즘을 통해 일반 지침 미세 조정을 위한 하위 집합 선택 작업에서 성능 저하 없이 속도를 크게 향상시킬 수 있다.
- 5. NN-CIFT의 하이퍼파라미터에 대한 심층 분석을 제공하며, 관련 코드는 GitHub에서 제공된다.


---

*Generated on 2025-09-23 09:50:55*