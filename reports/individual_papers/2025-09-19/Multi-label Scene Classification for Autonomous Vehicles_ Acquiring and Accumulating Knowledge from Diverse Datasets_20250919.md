
# Multi-label Scene Classification for Autonomous Vehicles: Acquiring and Accumulating Knowledge from Diverse Datasets

**Korean Title:** 자율주행 차량을 위한 다중 레이블 장면 분류: 다양한 데이터셋으로부터 지식 획득 및 축적

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-label Scene Classification

## 🔗 유사한 논문
- [[Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities_20250919|Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities]] (80.6% similar)
- [[MARIC Multi-Agent Reasoning for Image Classification]] (80.3% similar)
- [[AD-DINOv3 Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration]] (80.1% similar)
- [[Ensemble of Pre-Trained Models for Long-Tailed Trajectory Prediction]] (79.8% similar)
- [[Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention_20250919|Resolve Highway Conflict in Multi-Autonomous Vehicle Controls with Local State Attention]] (79.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.17101v3 Announce Type: replace 
Abstract: Driving scenes are inherently heterogeneous and dynamic. Multi-attribute scene identification, as a high-level visual perception capability, provides autonomous vehicles (AVs) with essential contextual awareness to understand, reason through, and interact with complex driving environments. Although scene identification is best modeled as a multi-label classification problem via multitask learning, it faces two major challenges: the difficulty of acquiring balanced, comprehensively annotated datasets and the need to re-annotate all training data when new attributes emerge. To address these challenges, this paper introduces a novel deep learning method that integrates Knowledge Acquisition and Accumulation (KAA) with Consistency-based Active Learning (CAL). KAA leverages monotask learning on heterogeneous single-label datasets to build a knowledge foundation, while CAL bridges the gap between single- and multi-label data, adapting the foundation model for multi-label scene classification. An ablation study on the newly developed Driving Scene Identification (DSI) dataset demonstrates a 56.1% improvement over an ImageNet-pretrained baseline. Moreover, KAA-CAL outperforms state-of-the-art multi-label classification methods on the BDD100K and HSD datasets, achieving this with 85% less data and even recognizing attributes unseen during foundation model training. The DSI dataset and KAA-CAL implementation code are publicly available at https://github.com/KELISBU/KAA-CAL .

## 🔍 Abstract (한글 번역)

arXiv:2506.17101v3 발표 유형: 교체  
초록: 운전 장면은 본질적으로 이질적이고 동적입니다. 다중 속성 장면 식별은 고차원 시각적 인식 능력으로서 자율 주행 차량(AV)이 복잡한 운전 환경을 이해하고, 추론하며, 상호작용할 수 있는 필수적인 맥락 인식을 제공합니다. 장면 식별은 다중 작업 학습을 통한 다중 레이블 분류 문제로 모델링하는 것이 가장 적합하지만, 두 가지 주요 과제에 직면해 있습니다: 균형 잡힌, 포괄적으로 주석된 데이터셋을 획득하는 어려움과 새로운 속성이 등장할 때 모든 학습 데이터를 다시 주석해야 하는 필요성입니다. 이러한 과제를 해결하기 위해, 본 논문은 지식 획득 및 축적(KAA)과 일관성 기반 능동 학습(CAL)을 통합한 새로운 딥러닝 방법을 소개합니다. KAA는 이질적인 단일 레이블 데이터셋에서 단일 작업 학습을 활용하여 지식 기반을 구축하며, CAL은 단일 레이블 데이터와 다중 레이블 데이터 간의 격차를 메우고, 다중 레이블 장면 분류를 위해 기반 모델을 적응시킵니다. 새로 개발된 운전 장면 식별(DSI) 데이터셋에 대한 소거 연구는 ImageNet으로 사전 학습된 기준선보다 56.1% 향상된 성능을 보여줍니다. 또한, KAA-CAL은 BDD100K 및 HSD 데이터셋에서 최첨단 다중 레이블 분류 방법을 능가하며, 85% 적은 데이터로도 기반 모델 학습 중에 보지 못한 속성을 인식합니다. DSI 데이터셋과 KAA-CAL 구현 코드는 https://github.com/KELISBU/KAA-CAL 에서 공개적으로 제공됩니다.

## 📝 요약

이 논문은 자율주행차의 복잡한 주행 환경 이해를 위한 다중 속성 장면 식별 문제를 다룹니다. 주요 기여는 지식 획득 및 축적(KAA)과 일관성 기반 능동 학습(CAL)을 통합한 새로운 딥러닝 방법론을 제안한 것입니다. KAA는 단일 레이블 데이터셋을 활용해 지식 기반을 구축하고, CAL은 이를 다중 레이블 분류로 확장합니다. 새로운 Driving Scene Identification(DSI) 데이터셋을 통해 ImageNet 사전 학습 모델 대비 56.1% 성능 향상을 보였으며, BDD100K 및 HSD 데이터셋에서도 85% 적은 데이터로 최신 방법들을 능가했습니다. KAA-CAL은 새로운 속성도 인식 가능하며, 관련 데이터셋과 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 자율주행차의 복잡한 주행 환경 이해를 위해 다중 속성 장면 식별이 중요하다.

- 2. 새로운 속성이 등장할 때마다 모든 훈련 데이터를 재주석해야 하는 문제를 해결하기 위해 KAA와 CAL을 통합한 새로운 딥러닝 방법을 제안한다.

- 3. KAA는 단일 레이블 데이터셋을 활용하여 지식 기반을 구축하고, CAL은 이를 다중 레이블 장면 분류에 적응시킨다.

- 4. 새로운 DSI 데이터셋에서 KAA-CAL은 ImageNet 사전 학습 모델 대비 56.1% 성능 향상을 보였다.

- 5. KAA-CAL은 BDD100K 및 HSD 데이터셋에서 최첨단 다중 레이블 분류 방법을 85% 적은 데이터로 능가하며, 훈련 시 보지 못한 속성도 인식한다.

---

*Generated on 2025-09-19 16:17:43*