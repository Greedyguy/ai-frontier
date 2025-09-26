<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:31:29.753286",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Predictive Process Monitoring",
    "Deep Learning",
    "Event Log",
    "Remaining Time Prediction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Predictive Process Monitoring": 0.75,
    "Deep Learning": 0.8,
    "Event Log": 0.7,
    "Remaining Time Prediction": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Predictive process monitoring",
        "canonical": "Predictive Process Monitoring",
        "aliases": [
          "Process Monitoring",
          "Predictive Monitoring"
        ],
        "category": "unique_technical",
        "rationale": "It is a specific sub-domain of process mining relevant to the paper's focus on forecasting.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Deep learning models",
        "canonical": "Deep Learning",
        "aliases": [
          "DL",
          "Deep Neural Networks"
        ],
        "category": "broad_technical",
        "rationale": "Deep learning is a key method used in the paper, linking to broader machine learning concepts.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "Event log",
        "canonical": "Event Log",
        "aliases": [
          "Process Log",
          "Execution Log"
        ],
        "category": "unique_technical",
        "rationale": "Event logs are critical data sources for process mining, central to the study's methodology.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      },
      {
        "surface": "Remaining time prediction",
        "canonical": "Remaining Time Prediction",
        "aliases": [
          "Time Prediction",
          "Duration Forecasting"
        ],
        "category": "unique_technical",
        "rationale": "This is the primary prediction target in the study, crucial for understanding the research focus.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "logistics company",
      "aviation business",
      "computational resources"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Predictive process monitoring",
      "resolved_canonical": "Predictive Process Monitoring",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Deep learning models",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Event log",
      "resolved_canonical": "Event Log",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Remaining time prediction",
      "resolved_canonical": "Remaining Time Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Remaining Time Prediction in Outbound Warehouse Processes: A Case Study (Short Paper)

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18986.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18986](https://arxiv.org/abs/2509.18986)

## 🔗 유사한 논문
- [[2025-09-23/On the Simplification of Neural Network Architectures for Predictive Process Monitoring_20250923|On the Simplification of Neural Network Architectures for Predictive Process Monitoring]] (83.1% similar)
- [[2025-09-18/Predicting Case Suffixes With Activity Start and End Times_ A Sweep-Line Based Approach_20250918|Predicting Case Suffixes With Activity Start and End Times: A Sweep-Line Based Approach]] (82.0% similar)
- [[2025-09-23/Time Series Forecasting Using a Hybrid Deep Learning Method_ A Bi-LSTM Embedding Denoising Auto Encoder Transformer_20250923|Time Series Forecasting Using a Hybrid Deep Learning Method: A Bi-LSTM Embedding Denoising Auto Encoder Transformer]] (79.3% similar)
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (79.0% similar)
- [[2025-09-22/Learning to Optimize Capacity Planning in Semiconductor Manufacturing_20250922|Learning to Optimize Capacity Planning in Semiconductor Manufacturing]] (78.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**⚡ Unique Technical**: [[keywords/Predictive Process Monitoring|Predictive Process Monitoring]], [[keywords/Event Log|Event Log]], [[keywords/Remaining Time Prediction|Remaining Time Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18986v1 Announce Type: new 
Abstract: Predictive process monitoring is a sub-domain of process mining which aims to forecast the future of ongoing process executions. One common prediction target is the remaining time, meaning the time that will elapse until a process execution is completed. In this paper, we compare four different remaining time prediction approaches in a real-life outbound warehouse process of a logistics company in the aviation business. For this process, the company provided us with a novel and original event log with 169,523 traces, which we can make publicly available. Unsurprisingly, we find that deep learning models achieve the highest accuracy, but shallow methods like conventional boosting techniques achieve competitive accuracy and require significantly fewer computational resources.

## 📝 요약

이 논문은 프로세스 마이닝의 하위 분야인 예측 프로세스 모니터링을 다루며, 특히 진행 중인 프로세스의 남은 시간을 예측하는 방법을 비교합니다. 항공 물류 회사의 실생활 아웃바운드 창고 프로세스를 대상으로 169,523개의 트레이스를 포함한 새로운 이벤트 로그를 사용하여 네 가지 남은 시간 예측 방법을 비교했습니다. 연구 결과, 딥러닝 모델이 가장 높은 정확도를 보였지만, 전통적인 부스팅 기법과 같은 얕은 방법도 경쟁력 있는 정확도를 제공하며 적은 계산 자원을 필요로 한다는 것을 발견했습니다.

## 🎯 주요 포인트

- 1. 예측 프로세스 모니터링은 진행 중인 프로세스 실행의 미래를 예측하는 프로세스 마이닝의 하위 분야이다.
- 2. 남은 시간 예측은 프로세스 실행이 완료될 때까지 경과할 시간을 예측하는 일반적인 목표이다.
- 3. 본 논문에서는 항공 물류 회사의 실생활 아웃바운드 창고 프로세스에서 네 가지 다른 남은 시간 예측 방법을 비교하였다.
- 4. 연구에 사용된 이벤트 로그는 169,523개의 트레이스를 포함하며, 공개적으로 이용 가능하다.
- 5. 딥러닝 모델이 가장 높은 정확도를 달성했지만, 기존의 부스팅 기법과 같은 얕은 방법도 경쟁력 있는 정확도를 보이며, 계산 자원이 적게 소모된다.


---

*Generated on 2025-09-24 13:31:29*