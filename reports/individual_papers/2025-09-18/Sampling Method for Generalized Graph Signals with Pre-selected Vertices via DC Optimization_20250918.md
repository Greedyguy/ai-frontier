---
keywords:
  - Graph Neural Networks
  - Nuclear Norm Minimization
  - Difference-of-Convex Optimization
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:11:30.503598",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Networks",
    "Nuclear Norm Minimization",
    "Difference-of-Convex Optimization"
  ],
  "rejected_keywords": [
    "Sampling Theory"
  ],
  "similarity_scores": {
    "Graph Neural Networks": 0.78,
    "Nuclear Norm Minimization": 0.75,
    "Difference-of-Convex Optimization": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Sampling Method for Generalized Graph Signals with Pre-selected Vertices via DC Optimization

**Korean Title:** 일반화된 그래프 신호의 샘플링 방법: DC 최적화를 통한 사전 선택된 정점 활용

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Networks|graph signals]]
**⚡ Unique Technical**: [[keywords/Nuclear Norm Minimization|nuclear norm]], [[keywords/Difference-of-Convex Optimization|DC optimization]]

## 🔗 유사한 논문
- [[Learning Graph from Smooth Signals under Partial Observation_ A Robustness Analysis_20250918|Learning Graph from Smooth Signals under Partial Observation A Robustness Analysis]] (80.6% similar)
- [[GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque Torque-Driven Rewiring Graph Neural Network]] (78.9% similar)
- [[Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (78.0% similar)
- [[Undersampled Phase Retrieval with Image Priors_20250918|Undersampled Phase Retrieval with Image Priors]] (77.7% similar)
- [[Attention Beyond Neighborhoods_ Reviving Transformer for Graph Clustering_20250918|Attention Beyond Neighborhoods Reviving Transformer for Graph Clustering]] (76.8% similar)

## 📋 저자 정보

**Authors:** Keitaro Yamashita, Kazuki Naganuma, Shunsuke Ono

## 📄 Abstract (원문)

This paper proposes a method for vertex-wise flexible sampling of a broad
class of graph signals, designed to attain the best possible recovery based on
the generalized sampling theory. This is achieved by designing a sampling
operator by an optimization problem, which is inherently non-convex, as the
best possible recovery imposes a rank constraint. An existing method for
vertex-wise flexible sampling is able to control the number of active vertices
but cannot incorporate prior knowledge of mandatory or forbidden vertices. To
address these challenges, we formulate the operator design as a problem that
handles a constraint of the number of active vertices and prior knowledge on
specific vertices for sampling, mandatory inclusion or exclusion. We
transformed this constrained problem into a difference-of-convex (DC)
optimization problem by using the nuclear norm and a DC penalty for vertex
selection. To solve this, we develop a convergent solver based on the general
double-proximal gradient DC algorithm. The effectiveness of our method is
demonstrated through experiments on various graph signal models, including
real-world data, showing superior performance in the recovery accuracy by
comparing to existing methods.

## 🔍 Abstract (한글 번역)

이 논문은 일반화된 샘플링 이론에 기반하여 최상의 복원을 달성하기 위해 설계된 광범위한 그래프 신호의 정점별 유연한 샘플링 방법을 제안합니다. 이는 최상의 복원이 랭크 제약을 부과하기 때문에 본질적으로 비볼록인 최적화 문제를 통해 샘플링 연산자를 설계함으로써 달성됩니다. 기존의 정점별 유연한 샘플링 방법은 활성 정점의 수를 제어할 수 있지만, 필수 또는 금지된 정점에 대한 사전 지식을 통합할 수 없습니다. 이러한 문제를 해결하기 위해, 우리는 샘플링을 위한 특정 정점에 대한 사전 지식과 활성 정점 수의 제약을 처리하는 문제로 연산자 설계를 공식화합니다. 이 제약 문제를 핵 노름과 정점 선택을 위한 DC 페널티를 사용하여 차이-볼록(Difference-of-Convex, DC) 최적화 문제로 변환했습니다. 이를 해결하기 위해 일반적인 이중-근접 경사 DC 알고리즘에 기반한 수렴 솔버를 개발했습니다. 우리의 방법의 효과는 다양한 그래프 신호 모델, 특히 실제 데이터에 대한 실험을 통해 입증되었으며, 기존 방법과 비교하여 복원 정확도에서 우수한 성능을 보였습니다.

## 📝 요약

이 논문은 일반화된 샘플링 이론에 기반하여 그래프 신호의 최적 복원을 위한 정점별 유연한 샘플링 방법을 제안합니다. 기존 방법은 활성 정점 수를 조절할 수 있지만 필수 또는 금지 정점에 대한 사전 지식을 반영하지 못합니다. 이를 해결하기 위해, 활성 정점 수와 특정 정점에 대한 사전 지식을 고려한 제약 조건을 포함하는 최적화 문제로 샘플링 연산자를 설계했습니다. 이 문제를 핵심적으로 비볼록 최적화 문제로 변환하고, 핵심 기법으로 핵 노름과 DC 패널티를 사용하여 차이-볼록(DC) 최적화 문제로 변환했습니다. 이를 해결하기 위해 일반적인 이중-근접 경사 DC 알고리즘에 기반한 수렴 솔버를 개발했습니다. 다양한 그래프 신호 모델과 실제 데이터를 통한 실험 결과, 제안된 방법이 기존 방법보다 복원 정확도에서 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 이 논문은 일반화된 샘플링 이론에 기반하여 그래프 신호의 최적 복원을 목표로 하는 정점 단위의 유연한 샘플링 방법을 제안합니다.

- 2. 최적 복원을 위한 샘플링 연산자는 본질적으로 비볼록한 최적화 문제로 설계되며, 이는 랭크 제약을 포함합니다.

- 3. 기존 방법은 활성 정점의 수를 제어할 수 있지만 필수 또는 금지 정점에 대한 사전 지식을 반영할 수 없습니다.

- 4. 제안된 방법은 활성 정점 수와 특정 정점에 대한 사전 지식을 처리하는 문제로 연산자 설계를 공식화합니다.

- 5. 다양한 그래프 신호 모델 실험을 통해 제안된 방법이 기존 방법보다 복원 정확도에서 우수한 성능을 보임을 입증했습니다.

---

*Generated on 2025-09-20 02:48:45*