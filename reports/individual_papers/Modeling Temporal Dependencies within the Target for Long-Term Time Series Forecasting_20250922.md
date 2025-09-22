# Modeling Temporal Dependencies within the Target for Long-Term Time Series Forecasting

**Korean Title:** 타임 시리즈 예측의 장기적 관점을 위한 목표 내 시간적 의존성 모델링

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Adaptive Loss Balancing|Adaptive Loss Balancing]] [[keywords/specific/Temporal Dependencies|Temporal Dependencies]] [[keywords/broad/Time Series Forecasting|Time Series Forecasting]] [[keywords/unique/Temporal Dependency Alignment|Temporal Dependency Alignment]] [[categories/cs.LG|cs.LG]] [[2025-09-17/Bridging Past and Future_ Distribution-Aware Alignment for Time Series Forecasting_20250917|Bridging Past and Future: Distribution-Aware Alignment for Time Series Forecasting]] (87.1% similar) [[2025-09-18/Super-Linear_ A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting_20250918|Super-Linear: A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting]] (81.2% similar) [[2025-09-22/DPANet_ Dual Pyramid Attention Network for Multivariate Time Series Forecasting_20250922|DPANet: Dual Pyramid Attention Network for Multivariate Time Series Forecasting]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive Loss Balancing
**🔗 Specific Connectable**: Temporal Dependencies
**🔬 Broad Technical**: Time Series Forecasting
**⭐ Unique Technical**: Temporal Dependency Alignment
## 🔗 유사한 논문
- [[2025-09-17/Bridging Past and Future_ Distribution-Aware Alignment for Time Series Forecasting_20250917|Bridging Past and Future Distribution-Aware Alignment for Time Series Forecasting]] (87.1% similar)
- [[2025-09-18/Super-Linear_ A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting_20250918|Super-Linear A Lightweight Pretrained Mixture of Linear Experts for Time Series Forecasting]] (81.2% similar)
- [[2025-09-22/DPANet_ Dual Pyramid Attention Network for Multivariate Time Series Forecasting_20250922|DPANet Dual Pyramid Attention Network for Multivariate Time Series Forecasting]] (81.2% similar)
- [[2025-09-17/TFMAdapter_ Lightweight Instance-Level Adaptation of Foundation Models for Forecasting with Covariates_20250917|TFMAdapter Lightweight Instance-Level Adaptation of Foundation Models for Forecasting with Covariates]] (81.2% similar)
- [[2025-09-22/FOVAL_ Calibration-Free and Subject-Invariant Fixation Depth Estimation Across Diverse Eye-Tracking Datasets_20250922|FOVAL Calibration-Free and Subject-Invariant Fixation Depth Estimation Across Diverse Eye-Tracking Datasets]] (80.0% similar)


**ArXiv ID**: [2406.04777](https://arxiv.org/abs/2406.04777)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2406.04777.pdf)


**ArXiv ID**: [2406.04777](https://arxiv.org/abs/2406.04777)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2406.04777.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive Loss Balancing
**🔗 Specific Connectable**: Temporal Dependencies
**⭐ Unique Technical**: Temporal Dependency Alignment
**🔬 Broad Technical**: Time Series Forecasting

## 🏷️ 추출된 키워드



`Time Series Forecasting` • 

`Temporal Dependencies` • 

`Temporal Dependency Alignment` • 

`Adaptive Loss Balancing`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2406.04777v3 Announce Type: replace 
Abstract: Long-term time series forecasting (LTSF) is a critical task across diverse domains. Despite significant advancements in LTSF research, we identify a performance bottleneck in existing LTSF methods caused by the inadequate modeling of Temporal Dependencies within the Target (TDT). To address this issue, we propose a novel and generic temporal modeling framework, Temporal Dependency Alignment (TDAlign), that equips existing LTSF methods with TDT learning capabilities. TDAlign introduces two key innovations: 1) a loss function that aligns the change values between adjacent time steps in the predictions with those in the target, ensuring consistency with variation patterns, and 2) an adaptive loss balancing strategy that seamlessly integrates the new loss function with existing LTSF methods without introducing additional learnable parameters. As a plug-and-play framework, TDAlign enhances existing methods with minimal computational overhead, featuring only linear time complexity and constant space complexity relative to the prediction length. Extensive experiments on six strong LTSF baselines across seven real-world datasets demonstrate the effectiveness and flexibility of TDAlign. On average, TDAlign reduces baseline prediction errors by \textbf{1.47\%} to \textbf{9.19\%} and change value errors by \textbf{4.57\%} to \textbf{15.78\%}, highlighting its substantial performance improvements.

## 🔍 Abstract (한글 번역)

arXiv:2406.04777v3 발표 유형: 교체  
초록: 장기 시계열 예측(LTSF)은 다양한 분야에서 중요한 과제입니다. LTSF 연구에서 상당한 발전이 있었음에도 불구하고, 기존 LTSF 방법에서 목표 내 시간적 종속성(TDT)의 불충분한 모델링으로 인해 성능 병목 현상이 발생하는 것을 확인했습니다. 이 문제를 해결하기 위해, 우리는 기존 LTSF 방법에 TDT 학습 기능을 제공하는 새로운 일반적 시간 모델링 프레임워크인 Temporal Dependency Alignment (TDAlign)을 제안합니다. TDAlign은 두 가지 주요 혁신을 도입합니다: 1) 예측의 인접한 시간 단계 간의 변화 값을 목표의 변화 값과 정렬하여 변화 패턴과의 일관성을 보장하는 손실 함수, 2) 추가 학습 가능한 매개변수를 도입하지 않고 새로운 손실 함수를 기존 LTSF 방법과 원활하게 통합하는 적응형 손실 균형 전략. 플러그 앤 플레이 프레임워크로서, TDAlign은 예측 길이에 비례하여 선형 시간 복잡도와 상수 공간 복잡도만을 특징으로 하여 최소한의 계산 오버헤드로 기존 방법을 향상시킵니다. 7개의 실제 데이터셋에서 6개의 강력한 LTSF 기준선에 대한 광범위한 실험은 TDAlign의 효과성과 유연성을 입증합니다. 평균적으로, TDAlign은 기준선 예측 오류를 \textbf{1.47\%}에서 \textbf{9.19\%}까지, 변화 값 오류를 \textbf{4.57\%}에서 \textbf{15.78\%}까지 감소시켜 상당한 성능 향상을 강조합니다.

