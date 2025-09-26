<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:40:52.638518",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Planorama",
    "Reinforcement Learning from Human Feedback",
    "ChatbotArena"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Planorama": 0.7,
    "Reinforcement Learning from Human Feedback": 0.8,
    "ChatbotArena": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study as it discusses alignment and helpfulness of LLM-generated plans.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Planorama",
        "canonical": "Planorama",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A unique interface used in the study to evaluate plan helpfulness and user preferences.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Reinforcement Learning from Human Feedback",
        "canonical": "Reinforcement Learning from Human Feedback",
        "aliases": [
          "RLHF"
        ],
        "category": "specific_connectable",
        "rationale": "A key method discussed for aligning LLM plans with user preferences.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "ChatbotArena",
        "canonical": "ChatbotArena",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific evaluation platform mentioned in the context of user preference testing.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.75,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "plan",
      "user preferences",
      "helpfulness"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Planorama",
      "resolved_canonical": "Planorama",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Reinforcement Learning from Human Feedback",
      "resolved_canonical": "Reinforcement Learning from Human Feedback",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "ChatbotArena",
      "resolved_canonical": "ChatbotArena",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.75,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# A Good Plan is Hard to Find: Aligning Models with Preferences is Misaligned with What Helps Users

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18632.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.18632](https://arxiv.org/abs/2509.18632)

## 🔗 유사한 논문
- [[2025-09-23/Improving User Interface Generation Models from Designer Feedback_20250923|Improving User Interface Generation Models from Designer Feedback]] (86.8% similar)
- [[2025-09-23/Challenging the Evaluator_ LLM Sycophancy Under User Rebuttal_20250923|Challenging the Evaluator: LLM Sycophancy Under User Rebuttal]] (85.9% similar)
- [[2025-09-22/Subjective Behaviors and Preferences in LLM_ Language of Browsing_20250922|Subjective Behaviors and Preferences in LLM: Language of Browsing]] (85.9% similar)
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (85.2% similar)
- [[2025-09-23/Strategic Dishonesty Can Undermine AI Safety Evaluations of Frontier LLM_20250923|Strategic Dishonesty Can Undermine AI Safety Evaluations of Frontier LLM]] (84.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning from Human Feedback|Reinforcement Learning from Human Feedback]]
**⚡ Unique Technical**: [[keywords/Planorama|Planorama]], [[keywords/ChatbotArena|ChatbotArena]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18632v1 Announce Type: new 
Abstract: To assist users in complex tasks, LLMs generate plans: step-by-step instructions towards a goal. While alignment methods aim to ensure LLM plans are helpful, they train (RLHF) or evaluate (ChatbotArena) on what users prefer, assuming this reflects what helps them. We test this with Planorama: an interface where 126 users answer 300 multi-step questions with LLM plans. We get 4388 plan executions and 5584 comparisons to measure plan helpfulness (QA success) and user preferences on plans, and recreate the setup in agents and reward models to see if they simulate or prefer what helps users. We expose: 1) user/model preferences and agent success do not accurately predict which plans help users, so common alignment feedback can misalign with helpfulness; 2) this gap is not due to user-specific preferences, as users are similarly successful when using plans they prefer/disprefer; 3) surface-level cues like brevity and question similarity strongly link to preferences, but such biases fail to predict helpfulness. In all, we argue aligning helpful LLMs needs feedback from real user interactions, not just preferences of what looks helpful, so we discuss the plan NLP researchers can execute to solve this problem.

## 📝 요약

이 논문은 복잡한 작업을 돕기 위해 LLMs(대형 언어 모델)가 생성하는 계획의 유용성을 평가합니다. Planorama라는 인터페이스를 통해 126명의 사용자가 300개의 다단계 질문에 대해 LLM 계획을 사용하여 답변하도록 하였고, 4388개의 계획 실행과 5584개의 비교를 통해 계획의 유용성과 사용자 선호도를 측정했습니다. 연구 결과, 사용자 및 모델의 선호도와 에이전트의 성공이 실제 사용자에게 도움이 되는 계획을 정확히 예측하지 못한다는 점을 밝혔습니다. 또한, 사용자 선호도와 계획의 유용성 간의 차이는 표면적인 요소에 기인하며, 실제 사용자 상호작용을 통한 피드백이 필요하다고 주장합니다.

## 🎯 주요 포인트

- 1. 사용자 및 모델의 선호도와 에이전트의 성공 여부는 사용자에게 도움이 되는 계획을 정확히 예측하지 못한다.
- 2. 사용자별 선호도 차이로 인한 것이 아니며, 사용자는 선호하는 계획과 선호하지 않는 계획을 사용할 때 유사한 성공률을 보인다.
- 3. 간결함 및 질문 유사성과 같은 표면적 단서는 선호도와 강하게 연결되지만, 이러한 편향은 유용성을 예측하지 못한다.
- 4. 유용한 LLM을 정렬하려면 겉보기의 유용성에 대한 선호도가 아닌 실제 사용자 상호작용에서 피드백을 받아야 한다.


---

*Generated on 2025-09-24 15:40:52*