---
keywords:
  - Large Language Model
  - Dialect Variation Dictionary
  - DiaLemma
  - Orthographic Dialect Variation
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17855
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:34:02.621244",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Dialect Variation Dictionary",
    "DiaLemma",
    "Orthographic Dialect Variation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Dialect Variation Dictionary": 0.7,
    "DiaLemma": 0.75,
    "Orthographic Dialect Variation": 0.65
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
        "rationale": "Central to the study, linking to broader discussions on language model capabilities.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Dialect Variation Dictionaries",
        "canonical": "Dialect Variation Dictionary",
        "aliases": [
          "Dialect Dictionaries"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept specific to the study of dialects.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "DiaLemma",
        "canonical": "DiaLemma",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A new framework introduced in the paper, essential for understanding the methodology.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.75
      },
      {
        "surface": "Orthographic Dialect Variation",
        "canonical": "Orthographic Dialect Variation",
        "aliases": [
          "Dialect Orthography"
        ],
        "category": "unique_technical",
        "rationale": "Key challenge addressed by the paper, relevant for dialect processing.",
        "novelty_score": 0.7,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
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
      "candidate_surface": "Dialect Variation Dictionaries",
      "resolved_canonical": "Dialect Variation Dictionary",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "DiaLemma",
      "resolved_canonical": "DiaLemma",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Orthographic Dialect Variation",
      "resolved_canonical": "Orthographic Dialect Variation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Make Every Letter Count: Building Dialect Variation Dictionaries from Monolingual Corpora

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17855.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17855](https://arxiv.org/abs/2509.17855)

## 🔗 유사한 논문
- [[2025-09-22/Benchmark of stylistic variation in LLM-generated texts_20250922|Benchmark of stylistic variation in LLM-generated texts]] (85.0% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (84.1% similar)
- [[2025-09-22/PolBiX_ Detecting LLMs' Political Bias in Fact-Checking through X-phemisms_20250922|PolBiX: Detecting LLMs' Political Bias in Fact-Checking through X-phemisms]] (83.3% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (83.2% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Dialect Variation Dictionary|Dialect Variation Dictionary]], [[keywords/DiaLemma|DiaLemma]], [[keywords/Orthographic Dialect Variation|Orthographic Dialect Variation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17855v1 Announce Type: new 
Abstract: Dialects exhibit a substantial degree of variation due to the lack of a standard orthography. At the same time, the ability of Large Language Models (LLMs) to process dialects remains largely understudied. To address this gap, we use Bavarian as a case study and investigate the lexical dialect understanding capability of LLMs by examining how well they recognize and translate dialectal terms across different parts-of-speech. To this end, we introduce DiaLemma, a novel annotation framework for creating dialect variation dictionaries from monolingual data only, and use it to compile a ground truth dataset consisting of 100K human-annotated German-Bavarian word pairs. We evaluate how well nine state-of-the-art LLMs can judge Bavarian terms as dialect translations, inflected variants, or unrelated forms of a given German lemma. Our results show that LLMs perform best on nouns and lexically similar word pairs, and struggle most in distinguishing between direct translations and inflected variants. Interestingly, providing additional context in the form of example usages improves the translation performance, but reduces their ability to recognize dialect variants. This study highlights the limitations of LLMs in dealing with orthographic dialect variation and emphasizes the need for future work on adapting LLMs to dialects.

## 📝 요약

이 논문은 방언의 표기법 부재로 인한 변이를 다루며, 대형 언어 모델(LLM)의 방언 처리 능력을 연구합니다. 바이에른 방언을 사례로 하여, LLM이 방언 용어를 인식하고 번역하는 능력을 조사합니다. 이를 위해, 단일 언어 데이터만으로 방언 변이 사전을 만드는 새로운 주석 프레임워크인 DiaLemma를 소개하고, 10만 개의 독일어-바이에른어 단어 쌍으로 구성된 데이터셋을 구축했습니다. 9개의 최신 LLM을 평가한 결과, 명사와 어휘적으로 유사한 단어 쌍에서 성능이 가장 좋았으나, 직접 번역과 굴절형 변형을 구분하는 데 어려움을 겪었습니다. 추가적인 문맥 제공이 번역 성능을 향상시키지만, 방언 변이 인식 능력은 감소시켰습니다. 이 연구는 LLM이 방언의 표기 변이에 대응하는 데 한계가 있음을 강조하며, 방언에 적응할 수 있는 LLM 개발의 필요성을 제시합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 방언 처리 능력이 충분히 연구되지 않았다.
- 2. 연구는 바이에른어를 사례로 사용하여 LLM의 방언 이해 능력을 조사하였다.
- 3. DiaLemma라는 새로운 주석 프레임워크를 도입하여 독일어-바이에른어 단어 쌍 10만 개의 데이터셋을 구축하였다.
- 4. LLM은 명사와 어휘적으로 유사한 단어 쌍에서 가장 좋은 성능을 보였으나, 직접 번역과 굴절 변형을 구분하는 데 어려움을 겪었다.
- 5. 추가적인 문맥 제공은 번역 성능을 향상시키지만 방언 변형 인식 능력을 감소시켰다.


---

*Generated on 2025-09-24 03:34:02*