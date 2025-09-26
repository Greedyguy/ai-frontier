---
keywords:
  - Machine Learning Models
  - Multi-Robot Systems
  - Source Localization
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:50:13.131476",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Machine Learning Models",
    "Multi-Robot Systems",
    "Source Localization"
  ],
  "rejected_keywords": [
    "Infotaxis"
  ],
  "similarity_scores": {
    "Machine Learning Models": 0.82,
    "Multi-Robot Systems": 0.8,
    "Source Localization": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Multi-robot Multi-source Localization in Complex Flows with Physics-Preserving Environment Models

**Korean Title:** 복잡한 흐름에서 물리 보존 환경 모델을 활용한 다중 로봇 다중 소스 위치 추정

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Machine Learning Models|machine-learned finite element model]]
**⚡ Unique Technical**: [[keywords/Multi-Robot Systems|multi-robot teams]], [[keywords/Source Localization|source localization]]

## 🔗 유사한 논문
- [[Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments_20250919|Semantic-LiDAR-Inertial-Wheel Odometry Fusion for Robust Localization in Large-Scale Dynamic Environments]] (81.3% similar)
- [[Multi-Quadruped Cooperative Object Transport_ Learning Decentralized Pinch-Lift-Move_20250919|Multi-Quadruped Cooperative Object Transport Learning Decentralized Pinch-Lift-Move]] (79.6% similar)
- [[Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion_20250919|Semantic Exploration and Dense Mapping of Complex Environments using Ground Robot with Panoramic LiDAR-Camera Fusion]] (79.2% similar)
- [[NavMoE_ Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts_20250918|NavMoE Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts]] (79.0% similar)
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (78.2% similar)

## 📋 저자 정보

**Authors:** Benjamin Shaffer, Victoria Edwards, Brooks Kinch, Nathaniel Trask, M. Ani Hsieh

## 📄 Abstract (원문)

Source localization in a complex flow poses a significant challenge for
multi-robot teams tasked with localizing the source of chemical leaks or
tracking the dispersion of an oil spill. The flow dynamics can be time-varying
and chaotic, resulting in sporadic and intermittent sensor readings, and
complex environmental geometries further complicate a team's ability to model
and predict the dispersion. To accurately account for the physical processes
that drive the dispersion dynamics, robots must have access to computationally
intensive numerical models, which can be difficult when onboard computation is
limited. We present a distributed mobile sensing framework for source
localization in which each robot carries a machine-learned, finite element
model of its environment to guide information-based sampling. The models are
used to evaluate an approximate mutual information criterion to drive an
infotaxis control strategy, which selects sensing regions that are expected to
maximize informativeness for the source localization objective. Our approach
achieves faster error reduction compared to baseline sensing strategies and
results in more accurate source localization compared to baseline machine
learning approaches.

## 🔍 Abstract (한글 번역)

복잡한 흐름에서의 출처 위치 추정은 화학 물질 누출의 출처를 찾거나 기름 유출의 확산을 추적하는 임무를 맡은 다중 로봇 팀에게 상당한 도전 과제를 제시합니다. 흐름 역학은 시간에 따라 변할 수 있고 혼란스러워서 센서 판독값이 산발적이고 간헐적으로 나타날 수 있으며, 복잡한 환경 지형은 팀이 확산을 모델링하고 예측하는 능력을 더욱 복잡하게 만듭니다. 확산 역학을 주도하는 물리적 과정을 정확하게 고려하기 위해, 로봇은 계산 집약적인 수치 모델에 접근할 수 있어야 하는데, 이는 온보드 계산이 제한될 때 어려울 수 있습니다. 우리는 출처 위치 추정을 위한 분산형 이동 감지 프레임워크를 제시하며, 각 로봇은 정보 기반 샘플링을 안내하기 위해 환경의 기계 학습된 유한 요소 모델을 탑재하고 있습니다. 이 모델들은 근사 상호 정보 기준을 평가하여 인포택시스 제어 전략을 구동하는 데 사용되며, 이는 출처 위치 추정 목표에 대해 정보성을 최대화할 것으로 예상되는 감지 영역을 선택합니다. 우리의 접근 방식은 기본 감지 전략에 비해 더 빠른 오류 감소를 달성하며, 기본 기계 학습 접근 방식에 비해 더 정확한 출처 위치 추정을 가능하게 합니다.

## 📝 요약

복잡한 유동 환경에서의 소스 위치 추적은 화학 물질 누출이나 기름 유출 확산을 추적하는 다중 로봇 팀에게 큰 도전 과제입니다. 이러한 환경에서는 유동 역학이 시간에 따라 변하고 혼란스러워 센서 데이터가 불규칙하게 수집되며, 복잡한 지형은 확산 모델링과 예측을 어렵게 만듭니다. 본 연구는 각 로봇이 환경의 유한 요소 모델을 기계 학습으로 탑재하여 정보 기반 샘플링을 유도하는 분산형 모바일 센싱 프레임워크를 제안합니다. 이 모델은 근사 상호 정보 기준을 평가하여 소스 위치 추적 목표에 가장 유익한 센싱 영역을 선택하는 인포택시스 제어 전략을 구동합니다. 제안된 방법은 기존의 센싱 전략보다 빠른 오류 감소와 더 정확한 소스 위치 추적을 달성합니다.

## 🎯 주요 포인트

- 1. 복잡한 흐름에서의 소스 위치 추적은 화학 누출이나 기름 유출 확산을 추적하는 다중 로봇 팀에게 큰 도전 과제입니다.

- 2. 로봇은 환경의 유한 요소 모델을 통해 정보 기반 샘플링을 안내받아야 하며, 이는 계산 집약적인 수치 모델을 필요로 합니다.

- 3. 제안된 분산형 모바일 센싱 프레임워크는 정보 택시스 제어 전략을 통해 정보성을 극대화할 수 있는 센싱 영역을 선택합니다.

- 4. 본 접근법은 기존의 센싱 전략에 비해 더 빠른 오류 감소를 달성하고, 기존의 기계 학습 방법에 비해 더 정확한 소스 위치 추적을 제공합니다.

---

*Generated on 2025-09-20 07:41:18*