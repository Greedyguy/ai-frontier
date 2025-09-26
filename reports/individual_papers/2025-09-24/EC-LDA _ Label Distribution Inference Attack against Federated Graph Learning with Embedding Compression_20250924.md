<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:24:49.181938",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Federated Graph Learning",
    "Label Distribution Attack",
    "Embedding Compression"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.88,
    "Federated Graph Learning": 0.82,
    "Label Distribution Attack": 0.81,
    "Embedding Compression": 0.79
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
        "rationale": "Graph Neural Networks are central to the study and provide strong connectivity to related graph-based learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Federated Graph Learning",
        "canonical": "Federated Graph Learning",
        "aliases": [
          "FGL"
        ],
        "category": "unique_technical",
        "rationale": "Federated Graph Learning is a unique approach discussed in the paper, offering novel insights into collaborative graph learning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Label Distribution Attack",
        "canonical": "Label Distribution Attack",
        "aliases": [
          "LDA"
        ],
        "category": "unique_technical",
        "rationale": "The concept of Label Distribution Attack is a key focus of the paper, providing a unique angle on privacy concerns in federated learning.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.87,
        "link_intent_score": 0.81
      },
      {
        "surface": "Embedding Compression",
        "canonical": "Embedding Compression",
        "aliases": [
          "EC"
        ],
        "category": "unique_technical",
        "rationale": "Embedding Compression is a novel technique proposed in the paper to enhance attack effectiveness, linking to broader compression strategies.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "model parameters",
      "node classification",
      "link prediction"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Networks",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Federated Graph Learning",
      "resolved_canonical": "Federated Graph Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Label Distribution Attack",
      "resolved_canonical": "Label Distribution Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.87,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Embedding Compression",
      "resolved_canonical": "Embedding Compression",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# EC-LDA : Label Distribution Inference Attack against Federated Graph Learning with Embedding Compression

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.15140.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2505.15140](https://arxiv.org/abs/2505.15140)

## 🔗 유사한 논문
- [[2025-09-19/Federated Hypergraph Learning with Local Differential Privacy_ Toward Privacy-Aware Hypergraph Structure Completion_20250919|Federated Hypergraph Learning with Local Differential Privacy: Toward Privacy-Aware Hypergraph Structure Completion]] (82.6% similar)
- [[2025-09-24/FedIA_ A Plug-and-Play Importance-Aware Gradient Pruning Aggregation Method for Domain-Robust Federated Graph Learning on Node Classification_20250924|FedIA: A Plug-and-Play Importance-Aware Gradient Pruning Aggregation Method for Domain-Robust Federated Graph Learning on Node Classification]] (82.1% similar)
- [[2025-09-22/A Survey of Large Language Models for Data Challenges in Graphs_20250922|A Survey of Large Language Models for Data Challenges in Graphs]] (81.3% similar)
- [[2025-09-23/Preserving Node-level Privacy in Graph Neural Networks_20250923|Preserving Node-level Privacy in Graph Neural Networks]] (80.7% similar)
- [[2025-09-17/Differential Privacy in Federated Learning_ Mitigating Inference Attacks with Randomized Response_20250917|Differential Privacy in Federated Learning: Mitigating Inference Attacks with Randomized Response]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Federated Graph Learning|Federated Graph Learning]], [[keywords/Label Distribution Attack|Label Distribution Attack]], [[keywords/Embedding Compression|Embedding Compression]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.15140v2 Announce Type: replace 
Abstract: Graph Neural Networks (GNNs) have been widely used for graph analysis. Federated Graph Learning (FGL) is an emerging learning framework to collaboratively train graph data from various clients. However, since clients are required to upload model parameters to the server in each round, this provides the server with an opportunity to infer each client's data privacy. In this paper, we focus on label distribution attacks(LDAs) that aim to infer the label distributions of the clients' local data. We take the first step to attack client's label distributions in FGL. Firstly, we observe that the effectiveness of LDA is closely related to the variance of node embeddings in GNNs. Next, we analyze the relation between them and we propose a new attack named EC-LDA, which significantly improves the attack effectiveness by compressing node embeddings. Thirdly, extensive experiments on node classification and link prediction tasks across six widely used graph datasets show that EC-LDA outperforms the SOTA LDAs. For example, EC-LDA attains optimal values under both Cos-sim and JS-div evaluation metrics in the CoraFull and LastFM datasets. Finally, we explore the robustness of EC-LDA under differential privacy protection.

## 📝 요약

이 논문은 연합 그래프 학습(FGL) 환경에서 클라이언트의 레이블 분포를 추론하는 공격인 레이블 분포 공격(LDA)에 대해 다룹니다. 저자들은 GNN의 노드 임베딩 분산과 LDA의 효과성 간의 관계를 분석하고, 이를 기반으로 노드 임베딩을 압축하여 공격 효과를 향상시키는 새로운 공격 방법인 EC-LDA를 제안합니다. 6개의 그래프 데이터셋에서의 실험 결과, EC-LDA는 기존의 LDA보다 뛰어난 성능을 보였으며, 특히 CoraFull과 LastFM 데이터셋에서 최적의 평가 지표를 달성했습니다. 또한, EC-LDA의 차등 개인정보 보호 하에서의 강인성도 탐구했습니다.

## 🎯 주요 포인트

- 1. 그래프 신경망(GNN)은 그래프 분석에 널리 사용되며, 연합 그래프 학습(FGL)은 다양한 클라이언트의 그래프 데이터를 협력적으로 학습하는 새로운 프레임워크이다.
- 2. 클라이언트가 매 라운드마다 모델 매개변수를 서버에 업로드해야 하므로, 서버가 클라이언트의 데이터 프라이버시를 추론할 수 있는 기회를 제공한다.
- 3. 본 연구는 클라이언트의 레이블 분포를 추론하는 레이블 분포 공격(LDA)에 초점을 맞추고 있으며, 노드 임베딩의 분산이 LDA의 효과성과 밀접한 관련이 있음을 관찰하였다.
- 4. 새로운 공격 방법인 EC-LDA를 제안하여 노드 임베딩을 압축함으로써 공격 효과를 크게 개선하였다.
- 5. EC-LDA는 차별적 프라이버시 보호 하에서도 높은 성능을 유지하며, 여러 그래프 데이터셋에서 기존의 LDA보다 우수한 성능을 보였다.


---

*Generated on 2025-09-24 15:24:49*