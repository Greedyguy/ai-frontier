# ThermalGuardian: Temperature-Aware Testing of Automotive Deep Learning Frameworks

**Korean Title:** 열수호자: 자동차 딥러닝 프레임워크의 온도 인식 테스트

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Temperature-Sensitive Operators

## 🔗 유사한 논문
- [[2025-09-19/Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization_20250919|Towards Robust Agentic CUDA Kernel Benchmarking, Verification, and Optimization]] (78.8% similar)
- [[2025-09-19/MetaTrading_ An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services_20250919|MetaTrading An Immersion-Aware Model Trading Framework for Vehicular Metaverse Services]] (77.8% similar)
- [[2025-09-19/DINAMO_ Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments_20250919|DINAMO Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments]] (77.6% similar)
- [[2025-09-19/STEP_ Structured Training and Evaluation Platform for benchmarking trajectory prediction models_20250919|STEP Structured Training and Evaluation Platform for benchmarking trajectory prediction models]] (77.5% similar)
- [[2025-09-17/Physics-based deep kernel learning for parameter estimation in high dimensional PDEs_20250917|Physics-based deep kernel learning for parameter estimation in high dimensional PDEs]] (77.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15815v1 Announce Type: new 
Abstract: Deep learning models play a vital role in autonomous driving systems, supporting critical functions such as environmental perception. To accelerate model inference, these deep learning models' deployment relies on automotive deep learning frameworks, for example, PaddleInference in Apollo and TensorRT in AutoWare. However, unlike deploying deep learning models on the cloud, vehicular environments experience extreme ambient temperatures varying from -40{\deg}C to 50{\deg}C, significantly impacting GPU temperature. Additionally, heats generated when computing further lead to the GPU temperature increase. These temperature fluctuations lead to dynamic GPU frequency adjustments through mechanisms such as DVFS. However, automotive deep learning frameworks are designed without considering the impact of temperature-induced frequency variations. When deployed on temperature-varying GPUs, these frameworks suffer critical quality issues: compute-intensive operators face delays or errors, high/mixed-precision operators suffer from precision errors, and time-series operators suffer from synchronization issues. The above quality issues cannot be detected by existing deep learning framework testing methods because they ignore temperature's effect on the deep learning framework quality. To bridge this gap, we propose ThermalGuardian, the first automotive deep learning framework testing method under temperature-varying environments. Specifically, ThermalGuardian generates test input models using model mutation rules targeting temperature-sensitive operators, simulates GPU temperature fluctuations based on Newton's law of cooling, and controls GPU frequency based on real-time GPU temperature.

## 🔍 Abstract (한글 번역)

arXiv:2509.15815v1 발표 유형: 신규  
초록: 딥러닝 모델은 자율 주행 시스템에서 환경 인식과 같은 중요한 기능을 지원하며 중요한 역할을 합니다. 모델 추론을 가속화하기 위해, 이러한 딥러닝 모델의 배포는 예를 들어 Apollo의 PaddleInference와 AutoWare의 TensorRT와 같은 자동차 딥러닝 프레임워크에 의존합니다. 그러나 클라우드에서 딥러닝 모델을 배포하는 것과 달리, 차량 환경은 -40°C에서 50°C까지 변동하는 극한의 주변 온도를 경험하며, 이는 GPU 온도에 상당한 영향을 미칩니다. 또한, 계산 시 발생하는 열은 GPU 온도를 더욱 증가시킵니다. 이러한 온도 변동은 DVFS와 같은 메커니즘을 통해 동적인 GPU 주파수 조정을 초래합니다. 그러나 자동차 딥러닝 프레임워크는 온도 유발 주파수 변동의 영향을 고려하지 않고 설계되었습니다. 온도가 변동하는 GPU에 배포될 때, 이러한 프레임워크는 중요한 품질 문제를 겪습니다: 계산 집약적인 연산자는 지연이나 오류가 발생하고, 고정밀/혼합 정밀 연산자는 정밀도 오류가 발생하며, 시계열 연산자는 동기화 문제를 겪습니다. 기존의 딥러닝 프레임워크 테스트 방법은 온도가 딥러닝 프레임워크 품질에 미치는 영향을 무시하기 때문에 위의 품질 문제를 감지할 수 없습니다. 이러한 격차를 해소하기 위해, 우리는 온도 변동 환경에서 최초의 자동차 딥러닝 프레임워크 테스트 방법인 ThermalGuardian을 제안합니다. 구체적으로, ThermalGuardian은 온도 민감 연산자를 대상으로 하는 모델 변이 규칙을 사용하여 테스트 입력 모델을 생성하고, 뉴턴의 냉각 법칙에 기반하여 GPU 온도 변동을 시뮬레이션하며, 실시간 GPU 온도에 기반하여 GPU 주파수를 제어합니다.

## 📝 요약

이 논문은 자율 주행 시스템에서 중요한 역할을 하는 딥러닝 모델의 온도 변화에 따른 성능 문제를 해결하기 위해 ThermalGuardian을 제안합니다. 기존의 자동차 딥러닝 프레임워크는 온도 변화에 따른 GPU 주파수 변동을 고려하지 않아 품질 문제가 발생합니다. ThermalGuardian은 모델 변이 규칙을 사용해 온도에 민감한 연산자를 테스트하고, 뉴턴의 냉각 법칙을 기반으로 GPU 온도 변화를 시뮬레이션하며, 실시간 GPU 온도에 따라 주파수를 조절합니다. 이를 통해 온도 변화 환경에서의 딥러닝 프레임워크 테스트를 가능하게 합니다.

## 🎯 주요 포인트

- 1. 자율주행 시스템에서 딥러닝 모델은 환경 인식과 같은 중요한 기능을 지원하며, 이러한 모델의 추론 가속화를 위해 자동차 딥러닝 프레임워크가 사용된다.

- 2. 차량 환경에서는 -40°C에서 50°C까지 극단적인 온도 변화가 발생하며, 이는 GPU 온도에 큰 영향을 미친다.

- 3. 온도 변화로 인해 GPU 주파수가 동적으로 조정되지만, 기존 자동차 딥러닝 프레임워크는 이러한 온도 유발 주파수 변화를 고려하지 않아 품질 문제를 겪는다.

- 4. ThermalGuardian은 온도 변화 환경에서 자동차 딥러닝 프레임워크를 테스트하기 위한 최초의 방법으로, 온도 민감 연산자를 대상으로 모델 변이 규칙을 사용하여 테스트 입력 모델을 생성한다.

- 5. ThermalGuardian은 뉴턴 냉각 법칙을 기반으로 GPU 온도 변동을 시뮬레이션하고, 실시간 GPU 온도에 따라 GPU 주파수를 제어한다.

---

*Generated on 2025-09-22 15:24:25*