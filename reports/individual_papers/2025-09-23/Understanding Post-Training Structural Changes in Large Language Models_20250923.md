---
keywords:
  - Large Language Model
  - Instruction Tuning
  - Long-CoT Distillation
  - Singular Value Decomposition
  - Attention Mechanism
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17866
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:11:24.370883",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Instruction Tuning",
    "Long-CoT Distillation",
    "Singular Value Decomposition",
    "Attention Mechanism"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Instruction Tuning": 0.78,
    "Long-CoT Distillation": 0.82,
    "Singular Value Decomposition": 0.77,
    "Attention Mechanism": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study, linking to foundational concepts in NLP and AI.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Instruction Tuning",
        "canonical": "Instruction Tuning",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific post-training method analyzed in the paper, relevant for understanding LLM adaptation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Long-Chain-of-Thought Distillation",
        "canonical": "Long-CoT Distillation",
        "aliases": [
          "Long-CoT"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel post-training technique critical to the paper's findings.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Singular Value Decomposition",
        "canonical": "Singular Value Decomposition",
        "aliases": [
          "SVD"
        ],
        "category": "specific_connectable",
        "rationale": "Key analytical method used to understand structural changes in LLMs.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "Attention Mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Fundamental to understanding the modulation of attention scores in LLMs.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "post-training",
      "parameter space",
      "performance degradation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
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
      "candidate_surface": "Instruction Tuning",
      "resolved_canonical": "Instruction Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Long-Chain-of-Thought Distillation",
      "resolved_canonical": "Long-CoT Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Singular Value Decomposition",
      "resolved_canonical": "Singular Value Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Attention Mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Understanding Post-Training Structural Changes in Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17866.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17866](https://arxiv.org/abs/2509.17866)

## 🔗 유사한 논문
- [[2025-09-22/Natural Fingerprints of Large Language Models_20250922|Natural Fingerprints of Large Language Models]] (83.4% similar)
- [[2025-09-23/Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels_20250923|Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels]] (83.3% similar)
- [[2025-09-22/Characterizing the Efficiency of Distributed Training_ A Power, Performance, and Thermal Perspective_20250922|Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective]] (82.6% similar)
- [[2025-09-22/Not All Parameters Are Created Equal_ Smart Isolation Boosts Fine-Tuning Performance_20250922|Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance]] (82.6% similar)
- [[2025-09-22/RePIC_ Reinforced Post-Training for Personalizing Multi-Modal Language Models_20250922|RePIC: Reinforced Post-Training for Personalizing Multi-Modal Language Models]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Singular Value Decomposition|Singular Value Decomposition]], [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Instruction Tuning|Instruction Tuning]], [[keywords/Long-CoT Distillation|Long-CoT Distillation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17866v1 Announce Type: cross 
Abstract: Post-training fundamentally alters the behavior of large language models (LLMs), yet its impact on the internal parameter space remains poorly understood. In this work, we conduct a systematic singular value decomposition (SVD) analysis of principal linear layers in pretrained LLMs, focusing on two widely adopted post-training methods: instruction tuning and long-chain-of-thought (Long-CoT) distillation. Our analysis reveals two consistent and unexpected structural changes:(1) a near-uniform geometric scaling of singular values across layers, which theoretically modulates attention scores; and (2) highly consistent orthogonal transformations are applied to the left and right singular vectors of each matrix. Disrupting this orthogonal consistency leads to catastrophic performance degradation. Based on these findings, we propose a simple yet effective framework that interprets post-training as a reparameterization of fixed subspaces in the pretrained parameter space. Further experiments reveal that singular value scaling behaves as a secondary effect, analogous to a temperature adjustment, whereas the core functional transformation lies in the coordinated rotation of singular vectors. These results challenge the prevailing view of the parameter space in large models as a black box, uncovering the first clear regularities in how parameters evolve during training, and providing a new perspective for deeper investigation into model parameter changes.

## 📝 요약

이 연구는 대규모 언어 모델(LLM)의 사후 훈련이 내부 매개변수 공간에 미치는 영향을 분석합니다. 저자들은 사후 훈련 방법인 지시 조정과 긴 사고 체인(Long-CoT) 증류에 초점을 맞춰, 주요 선형 계층의 특이값 분해(SVD)를 체계적으로 수행했습니다. 분석 결과, 계층 전반에 걸친 특이값의 거의 균일한 기하학적 스케일링과 각 행렬의 좌우 특이 벡터에 일관된 직교 변환이 발견되었습니다. 이러한 직교 일관성을 방해하면 성능이 급격히 저하됩니다. 연구는 사후 훈련을 사전 훈련된 매개변수 공간의 고정된 부분 공간의 재매개변수화로 해석하는 간단하고 효과적인 프레임워크를 제안합니다. 실험 결과, 특이값 스케일링은 온도 조정과 유사한 2차 효과이며, 핵심 기능적 변환은 특이 벡터의 조정된 회전에 있음을 밝혔습니다. 이 결과는 대규모 모델의 매개변수 공간을 블랙박스로 보는 기존 관점을 도전하며, 매개변수 변화에 대한 새로운 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 사후 훈련은 대형 언어 모델(LLM)의 내부 매개변수 공간에 예상치 못한 구조적 변화를 초래한다.
- 2. 특이값 분해(SVD) 분석 결과, 층 전반에 걸쳐 거의 균일한 기하학적 스케일링이 발생하며 이는 주의(attention) 점수를 조절한다.
- 3. 왼쪽과 오른쪽 특이 벡터에 일관된 직교 변환이 적용되며, 이 일관성이 깨지면 성능이 크게 저하된다.
- 4. 사후 훈련은 사전 훈련된 매개변수 공간의 고정된 부분 공간을 재매개변수화하는 것으로 해석될 수 있다.
- 5. 특이값 스케일링은 부차적 효과로 작용하며, 특이 벡터의 회전이 핵심 기능적 변화를 이끈다.


---

*Generated on 2025-09-24 00:11:24*