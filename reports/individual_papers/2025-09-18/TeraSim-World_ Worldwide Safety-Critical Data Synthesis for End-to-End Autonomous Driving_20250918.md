---
keywords:
  - End-to-End Autonomous Driving
  - Safety-Critical Data Synthesis
  - Sim-to-Real Gap
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13164
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:05:48.427165",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "End-to-End Autonomous Driving",
    "Safety-Critical Data Synthesis",
    "Sim-to-Real Gap"
  ],
  "rejected_keywords": [
    "Geospatial Data"
  ],
  "similarity_scores": {
    "End-to-End Autonomous Driving": 0.8,
    "Safety-Critical Data Synthesis": 0.78,
    "Sim-to-Real Gap": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# TeraSim-World: Worldwide Safety-Critical Data Synthesis for End-to-End Autonomous Driving

**Korean Title:** 테라심-월드: 자율 주행을 위한 종단 간 안전 중요 데이터 합성을 위한 세계적인 시뮬레이션

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Sim-to-Real Gap|sim-to-real gap]]
**⚡ Unique Technical**: [[keywords/End-to-End Autonomous Driving|end-to-end autonomous driving]], [[keywords/Safety-Critical Data Synthesis|safety-critical data synthesis]]

## 🔗 유사한 논문
- [[MAP: End-to-End Autonomous Driving with Map-Assisted Planning]] (81.6% similar)
- [[FlightDiffusion_Revolutionising_Autonomous_Drone_Training_with_Diffusion_Models_Generating_FPV_Video_20250918|FlightDiffusion: Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (79.2% similar)
- [[Mining the Long Tail: A Comparative Study of Data-Centric Criticality Metrics for Robust Offline Reinforcement Learning in Autonomous Motion Planning]] (79.1% similar)
- [[Search-TTA: A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild]] (78.6% similar)
- [[DECAMP: Towards Scene-Consistent Multi-Agent Motion Prediction with Disentangled Context-Aware Pre-Training]] (77.6% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13164v2 Announce Type: replace 
Abstract: Safe and scalable deployment of end-to-end (E2E) autonomous driving requires extensive and diverse data, particularly safety-critical events. Existing data are mostly generated from simulators with a significant sim-to-real gap or collected from on-road testing that is costly and unsafe. This paper presents TeraSim-World, an automated pipeline that synthesizes realistic and geographically diverse safety-critical data for E2E autonomous driving at anywhere in the world. Starting from an arbitrary location, TeraSim-World retrieves real-world maps and traffic demand from geospatial data sources. Then, it simulates agent behaviors from naturalistic driving datasets, and orchestrates diverse adversities to create corner cases. Informed by street views of the same location, it achieves photorealistic, geographically grounded sensor rendering via the frontier video generation model Cosmos-Drive. By bridging agent and sensor simulations, TeraSim-World provides a scalable and critical data synthesis framework for training and evaluation of E2E autonomous driving systems. Codes and videos are available at https://wjiawei.com/terasim-world-web/ .

## 🔍 Abstract (한글 번역)

arXiv:2509.13164v2 발표 유형: 대체
초록: 엔드 투 엔드(E2E) 자율 주행의 안전하고 확장 가능한 배포를 위해서는 특히 안전 중요 이벤트를 포함한 광범위하고 다양한 데이터가 필요합니다. 기존 데이터는 대부분 시뮬레이터에서 생성되어 있으며 현실과의 큰 차이가 있는 것이 일반적이거나 비용이 많이 들고 안전하지 않은 도로 테스트에서 수집되었습니다. 본 논문에서는 TeraSim-World를 제시합니다. 이는 세계 어디에서든 E2E 자율 주행을 위한 현실적이고 지리적으로 다양한 안전 중요 데이터를 자동으로 합성하는 파이프라인입니다. 임의의 위치에서 시작하여 TeraSim-World는 지리 데이터 소스로부터 실제 지도와 교통 수요를 검색합니다. 그런 다음 자연주의 운전 데이터셋에서 에이전트 행동을 시뮬레이션하고 다양한 역경을 조합하여 극단적인 상황을 만듭니다. 동일한 위치의 거리뷰를 기반으로 하여 Cosmos-Drive 모델을 통해 포토리얼리스틱하고 지리적으로 근거있는 센서 렌더링을 달성합니다. 에이전트 및 센서 시뮬레이션을 연결함으로써 TeraSim-World는 E2E 자율 주행 시스템의 교육 및 평가를 위한 확장 가능하고 중요한 데이터 합성 프레임워크를 제공합니다. 코드 및 비디오는 https://wjiawei.com/terasim-world-web/에서 이용할 수 있습니다.

## 📝 요약

자율 주행의 안전하고 확장 가능한 배포를 위해서는 다양하고 광범위한 데이터가 필요합니다. 기존 데이터는 주로 시뮬레이터에서 생성되거나 비용이 많이 들고 위험한 도로 테스트에서 수집됩니다. 본 논문은 TeraSim-World를 제안합니다. 이는 세계 어디에서나 자율 주행을 위한 현실적이고 지리적으로 다양한 안전 중요 데이터를 자동으로 합성하는 파이프라인입니다. TeraSim-World는 실제 지도와 교통 수요를 가져와 에이전트 행동을 시뮬레이션하고 다양한 어려움을 조합하여 모험적인 상황을 만듭니다. 에이전트와 센서 시뮬레이션을 연결함으로써 자율 주행 시스템의 교육과 평가를 위한 확장 가능하고 중요한 데이터 합성 프레임워크를 제공합니다.

## 🎯 주요 포인트

- 1. 자율 주행의 안전하고 확장 가능한 배포를 위해 다양하고 안전한 데이터가 필요하다.

- 2. TeraSim-World는 실제적이고 지리적으로 다양한 안전 중요 데이터를 자동으로 합성한다.

- 3. Cosmos-Drive를 통해 지리적으로 기반된 센서 렌더링을 달성하여 자율 주행 시스템의 훈련과 평가를 위한 확장 가능한 데이터 합성 프레임워크를 제공한다.

---

*Generated on 2025-09-18 17:22:03*