---
keywords:
  - Foundation Models
  - Neural Networks
  - Cross-Modal Distillation
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15224
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:48:58.971087",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Foundation Models",
    "Neural Networks",
    "Cross-Modal Distillation"
  ],
  "rejected_keywords": [
    "Event-Based Monocular Depth Estimation"
  ],
  "similarity_scores": {
    "Foundation Models": 0.82,
    "Neural Networks": 0.77,
    "Cross-Modal Distillation": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Depth AnyEvent: A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation

**Korean Title:** AnyEvent 깊이: 이벤트 기반 단안 깊이 추정을 위한 교차 모달 증류 패러다임

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Neural Networks|Recurrent Architecture]]
**⚡ Unique Technical**: [[keywords/Cross-Modal Distillation|Cross-Modal Distillation]]
**🚀 Evolved Concepts**: [[keywords/Foundation Models|Vision Foundation Model]]

## 🔗 유사한 논문
- [[VSE-MOT Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (80.6% similar)
- [[ColonCrafter A Depth Estimation Model for Colonoscopy Videos Using Diffusion Priors]] (80.5% similar)
- [[BEVUDA++ Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection]] (80.3% similar)
- [[FishBEV Distortion-Resilient Bird's Eye View Segmentation with Surround-View Fisheye Cameras]] (80.0% similar)
- [[UCorr Wire Detection and Depth Estimation for Autonomous Drones]] (79.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15224v1 Announce Type: new 
Abstract: Event cameras capture sparse, high-temporal-resolution visual information, making them particularly suitable for challenging environments with high-speed motion and strongly varying lighting conditions. However, the lack of large datasets with dense ground-truth depth annotations hinders learning-based monocular depth estimation from event data. To address this limitation, we propose a cross-modal distillation paradigm to generate dense proxy labels leveraging a Vision Foundation Model (VFM). Our strategy requires an event stream spatially aligned with RGB frames, a simple setup even available off-the-shelf, and exploits the robustness of large-scale VFMs. Additionally, we propose to adapt VFMs, either a vanilla one like Depth Anything v2 (DAv2), or deriving from it a novel recurrent architecture to infer depth from monocular event cameras. We evaluate our approach with synthetic and real-world datasets, demonstrating that i) our cross-modal paradigm achieves competitive performance compared to fully supervised methods without requiring expensive depth annotations, and ii) our VFM-based models achieve state-of-the-art performance.

## 🔍 Abstract (한글 번역)

arXiv:2509.15224v1 발표 유형: 신규  
초록: 이벤트 카메라는 희소하고 높은 시간 해상도의 시각 정보를 포착하여 고속 움직임과 강하게 변하는 조명 조건을 가진 까다로운 환경에 특히 적합합니다. 그러나 조밀한 실제 깊이 주석이 포함된 대규모 데이터 세트의 부족은 이벤트 데이터에서 학습 기반 단안 깊이 추정을 방해합니다. 이 한계를 극복하기 위해, 우리는 비전 파운데이션 모델(VFM)을 활용하여 조밀한 대리 레이블을 생성하는 교차 모달 증류 패러다임을 제안합니다. 우리의 전략은 RGB 프레임과 공간적으로 정렬된 이벤트 스트림을 필요로 하며, 이는 상용으로도 간단히 사용할 수 있는 설정이며, 대규모 VFM의 견고함을 활용합니다. 또한, VFMs를 적응시키기 위해, Depth Anything v2 (DAv2)와 같은 기본 모델을 사용하거나, 단안 이벤트 카메라로부터 깊이를 추론하기 위해 새로운 순환 아키텍처를 도출하는 것을 제안합니다. 우리는 합성 및 실제 데이터 세트를 사용하여 우리의 접근 방식을 평가하며, i) 우리의 교차 모달 패러다임이 비싼 깊이 주석 없이도 완전 감독 방법과 비교하여 경쟁력 있는 성능을 달성하고, ii) 우리의 VFM 기반 모델이 최첨단 성능을 달성함을 입증합니다.

## 📝 요약

이 논문은 이벤트 카메라를 활용한 단안 깊이 추정의 한계를 극복하기 위해 크로스 모달 증류 패러다임을 제안합니다. 이 방법은 Vision Foundation Model(VFM)을 활용하여 밀도 있는 대리 라벨을 생성하며, 이벤트 스트림과 RGB 프레임의 공간적 정렬을 요구합니다. 또한, Depth Anything v2(DAv2)와 같은 VFM을 활용하거나 이를 기반으로 새로운 순환 구조를 도입하여 깊이를 추론합니다. 제안된 방법은 합성 및 실제 데이터셋에서 평가되었으며, 비싼 깊이 주석 없이도 경쟁력 있는 성능을 보였고, VFM 기반 모델은 최첨단 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. 이벤트 카메라는 고속 움직임과 조명이 크게 변하는 환경에서 적합한 고해상도의 시각 정보를 포착한다.

- 2. 대규모 데이터셋의 부족은 이벤트 데이터를 통한 단안 깊이 추정 학습에 장애가 된다.

- 3. 비전 파운데이션 모델(VFM)을 활용한 교차 모달 증류 패러다임을 제안하여 밀집된 대리 라벨을 생성한다.

- 4. RGB 프레임과 공간적으로 정렬된 이벤트 스트림을 사용하여 간단한 설정으로 깊이 추정을 수행한다.

- 5. 제안된 VFM 기반 모델은 비싼 깊이 주석 없이도 최첨단 성능을 달성한다.

---

*Generated on 2025-09-19 16:11:26*