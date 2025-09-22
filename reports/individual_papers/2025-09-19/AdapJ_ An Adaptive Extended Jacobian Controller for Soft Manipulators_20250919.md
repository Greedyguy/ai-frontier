
# AdapJ: An Adaptive Extended Jacobian Controller for Soft Manipulators

**Korean Title:** AdapJ: 연성 매니퓰레이터를 위한 적응형 확장 야코비안 제어기

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive Control Mechanism

## 🔗 유사한 논문
- [[ActivePusher Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (81.4% similar)
- [[Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning_20250919|Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning]] (79.5% similar)
- [[MIMIC-D Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (79.3% similar)
- [[M4Diffuser Multi-View Diffusion Policy with Manipulability-Aware Control for Robust Mobile Manipulation]] (79.2% similar)
- [[Embracing Bulky Objects with Humanoid Robots Whole-Body Manipulation with Reinforcement Learning]] (78.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2406.04094v3 Announce Type: replace 
Abstract: The nonlinearity and hysteresis of soft robot motions present challenges for control. To solve these issues, the Jacobian controller has been applied to approximate the nonlinear behaviors in a linear format. Accurate controllers like neural networks can handle delayed and nonlinear motions, but they require large datasets and exhibit low adaptability. Based on a novel analysis on these controllers, we propose an adaptive extended Jacobian controller, AdapJ, for soft manipulators. This controller retains the concise format of the Jacobian controller but introduces independent parameters. Similar to neural networks, its initialization and updating mechanism leverages the inverse model without building the corresponding forward model. In the experiments, we first compare the performance of the Jacobian controller, model predictive controller, neural network controller, iterative feedback controller, and AdapJ in simulation. We further analyze how AdapJ parameters adapt in response to the physical property change. Then, real-world experiments have validated that AdapJ outperforms the neural network controller, model predictive controller, and iterative feedback controller with fewer training samples and adapts robustly to varying conditions, including different control frequencies, material softness, and external disturbances. Future work may include online adjustment of the controller format and adaptability validation in more scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2406.04094v3 발표 유형: 교체  
초록: 소프트 로봇의 움직임에서 나타나는 비선형성과 히스테리시스는 제어에 있어 도전 과제를 제시합니다. 이러한 문제를 해결하기 위해, 야코비안 컨트롤러가 비선형 동작을 선형 형식으로 근사하기 위해 적용되었습니다. 신경망과 같은 정확한 컨트롤러는 지연된 비선형 동작을 처리할 수 있지만, 대규모 데이터셋이 필요하고 적응성이 낮습니다. 이러한 컨트롤러에 대한 새로운 분석을 바탕으로, 우리는 소프트 매니퓰레이터를 위한 적응형 확장 야코비안 컨트롤러인 AdapJ를 제안합니다. 이 컨트롤러는 야코비안 컨트롤러의 간결한 형식을 유지하면서 독립적인 매개변수를 도입합니다. 신경망과 유사하게, 초기화 및 업데이트 메커니즘은 해당 순방향 모델을 구축하지 않고 역 모델을 활용합니다. 실험에서는 시뮬레이션에서 야코비안 컨트롤러, 모델 예측 컨트롤러, 신경망 컨트롤러, 반복 피드백 컨트롤러, 그리고 AdapJ의 성능을 비교합니다. 우리는 또한 AdapJ 매개변수가 물리적 특성 변화에 어떻게 적응하는지를 분석합니다. 그런 다음, 실제 실험을 통해 AdapJ가 신경망 컨트롤러, 모델 예측 컨트롤러, 반복 피드백 컨트롤러보다 적은 훈련 샘플로 우수한 성능을 발휘하며, 다양한 조건, 즉 서로 다른 제어 주파수, 재료의 부드러움, 외부 방해에 강력하게 적응함을 검증했습니다. 향후 연구는 컨트롤러 형식의 온라인 조정 및 더 많은 시나리오에서의 적응성 검증을 포함할 수 있습니다.

## 📝 요약

이 논문은 소프트 로봇의 비선형성과 이력 현상 문제를 해결하기 위해 적응형 확장 야코비안 컨트롤러(AdapJ)를 제안합니다. AdapJ는 야코비안 컨트롤러의 간결한 형식을 유지하면서 독립적인 매개변수를 도입하여 초기화 및 업데이트 메커니즘을 역 모델을 통해 수행합니다. 실험 결과, AdapJ는 적은 데이터로도 신경망, 모델 예측, 반복 피드백 컨트롤러보다 우수한 성능을 보이며, 다양한 조건 변화에 강인하게 적응합니다. 향후 연구에서는 컨트롤러 형식의 온라인 조정 및 다양한 시나리오에서의 적응성 검증이 포함될 예정입니다.

## 🎯 주요 포인트

- 1. 소프트 로봇의 비선형성과 히스테리시스를 해결하기 위해 Jacobian 컨트롤러가 비선형 동작을 선형 형식으로 근사하는 데 사용되었습니다.

- 2. AdapJ라는 적응형 확장 Jacobian 컨트롤러를 제안하여 독립적인 매개변수를 도입하고, 초기화 및 업데이트 메커니즘에서 역 모델을 활용합니다.

- 3. 실험 결과, AdapJ는 적은 훈련 샘플로 다양한 조건에 강건하게 적응하며, 신경망 컨트롤러, 모델 예측 컨트롤러, 반복 피드백 컨트롤러보다 우수한 성능을 보였습니다.

- 4. AdapJ는 물리적 특성 변화에 대한 매개변수 적응을 통해 소프트 매니퓰레이터의 제어 성능을 향상시킵니다.

- 5. 향후 연구에서는 컨트롤러 형식의 온라인 조정 및 다양한 시나리오에서의 적응성 검증이 포함될 수 있습니다.

---

*Generated on 2025-09-19 16:37:07*