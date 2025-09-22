# Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media

**Korean Title:** 공간-시간적, 다중 필드 심층 학습을 통한 중간 구조 매체에서의 충격 전파 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Autoregressive Surrogate

## 🔗 유사한 논문
- [[2025-09-18/Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model_20250918|Lightweight and Accurate Multi-View Stereo with Confidence-Aware Diffusion Model]] (81.2% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (81.0% similar)
- [[2025-09-18/Towards universal property prediction in Cartesian space_ TACE is all you need_20250918|Towards universal property prediction in Cartesian space TACE is all you need]] (80.5% similar)
- [[2025-09-18/Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (79.7% similar)
- [[2025-09-22/An Equivariant Graph Network for Interpretable Nanoporous Materials Design_20250922|An Equivariant Graph Network for Interpretable Nanoporous Materials Design]] (79.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16139v1 Announce Type: new 
Abstract: The ability to predict how shock waves traverse porous and architected materials is a decisive factor in planetary defense, national security, and the race to achieve inertial fusion energy. Yet capturing pore collapse, anomalous Hugoniot responses, and localized heating -- phenomena that can determine the success of asteroid deflection or fusion ignition -- has remained a major challenge despite recent advances in single-field and reduced representations. We introduce a multi-field spatio-temporal deep learning model (MSTM) that unifies seven coupled fields -- pressure, density, temperature, energy, material distribution, and two velocity components -- into a single autoregressive surrogate. Trained on high-fidelity hydrocode data, MSTM runs about a thousand times faster than direct simulation, achieving errors below 4\% in porous materials and below 10\% in lattice structures. Unlike prior single-field or operator-based surrogates, MSTM resolves sharp shock fronts while preserving integrated quantities such as mass-averaged pressure and temperature to within 5\%. This advance transforms problems once considered intractable into tractable design studies, establishing a practical framework for optimizing meso-structured materials in planetary impact mitigation, inertial fusion energy, and national security.

## 🔍 Abstract (한글 번역)

arXiv:2509.16139v1 발표 유형: 신규  
초록: 충격파가 다공성 및 구조화된 재료를 어떻게 통과하는지를 예측하는 능력은 행성 방어, 국가 안보, 그리고 관성 융합 에너지를 달성하기 위한 경쟁에서 결정적인 요소입니다. 그러나 최근 단일 필드 및 축소 표현에서의 발전에도 불구하고, 공극 붕괴, 비정상적인 Hugoniot 반응, 국부적 가열과 같은 현상을 포착하는 것은 여전히 주요 과제로 남아 있습니다. 이러한 현상은 소행성 편향이나 융합 점화의 성공을 결정할 수 있습니다. 우리는 7개의 결합된 필드 -- 압력, 밀도, 온도, 에너지, 물질 분포, 그리고 두 개의 속도 성분 -- 를 단일 자기회귀 대리모델로 통합하는 다중 필드 시공간 딥러닝 모델(MSTM)을 소개합니다. 고충실도 유체역학 코드 데이터를 기반으로 훈련된 MSTM은 직접 시뮬레이션보다 약 천 배 빠르게 실행되며, 다공성 재료에서는 4% 이하, 격자 구조에서는 10% 이하의 오류를 달성합니다. 이전의 단일 필드 또는 연산자 기반 대리모델과 달리, MSTM은 질량 평균 압력 및 온도와 같은 통합된 양을 5% 이내로 유지하면서도 날카로운 충격 전선을 해결합니다. 이 진보는 한때 해결 불가능하다고 여겨졌던 문제를 해결 가능한 설계 연구로 변환하여, 행성 충돌 완화, 관성 융합 에너지, 국가 안보에서 중간 구조 재료를 최적화하기 위한 실용적인 프레임워크를 확립합니다.

## 📝 요약

이 논문은 다공성 및 구조화된 물질에서 충격파의 전파를 예측하는 새로운 다중 필드 시공간 딥러닝 모델(MSTM)을 제안합니다. 이 모델은 압력, 밀도, 온도, 에너지, 물질 분포 및 두 개의 속도 성분을 포함한 7개의 필드를 통합하여 단일 대리 모델로 작동합니다. 고정밀 하이드로코드 데이터로 훈련된 MSTM은 직접 시뮬레이션보다 약 천 배 빠르게 실행되며, 다공성 물질에서는 4% 이하, 격자 구조에서는 10% 이하의 오차를 달성합니다. 기존의 단일 필드 또는 연산자 기반 대리 모델과 달리, MSTM은 충격파의 급격한 전선을 해결하면서도 질량 평균 압력 및 온도와 같은 통합된 양을 5% 이내로 유지합니다. 이 모델은 행성 충돌 완화, 관성 융합 에너지 및 국가 안보 분야에서 중간 구조 물질을 최적화할 수 있는 실용적인 프레임워크를 제공합니다.

## 🎯 주요 포인트

- 1. 다중장 시공간 딥러닝 모델(MSTM)은 압력, 밀도, 온도, 에너지, 물질 분포, 두 개의 속도 성분 등 일곱 개의 결합된 장을 통합하여 자동회귀 대리모델을 형성합니다.

- 2. MSTM은 고품질 하이드로코드 데이터를 기반으로 훈련되어, 직접 시뮬레이션보다 약 천 배 빠르게 실행되며, 다공성 물질에서 4% 이하, 격자 구조에서 10% 이하의 오류를 달성합니다.

- 3. MSTM은 이전의 단일장 또는 연산자 기반 대리모델과 달리, 질량 평균 압력 및 온도와 같은 통합된 양을 5% 이내로 유지하면서도 날카로운 충격파 전선을 해결합니다.

- 4. 이 모델은 행성 충돌 완화, 관성 융합 에너지, 국가 안보에서 중간 구조 물질을 최적화하기 위한 실용적인 프레임워크를 확립하여, 한때 난해했던 문제들을 해결 가능한 설계 연구로 전환합니다.

---

*Generated on 2025-09-22 15:33:34*