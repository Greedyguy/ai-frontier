---
keywords:
  - WiFi Sensing
  - Channel State Information
  - Automatic Gain Control
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13807
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:31:58.925052",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "WiFi Sensing",
    "Channel State Information",
    "Automatic Gain Control"
  ],
  "rejected_keywords": [
    "802.11 Protocols"
  ],
  "similarity_scores": {
    "WiFi Sensing": 0.78,
    "Channel State Information": 0.77,
    "Automatic Gain Control": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Domino: Dominant Path-based Compensation for Hardware Impairments in Modern WiFi Sensing

**Korean Title:** 도미노: 최신 WiFi 센싱에서 하드웨어 장애 보상을 위한 지배적인 경로 기반 보상

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Automatic Gain Control|Automatic Gain Control]]
**⚡ Unique Technical**: [[keywords/WiFi Sensing|WiFi Sensing]], [[keywords/Channel State Information|Channel State Information]]

## 🔗 유사한 논문
- [[RF-LSCM: Pushing Radiance Fields to Multi-Domain Localized Statistical Channel Modeling for Cellular Network Optimization]] (78.2% similar)
- [[BERTector_An_Intrusion_Detection_Framework_Constructed_via_Joint-dataset_Learning_Based_on_Language_Model_20250918|BERTector: An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model]] (75.8% similar)
- [[Queen Detection in Beehives via Environmental Sensor Fusion for Low-Power Edge Computing]] (75.4% similar)
- [[Dual Actor DDPG for Airborne STAR-RIS Assisted Communications]] (75.0% similar)
- [[Anomaly_Detection_in_Offshore_Open_Radio_Access_Network_Using_Long_Short-Term_Memory_Models_on_a_Novel_Artificial_Intelligence-Driven_Cloud-Native_Data_Platform_20250918|Anomaly Detection in Offshore Open Radio Access Network Using Long Short-Term Memory Models on a Novel Artificial Intelligence-Driven Cloud-Native Data Platform]] (75.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13807v1 Announce Type: cross 
Abstract: WiFi sensing faces a critical reliability challenge due to hardware-induced RF distortions, especially with modern, market-dominant WiFi cards supporting 802.11ac/ax protocols. These cards employ sensitive automatic gain control and separate RF chains, introducing complex and dynamic distortions that render existing compensation methods ineffective. In this paper, we introduce Domino, a new framework that transforms channel state information (CSI) into channel impulse response (CIR) and leverages it for precise distortion compensation. Domino is built on the key insight that hardware-induced distortions impact all signal paths uniformly, allowing the dominant static path to serve as a reliable reference for effective compensation through delay-domain processing. Real-world respiration monitoring experiments show that Domino achieves at least 2x higher mean accuracy over existing methods, maintaining robust performance with a median error below 0.24 bpm, even using a single antenna in both direct line-of-sight and obstructed scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2509.13807v1 발표 유형: 교차
요약: WiFi 센싱은 하드웨어로 인한 RF 왜곡으로 인한 신뢰성에 중대한 도전을 겪고 있습니다, 특히 802.11ac/ax 프로토콜을 지원하는 현대의 시장 지배적인 WiFi 카드들과 함께. 이러한 카드들은 민감한 자동 이득 제어 및 별도의 RF 체인을 사용하여 기존 보상 방법을 효과적으로 만드는 복잡하고 동적인 왜곡을 도입합니다. 본 논문에서는 채널 상태 정보(CSI)를 채널 임펄스 응답(CIR)으로 변환하고 정확한 왜곡 보상을 위해 그것을 활용하는 새로운 프레임워크인 Domino를 소개합니다. Domino는 하드웨어로 인한 왜곡이 모든 신호 경로에 균일하게 영향을 미치기 때문에, 지연 도메인 처리를 통해 효과적인 보상을 위한 신뢰할 수 있는 참조로서 주요 정적 경로를 활용합니다. 실제 세계 호흡 모니터링 실험에서 Domino는 기존 방법보다 최소 2배 이상 높은 평균 정확도를 달성하며, 직접 시야 및 가로막힌 시나리오에서도 중간 오차가 0.24 bpm 이하인 단일 안테나를 사용하여 견고한 성능을 유지합니다.

## 📝 요약

이 연구는 WiFi 센싱이 현대 시장을 지배하는 802.11ac/ax 프로토콜을 지원하는 WiFi 카드의 하드웨어로 인한 RF 왜곡으로 신뢰성 문제를 겪고 있음을 밝힙니다. 기존 보상 방법이 효과적이지 못한 복잡하고 동적인 왜곡을 도입하는 이러한 카드는 Domino라는 새로운 프레임워크를 소개합니다. Domino은 하드웨어로 인한 왜곡이 모든 신호 경로에 동일하게 영향을 미치기 때문에 지연 도메인 처리를 통해 효과적인 보상을 가능하게 합니다. Domino은 기존 방법보다 최소 2배 높은 평균 정확도를 달성하며, 직접 시야 및 가로막힌 시나리오에서도 중앙 오차가 0.24 bpm 이하로 유지됩니다.

## 🎯 주요 포인트

- 1. WiFi sensing의 신뢰성 도전: 하드웨어로 인한 RF 왜곡

- 2. Domino 프레임워크: CSI를 CIR로 변환하여 왜곡 보상

- 3. Domino의 성능: 기존 방법보다 2배 높은 정확도 달성

- 4. 실시간 호흡 모니터링 실험 결과: Domino는 낮은 오차로 강력한 성능 유지.

---

*Generated on 2025-09-18 17:13:47*