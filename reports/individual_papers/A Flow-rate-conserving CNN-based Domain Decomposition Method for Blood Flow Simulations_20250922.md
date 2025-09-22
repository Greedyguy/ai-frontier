# A Flow-rate-conserving CNN-based Domain Decomposition Method for Blood Flow Simulations

**Korean Title:** 혈류 시뮬레이션을 위한 유량 보존 CNN 기반 영역 분할 방법

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Physics-aware Approach|Physics-aware Approach]] [[keywords/specific/Non-Newtonian Viscosity|Non-Newtonian Viscosity]] [[keywords/broad/Convolutional Neural Network|Convolutional Neural Network]] [[keywords/broad/Domain Decomposition|Domain Decomposition]] [[keywords/unique/Universal Subdomain Solver|Universal Subdomain Solver]] [[categories/cs.LG|cs.LG]] [[2025-09-17/Floating-Body Hydrodynamic Neural Networks_20250917|Floating-Body Hydrodynamic Neural Networks]] (81.8% similar) [[2025-09-22/Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction_20250922|Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction]] (81.2% similar) [[2025-09-22/ChannelFlow-Tools_ A Standardized Dataset Creation Pipeline for 3D Obstructed Channel Flows_20250922|ChannelFlow-Tools: A Standardized Dataset Creation Pipeline for 3D Obstructed Channel Flows]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Physics-aware Approach
**🔗 Specific Connectable**: Non-Newtonian Viscosity
**🔬 Broad Technical**: Convolutional Neural Network, Domain Decomposition
**⭐ Unique Technical**: Universal Subdomain Solver
## 🔗 유사한 논문
- [[2025-09-17/Floating-Body Hydrodynamic Neural Networks_20250917|Floating-Body Hydrodynamic Neural Networks]] (81.8% similar)
- [[2025-09-22/Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction_20250922|Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction]] (81.2% similar)
- [[2025-09-22/ChannelFlow-Tools_ A Standardized Dataset Creation Pipeline for 3D Obstructed Channel Flows_20250922|ChannelFlow-Tools A Standardized Dataset Creation Pipeline for 3D Obstructed Channel Flows]] (80.7% similar)
- [[2025-09-18/Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (80.2% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation Architectural Considerations and Performance Evaluation]] (79.9% similar)


**ArXiv ID**: [2509.15900](https://arxiv.org/abs/2509.15900)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.15900.pdf)


**ArXiv ID**: [2509.15900](https://arxiv.org/abs/2509.15900)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.15900.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Physics-aware Approach
**🔗 Specific Connectable**: Non-Newtonian Viscosity
**⭐ Unique Technical**: Universal Subdomain Solver
**🔬 Broad Technical**: Convolutional Neural Network, Domain Decomposition

## 🏷️ 추출된 키워드



`Convolutional Neural Network` • 

`Domain Decomposition Method` • 

`Universal Subdomain Solver` • 

`Physics-aware Approach`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15900v1 Announce Type: cross 
Abstract: This work aims to predict blood flow with non-Newtonian viscosity in stenosed arteries using convolutional neural network (CNN) surrogate models. An alternating Schwarz domain decomposition method is proposed which uses CNN-based subdomain solvers. A universal subdomain solver (USDS) is trained on a single, fixed geometry and then applied for each subdomain solve in the Schwarz method. Results for two-dimensional stenotic arteries of varying shape and length for different inflow conditions are presented and statistically evaluated. One key finding, when using a limited amount of training data, is the need to implement a USDS which preserves some of the physics, as, in our case, flow rate conservation. A physics-aware approach outperforms purely data-driven USDS, delivering improved subdomain solutions and preventing overshooting or undershooting of the global solution during the Schwarz iterations, thereby leading to more reliable convergence.

## 🔍 Abstract (한글 번역)

arXiv:2509.15900v1 발표 유형: 교차  
초록: 본 연구는 합성곱 신경망(CNN) 대체 모델을 사용하여 협착된 동맥에서 비뉴턴 점성을 가진 혈류를 예측하는 것을 목표로 합니다. CNN 기반의 부분 영역 해법을 사용하는 교대 슈바르츠 영역 분해 방법을 제안합니다. 보편적 부분 영역 해법(USDS)은 단일 고정된 기하학에서 학습되며, 슈바르츠 방법에서 각 부분 영역 해법에 적용됩니다. 다양한 유입 조건에 대한 다양한 형태와 길이의 2차원 협착 동맥에 대한 결과가 제시되고 통계적으로 평가됩니다. 제한된 양의 학습 데이터를 사용할 때의 주요 발견 중 하나는, 물리적 특성을 일부 보존하는 USDS를 구현해야 한다는 점입니다. 우리의 경우, 이는 유량 보존입니다. 물리적 인식을 고려한 접근 방식은 순수하게 데이터 기반의 USDS보다 우수한 성능을 발휘하여, 슈바르츠 반복 과정에서 전역 솔루션의 과도한 증가나 감소를 방지하고, 더 신뢰할 수 있는 수렴을 이끌어냅니다.

## 📝 요약

이 연구는 협착된 동맥에서 비뉴턴 유동성을 가진 혈류를 예측하기 위해 합성곱 신경망(CNN) 대체 모델을 사용하는 방법을 제안합니다. CNN 기반의 부분 영역 해법을 사용하는 교대 슈바르츠 영역 분할 방법을 도입하였으며, 단일 고정된 기하학에서 훈련된 범용 부분 영역 해법(USDS)을 각 부분 영역에 적용했습니다. 다양한 형태와 길이의 2차원 협착 동맥에 대한 결과를 제시하고 통계적으로 평가했습니다. 주요 발견은 제한된 훈련 데이터로 물리적 특성을 보존하는 USDS를 구현해야 한다는 점이며, 이는 순수 데이터 기반 접근법보다 더 나은 결과를 제공합니다. 물리적 인식 접근법은 전역 해법의 과도한 예측을 방지하고, 더 신뢰할 수 있는 수렴을 이끌어냅니다.

## 🎯 주요 포인트


- 1. 비뉴턴 점성을 가진 협착된 동맥의 혈류를 예측하기 위해 CNN 대체 모델을 사용한다.

- 2. CNN 기반의 부분 영역 해석기를 사용하는 교대 슈바르츠 영역 분할 방법을 제안한다.

- 3. 단일 고정된 기하학에서 훈련된 범용 부분 영역 해석기(USDS)를 사용하여 다양한 조건에서 적용한다.

- 4. 물리적 보존을 고려한 USDS가 순수 데이터 기반 접근법보다 우수한 성능을 보인다.

- 5. 물리 인식 접근법은 슈바르츠 반복 과정에서 전역 솔루션의 신뢰할 수 있는 수렴을 보장한다.


---

*Generated on 2025-09-22 15:43:52*