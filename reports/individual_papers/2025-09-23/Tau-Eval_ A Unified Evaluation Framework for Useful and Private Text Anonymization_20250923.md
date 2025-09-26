---
keywords:
  - Text Anonymization
  - Privacy Protection
  - Information Preservation
  - Utility Task Sensitivity
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2506.05979
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:03:43.892178",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Text Anonymization",
    "Privacy Protection",
    "Information Preservation",
    "Utility Task Sensitivity"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Text Anonymization": 0.78,
    "Privacy Protection": 0.8,
    "Information Preservation": 0.77,
    "Utility Task Sensitivity": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "text anonymization",
        "canonical": "Text Anonymization",
        "aliases": [
          "text de-identification",
          "data anonymization"
        ],
        "category": "unique_technical",
        "rationale": "Text anonymization is central to the paper's focus on privacy and utility trade-offs.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "privacy protection",
        "canonical": "Privacy Protection",
        "aliases": [
          "data privacy",
          "information privacy"
        ],
        "category": "broad_technical",
        "rationale": "Privacy protection is a key aspect of evaluating text anonymization methods.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "information preservation",
        "canonical": "Information Preservation",
        "aliases": [
          "data retention",
          "information retention"
        ],
        "category": "unique_technical",
        "rationale": "Information preservation is crucial for maintaining utility in anonymized texts.",
        "novelty_score": 0.62,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "utility task sensitivity",
        "canonical": "Utility Task Sensitivity",
        "aliases": [
          "task sensitivity",
          "utility sensitivity"
        ],
        "category": "unique_technical",
        "rationale": "Utility task sensitivity is a novel concept introduced for evaluating anonymization.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "framework",
      "benchmarking",
      "Python library"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "text anonymization",
      "resolved_canonical": "Text Anonymization",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "privacy protection",
      "resolved_canonical": "Privacy Protection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "information preservation",
      "resolved_canonical": "Information Preservation",
      "decision": "linked",
      "scores": {
        "novelty": 0.62,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "utility task sensitivity",
      "resolved_canonical": "Utility Task Sensitivity",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Tau-Eval: A Unified Evaluation Framework for Useful and Private Text Anonymization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.05979.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2506.05979](https://arxiv.org/abs/2506.05979)

## 🔗 유사한 논문
- [[2025-09-23/MEF_ A Systematic Evaluation Framework for Text-to-Image Models_20250923|MEF: A Systematic Evaluation Framework for Text-to-Image Models]] (79.2% similar)
- [[2025-09-19/Controllable Localized Face Anonymization Via Diffusion Inpainting_20250919|Controllable Localized Face Anonymization Via Diffusion Inpainting]] (78.9% similar)
- [[2025-09-18/SynBench_ A Benchmark for Differentially Private Text Generation_20250918|SynBench: A Benchmark for Differentially Private Text Generation]] (78.8% similar)
- [[2025-09-23/RadEval_ A framework for radiology text evaluation_20250923|RadEval: A framework for radiology text evaluation]] (78.6% similar)
- [[2025-09-23/Privacy in Action_ Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents_20250923|Privacy in Action: Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents]] (78.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Privacy Protection|Privacy Protection]]
**⚡ Unique Technical**: [[keywords/Text Anonymization|Text Anonymization]], [[keywords/Information Preservation|Information Preservation]], [[keywords/Utility Task Sensitivity|Utility Task Sensitivity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.05979v2 Announce Type: replace 
Abstract: Text anonymization is the process of removing or obfuscating information from textual data to protect the privacy of individuals. This process inherently involves a complex trade-off between privacy protection and information preservation, where stringent anonymization methods can significantly impact the text's utility for downstream applications. Evaluating the effectiveness of text anonymization proves challenging from both privacy and utility perspectives, as there is no universal benchmark that can comprehensively assess anonymization techniques across diverse, and sometimes contradictory contexts. We present Tau-Eval, an open-source framework for benchmarking text anonymization methods through the lens of privacy and utility task sensitivity. A Python library, code, documentation and tutorials are publicly available.

## 📝 요약

이 논문은 텍스트 익명화의 효과를 평가하기 위한 오픈 소스 프레임워크인 Tau-Eval을 소개합니다. 텍스트 익명화는 개인의 프라이버시를 보호하기 위해 텍스트 데이터에서 정보를 제거하거나 모호하게 만드는 과정으로, 프라이버시 보호와 정보 보존 간의 복잡한 균형을 요구합니다. Tau-Eval은 다양한 문맥에서 익명화 기법을 프라이버시와 유용성의 관점에서 평가할 수 있는 도구를 제공합니다. 이 프레임워크는 Python 라이브러리, 코드, 문서 및 튜토리얼을 포함하여 공개적으로 제공됩니다.

## 🎯 주요 포인트

- 1. 텍스트 익명화는 개인의 프라이버시를 보호하기 위해 텍스트 데이터에서 정보를 제거하거나 모호하게 만드는 과정이다.
- 2. 익명화 과정에서는 프라이버시 보호와 정보 보존 사이의 복잡한 균형이 필요하며, 엄격한 익명화 방법은 텍스트의 활용성을 크게 저하시킬 수 있다.
- 3. 텍스트 익명화의 효과를 평가하는 것은 다양한 맥락에서 포괄적으로 평가할 수 있는 보편적인 기준이 없어 어려움을 겪고 있다.
- 4. Tau-Eval은 프라이버시와 유틸리티 작업 민감성의 관점에서 텍스트 익명화 방법을 벤치마킹하기 위한 오픈 소스 프레임워크를 제공한다.
- 5. Tau-Eval의 파이썬 라이브러리, 코드, 문서 및 튜토리얼이 공개적으로 제공된다.


---

*Generated on 2025-09-24 04:03:43*