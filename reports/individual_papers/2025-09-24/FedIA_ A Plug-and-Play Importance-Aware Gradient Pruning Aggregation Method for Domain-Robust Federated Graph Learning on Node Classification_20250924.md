<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:49:09.306759",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Graph Learning",
    "Gradient Pruning",
    "Graph Neural Network",
    "Domain Skew"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Federated Graph Learning": 0.78,
    "Gradient Pruning": 0.77,
    "Graph Neural Network": 0.85,
    "Domain Skew": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Federated Graph Learning",
        "canonical": "Federated Graph Learning",
        "aliases": [
          "FGL"
        ],
        "category": "unique_technical",
        "rationale": "Federated Graph Learning is a specific technique that addresses domain skew in federated learning, making it a unique and relevant concept for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Gradient Pruning",
        "canonical": "Gradient Pruning",
        "aliases": [
          "Pruning"
        ],
        "category": "unique_technical",
        "rationale": "Gradient Pruning is a technique used to improve model efficiency, which is central to the paper's methodology.",
        "novelty_score": 0.67,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Graph Neural Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are a core component of the discussed federated learning framework, providing strong connectivity to related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.88,
        "link_intent_score": 0.85
      },
      {
        "surface": "Domain Skew",
        "canonical": "Domain Skew",
        "aliases": [
          "Domain Shift"
        ],
        "category": "unique_technical",
        "rationale": "Domain Skew is a critical challenge addressed in the paper, relevant for understanding the context of federated learning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "method",
      "aggregation",
      "convergence"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Federated Graph Learning",
      "resolved_canonical": "Federated Graph Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Gradient Pruning",
      "resolved_canonical": "Gradient Pruning",
      "decision": "linked",
      "scores": {
        "novelty": 0.67,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.88,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Domain Skew",
      "resolved_canonical": "Domain Skew",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# FedIA: A Plug-and-Play Importance-Aware Gradient Pruning Aggregation Method for Domain-Robust Federated Graph Learning on Node Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18171.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18171](https://arxiv.org/abs/2509.18171)

## 🔗 유사한 논문
- [[2025-09-17/FedSSG_ Expectation-Gated and History-Aware Drift Alignment for Federated Learning_20250917|FedSSG: Expectation-Gated and History-Aware Drift Alignment for Federated Learning]] (85.0% similar)
- [[2025-09-24/FedFusion_ Federated Learning with Diversity- and Cluster-Aware Encoders for Robust Adaptation under Label Scarcity_20250924|FedFusion: Federated Learning with Diversity- and Cluster-Aware Encoders for Robust Adaptation under Label Scarcity]] (84.8% similar)
- [[2025-09-24/FedFiTS_ Fitness-Selected, Slotted Client Scheduling for Trustworthy Federated Learning in Healthcare AI_20250924|FedFiTS: Fitness-Selected, Slotted Client Scheduling for Trustworthy Federated Learning in Healthcare AI]] (83.6% similar)
- [[2025-09-19/FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT: Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (83.3% similar)
- [[2025-09-19/Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Federated Graph Learning|Federated Graph Learning]], [[keywords/Gradient Pruning|Gradient Pruning]], [[keywords/Domain Skew|Domain Skew]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18171v1 Announce Type: new 
Abstract: Federated Graph Learning (FGL) under domain skew -- as observed on platforms such as \emph{Twitch Gamers} and multilingual \emph{Wikipedia} networks -- drives client models toward incompatible representations, rendering naive aggregation both unstable and ineffective. We find that the culprit is not the weighting scheme but the \emph{noisy gradient signal}: empirical analysis of baseline methods suggests that a vast majority of gradient dimensions can be dominated by domain-specific variance. We therefore shift focus from "aggregation-first" to a \emph{projection-first} strategy that denoises client updates \emph{before} they are combined. The proposed FedIA framework realises this \underline{I}mportance-\underline{A}ware idea through a two-stage, plug-and-play pipeline: (i) a server-side top-$\rho$ mask keeps only the most informative about 5% of coordinates, and (ii) a lightweight influence-regularised momentum weight suppresses outlier clients. FedIA adds \emph{no extra uplink traffic and only negligible server memory}, making it readily deployable. On both homogeneous (Twitch Gamers) and heterogeneous (Wikipedia) graphs, it yields smoother, more stable convergence and higher final accuracy than nine strong baselines. A convergence sketch further shows that dynamic projection maintains the optimal $\mathcal{O}(\sigma^{2}/\sqrt{T})$ rate.

## 📝 요약

이 논문은 도메인 불균형이 있는 환경에서의 연합 그래프 학습(FGL)을 다룹니다. 기존 방법의 문제는 가중치가 아닌, 도메인 특이적 변동성에 의해 지배되는 노이즈가 많은 그래디언트 신호라는 점을 발견했습니다. 이를 해결하기 위해, 클라이언트 업데이트를 결합하기 전에 노이즈를 제거하는 '프로젝션 우선' 전략을 제안합니다. 제안된 FedIA 프레임워크는 두 단계로 구성되며, 서버 측에서 가장 중요한 5%의 좌표만 유지하는 마스크와, 이상치 클라이언트를 억제하는 가벼운 영향-정규화 모멘텀 가중치를 사용합니다. FedIA는 추가적인 업링크 트래픽 없이도 안정적이고 높은 정확도를 달성하며, 수렴 속도도 최적의 $\mathcal{O}(\sigma^{2}/\sqrt{T})$를 유지합니다.

## 🎯 주요 포인트

- 1. 도메인 편향이 있는 연합 그래프 학습(FGL)에서는 클라이언트 모델 간의 표현 불일치가 발생하여 단순한 집계가 불안정하고 비효율적이다.
- 2. 문제의 원인은 가중치 체계가 아니라 도메인 특이적 분산에 의해 지배되는 \emph{노이즈가 많은 그래디언트 신호}이다.
- 3. FedIA 프레임워크는 클라이언트 업데이트를 결합하기 전에 노이즈를 제거하는 \emph{투영 우선} 전략을 채택한다.
- 4. FedIA는 서버 측에서 가장 정보가 많은 약 5%의 좌표만 유지하는 상위-$\rho$ 마스크와 이상치 클라이언트를 억제하는 경량의 영향-정규화 모멘텀 가중치를 사용한다.
- 5. FedIA는 추가적인 업링크 트래픽 없이 배포 가능하며, 동적 투영을 통해 최적의 수렴 속도를 유지한다.


---

*Generated on 2025-09-24 14:49:09*