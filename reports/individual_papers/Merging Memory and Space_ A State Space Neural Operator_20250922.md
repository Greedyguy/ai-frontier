# Merging Memory and Space: A State Space Neural Operator

**Korean Title:** 기억과 공간의 융합: 상태 공간 신경 연산자

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/specific/State Space Models|State Space Models]] [[keywords/specific/Frequency Modulation|Frequency Modulation]] [[keywords/broad/Neural Operator|Neural Operator]] [[keywords/broad/Partial Differential Equations|Partial Differential Equations]] [[keywords/unique/State Space Neural Operator|State Space Neural Operator]] [[categories/cs.LG|cs.LG]] [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (79.7% similar) [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks: A Second-Order Optimization Perspective]] (79.3% similar) [[2025-09-17/State Space Models over Directed Graphs_20250917|State Space Models over Directed Graphs]] (79.0% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive Damping
**🔗 Specific Connectable**: State Space Model
**🔬 Broad Technical**: Neural Operator, Partial Differential Equations
**⭐ Unique Technical**: State Space Neural Operator
## 🔗 유사한 논문
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (79.7% similar)
- [[2025-09-22/Gradient Alignment in Physics-informed Neural Networks_ A Second-Order Optimization Perspective_20250922|Gradient Alignment in Physics-informed Neural Networks A Second-Order Optimization Perspective]] (79.3% similar)
- [[2025-09-17/State Space Models over Directed Graphs_20250917|State Space Models over Directed Graphs]] (79.0% similar)
- [[2025-09-22/Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media_20250922|Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media]] (78.9% similar)
- [[2025-09-22/SPACE_ SPike-Aware Consistency Enhancement for Test-Time Adaptation in Spiking Neural Networks_20250922|SPACE SPike-Aware Consistency Enhancement for Test-Time Adaptation in Spiking Neural Networks]] (78.6% similar)


**ArXiv ID**: [2507.23428](https://arxiv.org/abs/2507.23428)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2507.23428.pdf)


**ArXiv ID**: [2507.23428](https://arxiv.org/abs/2507.23428)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2507.23428.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Spatiotemporal Modeling
**🔗 Specific Connectable**: State Space Models
**⭐ Unique Technical**: State Space Neural Operator
**🔬 Broad Technical**: Neural Operator, Partial Differential Equations

## 🏷️ 추출된 키워드



`Neural Operator` • 

`Partial Differential Equations` • 

`State Space Models` • 

`State Space Neural Operator` • 

`Adaptive Damping`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.23428v2 Announce Type: replace 
Abstract: We propose the State Space Neural Operator (SS-NO), a compact architecture for learning solution operators of time-dependent partial differential equations (PDEs). Our formulation extends structured state space models (SSMs) to joint spatiotemporal modeling, introducing two key mechanisms: adaptive damping, which stabilizes learning by localizing receptive fields, and learnable frequency modulation, which enables data-driven spectral selection. These components provide a unified framework for capturing long-range dependencies with parameter efficiency. Theoretically, we establish connections between SSMs and neural operators, proving a universality theorem for convolutional architectures with full field-of-view. Empirically, SS-NO achieves state-of-the-art performance across diverse PDE benchmarks-including 1D Burgers' and Kuramoto-Sivashinsky equations, and 2D Navier-Stokes and compressible Euler flows-while using significantly fewer parameters than competing approaches. A factorized variant of SS-NO further demonstrates scalable performance on challenging 2D problems. Our results highlight the effectiveness of damping and frequency learning in operator modeling, while showing that lightweight factorization provides a complementary path toward efficient large-scale PDE learning.

## 🔍 Abstract (한글 번역)

arXiv:2507.23428v2 발표 유형: 교체  
초록: 우리는 시간에 의존하는 편미분 방정식(PDE)의 해 연산자를 학습하기 위한 간결한 구조인 상태 공간 신경 연산자(SS-NO)를 제안합니다. 우리의 공식화는 구조화된 상태 공간 모델(SSM)을 확장하여 시공간 통합 모델링을 도입하며, 두 가지 주요 메커니즘을 소개합니다: 수용 영역을 국지화하여 학습을 안정화하는 적응 감쇠와 데이터 기반의 스펙트럼 선택을 가능하게 하는 학습 가능한 주파수 변조입니다. 이러한 구성 요소들은 매개변수 효율성을 유지하면서 장거리 의존성을 포착하기 위한 통합된 프레임워크를 제공합니다. 이론적으로, 우리는 SSM과 신경 연산자 간의 연결을 확립하고, 전체 시야를 갖춘 합성곱 구조에 대한 보편성 정리를 증명합니다. 실험적으로, SS-NO는 1D 버거스 방정식과 쿠라모토-시바신스키 방정식, 2D 나비에-스토크스 및 압축성 오일러 흐름을 포함한 다양한 PDE 벤치마크에서 최첨단 성능을 달성하며, 경쟁 접근법보다 훨씬 적은 매개변수를 사용합니다. SS-NO의 인수 분해된 변형은 도전적인 2D 문제에서 확장 가능한 성능을 추가로 입증합니다. 우리의 결과는 연산자 모델링에서 감쇠와 주파수 학습의 효과를 강조하며, 경량 인수 분해가 효율적인 대규모 PDE 학습을 위한 보완적인 경로를 제공함을 보여줍니다.

## 📝 요약

State Space Neural Operator (SS-NO)는 시공간적 모델링을 위한 컴팩트한 구조로, 시간 의존적 편미분 방정식(PDE)의 해 연산자를 학습하는 데 사용됩니다. SS-NO는 적응형 감쇠와 학습 가능한 주파수 변조를 도입하여 학습 안정성과 데이터 기반 스펙트럼 선택을 가능하게 합니다. 이 방법은 파라미터 효율성을 유지하면서 장거리 의존성을 포착할 수 있는 통합된 프레임워크를 제공합니다. 이론적으로는 SSM과 신경 연산자 간의 연결을 확립하고, 전 시야를 갖춘 컨볼루션 아키텍처의 보편성 정리를 증명했습니다. 실험적으로 SS-NO는 1D Burgers' 방정식, Kuramoto-Sivashinsky 방정식, 2D Navier-Stokes 및 압축성 Euler 흐름 등 다양한 PDE 벤치마크에서 최첨단 성능을 발휘하며, 경쟁 접근법보다 적은 파라미터를 사용합니다. 또한, SS-NO의 팩터화된 변형은 2D 문제에서 확장 가능한 성능을 보여줍니다. 이 연구는 감쇠와 주파수 학습이 연산자 모델링에 효과적임을 강조하며, 경량 팩터화가 대규모 PDE 학습의 효율성을 높이는 보완적 경로임을 시사합니다.

## 🎯 주요 포인트


- 1. State Space Neural Operator (SS-NO)는 시간에 따른 편미분 방정식(PDE)의 솔루션 연산자를 학습하기 위한 컴팩트한 아키텍처를 제안합니다.

- 2. SS-NO는 적응형 감쇠와 학습 가능한 주파수 변조를 통해 수용 영역을 국지화하고 데이터 기반의 스펙트럼 선택을 가능하게 합니다.

- 3. 이 아키텍처는 파라미터 효율성을 유지하면서 장거리 의존성을 포착할 수 있는 통합된 프레임워크를 제공합니다.

- 4. SS-NO는 다양한 PDE 벤치마크에서 최첨단 성능을 달성하며, 경쟁 접근법보다 훨씬 적은 파라미터를 사용합니다.

- 5. SS-NO의 경량화된 버전은 2D 문제에서 확장 가능한 성능을 보여주며, 대규모 PDE 학습의 효율성을 향상시킵니다.


---

*Generated on 2025-09-22 16:00:33*