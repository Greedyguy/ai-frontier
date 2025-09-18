
# Controllable Pareto Trade-off between Fairness and Accuracy

**Korean Title:** 공정성과 정확성 사이의 조절 가능한 파레토 트레이드오프 유지하기

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Human-defined Reference Vectors|Human-defined Reference Vectors]] [[keywords/broad/Multi-objective Optimization|Multi-objective Optimization]] [[keywords/broad/Fairness-Accuracy Trade-off|Fairness-Accuracy Trade-off]] [[keywords/specific/Hate Speech Detection|Hate Speech Detection]] [[keywords/unique/Controllable Pareto Trade-off (CPT|Controllable Pareto Trade-off (CPT]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Human-defined Reference Vectors
**🔬 Broad Technical**: Multi-objective Optimization, Fairness-Accuracy Trade-off
**🔗 Specific Connectable**: Hate Speech Detection
**⭐ Unique Technical**: Controllable Pareto Trade-off (CPT

**ArXiv ID**: [2509.13651](https://arxiv.org/abs/2509.13651)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13651.pdf)


## 🏷️ 추출된 키워드



`Multi-objective Optimization` • 

`Fairness-Accuracy Trade-off` • 

`Hate Speech Detection` • 

`Controllable Pareto Trade-off (CPT` • 

`Reference Vector`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13651v1 Announce Type: new 
Abstract: The fairness-accuracy trade-off is a key challenge in NLP tasks. Current work focuses on finding a single "optimal" solution to balance the two objectives, which is limited considering the diverse solutions on the Pareto front. This work intends to provide controllable trade-offs according to the user's preference of the two objectives, which is defined as a reference vector. To achieve this goal, we apply multi-objective optimization (MOO), which can find solutions from various regions of the Pareto front. However, it is challenging to precisely control the trade-off due to the stochasticity of the training process and the high dimentional gradient vectors. Thus, we propose Controllable Pareto Trade-off (CPT) that can effectively train models to perform different trade-offs according to users' preferences. CPT 1) stabilizes the fairness update with a moving average of stochastic gradients to determine the update direction, and 2) prunes the gradients by only keeping the gradients of the critical parameters. We evaluate CPT on hate speech detection and occupation classification tasks. Experiments show that CPT can achieve a higher-quality set of solutions on the Pareto front than the baseline methods. It also exhibits better controllability and can precisely follow the human-defined reference vectors.

## 🔍 Abstract (한글 번역)

arXiv:2509.13651v1 발표 유형: 새로운
요약: 공정성-정확도 트레이드 오프는 NLP 작업에서 중요한 도전 과제입니다. 현재 연구는 두 가지 목표를 균형있게 조정하는 단일 "최적" 솔루션을 찾는 데 초점을 맞추고 있으며, 이는 파레토 전면의 다양한 솔루션을 고려할 때 제한적입니다. 본 연구는 사용자의 두 가지 목표에 대한 선호도에 따라 조절 가능한 트레이드 오프를 제공하고자 합니다. 이는 참조 벡터로 정의됩니다. 이 목표를 달성하기 위해 우리는 다목적 최적화(MOO)를 적용하였으며, 이는 파레토 전면의 다양한 영역에서 솔루션을 찾을 수 있습니다. 그러나 훈련 과정의 확률성과 고차원 그래디언트 벡터의 높은 차원 때문에 트레이드 오프를 정확하게 제어하는 것은 어려운 일입니다. 따라서 우리는 사용자의 선호도에 따라 다양한 트레이드 오프를 수행할 수 있는 효과적인 모델 훈련을 위한 Controllable Pareto Trade-off (CPT)를 제안합니다. CPT는 1) 확률적 그래디언트의 이동 평균을 사용하여 공정성 업데이트를 안정화하고 업데이트 방향을 결정하며, 2) 중요한 매개변수의 그래디언트만 유지함으로써 그래디언트를 가지런히 합니다. 우리는 CPT를 혐오 발언 탐지 및 직업 분류 작업에서 평가하였습니다. 실험 결과, CPT는 베이스라인 방법보다 더 높은 품질의 솔루션 집합을 파레토 전면에서 달성할 수 있습니다. 또한 더 나은 조절 가능성을 보여주며 인간이 정의한 참조 벡터를 정확하게 따를 수 있습니다.

## 📝 요약

본 연구는 자연어 처리 작업에서 공정성과 정확성 간의 균형을 맞추는 것이 중요한데, 기존 연구들은 두 목표를 균형있게 달성하는 단일 "최적" 솔루션을 찾는 데 초점을 맞추었습니다. 본 연구는 사용자의 두 목표에 대한 선호도에 따라 조절 가능한 교환을 제공하고자 합니다. 이를 위해 Pareto front의 다양한 영역에서 솔루션을 찾을 수 있는 다목적 최적화(MOO)를 적용합니다. CPT는 공정성 업데이트를 안정화하고 중요한 매개변수의 그래디언트만 유지함으로써 모델을 다양한 교환에 대해 효과적으로 훈련할 수 있음을 제안합니다. 실험 결과, CPT는 기준 방법보다 Pareto front에서 더 높은 품질의 솔루션을 달성할 수 있음을 보여주었으며, 더 나은 조절성을 보여주며 인간이 정의한 참조 벡터를 정확하게 따를 수 있음을 입증하였습니다.

## 🎯 주요 포인트


- 1. NLP 작업에서 공정성-정확도 균형은 중요한 도전 과제이다.

- 2. 다양한 Pareto front 영역에서 해결책을 찾기 위해 MOO를 적용한다.

- 3. CPT는 사용자의 선호도에 따라 모델을 효과적으로 훈련시킬 수 있다.

- 4. CPT는 기준 벡터에 정확히 따라 다양한 trade-offs를 수행할 수 있다.


---

*Generated on 2025-09-18 16:37:53*