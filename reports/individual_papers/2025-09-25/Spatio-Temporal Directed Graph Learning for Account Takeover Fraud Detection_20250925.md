---
keywords:
  - Spatio-Temporal Directed Graph
  - Graph Neural Network
  - Account Takeover Fraud
  - Inductive Learning
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20339
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:49:10.357657",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Spatio-Temporal Directed Graph",
    "Graph Neural Network",
    "Account Takeover Fraud",
    "Inductive Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Spatio-Temporal Directed Graph": 0.78,
    "Graph Neural Network": 0.85,
    "Account Takeover Fraud": 0.8,
    "Inductive Learning": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Spatio-Temporal Directed Graph",
        "canonical": "Spatio-Temporal Directed Graph",
        "aliases": [
          "Spatio-Temporal Graph",
          "Directed Graph"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach to modeling account takeover fraud detection using graph structures.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      },
      {
        "surface": "GraphSAGE",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GraphSAGE"
        ],
        "category": "specific_connectable",
        "rationale": "GraphSAGE is a variant of Graph Neural Networks, which is a specific connectable concept in the context of graph learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Account Takeover Fraud",
        "canonical": "Account Takeover Fraud",
        "aliases": [
          "ATO Fraud"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus, providing a specific context for the application of graph learning techniques.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Inductive Learning",
        "canonical": "Inductive Learning",
        "aliases": [
          "Inductive Graph Learning"
        ],
        "category": "broad_technical",
        "rationale": "Inductive learning is a broad technical concept relevant to the scalability of graph-based models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "XGBoost",
      "Capital One"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Spatio-Temporal Directed Graph",
      "resolved_canonical": "Spatio-Temporal Directed Graph",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "GraphSAGE",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Account Takeover Fraud",
      "resolved_canonical": "Account Takeover Fraud",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Inductive Learning",
      "resolved_canonical": "Inductive Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Spatio-Temporal Directed Graph Learning for Account Takeover Fraud Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20339.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20339](https://arxiv.org/abs/2509.20339)

## 🔗 유사한 논문
- [[2025-09-23/Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning_20250923|Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning]] (80.9% similar)
- [[2025-09-18/TFLAG_Towards Practical APT Detection via Deviation-Aware Learning on Temporal Provenance Graph_20250918|TFLAG:Towards Practical APT Detection via Deviation-Aware Learning on Temporal Provenance Graph]] (80.4% similar)
- [[2025-09-24/Improving Credit Card Fraud Detection through Transformer-Enhanced GAN Oversampling_20250924|Improving Credit Card Fraud Detection through Transformer-Enhanced GAN Oversampling]] (79.7% similar)
- [[2025-09-25/Anti-Money Laundering Systems Using Deep Learning_20250925|Anti-Money Laundering Systems Using Deep Learning]] (79.3% similar)
- [[2025-09-23/A Comprehensive Performance Comparison of Traditional and Ensemble Machine Learning Models for Online Fraud Detection_20250923|A Comprehensive Performance Comparison of Traditional and Ensemble Machine Learning Models for Online Fraud Detection]] (79.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Inductive Learning|Inductive Learning]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Spatio-Temporal Directed Graph|Spatio-Temporal Directed Graph]], [[keywords/Account Takeover Fraud|Account Takeover Fraud]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20339v1 Announce Type: new 
Abstract: Account Takeover (ATO) fraud poses a significant challenge in consumer banking, requiring high recall under strict latency while minimizing friction for legitimate users. Production systems typically rely on tabular gradient-boosted decision trees (e.g., XGBoost) that score sessions independently, overlooking the relational and temporal structure of online activity that characterizes coordinated attacks and "fraud rings." We introduce ATLAS (Account Takeover Learning Across Spatio-Temporal Directed Graph), a framework that reformulates ATO detection as spatio-temporal node classification on a time-respecting directed session graph. ATLAS links entities via shared identifiers (account, device, IP) and regulates connectivity with time-window and recency constraints, enabling causal, time-respecting message passing and latency-aware label propagation that uses only labels available at scoring time, non-anticipative and leakage-free. We operationalize ATLAS with inductive GraphSAGE variants trained via neighbor sampling, at scale on a sessions graph with more than 100M nodes and around 1B edges. On a high-risk digital product at Capital One, ATLAS delivers 6.38 percent AUC improvement and more than 50 percent reduction in customer friction, improving fraud capture while reducing user friction.

## 📝 요약

이 논문은 소비자 은행에서의 계정 탈취(ATO) 사기를 효과적으로 탐지하기 위한 새로운 프레임워크인 ATLAS를 소개합니다. 기존의 시스템은 독립적인 세션 점수화에 의존하여 온라인 활동의 관계적 및 시간적 구조를 간과하는 반면, ATLAS는 시간-존중 방향성 세션 그래프에서의 시공간 노드 분류로 ATO 탐지를 재구성합니다. ATLAS는 계정, 장치, IP와 같은 공유 식별자를 통해 엔티티를 연결하고, 시간 창 및 최신성 제약을 통해 연결성을 조절하여 인과적이고 시간-존중적인 메시지 전달과 지연 인식 레이블 전파를 가능하게 합니다. Capital One의 고위험 디지털 제품에서 ATLAS는 AUC를 6.38% 개선하고 고객 마찰을 50% 이상 줄여 사기 탐지 성능을 향상시켰습니다.

## 🎯 주요 포인트

- 1. ATO(계정 탈취) 사기는 소비자 은행업에 큰 도전 과제를 제시하며, 높은 재현율과 낮은 사용자 마찰을 요구합니다.
- 2. 기존 시스템은 독립적으로 세션을 평가하는 테이블형 그래디언트 부스팅 결정 트리에 의존하지만, 이는 온라인 활동의 관계적 및 시간적 구조를 간과합니다.
- 3. ATLAS는 시간-존중 지향 세션 그래프에서의 시공간 노드 분류로 ATO 탐지를 재구성하는 프레임워크입니다.
- 4. ATLAS는 1억 개 이상의 노드와 약 10억 개의 엣지를 가진 세션 그래프에서 대규모로 인덕티브 GraphSAGE 변형을 사용하여 운영됩니다.
- 5. Capital One의 고위험 디지털 제품에서 ATLAS는 AUC를 6.38% 개선하고 고객 마찰을 50% 이상 줄이며 사기 탐지와 사용자 마찰을 동시에 개선합니다.


---

*Generated on 2025-09-25 16:49:10*