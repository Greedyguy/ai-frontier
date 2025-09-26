---
keywords:
  - Large Language Model
  - User Interface Generation
  - Designer Feedback
  - Reinforcement Learning from Human Feedback
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.16779
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:15:23.280298",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "User Interface Generation",
    "Designer Feedback",
    "Reinforcement Learning from Human Feedback"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "User Interface Generation": 0.78,
    "Designer Feedback": 0.77,
    "Reinforcement Learning from Human Feedback": 0.8
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
        "rationale": "Essential for linking as it is the core technology being improved in the study.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "UI Generation",
        "canonical": "User Interface Generation",
        "aliases": [
          "UI Design Generation"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's focus on improving design models with feedback.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Designer Feedback",
        "canonical": "Designer Feedback",
        "aliases": [
          "Design Feedback"
        ],
        "category": "unique_technical",
        "rationale": "Key element in the study for enhancing model performance through human input.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.77
      },
      {
        "surface": "Reinforcement Learning from Human Feedback",
        "canonical": "Reinforcement Learning from Human Feedback",
        "aliases": [
          "RLHF"
        ],
        "category": "specific_connectable",
        "rationale": "Relevant for linking due to its role in training models with human input.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "study",
      "models"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "UI Generation",
      "resolved_canonical": "User Interface Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Designer Feedback",
      "resolved_canonical": "Designer Feedback",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Reinforcement Learning from Human Feedback",
      "resolved_canonical": "Reinforcement Learning from Human Feedback",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Improving User Interface Generation Models from Designer Feedback

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16779.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.16779](https://arxiv.org/abs/2509.16779)

## 🔗 유사한 논문
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL: Replacing Human Feedback for Reward Shaping]] (85.2% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (85.0% similar)
- [[2025-09-23/Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues_20250923|Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues]] (84.7% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (84.4% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning from Human Feedback|Reinforcement Learning from Human Feedback]]
**⚡ Unique Technical**: [[keywords/User Interface Generation|User Interface Generation]], [[keywords/Designer Feedback|Designer Feedback]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16779v1 Announce Type: cross 
Abstract: Despite being trained on vast amounts of data, most LLMs are unable to reliably generate well-designed UIs. Designer feedback is essential to improving performance on UI generation; however, we find that existing RLHF methods based on ratings or rankings are not well-aligned with designers' workflows and ignore the rich rationale used to critique and improve UI designs. In this paper, we investigate several approaches for designers to give feedback to UI generation models, using familiar interactions such as commenting, sketching and direct manipulation. We first perform a study with 21 designers where they gave feedback using these interactions, which resulted in ~1500 design annotations. We then use this data to finetune a series of LLMs to generate higher quality UIs. Finally, we evaluate these models with human judges, and we find that our designer-aligned approaches outperform models trained with traditional ranking feedback and all tested baselines, including GPT-5.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)이 사용자 인터페이스(UI)를 생성하는 데 있어 디자이너의 피드백이 중요하다는 점을 강조합니다. 기존의 순위 기반 강화 학습(RLHF) 방법은 디자이너의 작업 흐름과 잘 맞지 않으며, UI 디자인 개선에 사용되는 풍부한 논리를 무시합니다. 연구진은 디자이너가 댓글, 스케치, 직접 조작 등 익숙한 방식으로 피드백을 제공할 수 있는 여러 접근법을 조사했습니다. 21명의 디자이너와의 연구를 통해 약 1500개의 디자인 주석을 수집하고, 이를 기반으로 LLM을 미세 조정하여 더 높은 품질의 UI를 생성했습니다. 최종적으로 인간 평가자와의 평가에서 이러한 디자이너 중심 접근법이 기존의 순위 피드백 및 GPT-5를 포함한 모든 테스트된 기준 모델보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 대부분의 대형 언어 모델(LLM)은 방대한 데이터로 훈련되었음에도 불구하고 잘 설계된 UI를 생성하는 데 어려움을 겪고 있다.
- 2. 기존의 평가 기반 강화 학습(RLHF) 방법은 디자이너의 워크플로우와 잘 맞지 않으며, UI 디자인을 개선하기 위한 풍부한 근거를 무시하고 있다.
- 3. 디자이너가 주석 달기, 스케치, 직접 조작과 같은 익숙한 상호작용을 통해 UI 생성 모델에 피드백을 제공하는 여러 접근 방식을 조사하였다.
- 4. 21명의 디자이너가 참여한 연구에서 약 1500개의 디자인 주석이 수집되었으며, 이를 통해 LLM을 미세 조정하여 더 높은 품질의 UI를 생성하였다.
- 5. 인간 심사위원을 통해 평가한 결과, 디자이너와의 상호작용을 반영한 접근 방식이 기존의 순위 기반 피드백 및 GPT-5를 포함한 모든 테스트된 기준 모델보다 우수한 성능을 보였다.


---

*Generated on 2025-09-24 02:15:23*