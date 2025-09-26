---
keywords:
  - General Data Protection Regulation
  - Machine Unlearning
  - Collaborative Filtering
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2508.17076
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:20:41.676475",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "General Data Protection Regulation",
    "Machine Unlearning",
    "Collaborative Filtering"
  ],
  "rejected_keywords": [
    "Recommender Systems",
    "Next-Basket Recommendation"
  ],
  "similarity_scores": {
    "General Data Protection Regulation": 0.8,
    "Machine Unlearning": 0.78,
    "Collaborative Filtering": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Towards a Real-World Aligned Benchmark for Unlearning in Recommender Systems

**Korean Title:** 현실 세계에 부합하는 추천 시스템에서의 비학습을 위한 벤치마크 구축을 향하여

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/General Data Protection Regulation|GDPR]], [[keywords/Collaborative Filtering|Collaborative Filtering]]
**⚡ Unique Technical**: [[keywords/Machine Unlearning|Machine Unlearning]]

## 🔗 유사한 논문
- [[Sample Efficient Experience Replay in Non-stationary Environments_20250919|Sample Efficient Experience Replay in Non-stationary Environments]] (78.5% similar)
- [[Towards Unified and Adaptive Cross-Domain Collaborative Filtering via Graph Signal Processing]] (78.1% similar)
- [[Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (78.0% similar)
- [[Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (77.2% similar)
- [[GEM-Bench A Benchmark for Ad-Injected Response Generation within Generative Engine Marketing]] (77.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.17076v2 Announce Type: replace 
Abstract: Modern recommender systems heavily leverage user interaction data to deliver personalized experiences. However, relying on personal data presents challenges in adhering to privacy regulations, such as the GDPR's "right to be forgotten". Machine unlearning (MU) aims to address these challenges by enabling the efficient removal of specific training data from models post-training, without compromising model utility or leaving residual information. However, current benchmarks for unlearning in recommender systems -- most notably CURE4Rec -- fail to reflect real-world operational demands. They focus narrowly on collaborative filtering, overlook tasks like session-based and next-basket recommendation, simulate unrealistically large unlearning requests, and ignore critical efficiency constraints. In this paper, we propose a set of design desiderata and research questions to guide the development of a more realistic benchmark for unlearning in recommender systems, with the goal of gathering feedback from the research community. Our benchmark proposal spans multiple recommendation tasks, includes domain-specific unlearning scenarios, and several unlearning algorithms -- including ones adapted from a recent NeurIPS unlearning competition. Furthermore, we argue for an unlearning setup that reflects the sequential, time-sensitive nature of real-world deletion requests. We also present a preliminary experiment in a next-basket recommendation setting based on our proposed desiderata and find that unlearning also works for sequential recommendation models, exposed to many small unlearning requests. In this case, we observe that a modification of a custom-designed unlearning algorithm for recommender systems outperforms general unlearning algorithms significantly, and that unlearning can be executed with a latency of only several seconds.

## 🔍 Abstract (한글 번역)

arXiv:2508.17076v2 발표 유형: 교체  
초록: 현대의 추천 시스템은 사용자 상호작용 데이터를 활용하여 개인화된 경험을 제공합니다. 그러나 개인 데이터에 의존하는 것은 GDPR의 "잊혀질 권리"와 같은 개인정보 보호 규정을 준수하는 데 있어 도전 과제를 제시합니다. 머신 언러닝(MU)은 모델의 유용성을 손상시키거나 잔여 정보를 남기지 않고 훈련 후 특정 훈련 데이터를 효율적으로 제거할 수 있도록 하여 이러한 문제를 해결하고자 합니다. 그러나 추천 시스템에서의 언러닝을 위한 현재의 벤치마크, 특히 CURE4Rec는 실제 운영 요구를 반영하지 못하고 있습니다. 이들은 협업 필터링에만 집중하고, 세션 기반 추천 및 다음 장바구니 추천과 같은 작업을 간과하며, 비현실적으로 큰 언러닝 요청을 시뮬레이션하고, 중요한 효율성 제약을 무시합니다. 본 논문에서는 추천 시스템에서의 언러닝을 위한 보다 현실적인 벤치마크 개발을 안내하기 위한 설계 요구사항과 연구 질문을 제안하며, 연구 커뮤니티로부터 피드백을 수집하는 것을 목표로 합니다. 우리의 벤치마크 제안은 여러 추천 작업을 포함하고, 도메인별 언러닝 시나리오와 최근 NeurIPS 언러닝 대회에서 적응된 알고리즘을 포함한 여러 언러닝 알고리즘을 포함합니다. 또한, 우리는 실제 삭제 요청의 순차적이고 시간 민감한 특성을 반영하는 언러닝 설정을 주장합니다. 우리는 또한 제안된 요구사항에 기반한 다음 장바구니 추천 설정에서의 예비 실험을 제시하며, 언러닝이 많은 작은 언러닝 요청에 노출된 순차적 추천 모델에서도 작동함을 발견했습니다. 이 경우, 추천 시스템을 위한 맞춤형 언러닝 알고리즘의 수정이 일반적인 언러닝 알고리즘보다 성능이 훨씬 뛰어나며, 언러닝이 단 몇 초의 지연 시간으로 실행될 수 있음을 관찰했습니다.

## 📝 요약

현대 추천 시스템은 사용자 상호작용 데이터를 활용하여 개인화된 경험을 제공합니다. 그러나 개인정보 보호 규정 준수 문제, 특히 GDPR의 "잊힐 권리"로 인해 어려움이 발생합니다. 머신 언러닝(MU)은 훈련 후 특정 데이터를 효율적으로 제거하여 이러한 문제를 해결하려고 합니다. 그러나 현재의 언러닝 벤치마크, 특히 CURE4Rec는 실제 운영 요구를 반영하지 못합니다. 이 연구에서는 추천 시스템에서 보다 현실적인 언러닝 벤치마크 개발을 위한 설계 기준과 연구 질문을 제안합니다. 제안된 벤치마크는 여러 추천 작업을 포함하고, 도메인별 언러닝 시나리오와 다양한 언러닝 알고리즘을 포함합니다. 또한, 실제 삭제 요청의 순차적, 시간 민감적 특성을 반영하는 언러닝 설정을 주장합니다. 초기 실험 결과, 제안된 기준에 기반한 다음 장바구니 추천 설정에서 맞춤형 언러닝 알고리즘이 일반 알고리즘보다 우수하며, 언러닝이 몇 초의 지연으로 실행될 수 있음을 발견했습니다.

## 🎯 주요 포인트

- 1. 현대 추천 시스템은 사용자 상호작용 데이터를 활용하여 개인화된 경험을 제공하지만, 개인 데이터 의존은 GDPR의 "잊혀질 권리"와 같은 프라이버시 규정을 준수하는 데 어려움을 초래합니다.

- 2. 기계 학습 삭제(MU)는 모델의 유용성을 유지하면서 특정 훈련 데이터를 효율적으로 제거하여 이러한 프라이버시 문제를 해결하려고 합니다.

- 3. 기존의 추천 시스템에서의 삭제 벤치마크는 현실적인 운영 요구를 반영하지 못하며, 협업 필터링에만 집중하고 세션 기반 추천이나 다음 장바구니 추천과 같은 작업을 간과합니다.

- 4. 본 논문에서는 추천 시스템에서의 삭제를 위한 보다 현실적인 벤치마크 개발을 위한 설계 기준과 연구 질문을 제안하며, 연구 커뮤니티의 피드백을 수집하고자 합니다.

- 5. 제안된 벤치마크는 여러 추천 작업을 포함하고, 도메인별 삭제 시나리오와 다양한 삭제 알고리즘을 포함하며, 특히 순차적이고 시간 민감한 삭제 요청을 반영하는 설정을 주장합니다.

---

*Generated on 2025-09-19 16:26:34*