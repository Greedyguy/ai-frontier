# Ideal Registration? Segmentation is All You Need

**Korean Title:** 이상적인 등록? 세분화가 전부입니다

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Segmentation-driven Registration

## 🔗 유사한 논문
- [[2025-09-18/Semi-MoE_ Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation_20250918|Semi-MoE Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (79.6% similar)
- [[2025-09-18/Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model_20250918|Semi-Supervised 3D Medical Segmentation from 2D Natural Images Pretrained Model]] (79.5% similar)
- [[2025-09-19/DiffCut_ Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut_20250919|DiffCut Catalyzing Zero-Shot Semantic Segmentation with Diffusion Features and Recursive Normalized Cut]] (79.4% similar)
- [[2025-09-18/Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows_20250918|Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows]] (79.3% similar)
- [[2025-09-19/Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (78.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15784v1 Announce Type: cross 
Abstract: Deep learning has revolutionized image registration by its ability to handle diverse tasks while achieving significant speed advantages over conventional approaches. Current approaches, however, often employ globally uniform smoothness constraints that fail to accommodate the complex, regionally varying deformations characteristic of anatomical motion. To address this limitation, we propose SegReg, a Segmentation-driven Registration framework that implements anatomically adaptive regularization by exploiting region-specific deformation patterns. Our SegReg first decomposes input moving and fixed images into anatomically coherent subregions through segmentation. These localized domains are then processed by the same registration backbone to compute optimized partial deformation fields, which are subsequently integrated into a global deformation field. SegReg achieves near-perfect structural alignment (98.23% Dice on critical anatomies) using ground-truth segmentation, and outperforms existing methods by 2-12% across three clinical registration scenarios (cardiac, abdominal, and lung images) even with automatic segmentation. Our SegReg demonstrates a near-linear dependence of registration accuracy on segmentation quality, transforming the registration challenge into a segmentation problem. The source code will be released upon manuscript acceptance.

## 🔍 Abstract (한글 번역)

arXiv:2509.15784v1 발표 유형: 교차  
초록: 딥러닝은 다양한 작업을 처리하면서도 기존 방법에 비해 상당한 속도 이점을 제공함으로써 이미지 정합을 혁신적으로 변화시켰습니다. 그러나 현재의 접근법은 종종 전역적으로 균일한 매끄러움 제약을 사용하여 해부학적 움직임의 복잡하고 지역적으로 다양한 변형을 수용하지 못합니다. 이러한 한계를 해결하기 위해, 우리는 SegReg라는 분할 기반 정합 프레임워크를 제안합니다. 이는 지역별 변형 패턴을 활용하여 해부학적으로 적응적인 정규화를 구현합니다. SegReg는 먼저 입력 이동 이미지와 고정 이미지를 분할을 통해 해부학적으로 일관된 하위 영역으로 분해합니다. 이러한 지역화된 도메인은 동일한 정합 백본에 의해 처리되어 최적화된 부분 변형 필드를 계산하며, 이는 이후 전역 변형 필드로 통합됩니다. SegReg는 진실 기반 분할을 사용하여 거의 완벽한 구조적 정렬(중요 해부학에서 98.23% Dice)을 달성하며, 자동 분할을 사용하더라도 세 가지 임상 정합 시나리오(심장, 복부 및 폐 이미지)에서 기존 방법보다 2-12% 더 우수한 성능을 보입니다. 우리의 SegReg는 정합 정확도가 분할 품질에 거의 선형적으로 의존함을 보여주며, 정합 문제를 분할 문제로 변환합니다. 소스 코드는 원고가 승인되면 공개될 예정입니다.

## 📝 요약

이 논문에서는 이미지 등록 문제를 해결하기 위해 SegReg라는 새로운 프레임워크를 제안합니다. 기존 방법들은 전역적으로 균일한 매끄러움 제약을 사용하여 해부학적 움직임의 복잡한 변형을 제대로 반영하지 못하는 한계가 있습니다. SegReg는 해부학적으로 적응적인 정규화를 통해 이러한 문제를 해결합니다. 이 방법은 입력 이미지를 해부학적으로 일관된 하위 영역으로 분할한 후, 각 영역에 대해 최적화된 변형 필드를 계산하여 전체 변형 필드로 통합합니다. SegReg는 중요한 해부학적 구조에서 98.23%의 Dice 점수를 기록하며, 세 가지 임상 시나리오(심장, 복부, 폐 이미지)에서 기존 방법보다 2-12% 더 높은 성능을 보입니다. 이 연구는 등록 정확도가 분할 품질에 거의 선형적으로 의존함을 보여주며, 등록 문제를 분할 문제로 전환합니다. 논문의 소스 코드는 승인 시 공개될 예정입니다.

## 🎯 주요 포인트

- 1. SegReg는 해부학적으로 적응적인 정규화를 구현하여 지역별 변형 패턴을 활용하는 세분화 기반 등록 프레임워크입니다.

- 2. SegReg는 입력 이미지를 해부학적으로 일관된 하위 영역으로 분할하여 부분 변형 필드를 최적화하고 이를 통합하여 전역 변형 필드를 생성합니다.

- 3. SegReg는 구조적 정렬에서 98.23%의 Dice 점수를 기록하며, 자동 세분화에서도 기존 방법보다 2-12% 더 우수한 성능을 보입니다.

- 4. SegReg는 등록 정확도가 세분화 품질에 거의 선형적으로 의존함을 보여주며, 등록 문제를 세분화 문제로 변환합니다.

---

*Generated on 2025-09-22 14:10:32*