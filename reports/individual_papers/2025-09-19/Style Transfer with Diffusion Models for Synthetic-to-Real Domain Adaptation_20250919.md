---
keywords:
  - Diffusion Models
  - Attention Mechanism
  - Semantic Segmentation
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2505.16360
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:22:54.696584",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Attention Mechanism",
    "Semantic Segmentation"
  ],
  "rejected_keywords": [
    "Style Transfer",
    "Foundation Models"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.8,
    "Attention Mechanism": 0.78,
    "Semantic Segmentation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation

**Korean Title:** 확산 모델을 이용한 스타일 전이: 합성에서 실제 도메인 적응으로

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Models]], [[keywords/Attention Mechanism|Cross-Attention]], [[keywords/Semantic Segmentation|Semantic Segmentation]]

## 🔗 유사한 논문
- [[StyleSculptor Zero-Shot Style-Controllable 3D Asset Generation with Texture-Geometry Dual Guidance]] (83.2% similar)
- [[Masked Feature Modeling Enhances Adaptive Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (79.6% similar)
- [[Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (79.6% similar)
- [[Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models_20250919|Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models]] (79.5% similar)
- [[Moment- and Power-Spectrum-Based Gaussianity Regularization for Text-to-Image Models_20250919|Moment- and Power-Spectrum-Based Gaussianity Regularization for Text-to-Image Models]] (78.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.16360v2 Announce Type: replace-cross 
Abstract: Semantic segmentation models trained on synthetic data often perform poorly on real-world images due to domain gaps, particularly in adverse conditions where labeled data is scarce. Yet, recent foundation models enable to generate realistic images without any training. This paper proposes to leverage such diffusion models to improve the performance of vision models when learned on synthetic data. We introduce two novel techniques for semantically consistent style transfer using diffusion models: Class-wise Adaptive Instance Normalization and Cross-Attention (CACTI) and its extension with selective attention Filtering (CACTIF). CACTI applies statistical normalization selectively based on semantic classes, while CACTIF further filters cross-attention maps based on feature similarity, preventing artifacts in regions with weak cross-attention correspondences. Our methods transfer style characteristics while preserving semantic boundaries and structural coherence, unlike approaches that apply global transformations or generate content without constraints. Experiments using GTA5 as source and Cityscapes/ACDC as target domains show that our approach produces higher quality images with lower FID scores and better content preservation. Our work demonstrates that class-aware diffusion-based style transfer effectively bridges the synthetic-to-real domain gap even with minimal target domain data, advancing robust perception systems for challenging real-world applications. The source code is available at: https://github.com/echigot/cactif.

## 🔍 Abstract (한글 번역)

arXiv:2505.16360v2 발표 유형: 교차 교체  
초록: 합성 데이터로 학습된 의미론적 분할 모델은 라벨이 부족한 악조건에서 특히 도메인 차이로 인해 실제 이미지에서 성능이 저하되는 경우가 많습니다. 그러나 최근의 기초 모델은 훈련 없이도 현실적인 이미지를 생성할 수 있습니다. 본 논문은 이러한 확산 모델을 활용하여 합성 데이터로 학습된 비전 모델의 성능을 향상시키는 방법을 제안합니다. 우리는 확산 모델을 사용한 의미론적으로 일관된 스타일 전환을 위한 두 가지 새로운 기술을 소개합니다: 클래스별 적응 인스턴스 정규화 및 교차 주의 (CACTI)와 선택적 주의 필터링을 확장한 CACTIF입니다. CACTI는 의미론적 클래스에 기반하여 통계적 정규화를 선택적으로 적용하며, CACTIF는 특징 유사성을 기반으로 교차 주의 맵을 추가로 필터링하여 약한 교차 주의 대응이 있는 영역에서의 아티팩트를 방지합니다. 우리의 방법은 전역 변환을 적용하거나 제약 없이 콘텐츠를 생성하는 접근법과 달리 스타일 특성을 전환하면서 의미론적 경계와 구조적 일관성을 유지합니다. GTA5를 소스로, Cityscapes/ACDC를 타겟 도메인으로 사용한 실험에서 우리의 접근법이 더 낮은 FID 점수와 더 나은 콘텐츠 보존으로 더 높은 품질의 이미지를 생성함을 보여줍니다. 우리의 연구는 클래스 인식 확산 기반 스타일 전환이 최소한의 타겟 도메인 데이터로도 합성-실제 도메인 간의 격차를 효과적으로 메우며, 도전적인 실제 응용을 위한 강력한 인식 시스템을 발전시킴을 입증합니다. 소스 코드는 다음에서 확인할 수 있습니다: https://github.com/echigot/cactif.

## 📝 요약

이 논문은 합성 데이터로 학습된 시맨틱 세그멘테이션 모델이 실제 이미지에서 성능이 저하되는 문제를 해결하기 위해, 훈련 없이도 현실적인 이미지를 생성할 수 있는 최신 기초 모델을 활용하는 방법을 제안합니다. 저자들은 두 가지 새로운 기법인 CACTI와 CACTIF를 소개하여, 확산 모델을 사용한 의미론적 일관성 있는 스타일 전이를 구현했습니다. CACTI는 클래스별로 통계적 정규화를 적용하고, CACTIF는 선택적 주의 필터링을 통해 교차 주의 맵을 개선하여, 약한 교차 주의 대응 영역에서의 아티팩트를 방지합니다. 이 방법들은 스타일 특성을 전이하면서도 의미 경계와 구조적 일관성을 유지합니다. GTA5를 소스 도메인으로, Cityscapes/ACDC를 타겟 도메인으로 한 실험에서, 제안된 방법이 더 낮은 FID 점수와 더 나은 콘텐츠 보존을 통해 높은 품질의 이미지를 생성함을 보여주었습니다. 이 연구는 최소한의 타겟 도메인 데이터로도 합성-실제 도메인 간 격차를 효과적으로 줄일 수 있음을 입증합니다.

## 🎯 주요 포인트

- 1. 본 논문은 합성 데이터로 학습된 시맨틱 세그멘테이션 모델의 성능을 개선하기 위해 확산 모델을 활용하는 방법을 제안합니다.

- 2. CACTI와 CACTIF라는 두 가지 새로운 기법을 도입하여, 확산 모델을 통한 의미적으로 일관된 스타일 전환을 구현합니다.

- 3. CACTI는 의미적 클래스에 기반한 통계적 정규화를 선택적으로 적용하며, CACTIF는 특징 유사성에 기반하여 교차 주의 맵을 필터링합니다.

- 4. 제안된 방법은 스타일 특성을 전환하면서도 의미 경계와 구조적 일관성을 유지하여, 글로벌 변환을 적용하거나 제약 없이 콘텐츠를 생성하는 기존 접근 방식과 차별화됩니다.

- 5. 실험 결과, 제안된 방법은 GTA5를 소스로 하고 Cityscapes/ACDC를 타겟 도메인으로 할 때, 더 낮은 FID 점수와 더 나은 콘텐츠 보존으로 높은 품질의 이미지를 생성합니다.

---

*Generated on 2025-09-19 15:45:09*