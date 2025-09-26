---
keywords:
  - Reinforcement Learning
  - Multi-Modal Learning
  - Transfer Learning
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.11839
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:03:04.564009",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Multi-Modal Learning",
    "Transfer Learning"
  ],
  "rejected_keywords": [
    "Trajectory-Centric Learning",
    "Whole-Body Manipulation"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.82,
    "Multi-Modal Learning": 0.8,
    "Transfer Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning

**Korean Title:** TrajBooster: 궤적 중심 학습을 통해 인간형 전신 조작 강화

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]], [[keywords/Transfer Learning|Zero-Shot Skill Transfer]]
**🚀 Evolved Concepts**: [[keywords/Multi-Modal Learning|Vision-Language-Action models]]

## 🔗 유사한 논문
- [[Embracing_Bulky_Objects_with_Humanoid_Robots_Whole-Body_Manipulation_with_Reinforcement_Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (85.2% similar)
- [[Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations]] (83.1% similar)
- [[Humanoid_Agent_via_Embodied_Chain-of-Action_Reasoning_with_Multimodal_Foundation_Models_for_Zero-Shot_Loco-Manipulation_20250918|Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation]] (82.8% similar)
- [[textsc{Gen2Real}_Towards_Demo-Free_Dexterous_Manipulation_by_Harnessing_Generated_Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (82.8% similar)
- [[GeoAware-VLA_Implicit_Geometry_Aware_Vision-Language-Action_Model_20250918|GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model]] (82.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.11839v2 Announce Type: replace-cross 
Abstract: Recent Vision-Language-Action models show potential to generalize across embodiments but struggle to quickly align with a new robot's action space when high-quality demonstrations are scarce, especially for bipedal humanoids. We present TrajBooster, a cross-embodiment framework that leverages abundant wheeled-humanoid data to boost bipedal VLA. Our key idea is to use end-effector trajectories as a morphology-agnostic interface. TrajBooster (i) extracts 6D dual-arm end-effector trajectories from real-world wheeled humanoids, (ii) retargets them in simulation to Unitree G1 with a whole-body controller trained via a heuristic-enhanced harmonized online DAgger to lift low-dimensional trajectory references into feasible high-dimensional whole-body actions, and (iii) forms heterogeneous triplets that couple source vision/language with target humanoid-compatible actions to post-pre-train a VLA, followed by only 10 minutes of teleoperation data collection on the target humanoid domain. Deployed on Unitree G1, our policy achieves beyond-tabletop household tasks, enabling squatting, cross-height manipulation, and coordinated whole-body motion with markedly improved robustness and generalization. Results show that TrajBooster allows existing wheeled-humanoid data to efficiently strengthen bipedal humanoid VLA performance, reducing reliance on costly same-embodiment data while enhancing action space understanding and zero-shot skill transfer capabilities. For more details, For more details, please refer to our \href{https://jiachengliu3.github.io/TrajBooster/}.

## 🔍 Abstract (한글 번역)

arXiv:2509.11839v2 발표 유형: replace-cross
초록: 최근의 Vision-Language-Action 모델은 다양한 실체에 대해 일반화의 잠재력을 보여주지만, 고품질의 데모가 부족한 경우 특히 양다리 휴머노이드에 대해 새로운 로봇의 행동 공간과 빠르게 정렬하는 데 어려움을 겪습니다. 우리는 TrajBooster를 제시합니다. 이는 휠-휴머노이드 데이터를 활용하여 양다리 VLA를 강화하는 교차 실체 프레임워크입니다. 우리의 주요 아이디어는 엔드-이펙터 궤적을 형태에 무관한 인터페이스로 사용하는 것입니다. TrajBooster는 (i) 실제 세계의 휠-휴머노이드로부터 6D 듀얼 암 엔드-이펙터 궤적을 추출하고, (ii) 휴리스틱이 향상된 조화롭고 온라인 DAgger를 통해 훈련된 전신 컨트롤러를 사용하여 Unitree G1로 시뮬레이션에서 다시 지정하여 낮은 차원의 궤적 참조를 실행 가능한 고차원의 전신 행동으로 변환하고, (iii) 소스 비전/언어를 대상 휴머노이드 호환 행동과 결합시킨 이질적인 삼쌍을 형성하여 VLA를 사전-사후 훈련하고, 대상 휴머노이드 도메인에서 단 10분의 원격 조작 데이터 수집을 통해 결과를 달성합니다. Unitree G1에 배치된 우리의 정책은 탁자 이상의 가정 업무를 수행하며, 스쿼팅, 교차 높이 조작 및 협조하는 전신 동작을 가능하게 하며, 현저히 향상된 견고성과 일반화를 보여줍니다. 결과는 TrajBooster가 기존의 휠-휴머노이드 데이터를 효율적으로 강화하여 양다리 휴머노이드 VLA 성능을 향상시키고, 비용이 많이 드는 동일 실체 데이터에 대한 의존을 줄이면서 행동 공간 이해와 제로샷 기술 전이 능력을 향상시킨다는 것을 보여줍니다. 더 자세한 내용은 저희의 \href{https://jiachengliu3.github.io/TrajBooster/}를 참조해주십시오.

## 📝 요약

최근의 Vision-Language-Action 모델은 다양한 신체 구조에 대해 일반화할 수 있는 잠재력을 보여주지만, 고품질 데모가 부족한 경우 새로운 로봇의 행동 공간과 빠르게 정렬하는 데 어려움을 겪습니다. 본 연구에서는 TrajBooster를 제안하여 바퀴 달린 로봇 데이터를 활용하여 양다리 인간형 로봇의 성능을 향상시킵니다. 우리의 주요 아이디어는 엔드 이펙터 궤적을 형태에 구애받지 않는 인터페이스로 사용하는 것입니다. TrajBooster는 실제 세계의 바퀴 달린 로봇에서 6D 이중 팔 엔드 이펙터 궤적을 추출하고, 시뮬레이션에서 Unitree G1로 재지정하여 저차원 궤적 참조를 고차원 전신 동작으로 변환하는 휴리스틱 향상된 조화 온라인 DAgger를 통해 훈련된 전신 컨트롤러를 사용합니다. 결과적으로 TrajBooster는 바퀴 달린 로봇 데이터를 활용하여 양다리 인간형 로봇의 VLA 성능을 효율적으로 강화시키며, 고가의 동일 신체 데이터에 대한 의존성을 줄이고 행동 공간 이해력 및 제로샷 기술 전이 능력을 향상시킵니다.

## 🎯 주요 포인트

- 1. TrajBooster는 다리가 두 개인 인간형 로봇의 성능을 향상시키는 데 효과적인 방법을 제시한다.

- 2. 이 프레임워크는 휠-인간형 데이터를 활용하여 새로운 로봇의 행동 공간에 빠르게 적응할 수 있도록 도와준다.

- 3. TrajBooster는 휠-인간형 데이터를 활용하여 다리가 두 개인 로봇의 시각-언어-행동 모델의 성능을 강화시키는데 도움을 준다.

---

*Generated on 2025-09-18 17:08:32*