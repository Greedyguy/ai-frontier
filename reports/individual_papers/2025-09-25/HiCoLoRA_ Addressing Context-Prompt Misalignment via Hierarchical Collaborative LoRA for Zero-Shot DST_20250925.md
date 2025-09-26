---
keywords:
  - Zero-Shot Learning
  - Hierarchical Collaborative Low-Rank Adaptation
  - Task-Oriented Dialog Systems
  - Spectral Joint Domain-Slot Clustering
  - Semantic-Enhanced SVD Initialization
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19742
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:46:35.359937",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Zero-Shot Learning",
    "Hierarchical Collaborative Low-Rank Adaptation",
    "Task-Oriented Dialog Systems",
    "Spectral Joint Domain-Slot Clustering",
    "Semantic-Enhanced SVD Initialization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Zero-Shot Learning": 0.82,
    "Hierarchical Collaborative Low-Rank Adaptation": 0.79,
    "Task-Oriented Dialog Systems": 0.75,
    "Spectral Joint Domain-Slot Clustering": 0.72,
    "Semantic-Enhanced SVD Initialization": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Zero-shot Dialog State Tracking",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "zs-DST"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot learning is a trending concept that directly relates to the paper's focus on dialog state tracking without prior domain-specific data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Hierarchical Collaborative Low-Rank Adaptation",
        "canonical": "Hierarchical Collaborative Low-Rank Adaptation",
        "aliases": [
          "HiCoLoRA"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.91,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.79
      },
      {
        "surface": "Task-Oriented Dialog Systems",
        "canonical": "Task-Oriented Dialog Systems",
        "aliases": [
          "TODs"
        ],
        "category": "specific_connectable",
        "rationale": "Task-oriented dialog systems are a key application area for the proposed method, linking it to broader research in dialog systems.",
        "novelty_score": 0.48,
        "connectivity_score": 0.78,
        "specificity_score": 0.81,
        "link_intent_score": 0.75
      },
      {
        "surface": "Spectral Joint Domain-Slot Clustering",
        "canonical": "Spectral Joint Domain-Slot Clustering",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique is a specific innovation within the paper that enhances the framework's performance.",
        "novelty_score": 0.87,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Semantic-Enhanced SVD Initialization",
        "canonical": "Semantic-Enhanced SVD Initialization",
        "aliases": [
          "SemSVD-Init"
        ],
        "category": "unique_technical",
        "rationale": "This initialization method is a unique contribution that aids in preserving pre-trained knowledge.",
        "novelty_score": 0.89,
        "connectivity_score": 0.58,
        "specificity_score": 0.83,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "dialog context",
      "domain interference",
      "catastrophic forgetting"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Zero-shot Dialog State Tracking",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Hierarchical Collaborative Low-Rank Adaptation",
      "resolved_canonical": "Hierarchical Collaborative Low-Rank Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.91,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Task-Oriented Dialog Systems",
      "resolved_canonical": "Task-Oriented Dialog Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.78,
        "specificity": 0.81,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Spectral Joint Domain-Slot Clustering",
      "resolved_canonical": "Spectral Joint Domain-Slot Clustering",
      "decision": "linked",
      "scores": {
        "novelty": 0.87,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Semantic-Enhanced SVD Initialization",
      "resolved_canonical": "Semantic-Enhanced SVD Initialization",
      "decision": "linked",
      "scores": {
        "novelty": 0.89,
        "connectivity": 0.58,
        "specificity": 0.83,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# HiCoLoRA: Addressing Context-Prompt Misalignment via Hierarchical Collaborative LoRA for Zero-Shot DST

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19742.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19742](https://arxiv.org/abs/2509.19742)

## 🔗 유사한 논문
- [[2025-09-23/COLA_ Context-aware Language-driven Test-time Adaptation_20250923|COLA: Context-aware Language-driven Test-time Adaptation]] (82.4% similar)
- [[2025-09-22/CoDoL_ Conditional Domain Prompt Learning for Out-of-Distribution Generalization_20250922|CoDoL: Conditional Domain Prompt Learning for Out-of-Distribution Generalization]] (81.8% similar)
- [[2025-09-23/CLaC at DISRPT 2025_ Hierarchical Adapters for Cross-Framework Multi-lingual Discourse Relation Classification_20250923|CLaC at DISRPT 2025: Hierarchical Adapters for Cross-Framework Multi-lingual Discourse Relation Classification]] (81.7% similar)
- [[2025-09-18/Lost in Translation? Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation_20250918|Lost in Translation? Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation]] (81.6% similar)
- [[2025-09-18/AD-DINOv3_ Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration_20250918|AD-DINOv3: Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration]] (81.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Task-Oriented Dialog Systems|Task-Oriented Dialog Systems]]
**⚡ Unique Technical**: [[keywords/Hierarchical Collaborative Low-Rank Adaptation|Hierarchical Collaborative Low-Rank Adaptation]], [[keywords/Spectral Joint Domain-Slot Clustering|Spectral Joint Domain-Slot Clustering]], [[keywords/Semantic-Enhanced SVD Initialization|Semantic-Enhanced SVD Initialization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19742v1 Announce Type: cross 
Abstract: Zero-shot Dialog State Tracking (zs-DST) is essential for enabling Task-Oriented Dialog Systems (TODs) to generalize to new domains without costly data annotation. A central challenge lies in the semantic misalignment between dynamic dialog contexts and static prompts, leading to inflexible cross-layer coordination, domain interference, and catastrophic forgetting. To tackle this, we propose Hierarchical Collaborative Low-Rank Adaptation (HiCoLoRA), a framework that enhances zero-shot slot inference through robust prompt alignment. It features a hierarchical LoRA architecture for dynamic layer-specific processing (combining lower-layer heuristic grouping and higher-layer full interaction), integrates Spectral Joint Domain-Slot Clustering to identify transferable associations (feeding an Adaptive Linear Fusion Mechanism), and employs Semantic-Enhanced SVD Initialization (SemSVD-Init) to preserve pre-trained knowledge. Experiments on multi-domain datasets MultiWOZ and SGD show that HiCoLoRA outperforms baselines, achieving SOTA in zs-DST. Code is available at https://github.com/carsonz/HiCoLoRA.

## 📝 요약

이 논문은 새로운 도메인에 대한 데이터 주석 없이도 작업 지향 대화 시스템(TODs)이 일반화할 수 있도록 하는 제로샷 대화 상태 추적(zs-DST)의 문제를 다룹니다. 주요 기여는 동적 대화 맥락과 정적 프롬프트 간의 의미적 불일치를 해결하기 위한 Hierarchical Collaborative Low-Rank Adaptation(HiCoLoRA) 프레임워크 제안입니다. HiCoLoRA는 계층적 LoRA 아키텍처를 통해 동적 레이어별 처리를 수행하고, 스펙트럼 기반 도메인-슬롯 클러스터링을 통해 전이 가능한 연관성을 식별하며, Semantic-Enhanced SVD Initialization(SemSVD-Init)을 사용하여 사전 학습된 지식을 보존합니다. 실험 결과, HiCoLoRA는 MultiWOZ와 SGD 데이터셋에서 기존 방법들을 능가하며 제로샷 대화 상태 추적에서 최첨단 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. Zero-shot 대화 상태 추적(zs-DST)은 새로운 도메인에 일반화할 수 있는 작업 지향 대화 시스템(TODs)을 구현하는 데 필수적입니다.
- 2. HiCoLoRA는 동적 대화 맥락과 정적 프롬프트 간의 의미적 불일치를 해결하기 위해 제안된 프레임워크입니다.
- 3. HiCoLoRA는 계층적 LoRA 아키텍처를 통해 동적 계층별 처리를 강화하고, Spectral Joint Domain-Slot Clustering을 통합하여 전이 가능한 연관성을 식별합니다.
- 4. HiCoLoRA는 Semantic-Enhanced SVD Initialization(SemSVD-Init)을 사용하여 사전 학습된 지식을 보존합니다.
- 5. MultiWOZ와 SGD의 다중 도메인 데이터셋 실험에서 HiCoLoRA는 기존 모델을 능가하며 zs-DST에서 SOTA를 달성했습니다.


---

*Generated on 2025-09-25 15:46:35*