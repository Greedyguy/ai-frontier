<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:33:56.541717",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Spoken Dialogue Models",
    "Audio Language Models",
    "Reinforcement Learning",
    "ChatReward-30K Dataset",
    "WavReward Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Spoken Dialogue Models": 0.82,
    "Audio Language Models": 0.8,
    "Reinforcement Learning": 0.78,
    "ChatReward-30K Dataset": 0.85,
    "WavReward Model": 0.88
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "spoken dialogue models",
        "canonical": "Spoken Dialogue Models",
        "aliases": [
          "spoken dialogue systems",
          "spoken conversational models"
        ],
        "category": "specific_connectable",
        "rationale": "This term is central to the paper's focus on evaluating conversational performance in audio-based systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "audio language models",
        "canonical": "Audio Language Models",
        "aliases": [
          "audio-based language models"
        ],
        "category": "specific_connectable",
        "rationale": "These models are crucial for understanding and processing spoken dialogue, linking to broader NLP and audio processing fields.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "reinforcement learning algorithm",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL",
          "reinforcement learning methods"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement learning is a key technique used in the paper for training evaluators, connecting to machine learning methodologies.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.68,
        "link_intent_score": 0.78
      },
      {
        "surface": "ChatReward-30K",
        "canonical": "ChatReward-30K Dataset",
        "aliases": [
          "ChatReward dataset"
        ],
        "category": "unique_technical",
        "rationale": "This dataset is uniquely introduced in the paper and is pivotal for training the proposed evaluation model.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "WavReward",
        "canonical": "WavReward Model",
        "aliases": [
          "WavReward"
        ],
        "category": "unique_technical",
        "rationale": "WavReward is the central innovation of the paper, providing a novel evaluation mechanism for spoken dialogue systems.",
        "novelty_score": 0.78,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "spoken dialogue models",
      "resolved_canonical": "Spoken Dialogue Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "audio language models",
      "resolved_canonical": "Audio Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "reinforcement learning algorithm",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.68,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "ChatReward-30K",
      "resolved_canonical": "ChatReward-30K Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "WavReward",
      "resolved_canonical": "WavReward Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    }
  ]
}
-->

# WavReward: Spoken Dialogue Models With Generalist Reward Evaluators

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.09558.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2505.09558](https://arxiv.org/abs/2505.09558)

## 🔗 유사한 논문
- [[2025-09-23/R3_ Robust Rubric-Agnostic Reward Models_20250923|R3: Robust Rubric-Agnostic Reward Models]] (83.4% similar)
- [[2025-09-22/reWordBench_ Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs_20250922|reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs]] (83.2% similar)
- [[2025-09-23/SoundMind_ RL-Incentivized Logic Reasoning for Audio-Language Models_20250923|SoundMind: RL-Incentivized Logic Reasoning for Audio-Language Models]] (82.8% similar)
- [[2025-09-22/BaseReward_ A Strong Baseline for Multimodal Reward Model_20250922|BaseReward: A Strong Baseline for Multimodal Reward Model]] (82.1% similar)
- [[2025-09-24/Explore the Reinforcement Learning for the LLM based ASR and TTS system_20250924|Explore the Reinforcement Learning for the LLM based ASR and TTS system]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🔗 Specific Connectable**: [[keywords/Spoken Dialogue Models|Spoken Dialogue Models]], [[keywords/Audio Language Models|Audio Language Models]]
**⚡ Unique Technical**: [[keywords/ChatReward-30K Dataset|ChatReward-30K Dataset]], [[keywords/WavReward Model|WavReward Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.09558v2 Announce Type: replace-cross 
Abstract: End-to-end spoken dialogue models such as GPT-4o-audio have recently garnered significant attention in the speech domain. However, the evaluation of spoken dialogue models' conversational performance has largely been overlooked. This is primarily due to the intelligent chatbots convey a wealth of non-textual information which cannot be easily measured using text-based language models like ChatGPT. To address this gap, we propose WavReward, a reward feedback model based on audio language models that can evaluate both the IQ and EQ of spoken dialogue systems with speech input. Specifically, 1) based on audio language models, WavReward incorporates the deep reasoning process and the nonlinear reward mechanism for post-training. By utilizing multi-sample feedback via the reinforcement learning algorithm, we construct a specialized evaluator tailored to spoken dialogue models. 2) We introduce ChatReward-30K, a preference dataset used to train WavReward. ChatReward-30K includes both comprehension and generation aspects of spoken dialogue models. These scenarios span various tasks, such as text-based chats, nine acoustic attributes of instruction chats, and implicit chats. WavReward outperforms previous state-of-the-art evaluation models across multiple spoken dialogue scenarios, achieving a substantial improvement about Qwen2.5-Omni in objective accuracy from 53.4$\%$ to 91.5$\%$. In subjective A/B testing, WavReward also leads by a margin of 83$\%$. Comprehensive ablation studies confirm the necessity of each component of WavReward. All data and code will be publicly at https://github.com/jishengpeng/WavReward after the paper is accepted.

## 📝 요약

최근 음성 대화 모델인 GPT-4o-audio가 주목받고 있지만, 대화 성능 평가가 미흡했습니다. 이를 해결하기 위해 우리는 음성 입력을 사용하는 대화 시스템의 IQ와 EQ를 평가할 수 있는 오디오 기반 보상 피드백 모델인 WavReward를 제안합니다. WavReward는 심층 추론 과정과 비선형 보상 메커니즘을 통합하여 강화 학습 알고리즘을 통해 다중 샘플 피드백을 활용합니다. 또한, WavReward 학습을 위한 ChatReward-30K 데이터셋을 소개하며, 이는 다양한 대화 시나리오를 포함합니다. WavReward는 기존 평가 모델을 능가하며, Qwen2.5-Omni 대비 객관적 정확도가 53.4%에서 91.5%로 향상되었습니다. 주관적 A/B 테스트에서도 83%의 우위를 보였습니다. 모든 데이터와 코드는 공개될 예정입니다.

## 🎯 주요 포인트

- 1. 최근 음성 대화 모델인 GPT-4o-audio는 많은 주목을 받고 있지만, 대화 성능 평가가 간과되고 있습니다.
- 2. WavReward는 음성 입력을 통해 대화 시스템의 IQ와 EQ를 평가할 수 있는 오디오 기반 보상 피드백 모델입니다.
- 3. WavReward는 심층 추론 과정과 비선형 보상 메커니즘을 통합하여 강화 학습 알고리즘을 통해 맞춤형 평가자를 구축합니다.
- 4. ChatReward-30K 데이터셋은 WavReward 훈련에 사용되며, 다양한 음성 대화 시나리오에서 이전 모델보다 뛰어난 성능을 보입니다.
- 5. WavReward는 기존 평가 모델보다 객관적 정확도와 주관적 A/B 테스트에서 우수한 성과를 기록했습니다.


---

*Generated on 2025-09-24 14:33:56*