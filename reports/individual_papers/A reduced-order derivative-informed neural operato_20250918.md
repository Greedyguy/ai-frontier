
# A reduced-order derivative-informed neural operator for subsurface fluid-flow

**Korean Title:** 지하 유체 흐름을 위한 감소 차수 도함수 정보를 활용한 신경 연산자

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Derivative-based training|Derivative-based training]] [[keywords/broad/Neural operators|Neural operators]] [[keywords/broad/Physics-informed methods|Physics-informed methods]] [[keywords/specific/Fourier neural operators|Fourier neural operators]] [[keywords/unique/DeFINO|DeFINO]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Derivative-based training strategy
**🔬 Broad Technical**: Neural operators, Physics-informed methods
**🔗 Specific Connectable**: Fourier neural operators
**⭐ Unique Technical**: DeFINO

**ArXiv ID**: [2509.13620](https://arxiv.org/abs/2509.13620)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.13620.pdf)


## 🏷️ 추출된 키워드



`Neural operators` • 

`Physics-informed methods` • 

`Permeability inversion` • 

`DeFINO` • 

`Reduced-order training`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13620v1 Announce Type: cross 
Abstract: Neural operators have emerged as cost-effective surrogates for expensive fluid-flow simulators, particularly in computationally intensive tasks such as permeability inversion from time-lapse seismic data, and uncertainty quantification. In these applications, the fidelity of the surrogate's gradients with respect to system parameters is crucial, as the accuracy of downstream tasks, such as optimization and Bayesian inference, relies directly on the quality of the derivative information. Recent advances in physics-informed methods have leveraged derivative information to improve surrogate accuracy. However, incorporating explicit Jacobians can become computationally prohibitive, as the complexity typically scales quadratically with the number of input parameters. To address this limitation, we propose DeFINO (Derivative-based Fisher-score Informed Neural Operator), a reduced-order, derivative-informed training framework. DeFINO integrates Fourier neural operators (FNOs) with a novel derivative-based training strategy guided by the Fisher Information Matrix (FIM). By projecting Jacobians onto dominant eigen-directions identified by the FIM, DeFINO captures critical sensitivity information directly informed by observational data, significantly reducing computational expense. We validate DeFINO through synthetic experiments in the context of subsurface multi-phase fluid-flow, demonstrating improvements in gradient accuracy while maintaining robust forward predictions of underlying fluid dynamics. These results highlight DeFINO's potential to offer practical, scalable solutions for inversion problems in complex real-world scenarios, all at substantially reduced computational cost.

## 🔍 Abstract (한글 번역)

arXiv:2509.13620v1 발표 유형: 교차
요약: 신경 연산자는 특히 시간 경과 지진 데이터로부터 침투성 역전 및 불확실성 양자화와 같은 계산 집중적 작업에서 비용이 많이 드는 유체 흐름 시뮬레이터의 비용 효율적인 대체물로 등장했습니다. 이러한 응용 프로그램에서는 대리자의 그라디언트의 충실성이 시스템 매개 변수에 대한 것이 중요합니다. 최적화 및 베이지안 추론과 같은 하류 작업의 정확도는 직접적으로 도함수 정보의 품질에 의존합니다. 물리학적으로 안내된 방법의 최근 발전은 대리자 정보를 활용하여 대리자의 정확도를 향상시켰습니다. 그러나 명시적인 야코비안을 통합하는 것은 일반적으로 입력 매개 변수의 수에 제곱 비례하여 계산상 금지될 수 있습니다. 이 한계를 해결하기 위해 우리는 DeFINO (Derivative-based Fisher-score Informed Neural Operator)라는 감소 차수, 도함수 정보화된 훈련 프레임워크를 제안합니다. DeFINO는 Fisher 정보 행렬 (FIM)에 의해 안내되는 새로운 도함수 기반 훈련 전략과 푸리에 신경 연산자 (FNOs)를 통합합니다. FIM에 의해 식별된 주요 고유 방향에 야코비안을 투영함으로써 DeFINO는 관측 데이터에 직접 안내되는 중요한 민감도 정보를 포착하여 계산 비용을 크게 줄입니다. 우리는 지하 다상 유체 흐름의 맥락에서 합성 실험을 통해 DeFINO를 검증하고, 기본 유체 역학의 강력한 전방 예측을 유지하면서 그라디언트 정확도를 향상시켜 보여줍니다. 이러한 결과는 DeFINO가 복잡한 현실 시나리오에서 역전 문제에 대한 실용적이고 확장 가능한 솔루션을 제공할 잠재력을 강조하며, 이 모든 것을 상당히 줄인 계산 비용으로 제공할 수 있습니다.

## 📝 요약

최근 물리학적인 방법론의 발전으로 인해 도함수 정보를 활용하여 대체 모델의 정확도를 향상시키는 것이 가능해졌다. 그러나 명시적인 야코비안을 통합하는 것은 계산적으로 어려워질 수 있다. 이 연구에서는 DeFINO (Derivative-based Fisher-score Informed Neural Operator)를 제안하며, 이는 퓨리에 신경 연산자(FNOs)를 활용한 새로운 도함수 기반 훈련 전략을 통해 계산 비용을 크게 줄이면서도 관측 데이터에 의해 직접적으로 영향을 받은 중요한 민감도 정보를 포착한다. 이를 통해 복잡한 실제 시나리오에서 역문제에 대한 실용적이고 확장 가능한 솔루션을 제공할 수 있는 DeFINO의 잠재력을 확인하였다.

## 🎯 주요 포인트


- 1. 신경 연산자는 비용이 많이 드는 유체 흐름 시뮬레이터의 비용 효율적인 대안으로 부상하고 있으며, 특히 시간 경과에 따른 지진 데이터로부터 침투성 역전 및 불확실성 양자화와 같은 계산 집약적인 작업에서 중요하다.

- 2. DeFINO는 퓨리에 신경 연산자(FNOs)를 활용하여 Fisher 정보 행렬(FIM)에 의해 식별된 주요 고유 방향으로 야코비안을 투영하여 관측 데이터에 직접 영향을 받은 중요한 민감도 정보를 캡처함으로써 계산 비용을 크게 줄인다.

- 3. DeFINO는 지하 다상 유체 흐름의 맥락에서 합성 실험을 통해 검증되었으며, 기본적인 유체 역학의 강력한 전방 예측을 유지하면서 기울기 정확도를 향상시킨다.


---

*Generated on 2025-09-18 16:20:30*