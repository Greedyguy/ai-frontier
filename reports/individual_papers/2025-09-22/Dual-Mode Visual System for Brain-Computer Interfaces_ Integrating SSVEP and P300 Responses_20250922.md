# Dual-Mode Visual System for Brain-Computer Interfaces: Integrating SSVEP and P300 Responses

**Korean Title:** 이중 모드 시각 시스템을 통한 뇌-컴퓨터 인터페이스: SSVEP 및 P300 반응 통합

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Hybrid SSVEP and P300 System

## 🔗 유사한 논문
- [[2025-09-22/IEFS-GMB_ Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders_20250922|IEFS-GMB Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders]] (80.1% similar)
- [[2025-09-19/UMind_ A Unified Multitask Network for Zero-Shot MEEG Visual Decoding_20250919|UMind A Unified Multitask Network for Zero-Shot MEEG Visual Decoding]] (79.8% similar)
- [[2025-09-17/Personalization on a Budget_ Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection_20250917|Personalization on a Budget Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (79.1% similar)
- [[2025-09-19/Sensing the Shape of Data_ Non-Visual Exploration of Statistical Concepts in Histograms with Blind and Low-Vision Learners_20250919|Sensing the Shape of Data Non-Visual Exploration of Statistical Concepts in Histograms with Blind and Low-Vision Learners]] (78.4% similar)
- [[2025-09-17/Exploring the Relationship between Brain Hemisphere States and Frequency Bands through Deep Learning Optimization Techniques_20250917|Exploring the Relationship between Brain Hemisphere States and Frequency Bands through Deep Learning Optimization Techniques]] (78.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15439v1 Announce Type: cross 
Abstract: In brain-computer interface (BCI) systems, steady-state visual evoked potentials (SSVEP) and P300 responses have achieved widespread implementation owing to their superior information transfer rates (ITR) and minimal training requirements. These neurophysiological signals have exhibited robust efficacy and versatility in external device control, demonstrating enhanced precision and scalability. However, conventional implementations predominantly utilise liquid crystal display (LCD)-based visual stimulation paradigms, which present limitations in practical deployment scenarios. This investigation presents the development and evaluation of a novel light-emitting diode (LED)-based dual stimulation apparatus designed to enhance SSVEP classification accuracy through the integration of both SSVEP and P300 paradigms. The system employs four distinct frequencies, 7 Hz, 8 Hz, 9 Hz, and 10 Hz, corresponding to forward, backward, right, and left directional controls, respectively. Oscilloscopic verification confirmed the precision of these stimulation frequencies. Real-time feature extraction was accomplished through the concurrent analysis of maximum Fast Fourier Transform (FFT) amplitude and P300 peak detection to ascertain user intent. Directional control was determined by the frequency exhibiting maximal amplitude characteristics. The visual stimulation hardware demonstrated minimal frequency deviation, with error differentials ranging from 0.15%to 0.20%across all frequencies. The implemented signal processing algorithm successfully discriminated all four stimulus frequencies whilst correlating them with their respective P300 event markers. Classification accuracy was evaluated based on correct task intention recognition. The proposed hybrid system achieved a mean classification accuracy of 86.25%, coupled with an average ITR of 42.08 bits per minute (bpm).

## 🔍 Abstract (한글 번역)

arXiv:2509.15439v1 발표 유형: 교차  
초록: 뇌-컴퓨터 인터페이스(BCI) 시스템에서 지속적 시각 유발 전위(SSVEP)와 P300 반응은 우수한 정보 전송률(ITR)과 최소한의 훈련 요구사항 덕분에 널리 구현되고 있습니다. 이러한 신경생리학적 신호는 외부 장치 제어에서 강력한 효율성과 다재다능성을 보여주며, 향상된 정밀도와 확장성을 입증했습니다. 그러나 기존 구현은 주로 액정 디스플레이(LCD) 기반의 시각 자극 패러다임을 사용하며, 이는 실용적인 배포 시나리오에서 제한점을 나타냅니다. 본 연구는 SSVEP 분류 정확도를 향상시키기 위해 SSVEP와 P300 패러다임을 통합한 새로운 발광 다이오드(LED) 기반 이중 자극 장치의 개발 및 평가를 제시합니다. 시스템은 각각 전진, 후진, 오른쪽, 왼쪽 방향 제어에 해당하는 7 Hz, 8 Hz, 9 Hz, 10 Hz의 네 가지 주파수를 사용합니다. 오실로스코프 검증을 통해 이러한 자극 주파수의 정확성을 확인했습니다. 실시간 특징 추출은 최대 고속 푸리에 변환(FFT) 진폭과 P300 피크 검출의 동시 분석을 통해 사용자 의도를 파악하여 수행되었습니다. 방향 제어는 최대 진폭 특성을 보이는 주파수에 의해 결정되었습니다. 시각 자극 하드웨어는 모든 주파수에서 0.15%에서 0.20% 범위의 오류 차이를 보이며 최소한의 주파수 편차를 나타냈습니다. 구현된 신호 처리 알고리즘은 모든 네 가지 자극 주파수를 성공적으로 구별하고 각각의 P300 이벤트 마커와 연관시켰습니다. 분류 정확도는 올바른 작업 의도 인식을 기반으로 평가되었습니다. 제안된 하이브리드 시스템은 평균 86.25%의 분류 정확도와 분당 42.08 비트(bpm)의 평균 ITR을 달성했습니다.

## 📝 요약

이 논문은 뇌-컴퓨터 인터페이스(BCI) 시스템에서 SSVEP와 P300 반응을 활용한 새로운 LED 기반 이중 자극 장치를 개발하고 평가했습니다. 기존의 LCD 기반 시각 자극의 한계를 극복하고자, 7Hz, 8Hz, 9Hz, 10Hz의 네 가지 주파수를 사용하여 방향 제어를 구현했습니다. 실시간 특징 추출은 FFT 최대 진폭과 P300 피크 검출을 통해 사용자 의도를 파악했습니다. 주파수 편차는 0.15%에서 0.20%로 매우 적었으며, 제안된 시스템은 평균 86.25%의 분류 정확도와 42.08 bpm의 정보 전송률을 달성했습니다.

## 🎯 주요 포인트

- 1. 본 연구는 SSVEP와 P300 패러다임을 통합한 새로운 LED 기반 이중 자극 장치를 개발하여 SSVEP 분류 정확도를 향상시켰습니다.

- 2. 시스템은 7 Hz, 8 Hz, 9 Hz, 10 Hz의 네 가지 주파수를 사용하여 각각 전진, 후진, 우측, 좌측 방향 제어를 구현했습니다.

- 3. 최대 FFT 진폭과 P300 피크 검출을 통한 실시간 특징 추출로 사용자 의도를 파악했습니다.

- 4. 제안된 하이브리드 시스템은 평균 86.25%의 분류 정확도와 42.08 bpm의 정보 전송률을 달성했습니다.

- 5. 시각적 자극 하드웨어는 모든 주파수에서 0.15%에서 0.20%의 최소 주파수 편차를 보였습니다.

---

*Generated on 2025-09-22 13:56:31*