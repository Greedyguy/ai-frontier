---
keywords:
  - Large Language Models
  - Language-Specific Steering Vectors
  - Language Confusion
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14814
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:27:24.502025",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Language-Specific Steering Vectors",
    "Language Confusion"
  ],
  "rejected_keywords": [
    "Natural Language Processing"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Language-Specific Steering Vectors": 0.75,
    "Language Confusion": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# ReCoVeR the Target Language: Language Steering without Sacrificing Task Performance

**Korean Title:** 대상 언어 회복: 과제 성능을 희생하지 않는 언어 조정

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Language-Specific Steering Vectors|language-specific steering vectors]], [[keywords/Language Confusion|language confusion]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.0% similar)
- [[Forget What You Know about LLMs Evaluations -- LLMs are Like a Chameleon]] (83.3% similar)
- [[DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (83.2% similar)
- [[Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (82.4% similar)
- [[Understanding and Mitigating Overrefusal in LLMs from an Unveiling Perspective of Safety Decision Boundary]] (82.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14814v1 Announce Type: new 
Abstract: As they become increasingly multilingual, Large Language Models (LLMs) exhibit more language confusion, i.e., they tend to generate answers in a language different from the language of the prompt or the answer language explicitly requested by the user. In this work, we propose ReCoVeR (REducing language COnfusion in VEctor Representations), a novel lightweight approach for reducing language confusion based on language-specific steering vectors. We first isolate language vectors with the help of multi-parallel corpus and then effectively leverage those vectors for effective LLM steering via fixed (i.e., unsupervised) as well as trainable steering functions. Our extensive evaluation, encompassing three benchmarks and 18 languages, shows that ReCoVeR effectively mitigates language confusion in both monolingual and cross-lingual setups while at the same time -- and in contrast to prior language steering methods -- retaining task performance. Our data code is available at https://github.com/hSterz/recover.

## 🔍 Abstract (한글 번역)

arXiv:2509.14814v1 발표 유형: 신규  
초록: 대형 언어 모델(LLMs)이 점점 더 다국어화됨에 따라 언어 혼동이 증가하고 있습니다. 즉, LLM은 프롬프트의 언어 또는 사용자가 명시적으로 요청한 답변 언어와 다른 언어로 답변을 생성하는 경향이 있습니다. 본 연구에서는 언어별 조정 벡터에 기반한 언어 혼동 감소를 위한 새로운 경량 접근법인 ReCoVeR(REducing language COnfusion in VEctor Representations)을 제안합니다. 먼저 다중 병렬 코퍼스를 활용하여 언어 벡터를 분리한 후, 고정(즉, 비지도 학습) 및 학습 가능한 조정 함수를 통해 효과적으로 LLM을 조정하기 위해 이러한 벡터를 활용합니다. 세 가지 벤치마크와 18개 언어를 포함하는 광범위한 평가를 통해 ReCoVeR가 단일 언어 및 교차 언어 설정 모두에서 언어 혼동을 효과적으로 완화하면서도 -- 이전의 언어 조정 방법과는 대조적으로 -- 작업 성능을 유지한다는 것을 보여줍니다. 우리의 데이터 코드는 https://github.com/hSterz/recover에서 이용할 수 있습니다.

## 📝 요약

이 논문은 다국어 환경에서 대형 언어 모델(LLM)이 언어 혼동을 일으키는 문제를 해결하기 위해 ReCoVeR라는 새로운 접근법을 제안합니다. ReCoVeR는 언어별 조정 벡터를 활용하여 언어 혼동을 줄이는 경량 방법론입니다. 다중 병렬 코퍼스를 통해 언어 벡터를 분리하고, 이를 고정 및 학습 가능한 조정 함수로 LLM을 효과적으로 조정합니다. 세 가지 벤치마크와 18개 언어를 포함한 평가 결과, ReCoVeR는 단일 언어 및 교차 언어 설정에서 언어 혼동을 효과적으로 완화하면서도 작업 성능을 유지하는 것으로 나타났습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 다국어 환경에서 언어 혼동을 일으키는 경향이 있다.

- 2. ReCoVeR는 언어별 조정 벡터를 활용하여 언어 혼동을 줄이는 경량 접근법이다.

- 3. ReCoVeR는 고정 및 학습 가능한 조정 기능을 통해 LLM을 효과적으로 조정한다.

- 4. 세 가지 벤치마크와 18개 언어에 대한 평가에서 ReCoVeR는 언어 혼동을 효과적으로 완화하면서도 작업 성능을 유지한다.

- 5. ReCoVeR의 데이터 코드는 https://github.com/hSterz/recover에서 제공된다.

---

*Generated on 2025-09-19 15:52:12*