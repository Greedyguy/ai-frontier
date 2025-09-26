---
keywords:
  - Large Language Model
  - Highlighted Chain-of-Thought Prompting
  - Few-Shot Learning
  - Chain of Thought Prompting
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2503.02003
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:52:17.892660",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Highlighted Chain-of-Thought Prompting",
    "Few-Shot Learning",
    "Chain of Thought Prompting"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Highlighted Chain-of-Thought Prompting": 0.8,
    "Few-Shot Learning": 0.78,
    "Chain of Thought Prompting": 0.75
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
        "rationale": "Central to the paper's discussion, providing a basis for linking with other works on language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Highlighted Chain-of-Thought Prompting",
        "canonical": "Highlighted Chain-of-Thought Prompting",
        "aliases": [
          "HoT"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel technique specific to this paper, crucial for understanding its unique contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Few-Shot Settings",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the broader topic of learning paradigms, relevant for linking with other few-shot learning research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Chain of Thought Prompting",
        "canonical": "Chain of Thought Prompting",
        "aliases": [
          "CoT"
        ],
        "category": "unique_technical",
        "rationale": "A specific prompting technique that is central to the paper's methodology, useful for linking to related prompting strategies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "arithmetic",
      "reading comprehension",
      "logical reasoning"
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
      "candidate_surface": "Highlighted Chain-of-Thought Prompting",
      "resolved_canonical": "Highlighted Chain-of-Thought Prompting",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Few-Shot Settings",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Chain of Thought Prompting",
      "resolved_canonical": "Chain of Thought Prompting",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# HoT: Highlighted Chain of Thought for Referencing Supporting Facts from Inputs

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2503.02003.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2503.02003](https://arxiv.org/abs/2503.02003)

## 🔗 유사한 논문
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (85.6% similar)
- [[2025-09-23/No Need for Explanations_ LLMs can implicitly learn from mistakes in-context_20250923|No Need for Explanations: LLMs can implicitly learn from mistakes in-context]] (85.4% similar)
- [[2025-09-24/Please Translate Again_ Two Simple Experiments on Whether Human-Like Reasoning Helps Translation_20250924|Please Translate Again: Two Simple Experiments on Whether Human-Like Reasoning Helps Translation]] (84.7% similar)
- [[2025-09-25/Understanding Before Reasoning_ Enhancing Chain-of-Thought with Iterative Summarization Pre-Prompting_20250925|Understanding Before Reasoning: Enhancing Chain-of-Thought with Iterative Summarization Pre-Prompting]] (84.6% similar)
- [[2025-09-24/Pathways of Thoughts_ Multi-Directional Thinking for Long-form Personalized Question Answering_20250924|Pathways of Thoughts: Multi-Directional Thinking for Long-form Personalized Question Answering]] (84.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Highlighted Chain-of-Thought Prompting|Highlighted Chain-of-Thought Prompting]], [[keywords/Chain of Thought Prompting|Chain of Thought Prompting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.02003v4 Announce Type: replace 
Abstract: An Achilles heel of Large Language Models (LLMs) is their tendency to hallucinate non-factual statements. A response mixed of factual and non-factual statements poses a challenge for humans to verify and accurately base their decisions on. To combat this problem, we propose Highlighted Chain-of-Thought Prompting (HoT), a technique for prompting LLMs to generate responses with XML tags that ground facts to those provided in the query. That is, given an input question, LLMs would first re-format the question to add XML tags highlighting key facts, and then, generate a response with highlights over the facts referenced from the input. Interestingly, in few-shot settings, HoT outperforms vanilla chain of thought prompting (CoT) on a wide range of 17 tasks from arithmetic, reading comprehension to logical reasoning. When asking humans to verify LLM responses, highlights help time-limited participants to more accurately and efficiently recognize when LLMs are correct. Yet, surprisingly, when LLMs are wrong, HoTs tend to make users believe that an answer is correct.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 비사실적 진술 생성 문제를 해결하기 위해 '강조된 사고 사슬 프롬프트(HoT)' 기법을 제안합니다. 이 방법은 입력 질문에 XML 태그를 사용하여 사실을 강조하고, 이를 기반으로 한 응답을 생성하도록 합니다. HoT는 소수의 예시만으로도 산술, 독해, 논리적 추론 등 17가지 과제에서 기존의 사고 사슬 프롬프트(CoT)보다 우수한 성능을 보였습니다. 인간이 LLM의 응답을 검증할 때, 강조 표시가 시간 제한이 있는 참가자들이 LLM의 정확성을 더 효율적으로 인식하도록 돕지만, LLM이 틀린 경우에도 정답으로 믿게 만드는 경향이 있습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)의 약점은 비사실적 진술을 생성하는 경향이 있다는 점이다.
- 2. Highlighted Chain-of-Thought Prompting(HoT)는 XML 태그를 사용하여 사실을 강조함으로써 LLM의 응답을 개선하는 기법이다.
- 3. HoT는 소수 샷 설정에서 17개의 다양한 과제에서 기존의 체인 오브 쏘트 프롬프팅(CoT)보다 더 나은 성능을 보였다.
- 4. 인간이 LLM의 응답을 검증할 때, 강조 표시가 제한된 시간 내에 더 정확하고 효율적으로 인식하는 데 도움을 준다.
- 5. 그러나 LLM이 틀렸을 때, HoT는 사용자가 답변이 맞다고 믿게 만드는 경향이 있다.


---

*Generated on 2025-09-26 08:52:17*