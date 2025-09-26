---
keywords:
  - Diffusion Models
  - Face Anonymization
  - Attribute-Guidance Module
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14866
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:51:21.544370",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Face Anonymization",
    "Attribute-Guidance Module"
  ],
  "rejected_keywords": [
    "Computer Vision"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.82,
    "Face Anonymization": 0.78,
    "Attribute-Guidance Module": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Controllable Localized Face Anonymization Via Diffusion Inpainting

**Korean Title:** 확산 인페인팅을 통한 제어 가능한 국소화 얼굴 익명화

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Diffusion Models|Diffusion Inpainting]]
**⚡ Unique Technical**: [[keywords/Face Anonymization|Face Anonymization]], [[keywords/Attribute-Guidance Module|Attribute-Guidance Module]]

## 🔗 유사한 논문
- [[Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (81.2% similar)
- [[FMGS-Avatar Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (80.3% similar)
- [[DACoN DINO for Anime Paint Bucket Colorization with Any Number of Reference Images]] (80.0% similar)
- [[Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models_20250919|Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models]] (80.0% similar)
- [[Roll Your Eyes Gaze Redirection via Explicit 3D Eyeball Rotation]] (79.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14866v1 Announce Type: new 
Abstract: The growing use of portrait images in computer vision highlights the need to protect personal identities. At the same time, anonymized images must remain useful for downstream computer vision tasks. In this work, we propose a unified framework that leverages the inpainting ability of latent diffusion models to generate realistic anonymized images. Unlike prior approaches, we have complete control over the anonymization process by designing an adaptive attribute-guidance module that applies gradient correction during the reverse denoising process, aligning the facial attributes of the generated image with those of the synthesized target image. Our framework also supports localized anonymization, allowing users to specify which facial regions are left unchanged. Extensive experiments conducted on the public CelebA-HQ and FFHQ datasets show that our method outperforms state-of-the-art approaches while requiring no additional model training. The source code is available on our page.

## 🔍 Abstract (한글 번역)

arXiv:2509.14866v1 발표 유형: 신규  
초록: 컴퓨터 비전에서 초상화 이미지의 사용이 증가함에 따라 개인 신원을 보호할 필요성이 강조되고 있습니다. 동시에 익명화된 이미지가 후속 컴퓨터 비전 작업에 유용하게 남아 있어야 합니다. 본 연구에서는 잠재 확산 모델의 인페인팅 능력을 활용하여 현실적인 익명화 이미지를 생성하는 통합 프레임워크를 제안합니다. 이전 접근 방식과 달리, 우리는 역 잡음 제거 과정에서 그라디언트 보정을 적용하여 생성된 이미지의 얼굴 속성을 합성된 대상 이미지의 속성과 일치시키는 적응형 속성 안내 모듈을 설계함으로써 익명화 과정에 대한 완전한 제어를 제공합니다. 또한, 우리 프레임워크는 국소화된 익명화를 지원하여 사용자가 변경하지 않을 얼굴 영역을 지정할 수 있도록 합니다. 공개된 CelebA-HQ 및 FFHQ 데이터셋에서 수행된 광범위한 실험은 추가적인 모델 훈련 없이도 우리의 방법이 최첨단 접근 방식을 능가함을 보여줍니다. 소스 코드는 우리의 페이지에서 이용 가능합니다.

## 📝 요약

이 논문은 컴퓨터 비전에서 초상화 이미지의 개인 식별 보호 필요성을 다루며, 익명화된 이미지가 여전히 유용해야 함을 강조합니다. 저자들은 잠재 확산 모델의 인페인팅 능력을 활용하여 현실적인 익명화 이미지를 생성하는 통합 프레임워크를 제안합니다. 적응형 속성 안내 모듈을 설계하여 역잡음 제거 과정에서 생성된 이미지의 얼굴 속성을 목표 이미지와 일치시키며 익명화 과정을 완전히 제어합니다. 또한, 사용자가 특정 얼굴 부위를 변경하지 않도록 지정할 수 있는 지역화된 익명화를 지원합니다. CelebA-HQ 및 FFHQ 데이터셋에서의 실험 결과, 추가 모델 훈련 없이도 최첨단 방법보다 우수한 성능을 보였습니다. 소스 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 본 연구는 잠재 확산 모델의 인페인팅 능력을 활용하여 현실적인 익명화 이미지를 생성하는 통합 프레임워크를 제안합니다.

- 2. 적응형 속성 안내 모듈을 설계하여 역 디노이징 과정에서 그래디언트 보정을 적용함으로써 생성된 이미지의 얼굴 속성을 목표 이미지와 일치시킵니다.

- 3. 사용자가 특정 얼굴 부위를 변경하지 않고 남겨둘 수 있는 국소화된 익명화를 지원합니다.

- 4. CelebA-HQ 및 FFHQ 데이터셋에서의 실험 결과, 추가 모델 훈련 없이도 최첨단 접근 방식을 능가하는 성능을 보였습니다.

- 5. 소스 코드는 연구 페이지에서 제공됩니다.

---

*Generated on 2025-09-19 16:07:09*