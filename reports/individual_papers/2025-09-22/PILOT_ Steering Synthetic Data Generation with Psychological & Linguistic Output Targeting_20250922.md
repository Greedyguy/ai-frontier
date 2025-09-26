---
keywords:
  - Large Language Model
  - Psycholinguistic Profiles
  - Schema-Based Steering
  - Hybrid Persona-Schema Steering
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15447
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:58:42.625089",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Psycholinguistic Profiles",
    "Schema-Based Steering",
    "Hybrid Persona-Schema Steering"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Psycholinguistic Profiles": 0.8,
    "Schema-Based Steering": 0.78,
    "Hybrid Persona-Schema Steering": 0.77
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
        "rationale": "Large Language Models are central to the study and are a key component in the framework being evaluated.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Psycholinguistic Profiles",
        "canonical": "Psycholinguistic Profiles",
        "aliases": [
          "Psycholinguistic Profile"
        ],
        "category": "unique_technical",
        "rationale": "This term is central to the PILOT framework and represents a novel approach to steering synthetic data generation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Schema-Based Steering",
        "canonical": "Schema-Based Steering",
        "aliases": [
          "SBS"
        ],
        "category": "unique_technical",
        "rationale": "Schema-Based Steering is a novel method evaluated in the paper for improving output coherence and reducing repetition.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Hybrid Persona-Schema Steering",
        "canonical": "Hybrid Persona-Schema Steering",
        "aliases": [
          "HPS"
        ],
        "category": "unique_technical",
        "rationale": "This approach combines elements of both schema-based and natural-language steering, offering a balanced method.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Natural-language Persona Steering",
      "Mistral Large 2",
      "Deepseek-R1",
      "LLaMA 3.3 70B"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Psycholinguistic Profiles",
      "resolved_canonical": "Psycholinguistic Profiles",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Schema-Based Steering",
      "resolved_canonical": "Schema-Based Steering",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Hybrid Persona-Schema Steering",
      "resolved_canonical": "Hybrid Persona-Schema Steering",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# PILOT: Steering Synthetic Data Generation with Psychological & Linguistic Output Targeting

