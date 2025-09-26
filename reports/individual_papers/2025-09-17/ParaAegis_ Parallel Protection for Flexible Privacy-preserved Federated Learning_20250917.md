---
keywords:
  - Federated Learning
  - Differential Privacy
  - Homomorphic Encryption
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:48:45.607720",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Differential Privacy",
    "Homomorphic Encryption"
  ],
  "rejected_keywords": [
    "Parallel Protection Framework",
    "Model Partitioning Scheme"
  ],
  "similarity_scores": {
    "Federated Learning": 0.95,
    "Differential Privacy": 0.9,
    "Homomorphic Encryption": 0.88
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# ParaAegis: Parallel Protection for Flexible Privacy-preserved Federated Learning

**Korean Title:** ParaAegis: 유연한 프라이버시 보호 연합 학습을 위한 병렬 보호

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Federated Learning|Federated Learning]], [[keywords/Differential Privacy|Differential Privacy]], [[keywords/Homomorphic Encryption|Homomorphic Encryption]]

## 🔗 유사한 논문
- [[Differential Privacy in Federated Learning_ Mitigating Inference Attacks with Randomized Response_20250917|Differential Privacy in Federated Learning Mitigating Inference Attacks with Randomized Response]] (84.9% similar)
- [[Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (84.4% similar)
- [[APFEx_ Adaptive Pareto Front Explorer for Intersectional Fairness_20250917|APFEx Adaptive Pareto Front Explorer for Intersectional Fairness]] (83.2% similar)
- [[Towards Privacy-Preserving and Heterogeneity-aware Split Federated Learning via Probabilistic Masking_20250918|Towards Privacy-Preserving and Heterogeneity-aware Split Federated Learning via Probabilistic Masking]] (81.9% similar)
- [[The Sum Leaks More Than Its Parts_ Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration_20250919|The Sum Leaks More Than Its Parts Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (81.4% similar)

## 📋 저자 정보

**Authors:** Zihou Wu, Yuecheng Li, Tianchi Liao, Jian Lou, Chuan Chen

## 📄 Abstract (원문)

Federated learning (FL) faces a critical dilemma: existing protection
mechanisms like differential privacy (DP) and homomorphic encryption (HE)
enforce a rigid trade-off, forcing a choice between model utility and
computational efficiency. This lack of flexibility hinders the practical
implementation. To address this, we introduce ParaAegis, a parallel protection
framework designed to give practitioners flexible control over the
privacy-utility-efficiency balance. Our core innovation is a strategic model
partitioning scheme. By applying lightweight DP to the less critical, low norm
portion of the model while protecting the remainder with HE, we create a
tunable system. A distributed voting mechanism ensures consensus on this
partitioning. Theoretical analysis confirms the adjustments between efficiency
and utility with the same privacy. Crucially, the experimental results
demonstrate that by adjusting the hyperparameters, our method enables flexible
prioritization between model accuracy and training time.

## 🔍 Abstract (한글 번역)

연합 학습(FL)은 중요한 딜레마에 직면해 있습니다. 차등 프라이버시(DP)와 동형 암호화(HE)와 같은 기존의 보호 메커니즘은 엄격한 절충을 강요하여 모델의 유용성과 계산 효율성 사이에서 선택을 강요합니다. 이러한 유연성의 부족은 실질적인 구현을 방해합니다. 이를 해결하기 위해 우리는 프라이버시-유용성-효율성 균형에 대한 실무자의 유연한 제어를 제공하도록 설계된 병렬 보호 프레임워크인 ParaAegis를 소개합니다. 우리의 핵심 혁신은 전략적 모델 분할 방식입니다. 모델의 덜 중요한, 낮은 노름 부분에 경량 DP를 적용하고 나머지를 HE로 보호함으로써 조정 가능한 시스템을 만듭니다. 분산 투표 메커니즘은 이 분할에 대한 합의를 보장합니다. 이론적 분석은 동일한 프라이버시를 유지하면서 효율성과 유용성 간의 조정을 확인합니다. 중요한 것은, 실험 결과가 하이퍼파라미터를 조정함으로써 우리의 방법이 모델 정확도와 훈련 시간 사이의 유연한 우선순위 설정을 가능하게 한다는 것을 보여줍니다.

## 📝 요약

연합 학습에서 기존의 보호 메커니즘인 차등 프라이버시(DP)와 동형 암호화(HE)는 모델의 유용성과 계산 효율성 사이에서 딜레마를 초래합니다. 이를 해결하기 위해 ParaAegis라는 병렬 보호 프레임워크를 제안합니다. 이 프레임워크는 모델을 전략적으로 분할하여 중요도가 낮은 부분에는 경량 DP를 적용하고, 나머지는 HE로 보호합니다. 분산 투표 메커니즘을 통해 이 분할에 대한 합의를 보장합니다. 이 방법은 동일한 프라이버시 수준에서 효율성과 유용성 간의 조정을 이론적으로 분석하며, 실험 결과 하이퍼파라미터 조정을 통해 모델 정확도와 학습 시간 간의 유연한 우선순위 조정이 가능함을 보여줍니다.

## 🎯 주요 포인트

- 1. 기존의 연합 학습 보호 메커니즘은 모델 유용성과 계산 효율성 사이의 엄격한 트레이드오프를 강요하여 실용적인 구현을 방해합니다.

- 2. ParaAegis는 프라이버시, 유용성, 효율성 간의 균형을 유연하게 조절할 수 있는 병렬 보호 프레임워크입니다.

- 3. 전략적인 모델 분할 기법을 통해 중요도가 낮은 부분에는 경량의 차등 프라이버시를 적용하고, 나머지는 동형 암호화로 보호합니다.

- 4. 분산 투표 메커니즘을 통해 모델 분할에 대한 합의를 보장합니다.

- 5. 실험 결과, 하이퍼파라미터 조정을 통해 모델 정확도와 훈련 시간 간의 우선순위를 유연하게 조절할 수 있음을 보여줍니다.

---

*Generated on 2025-09-20 09:36:53*