---
keywords:
  - Low-Power Edge Computing
  - Environmental Sensor Fusion
  - Precision Beekeeping
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:46:53.148695",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Low-Power Edge Computing",
    "Environmental Sensor Fusion",
    "Precision Beekeeping"
  ],
  "rejected_keywords": [
    "Quantized Decision Tree Inference"
  ],
  "similarity_scores": {
    "Low-Power Edge Computing": 0.8,
    "Environmental Sensor Fusion": 0.78,
    "Precision Beekeeping": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Queen Detection in Beehives via Environmental Sensor Fusion for Low-Power Edge Computing

**Korean Title:** 벌집에서의 여왕벌 탐지를 위한 저전력 엣지 컴퓨팅 환경 센서 융합 연구

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]     [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Environmental Sensor Fusion|environmental sensor fusion]]
**🚀 Evolved Concepts**: [[keywords/Low-Power Edge Computing|low-power edge computing]], [[keywords/Precision Beekeeping|precision beekeeping]]

## 🔗 유사한 논문
- [[Estimating Respiratory Effort from Nocturnal Breathing Sounds for Obstructive Sleep Apnoea Screening_20250918|Estimating Respiratory Effort from Nocturnal Breathing Sounds for Obstructive Sleep Apnoea Screening]] (76.3% similar)
- [[Domino_ Dominant Path-based Compensation for Hardware Impairments in Modern WiFi Sensing_20250918|Domino Dominant Path-based Compensation for Hardware Impairments in Modern WiFi Sensing]] (76.3% similar)
- [[HD3C_ Efficient Medical Data Classification for Embedded Devices_20250918|HD3C Efficient Medical Data Classification for Embedded Devices]] (76.1% similar)
- [[A Novel Compression Framework for YOLOv8_ Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation_20250918|A Novel Compression Framework for YOLOv8 Achieving Real-Time Aerial Object Detection on Edge Devices via Structured Pruning and Channel-Wise Distillation]] (76.1% similar)
- [[UCorr_ Wire Detection and Depth Estimation for Autonomous Drones_20250919|UCorr Wire Detection and Depth Estimation for Autonomous Drones]] (76.0% similar)

## 📋 저자 정보

**Authors:** Chiara De Luca, Elisa Donati

## 📄 Abstract (원문)

Queen bee presence is essential for the health and stability of honeybee
colonies, yet current monitoring methods rely on manual inspections that are
labor-intensive, disruptive, and impractical for large-scale beekeeping. While
recent audio-based approaches have shown promise, they often require high power
consumption, complex preprocessing, and are susceptible to ambient noise. To
overcome these limitations, we propose a lightweight, multimodal system for
queen detection based on environmental sensor fusion-specifically, temperature,
humidity, and pressure differentials between the inside and outside of the
hive. Our approach employs quantized decision tree inference on a commercial
STM32 microcontroller, enabling real-time, low-power edge computing without
compromising accuracy. We show that our system achieves over 99% queen
detection accuracy using only environmental inputs, with audio features
offering no significant performance gain. This work presents a scalable and
sustainable solution for non-invasive hive monitoring, paving the way for
autonomous, precision beekeeping using off-the-shelf, energy-efficient
hardware.

## 🔍 Abstract (한글 번역)

여왕벌의 존재는 꿀벌 군집의 건강과 안정성에 필수적이지만, 현재의 모니터링 방법은 노동 집약적이고 방해가 되며 대규모 양봉에는 비현실적인 수작업 검사를 기반으로 하고 있습니다. 최근의 오디오 기반 접근법은 가능성을 보여주었지만, 종종 높은 전력 소비, 복잡한 전처리 과정을 필요로 하며 주변 소음에 취약합니다. 이러한 한계를 극복하기 위해, 우리는 환경 센서 융합, 즉 벌통 내부와 외부의 온도, 습도, 압력 차이를 기반으로 한 경량의 다중 모드 여왕 탐지 시스템을 제안합니다. 우리의 접근법은 상용 STM32 마이크로컨트롤러에서 양자화된 결정 트리 추론을 사용하여 정확성을 손상시키지 않으면서 실시간 저전력 엣지 컴퓨팅을 가능하게 합니다. 우리는 오직 환경 입력만을 사용하여 99% 이상의 여왕 탐지 정확도를 달성했으며, 오디오 특징은 성능 향상에 유의미한 기여를 하지 않음을 보여줍니다. 이 연구는 비침습적 벌통 모니터링을 위한 확장 가능하고 지속 가능한 솔루션을 제시하며, 상용화된 에너지 효율적인 하드웨어를 사용한 자율적이고 정밀한 양봉의 길을 열어줍니다.

## 📝 요약

이 연구는 꿀벌 군집의 여왕벌 존재 여부를 감지하기 위한 경량의 다중 모달 시스템을 제안합니다. 기존의 수동 검사 방식은 노동 집약적이고 비효율적이며, 최근의 오디오 기반 접근법은 높은 전력 소모와 주변 소음에 취약한 문제를 가지고 있습니다. 이를 해결하기 위해, 본 연구는 환경 센서 융합을 통해 온도, 습도, 압력 차이를 활용하여 여왕벌을 감지합니다. 상용 STM32 마이크로컨트롤러에서 양자화된 결정 트리 추론을 사용하여 실시간 저전력 엣지 컴퓨팅을 구현하며, 99% 이상의 정확도를 달성했습니다. 이는 대규모 양봉에 적합한 비침습적 모니터링 솔루션을 제공하며, 에너지 효율적인 하드웨어를 통한 자율적이고 정밀한 양봉의 가능성을 열어줍니다.

## 🎯 주요 포인트

- 1. 여왕벌 존재 여부는 꿀벌 군집의 건강과 안정성에 필수적이지만, 현재의 모니터링 방법은 수작업 검사에 의존하여 대규모 양봉에는 비효율적입니다.

- 2. 기존의 오디오 기반 접근법은 유망하지만 높은 전력 소모, 복잡한 전처리, 주변 소음에 취약하다는 한계가 있습니다.

- 3. 우리는 환경 센서 융합을 기반으로 한 경량의 다중 모드 시스템을 제안하여, 실시간 저전력 엣지 컴퓨팅을 가능하게 합니다.

- 4. 제안된 시스템은 상업용 STM32 마이크로컨트롤러에서 양자화된 의사결정 트리 추론을 사용하여 99% 이상의 여왕벌 탐지 정확도를 달성합니다.

- 5. 이 연구는 비침습적 벌통 모니터링을 위한 확장 가능하고 지속 가능한 솔루션을 제시하며, 에너지 효율적인 하드웨어를 활용한 자율적 정밀 양봉의 길을 열어줍니다.

---

*Generated on 2025-09-20 07:52:00*