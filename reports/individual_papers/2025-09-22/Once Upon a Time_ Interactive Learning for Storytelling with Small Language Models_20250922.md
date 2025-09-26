---
keywords:
  - Interactive Learning
  - Storytelling
  - Cognitively Inspired Feedback
  - Large Language Model
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15714
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:11:23.898204",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Interactive Learning",
    "Storytelling",
    "Cognitively Inspired Feedback",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Interactive Learning": 0.82,
    "Storytelling": 0.75,
    "Cognitively Inspired Feedback": 0.78,
    "Large Language Model": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Interactive Learning",
        "canonical": "Interactive Learning",
        "aliases": [
          "Interactive Training"
        ],
        "category": "specific_connectable",
        "rationale": "Interactive learning is a key aspect of the paper's approach, offering a novel perspective on language model training.",
        "novelty_score": 0.65,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Storytelling",
        "canonical": "Storytelling",
        "aliases": [
          "Narrative Generation"
        ],
        "category": "unique_technical",
        "rationale": "Storytelling is the primary application explored, providing a unique context for language model evaluation.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Cognitively Inspired Feedback",
        "canonical": "Cognitively Inspired Feedback",
        "aliases": [
          "Cognitive Feedback"
        ],
        "category": "unique_technical",
        "rationale": "This feedback mechanism is a novel approach to improving language models, distinct from traditional methods.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language Model"
        ],
        "category": "broad_technical",
        "rationale": "Large language models are central to the paper's investigation, providing a basis for comparison.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "next-word prediction",
      "teacher model",
      "student model"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Interactive Learning",
      "resolved_canonical": "Interactive Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Storytelling",
      "resolved_canonical": "Storytelling",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Cognitively Inspired Feedback",
      "resolved_canonical": "Cognitively Inspired Feedback",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Once Upon a Time: Interactive Learning for Storytelling with Small Language Models

**Korean Title:** 옛날 옛적에: 소형 언어 모델을 활용한 스토리텔링을 위한 상호작용 학습

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15714.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15714](https://arxiv.org/abs/2509.15714)

## 🔗 유사한 논문
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (82.0% similar)
- [[2025-09-19/From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery: Reinforced Distillation of Large Language Model Agents]] (81.7% similar)
- [[2025-09-19/Controlling Language Difficulty in Dialogues with Linguistic Features_20250919|Controlling Language Difficulty in Dialogues with Linguistic Features]] (81.4% similar)
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (81.2% similar)
- [[2025-09-22/Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation_20250922|Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Interactive Learning|Interactive Learning]]
**⚡ Unique Technical**: [[keywords/Storytelling|Storytelling]], [[keywords/Cognitively Inspired Feedback|Cognitively Inspired Feedback]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15714v1 Announce Type: cross 
Abstract: Children efficiently acquire language not just by listening, but by interacting with others in their social environment. Conversely, large language models are typically trained with next-word prediction on massive amounts of text. Motivated by this contrast, we investigate whether language models can be trained with less data by learning not only from next-word prediction but also from high-level, cognitively inspired feedback. We train a student model to generate stories, which a teacher model rates on readability, narrative coherence, and creativity. By varying the amount of pretraining before the feedback loop, we assess the impact of this interactive learning on formal and functional linguistic competence. We find that the high-level feedback is highly data efficient: With just 1 M words of input in interactive learning, storytelling skills can improve as much as with 410 M words of next-word prediction.

## 🔍 Abstract (한글 번역)

arXiv:2509.15714v1 발표 유형: 교차  
초록: 어린이는 단순히 듣는 것만으로 언어를 습득하는 것이 아니라, 사회적 환경에서 다른 사람들과 상호작용함으로써 효율적으로 언어를 습득합니다. 반면에, 대규모 언어 모델은 일반적으로 방대한 양의 텍스트에 대한 다음 단어 예측을 통해 훈련됩니다. 이 대조에서 영감을 받아, 우리는 언어 모델이 다음 단어 예측뿐만 아니라 고차원적이고 인지적으로 영감을 받은 피드백을 통해 학습함으로써 더 적은 데이터로 훈련될 수 있는지 조사합니다. 우리는 학생 모델이 이야기를 생성하도록 훈련하고, 교사 모델이 가독성, 서사적 일관성 및 창의성에 대해 이를 평가합니다. 피드백 루프 이전의 사전 훈련 양을 조정하여, 이러한 상호작용 학습이 형식적 및 기능적 언어 능력에 미치는 영향을 평가합니다. 우리는 고차원 피드백이 매우 데이터 효율적임을 발견했습니다: 상호작용 학습에서 단 100만 단어의 입력만으로도 이야기 기술이 4억 1천만 단어의 다음 단어 예측만큼 향상될 수 있습니다.

## 📝 요약

이 논문은 아동이 사회적 상호작용을 통해 언어를 습득하는 방식과 대조적으로, 대형 언어 모델이 대량의 텍스트를 통해 다음 단어 예측으로 학습하는 점에 주목합니다. 연구에서는 언어 모델이 고차원적인 인지 피드백을 통해 더 적은 데이터로 학습할 수 있는지를 탐구합니다. 학생 모델이 이야기를 생성하면, 교사 모델이 가독성, 서사적 일관성, 창의성 측면에서 이를 평가합니다. 사전 학습량을 조절하여 상호작용 학습이 언어적 능력에 미치는 영향을 분석한 결과, 100만 단어의 상호작용 학습으로도 4억 1천만 단어의 예측 학습과 동일한 수준의 이야기 생성 능력 향상을 이룰 수 있음을 발견했습니다.

## 🎯 주요 포인트

- 1. 어린이는 사회적 환경에서 상호작용을 통해 언어를 효율적으로 습득한다는 점을 바탕으로 연구가 진행되었다.
- 2. 대형 언어 모델은 주로 대량의 텍스트를 통해 다음 단어 예측으로 훈련되지만, 본 연구는 인지적으로 영감을 받은 피드백을 통해 더 적은 데이터로 훈련할 수 있는지를 조사하였다.
- 3. 학생 모델이 이야기를 생성하고, 교사 모델이 가독성, 서사적 일관성, 창의성 측면에서 이를 평가하는 방식으로 훈련이 진행되었다.
- 4. 상호작용 학습에서 고수준의 피드백은 매우 데이터 효율적이며, 100만 단어의 입력만으로도 4억 1천만 단어의 다음 단어 예측과 동일한 수준의 이야기 생성 능력 향상을 이끌어낼 수 있었다.
- 5. 피드백 루프 이전의 사전 훈련 양을 조절하여 상호작용 학습이 언어적 능력에 미치는 영향을 평가하였다.


---

*Generated on 2025-09-23 09:11:23*