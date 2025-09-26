---
keywords:
  - Federated Learning
  - Privacy Attacks
  - Data Heterogeneity
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:04:17.736241",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Privacy Attacks",
    "Data Heterogeneity"
  ],
  "rejected_keywords": [
    "Probabilistic Masking"
  ],
  "similarity_scores": {
    "Federated Learning": 0.8,
    "Privacy Attacks": 0.78,
    "Data Heterogeneity": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Towards Privacy-Preserving and Heterogeneity-aware Split Federated Learning via Probabilistic Masking

**Korean Title:** 프라이버시 보호 및 이질성 인식을 위한 확률적 마스킹 기반 분할 연합 학습 연구

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Federated Learning|Split Federated Learning]], [[keywords/Privacy Attacks|Privacy Attacks]]
**🚀 Evolved Concepts**: [[keywords/Data Heterogeneity|Data Heterogeneity]]

## 🔗 유사한 논문
- [[Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (82.8% similar)
- [[Hierarchical Federated Learning for Social Network with Mobility_20250919|Hierarchical Federated Learning for Social Network with Mobility]] (81.8% similar)
- [[Differential Privacy in Federated Learning_ Mitigating Inference Attacks with Randomized Response_20250917|Differential Privacy in Federated Learning Mitigating Inference Attacks with Randomized Response]] (80.0% similar)
- [[Who to Trust Aggregating Client Knowledge in Logit-Based Federated Learning_20250919|Who to Trust Aggregating Client Knowledge in Logit-Based Federated Learning]] (79.6% similar)
- [[FedAVOT_ Exact Distribution Alignment in Federated Learning via Masked Optimal Transport_20250919|FedAVOT Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (79.0% similar)

## 📋 저자 정보

**Authors:** Xingchen Wang, Feijie Wu, Chenglin Miao, Tianchun Li, Haoyu Hu, Qiming Cao, Jing Gao, Lu Su

## 📄 Abstract (원문)

Split Federated Learning (SFL) has emerged as an efficient alternative to
traditional Federated Learning (FL) by reducing client-side computation through
model partitioning. However, exchanging of intermediate activations and model
updates introduces significant privacy risks, especially from data
reconstruction attacks that recover original inputs from intermediate
representations. Existing defenses using noise injection often degrade model
performance. To overcome these challenges, we present PM-SFL, a scalable and
privacy-preserving SFL framework that incorporates Probabilistic Mask training
to add structured randomness without relying on explicit noise. This mitigates
data reconstruction risks while maintaining model utility. To address data
heterogeneity, PM-SFL employs personalized mask learning that tailors submodel
structures to each client's local data. For system heterogeneity, we introduce
a layer-wise knowledge compensation mechanism, enabling clients with varying
resources to participate effectively under adaptive model splitting.
Theoretical analysis confirms its privacy protection, and experiments on image
and wireless sensing tasks demonstrate that PM-SFL consistently improves
accuracy, communication efficiency, and robustness to privacy attacks, with
particularly strong performance under data and system heterogeneity.

## 🔍 Abstract (한글 번역)

스플릿 연합 학습(Split Federated Learning, SFL)은 모델 분할을 통해 클라이언트 측 연산을 줄임으로써 전통적인 연합 학습(Federated Learning, FL)에 대한 효율적인 대안으로 부상하고 있습니다. 그러나 중간 활성화 및 모델 업데이트의 교환은 특히 중간 표현에서 원래 입력을 복구하는 데이터 재구성 공격으로 인해 상당한 프라이버시 위험을 초래합니다. 노이즈 주입을 사용하는 기존 방어 방법은 종종 모델 성능을 저하시킵니다. 이러한 문제를 해결하기 위해, 우리는 명시적인 노이즈에 의존하지 않고 구조화된 무작위성을 추가하는 확률적 마스크 학습을 통합한 확장 가능하고 프라이버시를 보장하는 SFL 프레임워크인 PM-SFL을 제안합니다. 이는 데이터 재구성 위험을 완화하면서 모델 유용성을 유지합니다. 데이터 이질성을 해결하기 위해, PM-SFL은 각 클라이언트의 로컬 데이터에 맞춰 서브모델 구조를 조정하는 개인화된 마스크 학습을 사용합니다. 시스템 이질성에 대해서는, 적응형 모델 분할 하에서 다양한 자원을 가진 클라이언트가 효과적으로 참여할 수 있도록 하는 계층별 지식 보상 메커니즘을 도입합니다. 이론적 분석은 프라이버시 보호를 확인하며, 이미지 및 무선 센싱 작업에 대한 실험은 PM-SFL이 데이터 및 시스템 이질성 하에서 특히 강력한 성능을 보이며 정확성, 통신 효율성 및 프라이버시 공격에 대한 강건성을 지속적으로 향상시킴을 보여줍니다.

## 📝 요약

Split Federated Learning(SFL)은 클라이언트 측 계산을 줄이기 위해 모델을 분할하여 전통적인 연합 학습(FL)의 대안으로 등장했습니다. 그러나 중간 활성화 및 모델 업데이트 교환은 데이터 재구성 공격으로 인한 프라이버시 위험을 초래합니다. 기존의 노이즈 주입 방어는 모델 성능을 저하시킵니다. 이를 해결하기 위해, 우리는 확장 가능하고 프라이버시를 보호하는 SFL 프레임워크인 PM-SFL을 제안합니다. 이는 명시적인 노이즈 없이 구조화된 무작위성을 추가하는 확률적 마스크 훈련을 통합하여 데이터 재구성 위험을 완화하면서 모델 유용성을 유지합니다. 데이터 이질성을 해결하기 위해, PM-SFL은 각 클라이언트의 로컬 데이터에 맞춘 개인화된 마스크 학습을 사용합니다. 시스템 이질성에 대해서는, 자원에 따라 적응형 모델 분할을 통해 다양한 클라이언트가 효과적으로 참여할 수 있도록 레이어별 지식 보상 메커니즘을 도입합니다. 이론적 분석은 프라이버시 보호를 확인했으며, 이미지 및 무선 센싱 작업 실험에서 PM-SFL은 데이터 및 시스템 이질성 하에서 특히 강력한 성능을 보이며 정확도, 통신 효율성 및 프라이버시 공격에 대한 강건성을 지속적으로 향상시킵니다.

## 🎯 주요 포인트

- 1. Split Federated Learning (SFL)은 모델 분할을 통해 클라이언트 측 계산을 줄여 전통적인 Federated Learning (FL)의 효율적인 대안으로 부상했습니다.

- 2. PM-SFL은 명시적인 노이즈에 의존하지 않고 구조화된 무작위성을 추가하는 Probabilistic Mask 훈련을 통합하여 데이터 재구성 공격의 위험을 완화합니다.

- 3. PM-SFL은 개인화된 마스크 학습을 통해 각 클라이언트의 로컬 데이터에 맞춘 서브모델 구조를 제공하여 데이터 이질성을 해결합니다.

- 4. 시스템 이질성을 해결하기 위해, PM-SFL은 계층별 지식 보상 메커니즘을 도입하여 다양한 자원을 가진 클라이언트들이 적응형 모델 분할 하에 효과적으로 참여할 수 있도록 합니다.

- 5. 이론적 분석과 실험 결과는 PM-SFL이 데이터 및 시스템 이질성 하에서도 정확성, 통신 효율성, 프라이버시 공격에 대한 강건성을 지속적으로 개선함을 보여줍니다.

---

*Generated on 2025-09-20 05:49:36*