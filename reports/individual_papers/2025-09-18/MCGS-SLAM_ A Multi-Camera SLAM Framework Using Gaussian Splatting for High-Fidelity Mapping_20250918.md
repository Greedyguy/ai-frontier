
# MCGS-SLAM: A Multi-Camera SLAM Framework Using Gaussian Splatting for High-Fidelity Mapping

**Korean Title:** MCGS-SLAM: 가우시안 스플래팅을 사용한 고품질 매핑을 위한 다중 카메라 SLAM 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Side-view reconstruction

## 🔗 유사한 논문
- [[Gaussian_Alignment_for_Relative_Camera_Pose_Estimation_via_Single-View_Reconstruction_20250918|Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction]] (83.9% similar)
- [[BIM_Informed_Visual_SLAM_for_Construction_Monitoring_20250918|BIM Informed Visual SLAM for Construction Monitoring]] (83.4% similar)
- [[Lightweight_Gradient-Aware_Upscaling_of_3D_Gaussian_Splatting_Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (82.1% similar)
- [[GeoAware-VLA_Implicit_Geometry_Aware_Vision-Language-Action_Model_20250918|GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model]] (81.1% similar)
- [[Semantic-Enhanced_Cross-Modal_Place_Recognition_for_Robust_Robot_Localization_20250918|Semantic-Enhanced Cross-Modal Place Recognition for Robust Robot Localization]] (80.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14191v1 Announce Type: cross 
Abstract: Recent progress in dense SLAM has primarily targeted monocular setups, often at the expense of robustness and geometric coverage. We present MCGS-SLAM, the first purely RGB-based multi-camera SLAM system built on 3D Gaussian Splatting (3DGS). Unlike prior methods relying on sparse maps or inertial data, MCGS-SLAM fuses dense RGB inputs from multiple viewpoints into a unified, continuously optimized Gaussian map. A multi-camera bundle adjustment (MCBA) jointly refines poses and depths via dense photometric and geometric residuals, while a scale consistency module enforces metric alignment across views using low-rank priors. The system supports RGB input and maintains real-time performance at large scale. Experiments on synthetic and real-world datasets show that MCGS-SLAM consistently yields accurate trajectories and photorealistic reconstructions, usually outperforming monocular baselines. Notably, the wide field of view from multi-camera input enables reconstruction of side-view regions that monocular setups miss, critical for safe autonomous operation. These results highlight the promise of multi-camera Gaussian Splatting SLAM for high-fidelity mapping in robotics and autonomous driving.

## 🔍 Abstract (한글 번역)

arXiv:2509.14191v1 발표 유형: 교차
초록: 밀도가 높은 SLAM의 최근 진전은 주로 단안 설정을 대상으로 하였으며 종종 견고성과 기하학적 커버리지를 희생시켰습니다. 우리는 3D 가우시안 스플래팅(3DGS)을 기반으로 한 최초의 순수 RGB 기반 다중 카메라 SLAM 시스템인 MCGS-SLAM을 제안합니다. 희소 지도나 관성 데이터에 의존하는 이전 방법과는 달리, MCGS-SLAM은 여러 시점에서의 밀도가 높은 RGB 입력을 통합된, 지속적으로 최적화된 가우시안 맵으로 융합합니다. 다중 카메라 번들 조정(MCBA)은 밀도가 높은 사진 및 기하학적 잔차를 통해 자세와 깊이를 함께 정제하며, 척도 일관성 모듈은 저랭크 사전을 사용하여 뷰 간의 미터 단위 정렬을 강제합니다. 이 시스템은 RGB 입력을 지원하며 대규모에서 실시간 성능을 유지합니다. 합성 및 실제 데이터셋에서의 실험 결과는 MCGS-SLAM이 일관적으로 정확한 궤적과 사실적인 재구성을 제공하며, 일반적으로 단안 기준을 능가한다는 것을 보여줍니다. 특히, 다중 카메라 입력에서의 넓은 시야는 단안 설정에서 놓치는 측면 영역의 재구성을 가능하게 하여 안전한 자율 운행에 중요합니다. 이러한 결과는 로봇 공학 및 자율 주행을 위한 고품질 매핑을 위한 다중 카메라 가우시안 스플래팅 SLAM의 가능성을 강조합니다.

## 📝 요약

최근 밀도 기반 SLAM 기술은 주로 단안 설정에 초점을 맞추어 왔으며 이는 안정성과 기하학적 범위를 희생시키는 경우가 많았습니다. 본 연구에서는 3D 가우시안 스플래팅(3DGS)을 기반으로 한 최초의 순수 RGB 기반 다중 카메라 SLAM 시스템인 MCGS-SLAM을 제안합니다. 이 시스템은 다중 시점에서의 밀도 높은 RGB 입력을 통합된, 지속적으로 최적화된 가우시안 맵으로 융합합니다. 본 연구에서는 MCBA와 스케일 일관성 모듈을 활용하여 정확한 궤적과 사실적인 재구성을 제공하며, 다중 카메라 입력의 넓은 시야각은 단안 설정에서 놓칠 수 있는 측면 영역의 재구성을 가능케 합니다. 이러한 결과는 다중 카메라 가우시안 스플래팅 SLAM이 로봇 공학 및 자율 주행 분야에서 고품질 매핑을 위한 가능성을 강조합니다.

## 🎯 주요 포인트

- 1. MCGS-SLAM은 3D 가우시안 스플래팅을 기반으로 한 첫 번째 순수 RGB 기반 다중 카메라 SLAM 시스템이다.

- 2. MCBA는 밀도가 높은 광도 및 기하학적 잔차를 통해 자세와 깊이를 함께 개선한다.

- 3. MCGS-SLAM은 다중 카메라 입력의 넓은 시야각을 통해 모노클러 설정에서 놓칠 수 있는 측면 영역의 재구성을 가능케 한다.

---

*Generated on 2025-09-18 17:05:11*