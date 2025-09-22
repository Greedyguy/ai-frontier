# Comprehensive Evaluation of CNN-Based Audio Tagging Models on Resource-Constrained Devices

**Korean Title:** 자원 제약 장치에서 CNN 기반 오디오 태깅 모델의 종합적 평가

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Jordi Grau-Haro|Jordi Grau-Haro]] [[authors/Ruben Ribes-Serrano|Ruben Ribes-Serrano]] [[authors/Javier Naranjo-Alcazar|Javier Naranjo-Alcazar]] [[authors/Marta Garcia-Ballesteros|Marta Garcia-Ballesteros]] [[authors/Pedro Zuccarello|Pedro Zuccarello]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Audio Classification, Model Optimization

## 🔗 유사한 논문
- [[Exploring the Relationship between Brain Hemisphere States and Frequency Bands through Deep Learning Optimization Techniques_20250917|Exploring the Relationship between Brain Hemisphere States and Frequency Bands through Deep Learning Optimization Techniques]] (78.0% similar)
- [[Spatial Audio Motion Understanding and Reasoning_20250918|Spatial Audio Motion Understanding and Reasoning]] (77.7% similar)
- [[TICL_ Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models_20250918|TICL Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (77.7% similar)
- [[MaRVIn_ A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration_20250919|MaRVIn A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (77.5% similar)
- [[HD3C_ Efficient Medical Data Classification for Embedded Devices_20250918|HD3C Efficient Medical Data Classification for Embedded Devices]] (77.3% similar)

## 📋 저자 정보

**Authors:** Jordi Grau-Haro, Ruben Ribes-Serrano, Javier Naranjo-Alcazar, Marta Garcia-Ballesteros, Pedro Zuccarello

## 📄 Abstract (원문)

Convolutional Neural Networks (CNNs) have demonstrated exceptional
performance in audio tagging tasks. However, deploying these models on
resource-constrained devices like the Raspberry Pi poses challenges related to
computational efficiency and thermal management. In this paper, a comprehensive
evaluation of multiple convolutional neural network (CNN) architectures for
audio tagging on the Raspberry Pi is conducted, encompassing all 1D and 2D
models from the Pretrained Audio Neural Networks (PANNs) framework, a
ConvNeXt-based model adapted for audio classification, as well as MobileNetV3
architectures. In addition, two PANNs-derived networks, CNN9 and CNN13,
recently proposed, are also evaluated. To enhance deployment efficiency and
portability across diverse hardware platforms, all models are converted to the
Open Neural Network Exchange (ONNX) format. Unlike previous works that focus on
a single model, our analysis encompasses a broader range of architectures and
involves continuous 24-hour inference sessions to assess performance stability.
Our experiments reveal that, with appropriate model selection and optimization,
it is possible to maintain consistent inference latency and manage thermal
behavior effectively over extended periods. These findings provide valuable
insights for deploying audio tagging models in real-world edge computing
scenarios.

## 🔍 Abstract (한글 번역)

합성곱 신경망(CNN)은 오디오 태깅 작업에서 뛰어난 성능을 보여주었습니다. 그러나 Raspberry Pi와 같은 자원이 제한된 장치에 이러한 모델을 배포하는 것은 계산 효율성과 열 관리와 관련된 문제를 제기합니다. 본 논문에서는 Raspberry Pi에서 오디오 태깅을 위한 여러 합성곱 신경망(CNN) 아키텍처에 대한 포괄적인 평가를 수행하며, 여기에는 사전 학습된 오디오 신경망(PANNs) 프레임워크의 모든 1D 및 2D 모델, 오디오 분류에 맞게 조정된 ConvNeXt 기반 모델, 그리고 MobileNetV3 아키텍처가 포함됩니다. 또한, 최근 제안된 두 개의 PANNs 파생 네트워크인 CNN9 및 CNN13도 평가됩니다. 다양한 하드웨어 플랫폼에서의 배포 효율성과 이동성을 향상시키기 위해 모든 모델은 Open Neural Network Exchange (ONNX) 형식으로 변환됩니다. 단일 모델에 초점을 맞춘 이전 연구와 달리, 우리의 분석은 더 넓은 범위의 아키텍처를 포괄하며 성능 안정성을 평가하기 위해 연속적인 24시간 추론 세션을 포함합니다. 우리의 실험은 적절한 모델 선택과 최적화를 통해 장기간 동안 일관된 추론 지연 시간을 유지하고 열 거동을 효과적으로 관리할 수 있음을 보여줍니다. 이러한 발견은 실제 엣지 컴퓨팅 시나리오에서 오디오 태깅 모델을 배포하기 위한 귀중한 통찰력을 제공합니다.

## 📝 요약

이 논문은 Raspberry Pi와 같은 자원 제한적인 장치에서 오디오 태깅을 위한 다양한 CNN 아키텍처의 성능을 평가합니다. PANNs 프레임워크의 1D 및 2D 모델, ConvNeXt 기반 모델, MobileNetV3 아키텍처, 그리고 새롭게 제안된 CNN9 및 CNN13을 포함하여 다양한 모델을 분석합니다. 모든 모델은 ONNX 형식으로 변환되어 다양한 하드웨어 플랫폼에서의 효율성과 이동성을 높였습니다. 24시간 연속 추론 세션을 통해 성능 안정성을 평가한 결과, 적절한 모델 선택과 최적화를 통해 일관된 추론 지연 시간을 유지하고 열 관리를 효과적으로 수행할 수 있음을 발견했습니다. 이 연구는 실제 엣지 컴퓨팅 시나리오에서 오디오 태깅 모델 배포에 유용한 통찰력을 제공합니다.

## 🎯 주요 포인트

- 1. 본 논문은 Raspberry Pi와 같은 자원 제한 장치에서 오디오 태깅을 위한 CNN 아키텍처의 성능을 평가합니다.

- 2. PANNs 프레임워크의 1D 및 2D 모델, ConvNeXt 기반 모델, MobileNetV3 아키텍처를 포함한 다양한 CNN 모델을 분석합니다.

- 3. 모든 모델은 ONNX 형식으로 변환되어 다양한 하드웨어 플랫폼에서의 효율성과 이식성을 향상시킵니다.

- 4. 24시간 연속 추론 세션을 통해 성능 안정성을 평가하며, 적절한 모델 선택과 최적화를 통해 일관된 추론 지연 시간과 열 관리를 유지할 수 있음을 발견했습니다.

- 5. 이 연구는 실제 엣지 컴퓨팅 시나리오에서 오디오 태깅 모델을 배포하는 데 유용한 통찰력을 제공합니다.

---

*Generated on 2025-09-20 09:14:34*