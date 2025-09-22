
# Spatio-Temporal Anomaly Detection with Graph Networks for Data Quality Monitoring of the Hadron Calorimeter

**Korean Title:** 스패시오-템포럴 이상 탐지와 그래프 네트워크를 활용한 하드론 칼로리미터의 데이터 품질 모니터링

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Spatio-Temporal Analysis, Graph Neural Network

## 🔗 유사한 논문
- [[Multimodal signal fusion for stress detection using deep neural networks a novel approach for converting 1D signals to unified 2D images]] (76.8% similar)
- [[Adversarial_Distilled_Retrieval-Augmented_Guarding_Model_for_Online_Malicious_Intent_Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (76.4% similar)
- [[TFLAGTowards Practical APT Detection via Deviation-Aware Learning on Temporal Provenance Graph]] (75.9% similar)
- [[Anomaly_Detection_in_Offshore_Open_Radio_Access_Network_Using_Long_Short-Term_Memory_Models_on_a_Novel_Artificial_Intelligence-Driven_Cloud-Native_Data_Platform_20250918|Anomaly Detection in Offshore Open Radio Access Network Using Long Short-Term Memory Models on a Novel Artificial Intelligence-Driven Cloud-Native Data Platform]] (75.8% similar)
- [[DSCC-HS A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models]] (75.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2311.04190v2 Announce Type: replace-cross 
Abstract: The Compact Muon Solenoid (CMS) experiment is a general-purpose detector for high-energy collision at the Large Hadron Collider (LHC) at CERN. It employs an online data quality monitoring (DQM) system to promptly spot and diagnose particle data acquisition problems to avoid data quality loss. In this study, we present a semi-supervised spatio-temporal anomaly detection (AD) monitoring system for the physics particle reading channels of the Hadron Calorimeter (HCAL) of the CMS using three-dimensional digi-occupancy map data of the DQM. We propose the GraphSTAD system, which employs convolutional and graph neural networks to learn local spatial characteristics induced by particles traversing the detector and the global behavior owing to shared backend circuit connections and housing boxes of the channels, respectively. Recurrent neural networks capture the temporal evolution of the extracted spatial features. We validate the accuracy of the proposed AD system in capturing diverse channel fault types using the LHC collision data sets. The GraphSTAD system achieves production-level accuracy and is being integrated into the CMS core production system for real-time monitoring of the HCAL. We provide a quantitative performance comparison with alternative benchmark models to demonstrate the promising leverage of the presented system. Code: \href{https://github.com/muleina/CMS_HCAL_ML_OnlineDQM}{https://github.com/muleina/CMS\_HCAL\_ML\_OnlineDQM}

## 🔍 Abstract (한글 번역)

arXiv:2311.04190v2 발표 유형: 교체-교차  
초록: 컴팩트 뮤온 솔레노이드(CMS) 실험은 CERN의 대형 강입자 충돌기(LHC)에서 고에너지 충돌을 위한 범용 검출기입니다. 이 실험은 데이터 품질 손실을 방지하기 위해 입자 데이터 수집 문제를 신속하게 발견하고 진단할 수 있는 온라인 데이터 품질 모니터링(DQM) 시스템을 사용합니다. 본 연구에서는 CMS의 하드론 칼로리미터(HCAL)의 물리 입자 판독 채널을 위한 반지도 학습 시공간 이상 탐지(AD) 모니터링 시스템을 제안합니다. 이 시스템은 DQM의 3차원 디지-점유 맵 데이터를 사용합니다. 우리는 입자가 검출기를 통과하면서 유도하는 국소 공간 특성과 채널의 공유 백엔드 회로 연결 및 하우징 박스에 기인하는 전역 행동을 학습하기 위해 컨볼루션 및 그래프 신경망을 사용하는 GraphSTAD 시스템을 제안합니다. 순환 신경망은 추출된 공간 특징의 시간적 변화를 포착합니다. 우리는 LHC 충돌 데이터 세트를 사용하여 다양한 채널 결함 유형을 포착하는 제안된 AD 시스템의 정확성을 검증합니다. GraphSTAD 시스템은 생산 수준의 정확성을 달성하며, HCAL의 실시간 모니터링을 위해 CMS 핵심 생산 시스템에 통합되고 있습니다. 우리는 제시된 시스템의 유망한 활용을 입증하기 위해 대체 벤치마크 모델과의 정량적 성능 비교를 제공합니다. 코드: \href{https://github.com/muleina/CMS_HCAL_ML_OnlineDQM}{https://github.com/muleina/CMS\_HCAL\_ML\_OnlineDQM}

## 📝 요약

이 연구는 CERN의 대형 강입자 충돌기(LHC)에서 고에너지 충돌을 감지하는 CMS 실험의 데이터 품질 모니터링 시스템을 개선하기 위해 제안된 방법론을 다룹니다. 연구진은 Hadron Calorimeter(HCAL)의 물리 입자 판독 채널을 위한 반지도 학습 기반의 시공간 이상 탐지 시스템(GraphSTAD)을 개발했습니다. 이 시스템은 컨볼루션 및 그래프 신경망을 활용하여 입자가 탐지기를 통과할 때 발생하는 국소적 공간 특성과 채널의 백엔드 회로 연결 및 하우징 박스에 의한 글로벌 행동을 학습합니다. 또한, 순환 신경망을 통해 추출된 공간 특징의 시간적 변화를 포착합니다. 이 시스템은 LHC 충돌 데이터 세트를 통해 다양한 채널 결함 유형을 정확히 탐지하는 것으로 검증되었으며, 실시간 HCAL 모니터링을 위해 CMS 핵심 생산 시스템에 통합되고 있습니다. 연구는 대체 모델과의 성능 비교를 통해 제안된 시스템의 우수성을 입증합니다.

## 🎯 주요 포인트

- 1. CMS 실험은 고에너지 충돌 실험에서 데이터 품질 손실을 방지하기 위해 온라인 데이터 품질 모니터링 시스템을 사용합니다.

- 2. 제안된 GraphSTAD 시스템은 컨볼루션 및 그래프 신경망을 활용하여 입자가 검출기를 통과할 때 발생하는 지역적 공간 특성과 채널의 공유 백엔드 회로 연결 및 하우징 박스에 의한 전역적 행동을 학습합니다.

- 3. 제안된 이상 탐지 시스템은 LHC 충돌 데이터 세트를 사용하여 다양한 채널 결함 유형을 정확하게 포착하는 것으로 검증되었습니다.

- 4. GraphSTAD 시스템은 실시간 HCAL 모니터링을 위해 CMS 핵심 생산 시스템에 통합되고 있으며, 생산 수준의 정확도를 달성했습니다.

- 5. 제안된 시스템의 유망한 활용을 입증하기 위해 대체 벤치마크 모델과의 정량적 성능 비교가 제공됩니다.

---

*Generated on 2025-09-19 15:10:44*