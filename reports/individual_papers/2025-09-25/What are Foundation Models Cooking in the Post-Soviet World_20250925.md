---
keywords:
  - Large Language Model
  - Multimodal Learning
  - Question Answering
  - Code Mixing
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2502.18583
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:51:42.842455",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multimodal Learning",
    "Question Answering",
    "Code Mixing"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multimodal Learning": 0.82,
    "Question Answering": 0.78,
    "Code Mixing": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "foundation models",
        "canonical": "Large Language Model",
        "aliases": [
          "foundation models"
        ],
        "category": "broad_technical",
        "rationale": "Foundation models are a subset of Large Language Models, which are central to the study.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "multimodal dataset",
        "canonical": "Multimodal Learning",
        "aliases": [
          "multimodal dataset"
        ],
        "category": "specific_connectable",
        "rationale": "The dataset is key to the study's approach, linking to multimodal learning concepts.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Question Answering",
        "canonical": "Question Answering",
        "aliases": [
          "QA"
        ],
        "category": "specific_connectable",
        "rationale": "QA is a primary method used in the study, relevant to evaluating model performance.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Russian-Ukrainian code mixing",
        "canonical": "Code Mixing",
        "aliases": [
          "Russian-Ukrainian code mixing"
        ],
        "category": "unique_technical",
        "rationale": "This linguistic phenomenon is crucial for understanding the dataset's challenges.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "Post-Soviet",
      "cultural understanding"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "foundation models",
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
      "candidate_surface": "multimodal dataset",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Question Answering",
      "resolved_canonical": "Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Russian-Ukrainian code mixing",
      "resolved_canonical": "Code Mixing",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# What are Foundation Models Cooking in the Post-Soviet World?

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2502.18583.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2502.18583](https://arxiv.org/abs/2502.18583)

## 🔗 유사한 논문
- [[2025-09-23/Seeing Culture_ A Benchmark for Visual Reasoning and Grounding_20250923|Seeing Culture: A Benchmark for Visual Reasoning and Grounding]] (79.6% similar)
- [[2025-09-22/CultureScope_ A Dimensional Lens for Probing Cultural Understanding in LLMs_20250922|CultureScope: A Dimensional Lens for Probing Cultural Understanding in LLMs]] (78.6% similar)
- [[2025-09-23/Fluent but Foreign_ Even Regional LLMs Lack Cultural Alignment_20250923|Fluent but Foreign: Even Regional LLMs Lack Cultural Alignment]] (77.2% similar)
- [[2025-09-19/RAcQUEt_ Unveiling the Dangers of Overlooked Referential Ambiguity in Visual LLMs_20250919|RAcQUEt: Unveiling the Dangers of Overlooked Referential Ambiguity in Visual LLMs]] (77.1% similar)
- [[2025-09-23/MAKIEval_ A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs_20250923|MAKIEval: A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs]] (77.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Question Answering|Question Answering]]
**⚡ Unique Technical**: [[keywords/Code Mixing|Code Mixing]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.18583v3 Announce Type: replace 
Abstract: The culture of the Post-Soviet states is complex, shaped by a turbulent history that continues to influence current events. In this study, we investigate the Post-Soviet cultural food knowledge of foundation models by constructing BORSch, a multimodal dataset encompassing 1147 and 823 dishes in the Russian and Ukrainian languages, centered around the Post-Soviet region. We demonstrate that leading models struggle to correctly identify the origins of dishes from Post-Soviet nations in both text-only and multimodal Question Answering (QA), instead over-predicting countries linked to the language the question is asked in. Through analysis of pretraining data, we show that these results can be explained by misleading dish-origin co-occurrences, along with linguistic phenomena such as Russian-Ukrainian code mixing. Finally, to move beyond QA-based assessments, we test models' abilities to produce accurate visual descriptions of dishes. The weak correlation between this task and QA suggests that QA alone may be insufficient as an evaluation of cultural understanding. To foster further research, we will make BORSch publicly available at https://github.com/alavrouk/BORSch.

## 📝 요약

이 연구는 포스트소비에트 국가들의 복잡한 문화적 음식 지식을 조사하기 위해 BORSch라는 다중 모달 데이터셋을 구축했습니다. 연구 결과, 주요 모델들이 포스트소비에트 국가들의 요리 기원을 정확히 식별하지 못하고, 질문이 제기된 언어와 관련된 국가를 과대 예측하는 경향이 있음을 발견했습니다. 이는 잘못된 요리 기원과 언어적 현상인 러시아-우크라이나 코드 혼합 때문임을 분석을 통해 밝혔습니다. 또한, 모델들이 요리에 대한 시각적 설명을 정확히 생성할 수 있는지를 테스트한 결과, QA와의 약한 상관관계가 드러나 QA만으로는 문화적 이해를 평가하기에 충분하지 않음을 시사합니다. 연구 촉진을 위해 BORSch 데이터셋은 공개될 예정입니다.

## 🎯 주요 포인트

- 1. 포스트소비에트 국가의 문화는 복잡하며, 이는 현재의 사건에도 영향을 미치고 있다.
- 2. 연구는 러시아어와 우크라이나어로 된 1147개와 823개의 요리를 포함하는 다중모달 데이터셋 BORSch를 구축하여 포스트소비에트 지역의 문화적 음식 지식을 조사한다.
- 3. 주요 모델들은 포스트소비에트 국가의 요리 기원을 정확히 식별하는 데 어려움을 겪으며, 질문이 제기된 언어와 관련된 국가를 과대 예측하는 경향이 있다.
- 4. 요리 기원과의 잘못된 공존 현상 및 러시아-우크라이나 코드 혼합과 같은 언어적 현상이 이러한 결과를 설명할 수 있음을 보여준다.
- 5. QA 기반 평가를 넘어, 모델의 요리 시각적 설명 생성 능력을 테스트하며, QA와의 약한 상관관계는 QA만으로는 문화적 이해 평가에 충분하지 않을 수 있음을 시사한다.


---

*Generated on 2025-09-26 08:51:42*