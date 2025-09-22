
# DACoN: DINO for Anime Paint Bucket Colorization with Any Number of Reference Images

**Korean Title:** DACoN: 다수의 참조 이미지를 활용한 애니메이션 페인트 버킷 채색을 위한 DINO

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Part-level Semantics

## 🔗 유사한 논문
- [[AD-DINOv3 Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration]] (79.8% similar)
- [[DINAMO Dynamic and INterpretable Anomaly MOnitoring for Large-Scale Particle Physics Experiments]] (78.8% similar)
- [[DiffGAN A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis]] (78.7% similar)
- [[DICE Diffusion Consensus Equilibrium for Sparse-view CT Reconstruction]] (78.1% similar)
- [[NDLPNet A Location-Aware Nighttime Deraining Network and a Real-World Benchmark Dataset]] (77.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14685v1 Announce Type: new 
Abstract: Automatic colorization of line drawings has been widely studied to reduce the labor cost of hand-drawn anime production. Deep learning approaches, including image/video generation and feature-based correspondence, have improved accuracy but struggle with occlusions, pose variations, and viewpoint changes. To address these challenges, we propose DACoN, a framework that leverages foundation models to capture part-level semantics, even in line drawings. Our method fuses low-resolution semantic features from foundation models with high-resolution spatial features from CNNs for fine-grained yet robust feature extraction. In contrast to previous methods that rely on the Multiplex Transformer and support only one or two reference images, DACoN removes this constraint, allowing any number of references. Quantitative and qualitative evaluations demonstrate the benefits of using multiple reference images, achieving superior colorization performance. Our code and model are available at https://github.com/kzmngt/DACoN.

## 🔍 Abstract (한글 번역)

arXiv:2509.14685v1 발표 유형: 신규  
초록: 손으로 그린 애니메이션 제작의 노동 비용을 줄이기 위해 선화의 자동 채색이 널리 연구되어 왔습니다. 이미지/비디오 생성 및 특징 기반 대응을 포함한 딥러닝 접근법은 정확도를 향상시켰지만, 가림, 자세 변화 및 시점 변화에 어려움을 겪고 있습니다. 이러한 문제를 해결하기 위해, 우리는 선화에서도 부분 수준의 의미론을 포착할 수 있는 기초 모델을 활용하는 프레임워크인 DACoN을 제안합니다. 우리의 방법은 기초 모델에서 얻은 저해상도 의미론적 특징을 CNN에서 얻은 고해상도 공간적 특징과 융합하여 세밀하면서도 견고한 특징 추출을 가능하게 합니다. Multiplex Transformer에 의존하고 하나 또는 두 개의 참조 이미지만 지원하는 이전 방법과 달리, DACoN은 이러한 제약을 제거하여 참조 이미지의 수에 제한이 없습니다. 정량적 및 정성적 평가를 통해 여러 참조 이미지를 사용하는 것이 우수한 채색 성능을 달성하는 데 유리함을 입증했습니다. 우리의 코드와 모델은 https://github.com/kzmngt/DACoN에서 제공됩니다.

## 📝 요약

이 논문은 선화의 자동 채색을 위한 새로운 프레임워크 DACoN을 제안합니다. 기존의 딥러닝 방법론은 가림, 자세 변화, 시점 변화에 어려움을 겪었으나, DACoN은 파운데이션 모델을 활용하여 선화에서도 부분 수준의 의미를 포착합니다. 이 방법은 파운데이션 모델의 저해상도 의미적 특징과 CNN의 고해상도 공간적 특징을 융합하여 세밀하면서도 강력한 특징 추출을 가능하게 합니다. 기존 방법과 달리 DACoN은 참조 이미지의 수에 제한이 없으며, 여러 참조 이미지를 사용하여 뛰어난 채색 성능을 입증했습니다. 코드와 모델은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. DACoN은 기초 모델을 활용하여 선화에서도 부분 수준의 의미를 포착하는 자동 채색 프레임워크를 제안합니다.

- 2. DACoN은 CNN의 고해상도 공간 특징과 기초 모델의 저해상도 의미적 특징을 융합하여 세밀하면서도 강력한 특징 추출을 수행합니다.

- 3. 기존 방법과 달리 DACoN은 다중 참조 이미지를 지원하여 채색 성능을 향상시킵니다.

- 4. 정량적 및 정성적 평가에서 DACoN의 다중 참조 이미지 사용이 우수한 채색 성능을 입증합니다.

- 5. DACoN의 코드와 모델은 https://github.com/kzmngt/DACoN에서 제공됩니다.

---

*Generated on 2025-09-19 16:04:58*