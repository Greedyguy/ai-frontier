---
keywords:
  - Meta-learning
  - Contrastive Meta-Objective
  - Task Identity
  - In-Context Learning
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2410.05975
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:35:53.215203",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Meta-learning",
    "Contrastive Meta-Objective",
    "Task Identity",
    "In-Context Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Meta-learning": 0.85,
    "Contrastive Meta-Objective": 0.78,
    "Task Identity": 0.7,
    "In-Context Learning": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Meta-learning",
        "canonical": "Meta-learning",
        "aliases": [
          "Meta Learning"
        ],
        "category": "broad_technical",
        "rationale": "Meta-learning is a foundational concept in machine learning that enables linking across various adaptive learning systems.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Contrastive Meta-Objective",
        "canonical": "Contrastive Meta-Objective",
        "aliases": [
          "ConML"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel concept introduced in the paper, offering a unique perspective on meta-training frameworks.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Task Identity",
        "canonical": "Task Identity",
        "aliases": [
          "Task ID"
        ],
        "category": "specific_connectable",
        "rationale": "Task identity provides a crucial link for understanding task-specific adaptations in meta-learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "In-Context Learning",
        "canonical": "In-Context Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "In-context learning is a trending approach that enhances the adaptability of learning models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "mini-batch episodic training",
      "problem- and learner-agnostic"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Meta-learning",
      "resolved_canonical": "Meta-learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Contrastive Meta-Objective",
      "resolved_canonical": "Contrastive Meta-Objective",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Task Identity",
      "resolved_canonical": "Task Identity",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "In-Context Learning",
      "resolved_canonical": "In-Context Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Learning to Learn with Contrastive Meta-Objective

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2410.05975.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2410.05975](https://arxiv.org/abs/2410.05975)

## 🔗 유사한 논문
- [[2025-09-23/CoUn_ Empowering Machine Unlearning via Contrastive Learning_20250923|CoUn: Empowering Machine Unlearning via Contrastive Learning]] (82.8% similar)
- [[2025-09-22/Two Is Better Than One_ Aligned Representation Pairs for Anomaly Detection_20250922|Two Is Better Than One: Aligned Representation Pairs for Anomaly Detection]] (82.5% similar)
- [[2025-09-22/Towards Robust Visual Continual Learning with Multi-Prototype Supervision_20250922|Towards Robust Visual Continual Learning with Multi-Prototype Supervision]] (82.1% similar)
- [[2025-09-22/XAutoLM_ Efficient Fine-Tuning of Language Models via Meta-Learning and AutoML_20250922|XAutoLM: Efficient Fine-Tuning of Language Models via Meta-Learning and AutoML]] (81.7% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Meta-learning|Meta-learning]]
**🔗 Specific Connectable**: [[keywords/Task Identity|Task Identity]], [[keywords/In-Context Learning|In-Context Learning]]
**⚡ Unique Technical**: [[keywords/Contrastive Meta-Objective|Contrastive Meta-Objective]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.05975v3 Announce Type: replace 
Abstract: Meta-learning enables learning systems to adapt quickly to new tasks, similar to humans. Different meta-learning approaches all work under/with the mini-batch episodic training framework. Such framework naturally gives the information about task identity, which can serve as additional supervision for meta-training to improve generalizability. We propose to exploit task identity as additional supervision in meta-training, inspired by the alignment and discrimination ability which is is intrinsic in human's fast learning. This is achieved by contrasting what meta-learners learn, i.e., model representations. The proposed ConML is evaluating and optimizing the contrastive meta-objective under a problem- and learner-agnostic meta-training framework. We demonstrate that ConML integrates seamlessly with existing meta-learners, as well as in-context learning models, and brings significant boost in performance with small implementation cost.

## 📝 요약

이 논문은 메타러닝 시스템이 새로운 작업에 빠르게 적응할 수 있도록 돕는 방법을 제안합니다. 기존의 메타러닝 접근법은 미니배치 에피소드 훈련 프레임워크를 사용하며, 이 과정에서 작업 식별 정보를 추가적인 감독으로 활용하여 일반화 능력을 향상시킬 수 있습니다. 저자들은 인간의 빠른 학습에서 나타나는 정렬 및 구별 능력에 영감을 받아, 작업 식별을 메타훈련의 추가 감독으로 활용하는 ConML을 제안합니다. ConML은 문제 및 학습자에 무관한 메타훈련 프레임워크에서 대조 메타 목표를 평가하고 최적화합니다. 실험 결과, ConML은 기존 메타러너 및 컨텍스트 학습 모델과 원활하게 통합되며, 적은 구현 비용으로 성능을 크게 향상시킵니다.

## 🎯 주요 포인트

- 1. 메타러닝은 인간과 유사하게 새로운 작업에 빠르게 적응할 수 있도록 학습 시스템을 지원합니다.
- 2. 미니배치 에피소드 훈련 프레임워크는 작업 식별 정보를 제공하여 메타훈련의 일반화를 향상시킬 수 있습니다.
- 3. 제안된 ConML은 문제 및 학습자에 무관한 메타훈련 프레임워크에서 대조적인 메타목표를 평가하고 최적화합니다.
- 4. ConML은 기존 메타러너 및 인컨텍스트 학습 모델과 원활하게 통합되며, 적은 구현 비용으로 성능을 크게 향상시킵니다.
- 5. 작업 식별을 추가적인 감독으로 활용하여 메타훈련의 정렬 및 차별화 능력을 강화합니다.


---

*Generated on 2025-09-24 02:35:53*