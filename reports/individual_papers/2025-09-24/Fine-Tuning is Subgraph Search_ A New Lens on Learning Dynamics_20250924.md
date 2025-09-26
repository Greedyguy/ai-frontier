<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:27:43.548772",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Fine-Tuning",
    "Subgraph Search",
    "Circuit-Tuning",
    "Learning Dynamics"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Fine-Tuning": 0.78,
    "Subgraph Search": 0.82,
    "Circuit-Tuning": 0.79,
    "Learning Dynamics": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "fine-tuning",
        "canonical": "Fine-Tuning",
        "aliases": [
          "model tuning",
          "parameter tuning"
        ],
        "category": "broad_technical",
        "rationale": "Fine-tuning is a common process in machine learning that involves adjusting a pre-trained model to improve performance on a specific task.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "subgraph search",
        "canonical": "Subgraph Search",
        "aliases": [
          "graph optimization",
          "subgraph optimization"
        ],
        "category": "unique_technical",
        "rationale": "Subgraph search is a novel approach in this paper, offering a new perspective on learning dynamics.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "circuit-tuning",
        "canonical": "Circuit-Tuning",
        "aliases": [
          "circuit optimization",
          "iterative tuning"
        ],
        "category": "unique_technical",
        "rationale": "Circuit-tuning is a specific algorithm introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.79
      },
      {
        "surface": "learning dynamics",
        "canonical": "Learning Dynamics",
        "aliases": [
          "training dynamics",
          "model dynamics"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding learning dynamics is essential for interpreting model behavior and improving training processes.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "mechanism",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "fine-tuning",
      "resolved_canonical": "Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "subgraph search",
      "resolved_canonical": "Subgraph Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "circuit-tuning",
      "resolved_canonical": "Circuit-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "learning dynamics",
      "resolved_canonical": "Learning Dynamics",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Fine-Tuning is Subgraph Search: A New Lens on Learning Dynamics

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.06106.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2502.06106](https://arxiv.org/abs/2502.06106)

## 🔗 유사한 논문
- [[2025-09-22/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250922|Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (82.9% similar)
- [[2025-09-22/Modeling Transformers as complex networks to analyze learning dynamics_20250922|Modeling Transformers as complex networks to analyze learning dynamics]] (82.2% similar)
- [[2025-09-23/A non-smooth regularization framework for learning over multitask graphs_20250923|A non-smooth regularization framework for learning over multitask graphs]] (82.1% similar)
- [[2025-09-23/Control Disturbance Rejection in Neural ODEs_20250923|Control Disturbance Rejection in Neural ODEs]] (82.1% similar)
- [[2025-09-23/Model Guidance via Robust Feature Attribution_20250923|Model Guidance via Robust Feature Attribution]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Fine-Tuning|Fine-Tuning]]
**🔗 Specific Connectable**: [[keywords/Learning Dynamics|Learning Dynamics]]
**⚡ Unique Technical**: [[keywords/Subgraph Search|Subgraph Search]], [[keywords/Circuit-Tuning|Circuit-Tuning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.06106v3 Announce Type: replace-cross 
Abstract: The study of mechanistic interpretability aims to reverse-engineer a model to explain its behaviors. While recent studies have focused on the static mechanism of a certain behavior, the learning dynamics inside a model remain to be explored. In this work, we develop a fine-tuning method for analyzing the mechanism behind learning. Inspired by the concept of intrinsic dimension, we view a model as a computational graph with redundancy for a specific task, and treat the fine-tuning process as a search for and optimization of a subgraph within this graph. Based on this hypothesis, we propose circuit-tuning, an algorithm that iteratively builds the subgraph for a specific task and updates the relevant parameters in a heuristic way. We first validate our hypothesis through a carefully designed experiment and provide a detailed analysis of the learning dynamics during fine-tuning. Subsequently, we conduct experiments on more complex tasks, demonstrating that circuit-tuning could strike a balance between the performance on the target task and the general capabilities. Our work offers a new analytical method for the dynamics of fine-tuning, provides new findings on the mechanisms behind the training process, and inspires the design of superior algorithms for the training of neural networks.

## 📝 요약

이 연구는 모델의 학습 메커니즘을 분석하기 위해 미세 조정 방법을 개발했습니다. 본 연구는 모델을 특정 작업에 대한 중복성을 가진 계산 그래프로 보고, 미세 조정 과정을 이 그래프 내의 서브그래프를 최적화하는 과정으로 간주합니다. 이를 기반으로 서킷 튜닝 알고리즘을 제안하여 특정 작업에 맞는 서브그래프를 반복적으로 구축하고 관련 매개변수를 갱신합니다. 실험을 통해 가설을 검증하고, 미세 조정 중 학습 역학을 분석했습니다. 복잡한 작업에 대한 실험 결과, 서킷 튜닝이 목표 작업 성능과 일반적 능력 간의 균형을 맞출 수 있음을 보여주었습니다. 이 연구는 미세 조정의 역학에 대한 새로운 분석 방법을 제시하고, 신경망 훈련을 위한 우수한 알고리즘 설계에 영감을 제공합니다.

## 🎯 주요 포인트

- 1. 본 연구는 모델의 학습 메커니즘을 분석하기 위해 세부 조정 방법을 개발하였다.
- 2. 모델을 특정 작업에 대한 중복성을 가진 계산 그래프로 보고, 세부 조정 과정을 이 그래프 내의 서브그래프를 탐색하고 최적화하는 과정으로 간주하였다.
- 3. 제안된 서킷-튜닝 알고리즘은 특정 작업에 대한 서브그래프를 반복적으로 구축하고 관련 매개변수를 휴리스틱하게 업데이트한다.
- 4. 실험을 통해 서킷-튜닝이 목표 작업의 성능과 일반적 능력 간의 균형을 맞출 수 있음을 입증하였다.
- 5. 본 연구는 세부 조정의 역학에 대한 새로운 분석 방법을 제공하고, 신경망 훈련을 위한 우수한 알고리즘 설계에 영감을 준다.


---

*Generated on 2025-09-24 14:27:43*