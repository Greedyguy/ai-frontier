---
keywords:
  - Neural PDE Solvers
  - Operator Learning
  - Optimization
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 23:02:31.772916",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural PDE Solvers",
    "Operator Learning",
    "Optimization"
  ],
  "rejected_keywords": [
    "Residual-Based Adaptivity",
    "Adaptive Weighting"
  ],
  "similarity_scores": {
    "Neural PDE Solvers": 0.78,
    "Operator Learning": 0.75,
    "Optimization": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# A Variational Framework for Residual-Based Adaptivity in Neural PDE Solvers and Operator Learning

**Korean Title:** 신경 편미분 방정식(PDE) 해석기와 연산자 학습에서 잔차 기반 적응성을 위한 변분적 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Optimization|Optimization]]
**⚡ Unique Technical**: [[keywords/Neural PDE Solvers|Neural PDE Solvers]], [[keywords/Operator Learning|Operator Learning]]

## 🔗 유사한 논문
- [[Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (80.3% similar)
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (80.2% similar)
- [[ActivePusher_ Active Learning and Planning with Residual Physics for Nonprehensile Manipulation_20250919|ActivePusher Active Learning and Planning with Residual Physics for Nonprehensile Manipulation]] (79.8% similar)
- [[Decentralized Optimization with Topology-Independent Communication_20250917|Decentralized Optimization with Topology-Independent Communication]] (79.6% similar)
- [[A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations Unifying Stochastic Mirror Descent, Learning and LLM Training]] (79.6% similar)

## 📋 저자 정보

**Authors:** Juan Diego Toscano, Daniel T. Chen, Vivek Oommen, George Em Karniadakis

## 📄 Abstract (원문)

Residual-based adaptive strategies are widely used in scientific machine
learning but remain largely heuristic. We introduce a unifying variational
framework that formalizes these methods by integrating convex transformations
of the residual. Different transformations correspond to distinct objective
functionals: exponential weights target the minimization of uniform error,
while linear weights recover the minimization of quadratic error. Within this
perspective, adaptive weighting is equivalent to selecting sampling
distributions that optimize the primal objective, thereby linking
discretization choices directly to error metrics. This principled approach
yields three benefits: (1) it enables systematic design of adaptive schemes
across norms, (2) reduces discretization error through variance reduction of
the loss estimator, and (3) enhances learning dynamics by improving the
gradient signal-to-noise ratio. Extending the framework to operator learning,
we demonstrate substantial performance gains across optimizers and
architectures. Our results provide a theoretical justification of
residual-based adaptivity and establish a foundation for principled
discretization and training strategies.

## 🔍 Abstract (한글 번역)

잔차 기반 적응 전략은 과학적 기계 학습에서 널리 사용되지만, 여전히 대부분은 경험적입니다. 우리는 이러한 방법을 잔차의 볼록 변환을 통합하여 형식화하는 통합 변분 프레임워크를 소개합니다. 서로 다른 변환은 서로 다른 목적 함수에 해당합니다: 지수 가중치는 균일한 오류 최소화를 목표로 하고, 선형 가중치는 이차 오류 최소화를 회복합니다. 이 관점에서 적응 가중화는 기본 목적을 최적화하는 샘플링 분포를 선택하는 것과 동등하며, 이를 통해 이산화 선택을 오류 메트릭에 직접 연결합니다. 이 원칙적인 접근법은 세 가지 이점을 제공합니다: (1) 다양한 노름에 걸쳐 적응형 스킴의 체계적인 설계를 가능하게 하고, (2) 손실 추정치의 분산 감소를 통해 이산화 오류를 줄이며, (3) 그래디언트 신호 대 잡음비를 개선하여 학습 역학을 향상시킵니다. 연산자 학습으로 프레임워크를 확장하여, 우리는 최적화기와 아키텍처 전반에 걸쳐 상당한 성능 향상을 입증합니다. 우리의 결과는 잔차 기반 적응성의 이론적 정당성을 제공하고, 원칙적인 이산화 및 훈련 전략의 기초를 확립합니다.

## 📝 요약

이 논문은 잔차 기반 적응 전략을 형식화하기 위해 변분 프레임워크를 도입하여 기존의 휴리스틱 방법을 체계화합니다. 이 프레임워크는 잔차의 볼록 변환을 통합하여 다양한 목적 함수로 변환합니다. 이를 통해 적응 가중치가 기본 목표를 최적화하는 샘플링 분포 선택과 동등하게 되어, 이산화 선택을 오류 메트릭과 직접 연결합니다. 이 접근법은 (1) 다양한 노름에서의 체계적인 적응 설계, (2) 손실 추정치의 분산 감소를 통한 이산화 오류 감소, (3) 기울기 신호 대 잡음비 개선을 통한 학습 동역학 향상을 제공합니다. 또한, 연산자 학습으로 확장하여 최적화기와 아키텍처 전반에 걸쳐 성능 향상을 입증합니다. 이 연구는 잔차 기반 적응의 이론적 정당성을 제공하고, 원칙적인 이산화 및 훈련 전략의 기초를 마련합니다.

## 🎯 주요 포인트

- 1. 잔차 기반 적응 전략을 통합하는 변분 프레임워크를 제안하여 기존의 휴리스틱 방법을 체계화합니다.

- 2. 다양한 변환을 통해 서로 다른 목표 함수가 정의되며, 이는 균일 오차와 이차 오차 최소화를 목표로 합니다.

- 3. 적응 가중치는 샘플링 분포 선택과 동일시되며, 이는 이산화 선택을 오류 메트릭과 직접 연결합니다.

- 4. 제안된 접근법은 다양한 노름에 걸친 체계적인 적응 스킴 설계를 가능하게 하고, 손실 추정기의 분산 감소를 통해 이산화 오류를 줄입니다.

- 5. 프레임워크를 연산자 학습으로 확장하여 최적화기와 아키텍처 전반에 걸쳐 성능 향상을 입증합니다.

---

*Generated on 2025-09-20 07:43:31*