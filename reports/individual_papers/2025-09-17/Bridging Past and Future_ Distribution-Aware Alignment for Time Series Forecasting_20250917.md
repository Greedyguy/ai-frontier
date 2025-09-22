# Bridging Past and Future: Distribution-Aware Alignment for Time Series Forecasting

**Korean Title:** 과거와 미래를 연결하기: 시계열 예측을 위한 분포 인식 정렬

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Yifan Hu|Yifan Hu]] [[authors/Jie Yang|Jie Yang]] [[authors/Tian Zhou|Tian Zhou]] [[authors/Peiyuan Liu|Peiyuan Liu]] [[authors/Yujin Tang|Yujin Tang]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Distribution Aware Alignment

## 🔗 유사한 논문
- [[Stochastic Clock Attention for Aligning Continuous and Ordered Sequences_20250918|Stochastic Clock Attention for Aligning Continuous and Ordered Sequences]] (82.7% similar)
- [[Super-Linear_ A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting_20250918|Super-Linear A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting]] (81.3% similar)
- [[Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (79.9% similar)
- [[DAG_ A Dual Causal Network for Time Series Forecasting with Exogenous Variables_20250919|DAG A Dual Causal Network for Time Series Forecasting with Exogenous Variables]] (78.9% similar)
- [[Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery_20250918|Structure-Aware Contrastive Learning with Fine-Grained Binding Representations for Drug Discovery]] (78.6% similar)

## 📋 저자 정보

**Authors:** Yifan Hu, Jie Yang, Tian Zhou, Peiyuan Liu, Yujin Tang, Rong Jin, Liang Sun

## 📄 Abstract (원문)

Representation learning techniques like contrastive learning have long been
explored in time series forecasting, mirroring their success in computer vision
and natural language processing. Yet recent state-of-the-art (SOTA) forecasters
seldom adopt these representation approaches because they have shown little
performance advantage. We challenge this view and demonstrate that explicit
representation alignment can supply critical information that bridges the
distributional gap between input histories and future targets. To this end, we
introduce TimeAlign, a lightweight, plug-and-play framework that learns
auxiliary features via a simple reconstruction task and feeds them back to any
base forecaster. Extensive experiments across eight benchmarks verify its
superior performance. Further studies indicate that the gains arises primarily
from correcting frequency mismatches between historical inputs and future
outputs. We also provide a theoretical justification for the effectiveness of
TimeAlign in increasing the mutual information between learned representations
and predicted targets. As it is architecture-agnostic and incurs negligible
overhead, TimeAlign can serve as a general alignment module for modern deep
learning time-series forecasting systems. The code is available at
https://github.com/TROUBADOUR000/TimeAlign.

## 🔍 Abstract (한글 번역)

대조 학습과 같은 표현 학습 기법은 컴퓨터 비전 및 자연어 처리에서의 성공을 반영하여 시계열 예측에서도 오랫동안 탐구되어 왔습니다. 그러나 최근의 최첨단(SOTA) 예측 모델들은 이러한 표현 접근 방식을 거의 채택하지 않는데, 이는 성능상의 이점이 거의 없었기 때문입니다. 우리는 이 관점을 도전하며, 명시적인 표현 정렬이 입력 이력과 미래 목표 간의 분포 차이를 연결하는 중요한 정보를 제공할 수 있음을 입증합니다. 이를 위해, 우리는 TimeAlign이라는 경량의 플러그 앤 플레이 프레임워크를 소개합니다. 이는 간단한 재구성 작업을 통해 보조 특징을 학습하고 이를 어떤 기본 예측 모델에도 피드백합니다. 여덟 가지 벤치마크에 걸친 광범위한 실험은 TimeAlign의 뛰어난 성능을 검증합니다. 추가 연구에서는 이러한 성과가 주로 과거 입력과 미래 출력 간의 주파수 불일치를 수정하는 데서 기인함을 나타냅니다. 우리는 또한 학습된 표현과 예측 목표 간의 상호 정보를 증가시키는 TimeAlign의 효과에 대한 이론적 정당성을 제공합니다. TimeAlign은 아키텍처에 구애받지 않으며, 거의 추가 비용이 들지 않기 때문에 현대의 딥러닝 시계열 예측 시스템을 위한 일반적인 정렬 모듈로 활용될 수 있습니다. 코드는 https://github.com/TROUBADOUR000/TimeAlign에서 제공됩니다.

## 📝 요약

이 논문은 시계열 예측에서 대조 학습과 같은 표현 학습 기법이 잘 활용되지 않는 문제를 다룹니다. 저자들은 TimeAlign이라는 경량 프레임워크를 제안하여 입력 데이터와 미래 목표 간의 분포 차이를 줄이는 데 중요한 정보를 제공한다고 주장합니다. TimeAlign은 간단한 재구성 작업을 통해 보조 특징을 학습하고 이를 기본 예측기에 전달합니다. 8개의 벤치마크 실험에서 TimeAlign의 우수한 성능이 입증되었으며, 주로 과거 입력과 미래 출력 간의 주파수 불일치를 수정함으로써 성능이 향상됨을 확인했습니다. 이 방법은 아키텍처에 구애받지 않으며 추가적인 부담이 거의 없어, 현대 딥러닝 시계열 예측 시스템에 일반적인 정렬 모듈로 활용될 수 있습니다.

## 🎯 주요 포인트

- 1. TimeAlign은 입력 이력과 미래 목표 간의 분포 차이를 해소하는 중요한 정보를 제공하는 경량의 플러그 앤 플레이 프레임워크입니다.

- 2. TimeAlign은 간단한 재구성 작업을 통해 보조 특징을 학습하고 이를 기반 예측기에 피드백하여 성능을 향상시킵니다.

- 3. 8개의 벤치마크 실험에서 TimeAlign의 우수한 성능이 검증되었으며, 주로 역사적 입력과 미래 출력 간의 주파수 불일치를 수정함으로써 성능 향상이 이루어졌습니다.

- 4. TimeAlign은 학습된 표현과 예측 목표 간의 상호 정보를 증가시키는 데 효과적이라는 이론적 근거를 제공합니다.

- 5. TimeAlign은 아키텍처에 구애받지 않으며, 최소한의 오버헤드를 발생시켜 현대 심층 학습 시계열 예측 시스템을 위한 일반적인 정렬 모듈로 활용될 수 있습니다.

---

*Generated on 2025-09-20 07:44:00*