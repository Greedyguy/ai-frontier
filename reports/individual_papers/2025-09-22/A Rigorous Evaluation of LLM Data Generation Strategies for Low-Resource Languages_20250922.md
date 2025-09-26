---
keywords:
  - Large Language Model
  - Low-Resource Languages
  - Synthetic Data Generation
  - Prompting Strategies
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2506.12158
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:48:51.861220",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Low-Resource Languages",
    "Synthetic Data Generation",
    "Prompting Strategies"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Low-Resource Languages": 0.7,
    "Synthetic Data Generation": 0.8,
    "Prompting Strategies": 0.78
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
        "rationale": "Central to the paper's focus on data generation strategies, linking to broader discussions on LLMs.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "low-resource languages",
        "canonical": "Low-Resource Languages",
        "aliases": [
          "low-resource language",
          "under-resourced languages"
        ],
        "category": "unique_technical",
        "rationale": "Key focus of the study, enabling connections to research on language diversity and resource scarcity.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "synthetic data generation",
        "canonical": "Synthetic Data Generation",
        "aliases": [
          "data synthesis",
          "synthetic data"
        ],
        "category": "specific_connectable",
        "rationale": "Crucial for understanding the paper's methodology and its implications for model training.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "prompting strategies",
        "canonical": "Prompting Strategies",
        "aliases": [
          "prompt engineering",
          "prompt techniques"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights a methodological aspect that can link to broader discussions on model prompting.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
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
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "low-resource languages",
      "resolved_canonical": "Low-Resource Languages",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "synthetic data generation",
      "resolved_canonical": "Synthetic Data Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "prompting strategies",
      "resolved_canonical": "Prompting Strategies",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages

**Korean Title:** 저자원이 부족한 언어를 위한 LLM 데이터 생성 전략에 대한 엄밀한 평가

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.12158.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2506.12158](https://arxiv.org/abs/2506.12158)

## 🔗 유사한 논문
- [[2025-09-22/How do Language Models Generate Slang_ A Systematic Comparison between Human and Machine-Generated Slang Usages_20250922|How do Language Models Generate Slang: A Systematic Comparison between Human and Machine-Generated Slang Usages]] (88.3% similar)
- [[2025-09-22/MUG-Eval_ A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language_20250922|MUG-Eval: A Proxy Evaluation Framework for Multilingual Generation Capabilities in Any Language]] (87.9% similar)
- [[2025-09-22/Benchmark of stylistic variation in LLM-generated texts_20250922|Benchmark of stylistic variation in LLM-generated texts]] (87.7% similar)
- [[2025-09-22/SyGra_ A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data_20250922|SyGra: A Unified Graph-Based Framework for Scalable Generation, Quality Tagging, and Management of Synthetic Data]] (86.8% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (86.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Synthetic Data Generation|Synthetic Data Generation]], [[keywords/Prompting Strategies|Prompting Strategies]]
**⚡ Unique Technical**: [[keywords/Low-Resource Languages|Low-Resource Languages]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.12158v3 Announce Type: replace 
Abstract: Large Language Models (LLMs) are increasingly used to generate synthetic textual data for training smaller specialized models. However, a comparison of various generation strategies for low-resource language settings is lacking. While various prompting strategies have been proposed, such as demonstrations, label-based summaries, and self-revision, their comparative effectiveness remains unclear, especially for low-resource languages. In this paper, we systematically evaluate the performance of these generation strategies and their combinations across 11 typologically diverse languages, including several extremely low-resource ones. Using three NLP tasks and four open-source LLMs, we assess downstream model performance on generated versus gold-standard data. Our results show that strategic combinations of generation methods, particularly target-language demonstrations with LLM-based revisions, yield strong performance, narrowing the gap with real data to as little as 5% in some settings. We also find that smart prompting techniques can reduce the advantage of larger LLMs, highlighting efficient generation strategies for synthetic data generation in low-resource scenarios with smaller models.

## 🔍 Abstract (한글 번역)

arXiv:2506.12158v3 발표 유형: 교체  
초록: 대형 언어 모델(LLMs)은 점점 더 작은 특화 모델을 훈련하기 위한 합성 텍스트 데이터를 생성하는 데 사용되고 있습니다. 그러나 저자원 언어 환경에 대한 다양한 생성 전략의 비교는 부족합니다. 시연, 레이블 기반 요약, 자기 수정과 같은 다양한 프롬프트 전략이 제안되었지만, 특히 저자원 언어에 대한 비교적 효과는 명확하지 않습니다. 본 논문에서는 11개의 유형학적으로 다양한 언어, 특히 몇몇 극히 저자원 언어를 포함하여 이러한 생성 전략과 그 조합의 성능을 체계적으로 평가합니다. 세 가지 NLP 과제와 네 가지 오픈 소스 LLM을 사용하여 생성된 데이터와 골드 스탠다드 데이터에 대한 다운스트림 모델 성능을 평가합니다. 우리의 결과는 생성 방법의 전략적 조합, 특히 LLM 기반 수정과 함께 목표 언어 시연이 강력한 성능을 발휘하며, 일부 환경에서는 실제 데이터와의 격차를 5%까지 줄일 수 있음을 보여줍니다. 또한 스마트 프롬프트 기술이 더 큰 LLM의 장점을 줄일 수 있음을 발견하여, 저자원 시나리오에서 작은 모델로 합성 데이터 생성을 위한 효율적인 생성 전략을 강조합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)을 활용하여 저자원 언어 환경에서의 텍스트 데이터를 생성하는 다양한 전략을 비교 평가합니다. 11개의 다양한 언어를 대상으로, 시연, 레이블 기반 요약, 자기 수정 등의 프롬프트 전략을 체계적으로 분석했습니다. 세 가지 NLP 작업과 네 개의 오픈소스 LLM을 사용하여 생성된 데이터와 실제 데이터의 성능을 비교한 결과, 목표 언어 시연과 LLM 기반 수정의 조합이 실제 데이터와의 성능 격차를 최대 5%까지 줄일 수 있음을 발견했습니다. 또한, 스마트 프롬프트 기술이 대형 LLM의 우위를 줄일 수 있음을 보여주어, 저자원 시나리오에서 효율적인 데이터 생성 전략을 제시합니다.

## 🎯 주요 포인트

- 1. 다양한 생성 전략의 비교 연구가 부족한 저자원 언어 환경에서 대형 언어 모델(LLMs)의 성능을 체계적으로 평가했습니다.
- 2. 11개의 다양한 언어에서 목표 언어 시연과 LLM 기반 수정의 전략적 조합이 실제 데이터와의 성능 차이를 5%까지 줄일 수 있음을 발견했습니다.
- 3. 스마트 프롬프트 기법이 더 큰 LLM의 장점을 줄일 수 있음을 보여주며, 저자원 시나리오에서 작은 모델을 위한 효율적인 합성 데이터 생성 전략을 강조합니다.
- 4. 세 가지 NLP 과제와 네 개의 오픈 소스 LLM을 사용하여 생성된 데이터와 골드 스탠다드 데이터 간의 다운스트림 모델 성능을 평가했습니다.


---

*Generated on 2025-09-23 11:48:51*