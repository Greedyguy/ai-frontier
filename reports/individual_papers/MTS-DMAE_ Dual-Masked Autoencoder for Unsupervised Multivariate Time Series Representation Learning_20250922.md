# MTS-DMAE: Dual-Masked Autoencoder for Unsupervised Multivariate Time Series Representation Learning

**Korean Title:** MTS-DMAE: 비지도 다변량 시계열 표현 학습을 위한 이중 마스크 자동 인코더

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Masked Autoencoder, Representation Learning

## 🔗 유사한 논문
- [[2025-09-18/Masked Feature Modeling Enhances Adaptive Segmentation_20250918|Masked Feature Modeling Enhances Adaptive Segmentation]] (81.5% similar)
- [[2025-09-22/VMDNet_ Time Series Forecasting with Leakage-Free Samplewise Variational Mode Decomposition and Multibranch Decoding_20250922|VMDNet Time Series Forecasting with Leakage-Free Samplewise Variational Mode Decomposition and Multibranch Decoding]] (80.7% similar)
- [[2025-09-17/Bridging Past and Future_ Distribution-Aware Alignment for Time Series Forecasting_20250917|Bridging Past and Future Distribution-Aware Alignment for Time Series Forecasting]] (80.6% similar)
- [[2025-09-18/Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (80.3% similar)
- [[2025-09-18/CSMoE_ An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts_20250918|CSMoE An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts]] (80.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16078v1 Announce Type: new 
Abstract: Unsupervised multivariate time series (MTS) representation learning aims to extract compact and informative representations from raw sequences without relying on labels, enabling efficient transfer to diverse downstream tasks. In this paper, we propose Dual-Masked Autoencoder (DMAE), a novel masked time-series modeling framework for unsupervised MTS representation learning. DMAE formulates two complementary pretext tasks: (1) reconstructing masked values based on visible attributes, and (2) estimating latent representations of masked features, guided by a teacher encoder. To further improve representation quality, we introduce a feature-level alignment constraint that encourages the predicted latent representations to align with the teacher's outputs. By jointly optimizing these objectives, DMAE learns temporally coherent and semantically rich representations. Comprehensive evaluations across classification, regression, and forecasting tasks demonstrate that our approach achieves consistent and superior performance over competitive baselines.

## 🔍 Abstract (한글 번역)

arXiv:2509.16078v1 발표 유형: 새로운 것  
초록: 비지도 다변량 시계열(MTS) 표현 학습은 레이블에 의존하지 않고 원시 시퀀스로부터 간결하고 정보가 풍부한 표현을 추출하여 다양한 다운스트림 작업으로의 효율적인 전이를 가능하게 하는 것을 목표로 합니다. 이 논문에서는 비지도 MTS 표현 학습을 위한 새로운 마스크드 시계열 모델링 프레임워크인 Dual-Masked Autoencoder (DMAE)를 제안합니다. DMAE는 두 가지 상호 보완적인 사전 작업을 구성합니다: (1) 보이는 속성을 기반으로 마스크된 값을 재구성하고, (2) 교사 인코더에 의해 안내되는 마스크된 특징의 잠재 표현을 추정하는 것입니다. 표현의 품질을 더욱 향상시키기 위해, 우리는 예측된 잠재 표현이 교사의 출력과 정렬되도록 유도하는 특징 수준의 정렬 제약을 도입합니다. 이러한 목표를 공동으로 최적화함으로써 DMAE는 시간적으로 일관되고 의미적으로 풍부한 표현을 학습합니다. 분류, 회귀 및 예측 작업 전반에 걸친 종합적인 평가를 통해 우리의 접근 방식이 경쟁력 있는 기준선에 비해 일관되고 우수한 성능을 달성함을 입증합니다.

## 📝 요약

이 논문은 비지도 다변량 시계열(MTS) 표현 학습을 위한 새로운 프레임워크인 Dual-Masked Autoencoder (DMAE)를 제안합니다. DMAE는 두 가지 보조 과제를 통해 시계열 데이터를 모델링합니다: (1) 보이는 속성을 기반으로 마스킹된 값을 재구성하고, (2) 교사 인코더의 지도를 받아 마스킹된 특징의 잠재 표현을 추정합니다. 또한, 예측된 잠재 표현이 교사의 출력과 일치하도록 하는 특징 수준 정렬 제약을 도입하여 표현의 품질을 향상시킵니다. 이러한 목표를 공동 최적화함으로써 DMAE는 시간적으로 일관되고 의미적으로 풍부한 표현을 학습합니다. 분류, 회귀, 예측 작업에 대한 종합적인 평가 결과, 제안된 방법이 기존의 경쟁 방법들보다 일관되고 우수한 성능을 보임을 확인했습니다.

## 🎯 주요 포인트

- 1. Dual-Masked Autoencoder (DMAE)는 비지도 다변량 시계열 표현 학습을 위한 새로운 마스킹 시계열 모델링 프레임워크입니다.

- 2. DMAE는 두 가지 보완적인 사전 과제를 설정하여, 가시 속성을 기반으로 마스킹된 값을 재구성하고, 교사 인코더의 지도를 받아 마스킹된 특징의 잠재 표현을 추정합니다.

- 3. 표현의 질을 향상시키기 위해, 예측된 잠재 표현이 교사의 출력과 정렬되도록 하는 특징 수준의 정렬 제약을 도입했습니다.

- 4. DMAE는 시간적으로 일관되고 의미적으로 풍부한 표현을 학습하며, 분류, 회귀, 예측 작업 전반에서 경쟁력 있는 기준보다 일관되고 우수한 성능을 보여줍니다.

---

*Generated on 2025-09-22 15:31:34*