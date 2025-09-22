
# Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior

**Korean Title:** 노이즈 우선순위를 가진 소음 환경에서의 확산 기반 비지도 음성-비주얼 분리

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Unsupervised Audio-Visual Speech Separation

## 🔗 유사한 논문
- [[MeanFlowSE one-step generative speech enhancement via conditional mean flow]] (81.1% similar)
- [[Explicit_Context-Driven_Neural_Acoustic_Modeling_for_High-Fidelity_RIR_Generation_20250919|Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation]] (80.6% similar)
- [[VocSegMRI Multimodal Learning for Precise Vocal Tract Segmentation in Real-time MRI]] (79.3% similar)
- [[Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (78.3% similar)
- [[Teacher-Guided_Pseudo_Supervision_and_Cross-Modal_Alignment_for_Audio-Visual_Video_Parsing_20250918|Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing]] (77.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14379v1 Announce Type: cross 
Abstract: In this paper, we address the problem of single-microphone speech separation in the presence of ambient noise. We propose a generative unsupervised technique that directly models both clean speech and structured noise components, training exclusively on these individual signals rather than noisy mixtures. Our approach leverages an audio-visual score model that incorporates visual cues to serve as a strong generative speech prior. By explicitly modelling the noise distribution alongside the speech distribution, we enable effective decomposition through the inverse problem paradigm. We perform speech separation by sampling from the posterior distributions via a reverse diffusion process, which directly estimates and removes the modelled noise component to recover clean constituent signals. Experimental results demonstrate promising performance, highlighting the effectiveness of our direct noise modelling approach in challenging acoustic environments.

## 🔍 Abstract (한글 번역)

arXiv:2509.14379v1 발표 유형: 교차  
초록: 본 논문에서는 주변 소음이 있는 환경에서 단일 마이크로폰 음성 분리 문제를 다룹니다. 우리는 깨끗한 음성과 구조화된 소음 요소를 모두 직접 모델링하는 생성적 비지도 학습 기법을 제안하며, 이는 소음이 섞인 신호가 아닌 개별 신호에 대해서만 훈련됩니다. 우리의 접근법은 시각적 단서를 통합하여 강력한 생성적 음성 사전으로 작용하는 오디오-비주얼 점수 모델을 활용합니다. 음성 분포와 함께 소음 분포를 명시적으로 모델링함으로써, 우리는 역문제 패러다임을 통해 효과적인 분해를 가능하게 합니다. 우리는 역확산 과정을 통해 후방 분포에서 샘플링하여 음성 분리를 수행하며, 이는 모델링된 소음 요소를 직접 추정하고 제거하여 깨끗한 구성 신호를 복원합니다. 실험 결과는 도전적인 음향 환경에서 우리의 직접 소음 모델링 접근법의 효과를 강조하며 유망한 성능을 보여줍니다.

## 📝 요약

이 논문에서는 단일 마이크로폰 환경에서 주변 소음이 있는 음성 분리 문제를 다룹니다. 저자들은 깨끗한 음성과 구조화된 소음 성분을 직접 모델링하는 생성적 비지도 학습 기법을 제안합니다. 이 방법은 시각적 단서를 활용한 오디오-비주얼 스코어 모델을 사용하여 강력한 생성적 음성 사전으로 작용합니다. 소음과 음성 분포를 명시적으로 모델링함으로써, 역문제 패러다임을 통해 효과적인 분해를 가능하게 합니다. 역확산 과정을 통해 후방 분포에서 샘플링하여 모델링된 소음 성분을 제거하고 깨끗한 음성을 복원합니다. 실험 결과는 이 방법이 어려운 음향 환경에서도 효과적임을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 논문은 단일 마이크로폰 환경에서 주변 소음이 있는 경우의 음성 분리 문제를 다룹니다.

- 2. 제안된 기법은 청정 음성과 구조화된 소음 성분을 직접 모델링하는 생성적 비지도 학습 방법입니다.

- 3. 오디오-비주얼 스코어 모델을 활용하여 시각적 단서를 강력한 생성적 음성 우선순위로 사용합니다.

- 4. 역확산 과정을 통해 후방 분포에서 샘플링하여 모델링된 소음 성분을 제거하고 청정 신호를 복원합니다.

- 5. 실험 결과, 제안된 직접 소음 모델링 접근 방식이 어려운 음향 환경에서 효과적임을 보여줍니다.

---

*Generated on 2025-09-19 15:34:59*