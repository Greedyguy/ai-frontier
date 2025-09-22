# Interpretable Network-assisted Random Forest+

**Korean Title:** 해석 가능한 네트워크 지원 랜덤 포레스트+

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Interpretable Network-assisted Models

## 🔗 유사한 논문
- [[2025-09-22/Adversarial generalization of unfolding (model-based) networks_20250922|Adversarial generalization of unfolding (model-based) networks]] (81.5% similar)
- [[2025-09-19/Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (80.9% similar)
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation Architectural Considerations and Performance Evaluation]] (80.0% similar)
- [[2025-09-18/Learning Graph from Smooth Signals under Partial Observation_ A Robustness Analysis_20250918|Learning Graph from Smooth Signals under Partial Observation A Robustness Analysis]] (79.1% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (79.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15611v1 Announce Type: cross 
Abstract: Machine learning algorithms often assume that training samples are independent. When data points are connected by a network, the induced dependency between samples is both a challenge, reducing effective sample size, and an opportunity to improve prediction by leveraging information from network neighbors. Multiple methods taking advantage of this opportunity are now available, but many, including graph neural networks, are not easily interpretable, limiting their usefulness for understanding how a model makes its predictions. Others, such as network-assisted linear regression, are interpretable but often yield substantially worse prediction performance. We bridge this gap by proposing a family of flexible network-assisted models built upon a generalization of random forests (RF+), which achieves highly-competitive prediction accuracy and can be interpreted through feature importance measures. In particular, we develop a suite of interpretation tools that enable practitioners to not only identify important features that drive model predictions, but also quantify the importance of the network contribution to prediction. Importantly, we provide both global and local importance measures as well as sample influence measures to assess the impact of a given observation. This suite of tools broadens the scope and applicability of network-assisted machine learning for high-impact problems where interpretability and transparency are essential.

## 🔍 Abstract (한글 번역)

arXiv:2509.15611v1 발표 유형: 교차  
초록: 기계 학습 알고리즘은 종종 훈련 샘플이 독립적이라고 가정합니다. 데이터 포인트가 네트워크로 연결되어 있을 때, 샘플 간의 유도된 종속성은 효과적인 샘플 크기를 감소시키는 도전 과제이자 네트워크 이웃의 정보를 활용하여 예측을 개선할 수 있는 기회가 됩니다. 이 기회를 활용하는 여러 방법이 현재 이용 가능하지만, 그래프 신경망을 포함한 많은 방법은 쉽게 해석할 수 없어 모델이 예측을 수행하는 방식을 이해하는 데 유용성이 제한됩니다. 반면에 네트워크 지원 선형 회귀와 같은 다른 방법은 해석 가능하지만 종종 예측 성능이 크게 떨어집니다. 우리는 랜덤 포레스트의 일반화를 기반으로 하는 유연한 네트워크 지원 모델 군(RF+)을 제안하여 이 격차를 해소하고, 경쟁력 있는 예측 정확도를 달성하며 특징 중요도 측정을 통해 해석할 수 있습니다. 특히, 우리는 실무자들이 모델 예측을 이끄는 중요한 특징을 식별할 수 있을 뿐만 아니라, 예측에 대한 네트워크 기여의 중요성을 정량화할 수 있는 해석 도구 모음을 개발했습니다. 중요한 것은, 우리는 주어진 관찰의 영향을 평가하기 위한 전역 및 지역 중요도 측정치뿐만 아니라 샘플 영향 측정치를 제공합니다. 이 도구 모음은 해석 가능성과 투명성이 필수적인 고영향 문제에 대한 네트워크 지원 기계 학습의 범위와 적용성을 넓힙니다.

## 📝 요약

이 논문은 네트워크로 연결된 데이터에서 샘플 간의 의존성을 활용하여 예측 성능을 향상시키는 방법을 제안합니다. 기존의 그래프 신경망은 해석이 어려운 반면, 네트워크 보조 선형 회귀는 예측 성능이 낮은 문제를 해결하기 위해, 해석 가능하면서도 높은 예측 정확도를 제공하는 랜덤 포레스트(RF+) 기반의 유연한 네트워크 보조 모델을 개발했습니다. 이 모델은 특징 중요도 측정을 통해 모델 예측에 기여하는 주요 특징과 네트워크의 기여도를 정량화할 수 있는 해석 도구를 제공합니다. 이러한 도구는 전반적 및 개별 샘플의 중요도를 평가할 수 있어, 해석 가능성과 투명성이 중요한 문제에 네트워크 보조 머신러닝의 적용 범위를 넓힙니다.

## 🎯 주요 포인트

- 1. 네트워크로 연결된 데이터 포인트 간의 의존성은 샘플 크기를 줄이는 도전이자, 네트워크 이웃의 정보를 활용하여 예측을 개선할 수 있는 기회입니다.

- 2. 그래프 신경망을 포함한 여러 방법은 해석이 어려워 모델의 예측 방식을 이해하는 데 한계가 있습니다.

- 3. 네트워크 보조 선형 회귀와 같은 방법은 해석 가능하지만 예측 성능이 떨어지는 경우가 많습니다.

- 4. RF+라는 랜덤 포레스트 일반화를 기반으로 유연한 네트워크 보조 모델을 제안하여 높은 예측 정확도를 달성하고, 특징 중요도 측정을 통해 해석할 수 있습니다.

- 5. 제안된 도구는 모델 예측에 중요한 특징을 식별하고, 네트워크 기여도의 중요성을 정량화하며, 글로벌 및 로컬 중요도와 샘플 영향력을 제공하여 해석 가능성을 높입니다.

---

*Generated on 2025-09-22 15:40:18*