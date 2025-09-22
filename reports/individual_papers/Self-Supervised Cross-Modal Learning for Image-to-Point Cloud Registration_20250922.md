# Self-Supervised Cross-Modal Learning for Image-to-Point Cloud Registration

**Korean Title:** 자기 지도 학습을 통한 이미지-포인트 클라우드 정합을 위한 교차 모달 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Self-supervised Registration

## 🔗 유사한 논문
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (85.3% similar)
- [[2025-09-18/InterKey_ Cross-modal Intersection Keypoints for Global Localization on OpenStreetMap_20250918|InterKey Cross-modal Intersection Keypoints for Global Localization on OpenStreetMap]] (82.0% similar)
- [[2025-09-19/Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (81.0% similar)
- [[2025-09-19/Multi-label Scene Classification for Autonomous Vehicles_ Acquiring and Accumulating Knowledge from Diverse Datasets_20250919|Multi-label Scene Classification for Autonomous Vehicles Acquiring and Accumulating Knowledge from Diverse Datasets]] (80.4% similar)
- [[2025-09-18/UniPLV_ Towards Label-Efficient Open-World 3D Scene Understanding by Regional Visual Language Supervision_20250918|UniPLV Towards Label-Efficient Open-World 3D Scene Understanding by Regional Visual Language Supervision]] (80.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15882v1 Announce Type: cross 
Abstract: Bridging 2D and 3D sensor modalities is critical for robust perception in autonomous systems. However, image-to-point cloud (I2P) registration remains challenging due to the semantic-geometric gap between texture-rich but depth-ambiguous images and sparse yet metrically precise point clouds, as well as the tendency of existing methods to converge to local optima. To overcome these limitations, we introduce CrossI2P, a self-supervised framework that unifies cross-modal learning and two-stage registration in a single end-to-end pipeline. First, we learn a geometric-semantic fused embedding space via dual-path contrastive learning, enabling annotation-free, bidirectional alignment of 2D textures and 3D structures. Second, we adopt a coarse-to-fine registration paradigm: a global stage establishes superpoint-superpixel correspondences through joint intra-modal context and cross-modal interaction modeling, followed by a geometry-constrained point-level refinement for precise registration. Third, we employ a dynamic training mechanism with gradient normalization to balance losses for feature alignment, correspondence refinement, and pose estimation. Extensive experiments demonstrate that CrossI2P outperforms state-of-the-art methods by 23.7% on the KITTI Odometry benchmark and by 37.9% on nuScenes, significantly improving both accuracy and robustness.

## 🔍 Abstract (한글 번역)

arXiv:2509.15882v1 발표 유형: 교차  
초록: 자율 시스템에서 견고한 인식을 위해 2D와 3D 센서 모달리티를 연결하는 것은 매우 중요합니다. 그러나 이미지와 포인트 클라우드(I2P) 간의 정합은 텍스처가 풍부하지만 깊이가 모호한 이미지와 희소하지만 측정적으로 정확한 포인트 클라우드 사이의 의미-기하학적 간극, 그리고 기존 방법들이 지역 최적점에 수렴하는 경향 때문에 여전히 도전 과제입니다. 이러한 한계를 극복하기 위해, 우리는 교차 모달 학습과 2단계 정합을 단일 종단 간 파이프라인으로 통합하는 자가 지도 학습 프레임워크인 CrossI2P를 소개합니다. 첫째, 이중 경로 대조 학습을 통해 기하학-의미 융합 임베딩 공간을 학습하여 주석 없이 2D 텍스처와 3D 구조의 양방향 정렬을 가능하게 합니다. 둘째, 우리는 거칠게부터 정밀하게 정합하는 패러다임을 채택합니다: 글로벌 단계에서는 모달 내 컨텍스트와 모달 간 상호작용 모델링을 통해 슈퍼포인트-슈퍼픽셀 대응을 설정하고, 이후 기하학적으로 제약된 포인트 레벨 정제를 통해 정밀한 정합을 수행합니다. 셋째, 우리는 피처 정렬, 대응 정제 및 자세 추정을 위한 손실을 균형 있게 조정하기 위해 그래디언트 정규화를 통한 동적 학습 메커니즘을 사용합니다. 광범위한 실험 결과, CrossI2P가 KITTI 주행 거리 벤치마크에서 23.7%, nuScenes에서 37.9% 더 우수한 성능을 발휘하여 정확성과 견고성을 크게 향상시킴을 보여줍니다.

## 📝 요약

이 논문은 자율 시스템에서 2D 이미지와 3D 포인트 클라우드 간의 효과적인 결합을 위한 새로운 방법론인 CrossI2P를 제안합니다. CrossI2P는 자가 지도 학습 프레임워크로, 두 가지 센서 모달리티 간의 의미-기하학적 차이를 극복하고, 기존 방법의 지역 최적화 문제를 해결합니다. 이 방법론은 대조 학습을 통해 2D와 3D 간의 주석 없이 양방향 정렬을 가능하게 하고, 거친 단계와 세밀한 단계로 나누어 정밀한 등록을 수행합니다. 또한, 동적 학습 메커니즘을 통해 특징 정렬과 자세 추정을 최적화합니다. 실험 결과, CrossI2P는 KITTI Odometry와 nuScenes 벤치마크에서 각각 23.7%와 37.9%의 성능 향상을 보여, 정확성과 견고성을 크게 개선했습니다.

## 🎯 주요 포인트

- 1. CrossI2P는 자가 지도 학습 프레임워크로, 2D 이미지와 3D 포인트 클라우드 간의 교차 모달 학습과 이단계 등록을 통합하여 이미지-포인트 클라우드 등록의 한계를 극복합니다.

- 2. 듀얼 경로 대조 학습을 통해 기하학적-의미적 융합 임베딩 공간을 학습하여 주석 없이 2D 텍스처와 3D 구조의 양방향 정렬을 가능하게 합니다.

- 3. 조-세밀 등록 패러다임을 채택하여, 글로벌 단계에서 슈퍼포인트-슈퍼픽셀 대응을 설정하고, 기하학적 제약을 통한 포인트 수준의 정밀한 등록을 수행합니다.

- 4. 동적 훈련 메커니즘과 그래디언트 정규화를 사용하여 특징 정렬, 대응 정제, 자세 추정의 손실을 균형 있게 조정합니다.

- 5. CrossI2P는 KITTI Odometry 벤치마크에서 23.7%, nuScenes에서 37.9% 향상된 성능을 보여, 정확성과 견고성을 크게 개선합니다.

---

*Generated on 2025-09-22 14:14:41*