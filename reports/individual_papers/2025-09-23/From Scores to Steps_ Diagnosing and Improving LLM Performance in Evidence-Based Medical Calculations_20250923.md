---
keywords:
  - Large Language Model
  - Retrieval Augmented Generation
  - MedRaC
  - Error Analysis Framework
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16584
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:26:24.890925",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Retrieval Augmented Generation",
    "MedRaC",
    "Error Analysis Framework"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Retrieval Augmented Generation": 0.82,
    "MedRaC": 0.7,
    "Error Analysis Framework": 0.65
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
        "rationale": "As a foundational technology, it connects to various subfields and applications in NLP and AI.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Retrieval-Augmented Generation",
        "canonical": "Retrieval Augmented Generation",
        "aliases": [
          "RAG"
        ],
        "category": "specific_connectable",
        "rationale": "It represents a trending method that enhances LLM capabilities, relevant for linking to recent advancements.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "MedRaC",
        "canonical": "MedRaC",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A unique framework introduced in the paper, pivotal for understanding the proposed methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Error Analysis Framework",
        "canonical": "Error Analysis Framework",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel approach for diagnosing LLM performance, crucial for linking to evaluation methodologies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "clinical decision-making",
      "final answer",
      "human evaluation"
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
      "candidate_surface": "Retrieval-Augmented Generation",
      "resolved_canonical": "Retrieval Augmented Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "MedRaC",
      "resolved_canonical": "MedRaC",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Error Analysis Framework",
      "resolved_canonical": "Error Analysis Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16584.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16584](https://arxiv.org/abs/2509.16584)

## 🔗 유사한 논문
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL: Toward Expert-Level Medical Text Validation with Language Models]] (87.6% similar)
- [[2025-09-22/EHR-MCP_ Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol_20250922|EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol]] (86.9% similar)
- [[2025-09-22/MEDAL_ A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators_20250922|MEDAL: A Framework for Benchmarking LLMs as Multilingual Open-Domain Dialogue Evaluators]] (86.8% similar)
- [[2025-09-23/EngiBench_ A Benchmark for Evaluating Large Language Models on Engineering Problem Solving_20250923|EngiBench: A Benchmark for Evaluating Large Language Models on Engineering Problem Solving]] (86.3% similar)
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (85.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Retrieval Augmented Generation|Retrieval Augmented Generation]]
**⚡ Unique Technical**: [[keywords/MedRaC|MedRaC]], [[keywords/Error Analysis Framework|Error Analysis Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16584v1 Announce Type: cross 
Abstract: Large language models (LLMs) have demonstrated promising performance on medical benchmarks; however, their ability to perform medical calculations, a crucial aspect of clinical decision-making, remains underexplored and poorly evaluated. Existing benchmarks often assess only the final answer with a wide numerical tolerance, overlooking systematic reasoning failures and potentially causing serious clinical misjudgments. In this work, we revisit medical calculation evaluation with a stronger focus on clinical trustworthiness. First, we clean and restructure the MedCalc-Bench dataset and propose a new step-by-step evaluation pipeline that independently assesses formula selection, entity extraction, and arithmetic computation. Under this granular framework, the accuracy of GPT-4o drops from 62.7% to 43.6%, revealing errors masked by prior evaluations. Second, we introduce an automatic error analysis framework that generates structured attribution for each failure mode. Human evaluation confirms its alignment with expert judgment, enabling scalable and explainable diagnostics. Finally, we propose a modular agentic pipeline, MedRaC, that combines retrieval-augmented generation and Python-based code execution. Without any fine-tuning, MedRaC improves the accuracy of different LLMs from 16.35% up to 53.19%. Our work highlights the limitations of current benchmark practices and proposes a more clinically faithful methodology. By enabling transparent and transferable reasoning evaluation, we move closer to making LLM-based systems trustworthy for real-world medical applications.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 의료 계산 능력을 평가하는 새로운 방법론을 제안합니다. 기존 벤치마크는 최종 답변만 평가하여 체계적인 추론 오류를 간과할 수 있습니다. 이를 개선하기 위해 MedCalc-Bench 데이터셋을 정리하고, 공식 선택, 엔티티 추출, 산술 계산을 독립적으로 평가하는 단계별 평가 파이프라인을 도입했습니다. 이로 인해 GPT-4o의 정확도가 62.7%에서 43.6%로 감소함을 발견했습니다. 또한, 자동 오류 분석 프레임워크를 도입하여 오류 모드에 대한 구조적 귀속을 생성하고, 인간 평가를 통해 전문가 판단과의 일치를 확인했습니다. 마지막으로, MedRaC라는 모듈형 에이전트 파이프라인을 제안하여 LLM의 정확성을 크게 향상시켰습니다. 이 연구는 현재 벤치마크의 한계를 강조하고, 임상적으로 신뢰할 수 있는 평가 방법론을 제시합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)의 의료 계산 수행 능력은 충분히 탐구되지 않았으며, 기존 벤치마크는 체계적인 추론 실패를 간과할 수 있다.
- 2. MedCalc-Bench 데이터셋을 정리하고 재구성하여 공식 선택, 엔티티 추출, 산술 계산을 독립적으로 평가하는 새로운 단계별 평가 파이프라인을 제안한다.
- 3. 새로운 평가 프레임워크 하에서 GPT-4o의 정확도가 62.7%에서 43.6%로 감소하여 이전 평가에서 가려졌던 오류를 드러낸다.
- 4. 실패 모드에 대한 구조화된 귀속을 생성하는 자동 오류 분석 프레임워크를 도입하여 전문가 판단과의 정렬을 확인한다.
- 5. MedRaC라는 모듈형 에이전트 파이프라인을 제안하여, 다양한 LLM의 정확도를 16.35%에서 최대 53.19%까지 향상시킨다.


---

*Generated on 2025-09-23 23:26:24*