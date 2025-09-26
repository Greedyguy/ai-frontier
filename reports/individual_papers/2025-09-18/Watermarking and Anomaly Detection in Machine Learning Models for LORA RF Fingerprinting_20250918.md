---
keywords:
  - Convolutional Neural Networks
  - Anomaly Detection
  - Radio Frequency Fingerprint Identification
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:01:37.712335",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Convolutional Neural Networks",
    "Anomaly Detection",
    "Radio Frequency Fingerprint Identification"
  ],
  "rejected_keywords": [
    "Watermarking",
    "Generative Models"
  ],
  "similarity_scores": {
    "Convolutional Neural Networks": 0.82,
    "Anomaly Detection": 0.8,
    "Radio Frequency Fingerprint Identification": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Watermarking and Anomaly Detection in Machine Learning Models for LORA RF Fingerprinting

**Korean Title:** 기계 학습 모델에서 LORA RF 핑거프린팅을 위한 워터마킹 및 이상 탐지

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]     [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Anomaly Detection|Anomaly Detection]]
**🔗 Specific Connectable**: [[keywords/Convolutional Neural Networks|ResNet-34]]
**⚡ Unique Technical**: [[keywords/Radio Frequency Fingerprint Identification|Radio Frequency Fingerprint Identification]]

## 🔗 유사한 논문
- [[RationAnomaly_ Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning_20250919|RationAnomaly Log Anomaly Detection with Rationality via Chain-of-Thought and Reinforcement Learning]] (78.2% similar)
- [[Lost in Translation Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation_20250918|Lost in Translation Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation]] (77.5% similar)
- [[Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (77.0% similar)
- [[Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (76.8% similar)
- [[Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning_20250919|Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning]] (76.7% similar)

## 📋 저자 정보

**Authors:** Aarushi Mahajan, Wayne Burleson

## 📄 Abstract (원문)

Radio frequency fingerprint identification (RFFI) distinguishes wireless
devices by the small variations in their analog circuits, avoiding heavy
cryptographic authentication. While deep learning on spectrograms improves
accuracy, models remain vulnerable to copying, tampering, and evasion. We
present a stronger RFFI system combining watermarking for ownership proof and
anomaly detection for spotting suspicious inputs. Using a ResNet-34 on log-Mel
spectrograms, we embed three watermarks: a simple trigger, an adversarially
trained trigger robust to noise and filtering, and a hidden gradient/weight
signature. A convolutional Variational Autoencoders (VAE) with Kullback-Leibler
(KL) warm-up and free-bits flags off-distribution queries. On the LoRa dataset,
our system achieves 94.6% accuracy, 98% watermark success, and 0.94 AUROC,
offering verifiable, tamper-resistant authentication.

## 🔍 Abstract (한글 번역)

라디오 주파수 지문 인식(RFFI)은 무선 장치의 아날로그 회로에서 발생하는 미세한 변화를 통해 장치를 구별하며, 무거운 암호화 인증을 피할 수 있습니다. 스펙트로그램에 대한 딥러닝은 정확도를 향상시키지만, 모델은 여전히 복제, 변조, 회피에 취약합니다. 우리는 소유권 증명을 위한 워터마킹과 의심스러운 입력을 감지하기 위한 이상 탐지를 결합한 강력한 RFFI 시스템을 제시합니다. 로그-멜 스펙트로그램에서 ResNet-34를 사용하여 세 가지 워터마크를 삽입합니다: 간단한 트리거, 노이즈와 필터링에 강한 적대적 학습 트리거, 숨겨진 그래디언트/가중치 서명입니다. Kullback-Leibler(KL) 워밍업과 자유 비트를 사용하는 컨볼루션 변이 오토인코더(VAE)는 분포 외 쿼리를 감지합니다. LoRa 데이터셋에서, 우리의 시스템은 94.6%의 정확도, 98%의 워터마크 성공률, 0.94 AUROC를 달성하여 검증 가능하고 변조에 강한 인증을 제공합니다.

## 📝 요약

이 논문은 무선 기기의 아날로그 회로의 미세한 변화를 이용해 기기를 식별하는 무선 주파수 지문 인식(RFFI) 시스템을 제안합니다. 기존의 심층 학습 기반 모델의 취약점을 보완하기 위해 워터마킹과 이상 탐지를 결합한 강력한 RFFI 시스템을 개발했습니다. ResNet-34 모델을 사용하여 로그-멜 스펙트로그램에서 세 가지 워터마크를 삽입하고, 변형 오토인코더(VAE)를 활용해 이상 입력을 탐지합니다. LoRa 데이터셋에서 94.6%의 정확도와 98%의 워터마크 성공률, 0.94의 AUROC를 달성하여 검증 가능하고 변조에 강한 인증을 제공합니다.

## 🎯 주요 포인트

- 1. 무선 장치 식별을 위한 RFFI 시스템은 아날로그 회로의 미세한 변화를 이용하여 암호학적 인증을 피합니다.

- 2. ResNet-34 모델을 사용하여 로그-멜 스펙트로그램에 세 가지 워터마크를 삽입하여 소유권 증명과 이상 탐지를 강화합니다.

- 3. 제안된 시스템은 LoRa 데이터셋에서 94.6%의 정확도와 98%의 워터마크 성공률을 달성합니다.

- 4. 변형 오토인코더(VAE)를 활용하여 분포 외 쿼리를 탐지하고, 시스템의 위변조 저항성을 높입니다.

- 5. 본 연구는 딥러닝 모델의 복제, 변조 및 회피에 대한 취약성을 해결하기 위한 방법을 제시합니다.

---

*Generated on 2025-09-20 00:54:15*