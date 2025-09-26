---
keywords:
  - Dynamic Graphs
  - Anomaly Detection
  - Normality Distribution Shift
  - WhENDS
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17400
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:52:31.224899",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Dynamic Graphs",
    "Anomaly Detection",
    "Normality Distribution Shift",
    "WhENDS"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Dynamic Graphs": 0.82,
    "Anomaly Detection": 0.85,
    "Normality Distribution Shift": 0.78,
    "WhENDS": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "dynamic graphs",
        "canonical": "Dynamic Graphs",
        "aliases": [
          "temporal graphs",
          "evolving graphs"
        ],
        "category": "specific_connectable",
        "rationale": "Dynamic graphs are crucial for understanding temporal changes in network structures, which is central to the paper's focus.",
        "novelty_score": 0.55,
        "connectivity_score": 0.87,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "anomaly detection",
        "canonical": "Anomaly Detection",
        "aliases": [
          "outlier detection",
          "abnormality detection"
        ],
        "category": "broad_technical",
        "rationale": "Anomaly detection is a foundational concept in the paper, linking it to a wide range of applications and methodologies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "normality distribution shift",
        "canonical": "Normality Distribution Shift",
        "aliases": [
          "NDS",
          "distributional shift"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's novelty, addressing a specific challenge in dynamic graph analysis.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "WhENDS",
        "canonical": "WhENDS",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "WhENDS is the proposed method in the paper, representing a novel approach to the problem discussed.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
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
      "candidate_surface": "dynamic graphs",
      "resolved_canonical": "Dynamic Graphs",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.87,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "anomaly detection",
      "resolved_canonical": "Anomaly Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "normality distribution shift",
      "resolved_canonical": "Normality Distribution Shift",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "WhENDS",
      "resolved_canonical": "WhENDS",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Robust Anomaly Detection Under Normality Distribution Shift in Dynamic Graphs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17400.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17400](https://arxiv.org/abs/2509.17400)

## 🔗 유사한 논문
- [[2025-09-23/Prospective Multi-Graph Cohesion for Multivariate Time Series Anomaly Detection_20250923|Prospective Multi-Graph Cohesion for Multivariate Time Series Anomaly Detection]] (83.0% similar)
- [[2025-09-23/Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning_20250923|Full-History Graphs with Edge-Type Decoupled Networks for Temporal Reasoning]] (81.9% similar)
- [[2025-09-22/DiRW_ Path-Aware Digraph Learning for Heterophily_20250922|DiRW: Path-Aware Digraph Learning for Heterophily]] (81.1% similar)
- [[2025-09-23/Intention-aware Hierarchical Diffusion Model for Long-term Trajectory Anomaly Detection_20250923|Intention-aware Hierarchical Diffusion Model for Long-term Trajectory Anomaly Detection]] (80.8% similar)
- [[2025-09-23/Self-Supervised Learning of Graph Representations for Network Intrusion Detection_20250923|Self-Supervised Learning of Graph Representations for Network Intrusion Detection]] (80.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Anomaly Detection|Anomaly Detection]]
**🔗 Specific Connectable**: [[keywords/Dynamic Graphs|Dynamic Graphs]]
**⚡ Unique Technical**: [[keywords/Normality Distribution Shift|Normality Distribution Shift]], [[keywords/WhENDS|WhENDS]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17400v1 Announce Type: new 
Abstract: Anomaly detection in dynamic graphs is a critical task with broad real-world applications, including social networks, e-commerce, and cybersecurity. Most existing methods assume that normal patterns remain stable over time; however, this assumption often fails in practice due to the phenomenon we refer to as normality distribution shift (NDS), where normal behaviors evolve over time. Ignoring NDS can lead models to misclassify shifted normal instances as anomalies, degrading detection performance. To tackle this issue, we propose WhENDS, a novel unsupervised anomaly detection method that aligns normal edge embeddings across time by estimating distributional statistics and applying whitening transformations. Extensive experiments on four widely-used dynamic graph datasets show that WhENDS consistently outperforms nine strong baselines, achieving state-of-the-art results and underscoring the importance of addressing NDS in dynamic graph anomaly detection.

## 📝 요약

이 논문은 동적 그래프에서의 이상 탐지를 다루며, 정상 패턴이 시간에 따라 변할 수 있다는 '정상성 분포 변화(NDS)' 현상을 고려하지 않으면 탐지 성능이 저하될 수 있음을 지적합니다. 이를 해결하기 위해, 저자들은 WhENDS라는 새로운 비지도 학습 방법을 제안합니다. 이 방법은 시간에 따른 정상 엣지 임베딩을 정렬하기 위해 분포 통계 추정과 화이트닝 변환을 적용합니다. 네 가지 동적 그래프 데이터셋에서의 실험 결과, WhENDS는 기존의 아홉 가지 강력한 기법들을 능가하며, NDS를 고려하는 것이 동적 그래프 이상 탐지에서 중요함을 강조합니다.

## 🎯 주요 포인트

- 1. 동적 그래프에서의 이상 탐지는 사회 네트워크, 전자 상거래, 사이버 보안 등 다양한 실제 응용 분야에서 중요한 과제입니다.
- 2. 기존 방법들은 정상 패턴이 시간에 따라 안정적이라고 가정하지만, 이는 정상성 분포 이동(NDS) 현상으로 인해 실제로는 자주 실패합니다.
- 3. NDS를 무시하면 모델이 이동된 정상 인스턴스를 이상으로 잘못 분류하여 탐지 성능이 저하될 수 있습니다.
- 4. WhENDS는 정상 엣지 임베딩을 시간에 따라 정렬하여 NDS 문제를 해결하는 새로운 비지도 학습 이상 탐지 방법입니다.
- 5. 네 가지 동적 그래프 데이터셋에서의 실험 결과, WhENDS는 9개의 강력한 기준 방법을 일관되게 능가하며, 동적 그래프 이상 탐지에서 NDS 문제를 해결하는 것이 중요함을 강조합니다.


---

*Generated on 2025-09-24 01:52:31*