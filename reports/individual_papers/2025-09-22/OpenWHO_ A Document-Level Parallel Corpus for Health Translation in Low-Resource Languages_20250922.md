---
keywords:
  - Large Language Model
  - Low-Resource Languages
  - Document-Level Translation
  - Health Domain
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2508.16048
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:08:40.426084",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Low-Resource Languages",
    "Document-Level Translation",
    "Health Domain"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Low-Resource Languages": 0.78,
    "Document-Level Translation": 0.77,
    "Health Domain": 0.75
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
        "rationale": "Large Language Models are central to the paper's evaluation of translation performance, linking to broader AI advancements.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "low-resource languages",
        "canonical": "Low-Resource Languages",
        "aliases": [
          "under-resourced languages"
        ],
        "category": "unique_technical",
        "rationale": "The focus on low-resource languages is unique to this research domain and crucial for understanding the paper's contribution.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "document-level translation",
        "canonical": "Document-Level Translation",
        "aliases": [
          "document translation"
        ],
        "category": "unique_technical",
        "rationale": "Document-level translation is a specific approach that enhances translation accuracy in specialized domains.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "health domain",
        "canonical": "Health Domain",
        "aliases": [
          "medical domain",
          "healthcare domain"
        ],
        "category": "unique_technical",
        "rationale": "The health domain is a specialized area where translation accuracy is critical, linking to domain-specific research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.72,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
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
      "candidate_surface": "low-resource languages",
      "resolved_canonical": "Low-Resource Languages",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "document-level translation",
      "resolved_canonical": "Document-Level Translation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "health domain",
      "resolved_canonical": "Health Domain",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.72,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# OpenWHO: A Document-Level Parallel Corpus for Health Translation in Low-Resource Languages

**Korean Title:** OpenWHO: 저자원 언어의 건강 번역을 위한 문서 수준 병렬 코퍼스

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2508.16048.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2508.16048](https://arxiv.org/abs/2508.16048)

## 🔗 유사한 논문
- [[2025-09-22/MedCOD_ Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework_20250922|MedCOD: Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework]] (82.1% similar)
- [[2025-09-19/OpenLens AI_ Fully Autonomous Research Agent for Health Infomatics_20250919|OpenLens AI: Fully Autonomous Research Agent for Health Infomatics]] (80.6% similar)
- [[2025-09-22/UPRPRC_ Unified Pipeline for Reproducing Parallel Resources -- Corpus from the United Nations_20250922|UPRPRC: Unified Pipeline for Reproducing Parallel Resources -- Corpus from the United Nations]] (79.9% similar)
- [[2025-09-22/EHR-MCP_ Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol_20250922|EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol]] (79.6% similar)
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL: Toward Expert-Level Medical Text Validation with Language Models]] (79.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Low-Resource Languages|Low-Resource Languages]], [[keywords/Document-Level Translation|Document-Level Translation]], [[keywords/Health Domain|Health Domain]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.16048v3 Announce Type: replace-cross 
Abstract: In machine translation (MT), health is a high-stakes domain characterised by widespread deployment and domain-specific vocabulary. However, there is a lack of MT evaluation datasets for low-resource languages in this domain. To address this gap, we introduce OpenWHO, a document-level parallel corpus of 2,978 documents and 26,824 sentences from the World Health Organization's e-learning platform. Sourced from expert-authored, professionally translated materials shielded from web-crawling, OpenWHO spans a diverse range of over 20 languages, of which nine are low-resource. Leveraging this new resource, we evaluate modern large language models (LLMs) against traditional MT models. Our findings reveal that LLMs consistently outperform traditional MT models, with Gemini 2.5 Flash achieving a +4.79 ChrF point improvement over NLLB-54B on our low-resource test set. Further, we investigate how LLM context utilisation affects accuracy, finding that the benefits of document-level translation are most pronounced in specialised domains like health. We release the OpenWHO corpus to encourage further research into low-resource MT in the health domain.

## 🔍 Abstract (한글 번역)

arXiv:2508.16048v3 발표 유형: 교체-크로스  
초록: 기계 번역(MT)에서 건강 분야는 광범위한 배포와 분야별 어휘로 특징지어지는 고위험 분야입니다. 그러나 이 분야에서 저자원 언어에 대한 MT 평가 데이터셋은 부족합니다. 이러한 격차를 해소하기 위해, 우리는 세계보건기구의 e-러닝 플랫폼에서 제공되는 2,978개의 문서와 26,824개의 문장으로 구성된 문서 수준의 병렬 코퍼스인 OpenWHO를 소개합니다. 전문가가 작성하고 전문적으로 번역된 자료로, 웹 크롤링으로부터 보호된 OpenWHO는 20개 이상의 다양한 언어를 포함하며, 그 중 9개는 저자원 언어입니다. 이 새로운 자원을 활용하여, 우리는 현대의 대형 언어 모델(LLM)을 전통적인 MT 모델과 비교 평가합니다. 우리의 연구 결과는 LLM이 전통적인 MT 모델보다 일관되게 우수하다는 것을 보여주며, Gemini 2.5 Flash는 저자원 테스트 세트에서 NLLB-54B보다 ChrF 점수가 +4.79 향상되었습니다. 또한, LLM의 문맥 활용이 정확도에 미치는 영향을 조사하여, 문서 수준 번역의 이점이 건강과 같은 전문 분야에서 가장 두드러진다는 것을 발견했습니다. 우리는 건강 분야의 저자원 MT 연구를 촉진하기 위해 OpenWHO 코퍼스를 공개합니다.

## 📝 요약

이 논문은 저자들이 세계보건기구의 e-learning 플랫폼에서 수집한 2,978개의 문서와 26,824개의 문장으로 구성된 OpenWHO라는 병렬 코퍼스를 소개합니다. 이 코퍼스는 20개 이상의 언어를 포함하며, 그중 9개는 자원이 부족한 언어입니다. 이를 통해 최신 대형 언어 모델(LLM)과 전통적인 기계 번역(MT) 모델을 비교 평가한 결과, LLM이 전통적인 MT 모델보다 우수한 성능을 보였으며, 특히 Gemini 2.5 Flash 모델이 NLLB-54B 모델보다 ChrF 점수가 4.79점 더 높았습니다. 또한, 문서 수준 번역의 맥락 활용이 정확도에 미치는 영향을 조사하여, 건강과 같은 전문 분야에서 그 효과가 두드러짐을 발견했습니다. OpenWHO 코퍼스는 건강 분야의 저자원 언어 MT 연구를 촉진하기 위해 공개되었습니다.

## 🎯 주요 포인트

- 1. OpenWHO는 WHO의 e-learning 플랫폼에서 수집된 2,978개의 문서와 26,824개의 문장으로 구성된 병렬 코퍼스로, 20개 이상의 언어를 포함하며 그 중 9개는 저자원 언어입니다.
- 2. OpenWHO를 활용한 연구에서 현대 대형 언어 모델(LLM)이 전통적인 기계 번역(MT) 모델보다 일관되게 우수한 성능을 보였습니다.
- 3. Gemini 2.5 Flash 모델은 저자원 테스트 세트에서 NLLB-54B 모델에 비해 ChrF 점수가 +4.79 향상되었습니다.
- 4. 문서 수준 번역의 이점은 건강과 같은 전문화된 도메인에서 가장 두드러지며, LLM의 문맥 활용이 번역 정확도에 미치는 영향을 조사했습니다.
- 5. OpenWHO 코퍼스를 공개하여 건강 분야의 저자원 기계 번역 연구를 촉진하고자 합니다.


---

*Generated on 2025-09-23 10:08:40*