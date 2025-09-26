---
keywords:
  - Neural Radiance Fields
  - 3D Gaze Redirection
  - 3D Gaussian Splatting
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2508.06136
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:26:47.505436",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Radiance Fields",
    "3D Gaze Redirection",
    "3D Gaussian Splatting"
  ],
  "rejected_keywords": [
    "Computer Vision"
  ],
  "similarity_scores": {
    "Neural Radiance Fields": 0.82,
    "3D Gaze Redirection": 0.78,
    "3D Gaussian Splatting": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Roll Your Eyes: Gaze Redirection via Explicit 3D Eyeball Rotation

**Korean Title:** 눈동자 굴리기: 명시적 3D 안구 회전을 통한 시선 재지정

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Neural Radiance Fields|Neural Radiance Fields]]
**⚡ Unique Technical**: [[keywords/3D Gaze Redirection|3D gaze redirection]], [[keywords/3D Gaussian Splatting|3D Gaussian Splatting]]

## 🔗 유사한 논문
- [[Lightweight_Gradient-Aware_Upscaling_of_3D_Gaussian_Splatting_Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (82.1% similar)
- [[WorldForge Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance]] (79.1% similar)
- [[MCGS-SLAM A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (78.9% similar)
- [[Gaussian_Alignment_for_Relative_Camera_Pose_Estimation_via_Single-View_Reconstruction_20250918|Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction]] (78.7% similar)
- [[LamiGauss Pitching Radiative Gaussian for Sparse-View X-ray Laminography Reconstruction]] (78.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.06136v2 Announce Type: replace-cross 
Abstract: We propose a novel 3D gaze redirection framework that leverages an explicit 3D eyeball structure. Existing gaze redirection methods are typically based on neural radiance fields, which employ implicit neural representations via volume rendering. Unlike these NeRF-based approaches, where the rotation and translation of 3D representations are not explicitly modeled, we introduce a dedicated 3D eyeball structure to represent the eyeballs with 3D Gaussian Splatting (3DGS). Our method generates photorealistic images that faithfully reproduce the desired gaze direction by explicitly rotating and translating the 3D eyeball structure. In addition, we propose an adaptive deformation module that enables the replication of subtle muscle movements around the eyes. Through experiments conducted on the ETH-XGaze dataset, we demonstrate that our framework is capable of generating diverse novel gaze images, achieving superior image quality and gaze estimation accuracy compared to previous state-of-the-art methods.

## 🔍 Abstract (한글 번역)

arXiv:2508.06136v2 발표 유형: 교차 교체  
초록: 우리는 명시적인 3D 안구 구조를 활용한 새로운 3D 시선 전환 프레임워크를 제안합니다. 기존의 시선 전환 방법은 일반적으로 볼륨 렌더링을 통한 암시적 신경 표현을 사용하는 신경 방사장(NeRF)에 기반하고 있습니다. 이러한 NeRF 기반 접근 방식과 달리, 3D 표현의 회전과 변환이 명시적으로 모델링되지 않는 경우, 우리는 3D 가우시안 스플래팅(3DGS)을 사용하여 안구를 표현하는 전용 3D 안구 구조를 도입합니다. 우리의 방법은 3D 안구 구조를 명시적으로 회전 및 변환하여 원하는 시선 방향을 충실히 재현하는 포토리얼리스틱 이미지를 생성합니다. 또한, 우리는 눈 주위의 미세한 근육 움직임을 복제할 수 있는 적응형 변형 모듈을 제안합니다. ETH-XGaze 데이터셋에서 수행된 실험을 통해, 우리의 프레임워크가 다양한 새로운 시선 이미지를 생성할 수 있으며, 이전 최첨단 방법들에 비해 우수한 이미지 품질과 시선 추정 정확도를 달성함을 입증합니다.

## 📝 요약

이 논문은 명시적인 3D 안구 구조를 활용한 새로운 3D 시선 전환 프레임워크를 제안합니다. 기존의 시선 전환 방법은 주로 암묵적인 신경 표현을 사용하는 신경 방사장(NeRF) 기반이지만, 본 연구는 3D 가우시안 스플래팅(3DGS)을 통해 안구를 명시적으로 회전 및 이동시킵니다. 이를 통해 원하는 시선 방향을 충실히 재현하는 사진 같은 이미지를 생성합니다. 또한, 눈 주위의 미세한 근육 움직임을 재현할 수 있는 적응형 변형 모듈을 제안합니다. ETH-XGaze 데이터셋을 사용한 실험 결과, 본 프레임워크는 다양한 새로운 시선 이미지를 생성하며, 기존 최첨단 방법들보다 우수한 이미지 품질과 시선 추정 정확도를 달성했습니다.

## 🎯 주요 포인트

- 1. 새로운 3D 시선 전환 프레임워크를 제안하여 명시적인 3D 안구 구조를 활용합니다.

- 2. 기존의 시선 전환 방법은 암묵적인 신경 표현을 사용하는 반면, 우리는 3D Gaussian Splatting을 통해 3D 안구 구조를 명시적으로 회전 및 변환합니다.

- 3. 적응형 변형 모듈을 도입하여 눈 주변의 미세한 근육 움직임을 재현할 수 있습니다.

- 4. ETH-XGaze 데이터셋을 활용한 실험을 통해, 우리의 프레임워크가 기존 최첨단 방법들보다 우수한 이미지 품질과 시선 추정 정확도를 달성함을 입증했습니다.

---

*Generated on 2025-09-19 15:19:42*