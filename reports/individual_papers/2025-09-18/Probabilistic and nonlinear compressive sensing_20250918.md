---
keywords:
  - Compressive Sensing
  - Nonlinear Compressive Sensing
  - Probabilistic Reformulation
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:15:03.769310",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Compressive Sensing",
    "Nonlinear Compressive Sensing",
    "Probabilistic Reformulation"
  ],
  "rejected_keywords": [
    "Best Subset Selection"
  ],
  "similarity_scores": {
    "Compressive Sensing": 0.85,
    "Nonlinear Compressive Sensing": 0.8,
    "Probabilistic Reformulation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Probabilistic and nonlinear compressive sensing

**Korean Title:** 확률적 및 비선형 압축 센싱

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]     [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Compressive Sensing|compressive sensing]], [[keywords/Nonlinear Compressive Sensing|nonlinear compressive sensing]], [[keywords/Probabilistic Reformulation|probabilistic reformulation]]

## 🔗 유사한 논문
- [[A Universal Banach--Bregman Framework for Stochastic Iterations_ Unifying Stochastic Mirror Descent, Learning and LLM Training_20250917|A Universal Banach--Bregman Framework for Stochastic Iterations Unifying Stochastic Mirror Descent, Learning and LLM Training]] (80.6% similar)
- [[Mini-Batch Robustness Verification of Deep Neural Networks_20250919|Mini-Batch Robustness Verification of Deep Neural Networks]] (80.6% similar)
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (80.4% similar)
- [[Geometry-Aware Decentralized Sinkhorn for Wasserstein Barycenters_20250919|Geometry-Aware Decentralized Sinkhorn for Wasserstein Barycenters]] (79.4% similar)
- [[Optimal Algorithms for Bandit Learning in Matching Markets_20250919|Optimal Algorithms for Bandit Learning in Matching Markets]] (78.7% similar)

## 📋 저자 정보

**Authors:** Lukas Silvester Barth, Paulo von Petersenn

## 📄 Abstract (원문)

We present a smooth probabilistic reformulation of $\ell_0$ regularized
regression that does not require Monte Carlo sampling and allows for the
computation of exact gradients, facilitating rapid convergence to local optima
of the best subset selection problem. The method drastically improves
convergence speed compared to similar Monte Carlo based approaches.
Furthermore, we empirically demonstrate that it outperforms compressive sensing
algorithms such as IHT and (Relaxed-) Lasso across a wide range of settings and
signal-to-noise ratios. The implementation runs efficiently on both CPUs and
GPUs and is freely available at
https://github.com/L0-and-behold/probabilistic-nonlinear-cs.
  We also contribute to research on nonlinear generalizations of compressive
sensing by investigating when parameter recovery of a nonlinear teacher network
is possible through compression of a student network. Building upon theorems of
Fefferman and Markel, we show theoretically that the global optimum in the
infinite-data limit enforces recovery up to certain symmetries. For empirical
validation, we implement a normal-form algorithm that selects a canonical
representative within each symmetry class. However, while compression can help
to improve test loss, we find that exact parameter recovery is not even
possible up to symmetries. In particular, we observe a surprising rebound
effect where teacher and student configurations initially converge but
subsequently diverge despite continuous decrease in test loss. These findings
indicate fundamental differences between linear and nonlinear compressive
sensing.

## 🔍 Abstract (한글 번역)

다음은 $\ell_0$ 정규화 회귀의 매끄러운 확률적 재구성을 제시하며, 이는 몬테카를로 샘플링을 필요로 하지 않고 정확한 기울기를 계산할 수 있어 최적 부분 집합 선택 문제의 지역 최적점으로의 빠른 수렴을 촉진합니다. 이 방법은 유사한 몬테카를로 기반 접근법에 비해 수렴 속도를 획기적으로 개선합니다. 또한, 우리는 다양한 설정과 신호 대 잡음비에서 IHT 및 (Relaxed-) Lasso와 같은 압축 센싱 알고리즘보다 성능이 뛰어남을 경험적으로 입증합니다. 이 구현은 CPU와 GPU 모두에서 효율적으로 실행되며, https://github.com/L0-and-behold/probabilistic-nonlinear-cs에서 무료로 제공됩니다.

우리는 또한 학생 네트워크의 압축을 통해 비선형 교사 네트워크의 매개변수 복구가 가능한 경우를 조사하여 압축 센싱의 비선형 일반화에 대한 연구에 기여합니다. Fefferman과 Markel의 정리를 바탕으로, 우리는 무한 데이터 한계에서의 전역 최적점이 특정 대칭까지 복구를 강제함을 이론적으로 보여줍니다. 경험적 검증을 위해, 각 대칭 클래스 내에서 정규형 대표를 선택하는 알고리즘을 구현했습니다. 그러나 압축이 테스트 손실을 개선하는 데 도움이 될 수 있지만, 대칭까지도 정확한 매개변수 복구는 불가능하다는 것을 발견했습니다. 특히, 교사와 학생 구성은 초기에는 수렴하지만 테스트 손실이 지속적으로 감소함에도 불구하고 이후에 발산하는 놀라운 반등 효과를 관찰했습니다. 이러한 발견은 선형 및 비선형 압축 센싱 간의 근본적인 차이를 나타냅니다.

## 📝 요약

이 논문은 $\ell_0$ 정규화 회귀 문제를 부드러운 확률적 재구성으로 변환하여 몬테카를로 샘플링 없이도 정확한 기울기를 계산할 수 있는 방법을 제안합니다. 이 방법은 기존의 몬테카를로 기반 접근법보다 수렴 속도를 크게 향상시킵니다. 또한, IHT와 (Relaxed-) Lasso 같은 압축 센싱 알고리즘보다 다양한 설정과 신호 대 잡음비에서 우수한 성능을 보입니다. 이 방법은 CPU와 GPU에서 효율적으로 실행되며, 소스 코드는 공개되어 있습니다. 비선형 압축 센싱의 일반화 연구에서는 비선형 교사 네트워크의 매개변수를 학생 네트워크의 압축을 통해 복구할 수 있는지를 조사했습니다. 이론적으로는 무한 데이터 한계에서 특정 대칭성을 제외하고는 복구가 가능함을 보였으나, 실험적으로는 대칭성을 고려해도 정확한 매개변수 복구가 불가능함을 발견했습니다. 특히, 교사와 학생 네트워크가 초기에는 수렴하다가 이후에 발산하는 현상을 관찰했습니다. 이는 선형과 비선형 압축 센싱 간의 근본적인 차이를 시사합니다.

## 🎯 주요 포인트

- 1. $\ell_0$ 정규화 회귀의 확률적 재구성을 통해 몬테카를로 샘플링 없이 정확한 기울기를 계산하여 최적의 부분 집합 선택 문제의 빠른 수렴을 가능하게 합니다.

- 2. 제안된 방법은 기존의 몬테카를로 기반 접근법에 비해 수렴 속도를 크게 향상시킵니다.

- 3. 다양한 설정과 신호 대 잡음 비율에서 IHT 및 (Relaxed-) Lasso와 같은 압축 센싱 알고리즘을 능가하는 성능을 보입니다.

- 4. 비선형 압축 센싱의 일반화 연구에 기여하며, 비선형 교사 네트워크의 매개변수 복구가 학생 네트워크의 압축을 통해 가능한지를 조사합니다.

- 5. 비선형 압축 센싱에서 교사와 학생 네트워크의 구성은 초기에는 수렴하지만 이후에는 테스트 손실이 지속적으로 감소함에도 불구하고 분기하는 반동 효과를 관찰합니다.

---

*Generated on 2025-09-20 01:05:50*