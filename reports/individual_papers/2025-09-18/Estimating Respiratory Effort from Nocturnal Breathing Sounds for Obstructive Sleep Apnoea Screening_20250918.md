# Estimating Respiratory Effort from Nocturnal Breathing Sounds for Obstructive Sleep Apnoea Screening

**Korean Title:** 수면 무호흡증 선별을 위한 야간 호흡 소리로부터 호흡 노력 추정

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Xiaolei Xu|Xiaolei Xu]] [[authors/Chaoyue Niu|Chaoyue Niu]] [[authors/Guy J. Brown|Guy J. Brown]] [[authors/Hector Romero|Hector Romero]] [[authors/Ning Ma|Ning Ma]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Sensor-free OSA Monitoring

## 🔗 유사한 논문
- [[Out-of-Sight Trajectories_ Tracking, Fusion, and Prediction_20250919|Out-of-Sight Trajectories Tracking, Fusion, and Prediction]] (76.6% similar)
- [[Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior_20250919|Diffusion-Based Unsupervised Audio-Visual Speech Separation in Noisy Environments with Noise Prior]] (76.4% similar)
- [[Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation_20250919|Explicit Context-Driven Neural Acoustic Modeling for High-Fidelity RIR Generation]] (75.9% similar)
- [[Multimodal signal fusion for stress detection using deep neural networks_ a novel approach for converting 1D signals to unified 2D images_20250918|Multimodal signal fusion for stress detection using deep neural networks a novel approach for converting 1D signals to unified 2D images]] (75.7% similar)
- [[Listening, Imagining & Refining_ A Heuristic Optimized ASR Correction Framework with LLMs_20250919|Listening, Imagining & Refining A Heuristic Optimized ASR Correction Framework with LLMs]] (75.2% similar)

## 📋 저자 정보

**Authors:** Xiaolei Xu, Chaoyue Niu, Guy J. Brown, Hector Romero, Ning Ma

## 📄 Abstract (원문)

Obstructive sleep apnoea (OSA) is a prevalent condition with significant
health consequences, yet many patients remain undiagnosed due to the complexity
and cost of over-night polysomnography. Acoustic-based screening provides a
scalable alternative, yet performance is limited by environmental noise and the
lack of physiological context. Respiratory effort is a key signal used in
clinical scoring of OSA events, but current approaches require additional
contact sensors that reduce scalability and patient comfort. This paper
presents the first study to estimate respiratory effort directly from nocturnal
audio, enabling physiological context to be recovered from sound alone. We
propose a latent-space fusion framework that integrates the estimated effort
embeddings with acoustic features for OSA detection. Using a dataset of 157
nights from 103 participants recorded in home environments, our respiratory
effort estimator achieves a concordance correlation coefficient of 0.48,
capturing meaningful respiratory dynamics. Fusing effort and audio improves
sensitivity and AUC over audio-only baselines, especially at low
apnoea-hypopnoea index thresholds. The proposed approach requires only
smartphone audio at test time, which enables sensor-free, scalable, and
longitudinal OSA monitoring.

## 🔍 Abstract (한글 번역)

폐쇄성 수면 무호흡증(OSA)은 건강에 중대한 영향을 미치는 흔한 질환이지만, 야간 다원검사의 복잡성과 비용 때문에 많은 환자들이 진단받지 못하고 있습니다. 음향 기반의 선별 검사는 확장 가능한 대안을 제공하지만, 환경 소음과 생리학적 맥락의 부족으로 성능이 제한됩니다. 호흡 노력은 OSA 사건의 임상 점수에 사용되는 주요 신호이지만, 현재의 접근법은 확장성과 환자 편안함을 감소시키는 추가 접촉 센서를 필요로 합니다. 본 논문은 야간 오디오로부터 직접 호흡 노력을 추정하여 소리만으로 생리학적 맥락을 회복할 수 있는 첫 번째 연구를 제시합니다. 우리는 OSA 감지를 위해 추정된 노력 임베딩을 음향 특징과 통합하는 잠재 공간 융합 프레임워크를 제안합니다. 가정 환경에서 녹음된 103명의 참가자로부터 수집된 157박의 데이터셋을 사용하여, 우리의 호흡 노력 추정기는 0.48의 일치 상관 계수를 달성하여 의미 있는 호흡 역학을 포착합니다. 노력과 오디오의 융합은 오디오만 사용한 기준선에 비해 민감도와 AUC를 향상시키며, 특히 낮은 무호흡-저호흡 지수 임계값에서 두드러집니다. 제안된 접근법은 테스트 시 스마트폰 오디오만 필요로 하여, 센서 없는, 확장 가능하며 장기적인 OSA 모니터링을 가능하게 합니다.

## 📝 요약

이 논문은 수면 무호흡증(OSA) 진단을 위해 야간 오디오에서 직접 호흡 노력을 추정하는 최초의 연구를 소개합니다. 기존의 복잡하고 비용이 많이 드는 방법 대신, 스마트폰 오디오만으로 OSA를 모니터링할 수 있는 잠재 공간 융합 프레임워크를 제안합니다. 103명의 참가자 데이터를 사용하여, 호흡 노력 추정기는 0.48의 일치 상관 계수를 기록하며 의미 있는 호흡 역학을 포착했습니다. 이 방법은 오디오와 호흡 노력을 융합하여 민감도와 AUC를 향상시켜, 특히 낮은 무호흡-저호흡 지수 임계값에서 성능을 개선했습니다.

## 🎯 주요 포인트

- 1. 폐쇄성 수면 무호흡증(OSA)은 건강에 심각한 영향을 미치지만, 야간 다원검사의 복잡성과 비용 때문에 많은 환자들이 진단되지 않고 있습니다.

- 2. 본 연구는 야간 오디오만으로 호흡 노력을 추정하여 생리학적 맥락을 회복할 수 있는 첫 번째 연구를 제시합니다.

- 3. 제안된 잠재 공간 융합 프레임워크는 추정된 호흡 노력 임베딩을 음향 특성과 통합하여 OSA를 감지합니다.

- 4. 호흡 노력과 오디오를 융합함으로써 오디오만 사용한 기준선에 비해 민감도와 AUC가 개선되었습니다.

- 5. 제안된 접근 방식은 테스트 시 스마트폰 오디오만 필요로 하여 센서 없는 확장 가능하고 장기적인 OSA 모니터링을 가능하게 합니다.

---

*Generated on 2025-09-20 01:43:02*