# Hybrid Deep Learning-Federated Learning Powered Intrusion Detection System for IoT/5G Advanced Edge Computing Network

**Korean Title:** 하이브리드 딥러닝-연합 학습 기반 IoT/5G 첨단 엣지 컴퓨팅 네트워크 침입 탐지 시스템

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Convolutional Neural Network, Bidirectional LSTM

## 🔗 유사한 논문
- [[2025-09-22/Threat Modeling for Enhancing Security of IoT Audio Classification Devices under a Secure Protocols Framework_20250922|Threat Modeling for Enhancing Security of IoT Audio Classification Devices under a Secure Protocols Framework]] (82.9% similar)
- [[2025-09-22/Hybrid Temporal Differential Consistency Autoencoder for Efficient and Sustainable Anomaly Detection in Cyber-Physical Systems_20250922|Hybrid Temporal Differential Consistency Autoencoder for Efficient and Sustainable Anomaly Detection in Cyber-Physical Systems]] (82.8% similar)
- [[2025-09-18/Anomaly Detection in Offshore Open Radio Access Network Using Long Short-Term Memory Models on a Novel Artificial Intelligence-Driven Cloud-Native Data Platform_20250918|Anomaly Detection in Offshore Open Radio Access Network Using Long Short-Term Memory Models on a Novel Artificial Intelligence-Driven Cloud-Native Data Platform]] (82.1% similar)
- [[2025-09-18/BERTector_ An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model_20250918|BERTector An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model]] (82.1% similar)
- [[2025-09-18/Threat Modeling for Enhancing Security of IoT Audio Classification Devices under a Secure Protocols Framework_20250918|Threat Modeling for Enhancing Security of IoT Audio Classification Devices under a Secure Protocols Framework]] (82.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15555v1 Announce Type: cross 
Abstract: The exponential expansion of IoT and 5G-Advanced applications has enlarged the attack surface for DDoS, malware, and zero-day intrusions. We propose an intrusion detection system that fuses a convolutional neural network (CNN), a bidirectional LSTM (BiLSTM), and an autoencoder (AE) bottleneck within a privacy-preserving federated learning (FL) framework. The CNN-BiLSTM branch captures local and gated cross-feature interactions, while the AE emphasizes reconstruction-based anomaly sensitivity. Training occurs across edge devices without sharing raw data. On UNSW-NB15 (binary), the fused model attains AUC 99.59 percent and F1 97.36 percent; confusion-matrix analysis shows balanced error rates with high precision and recall. Average inference time is approximately 0.0476 ms per sample on our test hardware, which is well within the less than 10 ms URLLC budget, supporting edge deployment. We also discuss explainability, drift tolerance, and FL considerations for compliant, scalable 5G-Advanced IoT security.

## 🔍 Abstract (한글 번역)

arXiv:2509.15555v1 발표 유형: 교차  
초록: IoT와 5G-Advanced 애플리케이션의 기하급수적인 확장은 DDoS, 악성코드, 제로데이 침입에 대한 공격 표면을 확대했습니다. 우리는 프라이버시를 보호하는 연합 학습(FL) 프레임워크 내에서 합성곱 신경망(CNN), 양방향 LSTM(BiLSTM), 오토인코더(AE) 병목을 융합한 침입 탐지 시스템을 제안합니다. CNN-BiLSTM 분기는 지역적 및 게이트된 교차 특징 상호작용을 포착하며, AE는 재구성 기반의 이상 감도를 강조합니다. 훈련은 원시 데이터를 공유하지 않고 엣지 디바이스에서 이루어집니다. UNSW-NB15(이진)에서 융합 모델은 AUC 99.59%와 F1 97.36%를 달성했으며, 혼동 행렬 분석은 높은 정밀도와 재현율을 가진 균형 잡힌 오류율을 보여줍니다. 평균 추론 시간은 테스트 하드웨어에서 샘플당 약 0.0476 ms로, 10 ms 미만의 URLLC 예산 내에 있어 엣지 배포를 지원합니다. 우리는 또한 설명 가능성, 드리프트 내성, 그리고 준수 가능하고 확장 가능한 5G-Advanced IoT 보안을 위한 FL 고려 사항에 대해 논의합니다.

## 📝 요약

이 논문은 IoT와 5G-Advanced 환경에서 증가하는 보안 위협에 대응하기 위한 침입 탐지 시스템을 제안합니다. 제안된 시스템은 CNN, BiLSTM, AE를 결합한 모델로, 프라이버시를 보호하는 연합 학습 프레임워크 내에서 작동합니다. CNN-BiLSTM은 지역적 및 교차 특징 상호작용을 포착하고, AE는 이상 탐지에 민감하게 반응합니다. UNSW-NB15 데이터셋에서 AUC 99.59%, F1 97.36%의 성능을 보였으며, 평균 추론 시간은 0.0476ms로, 엣지 디바이스에 적합합니다. 또한 설명 가능성, 드리프트 내성, FL 관련 고려사항을 논의합니다.

## 🎯 주요 포인트

- 1. IoT와 5G-Advanced 애플리케이션의 확장으로 DDoS, 멀웨어, 제로데이 침입에 대한 공격 표면이 확대되었습니다.

- 2. 제안된 침입 탐지 시스템은 CNN, BiLSTM, AE 병목을 프라이버시 보호 연합 학습 프레임워크 내에서 결합하여 사용합니다.

- 3. 제안된 모델은 UNSW-NB15 데이터셋에서 AUC 99.59%와 F1 97.36%를 달성하며, 높은 정밀도와 재현율을 보여줍니다.

- 4. 평균 추론 시간은 샘플당 약 0.0476 ms로, 10 ms 미만의 URLLC 예산 내에 있어 엣지 배포를 지원합니다.

- 5. 설명 가능성, 드리프트 내성, 연합 학습 고려 사항을 통해 5G-Advanced IoT 보안의 확장 가능성을 논의합니다.

---

*Generated on 2025-09-22 15:39:41*