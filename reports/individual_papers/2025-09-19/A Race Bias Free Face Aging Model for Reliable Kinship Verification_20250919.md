---
keywords:
  - Bias Mitigation in Computer Vision
  - Generative Models
  - Kinship Verification
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15177
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:59:28.343554",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Bias Mitigation in Computer Vision",
    "Generative Models",
    "Kinship Verification"
  ],
  "rejected_keywords": [
    "RA-GAN"
  ],
  "similarity_scores": {
    "Bias Mitigation in Computer Vision": 0.8,
    "Generative Models": 0.78,
    "Kinship Verification": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# A Race Bias Free Face Aging Model for Reliable Kinship Verification

**Korean Title:** 인종 편향이 없는 신뢰할 수 있는 친족 관계 검증을 위한 얼굴 노화 모델

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Generative Models|face aging GAN model]]
**⚡ Unique Technical**: [[keywords/Kinship Verification|kinship verification]]
**🚀 Evolved Concepts**: [[keywords/Bias Mitigation in Computer Vision|racially unbiased images]]

## 🔗 유사한 논문
- [[Controllable Localized Face Anonymization Via Diffusion Inpainting_20250919|Controllable Localized Face Anonymization Via Diffusion Inpainting]] (79.9% similar)
- [[DiffGAN A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis]] (77.0% similar)
- [[Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (76.5% similar)
- [[Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows_20250918|Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows]] (76.2% similar)
- [[Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (76.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15177v1 Announce Type: new 
Abstract: The age gap in kinship verification addresses the time difference between the photos of the parent and the child. Moreover, their same-age photos are often unavailable, and face aging models are racially biased, which impacts the likeness of photos. Therefore, we propose a face aging GAN model, RA-GAN, consisting of two new modules, RACEpSp and a feature mixer, to produce racially unbiased images. The unbiased synthesized photos are used in kinship verification to investigate the results of verifying same-age parent-child images. The experiments demonstrate that our RA-GAN outperforms SAM-GAN on an average of 13.14\% across all age groups, and CUSP-GAN in the 60+ age group by 9.1\% in terms of racial accuracy. Moreover, RA-GAN can preserve subjects' identities better than SAM-GAN and CUSP-GAN across all age groups. Additionally, we demonstrate that transforming parent and child images from the KinFaceW-I and KinFaceW-II datasets to the same age can enhance the verification accuracy across all age groups. The accuracy increases with our RA-GAN for the kinship relationships of father-son and father-daughter, mother-son, and mother-daughter, which are 5.22, 5.12, 1.63, and 0.41, respectively, on KinFaceW-I. Additionally, the accuracy for the relationships of father-daughter, father-son, and mother-son is 2.9, 0.39, and 1.6 on KinFaceW-II, respectively. The code is available at~\href{https://github.com/bardiya2254kariminia/An-Age-Transformation-whitout-racial-bias-for-Kinship-verification}{Github}

## 🔍 Abstract (한글 번역)

arXiv:2509.15177v1 발표 유형: 신규  
초록: 친족 관계 확인에서의 연령 차이는 부모와 자녀의 사진 간의 시간 차이를 다룹니다. 게다가, 동일 연령대의 사진이 종종 없으며, 얼굴 노화 모델은 인종적 편향을 가지기 때문에 사진의 유사성에 영향을 미칩니다. 따라서 우리는 인종적으로 편향되지 않은 이미지를 생성하기 위해 RACEpSp와 특징 믹서라는 두 개의 새로운 모듈로 구성된 얼굴 노화 GAN 모델, RA-GAN을 제안합니다. 편향되지 않은 합성 사진은 동일 연령대의 부모-자녀 이미지 확인 결과를 조사하기 위해 친족 관계 확인에 사용됩니다. 실험 결과, RA-GAN은 모든 연령대에서 SAM-GAN보다 평균 13.14\% 더 우수하며, 60세 이상 연령대에서 CUSP-GAN보다 인종 정확도 측면에서 9.1\% 더 우수함을 보여줍니다. 또한, RA-GAN은 모든 연령대에서 SAM-GAN 및 CUSP-GAN보다 피험자의 정체성을 더 잘 보존할 수 있습니다. 추가적으로, KinFaceW-I 및 KinFaceW-II 데이터셋에서 부모와 자녀의 이미지를 동일 연령대로 변환하면 모든 연령대에서 확인 정확도를 향상시킬 수 있음을 보여줍니다. KinFaceW-I에서 아버지-아들 및 아버지-딸, 어머니-아들 및 어머니-딸의 친족 관계에 대한 정확도는 각각 5.22, 5.12, 1.63, 0.41 증가합니다. 또한, KinFaceW-II에서 아버지-딸, 아버지-아들 및 어머니-아들의 관계에 대한 정확도는 각각 2.9, 0.39, 1.6 증가합니다. 코드는 [Github](https://github.com/bardiya2254kariminia/An-Age-Transformation-whitout-racial-bias-for-Kinship-verification)에서 확인할 수 있습니다.

## 📝 요약

이 논문은 부모와 자녀의 사진 간 나이 차이를 고려한 친족 관계 확인 문제를 다룹니다. 기존 얼굴 노화 모델의 인종적 편향 문제를 해결하기 위해 RA-GAN이라는 새로운 얼굴 노화 GAN 모델을 제안합니다. RA-GAN은 RACEpSp와 특징 믹서 모듈을 포함하여 인종적 편향이 없는 이미지를 생성합니다. 실험 결과, RA-GAN은 SAM-GAN과 CUSP-GAN보다 모든 연령대에서 더 높은 정확도를 보였으며, 특히 60세 이상 그룹에서 인종적 정확도가 각각 13.14%와 9.1% 향상되었습니다. 또한, KinFaceW-I 및 KinFaceW-II 데이터셋의 부모-자녀 이미지를 동일 연령대로 변환하면 확인 정확도가 향상됨을 보여주었습니다. RA-GAN은 부모-자녀 관계의 확인 정확도를 증가시키며, 코드도 공개되어 있습니다.

## 🎯 주요 포인트

- 1. RA-GAN은 인종적 편향이 없는 이미지를 생성하기 위해 RACEpSp와 feature mixer라는 두 가지 새로운 모듈을 포함한 얼굴 노화 GAN 모델입니다.

- 2. RA-GAN은 모든 연령대에서 SAM-GAN보다 평균 13.14% 더 우수한 성능을 보였으며, 60세 이상 연령대에서는 CUSP-GAN보다 인종 정확도에서 9.1% 더 높은 성능을 보였습니다.

- 3. RA-GAN은 KinFaceW-I 및 KinFaceW-II 데이터셋의 부모-자녀 이미지를 동일 연령대로 변환하여 모든 연령대에서 검증 정확도를 향상시킬 수 있습니다.

- 4. KinFaceW-I 데이터셋에서 RA-GAN은 아버지-아들, 아버지-딸, 어머니-아들, 어머니-딸 관계의 정확도를 각각 5.22, 5.12, 1.63, 0.41만큼 증가시켰습니다.

- 5. RA-GAN의 코드는 GitHub에서 사용할 수 있습니다.

---

*Generated on 2025-09-19 16:09:59*