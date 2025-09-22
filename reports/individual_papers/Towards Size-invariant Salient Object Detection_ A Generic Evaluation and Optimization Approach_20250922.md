# Towards Size-invariant Salient Object Detection: A Generic Evaluation and Optimization Approach

**Korean Title:** 크기 불변의 주목할 만한 객체 검출을 향하여: 일반적인 평가 및 최적화 접근법

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Salient Object Detection

## 🔗 유사한 논문
- [[2025-09-18/VSE-MOT_ Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement_20250918|VSE-MOT Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (78.4% similar)
- [[2025-09-18/Synthetic-to-Real Object Detection using YOLOv11 and Domain Randomization Strategies_20250918|Synthetic-to-Real Object Detection using YOLOv11 and Domain Randomization Strategies]] (77.7% similar)
- [[2025-09-19/An Evaluation-Centric Paradigm for Scientific Visualization Agents_20250919|An Evaluation-Centric Paradigm for Scientific Visualization Agents]] (77.5% similar)
- [[2025-09-18/A Novel Compression Framework for YOLOv8_ Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation_20250918|A Novel Compression Framework for YOLOv8 Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (77.3% similar)
- [[2025-09-18/GROOD_ GRadient-Aware Out-of-Distribution Detection_20250918|GROOD GRadient-Aware Out-of-Distribution Detection]] (76.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15573v1 Announce Type: cross 
Abstract: This paper investigates a fundamental yet underexplored issue in Salient Object Detection (SOD): the size-invariant property for evaluation protocols, particularly in scenarios when multiple salient objects of significantly different sizes appear within a single image. We first present a novel perspective to expose the inherent size sensitivity of existing widely used SOD metrics. Through careful theoretical derivations, we show that the evaluation outcome of an image under current SOD metrics can be essentially decomposed into a sum of several separable terms, with the contribution of each term being directly proportional to its corresponding region size. Consequently, the prediction errors would be dominated by the larger regions, while smaller yet potentially more semantically important objects are often overlooked, leading to biased performance assessments and practical degradation. To address this challenge, a generic Size-Invariant Evaluation (SIEva) framework is proposed. The core idea is to evaluate each separable component individually and then aggregate the results, thereby effectively mitigating the impact of size imbalance across objects. Building upon this, we further develop a dedicated optimization framework (SIOpt), which adheres to the size-invariant principle and significantly enhances the detection of salient objects across a broad range of sizes. Notably, SIOpt is model-agnostic and can be seamlessly integrated with a wide range of SOD backbones. Theoretically, we also present generalization analysis of SOD methods and provide evidence supporting the validity of our new evaluation protocols. Finally, comprehensive experiments speak to the efficacy of our proposed approach. The code is available at https://github.com/Ferry-Li/SI-SOD.

## 🔍 Abstract (한글 번역)

arXiv:2509.15573v1 발표 유형: 교차  
초록: 본 논문은 주목 객체 탐지(Salient Object Detection, SOD)에서 근본적이지만 충분히 탐구되지 않은 문제인 평가 프로토콜의 크기 불변성(size-invariant property)을 조사합니다. 특히, 단일 이미지 내에 크기가 크게 다른 여러 주목 객체가 나타나는 시나리오에서 이 문제가 중요합니다. 우리는 먼저 기존에 널리 사용되는 SOD 지표의 내재된 크기 민감성을 드러내는 새로운 관점을 제시합니다. 신중한 이론적 유도를 통해, 현재 SOD 지표 하에서 이미지의 평가 결과가 여러 개의 분리 가능한 항의 합으로 본질적으로 분해될 수 있음을 보여줍니다. 각 항의 기여도는 해당 영역의 크기에 직접 비례합니다. 따라서 예측 오류는 더 큰 영역에 의해 지배되며, 작지만 잠재적으로 더 의미 있는 객체는 종종 간과되어 편향된 성능 평가와 실제 성능 저하로 이어집니다. 이 문제를 해결하기 위해, 일반적인 크기 불변 평가(Size-Invariant Evaluation, SIEva) 프레임워크를 제안합니다. 핵심 아이디어는 각 분리 가능한 구성 요소를 개별적으로 평가한 후 결과를 집계하여 객체 간 크기 불균형의 영향을 효과적으로 완화하는 것입니다. 이를 바탕으로, 크기 불변 원칙을 준수하고 다양한 크기의 주목 객체 탐지를 크게 향상시키는 전용 최적화 프레임워크(SIOpt)를 개발합니다. 특히, SIOpt는 모델에 구애받지 않으며 다양한 SOD 백본과 원활하게 통합될 수 있습니다. 이론적으로, 우리는 또한 SOD 방법의 일반화 분석을 제시하고 새로운 평가 프로토콜의 타당성을 뒷받침하는 증거를 제공합니다. 마지막으로, 포괄적인 실험은 제안된 접근 방식의 효능을 입증합니다. 코드는 https://github.com/Ferry-Li/SI-SOD에서 이용 가능합니다.

## 📝 요약

이 논문은 주목 객체 검출(SOD)에서 평가 프로토콜의 크기 불변 특성을 조사합니다. 기존 SOD 지표가 크기에 민감하다는 점을 이론적으로 밝혀내고, 큰 객체가 작은 객체보다 평가에 더 큰 영향을 미쳐 성능 평가가 왜곡될 수 있음을 지적합니다. 이를 해결하기 위해 각 객체의 크기를 개별적으로 평가하고 결과를 종합하는 크기 불변 평가(SIEva) 프레임워크를 제안합니다. 또한, 다양한 크기의 주목 객체 검출을 개선하는 최적화 프레임워크(SIOpt)를 개발했습니다. SIOpt는 모델에 구애받지 않으며 다양한 SOD 백본과 통합될 수 있습니다. 실험 결과, 제안된 방법의 효과가 입증되었습니다.

## 🎯 주요 포인트

- 1. 본 논문은 Salient Object Detection(SOD)에서 평가 프로토콜의 크기 불변 속성을 조사하며, 특히 다양한 크기의 주목할 만한 객체들이 하나의 이미지에 나타나는 경우에 초점을 맞추고 있다.

- 2. 기존 SOD 지표의 크기 민감성을 드러내기 위해 새로운 관점을 제시하고, 이로 인해 큰 영역이 예측 오류를 지배하게 되어 작은 객체들이 간과되는 문제를 지적한다.

- 3. 크기 불균형 문제를 해결하기 위해 각 구성 요소를 개별적으로 평가하고 결과를 집계하는 일반적인 크기 불변 평가(SIEva) 프레임워크를 제안한다.

- 4. 제안된 최적화 프레임워크(SIOpt)는 크기 불변 원칙을 준수하며 다양한 크기의 주목할 만한 객체 탐지를 크게 향상시킨다.

- 5. 실험 결과는 제안된 접근 방식의 효능을 입증하며, 코드는 공개되어 있다.

---

*Generated on 2025-09-22 14:03:36*