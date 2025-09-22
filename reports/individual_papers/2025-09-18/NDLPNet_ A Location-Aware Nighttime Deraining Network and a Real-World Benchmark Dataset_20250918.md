
# NDLPNet: A Location-Aware Nighttime Deraining Network and a Real-World Benchmark Dataset

**Korean Title:** NDLPNet: 위치 인식형 야간 비 제거 네트워크 및 현실 세계 벤치마크 데이터셋

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Nighttime Deraining Task

## 🔗 유사한 논문
- [[Performance_Optimization_of_YOLO-FEDER_FusionNet_for_Robust_Drone_Detection_in_Visually_Complex_Environments_20250918|Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments]] (78.8% similar)
- [[Federated_Learning_for_Deforestation_Detection_A_Distributed_Approach_with_Satellite_Imagery_20250918|Federated Learning for Deforestation Detection: A Distributed Approach with Satellite Imagery]] (78.0% similar)
- [[BERTector_An_Intrusion_Detection_Framework_Constructed_via_Joint-dataset_Learning_Based_on_Language_Model_20250918|BERTector: An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model]] (77.9% similar)
- [[Search-TTA: A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild]] (77.5% similar)
- [[Semantic-Enhanced_Cross-Modal_Place_Recognition_for_Robust_Robot_Localization_20250918|Semantic-Enhanced Cross-Modal Place Recognition for Robust Robot Localization]] (77.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13766v1 Announce Type: new 
Abstract: Visual degradation caused by rain streak artifacts in low-light conditions significantly hampers the performance of nighttime surveillance and autonomous navigation. Existing image deraining techniques are primarily designed for daytime conditions and perform poorly under nighttime illumination due to the spatial heterogeneity of rain distribution and the impact of light-dependent stripe visibility. In this paper, we propose a novel Nighttime Deraining Location-enhanced Perceptual Network(NDLPNet) that effectively captures the spatial positional information and density distribution of rain streaks in low-light environments. Specifically, we introduce a Position Perception Module (PPM) to capture and leverage spatial contextual information from input data, enhancing the model's capability to identify and recalibrate the importance of different feature channels. The proposed nighttime deraining network can effectively remove the rain streaks as well as preserve the crucial background information. Furthermore, We construct a night scene rainy (NSR) dataset comprising 900 image pairs, all based on real-world nighttime scenes, providing a new benchmark for nighttime deraining task research. Extensive qualitative and quantitative experimental evaluations on both existing datasets and the NSR dataset consistently demonstrate our method outperform the state-of-the-art (SOTA) methods in nighttime deraining tasks. The source code and dataset is available at https://github.com/Feecuin/NDLPNet.

## 🔍 Abstract (한글 번역)

arXiv:2509.13766v1 발표 유형: 새로운
요약: 저조도 조건에서 비가 내리는 것에 의해 발생하는 시각적 손상은 야간 감시 및 자율 항법의 성능을 심각하게 저해합니다. 기존의 이미지 비제거 기술은 주로 주간 조건을 위해 설계되었으며, 비의 공간 이질성 및 빛에 따른 줄무늬 가시성의 영향으로 인해 야간 조명 하에서 성능이 저하됩니다. 본 논문에서는 저조도 환경에서 비가 내리는 위치 강화 인지 네트워크(NDLPNet)를 제안합니다. 이 네트워크는 비의 공간 위치 정보와 밀도 분포를 효과적으로 포착합니다. 구체적으로, 입력 데이터에서 공간적 맥락 정보를 포착하고 활용하기 위해 위치 인지 모듈(PPM)을 도입하여 모델이 서로 다른 특징 채널의 중요성을 식별하고 재보정하는 능력을 향상시킵니다. 제안된 야간 비제거 네트워크는 비를 효과적으로 제거하면서 중요한 배경 정보를 보존할 수 있습니다. 또한, 우리는 900개의 이미지 쌍으로 구성된 야간 장면 비(NDLPNet) 데이터셋을 구축했습니다. 이 데이터셋은 실제 야간 장면을 기반으로 하여 야간 비제거 작업 연구를 위한 새로운 기준을 제공합니다. 기존 데이터셋과 NSR 데이터셋에 대한 광범위한 질적 및 양적 실험 평가 결과는 우리의 방법이 야간 비제거 작업에서 최첨단 기술을 능가한다는 것을 일관되게 보여줍니다. 소스 코드 및 데이터셋은 https://github.com/Feecuin/NDLPNet에서 사용할 수 있습니다.

## 📝 요약

본 연구는 저조도 환경에서 비 스트릭이 초래하는 시각적 저하 문제를 해결하기 위해 새로운 Nighttime Deraining Location-enhanced Perceptual Network(NDLPNet)을 제안한다. 이 네트워크는 공간적 위치 정보와 비 스트릭 밀도 분포를 효과적으로 포착하여 비 스트릭을 제거하고 중요한 배경 정보를 보존한다. 또한, 실제 밤 장면을 기반으로 한 900개의 이미지 쌍으로 이루어진 night scene rainy (NSR) 데이터셋을 구축하여 새로운 벤치마크를 제공한다. 실험 결과, NDLPNet은 기존 방법들보다 우수한 성능을 보여주었다.

## 🎯 주요 포인트

- 1. 저조도 환경에서 비 스트릭 아티팩트로 인한 시각적 저하 문제를 해결하기 위해 NDLPNet을 제안함

- 2. PPM을 통해 공간적 맥락 정보를 캡처하고 활용하여 모델의 성능 향상

- 3. NSR 데이터셋을 구축하여 새로운 벤치마크 제공 및 NDLPNet의 우수성 입증함

---

*Generated on 2025-09-18 17:00:52*