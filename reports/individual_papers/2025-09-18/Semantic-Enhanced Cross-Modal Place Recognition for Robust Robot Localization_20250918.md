
# Semantic-Enhanced Cross-Modal Place Recognition for Robust Robot Localization

**Korean Title:** 로봇의 견고한 로봇 위치 결정을 위한 의미 강화된 교차 모달 장소 인식

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-View Semantic-Geometric Matching

## 🔗 유사한 논문
- [[FSR-VLN_Fast_and_Slow_Reasoning_for_Vision-Language_Navigation_with_Hierarchical_Multi-modal_Scene_Graph_20250918|FSR-VLN: Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph]] (81.1% similar)
- [[InterKey_Cross-modal_Intersection_Keypoints_for_Global_Localization_on_OpenStreetMap_20250918|InterKey: Cross-modal Intersection Keypoints for Global Localization on OpenStreetMap]] (80.6% similar)
- [[MCGS-SLAM_A_Multi-Camera_SLAM_Framework_Using_Gaussian_Splatting_for_High-Fidelity_Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (80.4% similar)
- [[Search-TTA: A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild]] (80.4% similar)
- [[BIM_Informed_Visual_SLAM_for_Construction_Monitoring_20250918|BIM Informed Visual SLAM for Construction Monitoring]] (79.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13474v1 Announce Type: new 
Abstract: Ensuring accurate localization of robots in environments without GPS capability is a challenging task. Visual Place Recognition (VPR) techniques can potentially achieve this goal, but existing RGB-based methods are sensitive to changes in illumination, weather, and other seasonal changes. Existing cross-modal localization methods leverage the geometric properties of RGB images and 3D LiDAR maps to reduce the sensitivity issues highlighted above. Currently, state-of-the-art methods struggle in complex scenes, fine-grained or high-resolution matching, and situations where changes can occur in viewpoint. In this work, we introduce a framework we call Semantic-Enhanced Cross-Modal Place Recognition (SCM-PR) that combines high-level semantics utilizing RGB images for robust localization in LiDAR maps. Our proposed method introduces: a VMamba backbone for feature extraction of RGB images; a Semantic-Aware Feature Fusion (SAFF) module for using both place descriptors and segmentation masks; LiDAR descriptors that incorporate both semantics and geometry; and a cross-modal semantic attention mechanism in NetVLAD to improve matching. Incorporating the semantic information also was instrumental in designing a Multi-View Semantic-Geometric Matching and a Semantic Consistency Loss, both in a contrastive learning framework. Our experimental work on the KITTI and KITTI-360 datasets show that SCM-PR achieves state-of-the-art performance compared to other cross-modal place recognition methods.

## 🔍 Abstract (한글 번역)

arXiv:2509.13474v1 발표 유형: 새로운
요약: GPS 기능이 없는 환경에서 로봇의 정확한 위치 지정을 보장하는 것은 어려운 과제입니다. 시각적 장소 인식(VPR) 기술은 이 목표를 달성할 수 있지만, 기존의 RGB 기반 방법은 조명, 날씨 및 계절 변화에 민감합니다. 기존의 교차 모달 로컬라이제이션 방법은 RGB 이미지와 3D LiDAR 지도의 기하학적 특성을 활용하여 위에서 강조한 민감성 문제를 줄입니다. 현재 최첨단 기술은 복잡한 장면, 미세한 또는 고해상도 매칭, 그리고 시점 변경이 발생할 수 있는 상황에서 어려움을 겪습니다. 본 연구에서는 우리가 Semantic-Enhanced Cross-Modal Place Recognition (SCM-PR)라고 부르는 프레임워크를 소개합니다. 이는 LiDAR 지도에서 강력한 위치 지정을 위해 RGB 이미지를 활용하는 고수준 의미론을 결합합니다. 우리의 제안된 방법은 다음을 도입합니다: RGB 이미지의 특징 추출을 위한 VMamba 백본; 장소 설명자와 분할 마스크를 모두 사용하는 Semantic-Aware Feature Fusion (SAFF) 모듈; 의미론과 기하학을 모두 포함하는 LiDAR 설명자; 그리고 일치를 개선하기 위한 NetVLAD의 교차 모달 의미주의 메커니즘. 의미 정보를 통합하는 것은 대조적 학습 프레임워크에서 Multi-View Semantic-Geometric Matching 및 Semantic Consistency Loss를 설계하는 데 중요한 역할을 했습니다. KITTI 및 KITTI-360 데이터셋에서의 실험 결과는 SCM-PR이 다른 교차 모달 장소 인식 방법과 비교하여 최첨단 성능을 달성한다는 것을 보여줍니다.

## 📝 요약

로봇의 정확한 위치 인식은 GPS 기능이 없는 환경에서 어려운 과제이다. 시각적 장소 인식(VPR) 기술은 이 목표를 달성할 수 있지만 기존의 RGB 기반 방법은 조명, 날씨 및 계절 변화에 민감하다. 본 연구에서는 RGB 이미지의 고수준 의미론을 활용하여 LiDAR 지도에서 강력한 로봇 위치 인식을 위한 Semantic-Enhanced Cross-Modal Place Recognition (SCM-PR) 프레임워크를 제안한다. VMamba 백본, Semantic-Aware Feature Fusion 모듈, LiDAR 설명자 및 NetVLAD의 교차 모달 의미주의 주의 메커니즘을 도입하여 상태-오브-더-아트 방법보다 우수한 성능을 보였다.

## 🎯 주요 포인트

- 로봇의 정확한 위치 지정은 GPS 기능이 없는 환경에서 어려운 과제이다.

- 기존 RGB 기반 방법은 조명, 날씨 및 계절 변화에 민감하다.

- SCM-PR은 RGB 이미지의 고수준 의미론을 활용하여 LiDAR 지도에서 강력한 위치 지정을 결합한다.

- SCM-PR은 다른 교차 모달 위치 인식 방법과 비교하여 최고 수준의 성능을 달성한다.

---

*Generated on 2025-09-18 16:58:23*