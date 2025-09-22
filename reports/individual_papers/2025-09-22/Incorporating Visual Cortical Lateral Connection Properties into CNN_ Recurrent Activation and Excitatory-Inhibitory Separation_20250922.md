# Incorporating Visual Cortical Lateral Connection Properties into CNN: Recurrent Activation and Excitatory-Inhibitory Separation

**Korean Title:** 시각 피질의 측면 연결 특성을 CNN에 통합하기: 재귀 활성화와 흥분-억제 분리

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Lateral Connections in CNN

## 🔗 유사한 논문
- [[2025-09-19/Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models_20250919|Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models]] (79.5% similar)
- [[2025-09-22/Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception_20250922|Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception]] (78.1% similar)
- [[2025-09-18/Multimodal signal fusion for stress detection using deep neural networks_ a novel approach for converting 1D signals to unified 2D images_20250918|Multimodal signal fusion for stress detection using deep neural networks a novel approach for converting 1D signals to unified 2D images]] (77.9% similar)
- [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (77.9% similar)
- [[2025-09-22/Region-Aware Deformable Convolutions_20250922|Region-Aware Deformable Convolutions]] (77.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15460v1 Announce Type: cross 
Abstract: The original Convolutional Neural Networks (CNNs) and their modern updates such as the ResNet are heavily inspired by the mammalian visual system. These models include afferent connections (retina and LGN to the visual cortex) and long-range projections (connections across different visual cortical areas). However, in the mammalian visual system, there are connections within each visual cortical area, known as lateral (or horizontal) connections. These would roughly correspond to connections within CNN feature maps, and this important architectural feature is missing in current CNN models. In this paper, we present how such lateral connections can be modeled within the standard CNN framework, and test its benefits and analyze its emergent properties in relation to the biological visual system. We will focus on two main architectural features of lateral connections: (1) recurrent activation and (2) separation of excitatory and inhibitory connections. We show that recurrent CNN using weight sharing is equivalent to lateral connections, and propose a custom loss function to separate excitatory and inhibitory weights. The addition of these two leads to increased classification accuracy, and importantly, the activation properties and connection properties of the resulting model show properties similar to those observed in the biological visual system. We expect our approach to help align CNN closer to its biological counterpart and better understand the principles of visual cortical computation.

## 🔍 Abstract (한글 번역)

arXiv:2509.15460v1 발표 유형: 교차  
초록: 원래의 합성곱 신경망(CNN)과 ResNet과 같은 현대적 업데이트는 포유류의 시각 시스템에서 크게 영감을 받았습니다. 이러한 모델은 구심성 연결(망막과 LGN에서 시각 피질로)과 장거리 투사(다양한 시각 피질 영역 간의 연결)를 포함합니다. 그러나 포유류의 시각 시스템에서는 각 시각 피질 영역 내에 있는 연결, 즉 측면(또는 수평) 연결이 있습니다. 이는 대략적으로 CNN 특징 맵 내의 연결에 해당하며, 현재 CNN 모델에서는 이 중요한 구조적 특징이 결여되어 있습니다. 이 논문에서는 표준 CNN 프레임워크 내에서 이러한 측면 연결을 어떻게 모델링할 수 있는지 제시하고, 그 이점을 테스트하며 생물학적 시각 시스템과 관련하여 발생하는 특성을 분석합니다. 우리는 측면 연결의 두 가지 주요 구조적 특징에 초점을 맞출 것입니다: (1) 반복 활성화와 (2) 흥분성 및 억제성 연결의 분리. 우리는 가중치 공유를 사용하는 반복 CNN이 측면 연결과 동등하다는 것을 보여주고, 흥분성 및 억제성 가중치를 분리하기 위한 맞춤 손실 함수를 제안합니다. 이 두 가지의 추가는 분류 정확도를 증가시키고, 중요한 것은 결과 모델의 활성화 특성과 연결 특성이 생물학적 시각 시스템에서 관찰되는 것과 유사한 특성을 보여줍니다. 우리는 우리의 접근 방식이 CNN을 생물학적 대응물에 더 가깝게 정렬하고 시각 피질 계산의 원리를 더 잘 이해하는 데 도움이 될 것으로 기대합니다.

## 📝 요약

이 논문은 기존의 CNN 모델에 결여된 측면 연결(lateral connections)을 도입하여 생물학적 시각 시스템과의 유사성을 높이고자 합니다. 저자들은 CNN 내에서 반복적 활성화와 흥분성 및 억제성 연결의 분리를 통해 이러한 측면 연결을 모델링합니다. 반복적 CNN은 가중치 공유를 통해 측면 연결과 동등하다는 점을 보이고, 흥분성 및 억제성 가중치를 분리하는 맞춤형 손실 함수를 제안합니다. 이러한 접근은 분류 정확도를 높이며, 결과 모델의 활성화 및 연결 특성이 생물학적 시각 시스템과 유사함을 보여줍니다. 이를 통해 CNN이 생물학적 시각 시스템과 더 잘 정렬되고 시각 피질 계산의 원리를 이해하는 데 기여할 것으로 기대됩니다.

## 🎯 주요 포인트

- 1. 기존의 CNN 모델은 포유류의 시각 시스템에서 영감을 받아 설계되었으나, 시각 피질 내의 측면 연결이 부족하다.

- 2. 본 연구는 CNN 내에서 측면 연결을 모델링하고, 생물학적 시각 시스템과의 관련성을 분석하였다.

- 3. 측면 연결의 두 가지 주요 구조적 특징인 재귀 활성화와 흥분성 및 억제성 연결의 분리를 강조하였다.

- 4. 재귀적 CNN은 측면 연결과 동등하며, 흥분성 및 억제성 가중치를 분리하는 맞춤형 손실 함수를 제안하였다.

- 5. 이러한 접근 방식은 분류 정확도를 높이고, 생물학적 시각 시스템과 유사한 활성화 및 연결 특성을 보여준다.

---

*Generated on 2025-09-22 13:58:22*