## 📝 요약

장기 시계열 예측(LTSF)에서 기존 방법의 성능 병목 현상을 해결하기 위해, Temporal Dependency Alignment(TDAlign)라는 새로운 프레임워크를 제안합니다. TDAlign은 예측값과 실제값의 변화 패턴을 일치시키는 손실 함수와 기존 방법에 무리 없이 통합되는 적응형 손실 균형 전략을 도입합니다. 이 프레임워크는 선형 시간 복잡도와 상수 공간 복잡도를 가지며, 7개의 실제 데이터셋에서 6개의 강력한 LTSF 기반을 대상으로 한 실험에서 평균적으로 예측 오류를 1.47%에서 9.19%까지, 변화값 오류를 4.57%에서 15.78%까지 감소시켜 성능을 크게 향상시켰습니다.

## 🎯 주요 포인트


- 1. 장기 시계열 예측(LTSF)에서 기존 방법의 성능 병목 현상은 목표 내 시간 종속성(TDT)의 부적절한 모델링에서 기인합니다.

- 2. 새로운 시간 모델링 프레임워크인 TDAlign은 기존 LTSF 방법에 TDT 학습 기능을 제공하여 이 문제를 해결합니다.

- 3. TDAlign은 인접 시간 단계의 변화 값을 정렬하는 손실 함수와 적응형 손실 균형 전략을 도입하여 기존 방법과의 통합을 용이하게 합니다.

- 4. TDAlign은 최소한의 계산 오버헤드로 기존 방법을 강화하며, 예측 길이에 대해 선형 시간 복잡도와 상수 공간 복잡도를 갖습니다.

- 5. 7개의 실제 데이터셋에서 6개의 강력한 LTSF 기준선에 대한 실험 결과, TDAlign은 평균적으로 예측 오류를 1.47%에서 9.19%까지 감소시킵니다.


---

*Generated on 2025-09-22 15:51:02*