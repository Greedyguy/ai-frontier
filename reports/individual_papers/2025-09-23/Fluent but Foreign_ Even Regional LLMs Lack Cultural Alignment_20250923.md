---
keywords:
  - Large Language Model
  - Cultural Alignment
  - Regional Language Models
  - Community-authored Corpora
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2505.21548
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:03:16.552481",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Cultural Alignment",
    "Regional Language Models",
    "Community-authored Corpora"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Cultural Alignment": 0.78,
    "Regional Language Models": 0.72,
    "Community-authored Corpora": 0.7
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
        "rationale": "This is a foundational concept in the paper, linking to broader discussions on language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cultural Alignment",
        "canonical": "Cultural Alignment",
        "aliases": [
          "Cultural Fit"
        ],
        "category": "unique_technical",
        "rationale": "Central to the paper's thesis, it addresses the alignment of models with local cultures.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Regional LLMs",
        "canonical": "Regional Language Models",
        "aliases": [
          "Localized LLMs"
        ],
        "category": "unique_technical",
        "rationale": "Highlights the focus on locally adapted language models, a key theme in the paper.",
        "novelty_score": 0.65,
        "connectivity_score": 0.65,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "Community-authored Corpora",
        "canonical": "Community-authored Corpora",
        "aliases": [
          "Community Data"
        ],
        "category": "unique_technical",
        "rationale": "Emphasizes the importance of community-driven data for model training.",
        "novelty_score": 0.68,
        "connectivity_score": 0.55,
        "specificity_score": 0.78,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "values",
      "practices",
      "surveys"
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
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cultural Alignment",
      "resolved_canonical": "Cultural Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Regional LLMs",
      "resolved_canonical": "Regional Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.65,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Community-authored Corpora",
      "resolved_canonical": "Community-authored Corpora",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.55,
        "specificity": 0.78,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Fluent but Foreign: Even Regional LLMs Lack Cultural Alignment

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.21548.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2505.21548](https://arxiv.org/abs/2505.21548)

## 🔗 유사한 논문
- [[2025-09-22/CultureScope_ A Dimensional Lens for Probing Cultural Understanding in LLMs_20250922|CultureScope: A Dimensional Lens for Probing Cultural Understanding in LLMs]] (86.3% similar)
- [[2025-09-19/Ticket-Bench_ A Kickoff for Multilingual and Regionalized Agent Evaluation_20250919|Ticket-Bench: A Kickoff for Multilingual and Regionalized Agent Evaluation]] (83.2% similar)
- [[2025-09-22/A method for improving multilingual quality and diversity of instruction fine-tuning datasets_20250922|A method for improving multilingual quality and diversity of instruction fine-tuning datasets]] (82.8% similar)
- [[2025-09-22/The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation_20250922|The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation]] (82.4% similar)
- [[2025-09-22/Benchmark of stylistic variation in LLM-generated texts_20250922|Benchmark of stylistic variation in LLM-generated texts]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Cultural Alignment|Cultural Alignment]], [[keywords/Regional Language Models|Regional Language Models]], [[keywords/Community-authored Corpora|Community-authored Corpora]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.21548v2 Announce Type: replace-cross 
Abstract: Large language models (LLMs) are used worldwide, yet exhibit Western cultural tendencies. Many countries are now building ``regional'' LLMs, but it remains unclear whether they reflect local values and practices or merely speak local languages. Using India as a case study, we evaluate six Indic and six global LLMs on two dimensions -- values and practices -- grounded in nationally representative surveys and community-sourced QA datasets. Across tasks, Indic models do not align better with Indian norms than global models; in fact, a U.S. respondent is a closer proxy for Indian values than any Indic model. Prompting and regional fine-tuning fail to recover alignment and can even degrade existing knowledge. We attribute this to scarce culturally grounded data, especially for pretraining. We position cultural evaluation as a first-class requirement alongside multilingual benchmarks and offer a reusable, community-grounded methodology. We call for native, community-authored corpora and thick x wide evaluations to build truly sovereign LLMs.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 서구 문화적 경향을 보이는 문제를 지적하며, 인도를 사례로 지역적 LLM이 실제로 지역의 가치와 관행을 반영하는지를 평가합니다. 연구 결과, 인도 지역 모델이 글로벌 모델보다 인도 문화에 더 잘 맞지 않으며, 미국 응답자가 인도 가치를 더 잘 대변할 수 있다는 점을 발견했습니다. 프롬프트 조정과 지역적 미세 조정도 효과적이지 않았습니다. 이는 문화적으로 기반이 된 데이터의 부족 때문으로, 저자들은 문화적 평가를 다국어 벤치마크와 함께 중요한 요구사항으로 제안하며, 지역 사회가 작성한 코퍼스와 폭넓은 평가를 통해 진정한 주권적 LLM을 구축할 것을 촉구합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 전 세계적으로 사용되지만 서구 문화적 경향을 보인다.
- 2. 인도 사례 연구를 통해 지역 LLMs가 인도적 규범에 더 잘 맞지 않음을 발견했다.
- 3. 프롬프트 및 지역 미세 조정은 정렬을 회복하지 못하고 기존 지식을 저하시킬 수 있다.
- 4. 문화적으로 기반이 된 데이터의 부족이 이러한 문제의 원인으로 지목된다.
- 5. 문화 평가를 다국어 벤치마크와 함께 중요한 요구사항으로 제안하고, 지역 사회가 작성한 코퍼스의 필요성을 강조한다.


---

*Generated on 2025-09-24 01:03:16*