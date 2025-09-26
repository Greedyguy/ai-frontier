---
keywords:
  - Cognitive Distortion
  - Large Language Model
  - Role-Switching Multi-LLM Negotiation
  - Synthetic Data Generation
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.00367
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:56:23.597324",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Cognitive Distortion",
    "Large Language Model",
    "Role-Switching Multi-LLM Negotiation",
    "Synthetic Data Generation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Cognitive Distortion": 0.8,
    "Large Language Model": 0.85,
    "Role-Switching Multi-LLM Negotiation": 0.7,
    "Synthetic Data Generation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Cognitive Distortion",
        "canonical": "Cognitive Distortion",
        "aliases": [
          "Negative Thinking Patterns"
        ],
        "category": "unique_technical",
        "rationale": "Cognitive distortion is a central theme of the study, providing a unique angle for linking research on mental health.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are crucial in the study's methodology, linking to broader NLP research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Role-Switching Multi-LLM Negotiation",
        "canonical": "Role-Switching Multi-LLM Negotiation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This novel method is specific to the study and enhances understanding of LLM interactions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.7
      },
      {
        "surface": "Synthetic Data Generation",
        "canonical": "Synthetic Data Generation",
        "aliases": [
          "Data Augmentation"
        ],
        "category": "specific_connectable",
        "rationale": "Synthetic data generation is a key technique for expanding datasets and improving model training.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "Dataset",
      "Implementation Details"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Cognitive Distortion",
      "resolved_canonical": "Cognitive Distortion",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Role-Switching Multi-LLM Negotiation",
      "resolved_canonical": "Role-Switching Multi-LLM Negotiation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Synthetic Data Generation",
      "resolved_canonical": "Synthetic Data Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# KoACD: The First Korean Adolescent Dataset for Cognitive Distortion Analysis via Role-Switching Multi-LLM Negotiation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.00367.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.00367](https://arxiv.org/abs/2505.00367)

## 🔗 유사한 논문
- [[2025-09-23/Multi-View Attention Multiple-Instance Learning Enhanced by LLM Reasoning for Cognitive Distortion Detection_20250923|Multi-View Attention Multiple-Instance Learning Enhanced by LLM Reasoning for Cognitive Distortion Detection]] (84.9% similar)
- [[2025-09-22/KatFishNet_ Detecting LLM-Generated Korean Text through Linguistic Feature Analysis_20250922|KatFishNet: Detecting LLM-Generated Korean Text through Linguistic Feature Analysis]] (79.6% similar)
- [[2025-09-23/Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning_20250923|Does Reasoning Introduce Bias? A Study of Social Bias Evaluation and Mitigation in LLM Reasoning]] (78.7% similar)
- [[2025-09-23/ReDepress_ A Cognitive Framework for Detecting Depression Relapse from Social Media_20250923|ReDepress: A Cognitive Framework for Detecting Depression Relapse from Social Media]] (78.5% similar)
- [[2025-09-23/AuditoryBench++_ Can Language Models Understand Auditory Knowledge without Hearing?_20250923|AuditoryBench++: Can Language Models Understand Auditory Knowledge without Hearing?]] (77.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Synthetic Data Generation|Synthetic Data Generation]]
**⚡ Unique Technical**: [[keywords/Cognitive Distortion|Cognitive Distortion]], [[keywords/Role-Switching Multi-LLM Negotiation|Role-Switching Multi-LLM Negotiation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.00367v2 Announce Type: replace-cross 
Abstract: Cognitive distortion refers to negative thinking patterns that can lead to mental health issues like depression and anxiety in adolescents. Previous studies using natural language processing (NLP) have focused mainly on small-scale adult datasets, with limited research on adolescents. This study introduces KoACD, the first large-scale dataset of cognitive distortions in Korean adolescents, containing 108,717 instances. We applied a multi-Large Language Model (LLM) negotiation method to refine distortion classification, enabling iterative feedback and role-switching between models to reduce bias and improve label consistency. In addition, we generated synthetic data using two approaches: cognitive clarification for textual clarity and cognitive balancing for diverse distortion representation. Validation through LLMs and expert evaluations showed that while LLMs classified distortions with explicit markers, they struggled with context-dependent reasoning, where human evaluators demonstrated higher accuracy. KoACD aims to enhance future research on cognitive distortion detection. The dataset and implementation details are publicly accessible.

## 📝 요약

이 연구는 청소년의 인지 왜곡을 탐구하며, 한국 청소년을 대상으로 한 대규모 데이터셋 KoACD를 소개합니다. 108,717개의 사례를 포함한 이 데이터셋은 인지 왜곡 분류를 개선하기 위해 다중 대형 언어 모델(LLM) 협상 방법을 적용하여 편향을 줄이고 라벨 일관성을 높였습니다. 또한, 인지 명료화와 인지 균형을 통해 합성 데이터를 생성했습니다. LLM과 전문가 평가를 통해 LLM이 명시적 표시가 있는 왜곡은 잘 분류했으나, 문맥에 의존하는 추론에서는 인간 평가자가 더 높은 정확성을 보였습니다. KoACD는 인지 왜곡 탐지 연구를 발전시키는 데 기여할 것입니다. 데이터셋과 구현 세부사항은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 이 연구는 한국 청소년의 인지 왜곡을 다룬 최초의 대규모 데이터셋인 KoACD를 소개하며, 108,717개의 사례를 포함하고 있습니다.
- 2. 다중 대형 언어 모델(LLM) 협상 방법을 적용하여 왜곡 분류를 개선하고, 모델 간 피드백과 역할 전환을 통해 편향을 줄이고 라벨 일관성을 높였습니다.
- 3. 인지 명료화와 인지 균형을 통해 텍스트 명확성과 다양한 왜곡 표현을 위한 합성 데이터를 생성했습니다.
- 4. LLM과 전문가 평가를 통해 LLM은 명시적 표시가 있는 왜곡을 잘 분류했으나, 맥락 의존적 추론에서는 인간 평가자가 더 높은 정확도를 보였습니다.
- 5. KoACD는 인지 왜곡 탐지에 관한 미래 연구를 강화하는 것을 목표로 하며, 데이터셋과 구현 세부사항은 공개적으로 접근 가능합니다.


---

*Generated on 2025-09-24 00:56:23*