---
keywords:
  - Large Language Model
  - SeCodePLT
  - CWE-based Risk Categories
  - Vulnerability Detection
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2410.11096
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:47:15.784358",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "SeCodePLT",
    "CWE-based Risk Categories",
    "Vulnerability Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "SeCodePLT": 0.8,
    "CWE-based Risk Categories": 0.78,
    "Vulnerability Detection": 0.77
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
          "Code LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on evaluating security capabilities of code-generating models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "SeCodePLT",
        "canonical": "SeCodePLT",
        "aliases": [
          "Security Code Platform"
        ],
        "category": "unique_technical",
        "rationale": "Represents the specific dataset introduced in the paper, crucial for linking to related security evaluation frameworks.",
        "novelty_score": 0.9,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "CWE-based risk categories",
        "canonical": "CWE-based Risk Categories",
        "aliases": [
          "Common Weakness Enumeration"
        ],
        "category": "specific_connectable",
        "rationale": "Provides a structured way to link security risks with standardized categories.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "vulnerability detection",
        "canonical": "Vulnerability Detection",
        "aliases": [
          "Vulnerability Identification"
        ],
        "category": "specific_connectable",
        "rationale": "Key aspect of the paper's evaluation focus, linking to broader security assessment topics.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "evaluation",
      "framework"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "SeCodePLT",
      "resolved_canonical": "SeCodePLT",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "CWE-based risk categories",
      "resolved_canonical": "CWE-based Risk Categories",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "vulnerability detection",
      "resolved_canonical": "Vulnerability Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# SeCodePLT: A Unified Platform for Evaluating the Security of Code GenAI

