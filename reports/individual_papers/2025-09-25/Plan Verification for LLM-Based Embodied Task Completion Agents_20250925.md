---
keywords:
  - Large Language Model
  - Plan Verification
  - Embodied AI
  - Imitation Learning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.02761
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:13:33.214600",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Plan Verification",
    "Embodied AI",
    "Imitation Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Plan Verification": 0.78,
    "Embodied AI": 0.8,
    "Imitation Learning": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's methodology, enabling connections to a wide range of AI and NLP literature.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Plan Verification",
        "canonical": "Plan Verification",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A unique concept introduced in the paper, crucial for understanding the iterative framework proposed.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Embodied AI",
        "canonical": "Embodied AI",
        "aliases": [
          "Embodied Artificial Intelligence"
        ],
        "category": "specific_connectable",
        "rationale": "Key application domain of the study, linking to research in robotics and AI.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Imitation Learning",
        "canonical": "Imitation Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Relevant for linking to machine learning methods focused on learning from demonstrations.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Plan Verification",
      "resolved_canonical": "Plan Verification",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Embodied AI",
      "resolved_canonical": "Embodied AI",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Imitation Learning",
      "resolved_canonical": "Imitation Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Plan Verification for LLM-Based Embodied Task Completion Agents

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.02761.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.02761](https://arxiv.org/abs/2509.02761)

## 🔗 유사한 논문
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (85.8% similar)
- [[2025-09-24/LogicGuard_ Improving Embodied LLM agents through Temporal Logic based Critics_20250924|LogicGuard: Improving Embodied LLM agents through Temporal Logic based Critics]] (85.1% similar)
- [[2025-09-19/ThinkAct_ Vision-Language-Action Reasoning via Reinforced Visual Latent Planning_20250919|ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (84.9% similar)
- [[2025-09-24/Reflect before Act_ Proactive Error Correction in Language Models_20250924|Reflect before Act: Proactive Error Correction in Language Models]] (84.9% similar)
- [[2025-09-23/Runaway is Ashamed, But Helpful_ On the Early-Exit Behavior of Large Language Model-based Agents in Embodied Environments_20250923|Runaway is Ashamed, But Helpful: On the Early-Exit Behavior of Large Language Model-based Agents in Embodied Environments]] (84.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Embodied AI|Embodied AI]], [[keywords/Imitation Learning|Imitation Learning]]
**⚡ Unique Technical**: [[keywords/Plan Verification|Plan Verification]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.02761v3 Announce Type: replace 
Abstract: Large language model (LLM) based task plans and corresponding human demonstrations for embodied AI may be noisy, with unnecessary actions, redundant navigation, and logical errors that reduce policy quality. We propose an iterative verification framework in which a Judge LLM critiques action sequences and a Planner LLM applies the revisions, yielding progressively cleaner and more spatially coherent trajectories. Unlike rule-based approaches, our method relies on natural language prompting, enabling broad generalization across error types including irrelevant actions, contradictions, and missing steps. On a set of manually annotated actions from the TEACh embodied AI dataset, our framework achieves up to 90% recall and 100% precision across four state-of-the-art LLMs (GPT o4-mini, DeepSeek-R1, Gemini 2.5, LLaMA 4 Scout). The refinement loop converges quickly, with 96.5% of sequences requiring at most three iterations, while improving both temporal efficiency and spatial action organization. Crucially, the method preserves human error-recovery patterns rather than collapsing them, supporting future work on robust corrective behavior. By establishing plan verification as a reliable LLM capability for spatial planning and action refinement, we provide a scalable path to higher-quality training data for imitation learning in embodied AI.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 기반으로 한 체화된 AI의 작업 계획과 인간 시연이 불필요한 행동, 중복된 이동, 논리적 오류로 인해 정책 품질이 저하될 수 있음을 지적합니다. 이를 해결하기 위해, 판사 LLM이 행동 순서를 비판하고 계획자 LLM이 수정 사항을 적용하는 반복 검증 프레임워크를 제안합니다. 이 방법은 자연어 프롬프트를 사용하여 다양한 오류 유형에 대해 일반화할 수 있으며, TEACh 데이터셋에서 높은 정밀도와 재현율을 달성했습니다. 이 프레임워크는 빠르게 수렴하며, 인간의 오류 회복 패턴을 유지하여 체화된 AI의 모방 학습을 위한 고품질 교육 데이터를 제공하는 데 기여합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM) 기반의 작업 계획과 인간 시연은 불필요한 행동, 중복된 탐색, 논리적 오류로 인해 정책 품질이 저하될 수 있습니다.
- 2. 제안된 반복 검증 프레임워크는 Judge LLM이 행동 시퀀스를 비판하고 Planner LLM이 수정 사항을 적용하여 점진적으로 더 깨끗하고 공간적으로 일관된 경로를 생성합니다.
- 3. 이 방법은 자연어 프롬프트를 사용하여 관련 없는 행동, 모순, 누락된 단계 등 다양한 오류 유형에 대해 광범위한 일반화를 가능하게 합니다.
- 4. TEACh embodied AI 데이터셋의 수동 주석된 행동 세트에서, 제안된 프레임워크는 네 가지 최첨단 LLM에서 최대 90%의 재현율과 100%의 정밀도를 달성합니다.
- 5. 이 방법은 인간의 오류 회복 패턴을 유지하면서 공간 계획 및 행동 정제를 위한 신뢰할 수 있는 LLM 기능으로 계획 검증을 확립하여 모방 학습을 위한 고품질 훈련 데이터로의 확장 가능한 경로를 제공합니다.


---

*Generated on 2025-09-25 16:13:33*