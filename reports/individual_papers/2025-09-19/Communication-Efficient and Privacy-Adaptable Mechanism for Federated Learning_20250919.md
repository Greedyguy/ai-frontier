
# Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning

**Korean Title:** 연합 학습을 위한 통신 효율적이고 프라이버시 적응 가능한 메커니즘

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Privacy Adaptability

## 🔗 유사한 논문
- [[Who to Trust_ Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust Aggregating Client Knowledge in Logit-Based Federated Learning]] (83.7% similar)
- [[The Sum Leaks More Than Its Parts Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (82.0% similar)
- [[FedDiverse Tackling Data Heterogeneity in Federated Learning with Diversity-Driven Client Selection]] (81.1% similar)
- [[CSMoE An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (80.5% similar)
- [[Hierarchical_Federated_Learning_for_Social_Network_with_Mobility_20250919|Hierarchical Federated Learning for Social Network with Mobility]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.12046v2 Announce Type: replace 
Abstract: Training machine learning models on decentralized private data via federated learning (FL) poses two key challenges: communication efficiency and privacy protection. In this work, we address these challenges within the trusted aggregator model by introducing a novel approach called the Communication-Efficient and Privacy-Adaptable Mechanism (CEPAM), achieving both objectives simultaneously. In particular, CEPAM leverages the rejection-sampled universal quantizer (RSUQ), a construction of randomized vector quantizer whose resulting distortion is equivalent to a prescribed noise, such as Gaussian or Laplace noise, enabling joint differential privacy and compression. Our CEPAM provides the additional benefit of privacy adaptability, allowing clients and the server to customize privacy protection based on required accuracy and protection. We theoretically analyze the privacy guarantee of CEPAM and investigate the trade-offs among user privacy and accuracy of CEPAM through experimental evaluations. Moreover, we assess CEPAM's utility performance using MNIST dataset, demonstrating that CEPAM surpasses baseline models in terms of learning accuracy.

## 🔍 Abstract (한글 번역)

arXiv:2501.12046v2 발표 유형: 교체  
초록: 연합 학습(FL)을 통해 분산된 개인 데이터를 기반으로 기계 학습 모델을 훈련하는 것은 두 가지 주요 과제인 통신 효율성과 프라이버시 보호를 제기합니다. 본 연구에서는 신뢰할 수 있는 집계자 모델 내에서 이러한 과제를 해결하기 위해 통신 효율적이고 프라이버시 적응 가능한 메커니즘(CEPAM)이라는 새로운 접근 방식을 도입하여 두 가지 목표를 동시에 달성합니다. 특히, CEPAM은 거부 샘플링된 범용 양자화기(RSUQ)를 활용하는데, 이는 결과적인 왜곡이 가우시안 또는 라플라스 잡음과 같은 규정된 잡음과 동등한 랜덤 벡터 양자화기의 구성으로, 차별적 프라이버시와 압축을 동시에 가능하게 합니다. 우리의 CEPAM은 추가적으로 프라이버시 적응성을 제공하여, 클라이언트와 서버가 요구되는 정확도와 보호 수준에 따라 프라이버시 보호를 맞춤화할 수 있도록 합니다. 우리는 CEPAM의 프라이버시 보장을 이론적으로 분석하고, 실험적 평가를 통해 사용자 프라이버시와 CEPAM의 정확도 간의 상충 관계를 조사합니다. 또한, MNIST 데이터셋을 사용하여 CEPAM의 유틸리티 성능을 평가하고, CEPAM이 학습 정확도 측면에서 기준 모델을 능가함을 입증합니다.

## 📝 요약

이 논문은 신뢰할 수 있는 집계자 모델에서 연합 학습(FL)의 통신 효율성과 프라이버시 보호 문제를 해결하기 위해 새로운 접근법인 CEPAM(Communication-Efficient and Privacy-Adaptable Mechanism)을 제안합니다. CEPAM은 RSUQ(거부 샘플링된 범용 양자화기)를 활용하여 차등 프라이버시와 데이터 압축을 동시에 달성합니다. 이 메커니즘은 프라이버시 적응성을 제공하여 클라이언트와 서버가 정확도와 보호 수준에 따라 프라이버시를 조정할 수 있게 합니다. 이론적 분석과 실험을 통해 CEPAM의 프라이버시 보장과 정확도 간의 상충 관계를 평가하고, MNIST 데이터셋을 사용한 실험에서 CEPAM이 기존 모델보다 학습 정확도가 우수함을 입증합니다.

## 🎯 주요 포인트

- 1. 본 연구는 신뢰할 수 있는 집계 모델에서 통신 효율성과 프라이버시 보호를 동시에 달성하는 새로운 접근법인 CEPAM을 제안합니다.

- 2. CEPAM은 RSUQ를 활용하여 차별적 프라이버시와 데이터 압축을 동시에 가능하게 합니다.

- 3. CEPAM은 프라이버시 적응성을 제공하여 클라이언트와 서버가 정확도와 보호 요구에 따라 프라이버시 보호를 조정할 수 있게 합니다.

- 4. 이론적 분석을 통해 CEPAM의 프라이버시 보장을 확인하고, 실험을 통해 사용자 프라이버시와 정확도 간의 균형을 조사합니다.

- 5. MNIST 데이터셋을 사용한 실험에서 CEPAM은 학습 정확도 면에서 기존 모델들을 능가하는 성능을 보였습니다.

---

*Generated on 2025-09-19 15:38:56*