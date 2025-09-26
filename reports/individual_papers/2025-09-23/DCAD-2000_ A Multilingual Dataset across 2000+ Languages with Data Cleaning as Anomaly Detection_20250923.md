---
keywords:
  - Large Language Model
  - Multilingual Dataset
  - Data Cleaning as Anomaly Detection
  - Common Crawl
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2502.11546
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:48:47.976635",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multilingual Dataset",
    "Data Cleaning as Anomaly Detection",
    "Common Crawl"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multilingual Dataset": 0.88,
    "Data Cleaning as Anomaly Detection": 0.82,
    "Common Crawl": 0.8
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
        "rationale": "Large Language Models are central to the paper's focus on multilingual datasets and are a key concept in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multilingual Datasets",
        "canonical": "Multilingual Dataset",
        "aliases": [
          "Multilingual Corpora"
        ],
        "category": "specific_connectable",
        "rationale": "The paper introduces a new multilingual dataset, which is crucial for linking multilingual research.",
        "novelty_score": 0.75,
        "connectivity_score": 0.8,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Data Cleaning as Anomaly Detection",
        "canonical": "Data Cleaning as Anomaly Detection",
        "aliases": [
          "DCAD"
        ],
        "category": "unique_technical",
        "rationale": "This novel approach to data cleaning is a unique contribution of the paper and offers new linking opportunities.",
        "novelty_score": 0.8,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Common Crawl Data",
        "canonical": "Common Crawl",
        "aliases": [
          "Common Crawl Dataset"
        ],
        "category": "specific_connectable",
        "rationale": "Common Crawl is a widely used dataset in NLP, making it a strong candidate for linking.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "task"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multilingual Datasets",
      "resolved_canonical": "Multilingual Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.8,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Data Cleaning as Anomaly Detection",
      "resolved_canonical": "Data Cleaning as Anomaly Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Common Crawl Data",
      "resolved_canonical": "Common Crawl",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# DCAD-2000: A Multilingual Dataset across 2000+ Languages with Data Cleaning as Anomaly Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2502.11546.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2502.11546](https://arxiv.org/abs/2502.11546)

## 🔗 유사한 논문
- [[2025-09-22/A method for improving multilingual quality and diversity of instruction fine-tuning datasets_20250922|A method for improving multilingual quality and diversity of instruction fine-tuning datasets]] (83.0% similar)
- [[2025-09-23/CUTE_ A Multilingual Dataset for Enhancing Cross-Lingual Knowledge Transfer in Low-Resource Languages_20250923|CUTE: A Multilingual Dataset for Enhancing Cross-Lingual Knowledge Transfer in Low-Resource Languages]] (83.0% similar)
- [[2025-09-23/DIVERS-Bench_ Evaluating Language Identification Across Domain Shifts and Code-Switching_20250923|DIVERS-Bench: Evaluating Language Identification Across Domain Shifts and Code-Switching]] (81.8% similar)
- [[2025-09-22/DynamicNER_ A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition_20250922|DynamicNER: A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition]] (81.3% similar)
- [[2025-09-22/CultureScope_ A Dimensional Lens for Probing Cultural Understanding in LLMs_20250922|CultureScope: A Dimensional Lens for Probing Cultural Understanding in LLMs]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multilingual Dataset|Multilingual Dataset]], [[keywords/Common Crawl|Common Crawl]]
**⚡ Unique Technical**: [[keywords/Data Cleaning as Anomaly Detection|Data Cleaning as Anomaly Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.11546v3 Announce Type: replace 
Abstract: The rapid development of multilingual large language models (LLMs) highlights the need for high-quality, diverse, and clean multilingual datasets. In this paper, we introduce DCAD-2000 (Data Cleaning as Anomaly Detection), a large-scale multilingual corpus built using newly extracted Common Crawl data and existing multilingual datasets. DCAD-2000 includes over 2,282 languages, 46.72TB of data, and 8.63 billion documents, spanning 155 high- and medium-resource languages and 159 writing scripts. To overcome the limitations of current data cleaning methods, which rely on manual heuristic thresholds, we propose reframing data cleaning as an anomaly detection task. This dynamic filtering approach significantly enhances data quality by identifying and removing noisy or anomalous content. We evaluate the quality of DCAD-2000 on the FineTask benchmark, demonstrating substantial improvements in multilingual dataset quality and task performance.

## 📝 요약

이 논문에서는 다국어 대형 언어 모델(LLM)의 발전에 따라 고품질의 다국어 데이터셋의 필요성을 강조하며, DCAD-2000이라는 대규모 다국어 코퍼스를 소개합니다. DCAD-2000은 2,282개 언어와 46.72TB의 데이터를 포함하며, 8.63억 개의 문서를 통해 155개의 고·중자원 언어와 159개의 문자 체계를 다룹니다. 기존의 수작업 기반 데이터 정제 방법의 한계를 극복하기 위해 데이터 정제를 이상 탐지 과제로 재구성하여 동적 필터링 방법을 제안합니다. 이를 통해 잡음이나 이상 콘텐츠를 식별하고 제거하여 데이터 품질을 크게 향상시킵니다. FineTask 벤치마크를 통해 DCAD-2000의 품질을 평가한 결과, 다국어 데이터셋의 품질과 과제 수행 능력이 크게 개선됨을 확인했습니다.

## 🎯 주요 포인트

- 1. DCAD-2000은 2,282개 이상의 언어와 46.72TB의 데이터를 포함하는 대규모 다국어 코퍼스입니다.
- 2. 기존의 수작업 임계값에 의존하는 데이터 정제 방법의 한계를 극복하기 위해 데이터 정제를 이상 탐지 작업으로 재구성했습니다.
- 3. 동적 필터링 접근법을 통해 잡음이 많거나 이상한 콘텐츠를 식별하고 제거하여 데이터 품질을 크게 향상시켰습니다.
- 4. FineTask 벤치마크를 통해 DCAD-2000의 품질을 평가한 결과, 다국어 데이터셋의 품질과 작업 성능이 크게 개선되었습니다.


---

*Generated on 2025-09-24 03:48:47*