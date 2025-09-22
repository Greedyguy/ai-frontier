
# NavMoE: Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts

**Korean Title:** NavMoE: 전문가들의 혼합을 통한 로컬 네비게이션을 위한 하이브리드 모델 및 학습 기반의 트래버서빌리티 추정

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Lazy Gating Mechanism

## 🔗 유사한 논문
- [[Embodied_Navigation_Foundation_Model_20250918|Embodied Navigation Foundation Model]] (84.2% similar)
- [[Ensemble of Pre-Trained Models for Long-Tailed Trajectory Prediction]] (80.5% similar)
- [[Semi-MoE_Mixture-of-Experts_meets_Semi-Supervised_Histopathology_Segmentation_20250918|Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (80.5% similar)
- [[CSMoE_An_Efficient_Remote_Sensing_Foundation_Model_with_Soft_Mixture-of-Experts_20250918|CSMoE: An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (79.5% similar)
- [[MAP: End-to-End Autonomous Driving with Map-Assisted Planning]] (79.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12747v2 Announce Type: replace 
Abstract: This paper explores traversability estimation for robot navigation. A key bottleneck in traversability estimation lies in efficiently achieving reliable and robust predictions while accurately encoding both geometric and semantic information across diverse environments. We introduce Navigation via Mixture of Experts (NAVMOE), a hierarchical and modular approach for traversability estimation and local navigation. NAVMOE combines multiple specialized models for specific terrain types, each of which can be either a classical model-based or a learning-based approach that predicts traversability for specific terrain types. NAVMOE dynamically weights the contributions of different models based on the input environment through a gating network. Overall, our approach offers three advantages: First, NAVMOE enables traversability estimation to adaptively leverage specialized approaches for different terrains, which enhances generalization across diverse and unseen environments. Second, our approach significantly improves efficiency with negligible cost of solution quality by introducing a training-free lazy gating mechanism, which is designed to minimize the number of activated experts during inference. Third, our approach uses a two-stage training strategy that enables the training for the gating networks within the hybrid MoE method that contains nondifferentiable modules. Extensive experiments show that NAVMOE delivers a better efficiency and performance balance than any individual expert or full ensemble across different domains, improving cross-domain generalization and reducing average computational cost by 81.2% via lazy gating, with less than a 2% loss in path quality.

## 🔍 Abstract (한글 번역)

arXiv:2509.12747v2 발표 유형: 대체
요약: 본 논문은 로봇 내비게이션을 위한 횡단 가능성 추정을 탐구한다. 횡단 가능성 추정의 주요 병목은 다양한 환경에서 기하학적 및 의미론적 정보를 정확하게 인코딩하면서 신뢰할 수 있고 견고한 예측을 효율적으로 달성하는 데 있다. 우리는 Navigation via Mixture of Experts (NAVMOE)라는 계층적이고 모듈화된 접근 방식을 소개한다. NAVMOE는 횡단 가능성 추정 및 지역 내비게이션을 위한 여러 특화된 모델을 결합한다. 각 모델은 특정 지형 유형을 위한 횡단 가능성을 예측하는 고전적인 모델 기반 또는 학습 기반 접근 방식 중 하나일 수 있다. NAVMOE는 입력 환경을 통해 다양한 모델의 기여를 동적으로 가중하는 게이팅 네트워크를 통해 모델의 기여를 가중한다. 전반적으로, 우리의 접근 방식은 세 가지 이점을 제공한다. 첫째, NAVMOE는 다양하고 보지 못한 환경을 횡단 가능성 추정을 위해 특화된 접근 방식을 적응적으로 활용할 수 있도록 하여 다양한 환경에서의 일반화를 향상시킨다. 둘째, 우리의 접근 방식은 훈련이 필요 없는 게으른 게이팅 메커니즘을 도입하여 솔루션 품질의 비용을 무시할 정도로 효율성을 크게 향상시킨다. 이 메커니즘은 추론 중에 활성화된 전문가의 수를 최소화하기 위해 설계되었다. 셋째, 우리의 접근 방식은 미분이 불가능한 모듈을 포함하는 혼합 MoE 방법 내에서 게이팅 네트워크의 훈련을 가능하게 하는 두 단계의 훈련 전략을 사용한다. 광범위한 실험 결과 NAVMOE가 다양한 도메인에서 개별 전문가나 전체 앙상블보다 더 나은 효율성과 성능 균형을 제공하며, 게으른 게이팅을 통해 평균 계산 비용을 81.2% 줄이고 경로 품질 손실이 2% 미만임을 보여준다.

## 📝 요약

이 연구는 로봇 내비게이션을 위한 횡단 가능성 추정을 탐구한다. 횡단 가능성 추정의 주요 병목 현상은 다양한 환경에서 기하학적 및 의미론적 정보를 정확하게 인코딩하면서 신뢰할 수 있고 견고한 예측을 효율적으로 달성하는 데 있다. 본 연구에서는 Navigation via Mixture of Experts (NAVMOE)라는 계층적이고 모듈화된 접근 방식을 소개한다. NAVMOE는 특정 지형 유형을 위한 여러 전문 모델을 결합하며, 입력 환경에 따라 다양한 모델의 기여를 동적으로 가중하는 게이팅 네트워크를 통해 횡단 가능성을 예측한다. 실험 결과, NAVMOE는 다양한 도메인에서 개별 전문가나 전체 앙상블보다 더 나은 효율성과 성능 균형을 제공하며, 게으른 게이팅을 통해 평균 계산 비용을 81.2% 줄이고 경로 품질 손실이 2% 미만인 결과를 도출한다.

## 🎯 주요 포인트

- 로봇 내비게이션을 위한 횡단 가능성 추정에 대한 연구

- NAVMOE는 특정 지형 유형에 대한 여러 전문 모델을 결합하여 횡단 가능성을 예측

- NAVMOE는 환경에 따라 다양한 모델의 기여를 동적으로 가중하는 게이팅 네트워크를 사용

- NAVMOE는 경량화된 게이팅 메커니즘을 도입하여 효율성을 향상시키고 계산 비용을 81.2% 줄임

---

*Generated on 2025-09-18 17:21:50*