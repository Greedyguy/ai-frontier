---
keywords:
  - Simultaneous Localization and Mapping
  - Visual SLAM
  - Building Information Model
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13972
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:38:29.281462",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Simultaneous Localization and Mapping",
    "Visual SLAM",
    "Building Information Model"
  ],
  "rejected_keywords": [
    "RGB-D SLAM"
  ],
  "similarity_scores": {
    "Simultaneous Localization and Mapping": 0.8,
    "Visual SLAM": 0.75,
    "Building Information Model": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# BIM Informed Visual SLAM for Construction Monitoring

**Korean Title:** 건설 모니터링을 위한 BIM 기반 시각 SLAM

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Simultaneous Localization and Mapping|Simultaneous Localization and Mapping]]
**🔗 Specific Connectable**: [[keywords/Visual SLAM|Visual SLAM]]
**⚡ Unique Technical**: [[keywords/Building Information Model|Building Information Model]]

## 🔗 유사한 논문
- [[MCGS-SLAM_A_Multi-Camera_SLAM_Framework_Using_Gaussian_Splatting_for_High-Fidelity_Mapping_20250918|MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping]] (83.4% similar)
- [[Semantic-Enhanced_Cross-Modal_Place_Recognition_for_Robust_Robot_Localization_20250918|Semantic-Enhanced Cross-Modal Place Recognition for Robust Robot Localization]] (79.4% similar)
- [[Re-purposing SAM into Efficient Visual Projectors for MLLM-Based Referring Image Segmentation]] (77.2% similar)
- [[Search-TTA: A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild]] (77.2% similar)
- [[GeoAware-VLA_Implicit_Geometry_Aware_Vision-Language-Action_Model_20250918|GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model]] (77.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13972v1 Announce Type: new 
Abstract: Simultaneous Localization and Mapping (SLAM) is a key tool for monitoring construction sites, where aligning the evolving as-built state with the as-planned design enables early error detection and reduces costly rework. LiDAR-based SLAM achieves high geometric precision, but its sensors are typically large and power-demanding, limiting their use on portable platforms. Visual SLAM offers a practical alternative with lightweight cameras already embedded in most mobile devices. however, visually mapping construction environments remains challenging: repetitive layouts, occlusions, and incomplete or low-texture structures often cause drift in the trajectory map. To mitigate this, we propose an RGB-D SLAM system that incorporates the Building Information Model (BIM) as structural prior knowledge. Instead of relying solely on visual cues, our system continuously establishes correspondences between detected wall and their BIM counterparts, which are then introduced as constraints in the back-end optimization. The proposed method operates in real time and has been validated on real construction sites, reducing trajectory error by an average of 23.71% and map RMSE by 7.14% compared to visual SLAM baselines. These results demonstrate that BIM constraints enable reliable alignment of the digital plan with the as-built scene, even under partially constructed conditions.

## 🔍 Abstract (한글 번역)

arXiv:2509.13972v1 발표 유형: 새로운
요약: 동시 위치추적 및 지도 작성(SLAM)은 건설 현장 모니터링에 중요한 도구로, 변화하는 실제 상태를 계획된 설계와 일치시켜 초기 오류 감지를 가능하게 하고 비용이 많이 드는 재작업을 줄입니다. LiDAR 기반 SLAM은 높은 기하학적 정밀도를 달성하지만, 그 센서는 일반적으로 크고 전력을 많이 필요로 하기 때문에 휴대용 플랫폼에서의 사용이 제한됩니다. 시각적 SLAM은 대부분의 모바일 장치에 이미 내장된 가벼운 카메라로 실용적인 대안을 제공합니다. 그러나 건설 환경을 시각적으로 매핑하는 것은 여전히 어렵습니다: 반복적인 레이아웃, 가려짐, 불완전하거나 낮은 질감의 구조물은 종종 궤적 지도에서 드리프트를 발생시킵니다. 이를 완화하기 위해, 우리는 건물 정보 모델(BIM)을 구조적 사전 지식으로 통합한 RGB-D SLAM 시스템을 제안합니다. 시각적 단서에만 의존하는 대신, 우리 시스템은 감지된 벽과 그들의 BIM 상대방 사이의 일치를 지속적으로 설정하고, 이를 백엔드 최적화에서 제약 조건으로 도입합니다. 제안된 방법은 실시간으로 작동하며, 실제 건설 현장에서 유효성이 검증되었으며, 시각적 SLAM 기준에 비해 평균 23.71%의 궤적 오차 및 지도 RMSE를 7.14% 줄였습니다. 이러한 결과는 BIM 제약이 부분적으로 건설된 상황에서도 디지털 계획과 실제 상황을 신뢰할 수 있는 방식으로 정렬할 수 있음을 보여줍니다.

## 📝 요약

건설 현장 모니터링을 위한 SLAM 기술은 중요하다. LiDAR 기반 SLAM은 높은 기하학적 정밀도를 제공하지만 대형이고 전력을 많이 필요로 하는 센서로 휴대용 플랫폼에서의 사용이 제한된다. 시각적 SLAM은 경량 카메라를 사용하여 실용적인 대안을 제공한다. 그러나 건설 환경에서의 시각적 맵핑은 도전적이다. 이를 해결하기 위해 우리는 BIM을 구조적 사전 지식으로 활용하는 RGB-D SLAM 시스템을 제안한다. 시스템은 실시간으로 작동하며 실제 건설 현장에서 검증되었으며, 시각적 SLAM과 비교하여 궤적 오차를 평균 23.71%, 맵 RMSE를 7.14% 줄였다. 이러한 결과는 BIM 제약 조건이 디지털 계획과 실제 현장을 신뢰할 수 있게 정렬하는 데 도움이 된다는 것을 보여준다.

## 🎯 주요 포인트

- 1. 건설 현장에서의 SLAM 기술은 건설 계획과 실제 현장을 정확하게 맞추어 오류를 미리 감지하고 비용을 절감하는 데 중요하다.

- 2. LiDAR 기반 SLAM은 높은 기하학적 정밀도를 제공하지만 대형이고 전력을 많이 필요로 하는 센서로 휴대용 플랫폼에서의 사용이 제한된다.

- 3. 건설 환경을 시각적으로 매핑하는 것은 반복적인 레이아웃, 가려짐, 불완전하거나 낮은 질감의 구조물로 인해 도전적이지만, BIM 제약 조건을 활용한 RGB-D SLAM 시스템은 이를 극복할 수 있다.

---

*Generated on 2025-09-18 17:16:29*