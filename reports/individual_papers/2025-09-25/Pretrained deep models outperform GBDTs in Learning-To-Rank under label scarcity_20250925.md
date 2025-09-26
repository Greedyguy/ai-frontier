---
keywords:
  - Deep Learning
  - Learning-to-Rank
  - Pretrained Models
  - Label Scarcity
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2308.00177
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:14:08.521368",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Learning-to-Rank",
    "Pretrained Models",
    "Label Scarcity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Learning-to-Rank": 0.8,
    "Pretrained Models": 0.79,
    "Label Scarcity": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is central to the paper's findings and connects to existing knowledge on neural networks.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Learning-to-Rank",
        "canonical": "Learning-to-Rank",
        "aliases": [
          "LTR"
        ],
        "category": "unique_technical",
        "rationale": "Learning-to-Rank is a specific application area where the paper demonstrates significant findings.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Pretrained Models",
        "canonical": "Pretrained Models",
        "aliases": [
          "Pretraining"
        ],
        "category": "specific_connectable",
        "rationale": "Pretrained models are crucial for the paper's methodology and connect to broader trends in model training.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "Label Scarcity",
        "canonical": "Label Scarcity",
        "aliases": [
          "Limited Labels"
        ],
        "category": "unique_technical",
        "rationale": "Label scarcity is a key challenge addressed in the paper, relevant to data availability issues.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "tabular data",
      "outlier data",
      "ranking metrics"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Learning-to-Rank",
      "resolved_canonical": "Learning-to-Rank",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Pretrained Models",
      "resolved_canonical": "Pretrained Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Label Scarcity",
      "resolved_canonical": "Label Scarcity",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Pretrained deep models outperform GBDTs in Learning-To-Rank under label scarcity

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2308.00177.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2308.00177](https://arxiv.org/abs/2308.00177)

## 🔗 유사한 논문
- [[2025-09-24/Reinforcement Learning on Pre-Training Data_20250924|Reinforcement Learning on Pre-Training Data]] (81.0% similar)
- [[2025-09-24/Is Pre-training Truly Better Than Meta-Learning?_20250924|Is Pre-training Truly Better Than Meta-Learning?]] (80.2% similar)
- [[2025-09-23/Evaluating the Effectiveness and Scalability of LLM-Based Data Augmentation for Retrieval_20250923|Evaluating the Effectiveness and Scalability of LLM-Based Data Augmentation for Retrieval]] (80.0% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (79.3% similar)
- [[2025-09-22/IGD_ Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation_20250922|IGD: Token Decisiveness Modeling via Information Gain in LLMs for Personalized Recommendation]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Pretrained Models|Pretrained Models]]
**⚡ Unique Technical**: [[keywords/Learning-to-Rank|Learning-to-Rank]], [[keywords/Label Scarcity|Label Scarcity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2308.00177v5 Announce Type: replace-cross 
Abstract: On tabular data, a significant body of literature has shown that current deep learning (DL) models perform at best similarly to Gradient Boosted Decision Trees (GBDTs), while significantly underperforming them on outlier data. However, these works often study idealized problem settings which may fail to capture complexities of real-world scenarios. We identify a natural tabular data setting where DL models can outperform GBDTs: tabular Learning-to-Rank (LTR) under label scarcity. Tabular LTR applications, including search and recommendation, often have an abundance of unlabeled data, and scarce labeled data. We show that DL rankers can utilize unsupervised pretraining to exploit this unlabeled data. In extensive experiments over both public and proprietary datasets, we show that pretrained DL rankers consistently outperform GBDT rankers on ranking metrics -- sometimes by as much as 38% -- both overall and on outliers.

## 📝 요약

이 논문은 딥러닝(DL) 모델이 레이블이 부족한 상황에서 테이블형 학습-순위화(LTR) 문제에서 그래디언트 부스팅 결정 트리(GBDT)보다 우수한 성능을 보일 수 있음을 제시합니다. 검색 및 추천과 같은 LTR 응용 분야에서는 레이블이 부족한 반면, 비레이블 데이터는 풍부합니다. 연구는 DL 순위자가 비레이블 데이터를 활용하기 위해 비지도 사전 학습을 사용할 수 있음을 보여줍니다. 공공 및 독점 데이터셋을 대상으로 한 실험에서, 사전 학습된 DL 순위자가 GBDT 순위자보다 최대 38%까지 뛰어난 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 딥러닝 모델은 레이블이 부족한 상황의 테이블형 학습-순위(LTR) 문제에서 GBDT보다 우수한 성능을 보일 수 있다.
- 2. 검색 및 추천과 같은 테이블형 LTR 응용에서는 레이블이 부족하고 비지도 학습을 통해 비레이블 데이터를 활용할 수 있다.
- 3. 사전 학습된 딥러닝 순위 모델은 공공 및 독점 데이터셋에서 GBDT 순위 모델보다 최대 38%까지 뛰어난 성능을 보인다.
- 4. 딥러닝 순위 모델은 전체적으로나 이상치 데이터에서도 GBDT 순위 모델을 능가하는 성능을 나타낸다.


---

*Generated on 2025-09-25 16:14:08*