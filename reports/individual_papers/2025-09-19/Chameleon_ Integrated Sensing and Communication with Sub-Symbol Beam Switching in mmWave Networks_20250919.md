---
keywords:
  - Integrated Sensing and Communication
  - Object Localization
  - Beamforming
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14628
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:53:12.328931",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Integrated Sensing and Communication",
    "Object Localization",
    "Beamforming"
  ],
  "rejected_keywords": [
    "Machine Learning"
  ],
  "similarity_scores": {
    "Integrated Sensing and Communication": 0.78,
    "Object Localization": 0.77,
    "Beamforming": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Chameleon: Integrated Sensing and Communication with Sub-Symbol Beam Switching in mmWave Networks

**Korean Title:** 카멜레온: 밀리미터파 네트워크에서 하위 심볼 빔 스위칭을 통한 통합 감지 및 통신

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Beamforming|Beamforming]]
**🔗 Specific Connectable**: [[keywords/Object Localization|Object Localization]]
**⚡ Unique Technical**: [[keywords/Integrated Sensing and Communication|Integrated Sensing and Communication]]

## 🔗 유사한 논문
- [[RF-LSCM Pushing Radiance Fields to Multi-Domain Localized Statistical Channel Modeling for Cellular Network Optimization]] (83.5% similar)
- [[FAWN A MultiEncoder Fusion-Attention Wave Network for Integrated Sensing and Communication Indoor Scene Inference]] (82.7% similar)
- [[A Software-Defined Radio Testbed for Distributed LiDAR Point Cloud Sharing with IEEE 802.11p in V2V Networks_20250919|A Software-Defined Radio Testbed for Distributed LiDAR Point Cloud Sharing with IEEE 802.11p in V2V Networks]] (80.0% similar)
- [[An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing_20250919|An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing]] (78.9% similar)
- [[Joint Power and Spectrum Orchestration for D2D Semantic Communication Underlying Energy-Efficient Cellular Networks_20250918|Joint Power and Spectrum Orchestration for D2D Semantic Communication Underlying Energy-Efficient Cellular Networks]] (78.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14628v1 Announce Type: new 
Abstract: Next-generation cellular networks are envisioned to integrate sensing capabilities with communication, particularly in the millimeter-wave (mmWave) spectrum, where beamforming using large-scale antenna arrays enables directional signal transmissions for improved spatial multiplexing. In current 5G networks, however, beamforming is typically designed either for communication or sensing (e.g., beam training during link establishment). In this paper, we present Chameleon, a novel framework that augments and rapidly switches beamformers during each demodulation reference signal (DMRS) symbol to achieve integrated sensing and communication (ISAC) in 5G mmWave networks. Each beamformer introduces an additional sensing beam toward target angles while maintaining the communication beams toward multiple users. We implement Chameleon on a 28 GHz software-defined radio testbed supporting over-the-air 5G physical downlink shared channel (PDSCH) transmissions. Extensive experiments in open environments show that Chameleon achieves multi-user communication with a sum data rate of up to 0.80 Gbps across two users. Simultaneously, Chameleon employs a beamformer switching interval of only 0.24 {\mu}s, therefore producing a 31x31-point 2D imaging within just 0.875 ms. Leveraging machine learning, Chameleon further enables object localization with median errors of 0.14 m (distance) and 0.24{\deg} (angle), and material classification with 99.0% accuracy.

## 🔍 Abstract (한글 번역)

arXiv:2509.14628v1 발표 유형: 신규  
초록: 차세대 셀룰러 네트워크는 통신과 함께 감지 기능을 통합할 것으로 예상되며, 특히 대규모 안테나 배열을 사용한 빔포밍이 향상된 공간 다중화를 위해 방향성 신호 전송을 가능하게 하는 밀리미터파(mmWave) 스펙트럼에서 그러합니다. 그러나 현재의 5G 네트워크에서는 빔포밍이 일반적으로 통신 또는 감지(예: 링크 설정 중 빔 트레이닝)를 위해 설계됩니다. 본 논문에서는 5G mmWave 네트워크에서 통합 감지 및 통신(ISAC)을 달성하기 위해 각 복조 참조 신호(DMRS) 심볼 동안 빔포머를 증강하고 빠르게 전환하는 새로운 프레임워크인 Chameleon을 제시합니다. 각 빔포머는 여러 사용자에 대한 통신 빔을 유지하면서 목표 각도 쪽으로 추가적인 감지 빔을 도입합니다. 우리는 28 GHz 소프트웨어 정의 라디오 테스트베드에서 Chameleon을 구현하여 무선 5G 물리적 하향 링크 공유 채널(PDSCH) 전송을 지원합니다. 개방된 환경에서의 광범위한 실험은 Chameleon이 두 사용자에 걸쳐 최대 0.80 Gbps의 총 데이터 속도로 다중 사용자 통신을 달성함을 보여줍니다. 동시에, Chameleon은 단 0.24 μs의 빔포머 전환 간격을 사용하여 단 0.875 ms 내에 31x31 포인트 2D 이미징을 생성합니다. 머신 러닝을 활용하여, Chameleon은 0.14 m(거리) 및 0.24°(각도)의 중간 오류로 객체 위치 추정을 가능하게 하고, 99.0%의 정확도로 재료 분류를 수행합니다.

## 📝 요약

이 논문은 차세대 셀룰러 네트워크에서 통신과 센싱을 통합하는 새로운 프레임워크인 Chameleon을 제안합니다. Chameleon은 5G 밀리미터파 네트워크에서 각 디모듈레이션 참조 신호(DMRS) 심볼 동안 빔포머를 빠르게 전환하여 통신과 센싱을 동시에 수행합니다. 28 GHz 소프트웨어 정의 라디오 테스트베드에서 구현된 Chameleon은 두 사용자 간 최대 0.80 Gbps의 데이터 전송 속도를 달성하며, 0.24 μs의 빔포머 전환 간격을 통해 0.875 ms 내에 31x31 포인트 2D 이미징을 수행합니다. 또한, 머신러닝을 활용하여 0.14 m의 거리 및 0.24도의 각도 오차로 객체 위치를 파악하고, 99.0%의 정확도로 재질 분류를 수행합니다.

## 🎯 주요 포인트

- 1. 차세대 셀룰러 네트워크는 밀리미터파 스펙트럼에서 통신과 센싱 기능을 통합할 것으로 예상됩니다.

- 2. Chameleon은 5G 밀리미터파 네트워크에서 통합 센싱 및 통신(ISAC)을 구현하기 위해 DMRS 심볼 동안 빔포머를 증강하고 빠르게 전환하는 새로운 프레임워크입니다.

- 3. Chameleon은 28 GHz 소프트웨어 정의 라디오 테스트베드에서 구현되어, 두 사용자 간 최대 0.80 Gbps의 합산 데이터 속도로 다중 사용자 통신을 달성합니다.

- 4. Chameleon은 0.24 μs의 빔포머 전환 간격을 사용하여 0.875 ms 내에 31x31 포인트의 2D 이미징을 생성합니다.

- 5. 머신러닝을 활용하여 Chameleon은 0.14 m의 거리 및 0.24°의 각도 오차로 객체 위치를 파악하고, 99.0%의 정확도로 재질을 분류할 수 있습니다.

---

*Generated on 2025-09-19 16:27:25*