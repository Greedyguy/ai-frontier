# Inference Offloading for Cost-Sensitive Binary Classification at the Edge

**Korean Title:** 엣지에서 비용 민감형 이진 분류를 위한 추론 오프로딩

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Online Learning Framework

## 🔗 유사한 논문
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (82.5% similar)
- [[2025-09-19/Online reinforcement learning via sparse Gaussian mixture model Q-functions_20250919|Online reinforcement learning via sparse Gaussian mixture model Q-functions]] (80.6% similar)
- [[2025-09-18/Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (80.4% similar)
- [[2025-09-18/Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (80.2% similar)
- [[2025-09-19/Reinforcement Learning Agent for a 2D Shooter Game_20250919|Reinforcement Learning Agent for a 2D Shooter Game]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15674v1 Announce Type: cross 
Abstract: We focus on a binary classification problem in an edge intelligence system where false negatives are more costly than false positives. The system has a compact, locally deployed model, which is supplemented by a larger, remote model, which is accessible via the network by incurring an offloading cost. For each sample, our system first uses the locally deployed model for inference. Based on the output of the local model, the sample may be offloaded to the remote model. This work aims to understand the fundamental trade-off between classification accuracy and these offloading costs within such a hierarchical inference (HI) system. To optimize this system, we propose an online learning framework that continuously adapts a pair of thresholds on the local model's confidence scores. These thresholds determine the prediction of the local model and whether a sample is classified locally or offloaded to the remote model. We present a closed-form solution for the setting where the local model is calibrated. For the more general case of uncalibrated models, we introduce H2T2, an online two-threshold hierarchical inference policy, and prove it achieves sublinear regret. H2T2 is model-agnostic, requires no training, and learns in the inference phase using limited feedback. Simulations on real-world datasets show that H2T2 consistently outperforms naive and single-threshold HI policies, sometimes even surpassing offline optima. The policy also demonstrates robustness to distribution shifts and adapts effectively to mismatched classifiers.

## 🔍 Abstract (한글 번역)

arXiv:2509.15674v1 발표 유형: 교차  
초록: 우리는 엣지 인텔리전스 시스템에서 이진 분류 문제를 다루며, 여기서 false negative가 false positive보다 더 비용이 많이 듭니다. 이 시스템은 소형의 로컬에 배치된 모델과 네트워크를 통해 접근할 수 있는 더 큰 원격 모델로 구성되어 있으며, 이는 오프로딩 비용을 수반합니다. 각 샘플에 대해, 시스템은 먼저 로컬에 배치된 모델을 사용하여 추론을 수행합니다. 로컬 모델의 출력에 따라 샘플은 원격 모델로 오프로딩될 수 있습니다. 이 연구는 이러한 계층적 추론(HI) 시스템 내에서 분류 정확도와 오프로딩 비용 간의 근본적인 균형을 이해하는 것을 목표로 합니다. 이 시스템을 최적화하기 위해, 우리는 로컬 모델의 신뢰도 점수에 대한 두 개의 임계값을 지속적으로 조정하는 온라인 학습 프레임워크를 제안합니다. 이 임계값은 로컬 모델의 예측과 샘플이 로컬에서 분류될지 원격 모델로 오프로딩될지를 결정합니다. 로컬 모델이 보정된 설정에 대한 닫힌 형식의 솔루션을 제시합니다. 보정되지 않은 모델의 보다 일반적인 경우에 대해, 우리는 H2T2라는 온라인 이중 임계값 계층적 추론 정책을 소개하고, 이것이 서브리니어 후회를 달성함을 증명합니다. H2T2는 모델에 구애받지 않으며, 훈련이 필요 없고, 제한된 피드백을 사용하여 추론 단계에서 학습합니다. 실제 데이터셋에 대한 시뮬레이션은 H2T2가 일관되게 단순하고 단일 임계값 HI 정책을 능가하며, 때로는 오프라인 최적값을 초과하기도 한다는 것을 보여줍니다. 이 정책은 분포 변화에 대한 강건성을 보여주며, 잘못된 분류기에 효과적으로 적응합니다.

## 📝 요약

이 논문은 엣지 인텔리전스 시스템에서 이진 분류 문제를 다루며, 특히 거짓 부정의 비용이 거짓 긍정보다 큰 상황을 고려합니다. 시스템은 로컬 모델과 네트워크를 통해 접근 가능한 원격 모델로 구성됩니다. 각 샘플은 먼저 로컬 모델로 예측되며, 필요시 원격 모델로 전송됩니다. 본 연구는 분류 정확도와 오프로드 비용 간의 균형을 이해하고 최적화하기 위해 온라인 학습 프레임워크를 제안합니다. 로컬 모델의 신뢰도 점수에 기반한 두 개의 임계값을 지속적으로 조정하여 샘플의 처리 방식을 결정합니다. 보정된 모델의 경우 폐쇄형 해를 제시하고, 비보정 모델에 대해서는 H2T2라는 온라인 이중 임계값 정책을 도입하여 서브리니어 후회를 달성함을 증명합니다. H2T2는 모델에 구애받지 않고, 훈련 없이 제한된 피드백을 통해 학습합니다. 실제 데이터셋 시뮬레이션 결과, H2T2는 단순한 정책보다 우수한 성능을 보이며, 분포 변화에 강건하고 분류기 불일치에도 효과적으로 적응합니다.

## 🎯 주요 포인트

- 1. 엣지 인텔리전스 시스템에서 이진 분류 문제를 다루며, 거짓 음성의 비용이 거짓 양성보다 더 큰 상황을 고려합니다.

- 2. 계층적 추론 시스템에서 분류 정확도와 오프로딩 비용 간의 근본적인 트레이드오프를 이해하고자 합니다.

- 3. 로컬 모델의 신뢰도 점수에 기반한 두 개의 임계값을 지속적으로 조정하는 온라인 학습 프레임워크를 제안합니다.

- 4. H2T2는 모델 비종속적이며, 학습 없이 제한된 피드백을 통해 추론 단계에서 학습합니다.

- 5. H2T2는 실세계 데이터셋 시뮬레이션에서 강력한 성능을 보이며, 분포 변화에 대한 강건성과 잘못된 분류기에 대한 적응력을 입증합니다.

---

*Generated on 2025-09-22 14:07:48*