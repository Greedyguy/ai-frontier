<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:49:54.555549",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Typologically Unattested Languages",
    "Greenberg's Universal 20",
    "Word Order Manipulation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Typologically Unattested Languages": 0.7,
    "Greenberg's Universal 20": 0.65,
    "Word Order Manipulation": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LMs"
        ],
        "category": "broad_technical",
        "rationale": "Central to the study, linking to a broad technical category enhances connectivity across language-related research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "typologically unattested languages",
        "canonical": "Typologically Unattested Languages",
        "aliases": [
          "impossible languages"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a unique concept that challenges existing language models, fostering discussions on linguistic diversity.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Greenberg's Universal 20",
        "canonical": "Greenberg's Universal 20",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific linguistic theory that provides a basis for testing language models, linking to linguistic theory discussions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.65
      },
      {
        "surface": "word order manipulation",
        "canonical": "Word Order Manipulation",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Highlights a specific experimental technique relevant to language processing studies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "language learning",
      "experiments",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "language models",
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
      "candidate_surface": "typologically unattested languages",
      "resolved_canonical": "Typologically Unattested Languages",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Greenberg's Universal 20",
      "resolved_canonical": "Greenberg's Universal 20",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.65
      }
    },
    {
      "candidate_surface": "word order manipulation",
      "resolved_canonical": "Word Order Manipulation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Anything Goes? A Crosslinguistic Study of (Im)possible Language Learning in LMs

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2502.18795.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2502.18795](https://arxiv.org/abs/2502.18795)

## 🔗 유사한 논문
- [[2025-09-19/Large Language Model probabilities cannot distinguish between possible and impossible language_20250919|Large Language Model probabilities cannot distinguish between possible and impossible language]] (87.7% similar)
- [[2025-09-22/How do Language Models Generate Slang_ A Systematic Comparison between Human and Machine-Generated Slang Usages_20250922|How do Language Models Generate Slang: A Systematic Comparison between Human and Machine-Generated Slang Usages]] (87.6% similar)
- [[2025-09-23/Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements_20250923|Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements]] (87.2% similar)
- [[2025-09-23/Learning to vary_ Teaching LMs to reproduce human linguistic variability in next-word prediction_20250923|Learning to vary: Teaching LMs to reproduce human linguistic variability in next-word prediction]] (86.8% similar)
- [[2025-09-23/Can Language Models Follow Multiple Turns of Entangled Instructions?_20250923|Can Language Models Follow Multiple Turns of Entangled Instructions?]] (85.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Word Order Manipulation|Word Order Manipulation]]
**⚡ Unique Technical**: [[keywords/Typologically Unattested Languages|Typologically Unattested Languages]], [[keywords/Greenberg's Universal 20|Greenberg's Universal 20]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.18795v3 Announce Type: replace 
Abstract: Do language models (LMs) offer insights into human language learning? A common argument against this idea is that because their architecture and training paradigm are so vastly different from humans, LMs can learn arbitrary inputs as easily as natural languages. We test this claim by training LMs to model impossible and typologically unattested languages. Unlike previous work, which has focused exclusively on English, we conduct experiments on 12 languages from 4 language families with two newly constructed parallel corpora. Our results show that while GPT-2 small can largely distinguish attested languages from their impossible counterparts, it does not achieve perfect separation between all the attested languages and all the impossible ones. We further test whether GPT-2 small distinguishes typologically attested from unattested languages with different NP orders by manipulating word order based on Greenberg's Universal 20. We find that the model's perplexity scores do not distinguish attested vs. unattested word orders, while its performance on the generalization test does. These findings suggest that LMs exhibit some human-like inductive biases, though these biases are weaker than those found in human learners.

## 📝 요약

이 논문은 언어 모델(LM)이 인간의 언어 학습에 대한 통찰을 제공할 수 있는지를 탐구합니다. 특히, LM이 불가능하거나 유형학적으로 존재하지 않는 언어를 학습할 수 있는지를 실험했습니다. 12개의 언어와 두 개의 새로운 병렬 코퍼스를 사용하여 실험한 결과, GPT-2 small은 대부분의 경우 존재하는 언어와 불가능한 언어를 구분할 수 있었지만, 완벽한 구분은 이루지 못했습니다. 또한, Greenberg의 보편적 20을 기반으로 명사구(NP) 순서를 조작하여 실험한 결과, 모델의 혼란도(perplexity) 점수는 존재하는 순서와 존재하지 않는 순서를 구분하지 못했지만, 일반화 테스트에서는 구분했습니다. 이는 LM이 인간과 유사한 귀납적 편향을 가지고 있지만, 그 강도는 인간 학습자보다 약하다는 것을 시사합니다.

## 🎯 주요 포인트

- 1. 언어 모델(LM)은 인간 언어 학습에 대한 통찰을 제공할 수 있는지에 대한 논란이 있다.
- 2. 연구는 불가능하거나 유형학적으로 관찰되지 않은 언어를 모델링하는 LMs의 능력을 테스트했다.
- 3. GPT-2 small은 가능 언어와 불가능 언어를 어느 정도 구별할 수 있지만, 완벽한 분리는 이루지 못했다.
- 4. Greenberg의 Universal 20을 기반으로 단어 순서를 조작하여 유형학적으로 관찰된 언어와 관찰되지 않은 언어를 구별할 수 있는지 추가 실험을 진행했다.
- 5. 연구 결과, LMs는 인간 학습자보다 약하지만 인간과 유사한 귀납적 편향을 일부 보인다.


---

*Generated on 2025-09-24 15:49:54*