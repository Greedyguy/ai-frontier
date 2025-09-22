# CBPNet: A Continual Backpropagation Prompt Network for Alleviating Plasticity Loss on Edge Devices

**Korean Title:** CBPNet: 엣지 디바이스에서 가소성 손실을 완화하기 위한 지속적 역전파 프롬프트 네트워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Plasticity Loss Mitigation

## 🔗 유사한 논문
- [[2025-09-18/HAM_ Hierarchical Adapter Merging for Scalable Continual Learning_20250918|HAM Hierarchical Adapter Merging for Scalable Continual Learning]] (81.5% similar)
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (81.3% similar)
- [[2025-09-19/PMPO_ Probabilistic Metric Prompt Optimization for Small and Large Language Models_20250919|PMPO Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (81.2% similar)
- [[2025-09-22/Pre-Forgettable Models_ Prompt Learning as a Native Mechanism for Unlearning_20250922|Pre-Forgettable Models Prompt Learning as a Native Mechanism for Unlearning]] (80.9% similar)
- [[2025-09-18/CUFG_ Curriculum Unlearning Guided by the Forgetting Gradient_20250918|CUFG Curriculum Unlearning Guided by the Forgetting Gradient]] (80.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15785v1 Announce Type: cross 
Abstract: To meet the demands of applications like robotics and autonomous driving that require real-time responses to dynamic environments, efficient continual learning methods suitable for edge devices have attracted increasing attention. In this transition, using frozen pretrained models with prompts has become a mainstream strategy to combat catastrophic forgetting. However, this approach introduces a new critical bottleneck: plasticity loss, where the model's ability to learn new knowledge diminishes due to the frozen backbone and the limited capacity of prompt parameters. We argue that the reduction in plasticity stems from a lack of update vitality in underutilized parameters during the training process. To this end, we propose the Continual Backpropagation Prompt Network (CBPNet), an effective and parameter efficient framework designed to restore the model's learning vitality. We innovatively integrate an Efficient CBP Block that counteracts plasticity decay by adaptively reinitializing these underutilized parameters. Experimental results on edge devices demonstrate CBPNet's effectiveness across multiple benchmarks. On Split CIFAR-100, it improves average accuracy by over 1% against a strong baseline, and on the more challenging Split ImageNet-R, it achieves a state of the art accuracy of 69.41%. This is accomplished by training additional parameters that constitute less than 0.2% of the backbone's size, validating our approach.

## 🔍 Abstract (한글 번역)

arXiv:2509.15785v1 발표 유형: 교차  
초록: 로봇 공학 및 자율 주행과 같은 동적 환경에 대한 실시간 응답이 필요한 응용 프로그램의 요구를 충족하기 위해 엣지 장치에 적합한 효율적인 연속 학습 방법이 점점 더 많은 관심을 받고 있습니다. 이 전환 과정에서, 프롬프트와 함께 고정된 사전 학습 모델을 사용하는 것이 망각 문제를 해결하기 위한 주류 전략이 되었습니다. 그러나 이 접근법은 모델의 새로운 지식을 학습하는 능력이 고정된 백본과 제한된 프롬프트 파라미터 용량으로 인해 감소하는 플라스틱성 손실이라는 새로운 중요한 병목 현상을 초래합니다. 우리는 플라스틱성 감소가 훈련 과정에서 활용되지 않은 파라미터의 업데이트 활력 부족에서 비롯된다고 주장합니다. 이를 위해, 우리는 모델의 학습 활력을 회복하기 위해 설계된 효과적이고 파라미터 효율적인 프레임워크인 연속 역전파 프롬프트 네트워크(CBPNet)를 제안합니다. 우리는 이러한 활용되지 않은 파라미터를 적응적으로 재초기화하여 플라스틱성 감소를 방지하는 효율적인 CBP 블록을 혁신적으로 통합했습니다. 엣지 장치에서의 실험 결과는 여러 벤치마크에서 CBPNet의 효과를 입증합니다. Split CIFAR-100에서 강력한 기준선 대비 평균 정확도를 1% 이상 향상시키고, 더 도전적인 Split ImageNet-R에서는 69.41%의 최첨단 정확도를 달성합니다. 이는 백본 크기의 0.2% 미만을 차지하는 추가 파라미터를 훈련함으로써 달성되며, 우리의 접근법을 검증합니다.

## 📝 요약

이 논문은 로봇공학과 자율주행과 같은 실시간 응답이 필요한 응용 분야를 위해 엣지 디바이스에 적합한 효율적인 지속 학습 방법을 제안합니다. 기존의 프롬프트를 사용하는 고정된 사전 학습 모델은 망각 문제를 해결하지만, 새로운 지식을 학습하는 능력인 가소성이 감소하는 문제를 야기합니다. 이를 해결하기 위해, 저자는 Continual Backpropagation Prompt Network (CBPNet)를 제안하여 모델의 학습 활력을 회복시키고자 합니다. CBPNet은 비효율적으로 사용되는 매개변수를 적응적으로 재초기화하는 효율적인 CBP 블록을 통합하여 가소성 감소를 방지합니다. 실험 결과, CBPNet은 여러 벤치마크에서 효과적임을 입증했으며, Split CIFAR-100에서 평균 정확도를 1% 이상 향상시키고, Split ImageNet-R에서는 69.41%의 최첨단 정확도를 달성했습니다. 이는 백본 크기의 0.2% 미만의 추가 매개변수를 학습하여 이루어졌습니다.

## 🎯 주요 포인트

- 1. 로봇공학 및 자율주행과 같은 실시간 응답이 필요한 애플리케이션을 위해 엣지 디바이스에 적합한 효율적인 지속 학습 방법이 주목받고 있습니다.

- 2. 프롬프트를 사용하는 고정된 사전 학습 모델은 망각 문제를 해결하는 주류 전략이지만, 이는 모델의 새로운 지식 학습 능력이 감소하는 가소성 손실이라는 문제를 야기합니다.

- 3. 가소성 감소는 훈련 과정에서 활용되지 않는 매개변수의 업데이트 활력 부족에서 비롯된다고 주장합니다.

- 4. CBPNet은 비효율적으로 사용되는 매개변수를 적응적으로 재초기화하여 가소성 감소를 방지하는 효율적인 CBP 블록을 통합하여 모델의 학습 활력을 복원합니다.

- 5. CBPNet은 Split CIFAR-100 및 Split ImageNet-R에서 각각 1% 이상의 평균 정확도 향상과 69.41%의 최첨단 정확도를 달성하며, 이는 백본 크기의 0.2% 미만의 추가 매개변수를 학습시켜 검증되었습니다.

---

*Generated on 2025-09-22 14:10:59*