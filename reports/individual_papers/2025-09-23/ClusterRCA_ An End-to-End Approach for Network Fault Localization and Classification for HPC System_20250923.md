---
keywords:
  - ClusterRCA
  - Network Fault Localization
  - Multimodal Learning
  - Graph Neural Network
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.20673
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:09:01.984559",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "ClusterRCA",
    "Network Fault Localization",
    "Multimodal Learning",
    "Graph Neural Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "ClusterRCA": 0.78,
    "Network Fault Localization": 0.82,
    "Multimodal Learning": 0.79,
    "Graph Neural Network": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "ClusterRCA",
        "canonical": "ClusterRCA",
        "aliases": [
          "Cluster RCA"
        ],
        "category": "unique_technical",
        "rationale": "ClusterRCA is the core framework introduced in the paper, crucial for network fault localization in HPC systems.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Network Fault Localization",
        "canonical": "Network Fault Localization",
        "aliases": [
          "Fault Localization"
        ],
        "category": "specific_connectable",
        "rationale": "Network Fault Localization is a key process in diagnosing network issues, directly related to the paper's focus.",
        "novelty_score": 0.58,
        "connectivity_score": 0.8,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multimodal Data",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Data is central to the framework's approach, linking it to broader multimodal learning techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.68,
        "link_intent_score": 0.79
      },
      {
        "surface": "Graph-Based Approach",
        "canonical": "Graph Neural Network",
        "aliases": [
          "Graph Approach"
        ],
        "category": "specific_connectable",
        "rationale": "The graph-based approach in the paper aligns with Graph Neural Networks, facilitating connections to similar methodologies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.88,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "HPC System",
      "Network Failure",
      "Classifier-Based Approaches"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "ClusterRCA",
      "resolved_canonical": "ClusterRCA",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Network Fault Localization",
      "resolved_canonical": "Network Fault Localization",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.8,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multimodal Data",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.68,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Graph-Based Approach",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.88,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# ClusterRCA: An End-to-End Approach for Network Fault Localization and Classification for HPC System

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.20673.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.20673](https://arxiv.org/abs/2506.20673)

## 🔗 유사한 논문
- [[2025-09-19/Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (80.9% similar)
- [[2025-09-22/MicroRCA-Agent_ Microservice Root Cause Analysis Method Based on Large Language Model Agents_20250922|MicroRCA-Agent: Microservice Root Cause Analysis Method Based on Large Language Model Agents]] (80.7% similar)
- [[2025-09-19/Spatio-Temporal Anomaly Detection with Graph Networks for Data Quality Monitoring of the Hadron Calorimeter_20250919|Spatio-Temporal Anomaly Detection with Graph Networks for Data Quality Monitoring of the Hadron Calorimeter]] (80.2% similar)
- [[2025-09-18/Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods: Reviving Transformer for Graph Clustering]] (79.7% similar)
- [[2025-09-22/Interpretable Network-assisted Random Forest+_20250922|Interpretable Network-assisted Random Forest+]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Network Fault Localization|Network Fault Localization]], [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/ClusterRCA|ClusterRCA]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.20673v2 Announce Type: replace-cross 
Abstract: Network failure diagnosis is challenging yet critical for high-performance computing (HPC) systems. Existing methods cannot be directly applied to HPC scenarios due to data heterogeneity and lack of accuracy. This paper proposes a novel framework, called ClusterRCA, to localize culprit nodes and determine failure types by leveraging multimodal data. ClusterRCA extracts features from topologically connected network interface controller (NIC) pairs to analyze the diverse, multimodal data in HPC systems. To accurately localize culprit nodes and determine failure types, ClusterRCA combines classifier-based and graph-based approaches. A failure graph is constructed based on the output of the state classifier, and then it performs a customized random walk on the graph to localize the root cause. Experiments on datasets collected by a top-tier global HPC device vendor show ClusterRCA achieves high accuracy in diagnosing network failure for HPC systems. ClusterRCA also maintains robust performance across different application scenarios.

## 📝 요약

이 논문은 고성능 컴퓨팅(HPC) 시스템에서 네트워크 장애 진단을 위한 새로운 프레임워크인 ClusterRCA를 제안합니다. 기존 방법들은 데이터의 이질성과 정확성 부족으로 인해 HPC에 직접 적용하기 어렵습니다. ClusterRCA는 다중 모달 데이터를 활용하여 문제의 원인이 되는 노드를 식별하고 장애 유형을 결정합니다. 이를 위해 네트워크 인터페이스 컨트롤러(NIC) 쌍의 연결성을 기반으로 특징을 추출하고, 분류기 기반 및 그래프 기반 접근법을 결합합니다. 상태 분류기의 출력으로 장애 그래프를 구성한 후, 맞춤형 랜덤 워크를 수행하여 근본 원인을 찾아냅니다. 글로벌 HPC 장치 공급업체의 데이터셋 실험 결과, ClusterRCA는 높은 정확도로 네트워크 장애를 진단하며 다양한 응용 시나리오에서도 견고한 성능을 유지합니다.

## 🎯 주요 포인트

- 1. ClusterRCA는 고성능 컴퓨팅(HPC) 시스템에서 네트워크 장애를 진단하기 위해 멀티모달 데이터를 활용하는 새로운 프레임워크입니다.
- 2. 이 프레임워크는 네트워크 인터페이스 컨트롤러(NIC) 쌍에서 특징을 추출하여 다양한 멀티모달 데이터를 분석합니다.
- 3. ClusterRCA는 분류기 기반 접근법과 그래프 기반 접근법을 결합하여 문제 노드를 정확히 찾아내고 장애 유형을 결정합니다.
- 4. 상태 분류기의 출력을 기반으로 장애 그래프를 구축하고, 그래프에서 맞춤형 랜덤 워크를 수행하여 근본 원인을 찾아냅니다.
- 5. 실험 결과, ClusterRCA는 다양한 응용 시나리오에서도 높은 정확도와 견고한 성능을 유지합니다.


---

*Generated on 2025-09-24 01:09:01*