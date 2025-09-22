# ChannelFlow-Tools: A Standardized Dataset Creation Pipeline for 3D Obstructed Channel Flows

**Korean Title:** 채널플로우-툴스: 3D 장애물 채널 흐름을 위한 표준화된 데이터셋 생성 파이프라인

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Voxelization, Hydrodynamic Simulation

## 🔗 유사한 논문
- [[2025-09-19/FlowDrive_ Energy Flow Field for End-to-End Autonomous Driving_20250919|FlowDrive Energy Flow Field for End-to-End Autonomous Driving]] (78.8% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (77.9% similar)
- [[2025-09-19/WorldForge_ Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance_20250919|WorldForge Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance]] (77.6% similar)
- [[2025-09-18/FlowCast-ODE_ Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration_20250918|FlowCast-ODE Continuous Hourly Weather Forecasting with Dynamic Flow Matching and ODE Integration]] (77.5% similar)
- [[2025-09-18/Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit_20250918|Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit]] (76.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15236v1 Announce Type: cross 
Abstract: We present ChannelFlow-Tools, a configuration-driven framework that standardizes the end-to-end path from programmatic CAD solid generation to ML-ready inputs and targets for 3D obstructed channel flows. The toolchain integrates geometry synthesis with feasibility checks, signed distance field (SDF) voxelization, automated solver orchestration on HPC (waLBerla LBM), and Cartesian resampling to co-registered multi-resolution tensors. A single Hydra/OmegaConf configuration governs all stages, enabling deterministic reproduction and controlled ablations. As a case study, we generate 10k+ scenes spanning Re=100-15000 with diverse shapes and poses. An end-to-end evaluation of storage trade-offs directly from the emitted artifacts, a minimal 3D U-Net at 128x32x32, and example surrogate models with dataset size illustrate that the standardized representations support reproducible ML training. ChannelFlow-Tools turns one-off dataset creation into a reproducible, configurable pipeline for CFD surrogate modeling.

## 🔍 Abstract (한글 번역)

arXiv:2509.15236v1 발표 유형: 교차  
초록: 우리는 ChannelFlow-Tools를 소개합니다. 이는 프로그래매틱 CAD 솔리드 생성에서 ML 준비 입력 및 3D 장애물 채널 흐름의 목표까지의 종단 간 경로를 표준화하는 구성 기반 프레임워크입니다. 이 도구 체인은 기하학 합성을 타당성 검사, 서명 거리 필드(SDF) 복셀화, HPC(waLBerla LBM)에서의 자동화된 솔버 조정, 공동 등록된 다중 해상도 텐서로의 직교 재샘플링과 통합합니다. 단일 Hydra/OmegaConf 구성이 모든 단계를 관리하여 결정론적 재현과 통제된 제거를 가능하게 합니다. 사례 연구로서, 우리는 다양한 형태와 자세를 가진 Re=100-15000 범위의 10,000개 이상의 장면을 생성합니다. 방출된 아티팩트로부터 직접적인 저장소 절충에 대한 종단 간 평가, 128x32x32의 최소 3D U-Net, 그리고 데이터셋 크기를 고려한 예제 대리 모델은 표준화된 표현이 재현 가능한 ML 훈련을 지원함을 보여줍니다. ChannelFlow-Tools는 일회성 데이터셋 생성을 CFD 대리 모델링을 위한 재현 가능하고 구성 가능한 파이프라인으로 전환합니다.

## 📝 요약

ChannelFlow-Tools는 프로그램 기반 CAD 고체 생성부터 기계 학습 준비 입력 및 목표 생성까지의 경로를 표준화하는 프레임워크입니다. 이 도구는 기하학적 합성, 타당성 검사, 서명 거리 필드(SDF) 복셀화, HPC에서의 자동 솔버 조정, 다중 해상도 텐서로의 직교 재샘플링을 통합합니다. Hydra/OmegaConf 설정을 통해 모든 단계를 제어하여 재현 가능성을 보장합니다. 사례 연구로 다양한 형태와 자세를 가진 10,000개 이상의 장면을 생성하고, 3D U-Net 및 대리 모델을 사용하여 ML 훈련의 재현 가능성을 입증합니다. ChannelFlow-Tools는 CFD 대리 모델링을 위한 재현 가능한 파이프라인을 제공합니다.

## 🎯 주요 포인트

- 1. ChannelFlow-Tools는 3D 장애물 채널 흐름을 위한 프로그램적 CAD 솔리드 생성부터 ML 준비 입력 및 목표까지의 경로를 표준화하는 프레임워크입니다.

- 2. 이 도구 체인은 기하학적 합성, 타당성 검사, 서명 거리 필드(SDF) 복셀화, HPC에서의 자동 솔버 오케스트레이션, 그리고 다중 해상도 텐서로의 직교 재샘플링을 통합합니다.

- 3. Hydra/OmegaConf 구성 하나로 모든 단계를 제어하여 결정론적 재현성과 제어된 소거를 가능하게 합니다.

- 4. 다양한 형태와 자세를 포함한 10,000개 이상의 장면을 생성하여 데이터셋 크기에 따른 저장소 절충 평가를 수행합니다.

- 5. ChannelFlow-Tools는 CFD 대리 모델링을 위한 재현 가능하고 구성 가능한 파이프라인으로 일회성 데이터셋 생성을 전환합니다.

---

*Generated on 2025-09-22 13:48:01*