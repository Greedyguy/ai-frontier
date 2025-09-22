# Pre-Forgettable Models: Prompt Learning as a Native Mechanism for Unlearning

**Korean Title:** 잊기 전 모델: 학습 해제를 위한 본질적 메커니즘으로서의 프롬프트 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Built-in Unlearning

## 🔗 유사한 논문
- [[2025-09-18/CUFG_ Curriculum Unlearning Guided by the Forgetting Gradient_20250918|CUFG Curriculum Unlearning Guided by the Forgetting Gradient]] (85.6% similar)
- [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release Iterative LLM Unlearning with Self-generated Data]] (83.9% similar)
- [[2025-09-19/Towards a Real-World Aligned Benchmark for Unlearning in Recommender Systems_20250919|Towards a Real-World Aligned Benchmark for Unlearning in Recommender Systems]] (83.0% similar)
- [[2025-09-17/Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning_20250917|Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning]] (82.9% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (79.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15230v1 Announce Type: cross 
Abstract: Foundation models have transformed multimedia analysis by enabling robust and transferable representations across diverse modalities and tasks. However, their static deployment conflicts with growing societal and regulatory demands -- particularly the need to unlearn specific data upon request, as mandated by privacy frameworks such as the GDPR. Traditional unlearning approaches, including retraining, activation editing, or distillation, are often computationally expensive, fragile, and ill-suited for real-time or continuously evolving systems. In this paper, we propose a paradigm shift: rethinking unlearning not as a retroactive intervention but as a built-in capability. We introduce a prompt-based learning framework that unifies knowledge acquisition and removal within a single training phase. Rather than encoding information in model weights, our approach binds class-level semantics to dedicated prompt tokens. This design enables instant unlearning simply by removing the corresponding prompt -- without retraining, model modification, or access to original data. Experiments demonstrate that our framework preserves predictive performance on retained classes while effectively erasing forgotten ones. Beyond utility, our method exhibits strong privacy and security guarantees: it is resistant to membership inference attacks, and prompt removal prevents any residual knowledge extraction, even under adversarial conditions. This ensures compliance with data protection principles and safeguards against unauthorized access to forgotten information, making the framework suitable for deployment in sensitive and regulated environments. Overall, by embedding removability into the architecture itself, this work establishes a new foundation for designing modular, scalable and ethically responsive AI models.

## 🔍 Abstract (한글 번역)

arXiv:2509.15230v1 발표 유형: 교차  
초록: 기초 모델은 다양한 모달리티와 작업 전반에 걸쳐 강력하고 전이 가능한 표현을 가능하게 함으로써 멀티미디어 분석을 혁신했습니다. 그러나 이러한 모델의 정적 배포는 특히 GDPR과 같은 개인정보 보호 프레임워크에 의해 요청 시 특정 데이터를 잊어야 하는 요구 사항과 같은 증가하는 사회적 및 규제적 요구와 충돌합니다. 재훈련, 활성화 편집 또는 증류와 같은 전통적인 잊기 접근법은 종종 계산 비용이 많이 들고, 취약하며, 실시간 또는 지속적으로 진화하는 시스템에 적합하지 않습니다. 이 논문에서는 잊기를 사후 개입이 아닌 내장된 기능으로 재구성하는 패러다임 전환을 제안합니다. 우리는 지식 획득과 제거를 단일 훈련 단계 내에서 통합하는 프롬프트 기반 학습 프레임워크를 소개합니다. 정보가 모델 가중치에 인코딩되는 대신, 우리의 접근법은 클래스 수준의 의미를 전용 프롬프트 토큰에 바인딩합니다. 이 설계는 재훈련, 모델 수정, 원본 데이터 접근 없이 해당 프롬프트를 제거함으로써 즉각적인 잊기를 가능하게 합니다. 실험 결과, 우리의 프레임워크는 유지된 클래스에 대한 예측 성능을 유지하면서도 잊힌 클래스는 효과적으로 삭제함을 보여줍니다. 유용성을 넘어, 우리의 방법은 강력한 개인정보 및 보안 보장을 제공합니다: 이는 멤버십 추론 공격에 저항하며, 프롬프트 제거는 심지어 적대적 조건에서도 잔여 지식 추출을 방지합니다. 이는 데이터 보호 원칙을 준수하고 잊힌 정보에 대한 무단 접근을 방지하여 민감하고 규제된 환경에서의 배포에 적합하게 만듭니다. 전반적으로, 제거 가능성을 아키텍처 자체에 내장함으로써, 이 연구는 모듈식, 확장 가능하며 윤리적으로 반응하는 AI 모델 설계를 위한 새로운 기초를 확립합니다.

## 📝 요약

이 논문은 멀티미디어 분석에서 강력한 표현력을 제공하는 기초 모델의 새로운 학습 프레임워크를 제안합니다. 기존의 데이터 삭제 방법은 비용이 많이 들고 실시간 시스템에 적합하지 않은 반면, 본 연구는 학습 단계에서 지식의 획득과 제거를 통합하는 프롬프트 기반 학습을 도입합니다. 클래스 수준의 의미를 프롬프트 토큰에 연결하여, 특정 데이터를 삭제할 때 재학습이나 모델 수정 없이 해당 프롬프트를 제거하는 것만으로 즉각적인 삭제가 가능합니다. 실험 결과, 보유한 클래스의 예측 성능을 유지하면서도 삭제된 클래스의 정보는 효과적으로 제거됩니다. 또한, 이 방법은 데이터 보호 원칙을 준수하며, 민감하고 규제가 엄격한 환경에서의 사용에 적합한 강력한 개인정보 보호 및 보안성을 제공합니다.

## 🎯 주요 포인트

- 1. 기존의 정적 배포 방식은 GDPR과 같은 프라이버시 프레임워크의 요구에 부합하지 않으며, 이를 해결하기 위해 내재된 제거 기능을 갖춘 새로운 패러다임이 필요합니다.

- 2. 제안된 프롬프트 기반 학습 프레임워크는 지식 획득과 제거를 단일 학습 단계에서 통합하여, 프롬프트 토큰을 통해 클래스 수준의 의미를 바인딩합니다.

- 3. 프롬프트 제거만으로 즉각적인 정보 삭제가 가능하며, 이는 재학습, 모델 수정, 원본 데이터 접근 없이 이루어집니다.

- 4. 제안된 방법은 보유된 클래스에 대한 예측 성능을 유지하면서도 삭제된 클래스의 정보를 효과적으로 제거하며, 멤버십 추론 공격에 대한 저항성을 보입니다.

- 5. 데이터 보호 원칙을 준수하고 민감하고 규제가 엄격한 환경에서의 배포에 적합한 모듈형, 확장 가능, 윤리적 대응 AI 모델 설계를 위한 새로운 기반을 마련합니다.

---

*Generated on 2025-09-22 13:47:41*