---
keywords:
  - Foundation Models
  - Weighted Traveling Repairman Problem
  - Zero-Shot Object Navigation
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2503.06937
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:40:54.900132",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Foundation Models",
    "Weighted Traveling Repairman Problem",
    "Zero-Shot Object Navigation"
  ],
  "rejected_keywords": [
    "Vision-Language Model"
  ],
  "similarity_scores": {
    "Foundation Models": 0.8,
    "Weighted Traveling Repairman Problem": 0.79,
    "Zero-Shot Object Navigation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Handle Object Navigation as Weighted Traveling Repairman Problem

**Korean Title:** 객체 내비게이션을 가중치가 부여된 여행 수리공 문제로 처리하기

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Weighted Traveling Repairman Problem|Weighted Traveling Repairman Problem]], [[keywords/Zero-Shot Object Navigation|Zero-Shot Object Navigation]]
**🚀 Evolved Concepts**: [[keywords/Foundation Models|Foundation Models]]

## 🔗 유사한 논문
- [[Search-TTA A Multimodal Test-Time Adaptation Framework for Visual Search in the Wild]] (82.4% similar)
- [[FSR-VLN Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph]] (82.1% similar)
- [[Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (80.6% similar)
- [[Embodied Navigation Foundation Model_20250918|Embodied Navigation Foundation Model]] (79.7% similar)
- [[VSE-MOT Multi-Object Tracking in Low-Quality Video Scenes Guided by Visual Semantic Enhancement]] (79.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.06937v2 Announce Type: replace 
Abstract: Zero-Shot Object Navigation (ZSON) requires agents to navigate to objects specified via open-ended natural language without predefined categories or prior environmental knowledge. While recent methods leverage foundation models or multi-modal maps, they often rely on 2D representations and greedy strategies or require additional training or modules with high computation load, limiting performance in complex environments and real applications. We propose WTRP-Searcher, a novel framework that formulates ZSON as a Weighted Traveling Repairman Problem (WTRP), minimizing the weighted waiting time of viewpoints. Using a Vision-Language Model (VLM), we score viewpoints based on object-description similarity, projected onto a 2D map with depth information. An open-vocabulary detector identifies targets, dynamically updating goals, while a 3D embedding feature map enhances spatial awareness and environmental recall. WTRP-Searcher outperforms existing methods, offering efficient global planning and improved performance in complex ZSON tasks. Code and design will be open-sourced upon acceptance.

## 🔍 Abstract (한글 번역)

arXiv:2503.06937v2 발표 유형: 교체  
초록: Zero-Shot Object Navigation (ZSON)은 사전 정의된 카테고리나 환경에 대한 사전 지식 없이 개방형 자연어로 지정된 객체로 에이전트가 이동하도록 요구합니다. 최근 방법들은 기초 모델이나 다중 모달 맵을 활용하지만, 종종 2D 표현과 탐욕적 전략에 의존하거나 높은 계산 부하를 가진 추가 훈련이나 모듈을 필요로 하여 복잡한 환경과 실제 응용에서 성능을 제한합니다. 우리는 ZSON을 가중 여행 수리공 문제(Weighted Traveling Repairman Problem, WTRP)로 공식화하여 관점의 가중 대기 시간을 최소화하는 새로운 프레임워크인 WTRP-Searcher를 제안합니다. 비전-언어 모델(Vision-Language Model, VLM)을 사용하여 객체 설명 유사성에 기반한 관점을 점수화하고, 깊이 정보를 포함한 2D 맵에 투영합니다. 개방형 어휘 탐지기가 목표를 식별하고 동적으로 업데이트하며, 3D 임베딩 특징 맵이 공간 인식과 환경 기억을 향상시킵니다. WTRP-Searcher는 기존 방법을 능가하며, 복잡한 ZSON 작업에서 효율적인 글로벌 계획과 향상된 성능을 제공합니다. 코드와 설계는 승인 시 오픈 소스로 공개될 예정입니다.

## 📝 요약

Zero-Shot Object Navigation (ZSON)은 사전 정의된 카테고리나 환경 지식 없이 자연어로 지정된 객체로의 탐색을 요구합니다. 기존 방법들은 2D 표현과 높은 계산 부하가 있는 추가 모듈에 의존하여 복잡한 환경에서의 성능이 제한됩니다. 우리는 ZSON을 가중치 이동 수리공 문제(WTRP)로 공식화한 WTRP-Searcher를 제안합니다. Vision-Language Model(VLM)을 사용하여 객체 설명 유사성을 기반으로 관점의 점수를 매기고, 깊이 정보를 포함한 2D 지도에 투영합니다. 개방형 어휘 탐지기가 목표를 동적으로 업데이트하며, 3D 임베딩 기능 지도가 공간 인식과 환경 회상을 강화합니다. WTRP-Searcher는 효율적인 글로벌 계획과 향상된 성능을 제공하며, 코드와 설계는 승인 시 공개될 예정입니다.

## 🎯 주요 포인트

- 1. Zero-Shot Object Navigation(ZSON)은 사전 정의된 카테고리나 환경 지식 없이 자연어로 지정된 객체로의 탐색을 요구합니다.

- 2. 기존 방법들은 2D 표현과 탐욕적 전략에 의존하거나 추가적인 훈련과 높은 계산 부하를 필요로 하여 복잡한 환경에서의 성능이 제한됩니다.

- 3. WTRP-Searcher는 ZSON을 가중치 대기 시간 최소화 문제로 공식화하여 효율적인 글로벌 계획을 제공합니다.

- 4. Vision-Language Model(VLM)을 사용하여 객체 설명 유사성에 기반한 관점 점수를 매기고, 2D 지도에 깊이 정보를 투영합니다.

- 5. WTRP-Searcher는 기존 방법보다 복잡한 ZSON 작업에서 향상된 성능을 보이며, 코드는 승인 시 공개될 예정입니다.

---

*Generated on 2025-09-19 16:37:57*