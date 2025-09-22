# ToFU: Transforming How Federated Learning Systems Forget User Data

**Korean Title:** ToFU: 연합 학습 시스템이 사용자 데이터를 잊는 방식을 변혁하다

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Learning-to-unlearn

## 🔗 유사한 논문
- [[2025-09-18/CUFG_ Curriculum Unlearning Guided by the Forgetting Gradient_20250918|CUFG Curriculum Unlearning Guided by the Forgetting Gradient]] (85.5% similar)
- [[2025-09-22/Pre-Forgettable Models_ Prompt Learning as a Native Mechanism for Unlearning_20250922|Pre-Forgettable Models Prompt Learning as a Native Mechanism for Unlearning]] (82.5% similar)
- [[2025-09-17/Differential Privacy in Federated Learning_ Mitigating Inference Attacks with Randomized Response_20250917|Differential Privacy in Federated Learning Mitigating Inference Attacks with Randomized Response]] (79.7% similar)
- [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release Iterative LLM Unlearning with Self-generated Data]] (79.7% similar)
- [[2025-09-19/Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (79.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15861v1 Announce Type: new 
Abstract: Neural networks unintentionally memorize training data, creating privacy risks in federated learning (FL) systems, such as inference and reconstruction attacks on sensitive data. To mitigate these risks and to comply with privacy regulations, Federated Unlearning (FU) has been introduced to enable participants in FL systems to remove their data's influence from the global model. However, current FU methods primarily act post-hoc, struggling to efficiently erase information deeply memorized by neural networks. We argue that effective unlearning necessitates a paradigm shift: designing FL systems inherently amenable to forgetting. To this end, we propose a learning-to-unlearn Transformation-guided Federated Unlearning (ToFU) framework that incorporates transformations during the learning process to reduce memorization of specific instances. Our theoretical analysis reveals how transformation composition provably bounds instance-specific information, directly simplifying subsequent unlearning. Crucially, ToFU can work as a plug-and-play framework that improves the performance of existing FU methods. Experiments on CIFAR-10, CIFAR-100, and the MUFAC benchmark show that ToFU outperforms existing FU baselines, enhances performance when integrated with current methods, and reduces unlearning time.

## 🔍 Abstract (한글 번역)

arXiv:2509.15861v1 발표 유형: 신규  
초록: 신경망은 의도치 않게 훈련 데이터를 암기하여, 민감한 데이터에 대한 추론 및 재구성 공격과 같은 연합 학습(FL) 시스템에서 프라이버시 위험을 초래합니다. 이러한 위험을 완화하고 프라이버시 규정을 준수하기 위해, 연합 학습 시스템의 참가자들이 글로벌 모델에서 자신의 데이터 영향을 제거할 수 있도록 하는 연합 잊기(FU)가 도입되었습니다. 그러나 현재의 FU 방법은 주로 사후적으로 작용하여 신경망에 깊이 암기된 정보를 효율적으로 지우는 데 어려움을 겪고 있습니다. 우리는 효과적인 잊기가 패러다임 전환을 필요로 한다고 주장합니다: 잊기에 본질적으로 적합한 FL 시스템 설계. 이를 위해, 특정 인스턴스의 암기를 줄이기 위해 학습 과정에서 변환을 통합하는 학습-잊기 변환 안내 연합 잊기(ToFU) 프레임워크를 제안합니다. 우리의 이론적 분석은 변환 구성이 인스턴스별 정보를 어떻게 증명 가능하게 제한하는지를 밝혀내며, 이는 후속 잊기를 직접적으로 단순화합니다. 중요한 것은, ToFU는 기존 FU 방법의 성능을 향상시키는 플러그 앤 플레이 프레임워크로 작동할 수 있습니다. CIFAR-10, CIFAR-100, MUFAC 벤치마크에 대한 실험은 ToFU가 기존 FU 기준선을 능가하고, 현재 방법과 통합될 때 성능을 향상시키며, 잊기 시간을 줄이는 것을 보여줍니다.

## 📝 요약

이 논문은 연합 학습(FL) 시스템에서 발생하는 프라이버시 위험을 줄이기 위해 제안된 연합 잊기(FU) 방법론을 개선합니다. 기존 FU 방법은 사후적으로 작용하여 신경망에 깊이 각인된 정보를 효율적으로 제거하는 데 한계가 있습니다. 이를 해결하기 위해, 학습 과정에서 특정 데이터의 암기를 줄이는 변환을 도입한 ToFU(Transformation-guided Federated Unlearning) 프레임워크를 제안합니다. 이 방법은 이론적으로 인스턴스별 정보를 제한하여 잊기 과정을 단순화하며, 기존 FU 방법의 성능을 향상시키는 플러그 앤 플레이 방식으로 작동합니다. CIFAR-10, CIFAR-100 및 MUFAC 벤치마크 실험에서 ToFU는 기존 FU 방법보다 뛰어난 성능을 보였고, 잊기 시간을 단축시켰습니다.

## 🎯 주요 포인트

- 1. 신경망은 훈련 데이터를 무의식적으로 기억하여 연합 학습 시스템에서 개인정보 침해 위험을 초래할 수 있습니다.

- 2. 연합 학습 시스템에서 참가자가 자신의 데이터 영향을 제거할 수 있도록 하는 Federated Unlearning(FU)이 도입되었습니다.

- 3. 기존 FU 방법은 주로 사후적으로 작용하여 신경망에 깊이 기억된 정보를 효율적으로 지우는 데 어려움을 겪습니다.

- 4. ToFU(Transformation-guided Federated Unlearning) 프레임워크는 학습 과정에서 변환을 통합하여 특정 인스턴스의 기억을 줄이는 방법을 제안합니다.

- 5. ToFU는 기존 FU 방법의 성능을 향상시키고, 실험 결과 CIFAR-10, CIFAR-100, MUFAC 벤치마크에서 우수한 성능을 보였습니다.

---

*Generated on 2025-09-22 15:26:49*