# Watermarking and Anomaly Detection in Machine Learning Models for LORA RF Fingerprinting

**Korean Title:** LORA RF 핑거프린팅을 위한 머신 러닝 모델에서의 워터마킹 및 이상 탐지

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Anomaly Detection, Watermarking

## 🔗 유사한 논문
- [[2025-09-18/Watermarking and Anomaly Detection in Machine Learning Models for LORA RF Fingerprinting_20250918|Watermarking and Anomaly Detection in Machine Learning Models for LORA RF Fingerprinting]] (98.5% similar)
- [[2025-09-22/VLA-Mark_ A cross modal watermark for large vision-language alignment model_20250922|VLA-Mark A cross modal watermark for large vision-language alignment model]] (82.5% similar)
- [[2025-09-17/Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection_20250917|Mixture of Low-Rank Adapter Experts in Generalizable Audio Deepfake Detection]] (81.7% similar)
- [[2025-09-19/RationAnomaly_ Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning_20250919|RationAnomaly Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning]] (79.9% similar)
- [[2025-09-22/Threat Modeling for Enhancing Security of IoT Audio Classification Devices under a Secure Protocols Framework_20250922|Threat Modeling for Enhancing Security of IoT Audio Classification Devices under a Secure Protocols Framework]] (79.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15170v2 Announce Type: replace-cross 
Abstract: Radio frequency fingerprint identification (RFFI) distinguishes wireless devices by the small variations in their analog circuits, avoiding heavy cryptographic authentication. While deep learning on spectrograms improves accuracy, models remain vulnerable to copying, tampering, and evasion. We present a stronger RFFI system combining watermarking for ownership proof and anomaly detection for spotting suspicious inputs. Using a ResNet-34 on log-Mel spectrograms, we embed three watermarks: a simple trigger, an adversarially trained trigger robust to noise and filtering, and a hidden gradient/weight signature. A convolutional Variational Autoencoders (VAE) with Kullback-Leibler (KL) warm-up and free-bits flags off-distribution queries. On the LoRa dataset, our system achieves 94.6% accuracy, 98% watermark success, and 0.94 AUROC, offering verifiable, tamper-resistant authentication.

## 🔍 Abstract (한글 번역)

arXiv:2509.15170v2 발표 유형: 교차 교체  
초록: 무선 주파수 지문 식별(RFFI)은 무선 장치의 아날로그 회로에서 발생하는 미세한 변화를 통해 장치를 구별하며, 무거운 암호학적 인증을 피할 수 있습니다. 스펙트로그램에 대한 딥러닝이 정확성을 향상시키지만, 모델은 여전히 복제, 변조, 회피에 취약합니다. 우리는 소유권 증명을 위한 워터마킹과 의심스러운 입력을 탐지하기 위한 이상 탐지를 결합한 강력한 RFFI 시스템을 제시합니다. 로그-멜 스펙트로그램에서 ResNet-34를 사용하여 세 가지 워터마크를 삽입합니다: 간단한 트리거, 노이즈 및 필터링에 강한 적대적 훈련 트리거, 숨겨진 그래디언트/가중치 서명. Kullback-Leibler (KL) 웜업과 자유 비트 플래그를 사용하는 컨볼루션 변분 오토인코더(VAE)는 분포 외 쿼리를 탐지합니다. LoRa 데이터셋에서 우리의 시스템은 94.6%의 정확도, 98%의 워터마크 성공률, 0.94 AUROC를 달성하여 검증 가능하고 변조에 저항하는 인증을 제공합니다.

## 📝 요약

이 논문은 무선 기기의 아날로그 회로의 미세한 변화를 이용하여 기기를 식별하는 무선 주파수 지문 인식(RFFI) 시스템을 제안합니다. 기존의 스펙트로그램 기반 딥러닝 모델의 취약점을 보완하기 위해, 저자는 소유권 증명을 위한 워터마킹과 의심스러운 입력을 감지하는 이상 탐지를 결합한 강력한 RFFI 시스템을 개발했습니다. ResNet-34 모델을 사용하여 로그-Mel 스펙트로그램에 세 가지 워터마크를 삽입했으며, 변형 오토인코더(VAE)를 활용하여 분포 밖의 쿼리를 탐지합니다. LoRa 데이터셋에서 이 시스템은 94.6%의 정확도, 98%의 워터마크 성공률, 0.94의 AUROC를 달성하여 검증 가능하고 변조에 강한 인증을 제공합니다.

## 🎯 주요 포인트

- 1. 무선 주파수 지문 인식(RFFI)은 아날로그 회로의 미세한 변화를 통해 무선 기기를 구별하며, 무거운 암호 인증을 피할 수 있습니다.

- 2. 스펙트로그램에 대한 딥러닝은 정확성을 향상시키지만, 모델은 여전히 복제, 변조, 회피에 취약합니다.

- 3. 본 연구는 소유권 증명을 위한 워터마킹과 의심스러운 입력을 감지하기 위한 이상 탐지를 결합한 강력한 RFFI 시스템을 제안합니다.

- 4. ResNet-34를 사용하여 로그-멜 스펙트로그램에 세 가지 워터마크를 삽입하며, 이는 단순 트리거, 잡음 및 필터링에 강한 적대적 훈련 트리거, 숨겨진 그래디언트/가중치 서명입니다.

- 5. LoRa 데이터셋에서 제안된 시스템은 94.6%의 정확도, 98%의 워터마크 성공률, 0.94의 AUROC를 달성하여 검증 가능하고 변조에 강한 인증을 제공합니다.

---

*Generated on 2025-09-22 15:08:43*