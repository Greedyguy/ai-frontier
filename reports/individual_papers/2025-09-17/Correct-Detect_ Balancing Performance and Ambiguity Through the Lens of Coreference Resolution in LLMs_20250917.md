---
keywords:
  - Large Language Models
  - Coreference Resolution
  - Natural Language Processing
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:58:09.495164",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Coreference Resolution",
    "Natural Language Processing"
  ],
  "rejected_keywords": [
    "Semantic Ambiguity"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Coreference Resolution": 0.78,
    "Natural Language Processing": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Correct-Detect: Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs

**Korean Title:** Correct-Detect: 대규모 언어 모델(LLM)에서의 상호 참조 해결을 통한 성능과 모호성의 균형 조정

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Natural Language Processing|Natural Language Processing]]
**⚡ Unique Technical**: [[keywords/Coreference Resolution|Coreference Resolution]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (85.1% similar)
- [[Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (82.8% similar)
- [[Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox A practical guide to getting the most out of human ratings]] (82.8% similar)
- [[Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (82.4% similar)
- [[Large Language Model probabilities cannot distinguish between possible and impossible language_20250919|Large Language Model probabilities cannot distinguish between possible and impossible language]] (82.4% similar)

## 📋 저자 정보

**Authors:** Amber Shore, Russell Scheinberg, Ameeta Agrawal, So Young Lee

## 📄 Abstract (원문)

Large Language Models (LLMs) are intended to reflect human linguistic
competencies. But humans have access to a broad and embodied context, which is
key in detecting and resolving linguistic ambiguities, even in isolated text
spans. A foundational case of semantic ambiguity is found in the task of
coreference resolution: how is a pronoun related to an earlier person mention?
This capability is implicit in nearly every downstream task, and the presence
of ambiguity at this level can alter performance significantly. We show that
LLMs can achieve good performance with minimal prompting in both coreference
disambiguation and the detection of ambiguity in coreference, however, they
cannot do both at the same time. We present the CORRECT-DETECT trade-off:
though models have both capabilities and deploy them implicitly, successful
performance balancing these two abilities remains elusive.

## 🔍 Abstract (한글 번역)

대형 언어 모델(LLM)은 인간의 언어 능력을 반영하도록 설계되었습니다. 그러나 인간은 넓고 구체화된 맥락에 접근할 수 있으며, 이는 고립된 텍스트 범위에서도 언어적 모호성을 감지하고 해결하는 데 핵심적입니다. 의미적 모호성의 근본적인 사례는 대명사 해소 작업에서 발견됩니다: 대명사가 이전에 언급된 사람과 어떻게 관련되는가? 이 능력은 거의 모든 하위 작업에 암묵적으로 포함되어 있으며, 이 수준에서의 모호성은 성능에 상당한 영향을 미칠 수 있습니다. 우리는 LLM이 대명사 모호성 해소와 대명사 모호성 감지 모두에서 최소한의 프롬프트로 우수한 성능을 달성할 수 있음을 보여주지만, 두 작업을 동시에 수행할 수는 없음을 보여줍니다. 우리는 CORRECT-DETECT 상충 관계를 제시합니다: 모델이 두 가지 능력을 모두 가지고 이를 암묵적으로 사용하지만, 이 두 능력을 균형 있게 성공적으로 수행하는 것은 여전히 어려운 과제입니다.

## 📝 요약

대형 언어 모델(LLM)은 인간의 언어 능력을 반영하려 하지만, 인간은 언어적 모호성을 해결하는 데 중요한 광범위하고 구체적인 맥락에 접근할 수 있습니다. 이러한 모호성의 대표적인 사례는 대명사와 이전 인물 언급 간의 관계를 파악하는 '공지 해결' 작업에서 나타납니다. 연구 결과, LLM은 최소한의 프롬프트로 공지 모호성 해소와 모호성 탐지에서 좋은 성능을 보이지만, 두 작업을 동시에 수행하는 데는 한계가 있음을 밝혔습니다. 이를 'CORRECT-DETECT' 트레이드오프로 정의하며, 두 능력을 균형 있게 발휘하는 것은 여전히 어려운 과제임을 제시합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 인간의 언어 능력을 반영하도록 설계되었지만, 인간은 넓고 체화된 맥락에 접근할 수 있어 언어적 모호성을 감지하고 해결하는 데 유리하다.

- 2. 의미적 모호성의 기본 사례는 대명사와 이전 인물 언급 간의 관계를 파악하는 '공지 해결' 작업에서 발견된다.

- 3. 공지 해결의 모호성은 거의 모든 하위 작업에 암묵적으로 포함되어 있으며, 이 수준에서의 모호성은 성능에 큰 영향을 미칠 수 있다.

- 4. LLMs는 최소한의 프롬프트로 공지 모호성 해소와 모호성 감지에서 좋은 성능을 발휘할 수 있지만, 두 작업을 동시에 수행할 수는 없다.

- 5. CORRECT-DETECT 상충 관계를 제시하며, 두 능력을 균형 있게 발휘하는 성공적인 성능은 여전히 어려운 과제로 남아 있다.

---

*Generated on 2025-09-20 05:56:00*