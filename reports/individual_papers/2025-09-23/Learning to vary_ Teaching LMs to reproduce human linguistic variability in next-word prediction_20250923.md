---
keywords:
  - Large Language Model
  - Linguistic Variability
  - Next-Word Prediction
  - Fine-Tuning
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17794
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:32:37.440893",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Linguistic Variability",
    "Next-Word Prediction",
    "Fine-Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Linguistic Variability": 0.78,
    "Next-Word Prediction": 0.77,
    "Fine-Tuning": 0.79
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
        "rationale": "Language models are central to the study and are a key component in NLP tasks, making them highly connectable.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "linguistic variability",
        "canonical": "Linguistic Variability",
        "aliases": [
          "language variability",
          "variability in language"
        ],
        "category": "unique_technical",
        "rationale": "The concept of linguistic variability is unique to this study and crucial for understanding the research focus.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "next-word prediction",
        "canonical": "Next-Word Prediction",
        "aliases": [
          "word prediction",
          "predicting next word"
        ],
        "category": "specific_connectable",
        "rationale": "Next-word prediction is a specific task that connects to broader NLP applications and model evaluations.",
        "novelty_score": 0.5,
        "connectivity_score": 0.7,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "fine-tuning techniques",
        "canonical": "Fine-Tuning",
        "aliases": [
          "model fine-tuning",
          "fine-tuning methods"
        ],
        "category": "specific_connectable",
        "rationale": "Fine-tuning is a widely applicable technique in machine learning, enhancing model performance and adaptability.",
        "novelty_score": 0.4,
        "connectivity_score": 0.82,
        "specificity_score": 0.68,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "context",
      "task",
      "evaluation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "language models",
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
      "candidate_surface": "linguistic variability",
      "resolved_canonical": "Linguistic Variability",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "next-word prediction",
      "resolved_canonical": "Next-Word Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.7,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "fine-tuning techniques",
      "resolved_canonical": "Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.82,
        "specificity": 0.68,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Learning to vary: Teaching LMs to reproduce human linguistic variability in next-word prediction

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17794.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17794](https://arxiv.org/abs/2509.17794)

## 🔗 유사한 논문
- [[2025-09-22/The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation_20250922|The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation]] (86.0% similar)
- [[2025-09-23/CIE_ Controlling Language Model Text Generations Using Continuous Signals_20250923|CIE: Controlling Language Model Text Generations Using Continuous Signals]] (85.8% similar)
- [[2025-09-23/Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements_20250923|Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements]] (85.3% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (85.3% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (85.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Next-Word Prediction|Next-Word Prediction]], [[keywords/Fine-Tuning|Fine-Tuning]]
**⚡ Unique Technical**: [[keywords/Linguistic Variability|Linguistic Variability]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17794v1 Announce Type: new 
Abstract: Natural language generation (NLG) tasks are often subject to inherent variability; \emph{e.g.} predicting the next word given a context has multiple valid responses, evident when asking multiple humans to complete the task. While having language models (LMs) that are aligned pluralistically, so that they are able to reproduce well the inherent diversity in perspectives of an entire population of interest is clearly beneficial, \citet{ilia2024predict} show that LMs do not reproduce this type of linguistic variability well. They speculate this inability might stem from the lack of consistent training of LMs with data reflecting this type of inherent variability. As such, we investigate whether training LMs on multiple plausible word continuations per context can improve their ability to reproduce human linguistic variability for next-word prediction. We employ fine-tuning techniques for pre-trained and instruction-tuned models; and demonstrate their potential when fine-tuning GPT-2 and Mistral-7B-IT, using Provo Corpus. Our evaluation, which measures divergence among empirically estimated human and model next-word distributions across contexts before and after fine-tuning, shows that our multi-label fine-tuning improves the LMs' ability to reproduce linguistic variability; both for contexts that admit higher and lower variability.

## 📝 요약

이 논문은 자연어 생성(NLG) 작업에서 언어 모델(LM)이 인간의 언어적 다양성을 잘 재현하지 못하는 문제를 다룹니다. 연구진은 다양한 문맥에서 여러 가능한 단어 연속을 학습시키는 것이 이러한 문제를 개선할 수 있는지를 조사했습니다. 이를 위해 사전 학습된 GPT-2와 Mistral-7B-IT 모델을 Provo Corpus를 사용해 미세 조정하였습니다. 평가 결과, 다중 레이블 미세 조정 기법이 모델의 언어적 다양성 재현 능력을 향상시킴을 확인했습니다. 이 연구는 LMs가 다양한 인간의 관점을 더 잘 반영할 수 있도록 하는 방법론적 기여를 제공합니다.

## 🎯 주요 포인트

- 1. 자연어 생성(NLG) 작업은 본질적으로 다양한 변동성을 가지며, 이는 여러 사람이 동일한 작업을 수행할 때 다양한 유효한 응답이 존재하는 것으로 나타난다.
- 2. 언어 모델(LM)이 다양한 관점을 잘 재현할 수 있도록 다원적으로 정렬되면 유익하지만, 기존 연구에 따르면 LMs는 이러한 언어적 변동성을 잘 재현하지 못한다.
- 3. LMs의 언어적 변동성 재현 능력을 개선하기 위해, 여러 가능한 단어 연속체로 훈련하는 것이 효과적일 수 있음을 조사하였다.
- 4. 사전 훈련된 모델과 지시 조정된 모델에 대한 미세 조정 기법을 사용하여, Provo Corpus를 활용한 GPT-2 및 Mistral-7B-IT의 미세 조정 가능성을 입증하였다.
- 5. 평가 결과, 멀티 레이블 미세 조정이 LMs의 언어적 변동성 재현 능력을 개선하며, 이는 변동성이 높은 문맥과 낮은 문맥 모두에서 효과적임을 보여준다.


---

*Generated on 2025-09-24 03:32:37*