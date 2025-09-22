# FloorSAM: SAM-Guided Floorplan Reconstruction with Semantic-Geometric Fusion

**Korean Title:** FloorSAM: 의미-기하학적 융합을 통한 SAM 기반 평면도 재구성

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Semantic-Geometric Fusion

## 🔗 유사한 논문
- [[2025-09-22/CAGE_ Continuity-Aware edGE Network Unlocks Robust Floorplan Reconstruction_20250922|CAGE Continuity-Aware edGE Network Unlocks Robust Floorplan Reconstruction]] (82.5% similar)
- [[2025-09-18/BIM Informed Visual SLAM for Construction Monitoring_20250918|BIM Informed Visual SLAM for Construction Monitoring]] (81.5% similar)
- [[2025-09-19/SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN Layout-guided 3D Indoor Scene Generation]] (79.5% similar)
- [[2025-09-19/Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (79.2% similar)
- [[2025-09-17/LamiGauss_ Pitching Radiative Gaussian for Sparse-View X-ray Laminography Reconstruction_20250917|LamiGauss Pitching Radiative Gaussian for Sparse-View X-ray Laminography Reconstruction]] (78.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15750v1 Announce Type: cross 
Abstract: Reconstructing building floor plans from point cloud data is key for indoor navigation, BIM, and precise measurements. Traditional methods like geometric algorithms and Mask R-CNN-based deep learning often face issues with noise, limited generalization, and loss of geometric details. We propose FloorSAM, a framework that integrates point cloud density maps with the Segment Anything Model (SAM) for accurate floor plan reconstruction from LiDAR data. Using grid-based filtering, adaptive resolution projection, and image enhancement, we create robust top-down density maps. FloorSAM uses SAM's zero-shot learning for precise room segmentation, improving reconstruction across diverse layouts. Room masks are generated via adaptive prompt points and multistage filtering, followed by joint mask and point cloud analysis for contour extraction and regularization. This produces accurate floor plans and recovers room topological relationships. Tests on Giblayout and ISPRS datasets show better accuracy, recall, and robustness than traditional methods, especially in noisy and complex settings. Code and materials: github.com/Silentbarber/FloorSAM.

## 🔍 Abstract (한글 번역)

arXiv:2509.15750v1 발표 유형: 교차  
초록: 포인트 클라우드 데이터로부터 건물 평면도를 재구성하는 것은 실내 내비게이션, BIM, 정밀 측정에 있어 핵심적입니다. 기하학적 알고리즘이나 Mask R-CNN 기반의 딥러닝과 같은 전통적인 방법들은 종종 노이즈, 제한된 일반화, 기하학적 세부사항의 손실과 같은 문제에 직면합니다. 우리는 LiDAR 데이터를 통해 정확한 평면도 재구성을 위해 포인트 클라우드 밀도 맵과 Segment Anything Model (SAM)을 통합한 프레임워크인 FloorSAM을 제안합니다. 그리드 기반 필터링, 적응형 해상도 투영, 이미지 향상을 사용하여 견고한 상단 밀도 맵을 생성합니다. FloorSAM은 SAM의 제로샷 학습을 사용하여 다양한 레이아웃에서 재구성을 개선하는 정확한 방 분할을 수행합니다. 방 마스크는 적응형 프롬프트 포인트와 다단계 필터링을 통해 생성되며, 이후 마스크와 포인트 클라우드의 공동 분석을 통해 윤곽 추출과 정규화를 수행합니다. 이를 통해 정확한 평면도를 생성하고 방의 위상 관계를 복원합니다. Giblayout 및 ISPRS 데이터셋에 대한 테스트 결과, 특히 노이즈가 많고 복잡한 환경에서 전통적인 방법보다 더 나은 정확도, 재현율 및 견고성을 보여줍니다. 코드 및 자료: github.com/Silentbarber/FloorSAM.

## 📝 요약

FloorSAM은 LiDAR 데이터로부터 건물 평면도를 정확하게 재구성하기 위한 새로운 프레임워크입니다. 기존의 기하학적 알고리즘과 딥러닝 방법이 가진 노이즈와 일반화 문제를 해결하기 위해, FloorSAM은 점군 밀도 맵과 Segment Anything Model (SAM)을 통합합니다. 그리드 기반 필터링, 적응형 해상도 투영, 이미지 향상을 통해 강력한 상단 밀도 맵을 생성하며, SAM의 제로샷 학습을 활용해 다양한 레이아웃에서 정밀한 방 분할을 수행합니다. 적응형 프롬프트 포인트와 다단계 필터링을 통해 생성된 방 마스크는 점군 분석과 결합되어 윤곽 추출 및 정규화를 진행합니다. 이로써 정확한 평면도와 방의 위상 관계를 복원합니다. Giblayout 및 ISPRS 데이터셋 테스트 결과, 기존 방법보다 높은 정확도와 회수율을 보이며, 특히 노이즈가 많고 복잡한 환경에서의 강인성을 입증했습니다. 코드와 자료는 GitHub에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. FloorSAM은 LiDAR 데이터를 활용하여 정확한 건물 평면도를 재구성하기 위해 포인트 클라우드 밀도 맵과 Segment Anything Model (SAM)을 통합한 프레임워크입니다.

- 2. 그리드 기반 필터링, 적응형 해상도 투영, 이미지 향상을 통해 강력한 탑다운 밀도 맵을 생성합니다.

- 3. SAM의 제로샷 학습을 활용하여 다양한 레이아웃에서 정밀한 방 분할을 개선합니다.

- 4. 적응형 프롬프트 포인트와 다단계 필터링을 통해 방 마스크를 생성하고, 마스크와 포인트 클라우드 분석을 결합하여 윤곽 추출 및 정규화를 수행합니다.

- 5. Giblayout 및 ISPRS 데이터셋 테스트 결과, 전통적인 방법보다 정확도, 재현율, 강건성에서 우수한 성능을 보였습니다.

---

*Generated on 2025-09-22 14:09:49*