---
keywords:
  - Trajectory Prediction
  - Role- and Domain-Aware Adapter
  - Contrastive Learning
  - Cross-Domain Trajectory Prediction
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.16095
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:19:58.741983",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Trajectory Prediction",
    "Role- and Domain-Aware Adapter",
    "Contrastive Learning",
    "Cross-Domain Trajectory Prediction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Trajectory Prediction": 0.79,
    "Role- and Domain-Aware Adapter": 0.82,
    "Contrastive Learning": 0.81,
    "Cross-Domain Trajectory Prediction": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Trajectory Prediction",
        "canonical": "Trajectory Prediction",
        "aliases": [
          "Trajectory Modeling"
        ],
        "category": "specific_connectable",
        "rationale": "Trajectory prediction is a key concept in modeling multi-agent systems, linking to various predictive modeling techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      },
      {
        "surface": "Role- and Domain-Aware Adapter",
        "canonical": "Role- and Domain-Aware Adapter",
        "aliases": [
          "Role-Aware Adapter",
          "Domain-Aware Adapter"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach specific to the paper, enhancing connectivity with domain adaptation techniques.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Hierarchical Contrastive Learning",
        "canonical": "Contrastive Learning",
        "aliases": [
          "Hierarchical Contrastive Learning"
        ],
        "category": "specific_connectable",
        "rationale": "Contrastive learning is a popular technique in machine learning, and its hierarchical variant adds specificity.",
        "novelty_score": 0.68,
        "connectivity_score": 0.83,
        "specificity_score": 0.76,
        "link_intent_score": 0.81
      },
      {
        "surface": "Cross-Domain Trajectory Prediction",
        "canonical": "Cross-Domain Trajectory Prediction",
        "aliases": [
          "Cross-Domain Prediction"
        ],
        "category": "unique_technical",
        "rationale": "This concept is crucial for linking different domain adaptation strategies in trajectory prediction.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
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
      "candidate_surface": "Trajectory Prediction",
      "resolved_canonical": "Trajectory Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Role- and Domain-Aware Adapter",
      "resolved_canonical": "Role- and Domain-Aware Adapter",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Hierarchical Contrastive Learning",
      "resolved_canonical": "Contrastive Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.83,
        "specificity": 0.76,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "Cross-Domain Trajectory Prediction",
      "resolved_canonical": "Cross-Domain Trajectory Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# AdaSports-Traj: Role- and Domain-Aware Adaptation for Multi-Agent Trajectory Modeling in Sports

**Korean Title:** AdaSports-Traj: 스포츠에서 다중 에이전트 궤적 모델링을 위한 역할 및 도메인 인식 적응

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16095.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.16095](https://arxiv.org/abs/2509.16095)

## 🔗 유사한 논문
- [[2025-09-19/STEP_ Structured Training and Evaluation Platform for benchmarking trajectory prediction models_20250919|STEP: Structured Training and Evaluation Platform for benchmarking trajectory prediction models]] (83.6% similar)
- [[2025-09-18/TrajBooster_ Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning_20250918|TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (80.5% similar)
- [[2025-09-22/Advances in Multimodal Adaptation and Generalization_ From Traditional Approaches to Foundation Models_20250922|Advances in Multimodal Adaptation and Generalization: From Traditional Approaches to Foundation Models]] (80.2% similar)
- [[2025-09-19/AgentCompass_ Towards Reliable Evaluation of Agentic Workflows in Production_20250919|AgentCompass: Towards Reliable Evaluation of Agentic Workflows in Production]] (79.9% similar)
- [[2025-09-19/Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems_20250919|Sentinel Agents for Secure and Trustworthy Agentic AI in Multi-Agent Systems]] (79.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Trajectory Prediction|Trajectory Prediction]], [[keywords/Contrastive Learning|Contrastive Learning]]
**⚡ Unique Technical**: [[keywords/Role- and Domain-Aware Adapter|Role- and Domain-Aware Adapter]], [[keywords/Cross-Domain Trajectory Prediction|Cross-Domain Trajectory Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16095v1 Announce Type: new 
Abstract: Trajectory prediction in multi-agent sports scenarios is inherently challenging due to the structural heterogeneity across agent roles (e.g., players vs. ball) and dynamic distribution gaps across different sports domains. Existing unified frameworks often fail to capture these structured distributional shifts, resulting in suboptimal generalization across roles and domains. We propose AdaSports-Traj, an adaptive trajectory modeling framework that explicitly addresses both intra-domain and inter-domain distribution discrepancies in sports. At its core, AdaSports-Traj incorporates a Role- and Domain-Aware Adapter to conditionally adjust latent representations based on agent identity and domain context. Additionally, we introduce a Hierarchical Contrastive Learning objective, which separately supervises role-sensitive and domain-aware representations to encourage disentangled latent structures without introducing optimization conflict. Experiments on three diverse sports datasets, Basketball-U, Football-U, and Soccer-U, demonstrate the effectiveness of our adaptive design, achieving strong performance in both unified and cross-domain trajectory prediction settings.

## 🔍 Abstract (한글 번역)

arXiv:2509.16095v1 발표 유형: 신규  
초록: 다중 에이전트 스포츠 시나리오에서의 궤적 예측은 에이전트 역할(예: 선수 대 공) 간의 구조적 이질성과 다양한 스포츠 도메인 간의 동적 분포 차이로 인해 본질적으로 어려운 문제입니다. 기존의 통합 프레임워크는 이러한 구조화된 분포적 변화를 포착하지 못하는 경우가 많아 역할 및 도메인 전반에 걸쳐 최적이 아닌 일반화를 초래합니다. 우리는 스포츠에서의 도메인 내 및 도메인 간 분포 불일치를 명시적으로 해결하는 적응형 궤적 모델링 프레임워크인 AdaSports-Traj를 제안합니다. AdaSports-Traj의 핵심은 에이전트 정체성과 도메인 맥락에 따라 잠재 표현을 조건부로 조정하는 역할 및 도메인 인식 어댑터를 통합하는 것입니다. 또한, 최적화 충돌을 일으키지 않고 분리된 잠재 구조를 장려하기 위해 역할 민감 및 도메인 인식 표현을 개별적으로 감독하는 계층적 대조 학습 목표를 도입합니다. 농구-U, 축구-U, 그리고 축구-U의 세 가지 다양한 스포츠 데이터셋에 대한 실험은 통합 및 도메인 간 궤적 예측 설정 모두에서 강력한 성능을 달성하며 우리의 적응형 설계의 효과를 입증합니다.

## 📝 요약

논문은 다중 에이전트 스포츠 시나리오에서의 궤적 예측 문제를 다룹니다. 기존의 통합 프레임워크는 에이전트 역할과 스포츠 도메인 간의 구조적 이질성을 잘 포착하지 못해 일반화에 한계가 있습니다. 이를 해결하기 위해 제안된 AdaSports-Traj는 에이전트의 정체성과 도메인 맥락에 따라 잠재 표현을 조정하는 역할 및 도메인 인식 어댑터를 포함합니다. 또한, 계층적 대조 학습 목표를 도입하여 역할과 도메인에 민감한 표현을 별도로 감독함으로써 잠재 구조를 명확히 분리합니다. 세 가지 스포츠 데이터셋에서 실험한 결과, 제안된 프레임워크는 통합 및 교차 도메인 궤적 예측에서 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 다중 에이전트 스포츠 시나리오에서의 궤적 예측은 에이전트 역할 간의 구조적 이질성과 스포츠 도메인 간의 동적 분포 차이로 인해 본질적으로 도전적입니다.
- 2. 기존의 통합 프레임워크는 이러한 구조적 분포 변화를 포착하지 못하여 역할 및 도메인 간 일반화가 최적화되지 않습니다.
- 3. AdaSports-Traj는 에이전트 정체성과 도메인 컨텍스트에 따라 잠재 표현을 조정하는 역할 및 도메인 인식 어댑터를 통합하여 분포 불일치를 해결합니다.
- 4. 계층적 대조 학습 목표를 도입하여 역할 민감성과 도메인 인식 표현을 별도로 감독함으로써 최적화 충돌 없이 분리된 잠재 구조를 장려합니다.
- 5. 세 가지 다양한 스포츠 데이터셋에서의 실험 결과, AdaSports-Traj의 적응형 설계가 통합 및 교차 도메인 궤적 예측 설정에서 강력한 성능을 발휘함을 보여줍니다.


---

*Generated on 2025-09-23 12:19:58*