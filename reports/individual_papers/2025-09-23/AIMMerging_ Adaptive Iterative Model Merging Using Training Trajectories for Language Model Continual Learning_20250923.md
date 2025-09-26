---
keywords:
  - Continual Learning
  - Large Language Model
  - Adaptive Iterative Model Merging
  - Training Trajectories
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17348
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:52:47.273223",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Continual Learning",
    "Large Language Model",
    "Adaptive Iterative Model Merging",
    "Training Trajectories"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Continual Learning": 0.85,
    "Large Language Model": 0.8,
    "Adaptive Iterative Model Merging": 0.9,
    "Training Trajectories": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Continual Learning",
        "canonical": "Continual Learning",
        "aliases": [
          "CL"
        ],
        "category": "broad_technical",
        "rationale": "Continual Learning is a key concept for linking discussions about adaptive and iterative learning in dynamic environments.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's focus on adaptive model merging, providing a strong connection to existing literature on language models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Adaptive Iterative Model Merging",
        "canonical": "Adaptive Iterative Model Merging",
        "aliases": [
          "AIMMerging"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper, crucial for understanding the proposed method's unique contribution.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.9
      },
      {
        "surface": "Training Trajectories",
        "canonical": "Training Trajectories",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Training Trajectories are pivotal for understanding the dynamic monitoring and merging process described in the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "model merging",
      "performance improvements"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Continual Learning",
      "resolved_canonical": "Continual Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Adaptive Iterative Model Merging",
      "resolved_canonical": "Adaptive Iterative Model Merging",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Training Trajectories",
      "resolved_canonical": "Training Trajectories",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17348.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17348](https://arxiv.org/abs/2509.17348)

## 🔗 유사한 논문
- [[2025-09-22/Towards Robust Visual Continual Learning with Multi-Prototype Supervision_20250922|Towards Robust Visual Continual Learning with Multi-Prototype Supervision]] (86.1% similar)
- [[2025-09-22/Exploring Polyglot Harmony_ On Multilingual Data Allocation for Large Language Models Pretraining_20250922|Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining]] (85.9% similar)
- [[2025-09-18/HAM_ Hierarchical Adapter Merging for Scalable Continual Learning_20250918|HAM: Hierarchical Adapter Merging for Scalable Continual Learning]] (84.9% similar)
- [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (84.7% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (84.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Continual Learning|Continual Learning]], [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Training Trajectories|Training Trajectories]]
**⚡ Unique Technical**: [[keywords/Adaptive Iterative Model Merging|Adaptive Iterative Model Merging]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17348v1 Announce Type: cross 
Abstract: Continual learning (CL) is essential for deploying large language models (LLMs) in dynamic real-world environments without the need for costly retraining. Recent model merging-based methods have attracted significant attention, but they still struggle to effectively manage the trade-off between learning new knowledge and preventing forgetting, a challenge largely stemming from suboptimal number of merges and merging frequency. In this paper, we introduce Adaptive Iterative Model Merging (AimMerging), a novel CL framework that utilizes learning and forgetting signals from the training trajectory to dynamically monitor the model's training status. Guided by dynamic monitoring, the training trajectory-guided merge controller adaptively determines the timing and frequency of iterative fusion, while the rehearsal-based knowledge fusion module computes the merging weights and executes the fusion. Comprehensive experiments on three CL benchmarks with various model sizes (from 770M to 13B) demonstrate that AimMerging achieves significant performance improvements over existing state-of-the-art methods, with an average relative improvement of 80% and 59% on FWT and BWT, respectively. The source code is provided for reproducibility.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 지속적 학습(CL)을 위한 새로운 프레임워크인 Adaptive Iterative Model Merging(AimMerging)을 제안합니다. AimMerging은 학습과 망각 신호를 활용하여 모델의 학습 상태를 동적으로 모니터링하고, 이를 통해 모델 병합의 시기와 빈도를 적절히 조절합니다. 또한, 리허설 기반의 지식 융합 모듈을 통해 병합 가중치를 계산하고 융합을 수행합니다. 세 가지 CL 벤치마크에서 다양한 모델 크기(770M에서 13B)로 실험한 결과, AimMerging은 기존 최첨단 방법들에 비해 평균 80%와 59%의 상대적 성능 향상을 보여주었습니다. 이 연구는 지속적 학습에서 새로운 지식을 효과적으로 학습하면서도 기존 지식을 잊지 않도록 하는 데 기여합니다.

## 🎯 주요 포인트

- 1. 지속 학습은 대형 언어 모델을 동적 환경에 배치하는 데 필수적이며, AimMerging은 이를 위한 새로운 프레임워크를 제안합니다.
- 2. AimMerging은 학습 및 망각 신호를 이용하여 모델의 학습 상태를 동적으로 모니터링하고, 최적의 병합 타이밍과 빈도를 결정합니다.
- 3. 이 방법은 리허설 기반 지식 융합 모듈을 통해 병합 가중치를 계산하고 융합을 실행합니다.
- 4. AimMerging은 세 가지 지속 학습 벤치마크에서 평균 80%와 59%의 상대적 성능 향상을 달성했습니다.
- 5. 재현성을 위해 소스 코드가 제공됩니다.


---

*Generated on 2025-09-23 23:52:47*