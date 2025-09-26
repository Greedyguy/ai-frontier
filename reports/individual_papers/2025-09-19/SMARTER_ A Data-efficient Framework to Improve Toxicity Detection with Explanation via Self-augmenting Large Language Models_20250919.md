---
keywords:
  - Large Language Models
  - Few-Shot Learning
  - Toxicity Detection
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15174
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:26:25.139031",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Models",
    "Few-Shot Learning",
    "Toxicity Detection"
  ],
  "rejected_keywords": [
    "Explainable Content Moderation"
  ],
  "similarity_scores": {
    "Large Language Models": 0.8,
    "Few-Shot Learning": 0.78,
    "Toxicity Detection": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# SMARTER: A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models

**Korean Title:** SMARTER: 자기 증강 대형 언어 모델을 통한 설명과 함께 독성 탐지를 개선하기 위한 데이터 효율적 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Large Language Models|Large Language Models]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Toxicity Detection|Toxicity Detection]]

## 🔗 유사한 논문
- [[Forget What You Know about LLMs Evaluations -- LLMs are Like a Chameleon]] (82.8% similar)
- [[Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (82.7% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (82.4% similar)
- [[DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (82.2% similar)
- [[Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (82.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15174v1 Announce Type: cross 
Abstract: WARNING: This paper contains examples of offensive materials. Toxic content has become pervasive on social media platforms. We introduce SMARTER, a data-efficient two-stage framework for explainable content moderation using Large Language Models (LLMs). In Stage 1, we leverage LLMs' own outputs to generate synthetic explanations for both correct and incorrect labels, enabling alignment via preference optimization with minimal human supervision. In Stage 2, we refine explanation quality through cross-model training, allowing weaker models to align stylistically and semantically with stronger ones. Experiments on three benchmark tasks -- HateXplain, Latent Hate, and Implicit Hate -- demonstrate that SMARTER enables LLMs to achieve up to a 13.5% macro-F1 improvement over standard few-shot baselines while using only a fraction of the full training data. Our framework offers a scalable strategy for low-resource settings by harnessing LLMs' self-improving capabilities for both classification and explanation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15174v1 발표 유형: 교차  
초록: 경고: 이 논문은 공격적인 자료의 예시를 포함하고 있습니다. 소셜 미디어 플랫폼에서 유해한 콘텐츠가 만연해지고 있습니다. 우리는 대형 언어 모델(LLMs)을 사용하여 설명 가능한 콘텐츠 관리를 위한 데이터 효율적인 2단계 프레임워크인 SMARTER를 소개합니다. 1단계에서는 LLM의 자체 출력을 활용하여 올바른 레이블과 잘못된 레이블 모두에 대한 합성 설명을 생성하고, 최소한의 인간 감독으로 선호 최적화를 통해 정렬을 가능하게 합니다. 2단계에서는 교차 모델 훈련을 통해 설명의 품질을 개선하여 약한 모델들이 강한 모델들과 스타일 및 의미적으로 정렬될 수 있도록 합니다. HateXplain, Latent Hate, Implicit Hate라는 세 가지 벤치마크 작업에 대한 실험은 SMARTER가 전체 훈련 데이터의 일부만 사용하면서도 표준 소수 샷 기준선에 비해 최대 13.5%의 매크로-F1 향상을 LLM이 달성할 수 있음을 보여줍니다. 우리의 프레임워크는 LLM의 자체 개선 기능을 활용하여 분류와 설명 모두에 대해 저자원 환경에서 확장 가능한 전략을 제공합니다.

## 📝 요약

이 논문은 소셜 미디어의 유해 콘텐츠 문제를 해결하기 위해 SMARTER라는 데이터 효율적인 두 단계 프레임워크를 제안합니다. 첫 번째 단계에서는 대형 언어 모델(LLM)의 출력을 활용해 올바른 및 잘못된 레이블에 대한 설명을 생성하고, 최소한의 인간 감독으로 선호 최적화를 통해 정렬합니다. 두 번째 단계에서는 교차 모델 학습을 통해 설명의 질을 개선하여 약한 모델이 강한 모델과 스타일 및 의미적으로 정렬되도록 합니다. HateXplain, Latent Hate, Implicit Hate 등 세 가지 벤치마크 과제에서 실험한 결과, SMARTER는 전체 훈련 데이터의 일부만 사용하면서도 표준 몇 샷 기준보다 최대 13.5% 높은 매크로 F1 점수를 달성했습니다. 이 프레임워크는 LLM의 자기 개선 능력을 활용하여 저자원 환경에서 분류와 설명을 위한 확장 가능한 전략을 제공합니다.

## 🎯 주요 포인트

- 1. SMARTER는 대형 언어 모델(LLMs)을 활용한 설명 가능한 콘텐츠 조절을 위한 데이터 효율적인 두 단계 프레임워크입니다.

- 2. 1단계에서는 LLMs의 출력을 활용하여 올바른 및 잘못된 레이블에 대한 합성 설명을 생성하고, 최소한의 인간 감독으로 선호 최적화를 통해 정렬을 가능하게 합니다.

- 3. 2단계에서는 교차 모델 훈련을 통해 설명의 질을 향상시켜, 약한 모델이 강한 모델과 스타일 및 의미적으로 정렬되도록 합니다.

- 4. SMARTER는 HateXplain, Latent Hate, Implicit Hate 등의 세 가지 벤치마크 작업에서 표준 몇 샷 기준보다 최대 13.5%의 매크로-F1 향상을 달성하며, 전체 훈련 데이터의 일부만 사용합니다.

- 5. 이 프레임워크는 LLMs의 자기 개선 능력을 활용하여 분류 및 설명 모두에서 저자원 환경에 대한 확장 가능한 전략을 제공합니다.

---

*Generated on 2025-09-19 15:07:54*