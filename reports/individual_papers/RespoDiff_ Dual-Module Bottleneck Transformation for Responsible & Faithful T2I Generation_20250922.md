# RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation

**Korean Title:** 책임 있고 충실한 텍스트-투-이미지(T2I) 생성을 위한 이중 모듈 병목 변환: RespoDiff

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Responsible Generation

## 🔗 유사한 논문
- [[2025-09-18/Iterative Prompt Refinement for Safer Text-to-Image Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (85.2% similar)
- [[2025-09-19/TIDE_ Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement_20250919|TIDE Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement]] (84.2% similar)
- [[2025-09-22/Dynamic Classifier-Free Diffusion Guidance via Online Feedback_20250922|Dynamic Classifier-Free Diffusion Guidance via Online Feedback]] (83.2% similar)
- [[2025-09-18/BiasMap_ Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation_20250918|BiasMap Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation]] (82.6% similar)
- [[2025-09-22/Diffusion-Based Cross-Modal Feature Extraction for Multi-Label Classification_20250922|Diffusion-Based Cross-Modal Feature Extraction for Multi-Label Classification]] (82.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15257v1 Announce Type: cross 
Abstract: The rapid advancement of diffusion models has enabled high-fidelity and semantically rich text-to-image generation; however, ensuring fairness and safety remains an open challenge. Existing methods typically improve fairness and safety at the expense of semantic fidelity and image quality. In this work, we propose RespoDiff, a novel framework for responsible text-to-image generation that incorporates a dual-module transformation on the intermediate bottleneck representations of diffusion models. Our approach introduces two distinct learnable modules: one focused on capturing and enforcing responsible concepts, such as fairness and safety, and the other dedicated to maintaining semantic alignment with neutral prompts. To facilitate the dual learning process, we introduce a novel score-matching objective that enables effective coordination between the modules. Our method outperforms state-of-the-art methods in responsible generation by ensuring semantic alignment while optimizing both objectives without compromising image fidelity. Our approach improves responsible and semantically coherent generation by 20% across diverse, unseen prompts. Moreover, it integrates seamlessly into large-scale models like SDXL, enhancing fairness and safety. Code will be released upon acceptance.

## 🔍 Abstract (한글 번역)

arXiv:2509.15257v1 발표 유형: 교차  
초록: 확산 모델의 급속한 발전은 고품질의 의미적으로 풍부한 텍스트-이미지 생성이 가능하게 했으나, 공정성과 안전성을 보장하는 것은 여전히 해결되지 않은 과제입니다. 기존 방법들은 일반적으로 의미적 충실도와 이미지 품질을 희생하여 공정성과 안전성을 개선합니다. 본 연구에서는 확산 모델의 중간 병목 표현에 이중 모듈 변환을 통합한 책임 있는 텍스트-이미지 생성을 위한 새로운 프레임워크인 RespoDiff를 제안합니다. 우리의 접근 방식은 공정성과 안전성 같은 책임 있는 개념을 포착하고 강화하는 데 중점을 둔 모듈과 중립적인 프롬프트와의 의미적 정렬을 유지하는 데 전념하는 두 가지 학습 가능한 모듈을 도입합니다. 이중 학습 과정을 촉진하기 위해, 모듈 간의 효과적인 조정을 가능하게 하는 새로운 점수 매칭 목표를 소개합니다. 우리의 방법은 이미지 충실도를 손상시키지 않으면서 두 목표를 최적화하여 의미적 정렬을 보장함으로써 책임 있는 생성에서 최첨단 방법들을 능가합니다. 우리의 접근 방식은 다양한 보지 못한 프롬프트에서 책임 있고 의미적으로 일관된 생성을 20% 개선합니다. 또한, SDXL과 같은 대규모 모델에 원활하게 통합되어 공정성과 안전성을 향상시킵니다. 코드는 승인 후 공개될 예정입니다.

## 📝 요약

이 논문에서는 텍스트-이미지 생성에서 공정성과 안전성을 보장하면서도 이미지 품질과 의미적 충실성을 유지하는 새로운 프레임워크인 RespoDiff를 제안합니다. RespoDiff는 확산 모델의 중간 표현에 이중 모듈 변환을 적용하여 공정성과 안전성을 강화하는 모듈과 중립적인 프롬프트와의 의미적 정렬을 유지하는 모듈을 포함합니다. 이중 학습을 위해 새로운 스코어 매칭 목표를 도입하여 모듈 간 효과적인 조율을 가능하게 합니다. 이 방법은 이미지 충실도를 손상시키지 않으면서 의미적 정렬과 책임 있는 생성을 최적화하여 기존 방법보다 20% 향상된 성과를 보입니다. 또한, 대규모 모델에 통합되어 공정성과 안전성을 강화합니다. 코드 공개는 논문 수락 후 예정입니다.

## 🎯 주요 포인트

- 1. RespoDiff는 확산 모델의 중간 병목 표현에 이중 모듈 변환을 도입하여 책임 있는 텍스트-이미지 생성을 가능하게 합니다.

- 2. 하나의 모듈은 공정성과 안전성 같은 책임 있는 개념을 포착하고 강화하는 데 중점을 두고, 다른 모듈은 중립적인 프롬프트와의 의미적 정렬을 유지하는 데 전념합니다.

- 3. 새로운 스코어 매칭 목표를 도입하여 두 모듈 간의 효과적인 조정을 가능하게 합니다.

- 4. 제안된 방법은 의미적 정렬을 보장하면서 이미지 충실도를 손상시키지 않고 두 가지 목표를 최적화하여 책임 있는 생성에서 최첨단 방법을 능가합니다.

- 5. 다양한 미지의 프롬프트에 대해 책임 있고 의미적으로 일관된 생성을 20% 개선하며, 대규모 모델에 원활하게 통합됩니다.

---

*Generated on 2025-09-22 15:36:07*