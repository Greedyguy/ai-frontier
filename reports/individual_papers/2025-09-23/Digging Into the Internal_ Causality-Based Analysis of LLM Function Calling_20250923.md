---
keywords:
  - Function Calling
  - Large Language Model
  - Causal Interventions
  - Safety Robustness
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16268
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:10:35.570559",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Function Calling",
    "Large Language Model",
    "Causal Interventions",
    "Safety Robustness"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Function Calling": 0.78,
    "Large Language Model": 0.8,
    "Causal Interventions": 0.77,
    "Safety Robustness": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Function Calling",
        "canonical": "Function Calling",
        "aliases": [
          "FC"
        ],
        "category": "unique_technical",
        "rationale": "Function Calling is central to the paper's analysis and offers a unique perspective on LLM interaction.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "The study focuses on LLMs, which are a fundamental component in the discussed techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Causal Interventions",
        "canonical": "Causal Interventions",
        "aliases": [
          "causal analysis"
        ],
        "category": "specific_connectable",
        "rationale": "Causal interventions are key to understanding the internal mechanisms of LLMs in the study.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Safety Robustness",
        "canonical": "Safety Robustness",
        "aliases": [
          "LLM safety"
        ],
        "category": "specific_connectable",
        "rationale": "Enhancing safety robustness is a critical application scenario discussed in the paper.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
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
      "candidate_surface": "Function Calling",
      "resolved_canonical": "Function Calling",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Causal Interventions",
      "resolved_canonical": "Causal Interventions",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Safety Robustness",
      "resolved_canonical": "Safety Robustness",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Digging Into the Internal: Causality-Based Analysis of LLM Function Calling

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16268.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16268](https://arxiv.org/abs/2509.16268)

## 🔗 유사한 논문
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (86.8% similar)
- [[2025-09-19/From Capabilities to Performance_ Evaluating Key Functional Properties of LLM Architectures in Penetration Testing_20250919|From Capabilities to Performance: Evaluating Key Functional Properties of LLM Architectures in Penetration Testing]] (85.1% similar)
- [[2025-09-23/Correlation or Causation_ Analyzing the Causal Structures of LLM and LRM Reasoning Process_20250923|Correlation or Causation: Analyzing the Causal Structures of LLM and LRM Reasoning Process]] (83.8% similar)
- [[2025-09-22/Can Large Language Models Infer Causal Relationships from Real-World Text?_20250922|Can Large Language Models Infer Causal Relationships from Real-World Text?]] (83.6% similar)
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (83.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Causal Interventions|Causal Interventions]], [[keywords/Safety Robustness|Safety Robustness]]
**⚡ Unique Technical**: [[keywords/Function Calling|Function Calling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16268v1 Announce Type: cross 
Abstract: Function calling (FC) has emerged as a powerful technique for facilitating large language models (LLMs) to interact with external systems and perform structured tasks. However, the mechanisms through which it influences model behavior remain largely under-explored. Besides, we discover that in addition to the regular usage of FC, this technique can substantially enhance the compliance of LLMs with user instructions. These observations motivate us to leverage causality, a canonical analysis method, to investigate how FC works within LLMs. In particular, we conduct layer-level and token-level causal interventions to dissect FC's impact on the model's internal computational logic when responding to user queries. Our analysis confirms the substantial influence of FC and reveals several in-depth insights into its mechanisms. To further validate our findings, we conduct extensive experiments comparing the effectiveness of FC-based instructions against conventional prompting methods. We focus on enhancing LLM safety robustness, a critical LLM application scenario, and evaluate four mainstream LLMs across two benchmark datasets. The results are striking: FC shows an average performance improvement of around 135% over conventional prompting methods in detecting malicious inputs, demonstrating its promising potential to enhance LLM reliability and capability in practical applications.

## 📝 요약

이 논문은 함수 호출(FC)이 대형 언어 모델(LLM)과 외부 시스템 간의 상호작용을 촉진하는 강력한 기법으로 주목받고 있으며, 모델의 행동에 미치는 영향에 대한 연구가 부족하다는 점을 지적합니다. 연구진은 FC가 사용자 지시사항에 대한 LLM의 준수성을 크게 향상시킬 수 있음을 발견하고, 인과성을 활용해 FC가 LLM 내부에서 어떻게 작용하는지 조사했습니다. 층 수준과 토큰 수준에서의 인과적 개입을 통해 FC가 모델의 내부 계산 논리에 미치는 영향을 분석한 결과, FC의 상당한 영향력과 그 메커니즘에 대한 심도 있는 통찰을 얻었습니다. 또한, FC 기반 지시와 기존의 프롬프트 방법을 비교하는 실험을 통해 LLM의 안전성 및 악의적 입력 탐지 성능을 평가한 결과, FC가 평균적으로 약 135%의 성능 향상을 보이며, LLM의 신뢰성과 기능을 강화할 수 있는 잠재력을 입증했습니다.

## 🎯 주요 포인트

- 1. 함수 호출(FC)은 대형 언어 모델(LLM)이 외부 시스템과 상호작용하고 구조화된 작업을 수행하는 데 중요한 기술로 부상했습니다.
- 2. FC는 LLM이 사용자 지시를 따르는 능력을 크게 향상시킬 수 있습니다.
- 3. 인과관계를 활용하여 FC가 LLM 내부에서 어떻게 작동하는지 조사하였습니다.
- 4. FC 기반 지시와 기존 프롬프트 방법의 효과를 비교하는 실험을 통해 FC의 상당한 성능 향상을 확인했습니다.
- 5. FC는 악의적인 입력을 감지하는 데 있어 기존 방법보다 평균 135%의 성능 향상을 보여, LLM의 신뢰성과 기능을 강화할 수 있는 잠재력을 입증했습니다.


---

*Generated on 2025-09-23 23:10:35*