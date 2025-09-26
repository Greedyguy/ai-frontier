<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:28:56.922711",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "ICD-10-CM Code Prediction",
    "Large Language Model",
    "Redundancy-Aware Sampling",
    "Section-Aware Fine-Tuning",
    "Embedding-Based Similarity Measures"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "ICD-10-CM Code Prediction": 0.78,
    "Large Language Model": 0.82,
    "Redundancy-Aware Sampling": 0.75,
    "Section-Aware Fine-Tuning": 0.77,
    "Embedding-Based Similarity Measures": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "ICD-10-CM code prediction",
        "canonical": "ICD-10-CM Code Prediction",
        "aliases": [
          "ICD-10-CM Prediction",
          "ICD Coding"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task central to the paper's contribution, linking to healthcare analytics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language Models"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are a core technology discussed in the paper, facilitating connections to NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.82
      },
      {
        "surface": "redundancy-aware sampling",
        "canonical": "Redundancy-Aware Sampling",
        "aliases": [
          "Redundancy Sampling"
        ],
        "category": "unique_technical",
        "rationale": "This technique is a novel approach to improve data quality, relevant to data processing.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "section-aware fine-tuning",
        "canonical": "Section-Aware Fine-Tuning",
        "aliases": [
          "Section Fine-Tuning"
        ],
        "category": "unique_technical",
        "rationale": "This method enhances model performance by leveraging document structure, linking to model optimization.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "embedding-based similarity measures",
        "canonical": "Embedding-Based Similarity Measures",
        "aliases": [
          "Embedding Similarity"
        ],
        "category": "specific_connectable",
        "rationale": "These measures are crucial for evaluating semantic similarity, connecting to machine learning techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "model selection",
      "input contextualization",
      "training data redundancy"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "ICD-10-CM code prediction",
      "resolved_canonical": "ICD-10-CM Code Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "large language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "redundancy-aware sampling",
      "resolved_canonical": "Redundancy-Aware Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "section-aware fine-tuning",
      "resolved_canonical": "Section-Aware Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "embedding-based similarity measures",
      "resolved_canonical": "Embedding-Based Similarity Measures",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# Model selection meets clinical semantics: Optimizing ICD-10-CM prediction via LLM-as-Judge evaluation, redundancy-aware sampling, and section-aware fine-tuning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18846.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18846](https://arxiv.org/abs/2509.18846)

## 🔗 유사한 논문
- [[2025-09-23/SparseDoctor_ Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models_20250923|SparseDoctor: Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models]] (86.9% similar)
- [[2025-09-22/EHR-MCP_ Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol_20250922|EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol]] (86.6% similar)
- [[2025-09-22/MedCOD_ Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework_20250922|MedCOD: Enhancing English-to-Spanish Medical Translation of Large Language Models Using Enriched Chain-of-Dictionary Framework]] (85.9% similar)
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (85.4% similar)
- [[2025-09-24/Advances in Large Language Models for Medicine_20250924|Advances in Large Language Models for Medicine]] (85.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Embedding-Based Similarity Measures|Embedding-Based Similarity Measures]]
**⚡ Unique Technical**: [[keywords/ICD-10-CM Code Prediction|ICD-10-CM Code Prediction]], [[keywords/Redundancy-Aware Sampling|Redundancy-Aware Sampling]], [[keywords/Section-Aware Fine-Tuning|Section-Aware Fine-Tuning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18846v1 Announce Type: new 
Abstract: Accurate International Classification of Diseases (ICD) coding is critical for clinical documentation, billing, and healthcare analytics, yet it remains a labour-intensive and error-prone task. Although large language models (LLMs) show promise in automating ICD coding, their challenges in base model selection, input contextualization, and training data redundancy limit their effectiveness. We propose a modular framework for ICD-10 Clinical Modification (ICD-10-CM) code prediction that addresses these challenges through principled model selection, redundancy-aware data sampling, and structured input design. The framework integrates an LLM-as-judge evaluation protocol with Plackett-Luce aggregation to assess and rank open-source LLMs based on their intrinsic comprehension of ICD-10-CM code definitions. We introduced embedding-based similarity measures, a redundancy-aware sampling strategy to remove semantically duplicated discharge summaries. We leverage structured discharge summaries from Taiwanese hospitals to evaluate contextual effects and examine section-wise content inclusion under universal and section-specific modelling paradigms. Experiments across two institutional datasets demonstrate that the selected base model after fine-tuning consistently outperforms baseline LLMs in internal and external evaluations. Incorporating more clinical sections consistently improves prediction performance. This study uses open-source LLMs to establish a practical and principled approach to ICD-10-CM code prediction. The proposed framework provides a scalable, institution-ready solution for real-world deployment of automated medical coding systems by combining informed model selection, efficient data refinement, and context-aware prompting.

## 📝 요약

이 논문은 ICD-10-CM 코드 예측을 위한 모듈형 프레임워크를 제안하여, 대형 언어 모델(LLM)의 선택, 입력 맥락화, 중복 데이터 문제를 해결합니다. LLM 평가 프로토콜과 Plackett-Luce 집계를 통해 ICD-10-CM 코드 정의에 대한 이해도를 기반으로 모델을 평가하고 순위를 매깁니다. 또한, 중복 제거를 위한 임베딩 기반 유사도 측정 및 중복 인식 샘플링 전략을 도입했습니다. 대만 병원의 구조화된 퇴원 요약을 활용해 맥락 효과를 평가하고, 다양한 모델링 패러다임 하에서 섹션별 콘텐츠 포함 여부를 조사했습니다. 두 기관의 데이터셋 실험 결과, 선택된 기본 모델이 일관되게 성능을 향상시켰으며, 임상 섹션을 추가할수록 예측 성능이 개선되었습니다. 이 연구는 오픈 소스 LLM을 활용해 ICD-10-CM 코드 예측을 위한 실용적이고 원칙적인 접근법을 제시하며, 실제 의료 코딩 시스템의 자동화를 위한 확장 가능한 솔루션을 제공합니다.

## 🎯 주요 포인트

- 1. ICD 코딩의 자동화를 위한 대형 언어 모델(LLM)의 활용 가능성을 탐구하지만, 모델 선택, 입력 맥락화, 데이터 중복성 문제로 인해 효과가 제한됨을 지적합니다.
- 2. 제안된 모듈형 프레임워크는 ICD-10-CM 코드 예측을 위해 원칙적인 모델 선택, 중복 인식 데이터 샘플링, 구조화된 입력 설계를 통해 이러한 문제를 해결합니다.
- 3. 대만 병원의 구조화된 퇴원 요약을 활용하여 맥락 효과를 평가하고, 보편적 및 섹션별 모델링 패러다임 하에서 섹션별 콘텐츠 포함을 검토합니다.
- 4. 두 개의 기관 데이터셋을 통한 실험에서, 선택된 기본 모델이 미세 조정 후 내부 및 외부 평가에서 일관되게 기본 LLM보다 우수한 성능을 보였습니다.
- 5. 제안된 프레임워크는 정보에 입각한 모델 선택, 효율적인 데이터 정제, 맥락 인식 프롬프트를 결합하여 자동화된 의료 코딩 시스템의 실제 배포를 위한 확장 가능하고 기관 준비된 솔루션을 제공합니다.


---

*Generated on 2025-09-24 13:28:56*