---
keywords:
  - Large Language Models
  - Dynamic Self-reinforcing Calibration for Hallucination Suppression
  - Factual Alignment Proxy
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:58:01.265519",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Dynamic Self-reinforcing Calibration for Hallucination Suppression",
    "Factual Alignment Proxy"
  ],
  "rejected_keywords": [
    "Hallucination Detection Proxy",
    "TruthfulQA"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Dynamic Self-reinforcing Calibration for Hallucination Suppression": 0.75,
    "Factual Alignment Proxy": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models

**Korean Title:** DSCC-HS: 대형 언어 모델에서 환각 억제를 위한 동적 자기 강화 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]    [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Dynamic Self-reinforcing Calibration for Hallucination Suppression|Dynamic Self-reinforcing Calibration for Hallucination Suppression]], [[keywords/Factual Alignment Proxy|Factual Alignment Proxy]]

## 🔗 유사한 논문
- [[Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.2% similar)
- [[Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (84.2% similar)
- [[DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (84.1% similar)
- [[Causal-Counterfactual RAG_ The Integration of Causal-Counterfactual Reasoning into RAG_20250919|Causal-Counterfactual RAG The Integration of Causal-Counterfactual Reasoning into RAG]] (83.7% similar)
- [[Correct-Detect_ Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs_20250917|Correct-Detect Balancing Performance and Ambiguity Through the Lens of Coreference Resolution in LLMs]] (82.7% similar)

## 📋 저자 정보

**Authors:** Xiao Zheng

## 📄 Abstract (원문)

Large Language Model (LLM) hallucination is a significant barrier to their
reliable deployment. Current methods like Retrieval-Augmented Generation (RAG)
are often reactive. We introduce **Dynamic Self-reinforcing Calibration for
Hallucination Suppression (DSCC-HS)**, a novel, proactive framework that
intervenes during autoregressive decoding. Inspired by dual-process cognitive
theory, DSCC-HS uses a compact proxy model, trained in adversarial roles as a
Factual Alignment Proxy (FAP) and a Hallucination Detection Proxy (HDP). During
inference, these proxies dynamically steer a large target model by injecting a
real-time steering vector, which is the difference between FAP and HDP logits,
at each decoding step. This plug-and-play approach requires no modification to
the target model. Our experiments on TruthfulQA and BioGEN show DSCC-HS
achieves state-of-the-art performance. On TruthfulQA, it reached a 99.2%
Factual Consistency Rate (FCR). On the long-form BioGEN benchmark, it attained
the highest FActScore of 46.50. These results validate DSCC-HS as a principled
and efficient solution for enhancing LLM factuality.

## 🔍 Abstract (한글 번역)

대형 언어 모델(LLM)의 환각은 신뢰할 수 있는 배포에 있어 중요한 장애물입니다. 현재의 방법들, 예를 들어 검색 보강 생성(RAG) 등은 종종 반응적입니다. 우리는 **환각 억제를 위한 동적 자기 강화 보정(DSCC-HS)**이라는 새로운 선제적 프레임워크를 소개합니다. 이는 자가회귀 디코딩 중에 개입합니다. 이중 처리 인지 이론에 영감을 받아, DSCC-HS는 사실 정렬 프록시(FAP)와 환각 탐지 프록시(HDP)로서 적대적 역할로 훈련된 간결한 프록시 모델을 사용합니다. 추론 중에, 이러한 프록시는 각 디코딩 단계에서 FAP와 HDP 로짓 간의 차이를 실시간 조정 벡터로 주입하여 대형 대상 모델을 동적으로 조정합니다. 이 플러그 앤 플레이 접근 방식은 대상 모델의 수정이 필요하지 않습니다. TruthfulQA와 BioGEN에 대한 우리의 실험에서 DSCC-HS는 최첨단 성능을 달성했습니다. TruthfulQA에서는 99.2%의 사실 일관성 비율(FCR)을 기록했습니다. 장문형 BioGEN 벤치마크에서는 46.50의 최고 FActScore를 달성했습니다. 이러한 결과는 DSCC-HS가 LLM의 사실성을 향상시키기 위한 원칙적이고 효율적인 솔루션임을 입증합니다.

## 📝 요약

대형 언어 모델(LLM)의 환각 문제는 신뢰성 있는 활용을 저해하는 주요 요인입니다. 기존 방법인 Retrieval-Augmented Generation(RAG)은 주로 반응적입니다. 우리는 **환각 억제를 위한 동적 자기 강화 보정(DSCC-HS)**이라는 새로운 프레임워크를 소개합니다. 이는 자가회귀 디코딩 중에 개입하는 방식으로, 이중 처리 인지 이론에서 영감을 받아 개발되었습니다. DSCC-HS는 사실 정렬 프록시(FAP)와 환각 탐지 프록시(HDP)로 훈련된 간결한 프록시 모델을 사용하여, 디코딩 단계마다 실시간 조정 벡터를 주입해 대형 모델을 동적으로 조정합니다. 이 방법은 대상 모델의 수정 없이 적용 가능합니다. TruthfulQA와 BioGEN 실험에서 DSCC-HS는 최첨단 성능을 보였으며, TruthfulQA에서는 99.2%의 사실 일관성 비율(FCR)을, BioGEN에서는 46.50의 최고 FActScore를 기록했습니다. 이는 DSCC-HS가 LLM의 사실성을 향상시키는 효과적인 솔루션임을 입증합니다.

## 🎯 주요 포인트

- 1. DSCC-HS는 자가 회귀 디코딩 중에 개입하여 환각을 억제하는 새로운 능동적 프레임워크입니다.

- 2. DSCC-HS는 사실 정렬 프록시(FAP)와 환각 탐지 프록시(HDP)로 훈련된 컴팩트한 프록시 모델을 사용합니다.

- 3. 이 접근 방식은 타겟 모델의 수정 없이 실시간 조정 벡터를 주입하여 모델을 동적으로 조정합니다.

- 4. TruthfulQA에서 DSCC-HS는 99.2%의 사실 일관성 비율(FCR)을 달성했습니다.

- 5. BioGEN 벤치마크에서 DSCC-HS는 46.50의 최고 FActScore를 기록했습니다.

---

*Generated on 2025-09-20 09:39:36*