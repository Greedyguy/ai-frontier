# Bayesian Physics Informed Neural Networks for Reliable Transformer Prognostics

**Korean Title:** 베이지안 물리학 기반 신경망을 활용한 신뢰할 수 있는 변압기 예측 모델 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Probabilistic Prognostics Estimation

## 🔗 유사한 논문
- [[2025-09-19/Evidential Physics-Informed Neural Networks for Scientific Discovery_20250919|Evidential Physics-Informed Neural Networks for Scientific Discovery]] (88.0% similar)
- [[2025-09-17/A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks_20250917|A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks]] (84.1% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks A Second-Order Optimization Perspective]] (81.9% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (81.6% similar)
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (80.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15933v1 Announce Type: new 
Abstract: Scientific Machine Learning (SciML) integrates physics and data into the learning process, offering improved generalization compared with purely data-driven models. Despite its potential, applications of SciML in prognostics remain limited, partly due to the complexity of incorporating partial differential equations (PDEs) for ageing physics and the scarcity of robust uncertainty quantification methods. This work introduces a Bayesian Physics-Informed Neural Network (B-PINN) framework for probabilistic prognostics estimation. By embedding Bayesian Neural Networks into the PINN architecture, the proposed approach produces principled, uncertainty-aware predictions. The method is applied to a transformer ageing case study, where insulation degradation is primarily driven by thermal stress. The heat diffusion PDE is used as the physical residual, and different prior distributions are investigated to examine their impact on predictive posterior distributions and their ability to encode a priori physical knowledge. The framework is validated against a finite element model developed and tested with real measurements from a solar power plant. Results, benchmarked against a dropout-PINN baseline, show that the proposed B-PINN delivers more reliable prognostic predictions by accurately quantifying predictive uncertainty. This capability is crucial for supporting robust and informed maintenance decision-making in critical power assets.

## 🔍 Abstract (한글 번역)

arXiv:2509.15933v1 발표 유형: 신규  
초록: 과학적 기계 학습(SciML)은 물리학과 데이터를 학습 과정에 통합하여 순수하게 데이터 기반 모델에 비해 일반화 능력을 향상시킵니다. 그 잠재력에도 불구하고, SciML의 예측학 분야에서의 응용은 제한적입니다. 이는 부분 미분 방정식(PDE)을 노화 물리학에 통합하는 복잡성과 강력한 불확실성 정량화 방법의 부족 때문입니다. 본 연구는 확률론적 예측 추정을 위한 베이지안 물리 기반 신경망(B-PINN) 프레임워크를 소개합니다. 베이지안 신경망을 PINN 아키텍처에 내장하여 제안된 접근법은 원칙적이고 불확실성 인식 예측을 제공합니다. 이 방법은 변압기 노화 사례 연구에 적용되며, 여기서 절연체 열화는 주로 열 스트레스에 의해 유발됩니다. 물리적 잔차로서 열 확산 PDE가 사용되며, 다양한 사전 분포를 조사하여 예측 후분포에 미치는 영향과 사전 물리적 지식을 인코딩하는 능력을 검토합니다. 이 프레임워크는 태양광 발전소에서의 실제 측정값으로 개발 및 테스트된 유한 요소 모델과 비교하여 검증되었습니다. 드롭아웃-PINN 기준선과 비교한 결과, 제안된 B-PINN은 예측 불확실성을 정확하게 정량화하여 보다 신뢰할 수 있는 예측 결과를 제공합니다. 이 능력은 중요한 전력 자산에서 강력하고 정보에 입각한 유지보수 의사 결정을 지원하는 데 필수적입니다.

## 📝 요약

이 논문은 과학적 기계 학습(SciML)을 활용하여 물리학과 데이터를 통합한 학습 과정을 통해 일반화를 개선하는 방법을 제안합니다. 특히, 노화 물리학을 설명하는 편미분 방정식(PDE)을 포함하는 복잡성과 불확실성 정량화 방법의 부족으로 인해 SciML의 예측적 활용이 제한되어 왔습니다. 본 연구에서는 베이지안 물리 기반 신경망(B-PINN) 프레임워크를 도입하여 확률적 예측을 수행합니다. 이 방법은 변압기 노화 사례 연구에 적용되며, 열 확산 PDE를 물리적 잔차로 사용하여 절연체 열화 예측을 수행합니다. 실험 결과, 제안된 B-PINN은 예측 불확실성을 정확히 정량화하여 기존의 dropout-PINN보다 더 신뢰할 수 있는 예측을 제공하며, 이는 전력 자산의 유지보수 의사결정에 중요한 기여를 합니다.

## 🎯 주요 포인트

- 1. SciML은 물리학과 데이터를 통합하여 순수 데이터 기반 모델보다 일반화 성능을 향상시킵니다.

- 2. Bayesian Physics-Informed Neural Network (B-PINN) 프레임워크는 불확실성을 고려한 예측을 제공합니다.

- 3. 제안된 방법은 변압기 노화 사례 연구에 적용되어 열 스트레스로 인한 절연 열화를 예측합니다.

- 4. 다양한 사전 분포를 조사하여 예측 후분포와 물리적 지식의 사전 인코딩 능력을 평가합니다.

- 5. B-PINN은 드롭아웃-PINN과 비교하여 예측 불확실성을 정확히 정량화하여 더 신뢰할 수 있는 예측을 제공합니다.

---

*Generated on 2025-09-22 15:27:49*