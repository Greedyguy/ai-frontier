# Both Asymptotic and Non-Asymptotic Convergence of Quasi-Hyperbolic Momentum using Increasing Batch Size

**Korean Title:** 점진적으로 증가하는 배치 크기를 사용한 준-쌍곡선 모멘텀의 점근적 및 비점근적 수렴

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Increasing Batch Size|Increasing Batch Size]] [[keywords/specific/Stochastic Nonconvex Optimization|Stochastic Nonconvex Optimization]] [[keywords/broad/Deep Neural Networks|Deep Neural Networks]] [[keywords/unique/Quasi-Hyperbolic Momentum|Quasi-Hyperbolic Momentum]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Faster Convergence of Riemannian Stochastic Gradient Descent with Increasing Batch Size_20250922|Faster Convergence of Riemannian Stochastic Gradient Descent with Increasing Batch Size]] (84.1% similar) [[2025-09-22/DIVEBATCH_ Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation_20250922|DIVEBATCH: Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation]] (83.0% similar) [[2025-09-22/Flavors of Margin_ Implicit Bias of Steepest Descent in Homogeneous Neural Networks_20250922|Flavors of Margin: Implicit Bias of Steepest Descent in Homogeneous Neural Networks]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Increasing Batch Size Strategy
**🔗 Specific Connectable**: Mini-batch Gradient Descent
**🔬 Broad Technical**: Stochastic Optimization, Deep Neural Networks
**⭐ Unique Technical**: Quasi-Hyperbolic Momentum
## 🔗 유사한 논문
- [[2025-09-22/Faster Convergence of Riemannian Stochastic Gradient Descent with Increasing Batch Size_20250922|Faster Convergence of Riemannian Stochastic Gradient Descent with Increasing Batch Size]] (84.1% similar)
- [[2025-09-22/DIVEBATCH_ Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation_20250922|DIVEBATCH Accelerating Model Training Through Gradient-Diversity Aware Batch Size Adaptation]] (83.0% similar)
- [[2025-09-22/Flavors of Margin_ Implicit Bias of Steepest Descent in Homogeneous Neural Networks_20250922|Flavors of Margin Implicit Bias of Steepest Descent in Homogeneous Neural Networks]] (82.2% similar)
- [[2025-09-22/Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization_20250922|Adaptive Algorithms with Sharp Convergence Rates for Stochastic Hierarchical Optimization]] (81.5% similar)
- [[2025-09-18/Stochastic Bilevel Optimization with Heavy-Tailed Noise_20250918|Stochastic Bilevel Optimization with Heavy-Tailed Noise]] (80.8% similar)


**ArXiv ID**: [2506.23544](https://arxiv.org/abs/2506.23544)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2506.23544.pdf)


**ArXiv ID**: [2506.23544](https://arxiv.org/abs/2506.23544)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2506.23544.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Increasing Batch Size Strategy
**🔗 Specific Connectable**: Mini-batch Gradient Descent
**⭐ Unique Technical**: Quasi-Hyperbolic Momentum
**🔬 Broad Technical**: Stochastic Optimization, Deep Neural Networks

## 🏷️ 추출된 키워드



`Stochastic Optimization` • 

`Deep Neural Networks` • 

`Mini-batch Gradient Descent` • 

`Quasi-Hyperbolic Momentum` • 

`Increasing Batch Size Strategy`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.23544v3 Announce Type: replace 
Abstract: Momentum methods were originally introduced for their superiority to stochastic gradient descent (SGD) in deterministic settings with convex objective functions. However, despite their widespread application to deep neural networks -- a representative case of stochastic nonconvex optimization -- the theoretical justification for their effectiveness in such settings remains limited. Quasi-hyperbolic momentum (QHM) is an algorithm that generalizes various momentum methods and has been studied to better understand the class of momentum-based algorithms as a whole. In this paper, we provide both asymptotic and non-asymptotic convergence results for mini-batch QHM with an increasing batch size. We show that achieving asymptotic convergence requires either a decaying learning rate or an increasing batch size. Since a decaying learning rate adversely affects non-asymptotic convergence, we demonstrate that using mini-batch QHM with an increasing batch size -- without decaying the learning rate -- can be a more effective strategy. Our experiments show that even a finite increase in batch size can provide benefits for training neural networks.

## 🔍 Abstract (한글 번역)

arXiv:2506.23544v3 발표 유형: 교체  
초록: 모멘텀 방법은 원래 결정론적 환경에서 볼록 목적 함수에 대해 확률적 경사 하강법(SGD)보다 우수하다는 이유로 도입되었습니다. 그러나 심층 신경망에 대한 광범위한 적용에도 불구하고, 이는 확률적 비볼록 최적화의 대표적인 사례로, 이러한 환경에서의 효과에 대한 이론적 정당성은 여전히 제한적입니다. 준-쌍곡선 모멘텀(QHM)은 다양한 모멘텀 방법을 일반화한 알고리즘으로, 모멘텀 기반 알고리즘 전체 클래스를 더 잘 이해하기 위해 연구되었습니다. 본 논문에서는 배치 크기가 증가하는 미니배치 QHM에 대한 점근적 및 비점근적 수렴 결과를 제공합니다. 점근적 수렴을 달성하려면 학습률을 감소시키거나 배치 크기를 증가시켜야 한다는 것을 보여줍니다. 학습률 감소는 비점근적 수렴에 부정적인 영향을 미치기 때문에, 학습률을 감소시키지 않고 배치 크기를 증가시키는 미니배치 QHM을 사용하는 것이 더 효과적인 전략이 될 수 있음을 입증합니다. 우리의 실험은 배치 크기의 유한한 증가만으로도 신경망 훈련에 이점을 제공할 수 있음을 보여줍니다.

## 📝 요약

이 논문은 모멘텀 기반 알고리즘의 일반화된 형태인 준-쌍곡선 모멘텀(QHM)을 연구하여, 확률적 비볼록 최적화 문제에서의 효과성을 이론적으로 뒷받침하고자 합니다. 저자들은 증가하는 배치 크기를 사용하는 미니배치 QHM의 수렴 결과를 제시하며, 비감소 학습률과 함께 배치 크기를 늘리는 것이 비비감소 수렴에 유리함을 보였습니다. 실험 결과, 배치 크기의 유한한 증가만으로도 신경망 훈련에 이점이 있음을 확인했습니다.

## 🎯 주요 포인트


- 1. 모멘텀 방법은 원래 결정론적 환경에서 SGD보다 우수한 성능을 보이는 것으로 소개되었으나, 비결정론적 비볼록 최적화 환경에서의 이론적 근거는 제한적이다.

- 2. 쿼시-하이퍼볼릭 모멘텀(QHM)은 다양한 모멘텀 방법을 일반화한 알고리즘으로, 모멘텀 기반 알고리즘 전체를 이해하기 위해 연구되었다.

- 3. 본 논문에서는 증가하는 배치 크기를 사용하는 미니배치 QHM의 점근적 및 비점근적 수렴 결과를 제시한다.

- 4. 점근적 수렴을 달성하려면 학습률 감소 또는 배치 크기 증가가 필요하며, 학습률 감소는 비점근적 수렴에 부정적 영향을 미친다.

- 5. 실험 결과, 배치 크기의 유한한 증가만으로도 신경망 훈련에 이점을 제공할 수 있음을 보여준다.


---

*Generated on 2025-09-22 16:00:07*