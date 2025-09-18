
# Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction

**Korean Title:** 단일 뷰 재구성을 통한 상대 카메라 자세 추정을 위한 가우시안 정렬

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Multi-view Geometry|Multi-view Geometry]] [[keywords/broad/Camera Pose Estimation|Camera Pose Estimation]] [[keywords/broad/3D Reconstruction|3D Reconstruction]] [[keywords/specific/Monocular Depth Estimator|Monocular Depth Estimator]] [[keywords/unique/GARPS|GARPS]] [[categories/cs.CV|cs.CV]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-view Geometry
**🔬 Broad Technical**: Camera Pose Estimation, 3D Reconstruction
**🔗 Specific Connectable**: Monocular Depth Estimator
**⭐ Unique Technical**: Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction

**ArXiv ID**: [2509.13652](https://arxiv.org/abs/2509.13652)
**Published**: 2025-09-18
**Category**: cs.CV
**PDF**: [Download](https://arxiv.org/pdf/2509.13652.pdf)


## 🏷️ 추출된 키워드



`Camera Pose Estimation` • 

`3D Reconstruction` • 

`Monocular Depth Estimator` • 

`Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction` • 

`Multi-view Geometry`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13652v1 Announce Type: new 
Abstract: Estimating metric relative camera pose from a pair of images is of great importance for 3D reconstruction and localisation. However, conventional two-view pose estimation methods are not metric, with camera translation known only up to a scale, and struggle with wide baselines and textureless or reflective surfaces. This paper introduces GARPS, a training-free framework that casts this problem as the direct alignment of two independently reconstructed 3D scenes. GARPS leverages a metric monocular depth estimator and a Gaussian scene reconstructor to obtain a metric 3D Gaussian Mixture Model (GMM) for each image. It then refines an initial pose from a feed-forward two-view pose estimator by optimising a differentiable GMM alignment objective. This objective jointly considers geometric structure, view-independent colour, anisotropic covariance, and semantic feature consistency, and is robust to occlusions and texture-poor regions without requiring explicit 2D correspondences. Extensive experiments on the Real\-Estate10K dataset demonstrate that GARPS outperforms both classical and state-of-the-art learning-based methods, including MASt3R. These results highlight the potential of bridging single-view perception with multi-view geometry to achieve robust and metric relative pose estimation.

## 🔍 Abstract (한글 번역)

arXiv:2509.13652v1 발표 유형: 새로운
요약: 두 장의 이미지로부터 메트릭 상대 카메라 포즈를 추정하는 것은 3D 재구성 및 위치 결정에 매우 중요합니다. 그러나 기존의 두 뷰 포즈 추정 방법은 메트릭이 아니며, 카메라 이동은 스케일까지만 알려져 있으며, 넓은 베이스라인 및 질감이 없거나 반사 표면과 같은 어려움이 있습니다. 본 논문에서는 이 문제를 두 개의 독립적으로 재구성된 3D 장면의 직접 정렬로 캐스팅하는 훈련 불필요한 프레임워크인 GARPS를 소개합니다. GARPS는 메트릭 단안 깊이 추정기와 가우시안 장면 재구성자를 활용하여 각 이미지에 대한 메트릭 3D 가우시안 혼합 모델 (GMM)을 얻습니다. 그런 다음 feed-forward 두 뷰 포즈 추정기에서 초기 포즈를 세밀하게 조정하여 미분 가능한 GMM 정렬 목적을 최적화합니다. 이 목적은 기하 구조, 뷰 독립적 색상, 이방성 공분산 및 의미적 특징 일관성을 고려하며, 명확한 2D 대응을 요구하지 않고, 가려짐 및 질감이 부족한 지역에 강건합니다. Real-Estate10K 데이터셋에서의 광범위한 실험 결과는 GARPS가 MASt3R을 포함한 고전적 및 최신 학습 기반 방법을 능가한다는 것을 보여줍니다. 이러한 결과는 단일 뷰 인식과 다중 뷰 기하를 연결하여 견고하고 메트릭 상대 포즈 추정을 달성하는 잠재력을 강조합니다.

## 📝 요약

이 연구는 두 장의 이미지로부터 메트릭 상대 카메라 자세를 추정하는 것이 3D 재구성과 위치 지정에 매우 중요하다. 그러나 기존의 두 뷰 자세 추정 방법은 메트릭이 아니며, 카메라 이동은 스케일까지만 알려져 있어 넓은 베이스라인과 질감이 없거나 반사 표면에서 어려움을 겪는다. 본 논문에서는 GARPS를 소개하는데, 이는 이 문제를 두 개의 독립적으로 재구성된 3D 장면의 직접적인 정렬로 캐스팅하는 훈련 필요 없는 프레임워크이다. GARPS는 메트릭 단안 깊이 추정기와 가우시안 장면 재구성기를 활용하여 각 이미지에 대한 메트릭 3D 가우시안 혼합 모델 (GMM)을 얻는다. 그런 다음, 미분 가능한 GMM 정렬 목적을 최적화함으로써 피드포워드 두 뷰 자세 추정기로부터 초기 자세를 개선한다. 이 목적은 기하 구조, 뷰 독립적 색상, 이방성 공분산 및 의미적 특징 일관성을 고려하며, 명확한 2D 대응을 필요로하지 않으면서도 가려짐 및 질감이 부족한 영역에 강건하다. Real-Estate10K 데이터셋에서의 광범위한 실험 결과는 GARPS가 MASt3R을 포함한 고전적 및 최신 학습 기반 방법을 능가함을 보여준다. 이러한 결과는 단일 뷰 인식과 다중 뷰 기하를 연결하여 견고하고 메트릭 상대 자세 추정을 달성하는 잠재력을 강조한다.

## 🎯 주요 포인트


- 3D 재구성 및 위치 추정을 위한 상대 카메라 자세 추정이 중요하다.

- 기존의 두 뷰 자세 추정 방법은 메트릭하지 않고, 넓은 베이스라인 및 질감이 없는 표면에서 어려움을 겪는다.

- GARPS는 훈련 없이 문제를 두 독립적으로 재구성된 3D 장면의 직접 정렬로 캐스팅하는 프레임워크를 소개한다.

- GARPS는 메트릭 단안 깊이 추정기와 가우시안 장면 재구성기를 활용하여 이미지마다 메트릭 3D 가우시안 혼합 모델을 얻는다.


---

*Generated on 2025-09-18 16:59:22*