---
keywords:
  - Foundation Models
  - Embodied Chain-of-Action
  - Humanoid Loco-Manipulation
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2504.09532
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:26:04.413926",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Foundation Models",
    "Embodied Chain-of-Action",
    "Humanoid Loco-Manipulation"
  ],
  "rejected_keywords": [
    "Affordance Analysis"
  ],
  "similarity_scores": {
    "Foundation Models": 0.8,
    "Embodied Chain-of-Action": 0.82,
    "Humanoid Loco-Manipulation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation

**Korean Title:** 제로샷 이동-조작을 위한 다중모달 기반 모델을 활용한 체화된 행동 연쇄 추론 기반 휴머노이드 에이전트

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Embodied Chain-of-Action|Embodied Chain-of-Action]], [[keywords/Humanoid Loco-Manipulation|Humanoid loco-manipulation]]
**🚀 Evolved Concepts**: [[keywords/Foundation Models|Foundation Models]]

## 🔗 유사한 논문
- [[PhysicalAgent Towards General Cognitive Robotics with Foundation World Models]] (85.3% similar)
- [[OpenHA A Series of Open-Source Hierarchical Agentic Models in Minecraft]] (83.8% similar)
- [[TrajBooster Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (82.8% similar)
- [[Embracing Bulky Objects with Humanoid Robots Whole-Body Manipulation with Reinforcement Learning]] (82.4% similar)
- [[Meta-Optimization_and_Program_Search_using_Language_Models_for_Task_and_Motion_Planning_20250918|Meta-Optimization and Program Search using Language Models for Task and Motion Planning]] (81.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.09532v2 Announce Type: replace-cross 
Abstract: Humanoid loco-manipulation, which integrates whole-body locomotion with dexterous manipulation, remains a fundamental challenge in robotics. Beyond whole-body coordination and balance, a central difficulty lies in understanding human instructions and translating them into coherent sequences of embodied actions. Recent advances in foundation models provide transferable multimodal representations and reasoning capabilities, yet existing efforts remain largely restricted to either locomotion or manipulation in isolation, with limited applicability to humanoid settings. In this paper, we propose Humanoid-COA, the first humanoid agent framework that integrates foundation model reasoning with an Embodied Chain-of-Action (CoA) mechanism for zero-shot loco-manipulation. Within the perception--reasoning--action paradigm, our key contribution lies in the reasoning stage, where the proposed CoA mechanism decomposes high-level human instructions into structured sequences of locomotion and manipulation primitives through affordance analysis, spatial inference, and whole-body action reasoning. Extensive experiments on two humanoid robots, Unitree H1-2 and G1, in both an open test area and an apartment environment, demonstrate that our framework substantially outperforms prior baselines across manipulation, locomotion, and loco-manipulation tasks, achieving robust generalization to long-horizon and unstructured scenarios. Project page: https://humanoid-coa.github.io/

## 🔍 Abstract (한글 번역)

arXiv:2504.09532v2 공지 유형: replace-cross 
초록: 전신 이동과 정교한 조작을 통합하는 휴머노이드 이동-조작(loco-manipulation)은 로봇공학의 근본적인 도전 과제로 남아있다. 전신 협응과 균형을 넘어서, 핵심적인 어려움은 인간의 지시를 이해하고 이를 일관된 체화된 행동 시퀀스로 변환하는 데 있다. 파운데이션 모델의 최근 발전은 전이 가능한 다중모달 표현과 추론 능력을 제공하지만, 기존의 노력들은 주로 이동 또는 조작을 개별적으로 다루는 데 제한되어 있으며, 휴머노이드 환경에서의 적용성이 제한적이다. 본 논문에서는 제로샷 이동-조작을 위해 파운데이션 모델 추론과 체화된 연쇄 행동(Chain-of-Action, CoA) 메커니즘을 통합한 최초의 휴머노이드 에이전트 프레임워크인 Humanoid-COA를 제안한다. 지각-추론-행동 패러다임 내에서, 우리의 핵심 기여는 추론 단계에 있으며, 여기서 제안된 CoA 메커니즘은 어포던스 분석, 공간 추론, 그리고 전신 행동 추론을 통해 상위 수준의 인간 지시를 이동 및 조작 프리미티브의 구조화된 시퀀스로 분해한다. 개방된 테스트 구역과 아파트 환경에서 두 개의 휴머노이드 로봇인 Unitree H1-2와 G1을 대상으로 한 광범위한 실험을 통해, 우리의 프레임워크가 조작, 이동, 그리고 이동-조작 작업에서 기존 베이스라인을 상당히 능가하며, 장기간 및 비구조화된 시나리오에 대한 강건한 일반화를 달성함을 보여준다. 프로젝트 페이지: https://humanoid-coa.github.io/

## 📝 요약

이 논문은 인간형 로봇의 전신 이동과 정교한 조작을 통합하는 "Humanoid-COA"라는 프레임워크를 제안합니다. 이 프레임워크는 기초 모델의 추론 능력과 Embodied Chain-of-Action(CoA) 메커니즘을 결합하여 인간의 지시를 구조화된 이동 및 조작 시퀀스로 변환합니다. 주요 기여는 지각-추론-행동 패러다임에서 추론 단계에 있으며, CoA 메커니즘을 통해 고수준의 인간 지시를 이동 및 조작 기본 요소로 분해합니다. 두 대의 인간형 로봇을 사용한 실험 결과, 이 프레임워크는 기존의 기준을 능가하며, 장기적이고 비구조화된 시나리오에서도 강력한 일반화 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 휴머노이드 로코-매니퓰레이션은 전신 이동과 정교한 조작을 통합하는 로봇 공학의 근본적인 도전 과제입니다.

- 2. Humanoid-COA는 기초 모델의 추론 능력을 Embodied Chain-of-Action 메커니즘과 통합하여 제로샷 로코-매니퓰레이션을 구현하는 최초의 휴머노이드 에이전트 프레임워크입니다.

- 3. 제안된 CoA 메커니즘은 인간의 고수준 지시를 이동 및 조작 프리미티브의 구조화된 시퀀스로 분해하여 추론 단계에서 중요한 기여를 합니다.

- 4. Unitree H1-2 및 G1 휴머노이드 로봇을 사용한 실험에서 제안된 프레임워크는 조작, 이동 및 로코-매니퓰레이션 작업에서 기존 기준을 크게 능가했습니다.

- 5. 이 프레임워크는 장기적이고 비구조적인 시나리오에 대한 강력한 일반화 성능을 보여줍니다.

---

*Generated on 2025-09-19 11:04:46*