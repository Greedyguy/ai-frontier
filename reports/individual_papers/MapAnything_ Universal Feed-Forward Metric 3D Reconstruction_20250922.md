# MapAnything: Universal Feed-Forward Metric 3D Reconstruction

**Korean Title:** MapAnything: 범용 피드포워드 메트릭 3D 재구성

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Unified 3D Reconstruction

## 🔗 유사한 논문
- [[2025-09-18/Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction_20250918|Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction]] (81.3% similar)
- [[2025-09-19/Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (80.9% similar)
- [[2025-09-19/Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration_20250919|Boost 3D Reconstruction using Diffusion-based Monocular Camera Calibration]] (80.4% similar)
- [[2025-09-18/GeoAware-VLA_ Implicit Geometry Aware Vision-Language-Action Model_20250918|GeoAware-VLA Implicit Geometry Aware Vision-Language-Action Model]] (80.1% similar)
- [[2025-09-18/Embodied Navigation Foundation Model_20250918|Embodied Navigation Foundation Model]] (79.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13414v2 Announce Type: replace-cross 
Abstract: We introduce MapAnything, a unified transformer-based feed-forward model that ingests one or more images along with optional geometric inputs such as camera intrinsics, poses, depth, or partial reconstructions, and then directly regresses the metric 3D scene geometry and cameras. MapAnything leverages a factored representation of multi-view scene geometry, i.e., a collection of depth maps, local ray maps, camera poses, and a metric scale factor that effectively upgrades local reconstructions into a globally consistent metric frame. Standardizing the supervision and training across diverse datasets, along with flexible input augmentation, enables MapAnything to address a broad range of 3D vision tasks in a single feed-forward pass, including uncalibrated structure-from-motion, calibrated multi-view stereo, monocular depth estimation, camera localization, depth completion, and more. We provide extensive experimental analyses and model ablations demonstrating that MapAnything outperforms or matches specialist feed-forward models while offering more efficient joint training behavior, thus paving the way toward a universal 3D reconstruction backbone.

## 🔍 Abstract (한글 번역)

arXiv:2509.13414v2 발표 유형: 교차 교체

초록: 우리는 MapAnything이라는 통합된 트랜스포머 기반의 피드포워드 모델을 소개합니다. 이 모델은 하나 이상의 이미지와 함께 카메라 내재 파라미터, 자세, 깊이 또는 부분적인 재구성과 같은 선택적인 기하학적 입력을 수용하고, 그 후 직접적으로 메트릭 3D 장면 기하학과 카메라를 회귀합니다. MapAnything은 다중 뷰 장면 기하학의 분해된 표현, 즉 깊이 맵, 로컬 레이 맵, 카메라 자세 및 로컬 재구성을 전역적으로 일관된 메트릭 프레임으로 효과적으로 업그레이드하는 메트릭 스케일 팩터의 집합을 활용합니다. 다양한 데이터셋에 걸쳐 감독과 훈련을 표준화하고 유연한 입력 증강을 통해 MapAnything은 비보정 구조-이동, 보정된 다중 뷰 스테레오, 단안 깊이 추정, 카메라 위치 추정, 깊이 완성 등 단일 피드포워드 패스로 다양한 3D 비전 작업을 처리할 수 있습니다. 우리는 광범위한 실험 분석과 모델 절제를 제공하여 MapAnything이 전문 피드포워드 모델을 능가하거나 일치하면서도 더 효율적인 공동 훈련 동작을 제공함을 보여주며, 궁극적으로 보편적인 3D 재구성 백본으로의 길을 열어줍니다.

## 📝 요약

MapAnything는 여러 이미지를 입력받아 3D 장면의 기하학적 구조와 카메라 정보를 직접 예측하는 통합 트랜스포머 기반 모델입니다. 이 모델은 다양한 데이터셋에서의 학습을 표준화하고 유연한 입력 확장을 통해 구조-이동, 다중 뷰 스테레오, 단안 깊이 추정 등 다양한 3D 비전 작업을 단일 패스로 처리합니다. 실험 결과, MapAnything는 전문 모델과 동등하거나 더 나은 성능을 보이며, 효율적인 공동 학습을 가능하게 하여 범용 3D 재구성의 기반을 마련합니다.

## 🎯 주요 포인트

- 1. MapAnything는 여러 이미지를 입력받아 3D 장면 기하학과 카메라를 직접 회귀하는 통합된 트랜스포머 기반 모델입니다.

- 2. 이 모델은 깊이 맵, 로컬 레이 맵, 카메라 포즈, 메트릭 스케일 팩터를 활용하여 지역적 재구성을 전역적으로 일관된 메트릭 프레임으로 업그레이드합니다.

- 3. 다양한 데이터셋에 대한 표준화된 감독과 유연한 입력 증강을 통해 MapAnything은 단일 피드포워드 패스로 다양한 3D 비전 작업을 처리할 수 있습니다.

- 4. 실험 분석과 모델 소거를 통해 MapAnything은 전문 피드포워드 모델과 비교하여 더 나은 성능을 보이거나 동등한 성능을 제공하며, 효율적인 공동 학습을 가능하게 합니다.

- 5. MapAnything은 범용 3D 재구성 백본으로의 발전을 위한 길을 열어줍니다.

---

*Generated on 2025-09-22 15:05:05*