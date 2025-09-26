---
keywords:
  - Diffusion Models
  - Generative Models
  - Historical Artworks
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14755
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:50:06.803861",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Generative Models",
    "Historical Artworks"
  ],
  "rejected_keywords": [
    "Smell-Related Objects"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.8,
    "Generative Models": 0.78,
    "Historical Artworks": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Data Augmentation via Latent Diffusion Models for Detecting Smell-Related Objects in Historical Artworks

**Korean Title:** 잠재 확산 모델을 통한 데이터 증강: 역사적 예술 작품에서 냄새 관련 객체 탐지를 위한 연구

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|latent diffusion models]], [[keywords/Generative Models|synthetic data generation]]
**⚡ Unique Technical**: [[keywords/Historical Artworks|historical artworks]]

## 🔗 유사한 논문
- [[Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows_20250918|Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows]] (79.2% similar)
- [[SpecDiff Accelerating Diffusion Model Inference with Self-Speculation]] (78.6% similar)
- [[Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (78.3% similar)
- [[DiffHash Text-Guided Targeted Attack via Diffusion Models against Deep Hashing Image Retrieval]] (78.0% similar)
- [[Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance_20250919|Mitigating data replication in text-to-audio generative diffusion models through anti-memorization guidance]] (78.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14755v1 Announce Type: new 
Abstract: Finding smell references in historic artworks is a challenging problem. Beyond artwork-specific challenges such as stylistic variations, their recognition demands exceptionally detailed annotation classes, resulting in annotation sparsity and extreme class imbalance. In this work, we explore the potential of synthetic data generation to alleviate these issues and enable accurate detection of smell-related objects. We evaluate several diffusion-based augmentation strategies and demonstrate that incorporating synthetic data into model training can improve detection performance. Our findings suggest that leveraging the large-scale pretraining of diffusion models offers a promising approach for improving detection accuracy, particularly in niche applications where annotations are scarce and costly to obtain. Furthermore, the proposed approach proves to be effective even with relatively small amounts of data, and scaling it up provides high potential for further enhancements.

## 🔍 Abstract (한글 번역)

arXiv:2509.14755v1 발표 유형: 신규  
초록: 역사적 예술 작품에서 냄새와 관련된 참조를 찾는 것은 도전적인 문제입니다. 스타일적 변동과 같은 작품 특유의 도전 과제 외에도, 이러한 참조를 인식하기 위해서는 매우 세밀한 주석 클래스가 필요하며, 이는 주석의 희소성과 극단적인 클래스 불균형을 초래합니다. 이 연구에서는 이러한 문제를 완화하고 냄새와 관련된 객체의 정확한 탐지를 가능하게 하기 위해 합성 데이터 생성의 잠재력을 탐구합니다. 우리는 여러 확산 기반 증강 전략을 평가하고, 합성 데이터를 모델 훈련에 통합하면 탐지 성능을 향상시킬 수 있음을 입증합니다. 우리의 연구 결과는 확산 모델의 대규모 사전 훈련을 활용하는 것이 주석이 드물고 획득 비용이 높은 틈새 응용 분야에서 탐지 정확도를 향상시키는 유망한 접근법을 제공한다는 것을 시사합니다. 또한, 제안된 접근법은 비교적 적은 양의 데이터로도 효과적이며, 이를 확장하면 추가적인 향상의 높은 잠재력을 제공합니다.

## 📝 요약

이 논문은 역사적 예술 작품에서 냄새와 관련된 요소를 식별하는 문제를 다룹니다. 작품의 스타일 다양성과 세부적인 주석 클래스 필요로 인해 주석이 드문드문하고 클래스 불균형이 심각한 문제를 해결하기 위해, 합성 데이터 생성의 가능성을 탐구합니다. 여러 확산 기반 증강 전략을 평가한 결과, 합성 데이터를 모델 훈련에 포함하면 탐지 성능이 향상됨을 보여줍니다. 특히 주석이 드물고 비용이 많이 드는 특수한 응용 분야에서 대규모 사전 학습된 확산 모델을 활용하는 것이 탐지 정확도를 높이는 유망한 접근법임을 시사합니다. 제안된 방법은 적은 양의 데이터로도 효과적이며, 데이터 규모를 확장하면 추가적인 개선 가능성이 큽니다.

## 🎯 주요 포인트

- 1. 역사적 예술 작품에서 냄새와 관련된 요소를 찾는 것은 스타일 변이와 같은 작품 특유의 문제로 인해 도전적인 과제입니다.

- 2. 합성 데이터 생성이 이러한 문제를 완화하고 냄새 관련 객체의 정확한 탐지를 가능하게 할 수 있음을 탐구했습니다.

- 3. 합성 데이터를 모델 훈련에 통합하면 탐지 성능이 향상될 수 있음을 보여주었습니다.

- 4. 대규모 사전 학습된 확산 모델을 활용하는 것이 주석이 드문 틈새 응용 분야에서 탐지 정확도를 개선하는 유망한 접근 방식임을 시사합니다.

- 5. 제안된 접근 방식은 비교적 적은 양의 데이터로도 효과적이며, 규모를 확장하면 추가적인 개선 가능성이 높습니다.

---

*Generated on 2025-09-19 16:06:24*