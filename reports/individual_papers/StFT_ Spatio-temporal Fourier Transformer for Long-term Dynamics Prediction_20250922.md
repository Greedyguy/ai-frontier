# StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction

**Korean Title:** StFT: 장기 동역학 예측을 위한 시공간 푸리에 변환기

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Autoregressive Spatio-temporal Modeling|Autoregressive Spatio-temporal Modeling]] [[keywords/specific/Frequency-domain Representation|Frequency-domain Representation]] [[keywords/broad/Neural Operators|Neural Operators]] [[keywords/broad/Transformer|Transformer]] [[keywords/unique/Spatio-temporal Fourier Transformer|Spatio-temporal Fourier Transformer]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media_20250922|Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media]] (82.9% similar) [[2025-09-22/DPANet_ Dual Pyramid Attention Network for Multivariate Time Series Forecasting_20250922|DPANet: Dual Pyramid Attention Network for Multivariate Time Series Forecasting]] (82.3% similar) [[2025-09-22/Modeling Temporal Dependencies within the Target for Long-Term Time Series Forecasting_20250922|Modeling Temporal Dependencies within the Target for Long-Term Time Series Forecasting]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Autoregressive Spatio-temporal Modeling
**🔗 Specific Connectable**: Frequency-domain Representation
**🔬 Broad Technical**: Neural Operators, Transformer
**⭐ Unique Technical**: Spatio-temporal Fourier Transformer
## 🔗 유사한 논문
- [[2025-09-22/Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media_20250922|Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media]] (82.9% similar)
- [[2025-09-22/DPANet_ Dual Pyramid Attention Network for Multivariate Time Series Forecasting_20250922|DPANet Dual Pyramid Attention Network for Multivariate Time Series Forecasting]] (82.3% similar)
- [[2025-09-22/Modeling Temporal Dependencies within the Target for Long-Term Time Series Forecasting_20250922|Modeling Temporal Dependencies within the Target for Long-Term Time Series Forecasting]] (82.0% similar)
- [[2025-09-18/Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (82.0% similar)
- [[2025-09-22/Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets_20250922|Incremental Multistep Forecasting of Battery Degradation Using Pseudo Targets]] (81.9% similar)


**ArXiv ID**: [2503.11899](https://arxiv.org/abs/2503.11899)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2503.11899.pdf)


**ArXiv ID**: [2503.11899](https://arxiv.org/abs/2503.11899)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2503.11899.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Autoregressive Spatio-temporal Modeling
**🔗 Specific Connectable**: Neural Operators, Frequency-domain Representation
**⭐ Unique Technical**: Spatio-temporal Fourier Transformer
**🔬 Broad Technical**: Transformer

## 🏷️ 추출된 키워드



`Neural Operators` • 

`Transformer` • 

`Frequency-domain Representation` • 

`Spatio-temporal Fourier Transformer` • 

`Autoregressive Spatio-temporal Modeling`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.11899v2 Announce Type: replace 
Abstract: Simulating the long-term dynamics of multi-scale and multi-physics systems poses a significant challenge in understanding complex phenomena across science and engineering. The complexity arises from the intricate interactions between scales and the interplay of diverse physical processes, which manifest in PDEs through coupled, nonlinear terms that govern the evolution of multiple physical fields across scales. Neural operators have shown potential in short-term prediction of such complex spatio-temporal dynamics; however, achieving stable high-fidelity predictions and providing robust uncertainty quantification over extended time horizons remains an open and unsolved area of research. These limitations often lead to stability degradation with rapid error accumulation, particularly in long-term forecasting of systems characterized by multi-scale behaviors involving dynamics of different orders. To address these challenges, we propose an autoregressive Spatio-temporal Fourier Transformer (StFT), in which each transformer block is designed to learn the system dynamics at a distinct scale through a dual-path architecture that integrates frequency-domain and spatio-temporal representations. By leveraging a structured hierarchy of \ours blocks, the resulting model explicitly captures the underlying dynamics across both macro- and micro- spatial scales. Furthermore, a generative residual correction mechanism is introduced to learn a probabilistic refinement temporally while simultaneously quantifying prediction uncertainties, enhancing both the accuracy and reliability of long-term probabilistic forecasting. Evaluations conducted on three benchmark datasets (plasma, fluid, and atmospheric dynamics) demonstrate the advantages of our approach over state-of-the-art ML methods.

## 🔍 Abstract (한글 번역)

arXiv:2503.11899v2 발표 유형: 교체  
초록: 다중 스케일 및 다중 물리 시스템의 장기 동역학을 시뮬레이션하는 것은 과학 및 공학 전반에 걸쳐 복잡한 현상을 이해하는 데 있어 상당한 도전 과제를 제시합니다. 이러한 복잡성은 스케일 간의 복잡한 상호작용과 다양한 물리적 과정의 상호작용에서 발생하며, 이는 여러 물리적 장의 진화를 지배하는 결합된 비선형 항을 통해 편미분 방정식(PDE)에 나타납니다. 신경 연산자는 이러한 복잡한 시공간 동역학의 단기 예측에서 잠재력을 보여주었지만, 장기적인 시간 범위에서 안정적인 고충실도 예측을 달성하고 강력한 불확실성 정량화를 제공하는 것은 여전히 미해결 연구 분야로 남아 있습니다. 이러한 제한은 특히 다양한 차수의 동역학을 포함하는 다중 스케일 행동으로 특징지어지는 시스템의 장기 예측에서 빠른 오류 축적과 함께 안정성 저하로 이어지는 경우가 많습니다. 이러한 문제를 해결하기 위해 우리는 주파수 도메인과 시공간 표현을 통합하는 이중 경로 아키텍처를 통해 각 트랜스포머 블록이 고유한 스케일에서 시스템 동역학을 학습하도록 설계된 자기회귀적 시공간 푸리에 트랜스포머(StFT)를 제안합니다. 구조화된 \ours 블록의 계층을 활용하여, 결과 모델은 거시적 및 미시적 공간 스케일 모두에서 기본 동역학을 명시적으로 포착합니다. 또한, 생성적 잔차 보정 메커니즘을 도입하여 예측 불확실성을 정량화하면서 동시에 시간적으로 확률적 세부 조정을 학습하여 장기 확률 예측의 정확성과 신뢰성을 모두 향상시킵니다. 플라즈마, 유체, 대기 동역학의 세 가지 벤치마크 데이터셋에 대해 수행된 평가 결과, 우리의 접근 방식이 최첨단 기계 학습 방법보다 우수하다는 것이 입증되었습니다.

## 📝 요약

이 논문은 다중 스케일 및 다중 물리 시스템의 장기 동역학 시뮬레이션의 어려움을 해결하기 위해 새로운 방법론을 제안합니다. 기존의 신경망 연산자는 단기 예측에 효과적이지만, 장기 예측에서는 안정성과 신뢰성 문제가 발생합니다. 이를 해결하기 위해 저자들은 주파수 도메인과 시공간 표현을 통합한 이중 경로 구조의 자기회귀적 시공간 푸리에 변환기(StFT)를 제안합니다. 이 모델은 다양한 스케일의 동역학을 명시적으로 포착하며, 생성적 잔차 보정 메커니즘을 통해 예측 불확실성을 정량화하고 장기 예측의 정확성과 신뢰성을 높입니다. 세 가지 벤치마크 데이터셋(플라즈마, 유체, 대기 역학)에서의 평가 결과, 제안된 방법이 기존 최첨단 기계 학습 방법보다 우수한 성능을 보였습니다.

## 🎯 주요 포인트


- 1. 다중 스케일 및 다중 물리 시스템의 장기 동역학 시뮬레이션은 복잡한 상호작용으로 인해 어려움을 겪고 있다.

- 2. 신경 연산자는 단기 예측에 잠재력을 보였으나, 장기 예측의 안정성과 불확실성 정량화는 여전히 해결되지 않은 문제로 남아 있다.

- 3. 제안된 자기회귀 시공간 푸리에 변환기(StFT)는 주파수 영역과 시공간 표현을 통합하여 각 스케일의 시스템 동역학을 학습한다.

- 4. 생성적 잔여 보정 메커니즘을 통해 장기 확률적 예측의 정확성과 신뢰성을 향상시킨다.

- 5. 세 가지 벤치마크 데이터셋(플라즈마, 유체, 대기 역학) 평가에서 제안된 접근 방식이 최신 기계 학습 방법보다 우수한 성능을 보였다.


---

*Generated on 2025-09-22 15:55:55*