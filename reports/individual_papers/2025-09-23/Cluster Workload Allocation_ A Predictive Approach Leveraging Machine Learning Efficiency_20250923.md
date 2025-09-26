---
keywords:
  - Machine Learning
  - Neural Network
  - Google Cluster Data
  - Ensemble Voting Classifier
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17695
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:06:50.821768",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning",
    "Neural Network",
    "Google Cluster Data",
    "Ensemble Voting Classifier"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Machine Learning": 0.85,
    "Neural Network": 0.8,
    "Google Cluster Data": 0.7,
    "Ensemble Voting Classifier": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Machine Learning",
        "canonical": "Machine Learning",
        "aliases": [
          "ML"
        ],
        "category": "broad_technical",
        "rationale": "Machine Learning is a central theme of the paper and connects to a wide range of related topics.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Artificial Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "ANN"
        ],
        "category": "broad_technical",
        "rationale": "Artificial Neural Networks are specifically mentioned as a classifier used in the study, linking to deep learning topics.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Google Cluster Data",
        "canonical": "Google Cluster Data",
        "aliases": [
          "GCD"
        ],
        "category": "unique_technical",
        "rationale": "Google Cluster Data is a unique dataset used in the study, providing a specific context for workload allocation research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Ensemble Voting Classifier",
        "canonical": "Ensemble Voting Classifier",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The ensemble voting classifier is a specific model that achieved high accuracy, relevant for discussions on classification techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "workload allocation",
      "node affinity operators",
      "task constraints"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Machine Learning",
      "resolved_canonical": "Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Artificial Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Google Cluster Data",
      "resolved_canonical": "Google Cluster Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Ensemble Voting Classifier",
      "resolved_canonical": "Ensemble Voting Classifier",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Cluster Workload Allocation: A Predictive Approach Leveraging Machine Learning Efficiency

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17695.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17695](https://arxiv.org/abs/2509.17695)

## 🔗 유사한 논문
- [[2025-09-22/Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises_20250922|Nonconvex Decentralized Stochastic Bilevel Optimization under Heavy-Tailed Noises]] (79.4% similar)
- [[2025-09-18/Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (79.4% similar)
- [[2025-09-19/Online Multi-Robot Coordination and Cooperation with Task Precedence Relationships_20250919|Online Multi-Robot Coordination and Cooperation with Task Precedence Relationships]] (79.2% similar)
- [[2025-09-22/Learning to Optimize Capacity Planning in Semiconductor Manufacturing_20250922|Learning to Optimize Capacity Planning in Semiconductor Manufacturing]] (78.4% similar)
- [[2025-09-22/FedHK-MVFC_ Federated Heat Kernel Multi-View Clustering_20250922|FedHK-MVFC: Federated Heat Kernel Multi-View Clustering]] (78.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Machine Learning|Machine Learning]], [[keywords/Neural Network|Neural Network]]
**⚡ Unique Technical**: [[keywords/Google Cluster Data|Google Cluster Data]], [[keywords/Ensemble Voting Classifier|Ensemble Voting Classifier]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17695v1 Announce Type: cross 
Abstract: This research investigates how Machine Learning (ML) algorithms can assist in workload allocation strategies by detecting tasks with node affinity operators (referred to as constraint operators), which constrain their execution to a limited number of nodes. Using real-world Google Cluster Data (GCD) workload traces and the AGOCS framework, the study extracts node attributes and task constraints, then analyses them to identify suitable node-task pairings. It focuses on tasks that can be executed on either a single node or fewer than a thousand out of 12.5k nodes in the analysed GCD cluster. Task constraint operators are compacted, pre-processed with one-hot encoding, and used as features in a training dataset. Various ML classifiers, including Artificial Neural Networks, K-Nearest Neighbours, Decision Trees, Naive Bayes, Ridge Regression, Adaptive Boosting, and Bagging, are fine-tuned and assessed for accuracy and F1-scores. The final ensemble voting classifier model achieved 98% accuracy and a 1.5-1.8% misclassification rate for tasks with a single suitable node.

## 📝 요약

이 연구는 머신러닝 알고리즘이 작업 부하 할당 전략을 개선하는 방법을 탐구합니다. 특히, 노드 제약 연산자를 사용하여 제한된 수의 노드에서만 실행 가능한 작업을 식별하는 데 중점을 둡니다. 실제 구글 클러스터 데이터(GCD)와 AGOCS 프레임워크를 활용하여 노드 속성과 작업 제약을 추출하고, 이를 분석하여 적합한 노드-작업 쌍을 식별합니다. 다양한 머신러닝 분류기들을 활용하여 정확도와 F1 점수를 평가한 결과, 최종 앙상블 투표 분류기 모델은 98%의 정확도와 1.5-1.8%의 오분류율을 기록했습니다.

## 🎯 주요 포인트

- 1. 머신러닝 알고리즘은 노드 친화성 연산자를 가진 작업을 감지하여 작업 할당 전략을 지원할 수 있다.
- 2. 연구는 Google Cluster Data의 작업 추적을 사용하여 노드 속성과 작업 제약 조건을 추출하고 분석한다.
- 3. 다양한 머신러닝 분류기를 미세 조정하여 정확도와 F1 점수를 평가하였으며, 최종 앙상블 투표 분류기 모델은 98%의 정확도를 달성했다.
- 4. 연구는 12.5k 노드 중 단일 노드 또는 1천 개 미만의 노드에서 실행 가능한 작업에 중점을 둔다.
- 5. 작업 제약 연산자는 원-핫 인코딩으로 전처리되어 훈련 데이터셋의 특징으로 사용된다.


---

*Generated on 2025-09-24 00:06:50*