---
keywords:
  - FRAUDGUESS
  - Micro-Clusters
  - Interactive Dashboard
  - Heatmaps
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15493
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:26:38.992186",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "FRAUDGUESS",
    "Micro-Clusters",
    "Interactive Dashboard",
    "Heatmaps"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "FRAUDGUESS": 0.88,
    "Micro-Clusters": 0.8,
    "Interactive Dashboard": 0.78,
    "Heatmaps": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "FRAUDGUESS",
        "canonical": "FRAUDGUESS",
        "aliases": [
          "Fraud Detection System"
        ],
        "category": "unique_technical",
        "rationale": "FRAUDGUESS is a unique system introduced in the paper for detecting and explaining fraud, making it a novel concept.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "micro-clusters",
        "canonical": "Micro-Clusters",
        "aliases": [
          "Cluster Analysis"
        ],
        "category": "specific_connectable",
        "rationale": "Micro-clusters are a key technique used in the paper for detecting new types of fraud, linking to clustering methods.",
        "novelty_score": 0.68,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "interactive dashboard",
        "canonical": "Interactive Dashboard",
        "aliases": [
          "Data Visualization Tool"
        ],
        "category": "specific_connectable",
        "rationale": "The interactive dashboard is crucial for providing evidence and justifications, connecting to visualization tools.",
        "novelty_score": 0.55,
        "connectivity_score": 0.77,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "heatmaps",
        "canonical": "Heatmaps",
        "aliases": [
          "Heat Map Visualization"
        ],
        "category": "specific_connectable",
        "rationale": "Heatmaps are used for visualization in the paper, linking to data visualization techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "financial transactions",
      "domain experts",
      "Anonymous Financial Institution"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "FRAUDGUESS",
      "resolved_canonical": "FRAUDGUESS",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "micro-clusters",
      "resolved_canonical": "Micro-Clusters",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "interactive dashboard",
      "resolved_canonical": "Interactive Dashboard",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.77,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "heatmaps",
      "resolved_canonical": "Heatmaps",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# FRAUDGUESS: Spotting and Explaining New Types of Fraud in Million-Scale Financial Data

