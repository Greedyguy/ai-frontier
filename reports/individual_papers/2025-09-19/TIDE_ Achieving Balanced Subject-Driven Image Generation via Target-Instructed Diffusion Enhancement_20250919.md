
# TIDE: Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement

**Korean Title:** TIDE: 목표 지시 확산 강화를 통한 균형 잡힌 주제 중심 이미지 생성 달성

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Subject Driven Image Generation

## 🔗 유사한 논문
- [[Iterative Prompt Refinement for Safer Text-to-Image Generation_20250918|Iterative Prompt Refinement for Safer Text-to-Image Generation]] (80.9% similar)
- [[BiasMap Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation]] (80.7% similar)
- [[Identity-Preserving Text-to-Video Generation Guided by Simple yet Effective Spatial-Temporal Decoupled Representations_20250918|Identity-Preserving Text-to-Video Generation Guided by Simple yet Effective Spatial-Temporal Decoupled Representations]] (80.5% similar)
- [[Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (80.3% similar)
- [[DiffHash Text-Guided Targeted Attack via Diffusion Models against Deep Hashing Image Retrieval]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.06499v2 Announce Type: replace 
Abstract: Subject-driven image generation (SDIG) aims to manipulate specific subjects within images while adhering to textual instructions, a task crucial for advancing text-to-image diffusion models. SDIG requires reconciling the tension between maintaining subject identity and complying with dynamic edit instructions, a challenge inadequately addressed by existing methods. In this paper, we introduce the Target-Instructed Diffusion Enhancing (TIDE) framework, which resolves this tension through target supervision and preference learning without test-time fine-tuning. TIDE pioneers target-supervised triplet alignment, modelling subject adaptation dynamics using a (reference image, instruction, target images) triplet. This approach leverages the Direct Subject Diffusion (DSD) objective, training the model with paired "winning" (balanced preservation-compliance) and "losing" (distorted) targets, systematically generated and evaluated via quantitative metrics. This enables implicit reward modelling for optimal preservation-compliance balance. Experimental results on standard benchmarks demonstrate TIDE's superior performance in generating subject-faithful outputs while maintaining instruction compliance, outperforming baseline methods across multiple quantitative metrics. TIDE's versatility is further evidenced by its successful application to diverse tasks, including structural-conditioned generation, image-to-image generation, and text-image interpolation. Our code is available at https://github.com/KomJay520/TIDE.

## 🔍 Abstract (한글 번역)

arXiv:2509.06499v2 발표 유형: 교체  
초록: 주제 기반 이미지 생성(SDIG)은 텍스트 지시에 따라 이미지 내 특정 주제를 조작하는 것을 목표로 하며, 이는 텍스트-이미지 확산 모델을 발전시키는 데 중요한 과제입니다. SDIG는 주제의 정체성을 유지하면서도 동적인 편집 지시에 따르는 것 사이의 긴장을 조화시켜야 하며, 이는 기존 방법들이 충분히 해결하지 못한 도전 과제입니다. 본 논문에서는 테스트 시간 미세 조정 없이 목표 감독과 선호 학습을 통해 이러한 긴장을 해결하는 Target-Instructed Diffusion Enhancing (TIDE) 프레임워크를 소개합니다. TIDE는 목표 감독 삼중 정렬을 개척하여 (참조 이미지, 지시, 목표 이미지) 삼중을 사용하여 주제 적응 동역학을 모델링합니다. 이 접근 방식은 Direct Subject Diffusion (DSD) 목표를 활용하여, 모델을 "승리" (균형 잡힌 보존-준수) 및 "패배" (왜곡된) 목표와 함께 훈련시키며, 이는 체계적으로 생성되고 정량적 지표를 통해 평가됩니다. 이를 통해 최적의 보존-준수 균형을 위한 암묵적 보상 모델링이 가능합니다. 표준 벤치마크에 대한 실험 결과는 TIDE가 주제에 충실한 출력을 생성하면서 지시 준수를 유지하는 데 있어 우수한 성능을 발휘하며, 여러 정량적 지표에서 기존 방법을 능가함을 보여줍니다. TIDE의 다재다능함은 구조 조건 생성, 이미지 간 생성, 텍스트-이미지 보간을 포함한 다양한 작업에 성공적으로 적용됨으로써 더욱 입증됩니다. 우리의 코드는 https://github.com/KomJay520/TIDE에서 이용할 수 있습니다.

## 📝 요약

이 논문은 주제 기반 이미지 생성(SDIG)에서 주제의 정체성을 유지하면서 텍스트 지시를 따르는 문제를 해결하기 위해 TIDE(Targe-Instructed Diffusion Enhancing) 프레임워크를 제안합니다. TIDE는 테스트 시점의 미세 조정 없이 목표 감독과 선호 학습을 통해 주제 적응의 긴장을 해결합니다. 이 방법은 참조 이미지, 지시, 목표 이미지의 삼중항을 사용하여 주제 적응 동력을 모델링하며, Direct Subject Diffusion(DSD) 목표를 활용하여 균형 잡힌 보존-준수와 왜곡된 목표를 생성 및 평가합니다. 실험 결과, TIDE는 다양한 정량적 지표에서 기존 방법보다 우수한 성능을 보이며, 구조 조건 생성, 이미지 간 생성, 텍스트-이미지 보간 등 다양한 작업에 성공적으로 적용됩니다.

## 🎯 주요 포인트

- 1. 주제 중심 이미지 생성(SDIG)은 이미지 내 특정 주제를 조작하면서 텍스트 지시를 따르는 작업으로, 텍스트-이미지 확산 모델 발전에 중요하다.

- 2. TIDE 프레임워크는 테스트 시 미세 조정 없이 목표 감독 및 선호 학습을 통해 주제 정체성 유지와 동적 편집 지시 준수 간의 긴장을 해결한다.

- 3. TIDE는 목표 감독 삼중 정렬을 개척하여 (참조 이미지, 지시, 목표 이미지) 삼중을 사용하여 주제 적응 역학을 모델링한다.

- 4. 실험 결과, TIDE는 다양한 정량적 지표에서 기존 방법을 능가하며 주제 충실한 출력 생성과 지시 준수를 동시에 달성한다.

- 5. TIDE의 다재다능함은 구조 조건 생성, 이미지-이미지 생성, 텍스트-이미지 보간 등 다양한 작업에 성공적으로 적용됨으로써 입증된다.

---

*Generated on 2025-09-19 16:18:38*