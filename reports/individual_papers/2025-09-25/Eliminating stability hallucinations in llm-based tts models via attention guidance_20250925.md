---
keywords:
  - Stability Hallucinations
  - Attention Mechanism
  - Optimal Alignment Score
  - Viterbi Algorithm
  - Chain-of-Thought
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19852
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:51:27.803809",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Stability Hallucinations",
    "Attention Mechanism",
    "Optimal Alignment Score",
    "Viterbi Algorithm",
    "Chain-of-Thought"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Stability Hallucinations": 0.78,
    "Attention Mechanism": 0.85,
    "Optimal Alignment Score": 0.82,
    "Viterbi Algorithm": 0.7,
    "Chain-of-Thought": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "stability hallucinations",
        "canonical": "Stability Hallucinations",
        "aliases": [
          "repetitive speech",
          "omitted speech"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the paper's focus on improving TTS models and represents a specific challenge in the field.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "attention mechanism",
        "canonical": "Attention Mechanism",
        "aliases": [
          "attention"
        ],
        "category": "specific_connectable",
        "rationale": "Attention mechanisms are crucial for improving model performance and are widely studied in related fields.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Optimal Alignment Score",
        "canonical": "Optimal Alignment Score",
        "aliases": [
          "OAS"
        ],
        "category": "unique_technical",
        "rationale": "Introduced in this paper, OAS is a novel metric for evaluating text-speech alignment, enhancing model training.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Viterbi algorithm",
        "canonical": "Viterbi Algorithm",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The Viterbi algorithm is a well-known method used for sequence alignment, relevant to the paper's methodology.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      },
      {
        "surface": "chain-of-thought",
        "canonical": "Chain-of-Thought",
        "aliases": [
          "CoT"
        ],
        "category": "specific_connectable",
        "rationale": "Chain-of-thought is a technique to guide model training, enhancing understanding and reducing errors.",
        "novelty_score": 0.55,
        "connectivity_score": 0.68,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "alignment mechanism",
      "training"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "stability hallucinations",
      "resolved_canonical": "Stability Hallucinations",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "attention mechanism",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Optimal Alignment Score",
      "resolved_canonical": "Optimal Alignment Score",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Viterbi algorithm",
      "resolved_canonical": "Viterbi Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "chain-of-thought",
      "resolved_canonical": "Chain-of-Thought",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.68,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Eliminating stability hallucinations in llm-based tts models via attention guidance

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19852.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19852](https://arxiv.org/abs/2509.19852)

## 🔗 유사한 논문
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (82.1% similar)
- [[2025-09-23/EvoCoT_ Overcoming the Exploration Bottleneck in Reinforcement Learning_20250923|EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning]] (81.8% similar)
- [[2025-09-24/Explore the Reinforcement Learning for the LLM based ASR and TTS system_20250924|Explore the Reinforcement Learning for the LLM based ASR and TTS system]] (81.6% similar)
- [[2025-09-22/Chain of Strategy Optimization Makes Large Language Models Better Emotional Supporter_20250922|Chain of Strategy Optimization Makes Large Language Models Better Emotional Supporter]] (81.3% similar)
- [[2025-09-19/ASCoT_ An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs_20250919|ASCoT: An Adaptive Self-Correction Chain-of-Thought Method for Late-Stage Fragility in LLMs]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Viterbi Algorithm|Viterbi Algorithm]], [[keywords/Chain-of-Thought|Chain-of-Thought]]
**⚡ Unique Technical**: [[keywords/Stability Hallucinations|Stability Hallucinations]], [[keywords/Optimal Alignment Score|Optimal Alignment Score]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19852v1 Announce Type: cross 
Abstract: This paper focuses on resolving stability hallucinations (e.g., repetitive or omitted speech) in LLM-based Text-to-Speech (TTS) models by improving and leveraging the attention mechanism. First, we analyzed the alignment mechanism between text tokens and speech tokens in LLMs. We then proposed a metric termed the Optimal Alignment Score (OAS), which employs the Viterbi algorithm to evaluate text-speech alignment quality. Subsequently, OAS was integrated into the training of CosyVoice2 to assist LLMs in learning continuous, stable alignment. Additionally, the pre-trained attention value is employed to guide the training of the student CosyVoice2 via chain-of-thought (CoT), which further reduces stability hallucinations in synthesized speech. Experiments on the Seed-TTS-Eval and CV3-Eval test sets demonstrate that the proposed methods can effectively reduce the stability hallucinations of CosyVoice2 without introducing additional negative effects. The appendix is available at https://wsmzzz.github.io/llm_attn.

## 📝 요약

이 논문은 LLM 기반의 텍스트-음성 변환(TTS) 모델에서 발생하는 안정성 환각 문제(예: 반복적이거나 누락된 음성)를 해결하기 위해 주의 메커니즘을 개선하고 활용하는 방법을 제안합니다. 텍스트 토큰과 음성 토큰 간의 정렬 메커니즘을 분석하고, Viterbi 알고리즘을 활용한 최적 정렬 점수(OAS)를 제안하여 텍스트-음성 정렬 품질을 평가했습니다. OAS는 CosyVoice2의 학습에 통합되어 연속적이고 안정적인 정렬을 학습하도록 도왔습니다. 또한, 사전 학습된 주의 값은 연쇄적 사고(CoT)를 통해 학생 모델 CosyVoice2의 학습을 안내하여 합성 음성의 안정성 환각을 줄였습니다. Seed-TTS-Eval 및 CV3-Eval 테스트 세트에서의 실험 결과, 제안된 방법이 CosyVoice2의 안정성 환각을 효과적으로 줄일 수 있음을 보여주었습니다.

## 🎯 주요 포인트

- 1. LLM 기반 TTS 모델의 안정성 환각 문제를 해결하기 위해 주의 메커니즘을 개선하고 활용하는 방법을 연구했습니다.
- 2. 텍스트 토큰과 음성 토큰 간의 정렬 메커니즘을 분석하고, Viterbi 알고리즘을 활용한 최적 정렬 점수(OAS)라는 지표를 제안했습니다.
- 3. OAS를 CosyVoice2의 훈련에 통합하여 LLM이 연속적이고 안정적인 정렬을 학습하도록 도왔습니다.
- 4. 사전 훈련된 주의 값을 활용하여 chain-of-thought(CoT)을 통해 학생 CosyVoice2의 훈련을 안내함으로써 합성 음성의 안정성 환각을 줄였습니다.
- 5. Seed-TTS-Eval 및 CV3-Eval 테스트 세트에서 제안된 방법이 CosyVoice2의 안정성 환각을 효과적으로 줄일 수 있음을 실험적으로 입증했습니다.


---

*Generated on 2025-09-25 15:51:27*