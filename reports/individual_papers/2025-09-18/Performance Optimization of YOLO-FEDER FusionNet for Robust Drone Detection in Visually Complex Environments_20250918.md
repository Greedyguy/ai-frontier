
# Performance Optimization of YOLO-FEDER FusionNet for Robust Drone Detection in Visually Complex Environments

**Korean Title:** 시각적으로 복잡한 환경에서 강력한 드론 탐지를 위한 YOLO-FEDER FusionNet의 성능 최적화

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Backbone Upgrades

## 🔗 유사한 논문
- [[A_Novel_Compression_Framework_for_YOLOv8_Achieving_Real-Time_Aerial_Object_Detection_on_Edge_Devices_via_Structured_Pruning_and_Channel-Wise_Distillation_20250918|A Novel Compression Framework for YOLOv8: Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (86.2% similar)
- [[Federated_Learning_for_Deforestation_Detection_A_Distributed_Approach_with_Satellite_Imagery_20250918|Federated Learning for Deforestation Detection: A Distributed Approach with Satellite Imagery]] (80.9% similar)
- [[MOCHA: Multi-modal Objects-aware Cross-arcHitecture Alignment]] (79.1% similar)
- [[FlightDiffusion_Revolutionising_Autonomous_Drone_Training_with_Diffusion_Models_Generating_FPV_Video_20250918|FlightDiffusion: Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (79.0% similar)
- [[NDLPNet_A_Location-Aware_Nighttime_Deraining_Network_and_a_Real-World_Benchmark_Dataset_20250918|NDLPNet: A Location-Aware Nighttime Deraining Network and a Real-World Benchmark Dataset]] (78.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14012v1 Announce Type: new 
Abstract: Drone detection in visually complex environments remains challenging due to background clutter, small object scale, and camouflage effects. While generic object detectors like YOLO exhibit strong performance in low-texture scenes, their effectiveness degrades in cluttered environments with low object-background separability. To address these limitations, this work presents an enhanced iteration of YOLO-FEDER FusionNet -- a detection framework that integrates generic object detection with camouflage object detection techniques. Building upon the original architecture, the proposed iteration introduces systematic advancements in training data composition, feature fusion strategies, and backbone design. Specifically, the training process leverages large-scale, photo-realistic synthetic data, complemented by a small set of real-world samples, to enhance robustness under visually complex conditions. The contribution of intermediate multi-scale FEDER features is systematically evaluated, and detection performance is comprehensively benchmarked across multiple YOLO-based backbone configurations. Empirical results indicate that integrating intermediate FEDER features, in combination with backbone upgrades, contributes to notable performance improvements. In the most promising configuration -- YOLO-FEDER FusionNet with a YOLOv8l backbone and FEDER features derived from the DWD module -- these enhancements lead to a FNR reduction of up to 39.1 percentage points and a mAP increase of up to 62.8 percentage points at an IoU threshold of 0.5, compared to the initial baseline.

## 🔍 Abstract (한글 번역)

arXiv:2509.14012v1 발표 유형: 새로운
요약: 시각적으로 복잡한 환경에서의 드론 감지는 배경 혼잡, 작은 객체 규모 및 위장 효과로 인해 여전히 어려운 문제입니다. YOLO와 같은 일반적인 객체 탐지기는 낮은 질감 장면에서 강력한 성능을 보이지만, 낮은 객체-배경 분리 가능성을 가진 혼잡한 환경에서의 효과는 저하됩니다. 이러한 한계를 해결하기 위해 본 연구는 일반적인 객체 탐지와 위장 객체 탐지 기술을 통합한 감지 프레임워크인 YOLO-FEDER FusionNet의 향상된 버전을 제시합니다. 제안된 반복은 원래 아키텍처를 기반으로 하며, 훈련 데이터 구성, 특징 퓨전 전략 및 백본 디자인에서 체계적인 진보를 도입합니다. 구체적으로, 훈련 과정은 시각적으로 복잡한 조건 하에서 견고성을 향상시키기 위해 대규모의 사실적인 합성 데이터와 함께 소량의 실제 샘플을 활용합니다. 중간 다중 스케일 FEDER 특징의 기여도가 체계적으로 평가되며, 여러 YOLO 기반 백본 구성에 걸쳐 감지 성능이 종합적으로 평가됩니다. 경험적 결과는 중간 FEDER 특징을 통합하고 백본 업그레이드를 결합함으로써 주목할만한 성능 향상을 이끌어냅니다. 가장 유망한 구성인 YOLO-FEDER FusionNet은 YOLOv8l 백본 및 DWD 모듈에서 파생된 FEDER 특징을 사용할 때, 초기 베이스라인과 비교하여 IoU 임계값 0.5에서 최대 39.1 포인트의 FNR 감소 및 최대 62.8 포인트의 mAP 증가를 보입니다.

## 📝 요약

이 연구는 시각적으로 복잡한 환경에서의 드론 탐지 문제를 해결하기 위해 YOLO-FEDER FusionNet을 개선한 것을 제시한다. 이 프레임워크는 일반적인 객체 탐지와 위장된 객체 탐지 기술을 통합하여 배경 혼잡, 작은 객체 규모, 위장 효과로 인한 어려움을 극복한다. 학습 데이터 조합, 특징 퓨전 전략, 백본 디자인에서 체계적인 개선을 도입하였으며, 중간 다중 스케일 FEDER 피쳐의 기여도를 평가하고 YOLO 기반 백본 구성에 대해 성능을 평가하였다. 실험 결과는 중간 FEDER 피쳐와 백본 업그레이드를 통해 성능이 향상되었음을 보여주며, 가장 유망한 구성에서는 FNR 감소와 mAP 증가를 보였다.

## 🎯 주요 포인트

- 시각적으로 복잡한 환경에서의 드론 탐지는 배경 혼잡, 작은 물체 규모 및 위장 효과로 인해 여전히 어려움을 겪고 있다.

- YOLO-FEDER FusionNet은 일반적인 물체 탐지와 위장 물체 탐지 기술을 통합한 감지 프레임워크를 제시한다.

- 학습 데이터 구성, 특징 퓨전 전략 및 백본 디자인에서 체계적인 개선을 도입하여 성능을 향상시킨다.

---

*Generated on 2025-09-18 17:02:30*