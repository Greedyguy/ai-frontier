---
keywords:
  - Graph Neural Network
  - Anomaly Detection
  - Sensor Networks
  - Adversarial Attack
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17987
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:00:36.095113",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Anomaly Detection",
    "Sensor Networks",
    "Adversarial Attack"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.95,
    "Anomaly Detection": 0.8,
    "Sensor Networks": 0.82,
    "Adversarial Attack": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Networks",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN",
          "Graph Networks"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's theme, linking to existing research on GNNs enhances connectivity.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.95
      },
      {
        "surface": "anomaly detection",
        "canonical": "Anomaly Detection",
        "aliases": [
          "outlier detection",
          "anomaly recognition"
        ],
        "category": "broad_technical",
        "rationale": "A core application area that connects to broader machine learning and security topics.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "sensor networks",
        "canonical": "Sensor Networks",
        "aliases": [
          "sensor systems",
          "networked sensors"
        ],
        "category": "specific_connectable",
        "rationale": "Key context for the study, linking to IoT and network analysis fields.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "adversarial attack",
        "canonical": "Adversarial Attack",
        "aliases": [
          "adversarial perturbation",
          "attack strategy"
        ],
        "category": "unique_technical",
        "rationale": "Specific to the study's method, connecting to security and robustness research.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
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
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.95
      }
    },
    {
      "candidate_surface": "anomaly detection",
      "resolved_canonical": "Anomaly Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "sensor networks",
      "resolved_canonical": "Sensor Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "adversarial attack",
      "resolved_canonical": "Adversarial Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# Budgeted Adversarial Attack against Graph-Based Anomaly Detection in Sensor Networks

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17987.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17987](https://arxiv.org/abs/2509.17987)

## 🔗 유사한 논문
- [[2025-09-23/Train to Defend_ First Defense Against Cryptanalytic Neural Network Parameter Extraction Attacks_20250923|Train to Defend: First Defense Against Cryptanalytic Neural Network Parameter Extraction Attacks]] (82.0% similar)
- [[2025-09-17/Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations_20250917|Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations]] (81.4% similar)
- [[2025-09-22/GIN-Graph_ A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks_20250922|GIN-Graph: A Generative Interpretation Network for Model-Level Explanation of Graph Neural Networks]] (81.2% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (81.2% similar)
- [[2025-09-22/EvoBrain_ Dynamic Multi-channel EEG Graph Modeling for Time-evolving Brain Network_20250922|EvoBrain: Dynamic Multi-channel EEG Graph Modeling for Time-evolving Brain Network]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Anomaly Detection|Anomaly Detection]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]], [[keywords/Sensor Networks|Sensor Networks]]
**⚡ Unique Technical**: [[keywords/Adversarial Attack|Adversarial Attack]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17987v1 Announce Type: new 
Abstract: Graph Neural Networks (GNNs) have emerged as powerful models for anomaly detection in sensor networks, particularly when analyzing multivariate time series. In this work, we introduce BETA, a novel grey-box evasion attack targeting such GNN-based detectors, where the attacker is constrained to perturb sensor readings from a limited set of nodes, excluding the target sensor, with the goal of either suppressing a true anomaly or triggering a false alarm at the target node. BETA identifies the sensors most influential to the target node's classification and injects carefully crafted adversarial perturbations into their features, all while maintaining stealth and respecting the attacker's budget. Experiments on three real-world sensor network datasets show that BETA reduces the detection accuracy of state-of-the-art GNN-based detectors by 30.62 to 39.16% on average, and significantly outperforms baseline attack strategies, while operating within realistic constraints.

## 📝 요약

이 연구는 센서 네트워크의 이상 탐지를 위한 그래프 신경망(GNN) 기반 모델을 대상으로 하는 새로운 회피 공격 기법인 BETA를 소개합니다. BETA는 제한된 노드 집합에서 센서 데이터를 교란하여 목표 노드에서의 이상 탐지를 억제하거나 잘못된 경보를 유발하는 것을 목표로 합니다. 이 공격은 목표 노드의 분류에 가장 큰 영향을 미치는 센서를 식별하고, 이들의 특징에 정교하게 설계된 적대적 교란을 주입합니다. 실험 결과, BETA는 최신 GNN 기반 탐지기의 정확도를 평균 30.62%에서 39.16%까지 감소시키며, 현실적인 제약 내에서 기존 공격 전략보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. BETA는 GNN 기반의 이상 탐지기를 대상으로 하는 새로운 회색 상자 회피 공격 기법입니다.
- 2. 공격자는 제한된 노드 집합에서 센서 판독값을 변형하여 목표 노드에서의 이상 탐지를 억제하거나 잘못된 경보를 유발합니다.
- 3. BETA는 목표 노드의 분류에 가장 영향을 미치는 센서를 식별하고, 정교하게 설계된 적대적 변형을 주입합니다.
- 4. 실험 결과, BETA는 최첨단 GNN 기반 탐지기의 탐지 정확도를 평균 30.62%에서 39.16%까지 감소시킵니다.
- 5. BETA는 현실적인 제약 내에서 기존의 공격 전략보다 뛰어난 성능을 보입니다.


---

*Generated on 2025-09-24 02:00:36*