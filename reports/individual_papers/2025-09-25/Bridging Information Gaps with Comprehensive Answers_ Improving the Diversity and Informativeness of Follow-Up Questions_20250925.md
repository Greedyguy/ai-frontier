---
keywords:
  - Large Language Model
  - Information Gap Knowledge Distillation
  - FollowupQG Dataset
  - Conversational Agents
  - Teacher-Student Models
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2502.17715
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:19:54.887891",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Information Gap Knowledge Distillation",
    "FollowupQG Dataset",
    "Conversational Agents",
    "Teacher-Student Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Information Gap Knowledge Distillation": 0.78,
    "FollowupQG Dataset": 0.77,
    "Conversational Agents": 0.8,
    "Teacher-Student Models": 0.79
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
        "rationale": "Large Language Models are central to the paper's methodology and are a well-established concept in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "information-gap-driven knowledge distillation",
        "canonical": "Information Gap Knowledge Distillation",
        "aliases": [
          "gap-driven distillation"
        ],
        "category": "unique_technical",
        "rationale": "This novel method is a key contribution of the paper, enhancing model training by focusing on information gaps.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "FollowupQG dataset",
        "canonical": "FollowupQG Dataset",
        "aliases": [
          "Followup Question Generation Dataset"
        ],
        "category": "unique_technical",
        "rationale": "The dataset is crucial for training models in the study and is specific to the paper's domain.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "conversational agents",
        "canonical": "Conversational Agents",
        "aliases": [
          "chatbots",
          "dialogue systems"
        ],
        "category": "specific_connectable",
        "rationale": "Conversational agents are the application focus of the paper, linking it to broader AI and NLP fields.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "teacher-student model pairs",
        "canonical": "Teacher-Student Models",
        "aliases": [
          "teacher-student architecture"
        ],
        "category": "specific_connectable",
        "rationale": "This architecture is a key mechanism in the paper for knowledge transfer and model training.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "comprehensive answers",
      "small models",
      "resource-constrained"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "information-gap-driven knowledge distillation",
      "resolved_canonical": "Information Gap Knowledge Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "FollowupQG dataset",
      "resolved_canonical": "FollowupQG Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "conversational agents",
      "resolved_canonical": "Conversational Agents",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "teacher-student model pairs",
      "resolved_canonical": "Teacher-Student Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Bridging Information Gaps with Comprehensive Answers: Improving the Diversity and Informativeness of Follow-Up Questions

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.17715.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2502.17715](https://arxiv.org/abs/2502.17715)

## 🔗 유사한 논문
- [[2025-09-23/A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue_20250923|A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue]] (85.1% similar)
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think: Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (83.2% similar)
- [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know: An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (83.1% similar)
- [[2025-09-25/Embedding Domain Knowledge for Large Language Models via Reinforcement Learning from Augmented Generation_20250925|Embedding Domain Knowledge for Large Language Models via Reinforcement Learning from Augmented Generation]] (83.0% similar)
- [[2025-09-25/The Knowledge-Behaviour Disconnect in LLM-based Chatbots_20250925|The Knowledge-Behaviour Disconnect in LLM-based Chatbots]] (83.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Conversational Agents|Conversational Agents]], [[keywords/Teacher-Student Models|Teacher-Student Models]]
**⚡ Unique Technical**: [[keywords/Information Gap Knowledge Distillation|Information Gap Knowledge Distillation]], [[keywords/FollowupQG Dataset|FollowupQG Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.17715v2 Announce Type: replace-cross 
Abstract: Generating diverse follow-up questions that uncover missing information remains challenging for conversational agents, particularly when they run on small, locally hosted models. To address this, we develop an information-gap-driven knowledge distillation pipeline in which a teacher LLM generates a comprehensive answer, contrasts it with the initial answer to identify information gaps, and formulates gap-bridging follow-up questions. Using this pipeline, we augment the existing FollowupQG dataset tenfold. We then fine-tune smaller student models on the augmented dataset to distill the teacher's knowledge. Experiments with selected teacher-student model pairs show that fine-tuned students achieve significantly higher informativeness and diversity than variations trained on the original dataset. These findings indicate that our pipeline, which mirrors the human cognitive process of information seeking, provides an efficient distillation channel from state-of-the-art LLMs to smaller models, enabling resource-constrained conversational systems to generate more diverse and informative follow-up questions.

## 📝 요약

이 논문은 대화형 에이전트가 다양한 후속 질문을 생성하는 데 어려움을 겪는 문제를 해결하기 위해 정보 격차 기반의 지식 증류 파이프라인을 제안합니다. 이 파이프라인에서는 대형 언어 모델(LLM)이 포괄적인 답변을 생성하고 초기 답변과 비교하여 정보 격차를 식별한 후, 그 격차를 메우는 후속 질문을 작성합니다. 이를 통해 기존 FollowupQG 데이터셋을 10배로 확장하고, 소형 모델을 미세 조정하여 대형 모델의 지식을 전달합니다. 실험 결과, 미세 조정된 소형 모델이 원래 데이터셋으로 훈련된 모델보다 정보성과 다양성이 크게 향상되었습니다. 이 연구는 자원이 제한된 대화 시스템이 더 다양하고 정보성 있는 후속 질문을 생성할 수 있도록 돕는 효율적인 방법을 제시합니다.

## 🎯 주요 포인트

- 1. 정보 격차를 메우기 위한 지식 증류 파이프라인을 개발하여 대화형 에이전트의 후속 질문 생성을 개선했습니다.
- 2. 교사 LLM이 포괄적인 답변을 생성하고 초기 답변과 비교하여 정보 격차를 식별한 후 이를 메우는 후속 질문을 작성합니다.
- 3. 개발한 파이프라인을 통해 기존 FollowupQG 데이터셋을 10배로 증강했습니다.
- 4. 증강된 데이터셋으로 소형 학생 모델을 미세 조정하여 교사의 지식을 증류하였습니다.
- 5. 실험 결과, 미세 조정된 학생 모델이 원본 데이터셋으로 훈련된 변형보다 정보성과 다양성에서 현저히 높은 성과를 보였습니다.


---

*Generated on 2025-09-25 16:19:54*