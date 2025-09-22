
# Differential Privacy in Federated Learning: Mitigating Inference Attacks with Randomized Response

**Korean Title:** 페더레이티드 러닝에서의 차별화된 프라이버시: 무작위 응답을 통한 추론 공격 완화

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Ozer Ozturk|Ozer Ozturk]] [[authors/Busra Buyuktanir|Busra Buyuktanir]] [[authors/Gozde Karatas Baydogmus|Gozde Karatas Baydogmus]] [[authors/Kazim Yildiz|Kazim Yildiz]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔬 Broad Technical**: Federated Learning, Differential Privacy

## 🔗 유사한 논문
- [[FedDiverse Tackling Data Heterogeneity in Federated Learning with Diversity-Driven Client Selection]] (83.0% similar)
- [[Federated Learning for Deforestation Detection A Distributed Approach with Satellite Imagery]] (80.0% similar)
- [[Privacy-Aware In-Context Learning for Large Language Models]] (78.3% similar)
- [[Mining the Long Tail A Comparative Study of Data-Centric Criticality Metrics for Robust Offline Reinforcement Learning in Autonomous Motion Planning]] (77.9% similar)
- [[FedSSG Expectation-Gated and History-Aware Drift Alignment for Federated Learning]] (77.9% similar)

## 📋 저자 정보

**Authors:** Ozer Ozturk, Busra Buyuktanir, Gozde Karatas Baydogmus, Kazim Yildiz

## 📄 Abstract (원문)

Machine learning models used for distributed architectures consisting of
servers and clients require large amounts of data to achieve high accuracy.
Data obtained from clients are collected on a central server for model
training. However, storing data on a central server raises concerns about
security and privacy. To address this issue, a federated learning architecture
has been proposed. In federated learning, each client trains a local model
using its own data. The trained models are periodically transmitted to the
central server. The server then combines the received models using federated
aggregation algorithms to obtain a global model. This global model is
distributed back to the clients, and the process continues in a cyclical
manner. Although preventing data from leaving the clients enhances security,
certain concerns still remain. Attackers can perform inference attacks on the
obtained models to approximate the training dataset, potentially causing data
leakage. In this study, differential privacy was applied to address the
aforementioned security vulnerability, and a performance analysis was
conducted. The Data-Unaware Classification Based on Association (duCBA)
algorithm was used as the federated aggregation method. Differential privacy
was implemented on the data using the Randomized Response technique, and the
trade-off between security and performance was examined under different epsilon
values. As the epsilon value decreased, the model accuracy declined, and class
prediction imbalances were observed. This indicates that higher levels of
privacy do not always lead to practical outcomes and that the balance between
security and performance must be carefully considered.

## 🔍 Abstract (한글 번역)

분산 아키텍처를 구성하는 서버 및 클라이언트에 사용되는 기계 학습 모델은 높은 정확도를 달성하기 위해 많은 양의 데이터가 필요합니다. 클라이언트로부터 얻은 데이터는 중앙 서버에서 모델 훈련을 위해 수집됩니다. 그러나 중앙 서버에 데이터를 저장하는 것은 보안 및 개인 정보 보호에 대한 우려를 불러일으킵니다. 이 문제를 해결하기 위해 연합 학습 아키텍처가 제안되었습니다. 연합 학습에서 각 클라이언트는 자체 데이터를 사용하여 로컬 모델을 훈련시킵니다. 훈련된 모델은 주기적으로 중앙 서버로 전송됩니다. 그런 다음 서버는 연합 집계 알고리즘을 사용하여 수신된 모델을 결합하여 전역 모델을 얻습니다. 이 전역 모델은 클라이언트로 분배되고, 프로세스는 주기적으로 계속됩니다. 클라이언트로부터 데이터가 나가지 않도록 하는 것은 보안을 강화하지만 일부 우려 사항이 여전히 남아 있습니다. 공격자는 훈련된 데이터 집합을 근사화하기 위해 획득한 모델에 추론 공격을 수행할 수 있으며, 이로 인해 데이터 누출이 발생할 수 있습니다. 본 연구에서는 상기된 보안 취약점을 해결하기 위해 민감한 개인 정보 보호가 적용되었으며, 성능 분석이 수행되었습니다. 연합 집계 방법으로 데이터-미인식 분류 기반 연합 (duCBA) 알고리즘을 사용했습니다. 민감한 개인 정보 보호는 무작위 응답 기술을 사용하여 데이터에 구현되었으며, 다양한 엡실론 값에서 보안과 성능 사이의 균형을 검토했습니다. 엡실론 값이 낮아질수록 모델 정확도가 감소하고, 클래스 예측 불균형이 관찰되었습니다. 이는 높은 수준의 개인 정보 보호가 항상 실용적인 결과로 이어지지 않으며, 보안과 성능 사이의 균형이 신중하게 고려되어야 함을 나타냅니다.

## 📝 요약

분산 아키텍처를 위해 사용되는 기계 학습 모델은 높은 정확도를 달성하기 위해 많은 양의 데이터가 필요합니다. 그러나 중앙 서버에 데이터를 저장하는 것은 보안과 개인 정보 보호에 대한 우려를 불러일으킵니다. 이를 해결하기 위해 연합 학습 아키텍처가 제안되었습니다. 연합 학습에서 각 클라이언트는 자체 데이터를 사용하여 로컬 모델을 훈련시킵니다. 훈련된 모델은 주기적으로 중앙 서버로 전송되어 연합 집계 알고리즘을 사용하여 전역 모델을 얻습니다. 이 연구에서는 차별적 개인 정보 보호가 적용되었고 성능 분석이 수행되었습니다. duCBA 알고리즘을 사용하여 연합 집계 방법을 적용하였고, 랜덤 응답 기술을 사용하여 데이터에 차별적 개인 정보 보호를 구현하였습니다. 이러한 보안 취약성을 해결하기 위해 다양한 엡실론 값에서 보안과 성능 사이의 균형을 조심스럽게 고려해야 함을 보여주는 성능 분석이 수행되었습니다.

## 🎯 주요 포인트

- 분산 아키텍처를 위해 사용되는 기계 학습 모델은 높은 정확도를 달성하기 위해 많은 양의 데이터가 필요하다.

- 페더레이티드 러닝 아키텍처는 중앙 서버에 데이터를 저장하는 것에 대한 보안 및 개인 정보 보호 우려를 해결하기 위해 제안되었다.

- 민감한 정보 노출을 방지하기 위해 미분적 프라이버시가 적용되었으며, 보안과 성능 사이의 균형을 신중하게 고려해야 한다.

---

*Generated on 2025-09-18 17:05:15*