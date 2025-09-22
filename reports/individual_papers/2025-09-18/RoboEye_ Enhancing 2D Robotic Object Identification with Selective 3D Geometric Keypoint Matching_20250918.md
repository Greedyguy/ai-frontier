# RoboEye: Enhancing 2D Robotic Object Identification with Selective 3D Geometric Keypoint Matching

**Korean Title:** RoboEye: 선택적 3D 기하학적 키포인트 매칭을 통한 2D 로봇 객체 식별 향상

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Xingwu Zhang|Xingwu Zhang]] [[authors/Guanxuan Li|Guanxuan Li]] [[authors/Zhuocheng Zhang|Zhuocheng Zhang]] [[authors/Zijun Long|Zijun Long]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: 3D Geometric Keypoint Matching

## 🔗 유사한 논문
- [[PRISM_ Product Retrieval In Shopping Carts using Hybrid Matching_20250919|PRISM Product Retrieval In Shopping Carts using Hybrid Matching]] (82.1% similar)
- [[Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (80.9% similar)
- [[Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (80.7% similar)
- [[Object Recognition and Force Estimation with the GelSight Baby Fin Ray_20250919|Object Recognition and Force Estimation with the GelSight Baby Fin Ray]] (80.6% similar)
- [[Seeing 3D Through 2D Lenses_ 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification_20250919|Seeing 3D Through 2D Lenses 3D Few-Shot Class-Incremental Learning via Cross-Modal Geometric Rectification]] (80.4% similar)

## 📋 저자 정보

**Authors:** Xingwu Zhang, Guanxuan Li, Zhuocheng Zhang, Zijun Long

## 📄 Abstract (원문)

The rapidly growing number of product categories in large-scale e-commerce
makes accurate object identification for automated packing in warehouses
substantially more difficult. As the catalog grows, intra-class variability and
a long tail of rare or visually similar items increase, and when combined with
diverse packaging, cluttered containers, frequent occlusion, and large
viewpoint changes-these factors amplify discrepancies between query and
reference images, causing sharp performance drops for methods that rely solely
on 2D appearance features. Thus, we propose RoboEye, a two-stage identification
framework that dynamically augments 2D semantic features with domain-adapted 3D
reasoning and lightweight adapters to bridge training deployment gaps. In the
first stage, we train a large vision model to extract 2D features for
generating candidate rankings. A lightweight 3D-feature-awareness module then
estimates 3D feature quality and predicts whether 3D re-ranking is necessary,
preventing performance degradation and avoiding unnecessary computation. When
invoked, the second stage uses our robot 3D retrieval transformer, comprising a
3D feature extractor that produces geometry-aware dense features and a
keypoint-based matcher that computes keypoint-correspondence confidences
between query and reference images instead of conventional cosine-similarity
scoring. Experiments show that RoboEye improves Recall@1 by 7.1% over the prior
state of the art (RoboLLM). Moreover, RoboEye operates using only RGB images,
avoiding reliance on explicit 3D inputs and reducing deployment costs. The code
used in this paper is publicly available at:
https://github.com/longkukuhi/RoboEye.

## 🔍 Abstract (한글 번역)

대규모 전자상거래에서 제품 카테고리의 급속한 증가는 창고에서 자동 포장을 위한 정확한 객체 식별을 상당히 어렵게 만듭니다. 카탈로그가 확장됨에 따라 클래스 내 변동성과 희귀하거나 시각적으로 유사한 항목의 긴 꼬리가 증가하고, 다양한 포장, 혼잡한 컨테이너, 빈번한 가림, 큰 시점 변화와 결합될 때, 이러한 요소들은 쿼리 이미지와 참조 이미지 간의 불일치를 증폭시켜 2D 외형 특징에만 의존하는 방법의 성능을 급격히 떨어뜨립니다. 따라서 우리는 RoboEye라는 두 단계 식별 프레임워크를 제안하며, 이는 도메인 적응 3D 추론과 경량 어댑터를 사용하여 2D 의미론적 특징을 동적으로 보강하여 훈련과 배포 간의 격차를 해소합니다. 첫 번째 단계에서는 대규모 비전 모델을 훈련하여 후보 순위를 생성하기 위한 2D 특징을 추출합니다. 경량 3D 특징 인식 모듈은 3D 특징 품질을 추정하고 3D 재순위가 필요한지를 예측하여 성능 저하를 방지하고 불필요한 계산을 피합니다. 호출될 경우, 두 번째 단계에서는 우리의 로봇 3D 검색 변환기를 사용하며, 이는 기하학적으로 인식하는 밀집 특징을 생성하는 3D 특징 추출기와 쿼리 이미지와 참조 이미지 간의 키포인트 대응 신뢰도를 계산하는 키포인트 기반 매처로 구성됩니다. 실험 결과, RoboEye는 이전 최첨단 기술(RoboLLM) 대비 Recall@1을 7.1% 향상시킵니다. 게다가, RoboEye는 RGB 이미지만을 사용하여 명시적인 3D 입력에 대한 의존을 피하고 배포 비용을 줄입니다. 이 논문에서 사용된 코드는 다음에서 공개적으로 제공됩니다: https://github.com/longkukuhi/RoboEye.

## 📝 요약

RoboEye는 대규모 전자상거래 환경에서 자동 포장 시스템의 객체 식별 정확도를 향상시키기 위한 이단계 식별 프레임워크입니다. 첫 번째 단계에서는 대형 비전 모델을 통해 2D 특징을 추출하여 후보 순위를 생성하고, 경량 3D 특징 인식 모듈이 3D 재순위 필요성을 예측합니다. 두 번째 단계에서는 3D 특징 추출기와 키포인트 기반 매처를 사용하여 질의 이미지와 참조 이미지 간의 키포인트 대응 신뢰도를 계산합니다. 실험 결과, RoboEye는 이전 최첨단 기술(RoboLLM) 대비 Recall@1을 7.1% 향상시켰으며, RGB 이미지만을 사용하여 3D 입력에 대한 의존성을 줄여 배포 비용을 절감합니다.

## 🎯 주요 포인트

- 1. 대규모 전자상거래의 제품 카테고리 증가로 인해 창고에서의 자동 포장용 객체 식별이 더욱 어려워지고 있습니다.

- 2. RoboEye는 2D 외관 특징에만 의존하는 방법의 성능 저하를 방지하기 위해 3D 추론과 경량 어댑터를 활용하는 두 단계 식별 프레임워크를 제안합니다.

- 3. 첫 번째 단계에서는 대형 비전 모델을 훈련시켜 2D 특징을 추출하고, 3D 특징 인식 모듈이 3D 재랭킹 필요성을 예측하여 불필요한 계산을 피합니다.

- 4. 두 번째 단계에서는 로봇 3D 검색 변환기를 사용하여 기하학적 밀집 특징을 생성하고, 쿼리와 참조 이미지 간의 키포인트 대응 신뢰도를 계산합니다.

- 5. 실험 결과, RoboEye는 이전 최첨단 기술(RoboLLM) 대비 Recall@1을 7.1% 개선하였으며, RGB 이미지만 사용하여 배포 비용을 절감합니다.

---

*Generated on 2025-09-20 01:40:18*