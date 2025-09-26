<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:51:18.768433",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Idiom Processing",
    "Multilingual Learning",
    "Contextual Cues"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Idiom Processing": 0.7,
    "Multilingual Learning": 0.75,
    "Contextual Cues": 0.65
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
        "rationale": "Large Language Models are central to the study and connect with various NLP tasks.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.8
      },
      {
        "surface": "Idiom Processing",
        "canonical": "Idiom Processing",
        "aliases": [
          "Idiom Understanding"
        ],
        "category": "unique_technical",
        "rationale": "Idiom Processing is a unique challenge in NLP, linking to semantic understanding.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Multilingual Settings",
        "canonical": "Multilingual Learning",
        "aliases": [
          "Multilingual Contexts"
        ],
        "category": "specific_connectable",
        "rationale": "Multilingual Learning is crucial for understanding idioms across languages.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "Contextual Cues",
        "canonical": "Contextual Cues",
        "aliases": [
          "Contextual Information"
        ],
        "category": "unique_technical",
        "rationale": "Contextual Cues are vital for reasoning and understanding idioms in LLMs.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.7,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "memorization",
      "reasoning",
      "dataset"
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
        "specificity": 0.5,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Idiom Processing",
      "resolved_canonical": "Idiom Processing",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Multilingual Settings",
      "resolved_canonical": "Multilingual Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Contextual Cues",
      "resolved_canonical": "Contextual Cues",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.7,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Memorization or Reasoning? Exploring the Idiom Understanding of LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.16216.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2505.16216](https://arxiv.org/abs/2505.16216)

## 🔗 유사한 논문
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (86.3% similar)
- [[2025-09-22/How do Language Models Generate Slang_ A Systematic Comparison between Human and Machine-Generated Slang Usages_20250922|How do Language Models Generate Slang: A Systematic Comparison between Human and Machine-Generated Slang Usages]] (85.5% similar)
- [[2025-09-17/Do Large Language Models Understand Word Senses?_20250917|Do Large Language Models Understand Word Senses?]] (85.2% similar)
- [[2025-09-23/Question Answering with LLMs and Learning from Answer Sets_20250923|Question Answering with LLMs and Learning from Answer Sets]] (84.6% similar)
- [[2025-09-23/MAKIEval_ A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs_20250923|MAKIEval: A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multilingual Learning|Multilingual Learning]]
**⚡ Unique Technical**: [[keywords/Idiom Processing|Idiom Processing]], [[keywords/Contextual Cues|Contextual Cues]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.16216v2 Announce Type: replace 
Abstract: Idioms have long posed a challenge due to their unique linguistic properties, which set them apart from other common expressions. While recent studies have leveraged large language models (LLMs) to handle idioms across various tasks, e.g., idiom-containing sentence generation and idiomatic machine translation, little is known about the underlying mechanisms of idiom processing in LLMs, particularly in multilingual settings. To this end, we introduce MIDAS, a new large-scale dataset of idioms in six languages, each paired with its corresponding meaning. Leveraging this resource, we conduct a comprehensive evaluation of LLMs' idiom processing ability, identifying key factors that influence their performance. Our findings suggest that LLMs rely not only on memorization, but also adopt a hybrid approach that integrates contextual cues and reasoning, especially when processing compositional idioms. This implies that idiom understanding in LLMs emerges from an interplay between internal knowledge retrieval and reasoning-based inference.

## 📝 요약

이 논문은 관용어구의 독특한 언어적 특성으로 인해 발생하는 도전 과제를 다룹니다. 연구에서는 대형 언어 모델(LLM)을 활용하여 다양한 작업에서 관용어구를 처리하는 방법을 조사하였으며, 특히 다국어 환경에서의 처리 메커니즘에 주목했습니다. 이를 위해 6개 언어의 관용어구와 그 의미를 포함한 대규모 데이터셋인 MIDAS를 소개하고, 이를 통해 LLM의 관용어구 처리 능력을 평가했습니다. 연구 결과, LLM은 단순 암기에 의존하지 않고, 문맥적 단서와 추론을 통합하는 혼합 접근 방식을 사용하여 관용어구를 처리한다는 것을 발견했습니다. 이는 LLM의 관용어구 이해가 내부 지식 검색과 추론 기반 추론의 상호작용에서 비롯된다는 것을 시사합니다.

## 🎯 주요 포인트

- 1. 관용구는 고유한 언어적 특성 때문에 다른 일반적인 표현과 구별되며, 이를 처리하는 데 있어 큰 언어 모델(LLM)이 최근 연구에서 활용되고 있다.
- 2. 다국어 환경에서 LLM의 관용구 처리 메커니즘은 잘 알려져 있지 않으며, 이를 위해 여섯 개 언어의 관용구와 그 의미를 포함한 대규모 데이터셋 MIDAS가 소개되었다.
- 3. 연구 결과, LLM은 관용구 처리 시 단순한 암기뿐만 아니라 맥락적 단서와 추론을 통합하는 혼합 접근 방식을 채택한다는 것을 발견했다.
- 4. 특히 구성적 관용구를 처리할 때 LLM의 관용구 이해는 내부 지식 검색과 추론 기반 추론의 상호작용에서 비롯된다는 것을 시사한다.


---

*Generated on 2025-09-24 15:51:18*