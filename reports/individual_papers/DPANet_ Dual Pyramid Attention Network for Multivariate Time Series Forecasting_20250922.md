# DPANet: Dual Pyramid Attention Network for Multivariate Time Series Forecasting

**Korean Title:** DPANet: 다중 변수 시계열 예측을 위한 이중 피라미드 주의 네트워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Cross-Pyramid Fusion

## 🔗 유사한 논문
- [[2025-09-18/DPANet_ Dual Pyramid Attention Network for Multivariate Time Series Forecasting_20250918|DPANet Dual Pyramid Attention Network for Multivariate Time Series Forecasting]] (90.9% similar)
- [[2025-09-22/Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction_20250922|Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction]] (80.4% similar)
- [[2025-09-22/No Black Box Anymore_ Demystifying Clinical Predictive Modeling with Temporal-Feature Cross Attention Mechanism_20250922|No Black Box Anymore Demystifying Clinical Predictive Modeling with Temporal-Feature Cross Attention Mechanism]] (80.2% similar)
- [[2025-09-18/Beyond Marginals_ Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection_20250918|Beyond Marginals Learning Joint Spatio-Temporal Patterns for Multivariate Anomaly Detection]] (79.7% similar)
- [[2025-09-18/DeCoP_ Enhancing Self-Supervised Time Series Representation with Dependency Controlled Pre-training_20250918|DeCoP Enhancing Self-Supervised Time Series Representation with Dependency Controlled Pre-training]] (79.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14868v2 Announce Type: replace-cross 
Abstract: Long-term time series forecasting (LTSF) is hampered by the challenge of modeling complex dependencies that span multiple temporal scales and frequency resolutions. Existing methods, including Transformer and MLP-based models, often struggle to capture these intertwined characteristics in a unified and structured manner. We propose the Dual Pyramid Attention Network (DPANet), a novel architecture that explicitly decouples and concurrently models temporal multi-scale dynamics and spectral multi-resolution periodicities. DPANet constructs two parallel pyramids: a Temporal Pyramid built on progressive downsampling, and a Frequency Pyramid built on band-pass filtering. The core of our model is the Cross-Pyramid Fusion Block, which facilitates deep, interactive information exchange between corresponding pyramid levels via cross-attention. This fusion proceeds in a coarse-to-fine hierarchy, enabling global context to guide local representation learning. Extensive experiments on public benchmarks show that DPANet achieves state-of-the-art performance, significantly outperforming prior models. Code is available at https://github.com/hit636/DPANet.

## 🔍 Abstract (한글 번역)

arXiv:2509.14868v2 발표 유형: 교차 대체  
초록: 장기 시계열 예측(LTSF)은 여러 시간적 규모와 주파수 해상도를 아우르는 복잡한 종속성을 모델링하는 데 어려움을 겪고 있습니다. Transformer 및 MLP 기반 모델을 포함한 기존 방법들은 이러한 얽힌 특성을 통합적이고 구조적인 방식으로 포착하는 데 종종 어려움을 겪습니다. 우리는 시간적 다중 규모 동역학과 스펙트럼 다중 해상도 주기성을 명시적으로 분리하고 동시에 모델링하는 새로운 아키텍처인 이중 피라미드 주의 네트워크(DPANet)를 제안합니다. DPANet은 두 개의 병렬 피라미드를 구성합니다: 점진적 다운샘플링을 기반으로 한 시간 피라미드와 대역 통과 필터링을 기반으로 한 주파수 피라미드. 우리 모델의 핵심은 교차 주의 메커니즘을 통해 해당 피라미드 수준 간의 깊고 상호적인 정보 교환을 촉진하는 교차 피라미드 융합 블록입니다. 이 융합은 전역적 맥락이 지역적 표현 학습을 안내할 수 있도록 하는 거친-세밀한 계층 구조로 진행됩니다. 공공 벤치마크에 대한 광범위한 실험 결과, DPANet이 최첨단 성능을 달성하여 이전 모델을 크게 능가함을 보여줍니다. 코드는 https://github.com/hit636/DPANet에서 사용할 수 있습니다.

## 📝 요약

이 논문은 장기 시계열 예측(LTSF)의 복잡한 시간적 및 주파수적 의존성을 효과적으로 모델링하기 위한 새로운 아키텍처인 Dual Pyramid Attention Network(DPANet)를 제안합니다. 기존의 Transformer 및 MLP 기반 모델들이 이러한 복합적 특성을 포착하는 데 어려움을 겪는 반면, DPANet은 시간적 다중 스케일 동역학과 주파수 다중 해상도 주기성을 명시적으로 분리하여 동시에 모델링합니다. DPANet은 점진적 다운샘플링을 사용하는 Temporal Pyramid와 밴드 패스 필터링을 사용하는 Frequency Pyramid라는 두 개의 병렬 피라미드를 구축합니다. 핵심 구성 요소인 Cross-Pyramid Fusion Block은 피라미드 레벨 간의 깊고 상호적인 정보 교환을 가능하게 하여 전역 컨텍스트가 지역 표현 학습을 안내하도록 합니다. 공공 벤치마크 실험에서 DPANet은 기존 모델을 크게 능가하며 최첨단 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. 장기 시계열 예측(LTSF)은 여러 시간적 규모와 주파수 해상도를 아우르는 복잡한 의존성을 모델링하는 데 어려움을 겪고 있습니다.

- 2. 기존의 Transformer 및 MLP 기반 모델은 이러한 얽힌 특성을 통합적이고 구조적으로 포착하는 데 한계가 있습니다.

- 3. Dual Pyramid Attention Network(DPANet)는 시간적 다중 규모 동역학과 주파수 다중 해상도 주기성을 명시적으로 분리하고 동시에 모델링하는 새로운 아키텍처입니다.

- 4. DPANet는 점진적 다운샘플링을 기반으로 한 시간 피라미드와 대역 통과 필터링을 기반으로 한 주파수 피라미드의 두 개의 병렬 피라미드를 구성합니다.

- 5. DPANet는 공공 벤치마크에서 광범위한 실험을 통해 최첨단 성능을 달성하며, 이전 모델을 크게 능가합니다.

---

*Generated on 2025-09-22 15:07:33*