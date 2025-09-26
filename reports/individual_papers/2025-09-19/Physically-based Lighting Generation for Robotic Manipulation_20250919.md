---
keywords:
  - Diffusion Models
  - Robotic Manipulation
  - Imitation Learning
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2508.01442
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:29:24.515515",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Models",
    "Robotic Manipulation",
    "Imitation Learning"
  ],
  "rejected_keywords": [
    "Inverse Rendering"
  ],
  "similarity_scores": {
    "Diffusion Models": 0.85,
    "Robotic Manipulation": 0.82,
    "Imitation Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Physically-based Lighting Generation for Robotic Manipulation

**Korean Title:** 물리 기반 조명 생성의 로봇 조작에의 응용

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Robotic Manipulation|robotic manipulation]], [[keywords/Imitation Learning|imitation learning]]

## 🔗 유사한 논문
- [[PhysicalAgent Towards General Cognitive Robotics with Foundation World Models]] (85.7% similar)
- [[textsc{Gen2Real} Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (83.7% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (80.9% similar)
- [[M4Diffuser Multi-View Diffusion Policy with Manipulability-Aware Control for Robust Mobile Manipulation]] (80.7% similar)
- [[WorldForge Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance]] (80.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.01442v2 Announce Type: replace 
Abstract: In this paper, we propose the first framework that leverages physically-based inverse rendering for novel lighting generation on existing real-world human demonstrations of robotic manipulation tasks. Specifically, inverse rendering decomposes the first frame in each demonstration into geometric (surface normal, depth) and material (albedo, roughness, metallic) properties, which are then used to render appearance changes under different lighting sources. To improve efficiency and maintain consistency across each generated sequence, we fine-tune Stable Video Diffusion on robot execution videos for temporal lighting propagation. We evaluate our framework by measuring the visual quality of the generated sequences, assessing its effectiveness in improving the imitation learning policy performance (38.75\%) under six unseen real-world lighting conditions, and conduct ablation studies on individual modules of the proposed framework. We further showcase three downstream applications enabled by the proposed framework: background generation, object texture generation and distractor positioning. The code for the framework will be made publicly available.

## 🔍 Abstract (한글 번역)

arXiv:2508.01442v2 발표 유형: 교체  
초록: 본 논문에서는 로봇 조작 작업의 기존 실제 시연에서 새로운 조명 생성을 위해 물리 기반의 역 렌더링을 활용하는 최초의 프레임워크를 제안합니다. 구체적으로, 역 렌더링은 각 시연의 첫 번째 프레임을 기하학적(표면 법선, 깊이) 및 물질적(반사율, 거칠기, 금속성) 속성으로 분해하여, 이를 다양한 조명 소스 하에서의 외관 변화를 렌더링하는 데 사용합니다. 각 생성된 시퀀스의 효율성을 높이고 일관성을 유지하기 위해, 우리는 로봇 실행 비디오에서 시간적 조명 전파를 위해 안정적인 비디오 확산을 미세 조정합니다. 우리는 생성된 시퀀스의 시각적 품질을 측정하고, 여섯 가지 보지 못한 실제 조명 조건에서 모방 학습 정책 성능을 38.75% 향상시키는 효과를 평가하며, 제안된 프레임워크의 개별 모듈에 대한 소거 연구를 수행합니다. 또한, 제안된 프레임워크가 가능하게 하는 세 가지 다운스트림 응용 프로그램인 배경 생성, 객체 텍스처 생성 및 방해물 배치를 소개합니다. 프레임워크의 코드는 공개적으로 제공될 예정입니다.

## 📝 요약

이 논문에서는 로봇 조작 작업의 실제 시연에서 새로운 조명 생성을 위해 물리 기반의 역 렌더링을 활용하는 최초의 프레임워크를 제안합니다. 역 렌더링은 시연의 첫 프레임을 기하학적(표면 법선, 깊이) 및 재질(반사율, 거칠기, 금속성) 속성으로 분해하여 다양한 조명 조건에서의 외관 변화를 렌더링합니다. 효율성을 높이고 일관성을 유지하기 위해 로봇 실행 비디오에서 안정적인 비디오 확산 모델을 미세 조정하여 시간적 조명 전파를 수행합니다. 제안된 프레임워크는 생성된 시퀀스의 시각적 품질을 평가하고, 여섯 가지 새로운 조명 조건에서 모방 학습 정책 성능을 38.75% 향상시키는 효과를 입증했습니다. 또한, 프레임워크의 개별 모듈에 대한 소거 연구를 수행하고, 배경 생성, 객체 텍스처 생성, 방해물 배치와 같은 세 가지 응용 사례를 제시합니다. 프레임워크의 코드는 공개될 예정입니다.

## 🎯 주요 포인트

- 1. 물리 기반 역 렌더링을 활용하여 로봇 조작 작업의 새로운 조명 생성 프레임워크를 제안했습니다.

- 2. 역 렌더링은 시연의 첫 프레임을 기하학적 및 물질적 속성으로 분해하여 다양한 조명 조건에서 외관 변화를 렌더링합니다.

- 3. 로봇 실행 비디오에서 안정적인 비디오 확산을 미세 조정하여 생성된 시퀀스의 효율성과 일관성을 개선했습니다.

- 4. 제안된 프레임워크는 6가지 새로운 실제 조명 조건에서 모방 학습 정책 성능을 38.75% 향상시켰습니다.

- 5. 제안된 프레임워크를 통해 배경 생성, 객체 텍스처 생성 및 방해물 위치 지정과 같은 세 가지 응용 프로그램을 구현할 수 있습니다.

---

*Generated on 2025-09-19 16:38:21*