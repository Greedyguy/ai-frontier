
# Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration

**Korean Title:** 3D 재구성을 향상시키기 위한 확산 기반 단안 카메라 보정

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Diffusion-based Calibration

## 🔗 유사한 논문
- [[MCGS-SLAM A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (82.6% similar)
- [[Depth AnyEvent A Cross-Modal Distillation Paradigm for Event-Based Monocular Depth Estimation]] (82.2% similar)
- [[Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction_20250918|Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction]] (82.0% similar)
- [[Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (80.8% similar)
- [[DICE Diffusion Consensus Equilibrium for Sparse-view CT Reconstruction]] (80.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2411.17240v3 Announce Type: replace 
Abstract: In this paper, we present DM-Calib, a diffusion-based approach for estimating pinhole camera intrinsic parameters from a single input image. Monocular camera calibration is essential for many 3D vision tasks. However, most existing methods depend on handcrafted assumptions or are constrained by limited training data, resulting in poor generalization across diverse real-world images. Recent advancements in stable diffusion models, trained on massive data, have shown the ability to generate high-quality images with varied characteristics. Emerging evidence indicates that these models implicitly capture the relationship between camera focal length and image content. Building on this insight, we explore how to leverage the powerful priors of diffusion models for monocular pinhole camera calibration. Specifically, we introduce a new image-based representation, termed Camera Image, which losslessly encodes the numerical camera intrinsics and integrates seamlessly with the diffusion framework. Using this representation, we reformulate the problem of estimating camera intrinsics as the generation of a dense Camera Image conditioned on an input image. By fine-tuning a stable diffusion model to generate a Camera Image from a single RGB input, we can extract camera intrinsics via a RANSAC operation. We further demonstrate that our monocular calibration method enhances performance across various 3D tasks, including zero-shot metric depth estimation, 3D metrology, pose estimation and sparse-view reconstruction. Extensive experiments on multiple public datasets show that our approach significantly outperforms baselines and provides broad benefits to 3D vision tasks.

## 🔍 Abstract (한글 번역)

arXiv:2411.17240v3 발표 유형: 교체  
초록: 이 논문에서는 단일 입력 이미지로부터 핀홀 카메라의 내재적 매개변수를 추정하기 위한 확산 기반 접근법인 DM-Calib를 제시합니다. 단안 카메라 보정은 많은 3D 비전 작업에 필수적입니다. 그러나 대부분의 기존 방법은 수작업으로 만들어진 가정에 의존하거나 제한된 훈련 데이터에 의해 제약을 받아 다양한 실제 이미지에 대한 일반화가 부족합니다. 대량의 데이터로 훈련된 안정적인 확산 모델의 최근 발전은 다양한 특성을 가진 고품질 이미지를 생성할 수 있는 능력을 보여주었습니다. 최근 증거에 따르면 이러한 모델은 카메라 초점 거리와 이미지 콘텐츠 간의 관계를 암묵적으로 포착하고 있습니다. 이 통찰력을 바탕으로, 우리는 단안 핀홀 카메라 보정을 위해 확산 모델의 강력한 사전 지식을 활용하는 방법을 탐구합니다. 구체적으로, 우리는 카메라의 수치적 내재성을 무손실로 인코딩하고 확산 프레임워크와 원활하게 통합되는 새로운 이미지 기반 표현인 '카메라 이미지'를 도입합니다. 이 표현을 사용하여, 우리는 카메라 내재성 추정 문제를 입력 이미지에 조건화된 밀집한 카메라 이미지 생성 문제로 재구성합니다. 단일 RGB 입력으로부터 카메라 이미지를 생성하도록 안정적인 확산 모델을 미세 조정함으로써, 우리는 RANSAC 작업을 통해 카메라 내재성을 추출할 수 있습니다. 우리는 또한 우리의 단안 보정 방법이 제로샷 메트릭 깊이 추정, 3D 계측, 자세 추정 및 희소 뷰 재구성을 포함한 다양한 3D 작업에서 성능을 향상시킨다는 것을 입증합니다. 여러 공개 데이터셋에 대한 광범위한 실험은 우리의 접근법이 기준선을 크게 능가하며 3D 비전 작업에 폭넓은 이점을 제공한다는 것을 보여줍니다.

## 📝 요약

이 논문에서는 단일 입력 이미지로부터 핀홀 카메라의 내재적 파라미터를 추정하는 확산 기반 접근법인 DM-Calib를 제안합니다. 기존의 단안 카메라 보정 방법은 제한된 훈련 데이터와 수작업 가정에 의존하여 다양한 실제 이미지에 대한 일반화가 부족합니다. 최근 대량의 데이터를 기반으로 훈련된 안정적 확산 모델은 카메라 초점 거리와 이미지 콘텐츠 간의 관계를 암묵적으로 포착할 수 있음을 보여주었습니다. 이를 바탕으로, 우리는 확산 모델의 강력한 사전 정보를 활용하여 단안 핀홀 카메라 보정을 수행합니다. 새로운 이미지 기반 표현인 '카메라 이미지'를 도입하여, 카메라 내재치를 손실 없이 인코딩하고 확산 프레임워크와 통합합니다. 이를 통해 카메라 내재치 추정을 입력 이미지에 조건화된 밀집 카메라 이미지 생성 문제로 재구성합니다. 단일 RGB 입력에서 카메라 이미지를 생성하도록 안정적 확산 모델을 미세 조정하여, RANSAC 작업을 통해 카메라 내재치를 추출합니다. 다양한 3D 작업에서 성능 향상을 입증하며, 여러 공개 데이터셋에서 기존 방법들을 능가하는 결과를 보여줍니다.

## 🎯 주요 포인트

- 1. DM-Calib는 단일 입력 이미지로부터 핀홀 카메라의 내재 파라미터를 추정하는 확산 기반 접근법을 제안합니다.

- 2. 기존 방법들은 제한된 훈련 데이터와 수작업 가정에 의존하여 다양한 실제 이미지에 대한 일반화가 부족합니다.

- 3. 안정적인 확산 모델의 발전은 카메라 초점 거리와 이미지 콘텐츠 간의 관계를 암묵적으로 포착할 수 있음을 보여줍니다.

- 4. 새로운 이미지 기반 표현인 Camera Image를 도입하여 카메라 내재 파라미터 추정을 단일 RGB 입력으로부터의 Camera Image 생성 문제로 재구성합니다.

- 5. 다양한 3D 작업에서 DM-Calib의 단안 캘리브레이션 방법이 성능을 향상시키며, 여러 공개 데이터셋에서 기존 방법들을 능가하는 성과를 보입니다.

---

*Generated on 2025-09-19 16:15:34*