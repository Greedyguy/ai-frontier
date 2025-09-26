---
keywords:
  - Parameter-Efficient Fine-Tuning
  - Vision Foundation Models
  - Low-Rank Adaptation
  - Atypical Mitotic Figures
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16935
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:38:30.198634",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Parameter-Efficient Fine-Tuning",
    "Vision Foundation Models",
    "Low-Rank Adaptation",
    "Atypical Mitotic Figures"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Parameter-Efficient Fine-Tuning": 0.85,
    "Vision Foundation Models": 0.88,
    "Low-Rank Adaptation": 0.82,
    "Atypical Mitotic Figures": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "parameter-efficient fine-tuning",
        "canonical": "Parameter-Efficient Fine-Tuning",
        "aliases": [
          "PEFT"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's approach and represents a novel adaptation strategy in model fine-tuning.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.85
      },
      {
        "surface": "Vision Foundation Models",
        "canonical": "Vision Foundation Models",
        "aliases": [
          "Vision Models"
        ],
        "category": "evolved_concepts",
        "rationale": "These models are pivotal in the study and represent a new class of models in computer vision.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.88
      },
      {
        "surface": "Low-Rank Adaptation",
        "canonical": "Low-Rank Adaptation",
        "aliases": [
          "LoRA"
        ],
        "category": "specific_connectable",
        "rationale": "LoRA is a specific technique used in the study, relevant for linking with other adaptation strategies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.77,
        "link_intent_score": 0.82
      },
      {
        "surface": "atypical mitotic figures",
        "canonical": "Atypical Mitotic Figures",
        "aliases": [
          "AMFs"
        ],
        "category": "unique_technical",
        "rationale": "The detection of AMFs is the primary application focus of the study, offering unique insights into medical image analysis.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
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
      "candidate_surface": "parameter-efficient fine-tuning",
      "resolved_canonical": "Parameter-Efficient Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Vision Foundation Models",
      "resolved_canonical": "Vision Foundation Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Low-Rank Adaptation",
      "resolved_canonical": "Low-Rank Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.77,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "atypical mitotic figures",
      "resolved_canonical": "Atypical Mitotic Figures",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Parameter-efficient fine-tuning (PEFT) of Vision Foundation Models for Atypical Mitotic Figure Classification

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16935.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16935](https://arxiv.org/abs/2509.16935)

## 🔗 유사한 논문
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (89.7% similar)
- [[2025-09-22/MIDOG 2025_ Mitotic Figure Detection with Attention-Guided False Positive Correction_20250922|MIDOG 2025: Mitotic Figure Detection with Attention-Guided False Positive Correction]] (84.0% similar)
- [[2025-09-23/MRN_ Harnessing 2D Vision Foundation Models for Diagnosing Parkinson's Disease with Limited 3D MR Data_20250923|MRN: Harnessing 2D Vision Foundation Models for Diagnosing Parkinson's Disease with Limited 3D MR Data]] (83.7% similar)
- [[2025-09-22/NeuroRAD-FM_ A Foundation Model for Neuro-Oncology with Distributionally Robust Training_20250922|NeuroRAD-FM: A Foundation Model for Neuro-Oncology with Distributionally Robust Training]] (82.7% similar)
- [[2025-09-22/Saccadic Vision for Fine-Grained Visual Classification_20250922|Saccadic Vision for Fine-Grained Visual Classification]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Low-Rank Adaptation|Low-Rank Adaptation]]
**⚡ Unique Technical**: [[keywords/Parameter-Efficient Fine-Tuning|Parameter-Efficient Fine-Tuning]], [[keywords/Atypical Mitotic Figures|Atypical Mitotic Figures]]
**🚀 Evolved Concepts**: [[keywords/Vision Foundation Models|Vision Foundation Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16935v1 Announce Type: new 
Abstract: Atypical mitotic figures (AMFs) are rare abnormal cell divisions associated with tumor aggressiveness and poor prognosis. Their detection remains a significant challenge due to subtle morphological cues, class imbalance, and inter-observer variability among pathologists. The MIDOG 2025 challenge introduced a dedicated track for atypical mitosis classification, enabling systematic evaluation of deep learning methods. In this study, we investigated the use of large vision foundation models, including Virchow, Virchow2, and UNI, with Low-Rank Adaptation (LoRA) for parameter-efficient fine-tuning. We conducted extensive experiments with different LoRA ranks, as well as random and group-based data splits, to analyze robustness under varied conditions. Our best approach, Virchow with LoRA rank 8 and ensemble of three-fold cross-validation, achieved a balanced accuracy of 88.37% on the preliminary test set, ranking joint 9th in the challenge leaderboard. These results highlight the promise of foundation models with efficient adaptation strategies for the classification of atypical mitosis, while underscoring the need for improvements in specificity and domain generalization.

## 📝 요약

이 논문은 종양의 공격성과 나쁜 예후와 관련된 비정형 유사 분열(AMF)의 분류를 다룹니다. MIDOG 2025 챌린지를 통해 심층 학습 방법의 체계적 평가가 가능해졌습니다. 연구에서는 Virchow, Virchow2, UNI 등의 대형 비전 기초 모델과 Low-Rank Adaptation(LoRA)을 사용하여 효율적인 파인튜닝을 수행했습니다. 다양한 LoRA 랭크와 데이터 분할 방법을 통해 모델의 견고성을 분석했으며, Virchow 모델과 LoRA 랭크 8을 사용한 3중 교차 검증 앙상블이 88.37%의 균형 정확도를 기록하며 챌린지에서 공동 9위를 차지했습니다. 이 결과는 비정형 유사 분열 분류에서 기초 모델의 잠재력을 보여주며, 특이성과 도메인 일반화의 개선 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. 비정형 유사분열(AMFs)은 종양의 공격성과 나쁜 예후와 관련된 드문 비정상 세포 분열이다.
- 2. MIDOG 2025 챌린지는 비정형 유사분열 분류를 위한 전용 트랙을 도입하여 딥러닝 방법의 체계적인 평가를 가능하게 했다.
- 3. Virchow, Virchow2, UNI와 같은 대형 비전 기초 모델과 Low-Rank Adaptation(LoRA)을 사용한 효율적인 파인튜닝을 연구했다.
- 4. Virchow 모델에 LoRA 랭크 8과 3겹 교차 검증 앙상블을 적용한 접근법이 88.37%의 균형 정확도를 달성하며 챌린지 리더보드에서 공동 9위를 기록했다.
- 5. 비정형 유사분열 분류를 위한 기초 모델의 가능성을 보여주면서도 특이성과 도메인 일반화의 개선 필요성을 강조했다.


---

*Generated on 2025-09-24 04:38:30*