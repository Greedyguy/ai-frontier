---
keywords:
  - Transformer Architecture
  - Encoder-based Classifiers
  - Decoder-based Models
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:42:01.146084",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer Architecture",
    "Encoder-based Classifiers",
    "Decoder-based Models"
  ],
  "rejected_keywords": [
    "Social Bot Detection",
    "Large Language Models"
  ],
  "similarity_scores": {
    "Transformer Architecture": 0.8,
    "Encoder-based Classifiers": 0.78,
    "Decoder-based Models": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# A Comparative Analysis of Transformer Models in Social Bot Detection

**Korean Title:** 소셜 봇 탐지에서의 트랜스포머 모델 비교 분석

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]     [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Transformer Architecture|Transformer Models]]
**⚡ Unique Technical**: [[keywords/Encoder-based Classifiers|Encoder-based Classifiers]], [[keywords/Decoder-based Models|Decoder-based Models]]

## 🔗 유사한 논문
- [[SMARTER_ A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models_20250919|SMARTER A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (78.4% similar)
- [[An Attention-Based Denoising Framework for Personality Detection in Social Media Texts_20250918|An Attention-Based Denoising Framework for Personality Detection in Social Media Texts]] (78.3% similar)
- [[Is GPT-4o mini Blinded by its Own Safety Filters Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection_20250918|Is GPT-4o mini Blinded by its Own Safety Filters Exposing the Multimodal-to-Unimodal Bottleneck in Hate Speech Detection]] (78.1% similar)
- [[DetectAnyLLM_ Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models_20250919|DetectAnyLLM Towards Generalizable and Robust Detection of Machine-Generated Text Across Domains and Models]] (77.9% similar)
- [[Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (77.3% similar)

## 📋 저자 정보

**Authors:** Rohan Veit, Michael Lones

## 📄 Abstract (원문)

Social media has become a key medium of communication in today's society.
This realisation has led to many parties employing artificial users (or bots)
to mislead others into believing untruths or acting in a beneficial manner to
such parties. Sophisticated text generation tools, such as large language
models, have further exacerbated this issue. This paper aims to compare the
effectiveness of bot detection models based on encoder and decoder
transformers. Pipelines are developed to evaluate the performance of these
classifiers, revealing that encoder-based classifiers demonstrate greater
accuracy and robustness. However, decoder-based models showed greater
adaptability through task-specific alignment, suggesting more potential for
generalisation across different use cases in addition to superior observa.
These findings contribute to the ongoing effort to prevent digital environments
being manipulated while protecting the integrity of online discussion.

## 🔍 Abstract (한글 번역)

소셜 미디어는 오늘날 사회에서 중요한 의사소통 수단이 되었습니다. 이러한 인식은 많은 당사자들이 인공 사용자(또는 봇)를 활용하여 다른 사람들을 오도하고 거짓을 믿게 하거나 해당 당사자들에게 유리한 방식으로 행동하도록 유도하게 만들었습니다. 대형 언어 모델과 같은 정교한 텍스트 생성 도구는 이 문제를 더욱 악화시켰습니다. 본 논문은 인코더와 디코더 변환기에 기반한 봇 탐지 모델의 효과를 비교하는 것을 목표로 합니다. 이러한 분류기의 성능을 평가하기 위한 파이프라인이 개발되었으며, 인코더 기반 분류기가 더 높은 정확성과 견고성을 보여준다는 것을 밝혀냈습니다. 그러나 디코더 기반 모델은 과제별 정렬을 통해 더 큰 적응성을 보여주었으며, 이는 다양한 사용 사례에 걸쳐 일반화할 수 있는 더 많은 잠재력을 시사합니다. 이러한 발견은 디지털 환경이 조작되는 것을 방지하고 온라인 토론의 무결성을 보호하기 위한 지속적인 노력에 기여합니다.

## 📝 요약

이 논문은 소셜 미디어에서 봇을 탐지하기 위한 모델의 효과를 비교합니다. 인코더와 디코더 기반의 트랜스포머 모델을 평가한 결과, 인코더 기반 분류기가 더 높은 정확성과 견고성을 보였습니다. 반면, 디코더 기반 모델은 특정 작업에 맞춘 적응력이 뛰어나 다양한 사용 사례에 대한 일반화 가능성을 보여주었습니다. 이러한 발견은 디지털 환경의 조작을 방지하고 온라인 토론의 무결성을 보호하는 데 기여합니다.

## 🎯 주요 포인트

- 1. 소셜 미디어에서 인공지능 사용자(봇)를 통한 오정보 확산 문제가 심각해지고 있다.

- 2. 대형 언어 모델과 같은 정교한 텍스트 생성 도구가 이러한 문제를 더욱 악화시키고 있다.

- 3. 본 논문은 인코더 및 디코더 트랜스포머 기반 봇 탐지 모델의 효과를 비교한다.

- 4. 인코더 기반 분류기가 더 높은 정확성과 강건성을 보이는 것으로 나타났다.

- 5. 디코더 기반 모델은 과제별 정렬을 통해 더 큰 적응성을 보여 다양한 사용 사례에서의 일반화 가능성을 시사한다.

---

*Generated on 2025-09-20 02:42:18*