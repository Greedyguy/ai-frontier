<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:02:21.993500",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Attention Mechanism",
    "Feed-Forward Network",
    "Supervised Fine-tuning",
    "Contextual Knowledge"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Attention Mechanism": 0.78,
    "Feed-Forward Network": 0.72,
    "Supervised Fine-tuning": 0.8,
    "Contextual Knowledge": 0.77
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
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's discussion on context length and fine-tuning.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multi-Head Attention",
        "canonical": "Attention Mechanism",
        "aliases": [
          "MHA",
          "Multi-Head Attention"
        ],
        "category": "specific_connectable",
        "rationale": "Key component analyzed for its role in context length effects.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Feed-Forward Network",
        "canonical": "Feed-Forward Network",
        "aliases": [
          "FFN"
        ],
        "category": "unique_technical",
        "rationale": "Analyzed independently for its contribution to model behavior.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "Supervised Fine-tuning",
        "canonical": "Supervised Fine-tuning",
        "aliases": [
          "SFT"
        ],
        "category": "unique_technical",
        "rationale": "Central to the study of context length effects on model performance.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Contextual Knowledge",
        "canonical": "Contextual Knowledge",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Describes a key finding related to knowledge preference bias in the study.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "short-context tasks",
      "real-world applications",
      "knowledge preference bias"
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
      "candidate_surface": "Multi-Head Attention",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Feed-Forward Network",
      "resolved_canonical": "Feed-Forward Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Supervised Fine-tuning",
      "resolved_canonical": "Supervised Fine-tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Contextual Knowledge",
      "resolved_canonical": "Contextual Knowledge",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# When Long Helps Short: How Context Length in Supervised Fine-tuning Affects Behavior of Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18762.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18762](https://arxiv.org/abs/2509.18762)

## 🔗 유사한 논문
- [[2025-09-23/Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels_20250923|Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels]] (86.7% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (86.3% similar)
- [[2025-09-22/LiteLong_ Resource-Efficient Long-Context Data Synthesis for LLMs_20250922|LiteLong: Resource-Efficient Long-Context Data Synthesis for LLMs]] (86.0% similar)
- [[2025-09-23/Language Modeling with Learned Meta-Tokens_20250923|Language Modeling with Learned Meta-Tokens]] (85.5% similar)
- [[2025-09-23/Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning_20250923|Can LLMs Reason Over Non-Text Modalities in a Training-Free Manner? A Case Study with In-Context Representation Learning]] (85.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/Feed-Forward Network|Feed-Forward Network]], [[keywords/Supervised Fine-tuning|Supervised Fine-tuning]], [[keywords/Contextual Knowledge|Contextual Knowledge]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18762v1 Announce Type: cross 
Abstract: Large language models (LLMs) have achieved impressive performance across natural language processing (NLP) tasks. As real-world applications increasingly demand longer context windows, continued pretraining and supervised fine-tuning (SFT) on long-context data has become a common approach. While the effects of data length in continued pretraining have been extensively studied, their implications for SFT remain unclear. In this work, we systematically investigate how SFT data length influences LLM behavior on short-context tasks. Counterintuitively, we find that long-context SFT improves short-context performance, contrary to the commonly observed degradation from long-context pretraining. To uncover the underlying mechanisms of this phenomenon, we first decouple and analyze two key components, Multi-Head Attention (MHA) and Feed-Forward Network (FFN), and show that both independently benefit from long-context SFT. We further study their interaction and reveal a knowledge preference bias: long-context SFT promotes contextual knowledge, while short-context SFT favors parametric knowledge, making exclusive reliance on long-context SFT suboptimal. Finally, we demonstrate that hybrid training mitigates this bias, offering explainable guidance for fine-tuning LLMs.

## 📝 요약

대형 언어 모델(LLM)은 자연어 처리 작업에서 뛰어난 성능을 보이고 있습니다. 실제 응용에서는 긴 문맥 창을 요구하는 경우가 많아, 긴 문맥 데이터를 사용한 지속적 사전 학습과 지도 미세 조정(SFT)이 일반적인 접근 방식이 되었습니다. 본 연구에서는 SFT 데이터 길이가 LLM의 짧은 문맥 작업에 미치는 영향을 체계적으로 조사했습니다. 놀랍게도, 긴 문맥 SFT가 짧은 문맥 성능을 향상시킨다는 결과를 발견했습니다. 이 현상의 메커니즘을 밝히기 위해, 다중 헤드 주의(MHA)와 피드포워드 네트워크(FFN)를 분리하여 분석한 결과, 두 요소 모두 긴 문맥 SFT에서 이점을 얻는 것으로 나타났습니다. 또한, 긴 문맥 SFT는 문맥적 지식을 촉진하고, 짧은 문맥 SFT는 매개변수적 지식을 선호하는 경향이 있음을 밝혔습니다. 마지막으로, 하이브리드 훈련이 이러한 편향을 완화할 수 있음을 보여주었습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 자연어 처리(NLP) 작업에서 뛰어난 성능을 보여주고 있습니다.
- 2. 실제 응용에서는 긴 문맥 창을 요구하며, 이를 위해 긴 문맥 데이터를 사용한 지속적 사전 훈련과 지도 학습 미세 조정(SFT)이 일반적인 접근 방식이 되고 있습니다.
- 3. 연구 결과, 긴 문맥 SFT가 짧은 문맥 작업의 성능을 향상시키는 것으로 나타났으며, 이는 일반적으로 긴 문맥 사전 훈련에서 관찰되는 성능 저하와는 반대되는 결과입니다.
- 4. Multi-Head Attention(MHA)와 Feed-Forward Network(FFN) 모두 긴 문맥 SFT로부터 독립적으로 이점을 얻는 것으로 분석되었습니다.
- 5. 하이브리드 훈련이 지식 선호 편향을 완화하여 LLM의 미세 조정에 대한 설명 가능한 지침을 제공합니다.


---

*Generated on 2025-09-24 14:02:21*