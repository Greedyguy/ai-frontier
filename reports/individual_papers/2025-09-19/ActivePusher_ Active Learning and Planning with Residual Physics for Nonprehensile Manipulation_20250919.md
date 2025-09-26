---
keywords:
  - Uncertainty Quantification
  - Active Learning
  - Residual Physics
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2506.04646
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:58:03.105509",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Uncertainty Quantification",
    "Active Learning",
    "Residual Physics"
  ],
  "rejected_keywords": [
    "Kinodynamic Planning"
  ],
  "similarity_scores": {
    "Uncertainty Quantification": 0.82,
    "Active Learning": 0.8,
    "Residual Physics": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# ActivePusher: Active Learning and Planning with Residual Physics for Nonprehensile Manipulation

**Korean Title:** ActivePusher: 비접촉 조작을 위한 잔여 물리 기반의 능동 학습 및 계획

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Uncertainty Quantification|Uncertainty Quantification]], [[keywords/Active Learning|Active Learning]]
**⚡ Unique Technical**: [[keywords/Residual Physics|Residual Physics]]

## 🔗 유사한 논문
- [[Embracing Bulky Objects with Humanoid Robots Whole-Body Manipulation with Reinforcement Learning]] (83.2% similar)
- [[PhysicalAgent Towards General Cognitive Robotics with Foundation World Models]] (82.6% similar)
- [[Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles_20250918|Disturbance-Aware Dynamical Trajectory Planning for Air-Land Bimodal Vehicles]] (81.8% similar)
- [[One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields_20250918|One-Step Model Predictive Path Integral for Manipulator Motion Planning Using Configuration Space Distance Fields]] (81.8% similar)
- [[Meta-Optimization and Program Search using Language Models for Task and Motion Planning_20250918|Meta-Optimization and Program Search using Language Models for Task and Motion Planning]] (81.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.04646v2 Announce Type: replace-cross 
Abstract: Planning with learned dynamics models offers a promising approach toward versatile real-world manipulation, particularly in nonprehensile settings such as pushing or rolling, where accurate analytical models are difficult to obtain. However, collecting training data for learning-based methods can be costly and inefficient, as it often relies on randomly sampled interactions that are not necessarily the most informative. Furthermore, learned models tend to exhibit high uncertainty in underexplored regions of the skill space, undermining the reliability of long-horizon planning. To address these challenges, we propose ActivePusher, a novel framework that combines residual-physics modeling with uncertainty-based active learning, to focus data acquisition on the most informative skill parameters. Additionally, ActivePusher seamlessly integrates with model-based kinodynamic planners, leveraging uncertainty estimates to bias control sampling toward more reliable actions. We evaluate our approach in both simulation and real-world environments, and demonstrate that it consistently improves data efficiency and achieves higher planning success rates in comparison to baseline methods. The source code is available at https://github.com/elpis-lab/ActivePusher.

## 🔍 Abstract (한글 번역)

arXiv:2506.04646v2 발표 유형: 교차 교체  
초록: 학습된 동역학 모델을 활용한 계획은 특히 밀기나 구르기와 같은 비파지 설정에서 정확한 분석 모델을 얻기 어려운 실세계 조작에 대한 유망한 접근법을 제공합니다. 그러나 학습 기반 방법을 위한 훈련 데이터를 수집하는 것은 비용이 많이 들고 비효율적일 수 있으며, 이는 종종 가장 유익하지 않은 무작위로 샘플링된 상호작용에 의존하기 때문입니다. 게다가 학습된 모델은 기술 공간의 미탐색 영역에서 높은 불확실성을 나타내는 경향이 있어 장기 계획의 신뢰성을 저해합니다. 이러한 문제를 해결하기 위해, 우리는 잔여 물리 모델링과 불확실성 기반 능동 학습을 결합하여 가장 유익한 기술 매개변수에 데이터 수집을 집중시키는 새로운 프레임워크인 ActivePusher를 제안합니다. 또한, ActivePusher는 모델 기반 운동역학 계획자와 매끄럽게 통합되어 불확실성 추정을 활용하여 제어 샘플링을 보다 신뢰할 수 있는 행동으로 편향시킵니다. 우리는 시뮬레이션 및 실제 환경 모두에서 우리의 접근법을 평가하고, 그것이 데이터 효율성을 지속적으로 개선하고 기준 방법에 비해 더 높은 계획 성공률을 달성함을 입증합니다. 소스 코드는 https://github.com/elpis-lab/ActivePusher에서 제공됩니다.

## 📝 요약

이 논문은 비파지적 조작 환경에서 학습된 동적 모델을 활용한 계획 방법을 제안합니다. 특히, 푸시나 롤링과 같은 상황에서 정확한 분석 모델을 얻기 어려운 문제를 해결하고자 합니다. 기존 학습 기반 방법은 무작위로 샘플링된 상호작용에 의존해 비효율적이며, 미탐색 영역에서 높은 불확실성을 나타내어 장기 계획의 신뢰성을 저하시킵니다. 이를 해결하기 위해, 이 논문은 잔여 물리 모델링과 불확실성 기반의 능동 학습을 결합한 ActivePusher 프레임워크를 제안합니다. 이 방법은 가장 유익한 기술 매개변수에 집중하여 데이터 수집을 최적화하며, 모델 기반 운동역학 계획자와 통합되어 불확실성 추정치를 활용해 더 신뢰할 수 있는 행동을 선택합니다. 시뮬레이션 및 실제 환경에서 평가한 결과, ActivePusher는 데이터 효율성을 개선하고 계획 성공률을 높였습니다. 소스 코드는 https://github.com/elpis-lab/ActivePusher에서 제공됩니다.

## 🎯 주요 포인트

- 1. 학습된 동적 모델을 활용한 계획은 비파지적 조작 환경에서 유망한 접근법을 제공한다.

- 2. ActivePusher는 잔여 물리 모델링과 불확실성 기반의 능동 학습을 결합하여 가장 정보가 많은 기술 매개변수에 데이터 수집을 집중한다.

- 3. ActivePusher는 모델 기반의 운동 계획자와 통합되어 불확실성 추정을 활용하여 더 신뢰할 수 있는 행동으로 제어 샘플링을 편향시킨다.

- 4. 제안된 방법은 시뮬레이션과 실제 환경에서 데이터 효율성을 개선하고 계획 성공률을 높이는 것으로 나타났다.

- 5. ActivePusher의 소스 코드는 GitHub에서 제공된다.

---

*Generated on 2025-09-19 15:45:55*