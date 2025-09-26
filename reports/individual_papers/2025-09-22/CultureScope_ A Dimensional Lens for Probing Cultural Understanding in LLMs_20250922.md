---
keywords:
  - Large Language Model
  - Cultural Understanding
  - Cultural Iceberg Theory
  - Multilingual Data
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.16188
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:31:17.676405",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Cultural Understanding",
    "Cultural Iceberg Theory",
    "Multilingual Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Cultural Understanding": 0.78,
    "Cultural Iceberg Theory": 0.7,
    "Multilingual Data": 0.72
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
        "rationale": "Central to the paper's focus on cultural understanding in AI models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cultural Understanding",
        "canonical": "Cultural Understanding",
        "aliases": [
          "Cultural Competence"
        ],
        "category": "unique_technical",
        "rationale": "Key concept for evaluating AI models in diverse cultural contexts.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Cultural Iceberg Theory",
        "canonical": "Cultural Iceberg Theory",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Provides a foundational framework for the proposed evaluation schema.",
        "novelty_score": 0.8,
        "connectivity_score": 0.5,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Multilingual Data",
        "canonical": "Multilingual Data",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Relevant to discussions on enhancing cultural understanding in LLMs.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.6,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "evaluation framework",
      "experimental results"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cultural Understanding",
      "resolved_canonical": "Cultural Understanding",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Cultural Iceberg Theory",
      "resolved_canonical": "Cultural Iceberg Theory",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.5,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Multilingual Data",
      "resolved_canonical": "Multilingual Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.6,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# CultureScope: A Dimensional Lens for Probing Cultural Understanding in LLMs

**Korean Title:** CultureScope: LLM에서 문화적 이해를 탐구하기 위한 차원적 렌즈

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16188.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.16188](https://arxiv.org/abs/2509.16188)

## 🔗 유사한 논문
- [[2025-09-22/A method for improving multilingual quality and diversity of instruction fine-tuning datasets_20250922|A method for improving multilingual quality and diversity of instruction fine-tuning datasets]] (84.8% similar)
- [[2025-09-19/Position_ Thematic Analysis of Unstructured Clinical Transcripts with Large Language Models_20250919|Position: Thematic Analysis of Unstructured Clinical Transcripts with Large Language Models]] (84.6% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (84.5% similar)
- [[2025-09-22/MUG-Eval_ A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language_20250922|MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language]] (84.4% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (84.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multilingual Data|Multilingual Data]]
**⚡ Unique Technical**: [[keywords/Cultural Understanding|Cultural Understanding]], [[keywords/Cultural Iceberg Theory|Cultural Iceberg Theory]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16188v1 Announce Type: cross 
Abstract: As large language models (LLMs) are increasingly deployed in diverse cultural environments, evaluating their cultural understanding capability has become essential for ensuring trustworthy and culturally aligned applications. However, most existing benchmarks lack comprehensiveness and are challenging to scale and adapt across different cultural contexts, because their frameworks often lack guidance from well-established cultural theories and tend to rely on expert-driven manual annotations. To address these issues, we propose CultureScope, the most comprehensive evaluation framework to date for assessing cultural understanding in LLMs. Inspired by the cultural iceberg theory, we design a novel dimensional schema for cultural knowledge classification, comprising 3 layers and 140 dimensions, which guides the automated construction of culture-specific knowledge bases and corresponding evaluation datasets for any given languages and cultures. Experimental results demonstrate that our method can effectively evaluate cultural understanding. They also reveal that existing large language models lack comprehensive cultural competence, and merely incorporating multilingual data does not necessarily enhance cultural understanding. All code and data files are available at https://github.com/HoganZinger/Culture

## 🔍 Abstract (한글 번역)

arXiv:2509.16188v1 발표 유형: 교차  
초록: 대형 언어 모델(LLM)이 다양한 문화적 환경에서 점점 더 많이 배치됨에 따라, 이들의 문화적 이해 능력을 평가하는 것이 신뢰할 수 있고 문화적으로 조화로운 응용 프로그램을 보장하는 데 필수적이 되었습니다. 그러나 대부분의 기존 벤치마크는 포괄성이 부족하고, 잘 확립된 문화 이론의 지침이 부족하며, 전문가 주도의 수동 주석에 의존하는 경향이 있어 다양한 문화적 맥락에 걸쳐 확장하고 적응하기 어렵습니다. 이러한 문제를 해결하기 위해, 우리는 LLM의 문화적 이해를 평가하기 위한 가장 포괄적인 평가 프레임워크인 CultureScope을 제안합니다. 문화적 빙산 이론에서 영감을 받아, 우리는 3개의 층과 140개의 차원으로 구성된 새로운 차원적 스키마를 설계하여, 특정 문화 지식 기반과 해당 평가 데이터셋을 자동으로 구축할 수 있도록 합니다. 실험 결과는 우리의 방법이 문화적 이해를 효과적으로 평가할 수 있음을 보여줍니다. 또한, 기존의 대형 언어 모델이 포괄적인 문화적 역량이 부족하며, 단순히 다국어 데이터를 통합하는 것이 반드시 문화적 이해를 향상시키는 것은 아님을 드러냅니다. 모든 코드와 데이터 파일은 https://github.com/HoganZinger/Culture에서 이용할 수 있습니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 문화적 이해 능력을 평가하기 위한 포괄적인 프레임워크인 CultureScope를 제안합니다. 기존의 평가 기준은 문화적 맥락에 따라 확장 및 적응이 어려웠으나, CultureScope는 문화 아이스버그 이론을 기반으로 3개의 층과 140개의 차원으로 구성된 새로운 분류 체계를 설계하여 자동화된 문화 지식 베이스와 평가 데이터셋을 구축합니다. 실험 결과, 이 방법이 효과적으로 문화적 이해를 평가할 수 있음을 보여주며, 현재의 대형 언어 모델이 문화적 역량이 부족함을 밝혔습니다. 다국어 데이터를 단순히 추가하는 것만으로는 문화적 이해가 향상되지 않는다는 점도 강조됩니다. 모든 코드와 데이터는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)의 문화적 이해 능력을 평가하는 것이 신뢰할 수 있는 문화적 정렬 응용 프로그램을 보장하는 데 필수적입니다.
- 2. 기존 벤치마크는 문화적 맥락에 따라 확장 및 적응하기 어렵고, 잘 확립된 문화 이론의 지침이 부족하여 한계가 있습니다.
- 3. CultureScope는 문화적 이해를 평가하기 위한 가장 포괄적인 프레임워크로, 문화 지식 분류를 위한 3층 140차원의 새로운 차원 스키마를 설계하였습니다.
- 4. 실험 결과, 기존 대형 언어 모델은 포괄적인 문화적 역량이 부족하며, 다국어 데이터를 단순히 통합하는 것만으로는 문화적 이해가 향상되지 않는다는 것을 보여줍니다.
- 5. CultureScope의 코드와 데이터 파일은 공개되어 있으며, 다양한 언어와 문화에 대한 평가 데이터셋을 자동으로 구축할 수 있습니다.


---

*Generated on 2025-09-23 09:31:17*