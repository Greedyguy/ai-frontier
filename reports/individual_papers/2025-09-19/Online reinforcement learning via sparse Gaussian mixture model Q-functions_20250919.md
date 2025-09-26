---
keywords:
  - Reinforcement Learning
  - Sparse Gaussian Mixture Model Q-functions
  - Optimization
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14585
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:31:18.461274",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Sparse Gaussian Mixture Model Q-functions",
    "Optimization"
  ],
  "rejected_keywords": [
    "Riemannian Manifold Structure"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.85,
    "Sparse Gaussian Mixture Model Q-functions": 0.8,
    "Optimization": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Online reinforcement learning via sparse Gaussian mixture model Q-functions

**Korean Title:** 희소 가우시안 혼합 모델 Q-함수를 통한 온라인 강화 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Optimization|Online Gradient Descent]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Sparse Gaussian Mixture Model Q-functions|Sparse Gaussian Mixture Model Q-functions]]

## 🔗 유사한 논문
- [[Mining the Long Tail A Comparative Study of Data-Centric Criticality Metrics for Robust Offline Reinforcement Learning in Autonomous Motion Planning]] (81.8% similar)
- [[Reinforcement_Learning_Agent_for_a_2D_Shooter_Game_20250919|Reinforcement Learning Agent for a 2D Shooter Game]] (80.6% similar)
- [[Learning quantum many-body data locally A provably scalable framework]] (80.1% similar)
- [[Adversarial_Distilled_Retrieval-Augmented_Guarding_Model_for_Online_Malicious_Intent_Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (79.9% similar)
- [[TGPO Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (79.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14585v1 Announce Type: new 
Abstract: This paper introduces a structured and interpretable online policy-iteration framework for reinforcement learning (RL), built around the novel class of sparse Gaussian mixture model Q-functions (S-GMM-QFs). Extending earlier work that trained GMM-QFs offline, the proposed framework develops an online scheme that leverages streaming data to encourage exploration. Model complexity is regulated through sparsification by Hadamard overparametrization, which mitigates overfitting while preserving expressiveness. The parameter space of S-GMM-QFs is naturally endowed with a Riemannian manifold structure, allowing for principled parameter updates via online gradient descent on a smooth objective. Numerical tests show that S-GMM-QFs match the performance of dense deep RL (DeepRL) methods on standard benchmarks while using significantly fewer parameters, and maintain strong performance even in low-parameter-count regimes where sparsified DeepRL methods fail to generalize.

## 🔍 Abstract (한글 번역)

arXiv:2509.14585v1 발표 유형: 신규  
초록: 본 논문은 희소 가우시안 혼합 모델 Q-함수(S-GMM-QFs)의 새로운 클래스에 기반한 강화 학습(RL)을 위한 구조적이고 해석 가능한 온라인 정책 반복 프레임워크를 소개합니다. 이전에 GMM-QFs를 오프라인으로 훈련했던 연구를 확장하여, 제안된 프레임워크는 스트리밍 데이터를 활용하여 탐색을 장려하는 온라인 방식을 개발합니다. 모델의 복잡성은 하다마드 과매개변수를 통한 희소화로 조절되며, 이는 표현력을 유지하면서 과적합을 완화합니다. S-GMM-QFs의 매개변수 공간은 자연스럽게 리만 다양체 구조를 갖추고 있어, 매끄러운 목적 함수에 대한 온라인 경사 하강법을 통해 원칙적인 매개변수 업데이트가 가능합니다. 수치적 테스트 결과, S-GMM-QFs는 표준 벤치마크에서 밀집 심층 RL(DeepRL) 방법과 성능이 동등하며, 희소화된 DeepRL 방법이 일반화에 실패하는 저매개변수 환경에서도 강력한 성능을 유지함을 보여줍니다.

## 📝 요약

이 논문은 강화 학습(RL)을 위한 구조적이고 해석 가능한 온라인 정책 반복 프레임워크를 소개합니다. 이 프레임워크는 희소 가우시안 혼합 모델 Q-함수(S-GMM-QFs)를 중심으로 구축되었습니다. 이전의 오프라인 학습을 확장하여, 스트리밍 데이터를 활용해 탐색을 촉진하는 온라인 방식을 개발했습니다. 모델 복잡성은 하다마드 과매개변수를 통해 희소화하여 과적합을 방지하면서 표현력을 유지합니다. S-GMM-QFs의 매개변수 공간은 리만 기하 구조를 가지며, 매끄러운 목표에 대한 온라인 경사 하강법을 통해 매개변수를 업데이트합니다. 수치 실험 결과, S-GMM-QFs는 표준 벤치마크에서 적은 매개변수를 사용하면서도 밀집된 심층 강화 학습(DeepRL) 방법과 성능이 비슷하며, 희소화된 DeepRL 방법이 일반화에 실패하는 저매개변수 환경에서도 강력한 성능을 유지합니다.

## 🎯 주요 포인트

- 1. 이 논문은 희소 가우시안 혼합 모델 Q-함수(S-GMM-QFs)를 중심으로 한 강화 학습을 위한 구조적이고 해석 가능한 온라인 정책 반복 프레임워크를 소개합니다.

- 2. 제안된 프레임워크는 스트리밍 데이터를 활용하여 탐색을 장려하는 온라인 방식을 개발하며, Hadamard 과매개변수를 통한 희소화를 통해 모델 복잡성을 조절합니다.

- 3. S-GMM-QFs의 매개변수 공간은 리만 기하 구조를 가지며, 매끄러운 목표에 대한 온라인 경사 하강법을 통해 원칙적인 매개변수 업데이트가 가능합니다.

- 4. 수치 테스트 결과, S-GMM-QFs는 표준 벤치마크에서 밀집 심층 강화 학습(DeepRL) 방법과 동등한 성능을 보이며, 매개변수 수가 적은 상황에서도 강력한 성능을 유지합니다.

---

*Generated on 2025-09-19 15:25:35*