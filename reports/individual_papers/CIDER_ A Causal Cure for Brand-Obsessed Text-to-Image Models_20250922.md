# CIDER: A Causal Cure for Brand-Obsessed Text-to-Image Models

**Korean Title:** CIDER: 브랜드 집착 텍스트-이미지 모델에 대한 인과적 해결책

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Brand Neutrality Score

## 🔗 유사한 논문
- [[2025-09-18/Iterative Prompt Refinement for Safer Text-to-Image Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (83.7% similar)
- [[2025-09-18/BiasMap_ Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation_20250918|BiasMap Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation]] (83.2% similar)
- [[2025-09-19/TIDE_ Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement_20250919|TIDE Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement]] (81.2% similar)
- [[2025-09-22/PRISM_ Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images_20250922|PRISM Phase-enhanced Radial-based Image Signature Mapping framework for fingerprinting AI-generated images]] (80.6% similar)
- [[2025-09-19/Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (79.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15803v1 Announce Type: cross 
Abstract: Text-to-image (T2I) models exhibit a significant yet under-explored "brand bias", a tendency to generate contents featuring dominant commercial brands from generic prompts, posing ethical and legal risks. We propose CIDER, a novel, model-agnostic framework to mitigate bias at inference-time through prompt refinement to avoid costly retraining. CIDER uses a lightweight detector to identify branded content and a Vision-Language Model (VLM) to generate stylistically divergent alternatives. We introduce the Brand Neutrality Score (BNS) to quantify this issue and perform extensive experiments on leading T2I models. Results show CIDER significantly reduces both explicit and implicit biases while maintaining image quality and aesthetic appeal. Our work offers a practical solution for more original and equitable content, contributing to the development of trustworthy generative AI.

## 🔍 Abstract (한글 번역)

arXiv:2509.15803v1 발표 유형: 교차  
초록: 텍스트-이미지(T2I) 모델은 일반적인 프롬프트에서 지배적인 상업 브랜드를 특징으로 하는 콘텐츠를 생성하는 경향이 있는, 상당하지만 아직 충분히 탐구되지 않은 "브랜드 편향"을 보이며, 이는 윤리적 및 법적 위험을 초래할 수 있습니다. 우리는 CIDER라는 새로운 모델-독립적 프레임워크를 제안하여, 비용이 많이 드는 재훈련을 피하기 위해 프롬프트 정제를 통해 추론 시 편향을 완화합니다. CIDER는 경량 탐지기를 사용하여 브랜드 콘텐츠를 식별하고, 비전-언어 모델(VLM)을 사용하여 스타일적으로 다양한 대안을 생성합니다. 우리는 이 문제를 정량화하기 위해 브랜드 중립성 점수(BNS)를 도입하고, 주요 T2I 모델에 대한 광범위한 실험을 수행합니다. 결과는 CIDER가 이미지 품질과 미적 매력을 유지하면서 명시적 및 암묵적 편향을 모두 상당히 줄이는 것을 보여줍니다. 우리의 연구는 보다 독창적이고 공정한 콘텐츠를 위한 실용적인 솔루션을 제공하며, 신뢰할 수 있는 생성 AI의 발전에 기여합니다.

## 📝 요약

이 논문은 텍스트-이미지(T2I) 모델이 상업적 브랜드를 과도하게 반영하는 "브랜드 편향" 문제를 다루고 있습니다. 이를 해결하기 위해 CIDER라는 새로운 프레임워크를 제안합니다. CIDER는 추론 시점에서 프롬프트를 개선하여 편향을 줄이며, 경량 탐지기를 사용해 브랜드 콘텐츠를 식별하고, 비전-언어 모델(VLM)을 통해 스타일적으로 다양한 대안을 생성합니다. 또한 브랜드 중립성 점수(BNS)를 도입하여 편향 정도를 측정합니다. 실험 결과, CIDER는 이미지 품질과 미적 매력을 유지하면서도 명시적 및 암묵적 편향을 크게 줄이는 것으로 나타났습니다. 이 연구는 신뢰할 수 있는 생성 AI 개발에 기여합니다.

## 🎯 주요 포인트

- 1. T2I 모델은 상업적 브랜드를 강조하는 "브랜드 편향"을 보이며, 이는 윤리적 및 법적 위험을 초래할 수 있다.

- 2. CIDER는 추론 시점에서 프롬프트 개선을 통해 편향을 완화하는 모델 비종속적 프레임워크로, 비용이 많이 드는 재훈련을 피할 수 있다.

- 3. CIDER는 경량 탐지기를 사용하여 브랜드 콘텐츠를 식별하고, 비전-언어 모델을 활용해 스타일적으로 다양한 대안을 생성한다.

- 4. 브랜드 중립성 점수(BNS)를 도입하여 브랜드 편향 문제를 정량화하고, 주요 T2I 모델을 대상으로 광범위한 실험을 수행했다.

- 5. CIDER는 이미지 품질과 미적 매력을 유지하면서 명시적 및 암시적 편향을 크게 줄이는 것으로 나타났다.

---

*Generated on 2025-09-22 14:12:30*