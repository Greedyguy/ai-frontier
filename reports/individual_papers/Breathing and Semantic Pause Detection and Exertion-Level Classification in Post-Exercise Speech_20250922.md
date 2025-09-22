# Breathing and Semantic Pause Detection and Exertion-Level Classification in Post-Exercise Speech

**Korean Title:** 운동 후 발화에서 호흡 및 의미적 휴지 탐지와 운동 강도 수준 분류

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Multimodal Analysis, Feature Fusion

## 🔗 유사한 논문
- [[2025-09-18/Multimodal signal fusion for stress detection using deep neural networks_ a novel approach for converting 1D signals to unified 2D images_20250918|Multimodal signal fusion for stress detection using deep neural networks a novel approach for converting 1D signals to unified 2D images]] (78.9% similar)
- [[2025-09-18/Estimating Respiratory Effort from Nocturnal Breathing Sounds for Obstructive Sleep Apnoea Screening_20250918|Estimating Respiratory Effort from Nocturnal Breathing Sounds for Obstructive Sleep Apnoea Screening]] (78.2% similar)
- [[2025-09-22/mucAI at BAREC Shared Task 2025_ Towards Uncertainty Aware Arabic Readability Assessment_20250922|mucAI at BAREC Shared Task 2025 Towards Uncertainty Aware Arabic Readability Assessment]] (77.8% similar)
- [[2025-09-17/Personalization on a Budget_ Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection_20250917|Personalization on a Budget Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (77.2% similar)
- [[2025-09-18/HD3C_ Efficient Medical Data Classification for Embedded Devices_20250918|HD3C Efficient Medical Data Classification for Embedded Devices]] (77.2% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15473v1 Announce Type: cross 
Abstract: Post-exercise speech contains rich physiological and linguistic cues, often marked by semantic pauses, breathing pauses, and combined breathing-semantic pauses. Detecting these events enables assessment of recovery rate, lung function, and exertion-related abnormalities. However, existing works on identifying and distinguishing different types of pauses in this context are limited. In this work, building on a recently released dataset with synchronized audio and respiration signals, we provide systematic annotations of pause types. Using these annotations, we systematically conduct exploratory breathing and semantic pause detection and exertion-level classification across deep learning models (GRU, 1D CNN-LSTM, AlexNet, VGG16), acoustic features (MFCC, MFB), and layer-stratified Wav2Vec2 representations. We evaluate three setups-single feature, feature fusion, and a two-stage detection-classification cascade-under both classification and regression formulations. Results show per-type detection accuracy up to 89$\%$ for semantic, 55$\%$ for breathing, 86$\%$ for combined pauses, and 73$\%$overall, while exertion-level classification achieves 90.5$\%$ accuracy, outperformin prior work.

## 🔍 Abstract (한글 번역)

arXiv:2509.15473v1 발표 유형: 교차  
초록: 운동 후 발화는 풍부한 생리적 및 언어적 단서를 포함하고 있으며, 종종 의미적 멈춤, 호흡 멈춤, 그리고 호흡-의미 결합 멈춤으로 특징지어집니다. 이러한 사건을 감지하면 회복 속도, 폐 기능 및 운동 관련 이상을 평가할 수 있습니다. 그러나 이 맥락에서 다양한 유형의 멈춤을 식별하고 구별하는 기존 연구는 제한적입니다. 이 연구에서는 최근에 공개된 오디오와 호흡 신호가 동기화된 데이터셋을 기반으로 멈춤 유형에 대한 체계적인 주석을 제공합니다. 이러한 주석을 사용하여 심층 학습 모델(GRU, 1D CNN-LSTM, AlexNet, VGG16), 음향 특징(MFCC, MFB), 및 계층별 Wav2Vec2 표현을 통해 탐색적 호흡 및 의미적 멈춤 감지와 운동 수준 분류를 체계적으로 수행합니다. 우리는 단일 특징, 특징 융합, 그리고 두 단계 감지-분류 연쇄라는 세 가지 설정을 분류 및 회귀 공식화 하에 평가합니다. 결과는 의미적 멈춤에 대해 최대 89%, 호흡 멈춤에 대해 55%, 결합 멈춤에 대해 86%, 전체적으로 73%의 유형별 감지 정확도를 보여주며, 운동 수준 분류는 90.5%의 정확도를 달성하여 이전 연구를 능가합니다.

## 📝 요약

이 논문은 운동 후 발화에서 나타나는 다양한 유형의 멈춤(의미적, 호흡적, 결합적)을 탐지하여 회복 속도, 폐 기능 및 운동 관련 이상을 평가하는 방법을 제안합니다. 최근 공개된 동기화된 오디오 및 호흡 신호 데이터셋을 기반으로 체계적인 멈춤 유형 주석을 제공하고, 이를 통해 GRU, 1D CNN-LSTM, AlexNet, VGG16 등의 딥러닝 모델과 MFCC, MFB, Wav2Vec2 등의 음향 특징을 활용하여 멈춤 탐지 및 운동 강도 분류를 수행했습니다. 단일 특징, 특징 융합, 2단계 탐지-분류 접근법을 평가한 결과, 의미적 멈춤 89%, 호흡적 멈춤 55%, 결합적 멈춤 86%, 전체적으로 73%의 탐지 정확도를 보였으며, 운동 강도 분류 정확도는 90.5%로 이전 연구를 능가했습니다.

## 🎯 주요 포인트

- 1. 운동 후 발화에는 의미적 휴지, 호흡 휴지, 결합된 호흡-의미 휴지와 같은 다양한 생리적 및 언어적 단서가 포함되어 있습니다.

- 2. 이 연구에서는 최근 공개된 오디오 및 호흡 신호가 동기화된 데이터셋을 기반으로 휴지 유형에 대한 체계적인 주석을 제공합니다.

- 3. GRU, 1D CNN-LSTM, AlexNet, VGG16과 같은 딥러닝 모델과 MFCC, MFB 등의 음향 특징을 사용하여 휴지 탐지 및 노력 수준 분류를 수행합니다.

- 4. 단일 특징, 특징 융합, 이단계 탐지-분류 연쇄의 세 가지 설정을 평가하며, 의미적 휴지 탐지 정확도는 최대 89%, 호흡 휴지는 55%, 결합된 휴지는 86%, 전체적으로는 73%의 정확도를 보입니다.

- 5. 노력 수준 분류에서는 90.5%의 정확도를 달성하여 이전 연구를 능가합니다.

---

*Generated on 2025-09-22 15:38:47*