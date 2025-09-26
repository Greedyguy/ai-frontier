---
keywords:
  - Transformer Architecture
  - Large Language Models
  - Computer Vision
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13352
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:40:31.990122",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer Architecture",
    "Large Language Models",
    "Computer Vision"
  ],
  "rejected_keywords": [
    "Agentic UAVs"
  ],
  "similarity_scores": {
    "Transformer Architecture": 0.82,
    "Large Language Models": 0.8,
    "Computer Vision": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Agentic UAVs: LLM-Driven Autonomy with Integrated Tool-Calling and Cognitive Reasoning

**Korean Title:** 에이전틱 무인항공기: 통합된 도구 호출과 인지적 추론을 통한 대규모 언어모델 기반 자율성

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Computer Vision|YOLOv11 object detection]]
**🔗 Specific Connectable**: [[keywords/Transformer Architecture|GPT-4 reasoning]], [[keywords/Large Language Models|Large Language Model agents]]

## 🔗 유사한 논문
- [[Reinforcement_Learning_for_Autonomous_Point-to-Point_UAV_Navigation_20250918|Reinforcement Learning for Autonomous Point-to-Point UAV Navigation]] (82.9% similar)
- [[SPAR Scalable LLM-based PDDL Domain Generation for Aerial Robotics]] (82.4% similar)
- [[ASTREA Introducing Agentic Intelligence for Orbital Thermal Autonomy]] (82.2% similar)
- [[Cooperative Target Detection with AUVs A Dual-Timescale Hierarchical MARDL Approach]] (81.9% similar)
- [[AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (81.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13352v1 Announce Type: new 
Abstract: Unmanned Aerial Vehicles (UAVs) are increasingly deployed in defense, surveillance, and disaster response, yet most systems remain confined to SAE Level 2--3 autonomy. Their reliance on rule-based control and narrow AI restricts adaptability in dynamic, uncertain missions. Existing UAV frameworks lack context-aware reasoning, autonomous decision-making, and ecosystem-level integration; critically, none leverage Large Language Model (LLM) agents with tool-calling for real-time knowledge access. This paper introduces the Agentic UAVs framework, a five-layer architecture (Perception, Reasoning, Action, Integration, Learning) that augments UAVs with LLM-driven reasoning, database querying, and third-party system interaction. A ROS2 and Gazebo-based prototype integrates YOLOv11 object detection with GPT-4 reasoning and local Gemma-3 deployment. In simulated search-and-rescue scenarios, agentic UAVs achieved higher detection confidence (0.79 vs. 0.72), improved person detection rates (91% vs. 75%), and markedly increased action recommendation (92% vs. 4.5%). These results confirm that modest computational overhead enables qualitatively new levels of autonomy and ecosystem integration.

## 🔍 Abstract (한글 번역)

arXiv:2509.13352v1 발표 유형: 신규
초록: 무인항공기(UAV)는 국방, 감시, 재난 대응 분야에서 점점 더 많이 배치되고 있으나, 대부분의 시스템은 여전히 SAE 레벨 2-3 자율성에 국한되어 있다. 규칙 기반 제어와 협소한 AI에 대한 의존성은 동적이고 불확실한 임무에서의 적응성을 제한한다. 기존 UAV 프레임워크는 상황 인식 추론, 자율적 의사결정, 생태계 수준의 통합이 부족하며, 결정적으로 실시간 지식 접근을 위한 도구 호출(tool-calling)을 갖춘 대형언어모델(LLM) 에이전트를 활용하는 시스템은 존재하지 않는다. 본 논문은 5계층 아키텍처(인지, 추론, 행동, 통합, 학습)로 구성된 에이전틱 UAV 프레임워크를 소개하며, 이는 LLM 기반 추론, 데이터베이스 질의, 제3자 시스템 상호작용으로 UAV를 증강시킨다. ROS2와 Gazebo 기반 프로토타입은 YOLOv11 객체 탐지를 GPT-4 추론 및 로컬 Gemma-3 배치와 통합한다. 시뮬레이션된 수색-구조 시나리오에서 에이전틱 UAV는 더 높은 탐지 신뢰도(0.79 대 0.72), 향상된 인물 탐지율(91% 대 75%), 그리고 현저히 증가한 행동 추천율(92% 대 4.5%)을 달성하였다. 이러한 결과는 적은 계산 오버헤드로도 질적으로 새로운 수준의 자율성과 생태계 통합이 가능함을 확인해준다.

## 📝 요약

이 논문은 무인 항공기(UAV)의 자율성을 향상시키기 위해 제안된 Agentic UAVs 프레임워크를 소개합니다. 기존 UAV 시스템은 주로 규칙 기반 제어와 좁은 AI에 의존하여 동적이고 불확실한 임무에서의 적응력이 제한적입니다. 이를 해결하기 위해, 이 프레임워크는 대형 언어 모델(LLM) 기반의 추론, 데이터베이스 쿼리, 그리고 타 시스템과의 상호작용을 포함한 5계층 구조(지각, 추론, 행동, 통합, 학습)를 제안합니다. ROS2와 Gazebo를 기반으로 한 프로토타입은 YOLOv11 객체 탐지와 GPT-4 추론을 통합하여, 시뮬레이션된 수색 및 구조 시나리오에서 높은 탐지 신뢰도와 향상된 인물 탐지율을 보였습니다. 결과적으로, 적은 계산 비용으로도 UAV의 자율성과 생태계 통합 수준을 크게 향상시킬 수 있음을 확인했습니다.

## 🎯 주요 포인트

- 1. 무인 항공기(UAV)는 주로 SAE 레벨 2-3 자율성에 머물러 있으며, 규칙 기반 제어와 좁은 AI에 의존하여 동적이고 불확실한 임무에서의 적응성이 제한됩니다.

- 2. 기존 UAV 프레임워크는 상황 인식 추론, 자율적 의사 결정, 생태계 수준의 통합이 부족하며, 실시간 지식 접근을 위한 대형 언어 모델(LLM) 에이전트를 활용하지 않습니다.

- 3. 본 논문은 LLM 기반 추론, 데이터베이스 쿼리, 타사 시스템 상호작용을 통해 UAV의 자율성을 증대시키는 에이전틱 UAV 프레임워크를 소개합니다.

- 4. ROS2와 Gazebo 기반 프로토타입은 YOLOv11 객체 탐지와 GPT-4 추론을 통합하여, 시뮬레이션된 수색 및 구조 시나리오에서 높은 탐지 신뢰도와 개선된 인물 탐지율을 달성했습니다.

- 5. 에이전틱 UAV는 적은 계산 오버헤드로 새로운 수준의 자율성과 생태계 통합을 가능하게 함을 실험 결과로 확인했습니다.

---

*Generated on 2025-09-19 10:25:56*