---
keywords:
  - Adversarial Scenario Generation
  - Preference Alignment
  - Autonomous Driving Systems
  - Linear Mode Connectivity
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20102
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:19:18.702121",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Adversarial Scenario Generation",
    "Preference Alignment",
    "Autonomous Driving Systems",
    "Linear Mode Connectivity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Adversarial Scenario Generation": 0.78,
    "Preference Alignment": 0.75,
    "Autonomous Driving Systems": 0.8,
    "Linear Mode Connectivity": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Adversarial Scenario Generation",
        "canonical": "Adversarial Scenario Generation",
        "aliases": [
          "Adversarial Scenario Creation",
          "Adversarial Scenario Design"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a unique approach to testing autonomous systems.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Preference Alignment",
        "canonical": "Preference Alignment",
        "aliases": [
          "Preference Matching",
          "Preference Optimization"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces a novel method of aligning preferences in adversarial scenarios, which is key to its contribution.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Autonomous Driving Systems",
        "canonical": "Autonomous Driving Systems",
        "aliases": [
          "Self-Driving Cars",
          "Driverless Vehicles"
        ],
        "category": "broad_technical",
        "rationale": "This is a fundamental application area for the proposed methods, linking it to broader research in autonomous systems.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Linear Mode Connectivity",
        "canonical": "Linear Mode Connectivity",
        "aliases": [
          "Linear Connectivity",
          "Mode Connectivity"
        ],
        "category": "unique_technical",
        "rationale": "Theoretical justification in the paper relies on this concept, making it crucial for understanding the methodology.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
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
      "candidate_surface": "Adversarial Scenario Generation",
      "resolved_canonical": "Adversarial Scenario Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Preference Alignment",
      "resolved_canonical": "Preference Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Autonomous Driving Systems",
      "resolved_canonical": "Autonomous Driving Systems",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Linear Mode Connectivity",
      "resolved_canonical": "Linear Mode Connectivity",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Steerable Adversarial Scenario Generation through Test-Time Preference Alignment

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20102.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20102](https://arxiv.org/abs/2509.20102)

## 🔗 유사한 논문
- [[2025-09-23/Safe Guaranteed Dynamics Exploration with Probabilistic Models_20250923|Safe Guaranteed Dynamics Exploration with Probabilistic Models]] (81.2% similar)
- [[2025-09-23/DriveDPO_ Policy Learning via Safety DPO For End-to-End Autonomous Driving_20250923|DriveDPO: Policy Learning via Safety DPO For End-to-End Autonomous Driving]] (80.9% similar)
- [[2025-09-24/Synthesizing Attitudes, Predicting Actions (SAPA)_ Behavioral Theory-Guided LLMs for Ridesourcing Mode Choice Modeling_20250924|Synthesizing Attitudes, Predicting Actions (SAPA): Behavioral Theory-Guided LLMs for Ridesourcing Mode Choice Modeling]] (80.2% similar)
- [[2025-09-24/Assistive Decision-Making for Right of Way Navigation at Uncontrolled Intersections_20250924|Assistive Decision-Making for Right of Way Navigation at Uncontrolled Intersections]] (80.2% similar)
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections: A Multi-Agent Reinforcement Learning Approach]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Autonomous Driving Systems|Autonomous Driving Systems]]
**⚡ Unique Technical**: [[keywords/Adversarial Scenario Generation|Adversarial Scenario Generation]], [[keywords/Preference Alignment|Preference Alignment]], [[keywords/Linear Mode Connectivity|Linear Mode Connectivity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20102v1 Announce Type: new 
Abstract: Adversarial scenario generation is a cost-effective approach for safety assessment of autonomous driving systems. However, existing methods are often constrained to a single, fixed trade-off between competing objectives such as adversariality and realism. This yields behavior-specific models that cannot be steered at inference time, lacking the efficiency and flexibility to generate tailored scenarios for diverse training and testing requirements. In view of this, we reframe the task of adversarial scenario generation as a multi-objective preference alignment problem and introduce a new framework named \textbf{S}teerable \textbf{A}dversarial scenario \textbf{GE}nerator (SAGE). SAGE enables fine-grained test-time control over the trade-off between adversariality and realism without any retraining. We first propose hierarchical group-based preference optimization, a data-efficient offline alignment method that learns to balance competing objectives by decoupling hard feasibility constraints from soft preferences. Instead of training a fixed model, SAGE fine-tunes two experts on opposing preferences and constructs a continuous spectrum of policies at inference time by linearly interpolating their weights. We provide theoretical justification for this framework through the lens of linear mode connectivity. Extensive experiments demonstrate that SAGE not only generates scenarios with a superior balance of adversariality and realism but also enables more effective closed-loop training of driving policies. Project page: https://tongnie.github.io/SAGE/.

## 📝 요약

자율주행 시스템의 안전성을 평가하기 위한 적대적 시나리오 생성은 비용 효율적인 방법입니다. 그러나 기존 방법은 적대성과 현실성 간의 고정된 균형에 제한되어 있어 다양한 요구에 맞춘 시나리오를 생성하는 데 비효율적입니다. 이를 해결하기 위해 우리는 적대적 시나리오 생성을 다중 목표 선호도 정렬 문제로 재구성하고, \textbf{S}teerable \textbf{A}dversarial scenario \textbf{GE}nerator (SAGE)라는 새로운 프레임워크를 제안합니다. SAGE는 테스트 시점에서 적대성과 현실성 간의 균형을 세밀하게 조정할 수 있으며, 재훈련 없이도 가능합니다. 계층적 그룹 기반 선호 최적화를 통해 경쟁 목표를 균형 있게 조정하고, 두 전문가의 가중치를 선형 보간하여 다양한 정책을 생성합니다. 이 방법은 이론적으로 선형 모드 연결성을 통해 정당화됩니다. 실험 결과, SAGE는 적대성과 현실성의 균형을 잘 맞춘 시나리오를 생성하며, 주행 정책의 효과적인 폐쇄 루프 훈련을 가능하게 합니다.

## 🎯 주요 포인트

- 1. 자율주행 시스템의 안전성 평가를 위한 적대적 시나리오 생성은 비용 효율적인 접근 방식이다.
- 2. 기존 방법은 적대성과 현실성 간의 고정된 절충안에 제한되어 있어 다양한 요구에 맞춘 시나리오 생성에 비효율적이다.
- 3. SAGE 프레임워크는 적대성과 현실성 간의 절충을 테스트 시점에서 세밀하게 조정할 수 있도록 한다.
- 4. SAGE는 두 전문가의 가중치를 선형 보간하여 연속적인 정책 스펙트럼을 생성함으로써 다양한 목표를 균형 있게 달성한다.
- 5. 실험 결과, SAGE는 적대성과 현실성의 균형이 우수한 시나리오를 생성하며, 주행 정책의 폐쇄 루프 훈련을 더욱 효과적으로 지원한다.


---

*Generated on 2025-09-25 15:19:18*