**Korean Title:** SeCodePLT: 코드 생성 인공지능의 보안을 평가하기 위한 통합 플랫폼

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2410.11096.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2410.11096](https://arxiv.org/abs/2410.11096)

## 🔗 유사한 논문
- [[2025-09-19/A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks_20250919|A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks]] (83.0% similar)
- [[2025-09-19/Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization_20250919|Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization]] (82.3% similar)
- [[2025-09-22/MUG-Eval_ A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language_20250922|MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language]] (81.4% similar)
- [[2025-09-22/Adaptive Self-improvement LLM Agentic System for ML Library Development_20250922|Adaptive Self-improvement LLM Agentic System for ML Library Development]] (81.3% similar)
- [[2025-09-18/Evaluating and Improving the Robustness of Security Attack Detectors Generated by LLMs_20250918|Evaluating and Improving the Robustness of Security Attack Detectors Generated by LLMs]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/CWE-based Risk Categories|CWE-based Risk Categories]], [[keywords/Vulnerability Detection|Vulnerability Detection]]
**⚡ Unique Technical**: [[keywords/SeCodePLT|SeCodePLT]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2410.11096v2 Announce Type: replace-cross 
Abstract: Existing benchmarks for evaluating the security risks and capabilities (e.g., vulnerability detection) of code-generating large language models (LLMs) face several key limitations: (1) limited coverage of risk and capabilities; (2) reliance on static evaluation metrics such as LLM judgments or rule-based detection, which lack the precision of dynamic analysis; and (3) a trade-off between data quality and benchmark scale. To address these challenges, we introduce a general and scalable benchmark construction framework that begins with manually validated, high-quality seed examples and expands them via targeted mutations. Our approach provides a comprehensive suite of artifacts so the benchmark can support comprehensive risk assessment and security capability evaluation using dynamic metrics. By combining expert insights with automated generation, we strike a balance between manual effort, data quality, and benchmark scale. Applying this framework to Python, C/C++, and Java, we build SeCodePLT, a dataset of more than 5.9k samples spanning 44 CWE-based risk categories and three security capabilities. Compared with state-of-the-art benchmarks, SeCodePLT offers broader coverage, higher data fidelity, and substantially greater scale. We use SeCodePLT to evaluate leading code LLMs and agents, revealing their strengths and weaknesses in both generating secure code and identifying or fixing vulnerabilities.

## 🔍 Abstract (한글 번역)

arXiv:2410.11096v2 발표 유형: 교차 교체

초록: 코드 생성 대형 언어 모델(LLM)의 보안 위험 및 기능(예: 취약점 탐지)을 평가하기 위한 기존 벤치마크는 몇 가지 주요 제한 사항에 직면해 있습니다: (1) 위험 및 기능의 제한된 범위; (2) LLM 판단이나 규칙 기반 탐지와 같은 정적 평가 지표에 의존하여 동적 분석의 정밀도가 부족함; (3) 데이터 품질과 벤치마크 규모 간의 균형 문제. 이러한 문제를 해결하기 위해, 우리는 수동으로 검증된 고품질 시드 예제를 시작으로 하여 목표 지향적 변이를 통해 확장하는 일반적이고 확장 가능한 벤치마크 구축 프레임워크를 소개합니다. 우리의 접근 방식은 벤치마크가 동적 지표를 사용한 포괄적인 위험 평가 및 보안 기능 평가를 지원할 수 있도록 포괄적인 아티팩트 모음을 제공합니다. 전문가의 통찰력과 자동 생성의 결합을 통해 수작업, 데이터 품질, 벤치마크 규모 간의 균형을 맞춥니다. 이 프레임워크를 Python, C/C++, Java에 적용하여 44개의 CWE 기반 위험 범주와 3개의 보안 기능을 아우르는 5.9k개 이상의 샘플로 구성된 SeCodePLT라는 데이터셋을 구축합니다. 최첨단 벤치마크와 비교했을 때, SeCodePLT는 더 넓은 범위, 더 높은 데이터 충실도, 그리고 상당히 더 큰 규모를 제공합니다. 우리는 SeCodePLT를 사용하여 선도적인 코드 LLM 및 에이전트를 평가하여 안전한 코드 생성 및 취약점 식별 또는 수정에서의 강점과 약점을 드러냅니다.

## 📝 요약

기존의 코드 생성 대형 언어 모델(LLM)의 보안 위험 및 기능 평가 벤치마크는 제한된 범위, 정적 평가 지표 의존, 데이터 품질과 규모 간의 균형 문제를 가지고 있습니다. 이를 해결하기 위해, 우리는 수작업으로 검증된 고품질 예제를 시작으로, 목표 지향적 변이를 통해 확장하는 일반적이고 확장 가능한 벤치마크 구축 프레임워크를 제안합니다. 이 접근법은 동적 지표를 사용하여 포괄적인 위험 평가와 보안 기능 평가를 지원하는 아티팩트를 제공합니다. Python, C/C++, Java에 적용하여 SeCodePLT라는 데이터셋을 구축했으며, 이는 44개의 CWE 기반 위험 카테고리와 3가지 보안 기능을 포함하는 5,900개 이상의 샘플로 구성됩니다. SeCodePLT는 기존 벤치마크보다 더 넓은 범위, 높은 데이터 정확성, 더 큰 규모를 제공합니다. 이를 통해 주요 코드 LLM과 에이전트를 평가하여 보안 코드 생성 및 취약점 식별 또는 수정에서의 강점과 약점을 밝혀냈습니다.

## 🎯 주요 포인트

- 1. 기존 코드 생성 대형 언어 모델의 보안 위험 및 기능 평가 벤치마크는 위험 및 기능의 제한된 범위를 다루고 있습니다.
- 2. 기존 벤치마크는 정적 평가 지표에 의존하여 동적 분석의 정밀성이 부족합니다.
- 3. 제안된 프레임워크는 수동으로 검증된 고품질 시드 예제를 기반으로 하여 목표 지향적 변이를 통해 확장됩니다.
- 4. SeCodePLT는 44개의 CWE 기반 위험 범주와 세 가지 보안 기능을 아우르는 5.9k 이상의 샘플을 포함하는 데이터셋입니다.
- 5. SeCodePLT는 기존 벤치마크보다 더 넓은 범위, 높은 데이터 충실도, 그리고 더 큰 규모를 제공합니다.


---

*Generated on 2025-09-23 09:47:15*