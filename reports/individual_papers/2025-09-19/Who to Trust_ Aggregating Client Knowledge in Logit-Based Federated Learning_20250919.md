---
keywords:
  - Federated Learning
  - Uncertainty Quantification
  - Logit-based Federated Learning
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.15147
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:17:17.889872",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Federated Learning",
    "Uncertainty Quantification",
    "Logit-based Federated Learning"
  ],
  "rejected_keywords": [
    "Meta-aggregation"
  ],
  "similarity_scores": {
    "Federated Learning": 0.9,
    "Uncertainty Quantification": 0.8,
    "Logit-based Federated Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Who to Trust? Aggregating Client Knowledge in Logit-Based Federated Learning

**Korean Title:** 신뢰할 대상은 누구인가? 로지트 기반 연합 학습에서 클라이언트 지식의 집계

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Federated Learning|Federated Learning]], [[keywords/Uncertainty Quantification|Uncertainty-weighted averaging]]
**⚡ Unique Technical**: [[keywords/Logit-based Federated Learning|Logit-based FL]]

## 🔗 유사한 논문
- [[FedAVOT Exact Distribution Alignment in Federated Learning via Masked Optimal Transport]] (86.0% similar)
- [[FedDiverse Tackling Data Heterogeneity in Federated Learning with Diversity-Driven Client Selection]] (85.3% similar)
- [[Hierarchical_Federated_Learning_for_Social_Network_with_Mobility_20250919|Hierarchical Federated Learning for Social Network with Mobility]] (81.5% similar)
- [[FedSSG Expectation-Gated and History-Aware Drift Alignment for Federated Learning]] (80.6% similar)
- [[Federated Learning for Deforestation Detection A Distributed Approach with Satellite Imagery]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15147v1 Announce Type: new 
Abstract: Federated learning (FL) usually shares model weights or gradients, which is costly for large models. Logit-based FL reduces this cost by sharing only logits computed on a public proxy dataset. However, aggregating information from heterogeneous clients is still challenging. This paper studies this problem, introduces and compares three logit aggregation methods: simple averaging, uncertainty-weighted averaging, and a learned meta-aggregator. Evaluated on MNIST and CIFAR-10, these methods reduce communication overhead, improve robustness under non-IID data, and achieve accuracy competitive with centralized training.

## 🔍 Abstract (한글 번역)

arXiv:2509.15147v1 발표 유형: 신규  
초록: 연합 학습(FL)은 일반적으로 모델 가중치나 그래디언트를 공유하는데, 이는 대규모 모델의 경우 비용이 많이 듭니다. 로짓 기반 FL은 공용 프록시 데이터셋에서 계산된 로짓만을 공유하여 이러한 비용을 줄입니다. 그러나 이질적인 클라이언트로부터 정보를 집계하는 것은 여전히 도전 과제입니다. 본 논문은 이 문제를 연구하고, 세 가지 로짓 집계 방법을 소개하고 비교합니다: 단순 평균, 불확실성 가중 평균, 학습된 메타 집계자. MNIST와 CIFAR-10에서 평가된 결과, 이러한 방법들은 통신 오버헤드를 줄이고, 비독립적이고 동일한 분포가 아닌(non-IID) 데이터에서의 강건성을 개선하며, 중앙 집중식 학습과 경쟁력 있는 정확도를 달성합니다.

## 📝 요약

이 논문은 연합 학습(FL)에서 대규모 모델의 가중치나 기울기를 공유하는 대신, 공용 프록시 데이터셋에서 계산된 로짓만을 공유하여 비용을 절감하는 방법을 제안합니다. 이 연구는 이질적인 클라이언트로부터 정보를 집계하는 문제를 다루며, 세 가지 로짓 집계 방법인 단순 평균, 불확실성 가중 평균, 학습된 메타 집계자를 소개하고 비교합니다. MNIST와 CIFAR-10 데이터셋에서 평가한 결과, 이 방법들은 통신 오버헤드를 줄이고 비독립적이고 동일하지 않은(non-IID) 데이터 환경에서의 강건성을 향상시키며, 중앙 집중식 학습과 경쟁력 있는 정확도를 달성했습니다.

## 🎯 주요 포인트

- 1. 연합 학습(FL)은 대규모 모델에서 모델 가중치나 기울기를 공유하는 것이 비용이 많이 든다.

- 2. 로짓 기반 FL은 공용 프록시 데이터셋에서 계산된 로짓만 공유하여 비용을 줄인다.

- 3. 이 논문은 이질적인 클라이언트로부터 정보를 집계하는 문제를 연구하고, 세 가지 로짓 집계 방법을 소개 및 비교한다.

- 4. 제안된 방법들은 MNIST와 CIFAR-10에서 평가되었으며, 통신 오버헤드를 줄이고 비독립적 동일 분포(non-IID) 데이터에서의 강건성을 개선하였다.

- 5. 제안된 방법들은 중앙 집중식 학습과 경쟁력 있는 정확도를 달성하였다.

---

*Generated on 2025-09-19 15:31:57*