**Korean Title:** 파일럿: 심리적 및 언어적 출력 타겟팅을 통한 합성 데이터 생성 조정

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15447.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15447](https://arxiv.org/abs/2509.15447)

## 🔗 유사한 논문
- [[2025-09-22/P2VA_ Converting Persona Descriptions into Voice Attributes for Fair and Controllable Text-to-Speech_20250922|P2VA: Converting Persona Descriptions into Voice Attributes for Fair and Controllable Text-to-Speech]] (86.3% similar)
- [[2025-09-22/Measuring Lexical Diversity of Synthetic Data Generated through Fine-Grained Persona Prompting_20250922|Measuring Lexical Diversity of Synthetic Data Generated through Fine-Grained Persona Prompting]] (84.0% similar)
- [[2025-09-22/Beyond Linear Steering_ Unified Multi-Attribute Control for Language Models_20250922|Beyond Linear Steering: Unified Multi-Attribute Control for Language Models]] (82.5% similar)
- [[2025-09-22/Creative Preference Optimization_20250922|Creative Preference Optimization]] (81.8% similar)
- [[2025-09-22/On Optimal Steering to Achieve Exact Fairness_20250922|On Optimal Steering to Achieve Exact Fairness]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Psycholinguistic Profiles|Psycholinguistic Profiles]], [[keywords/Schema-Based Steering|Schema-Based Steering]], [[keywords/Hybrid Persona-Schema Steering|Hybrid Persona-Schema Steering]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15447v1 Announce Type: cross 
Abstract: Generative AI applications commonly leverage user personas as a steering mechanism for synthetic data generation, but reliance on natural language representations forces models to make unintended inferences about which attributes to emphasize, limiting precise control over outputs. We introduce PILOT (Psychological and Linguistic Output Targeting), a two-phase framework for steering large language models with structured psycholinguistic profiles. In Phase 1, PILOT translates natural language persona descriptions into multidimensional profiles with normalized scores across linguistic and psychological dimensions. In Phase 2, these profiles guide generation along measurable axes of variation. We evaluate PILOT across three state-of-the-art LLMs (Mistral Large 2, Deepseek-R1, LLaMA 3.3 70B) using 25 synthetic personas under three conditions: Natural-language Persona Steering (NPS), Schema-Based Steering (SBS), and Hybrid Persona-Schema Steering (HPS). Results demonstrate that schema-based approaches significantly reduce artificial-sounding persona repetition while improving output coherence, with silhouette scores increasing from 0.098 to 0.237 and topic purity from 0.773 to 0.957. Our analysis reveals a fundamental trade-off: SBS produces more concise outputs with higher topical consistency, while NPS offers greater lexical diversity but reduced predictability. HPS achieves a balance between these extremes, maintaining output variety while preserving structural consistency. Expert linguistic evaluation confirms that PILOT maintains high response quality across all conditions, with no statistically significant differences between steering approaches.

## 🔍 Abstract (한글 번역)

arXiv:2509.15447v1 발표 유형: 교차  
초록: 생성적 인공지능 애플리케이션은 일반적으로 사용자 페르소나를 합성 데이터 생성의 조정 메커니즘으로 활용하지만, 자연어 표현에 의존함으로써 모델이 강조할 속성에 대해 의도치 않은 추론을 하게 되어 출력에 대한 정확한 제어가 제한됩니다. 우리는 구조화된 심리언어학적 프로파일을 통해 대형 언어 모델을 조정하는 두 단계의 프레임워크인 PILOT(Psychological and Linguistic Output Targeting)을 소개합니다. 1단계에서 PILOT은 자연어 페르소나 설명을 언어적 및 심리적 차원 전반에 걸쳐 정규화된 점수를 가진 다차원 프로파일로 변환합니다. 2단계에서는 이러한 프로파일이 측정 가능한 변이 축을 따라 생성을 안내합니다. 우리는 3가지 최첨단 대형 언어 모델(Mistral Large 2, Deepseek-R1, LLaMA 3.3 70B)을 사용하여 25개의 합성 페르소나를 세 가지 조건 하에 평가합니다: 자연어 페르소나 조정(NPS), 스키마 기반 조정(SBS), 하이브리드 페르소나-스키마 조정(HPS). 결과는 스키마 기반 접근 방식이 인위적으로 들리는 페르소나 반복을 크게 줄이면서 출력의 일관성을 향상시킨다는 것을 보여주며, 실루엣 점수는 0.098에서 0.237로, 주제 순도는 0.773에서 0.957로 증가했습니다. 우리의 분석은 근본적인 상충 관계를 드러냅니다: SBS는 주제 일관성이 높은 더 간결한 출력을 생성하는 반면, NPS는 더 큰 어휘 다양성을 제공하지만 예측 가능성은 감소합니다. HPS는 이러한 극단 사이의 균형을 이루어 구조적 일관성을 유지하면서 출력의 다양성을 유지합니다. 전문가 언어 평가에 따르면 PILOT은 모든 조건에서 높은 응답 품질을 유지하며, 조정 접근 방식 간에 통계적으로 유의미한 차이는 없습니다.

## 📝 요약

이 논문은 사용자 페르소나를 활용한 생성 AI의 데이터 생성 과정에서 발생하는 문제를 해결하기 위해 PILOT(Psychological and Linguistic Output Targeting)이라는 새로운 프레임워크를 제안합니다. PILOT는 두 단계로 구성되어 있으며, 첫 번째 단계에서는 자연어로 된 페르소나 설명을 심리언어학적 프로파일로 변환합니다. 두 번째 단계에서는 이 프로파일을 활용하여 생성 결과를 조정합니다. 세 가지 조건(Natural-language Persona Steering, Schema-Based Steering, Hybrid Persona-Schema Steering)에서 세 가지 최신 대형 언어 모델을 평가한 결과, 스키마 기반 접근법이 인위적인 반복을 줄이고 출력의 일관성을 높이는 데 효과적임을 발견했습니다. 특히, 스키마 기반 접근법은 주제 일관성을 높이고, 하이브리드 접근법은 다양성과 구조적 일관성을 균형 있게 유지합니다. 전문가 평가 결과, 모든 조건에서 높은 응답 품질을 유지했습니다.

## 🎯 주요 포인트

- 1. PILOT는 심리언어학적 프로파일을 활용하여 대형 언어 모델의 출력을 조정하는 두 단계의 프레임워크입니다.
- 2. Phase 1에서는 자연어로 된 페르소나 설명을 다차원 프로파일로 변환하여 언어적 및 심리적 차원에서 정규화된 점수를 부여합니다.
- 3. Phase 2에서는 이러한 프로파일이 측정 가능한 변동 축을 따라 데이터 생성을 안내합니다.
- 4. 연구 결과, 스키마 기반 접근 방식이 인위적인 페르소나 반복을 줄이고 출력의 일관성을 향상시키는 것으로 나타났습니다.
- 5. 하이브리드 페르소나-스키마 조정(HPS)은 출력의 다양성을 유지하면서 구조적 일관성을 보존하여 균형을 이룹니다.


---

*Generated on 2025-09-23 08:58:42*