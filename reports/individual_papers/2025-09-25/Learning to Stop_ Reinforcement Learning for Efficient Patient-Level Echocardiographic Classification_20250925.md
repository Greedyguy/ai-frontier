---
keywords:
  - Reinforcement Learning
  - Attention Mechanism
  - Cardiac Amyloidosis Detection
  - Echocardiographic Examination
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.19694
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:02:57.463650",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Attention Mechanism",
    "Cardiac Amyloidosis Detection",
    "Echocardiographic Examination"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Reinforcement Learning": 0.78,
    "Attention Mechanism": 0.82,
    "Cardiac Amyloidosis Detection": 0.75,
    "Echocardiographic Examination": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "reinforcement learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is crucial for the proposed method's decision-making process, linking it to broader machine learning strategies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "attention-based aggregation",
        "canonical": "Attention Mechanism",
        "aliases": [
          "attention-based fusion"
        ],
        "category": "specific_connectable",
        "rationale": "The use of an attention-based method for aggregating information connects to known attention mechanisms in machine learning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "cardiac amyloidosis detection",
        "canonical": "Cardiac Amyloidosis Detection",
        "aliases": [
          "heart amyloidosis detection"
        ],
        "category": "unique_technical",
        "rationale": "This specific application of the method highlights a unique medical use case, providing a specific link to medical imaging.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      },
      {
        "surface": "transthoracic echocardiographic examination",
        "canonical": "Echocardiographic Examination",
        "aliases": [
          "TTE"
        ],
        "category": "unique_technical",
        "rationale": "This term specifies the medical imaging context, which is essential for understanding the application domain.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "classification"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "reinforcement learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "attention-based aggregation",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "cardiac amyloidosis detection",
      "resolved_canonical": "Cardiac Amyloidosis Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "transthoracic echocardiographic examination",
      "resolved_canonical": "Echocardiographic Examination",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Learning to Stop: Reinforcement Learning for Efficient Patient-Level Echocardiographic Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19694.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.19694](https://arxiv.org/abs/2509.19694)

## 🔗 유사한 논문
- [[2025-09-23/CardiacCLIP_ Video-based CLIP Adaptation for LVEF Prediction in a Few-shot Manner_20250923|CardiacCLIP: Video-based CLIP Adaptation for LVEF Prediction in a Few-shot Manner]] (85.9% similar)
- [[2025-09-25/Advancing Few-Shot Pediatric Arrhythmia Classification with a Novel Contrastive Loss and Multimodal Learning_20250925|Advancing Few-Shot Pediatric Arrhythmia Classification with a Novel Contrastive Loss and Multimodal Learning]] (85.6% similar)
- [[2025-09-25/Anatomically Constrained Transformers for Cardiac Amyloidosis Classification_20250925|Anatomically Constrained Transformers for Cardiac Amyloidosis Classification]] (83.4% similar)
- [[2025-09-23/Echo-Path_ Pathology-Conditioned Echo Video Generation_20250923|Echo-Path: Pathology-Conditioned Echo Video Generation]] (83.2% similar)
- [[2025-09-25/Self-Alignment Learning to Improve Myocardial Infarction Detection from Single-Lead ECG_20250925|Self-Alignment Learning to Improve Myocardial Infarction Detection from Single-Lead ECG]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Cardiac Amyloidosis Detection|Cardiac Amyloidosis Detection]], [[keywords/Echocardiographic Examination|Echocardiographic Examination]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19694v1 Announce Type: new 
Abstract: Guidelines for transthoracic echocardiographic examination recommend the acquisition of multiple video clips from different views of the heart, resulting in a large number of clips. Typically, automated methods, for instance disease classifiers, either use one clip or average predictions from all clips. Relying on one clip ignores complementary information available from other clips, while using all clips is computationally expensive and may be prohibitive for clinical adoption.
  To select the optimal subset of clips that maximize performance for a specific task (image-based disease classification), we propose a method optimized through reinforcement learning. In our method, an agent learns to either keep processing view-specific clips to reduce the disease classification uncertainty, or stop processing if the achieved classification confidence is sufficient. Furthermore, we propose a learnable attention-based aggregation method as a flexible way of fusing information from multiple clips. The proposed method obtains an AUC of 0.91 on the task of detecting cardiac amyloidosis using only 30% of all clips, exceeding the performance achieved from using all clips and from other benchmarks.

## 📝 요약

이 논문은 심초음파 영상에서 질병을 분류하기 위한 최적의 영상 클립 집합을 선택하는 방법을 제안합니다. 기존 자동화 방법은 하나의 클립만 사용하거나 모든 클립의 예측을 평균화하는데, 이는 정보 손실이나 높은 계산 비용을 초래합니다. 이를 개선하기 위해 강화 학습을 통해 특정 작업에 최적화된 클립을 선택하고, 학습 가능한 주의 기반 집계 방법을 제안합니다. 제안된 방법은 전체 클립의 30%만 사용하여 심장 아밀로이드증을 탐지하는 작업에서 AUC 0.91의 성능을 달성하며, 이는 모든 클립을 사용하는 경우보다 높은 성능입니다.

## 🎯 주요 포인트

- 1. 경흉부 심초음파 검사에서 여러 비디오 클립을 사용하는 것은 정보가 풍부하지만 계산 비용이 높아 임상 적용에 제한적일 수 있습니다.
- 2. 특정 작업(이미지 기반 질병 분류)의 성능을 극대화하기 위해 최적의 클립 하위 집합을 선택하는 방법을 강화 학습을 통해 제안합니다.
- 3. 제안된 방법은 질병 분류 불확실성을 줄이기 위해 뷰별 클립을 계속 처리하거나, 분류 신뢰도가 충분할 경우 처리를 중단하도록 학습합니다.
- 4. 다중 클립에서 정보를 융합하기 위한 유연한 방법으로 학습 가능한 주의 기반 집계 방법을 제안합니다.
- 5. 제안된 방법은 심장 아밀로이드증 감지 작업에서 전체 클립의 30%만 사용하여 AUC 0.91을 달성하며, 이는 모든 클립을 사용했을 때보다 높은 성능을 보입니다.


---

*Generated on 2025-09-26 09:02:57*