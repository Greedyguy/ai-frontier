---
keywords:
  - Large Language Model
  - Fine-grained Persona Prompting
  - Lexical Diversity
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2505.17390
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:46:28.805374",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Fine-grained Persona Prompting",
    "Lexical Diversity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Fine-grained Persona Prompting": 0.7,
    "Lexical Diversity": 0.82
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
        "rationale": "Large Language Models are central to the study and connect well with other NLP concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Fine-grained Persona Prompting",
        "canonical": "Fine-grained Persona Prompting",
        "aliases": [
          "Persona-driven Prompting"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique method discussed in the paper, relevant for linking to specific NLP techniques.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Lexical Diversity",
        "canonical": "Lexical Diversity",
        "aliases": [
          "Text Diversity"
        ],
        "category": "specific_connectable",
        "rationale": "Lexical diversity is a key metric in evaluating NLP models, connecting to broader linguistic analysis.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "synthetic data",
      "diversity metrics"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Fine-grained Persona Prompting",
      "resolved_canonical": "Fine-grained Persona Prompting",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Lexical Diversity",
      "resolved_canonical": "Lexical Diversity",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Measuring Lexical Diversity of Synthetic Data Generated through Fine-Grained Persona Prompting

**Korean Title:** 합성 데이터의 어휘 다양성 측정: 세분화된 페르소나 프롬프트를 통한 생성

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.17390.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2505.17390](https://arxiv.org/abs/2505.17390)

## 🔗 유사한 논문
- [[2025-09-22/PILOT_ Steering Synthetic Data Generation with Psychological & Linguistic Output Targeting_20250922|PILOT: Steering Synthetic Data Generation with Psychological & Linguistic Output Targeting]] (84.0% similar)
- [[2025-09-22/P2VA_ Converting Persona Descriptions into Voice Attributes for Fair and Controllable Text-to-Speech_20250922|P2VA: Converting Persona Descriptions into Voice Attributes for Fair and Controllable Text-to-Speech]] (83.6% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (83.1% similar)
- [[2025-09-17/Synthetic Data Generation for Screen Time and App Usage_20250917|Synthetic Data Generation for Screen Time and App Usage]] (81.4% similar)
- [[2025-09-22/The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation_20250922|The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Lexical Diversity|Lexical Diversity]]
**⚡ Unique Technical**: [[keywords/Fine-grained Persona Prompting|Fine-grained Persona Prompting]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.17390v2 Announce Type: replace 
Abstract: Fine-grained personas have recently been used for generating 'diverse' synthetic data for pre-training and supervised fine-tuning of Large Language Models (LLMs). In this work, we measure the diversity of persona-driven synthetically generated prompts and responses with a suite of lexical diversity and redundancy metrics. First, we find that synthetic prompts/instructions are significantly less diverse than human-written ones. Next, we sample responses from LLMs of different sizes with fine-grained and coarse persona descriptions to investigate how much fine-grained detail in persona descriptions contribute to generated text diversity. Our results indicate that persona prompting produces higher lexical diversity than prompting without personas, particularly in larger models. In contrast, adding fine-grained persona details yields minimal gains in diversity compared to simply specifying a length cutoff in the prompt.

## 🔍 Abstract (한글 번역)

arXiv:2505.17390v2 발표 유형: 교체  
초록: 세밀한 페르소나는 최근 대형 언어 모델(LLMs)의 사전 훈련 및 지도 학습 미세 조정을 위한 '다양한' 합성 데이터를 생성하는 데 사용되고 있습니다. 본 연구에서는 어휘 다양성과 중복성 지표를 통해 페르소나 기반으로 합성된 프롬프트와 응답의 다양성을 측정합니다. 먼저, 합성된 프롬프트/지시문이 인간이 작성한 것보다 다양성이 현저히 낮다는 것을 발견했습니다. 다음으로, 세밀한 페르소나 설명과 대략적인 페르소나 설명을 사용하여 다양한 크기의 LLM에서 응답을 샘플링하여, 페르소나 설명의 세밀한 디테일이 생성된 텍스트의 다양성에 얼마나 기여하는지를 조사합니다. 우리의 결과는 페르소나 프롬프트가 페르소나 없이 프롬프트를 사용하는 것보다 더 높은 어휘 다양성을 생성하며, 특히 더 큰 모델에서 그러함을 나타냅니다. 반면, 세밀한 페르소나 디테일을 추가하는 것은 프롬프트에서 단순히 길이 제한을 지정하는 것에 비해 다양성에서 최소한의 이득만을 제공합니다.

## 📝 요약

이 연구는 대규모 언어 모델(LLM)의 사전 학습 및 지도 학습을 위한 '다양한' 합성 데이터를 생성하는 데 사용되는 세밀한 페르소나의 다양성을 측정합니다. 연구 결과, 합성된 프롬프트와 응답은 인간이 작성한 것보다 다양성이 낮으며, 페르소나 기반 프롬프트는 페르소나 없이 생성된 것보다 더 높은 어휘 다양성을 나타냅니다. 특히, 큰 모델에서는 이러한 경향이 두드러지지만, 세밀한 페르소나 세부사항을 추가하는 것은 단순히 프롬프트 길이 제한을 설정하는 것에 비해 다양성 증가에 미미한 영향을 미칩니다.

## 🎯 주요 포인트

- 1. 페르소나 기반의 합성 데이터는 대규모 언어 모델의 사전 학습 및 감독 학습에 사용되며, 이 연구에서는 이러한 합성 데이터의 다양성을 측정하였다.
- 2. 합성된 프롬프트와 지시문은 인간이 작성한 것보다 다양성이 현저히 낮다는 결과를 발견하였다.
- 3. 페르소나 프롬프트는 페르소나 없이 프롬프트를 생성하는 것보다 더 높은 어휘적 다양성을 제공하며, 특히 더 큰 모델에서 그 효과가 두드러진다.
- 4. 세밀한 페르소나 세부사항을 추가하는 것은 프롬프트에 단순히 길이 제한을 지정하는 것보다 다양성 증가에 미미한 영향을 미친다.


---

*Generated on 2025-09-23 11:46:28*