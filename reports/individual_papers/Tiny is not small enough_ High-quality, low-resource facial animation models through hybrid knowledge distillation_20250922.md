# Tiny is not small enough: High-quality, low-resource facial animation models through hybrid knowledge distillation

**Korean Title:** 작다는 충분히 작지 않다: 하이브리드 지식 증류를 통한 고품질, 저자원 얼굴 애니메이션 모델

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Speech-driven Animation|Speech-driven Animation]] [[keywords/specific/Hybrid Knowledge Distillation|Hybrid Knowledge Distillation]] [[keywords/broad/Machine Learning|Machine Learning]] [[keywords/broad/3D Facial Animation|3D Facial Animation]] [[keywords/unique/On-device Real-time Facial Animation|On-device Real-time Facial Animation]] [[categories/cs.LG|cs.LG]] [[2025-09-19/FMGS-Avatar_ Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction_20250919|FMGS-Avatar: Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (81.0% similar) [[2025-09-18/Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (81.0% similar) [[2025-09-19/Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Speech-driven Animation Models
**🔗 Specific Connectable**: Hybrid Knowledge Distillation
**🔬 Broad Technical**: Machine Learning, 3D Facial Animation
**⭐ Unique Technical**: On-device Real-time Facial Animation
## 🔗 유사한 논문
- [[2025-09-19/FMGS-Avatar_ Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction_20250919|FMGS-Avatar Mesh-Guided 2D Gaussian Splatting with Foundation Model Priors for 3D Monocular Avatar Reconstruction]] (81.0% similar)
- [[2025-09-18/Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers_20250918|Low-rank surrogate modeling and stochastic zero-order optimization for training of neural networks with black-box layers]] (81.0% similar)
- [[2025-09-19/Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (80.9% similar)
- [[2025-09-19/Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities_20250919|Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities]] (80.5% similar)
- [[2025-09-19/Reinforcement Learning Agent for a 2D Shooter Game_20250919|Reinforcement Learning Agent for a 2D Shooter Game]] (79.7% similar)


**ArXiv ID**: [2507.18352](https://arxiv.org/abs/2507.18352)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2507.18352.pdf)


**ArXiv ID**: [2507.18352](https://arxiv.org/abs/2507.18352)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2507.18352.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Speech-driven Animation
**🔗 Specific Connectable**: Hybrid Knowledge Distillation
**⭐ Unique Technical**: On-device Real-time Facial Animation
**🔬 Broad Technical**: Machine Learning, 3D Facial Animation

## 🏷️ 추출된 키워드



`Machine Learning` • 

`3D Facial Animation` • 

`Knowledge Distillation` • 

`Hybrid Knowledge Distillation` • 

`On-device Inference`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.18352v2 Announce Type: replace-cross 
Abstract: The training of high-quality, robust machine learning models for speech-driven 3D facial animation requires a large, diverse dataset of high-quality audio-animation pairs. To overcome the lack of such a dataset, recent work has introduced large pre-trained speech encoders that are robust to variations in the input audio and, therefore, enable the facial animation model to generalize across speakers, audio quality, and languages. However, the resulting facial animation models are prohibitively large and lend themselves only to offline inference on a dedicated machine. In this work, we explore on-device, real-time facial animation models in the context of game development. We overcome the lack of large datasets by using hybrid knowledge distillation with pseudo-labeling. Given a large audio dataset, we employ a high-performing teacher model to train very small student models. In contrast to the pre-trained speech encoders, our student models only consist of convolutional and fully-connected layers, removing the need for attention context or recurrent updates. In our experiments, we demonstrate that we can reduce the memory footprint to up to 3.4 MB and required future audio context to up to 81 ms while maintaining high-quality animations. This paves the way for on-device inference, an important step towards realistic, model-driven digital characters.

## 🔍 Abstract (한글 번역)

arXiv:2507.18352v2 발표 유형: 교차 교체  
초록: 고품질의 견고한 기계 학습 모델을 훈련하여 음성 기반 3D 얼굴 애니메이션을 생성하기 위해서는 고품질의 다양한 오디오-애니메이션 쌍 데이터셋이 필요합니다. 이러한 데이터셋의 부족을 극복하기 위해, 최근 연구에서는 입력 오디오의 변형에 강건한 대규모 사전 훈련된 음성 인코더를 도입하여 얼굴 애니메이션 모델이 화자, 오디오 품질, 언어에 걸쳐 일반화할 수 있도록 했습니다. 그러나 그 결과로 생성된 얼굴 애니메이션 모델은 지나치게 크며 전용 기기에서만 오프라인 추론이 가능합니다. 본 연구에서는 게임 개발을 위한 기기 내 실시간 얼굴 애니메이션 모델을 탐구합니다. 우리는 하이브리드 지식 증류와 유사 라벨링을 사용하여 대규모 데이터셋의 부족을 극복합니다. 대규모 오디오 데이터셋을 주어진 상황에서, 성능이 우수한 교사 모델을 사용하여 매우 작은 학생 모델을 훈련합니다. 사전 훈련된 음성 인코더와 달리, 우리의 학생 모델은 컨볼루션 및 완전 연결 계층만으로 구성되어 주의 컨텍스트나 순환 업데이트가 필요하지 않습니다. 실험에서 우리는 메모리 사용량을 최대 3.4 MB까지 줄이고, 필요한 미래 오디오 컨텍스트를 최대 81 ms까지 줄이면서도 고품질 애니메이션을 유지할 수 있음을 입증합니다. 이는 기기 내 추론을 가능하게 하며, 현실적이고 모델 기반의 디지털 캐릭터를 향한 중요한 단계입니다.

## 📝 요약

이 논문은 게임 개발에서 실시간으로 작동 가능한 기기 내 3D 얼굴 애니메이션 모델을 제안합니다. 기존의 대규모 사전 학습된 음성 인코더는 고품질의 얼굴 애니메이션을 생성하지만, 모델 크기가 커서 전용 기기에서만 오프라인 추론이 가능했습니다. 이를 해결하기 위해, 저자들은 하이브리드 지식 증류와 가상 라벨링을 사용하여 대규모 오디오 데이터셋을 활용해 작은 학생 모델을 훈련했습니다. 이 모델은 합성곱 및 완전 연결 계층만으로 구성되어 메모리 사용량을 3.4 MB까지 줄이고, 81 ms의 오디오 컨텍스트만 필요로 하면서도 높은 품질의 애니메이션을 유지합니다. 이는 현실적인 디지털 캐릭터 구현을 위한 중요한 진전을 의미합니다.

## 🎯 주요 포인트


- 1. 고품질의 음성 기반 3D 얼굴 애니메이션 모델 훈련에는 다양한 고품질 오디오-애니메이션 쌍 데이터셋이 필요합니다.

- 2. 최근 연구에서는 대규모 사전 훈련된 음성 인코더를 도입하여 화자, 오디오 품질, 언어에 걸쳐 일반화할 수 있는 얼굴 애니메이션 모델을 개발했습니다.

- 3. 본 연구에서는 하이브리드 지식 증류와 의사 레이블링을 사용하여 대규모 데이터셋 없이도 소형 학생 모델을 훈련합니다.

- 4. 제안된 학생 모델은 컨볼루션 및 완전 연결 레이어로만 구성되어 메모리 사용량을 최대 3.4 MB로 줄이고, 81 ms의 오디오 컨텍스트만 필요합니다.

- 5. 이 연구는 게임 개발 맥락에서 실시간, 기기 내 얼굴 애니메이션 모델을 구현하는 데 기여합니다.


---

*Generated on 2025-09-22 16:13:37*