**Korean Title:** FRAUDGUESS: 백만 규모의 금융 데이터에서 새로운 유형의 사기를 발견하고 설명하기

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15493.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15493](https://arxiv.org/abs/2509.15493)

## 🔗 유사한 논문
- [[2025-09-19/Evaluating Supervised Learning Models for Fraud Detection_ A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data_20250919|Evaluating Supervised Learning Models for Fraud Detection: A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data]] (82.8% similar)
- [[2025-09-17/Synthesizing Behaviorally-Grounded Reasoning Chains_ A Data-Generation Framework for Personal Finance LLMs_20250917|Synthesizing Behaviorally-Grounded Reasoning Chains: A Data-Generation Framework for Personal Finance LLMs]] (77.4% similar)
- [[2025-09-18/From Patterns to Predictions_ A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets_20250918|From Patterns to Predictions: A Shapelet-Based Framework for Directional Forecasting in Noisy Financial Markets]] (77.3% similar)
- [[2025-09-18/Credit Card Fraud Detection_20250918|Credit Card Fraud Detection]] (77.2% similar)
- [[2025-09-17/Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment_20250917|Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (76.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Micro-Clusters|Micro-Clusters]], [[keywords/Interactive Dashboard|Interactive Dashboard]], [[keywords/Heatmaps|Heatmaps]]
**⚡ Unique Technical**: [[keywords/FRAUDGUESS|FRAUDGUESS]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15493v1 Announce Type: new 
Abstract: Given a set of financial transactions (who buys from whom, when, and for how much), as well as prior information from buyers and sellers, how can we find fraudulent transactions? If we have labels for some transactions for known types of fraud, we can build a classifier. However, we also want to find new types of fraud, still unknown to the domain experts ('Detection'). Moreover, we also want to provide evidence to experts that supports our opinion ('Justification'). In this paper, we propose FRAUDGUESS, to achieve two goals: (a) for 'Detection', it spots new types of fraud as micro-clusters in a carefully designed feature space; (b) for 'Justification', it uses visualization and heatmaps for evidence, as well as an interactive dashboard for deep dives. FRAUDGUESS is used in real life and is currently considered for deployment in an Anonymous Financial Institution (AFI). Thus, we also present the three new behaviors that FRAUDGUESS discovered in a real, million-scale financial dataset. Two of these behaviors are deemed fraudulent or suspicious by domain experts, catching hundreds of fraudulent transactions that would otherwise go un-noticed.

## 🔍 Abstract (한글 번역)

arXiv:2509.15493v1 발표 유형: 신규  
초록: 금융 거래 집합(누가 누구에게, 언제, 얼마에 구매하는지)과 구매자 및 판매자로부터의 사전 정보를 고려할 때, 어떻게 사기 거래를 찾아낼 수 있을까요? 일부 거래에 대해 알려진 사기 유형의 레이블이 있다면, 분류기를 구축할 수 있습니다. 그러나 우리는 또한 도메인 전문가에게 아직 알려지지 않은 새로운 유형의 사기를 발견하고자 합니다('탐지'). 게다가, 우리의 의견을 뒷받침하는 증거를 전문가에게 제공하고자 합니다('정당화'). 본 논문에서는 두 가지 목표를 달성하기 위해 FRAUDGUESS를 제안합니다: (a) '탐지'를 위해, 신중하게 설계된 특성 공간에서 마이크로 클러스터로 새로운 유형의 사기를 발견합니다; (b) '정당화'를 위해, 증거로 시각화 및 히트맵을 사용하며, 심층 분석을 위한 인터랙티브 대시보드를 제공합니다. FRAUDGUESS는 실제로 사용되고 있으며, 현재 익명의 금융 기관(AFI)에서 배포를 고려 중입니다. 따라서, 우리는 실제 백만 규모의 금융 데이터셋에서 FRAUDGUESS가 발견한 세 가지 새로운 행동을 제시합니다. 이 중 두 가지 행동은 도메인 전문가에 의해 사기 또는 의심스러운 것으로 간주되며, 그렇지 않으면 간과될 수백 건의 사기 거래를 포착합니다.

## 📝 요약

이 논문은 금융 거래 데이터를 분석하여 새로운 유형의 사기 거래를 탐지하고 이를 전문가에게 설명하는 FRAUDGUESS라는 시스템을 제안합니다. FRAUDGUESS는 두 가지 주요 목표를 달성합니다. 첫째, '탐지' 측면에서 새로운 사기 유형을 미세 클러스터로 식별합니다. 둘째, '정당화' 측면에서 시각화와 히트맵을 사용하여 전문가에게 증거를 제공합니다. 실제 금융 데이터에 적용된 결과, FRAUDGUESS는 세 가지 새로운 행동 패턴을 발견했으며, 이 중 두 가지는 전문가에 의해 사기성 또는 의심스러운 것으로 판단되었습니다. 이 시스템은 수백 건의 사기 거래를 식별하는 데 기여했습니다.

## 🎯 주요 포인트

- 1. FRAUDGUESS는 새로운 유형의 사기를 미시 클러스터로 감지하여 '탐지' 목표를 달성합니다.
- 2. '정당화' 목표를 위해 FRAUDGUESS는 시각화, 히트맵, 대화형 대시보드를 사용하여 전문가에게 증거를 제공합니다.
- 3. FRAUDGUESS는 실제 금융 데이터에서 새로운 세 가지 행동을 발견했으며, 이 중 두 가지는 전문가에 의해 사기 또는 의심스러운 것으로 간주됩니다.
- 4. FRAUDGUESS는 익명의 금융 기관에서 실제로 사용되고 있으며, 배포가 고려되고 있습니다.
- 5. FRAUDGUESS는 수백 건의 사기 거래를 탐지하여, 그렇지 않으면 간과될 수 있는 사례들을 포착합니다.


---

*Generated on 2025-09-23 10:26:38*