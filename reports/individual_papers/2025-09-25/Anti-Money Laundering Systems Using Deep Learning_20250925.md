---
keywords:
  - Deep Learning
  - Graph Neural Network
  - Centrality Algorithms
  - Anti-Money Laundering
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19359
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:29:26.701616",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Graph Neural Network",
    "Centrality Algorithms",
    "Anti-Money Laundering"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Graph Neural Network": 0.88,
    "Centrality Algorithms": 0.82,
    "Anti-Money Laundering": 0.9
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational technology in the proposed AML system, linking it to other machine learning applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Graph Convolutional Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GCN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are crucial for analyzing structured financial data, enhancing AML systems' capabilities.",
        "novelty_score": 0.68,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.88
      },
      {
        "surface": "Centrality Algorithms",
        "canonical": "Centrality Algorithms",
        "aliases": [
          "Degree Centrality",
          "Closeness Centrality",
          "Betweenness Centrality",
          "PageRank"
        ],
        "category": "unique_technical",
        "rationale": "Centrality algorithms are key to identifying influential nodes in transaction networks, crucial for AML.",
        "novelty_score": 0.72,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Anti-Money Laundering",
        "canonical": "Anti-Money Laundering",
        "aliases": [
          "AML"
        ],
        "category": "unique_technical",
        "rationale": "Anti-Money Laundering is the central theme of the paper, linking it to financial crime prevention.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      }
    ],
    "ban_list_suggestions": [
      "financial transaction networks",
      "global financial industry"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Graph Convolutional Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Centrality Algorithms",
      "resolved_canonical": "Centrality Algorithms",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Anti-Money Laundering",
      "resolved_canonical": "Anti-Money Laundering",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    }
  ]
}
-->

# Anti-Money Laundering Systems Using Deep Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19359.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19359](https://arxiv.org/abs/2509.19359)

## 🔗 유사한 논문
- [[2025-09-24/Hybrid Data can Enhance the Utility of Synthetic Data for Training Anti-Money Laundering Models_20250924|Hybrid Data can Enhance the Utility of Synthetic Data for Training Anti-Money Laundering Models]] (85.5% similar)
- [[2025-09-19/Evaluating Supervised Learning Models for Fraud Detection_ A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data_20250919|Evaluating Supervised Learning Models for Fraud Detection: A Comparative Study of Classical and Deep Architectures on Imbalanced Transaction Data]] (82.5% similar)
- [[2025-09-22/FRAUDGUESS_ Spotting and Explaining New Types of Fraud in Million-Scale Financial Data_20250922|FRAUDGUESS: Spotting and Explaining New Types of Fraud in Million-Scale Financial Data]] (80.8% similar)
- [[2025-09-23/Enhancing Financial RAG with Agentic AI and Multi-HyDE_ A Novel Approach to Knowledge Retrieval and Hallucination Reduction_20250923|Enhancing Financial RAG with Agentic AI and Multi-HyDE: A Novel Approach to Knowledge Retrieval and Hallucination Reduction]] (80.5% similar)
- [[2025-09-24/LLM-Enhanced Self-Evolving Reinforcement Learning for Multi-Step E-Commerce Payment Fraud Risk Detection_20250924|LLM-Enhanced Self-Evolving Reinforcement Learning for Multi-Step E-Commerce Payment Fraud Risk Detection]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Centrality Algorithms|Centrality Algorithms]], [[keywords/Anti-Money Laundering|Anti-Money Laundering]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19359v1 Announce Type: cross 
Abstract: In this paper, we focused on using deep learning methods for detecting money laundering in financial transaction networks, in order to demonstrate that it can be used as a complement or instead of the more commonly used rule-based systems and conventional Anti-Money Laundering (AML) systems. The paper explores the pivotal role played by Anti-Money Laundering (AML) activities in the global financial industry. It underscores the drawbacks of conventional AML systems, which exhibit high rates of false positives and lack the sophistication to uncover intricate money laundering schemes. To tackle these challenges, the paper proposes an advanced AML system that capitalizes on link analysis using deep learning techniques. At the heart of this system lies the utilization of centrality algorithms like Degree Centrality, Closeness Centrality, Betweenness Centrality, and PageRank. These algorithms enhance the system's capability to identify suspicious activities by examining the influence and interconnections within networks of financial transactions. The significance of Anti-Money Laundering (AML) efforts within the global financial sector is discussed in this paper. It highlights the limitations of traditional AML systems. The results showed the practicality and superiority of the new implementation of the GCN model, which is a preferable method for connectively structured data, meaning that a transaction or account is analyzed in the context of its financial environment. In addition, the paper delves into the prospects of Anti-Money Laundering (AML) efforts, proposing the integration of emerging technologies such as deep learning and centrality algorithms. This integration holds promise for enhancing the effectiveness of AML systems by refining their capabilities.

## 📝 요약

이 논문은 금융 거래 네트워크에서 자금 세탁을 탐지하기 위해 딥러닝 기법을 활용하는 방법을 제안합니다. 기존의 규칙 기반 시스템과 전통적인 자금세탁방지(AML) 시스템의 높은 오탐률과 복잡한 세탁 수법을 발견하는 데 한계를 지적하며, 딥러닝을 활용한 링크 분석을 통해 이를 보완하고자 합니다. 중심성 알고리즘(예: Degree, Closeness, Betweenness, PageRank)을 활용하여 금융 거래 네트워크 내의 영향력과 상호 연결성을 분석함으로써 의심스러운 활동을 식별하는 능력을 강화합니다. 연구 결과, GCN 모델의 새로운 구현이 금융 환경 내에서 거래나 계정을 분석하는 데 있어 실용적이고 우수한 방법임을 보여줍니다. 이러한 접근은 AML 시스템의 효과성을 높이는 데 기여할 수 있습니다.

## 🎯 주요 포인트

- 1. 본 논문은 금융 거래 네트워크에서 자금 세탁을 탐지하기 위해 딥러닝 기법을 사용하는 방법을 제안합니다.
- 2. 기존의 규칙 기반 시스템 및 전통적인 자금 세탁 방지(AML) 시스템의 한계를 지적하며, 높은 오탐률과 복잡한 자금 세탁 수법을 발견하는 데 부족함을 강조합니다.
- 3. 딥러닝 기법을 활용한 링크 분석을 통해 고급 AML 시스템을 제안하며, 중심성 알고리즘을 사용하여 금융 거래 네트워크 내의 영향력과 상호 연결성을 분석합니다.
- 4. GCN 모델의 새로운 구현이 연결 구조 데이터를 분석하는 데 있어 실용적이고 우수하다는 결과를 보여줍니다.
- 5. 딥러닝 및 중심성 알고리즘과 같은 신기술의 통합이 AML 시스템의 효과를 향상시킬 가능성을 제시합니다.


---

*Generated on 2025-09-25 15:29:26*