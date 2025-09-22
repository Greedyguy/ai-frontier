# Spatio-Temporal Anomaly Detection with Graph Networks for Data Quality Monitoring of the Hadron Calorimeter

**Korean Title:** 시공간 이상 탐지를 위한 그래프 네트워크를 활용한 하드론 칼로리미터의 데이터 품질 모니터링

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Spatio-Temporal Analysis, Graph Neural Network

## 🔗 유사한 논문
- [[2025-09-19/DINAMO_ Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments_20250919|DINAMO Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments]] (81.9% similar)
- [[2025-09-17/Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations_20250917|Deep Temporal Graph Networks for Real-Time Correction of GNSS Jamming-Induced Deviations]] (80.2% similar)
- [[2025-09-17/H-Alpha Anomalyzer_ An Explainable Anomaly Detector for Solar H-Alpha Observations_20250917|H-Alpha Anomalyzer An Explainable Anomaly Detector for Solar H-Alpha Observations]] (78.5% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (78.2% similar)
- [[2025-09-17/DSCC-HS_ A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models_20250917|DSCC-HS A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (77.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2311.04190v3 Announce Type: replace-cross 
Abstract: The Compact Muon Solenoid (CMS) experiment is a general-purpose detector for high-energy collision at the Large Hadron Collider (LHC) at CERN. It employs an online data quality monitoring (DQM) system to promptly spot and diagnose particle data acquisition problems to avoid data quality loss. In this study, we present a semi-supervised spatio-temporal anomaly detection (AD) monitoring system for the physics particle reading channels of the Hadron Calorimeter (HCAL) of the CMS using three-dimensional digi-occupancy map data of the DQM. We propose the GraphSTAD system, which employs convolutional and graph neural networks to learn local spatial characteristics induced by particles traversing the detector and the global behavior owing to shared backend circuit connections and housing boxes of the channels, respectively. Recurrent neural networks capture the temporal evolution of the extracted spatial features. We validate the accuracy of the proposed AD system in capturing diverse channel fault types using the LHC collision data sets. The GraphSTAD system achieves production-level accuracy and is being integrated into the CMS core production system for real-time monitoring of the HCAL. We provide a quantitative performance comparison with alternative benchmark models to demonstrate the promising leverage of the presented system. Code: https://github.com/muleina/CMS_HCAL_ML_OnlineDQM .

## 🔍 Abstract (한글 번역)

arXiv:2311.04190v3 발표 유형: 교차 교체  
초록: 컴팩트 뮤온 솔레노이드(CMS) 실험은 CERN의 대형 강입자 충돌기(LHC)에서 고에너지 충돌을 위한 범용 검출기입니다. 이 실험은 데이터 품질 손실을 방지하기 위해 입자 데이터 수집 문제를 신속히 발견하고 진단하기 위한 온라인 데이터 품질 모니터링(DQM) 시스템을 사용합니다. 본 연구에서는 CMS의 하드론 칼로리미터(HCAL)의 물리 입자 판독 채널을 위한 반지도 시공간 이상 탐지(AD) 모니터링 시스템을 제안합니다. 이 시스템은 DQM의 3차원 디지털 점유 지도 데이터를 사용합니다. 우리는 입자가 검출기를 통과하면서 유도되는 국소적 공간 특성과 채널의 공유 백엔드 회로 연결 및 하우징 박스에 기인한 전역적 행동을 학습하기 위해 컨볼루션 및 그래프 신경망을 사용하는 GraphSTAD 시스템을 제안합니다. 순환 신경망은 추출된 공간 특징의 시간적 변화를 포착합니다. 우리는 LHC 충돌 데이터 세트를 사용하여 다양한 채널 결함 유형을 포착하는 제안된 AD 시스템의 정확성을 검증합니다. GraphSTAD 시스템은 생산 수준의 정확성을 달성하며, HCAL의 실시간 모니터링을 위해 CMS 핵심 생산 시스템에 통합되고 있습니다. 우리는 제시된 시스템의 유망한 활용을 입증하기 위해 대체 벤치마크 모델과의 정량적 성능 비교를 제공합니다. 코드: https://github.com/muleina/CMS_HCAL_ML_OnlineDQM .

## 📝 요약

이 연구는 CERN의 대형 강입자 충돌기(LHC)에서 고에너지 충돌을 감지하는 CMS 실험의 하드론 칼로리미터(HCAL)에서 발생하는 데이터 문제를 신속히 파악하기 위한 반지도 시공간 이상 탐지 시스템을 제안합니다. 제안된 GraphSTAD 시스템은 컨볼루션 및 그래프 신경망을 활용하여 입자가 탐지기를 통과할 때 발생하는 지역적 공간 특성과 채널의 공유 백엔드 회로 연결 및 하우징 박스에 따른 전역적 행동을 학습합니다. 또한, 순환 신경망을 통해 추출된 공간 특성의 시간적 변화를 포착합니다. LHC 충돌 데이터 세트를 사용하여 다양한 채널 결함 유형을 정확히 탐지하는 시스템의 성능을 검증하였으며, 실제 CMS 생산 시스템에 통합되어 HCAL의 실시간 모니터링에 활용되고 있습니다. 제안된 시스템의 성능은 대체 벤치마크 모델과의 비교를 통해 입증되었습니다.

## 🎯 주요 포인트

- 1. CMS 실험의 하드론 칼로리미터(HCAL)에서 입자 데이터 수집 문제를 신속히 감지하기 위해 반지도 학습 기반의 시공간 이상 탐지 시스템을 제안합니다.

- 2. GraphSTAD 시스템은 합성곱 및 그래프 신경망을 활용하여 입자가 탐지기를 통과할 때 발생하는 지역적 공간 특성과 채널의 공유 백엔드 회로 연결 및 하우징 박스에 따른 글로벌 행동을 학습합니다.

- 3. 제안된 이상 탐지 시스템은 LHC 충돌 데이터 세트를 사용하여 다양한 채널 결함 유형을 포착하는 정확성을 검증하였습니다.

- 4. GraphSTAD 시스템은 실시간 HCAL 모니터링을 위해 CMS 핵심 생산 시스템에 통합되고 있으며, 생산 수준의 정확성을 달성하였습니다.

- 5. 대체 벤치마크 모델과의 성능 비교를 통해 제안된 시스템의 유망한 활용 가능성을 입증하였습니다.

---

*Generated on 2025-09-22 14:35:03*