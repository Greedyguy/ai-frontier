---
keywords:
  - Reinforcement Learning
  - Contact-Rich Industrial Assembly
  - Human Demonstrations
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.13949
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:11:50.494325",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Contact-Rich Industrial Assembly",
    "Human Demonstrations"
  ],
  "rejected_keywords": [
    "Manipulation Primitives"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.88,
    "Contact-Rich Industrial Assembly": 0.7,
    "Human Demonstrations": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# SHaRe-RL: Structured, Interactive Reinforcement Learning for Contact-Rich Industrial Assembly Tasks

**Korean Title:** SHaRe-RL: 접촉이 많은 산업 조립 작업을 위한 구조화된 대화형 강화 학습

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Contact-Rich Industrial Assembly|Contact-Rich Industrial Assembly]]
**🚀 Evolved Concepts**: [[keywords/Human Demonstrations|Human Demonstrations]]

## 🔗 유사한 논문
- [[Reinforcement_Learning_for_Robotic_Insertion_of_Flexible_Cables_in_Industrial_Settings_20250918|Reinforcement Learning for Robotic Insertion of Flexible Cables in Industrial Settings]] (85.8% similar)
- [[Reinforcement_Learning_for_Autonomous_Point-to-Point_UAV_Navigation_20250918|Reinforcement Learning for Autonomous Point-to-Point UAV Navigation]] (79.5% similar)
- [[MIMIC-D: Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (78.6% similar)
- [[Embracing_Bulky_Objects_with_Humanoid_Robots_Whole-Body_Manipulation_with_Reinforcement_Learning_20250918|Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning]] (78.6% similar)
- [[textsc{Gen2Real}_Towards_Demo-Free_Dexterous_Manipulation_by_Harnessing_Generated_Video_20250918|\textsc{Gen2Real}: Towards Demo-Free Dexterous Manipulation by Harnessing Generated Video]] (78.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13949v1 Announce Type: new 
Abstract: High-mix low-volume (HMLV) industrial assembly, common in small and medium-sized enterprises (SMEs), requires the same precision, safety, and reliability as high-volume automation while remaining flexible to product variation and environmental uncertainty. Current robotic systems struggle to meet these demands. Manual programming is brittle and costly to adapt, while learning-based methods suffer from poor sample efficiency and unsafe exploration in contact-rich tasks. To address this, we present SHaRe-RL, a reinforcement learning framework that leverages multiple sources of prior knowledge. By (i) structuring skills into manipulation primitives, (ii) incorporating human demonstrations and online corrections, and (iii) bounding interaction forces with per-axis compliance, SHaRe-RL enables efficient and safe online learning for long-horizon, contact-rich industrial assembly tasks. Experiments on the insertion of industrial Harting connector modules with 0.2-0.4 mm clearance demonstrate that SHaRe-RL achieves reliable performance within practical time budgets. Our results show that process expertise, without requiring robotics or RL knowledge, can meaningfully contribute to learning, enabling safer, more robust, and more economically viable deployment of RL for industrial assembly.

## 🔍 Abstract (한글 번역)

arXiv:2509.13949v1 발표 유형: 새로운
요약: 소규모 및 중소기업(SMEs)에서 흔히 볼 수 있는 고믹스 저볼륨(HMLV) 산업 조립은 고볼륨 자동화와 동일한 정밀성, 안전성 및 신뢰성을 요구하면서 제품 변이와 환경 불확실성에 유연하게 대응해야 합니다. 현재의 로봇 시스템은 이러한 요구를 충족시키기 어렵습니다. 수동 프로그래밍은 취약하고 적응하기 어렵지만, 학습 기반 방법은 샘플 효율성이 낮고 접촉이 많은 작업에서 안전하지 못한 탐색을 겪습니다. 이를 해결하기 위해 우리는 SHaRe-RL이라는 강화 학습 프레임워크를 제시합니다. 이는 다양한 이전 지식 소스를 활용합니다. (i) 기술을 조작 기본 요소로 구조화하고, (ii) 인간의 시연과 온라인 수정을 통합하며, (iii) 축당순응력을 통해 상호 작용 힘을 제한함으로써 SHaRe-RL은 장기간, 접촉이 많은 산업 조립 작업에 대한 효율적이고 안전한 온라인 학습을 가능하게 합니다. 0.2-0.4mm 여유 공간을 가진 산업용 하팅 커넥터 모듈 삽입 실험은 SHaRe-RL이 실용적인 시간 예산 내에서 안정적인 성능을 달성한다는 것을 보여줍니다. 우리의 결과는 공정 전문 지식이 로봇학이나 강화 학습 지식을 요구하지 않으면서도 학습에 의미 있는 기여를 할 수 있음을 보여주며, 산업 조립을 위한 강화 학습의 더 안전하고 견고하며 경제적으로 실현 가능한 배치를 가능하게 합니다.

## 📝 요약

고민과 중소기업(SMEs)에서 흔한 고민 저량(HMLV) 산업 조립은 높은 정밀도, 안전성 및 신뢰성을 요구하지만 제품 변이와 환경 불확실성에 대응할 수 있어야 합니다. 현재 로봇 시스템은 이러한 요구를 충족하기 어렵습니다. 이에 우리는 SHaRe-RL이라는 강화 학습 프레임워크를 제안하여 여러 소스의 사전 지식을 활용합니다. 이를 통해 장기간, 접촉이 많은 산업 조립 작업에 대한 효율적이고 안전한 온라인 학습이 가능해졌습니다. 실험 결과는 SHaRe-RL이 실용적인 시간 예산 내에서 신뢰할 수 있는 성능을 달성한다는 것을 보여주었습니다. 이러한 결과는 공정 전문 지식이 로봇학이나 강화 학습 지식이 필요하지 않고도 학습에 의미 있는 기여를 할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 고혼합 저양산 산업 조립 작업에서 안전하고 신뢰성 높은 로봇 시스템 개발 필요

- SHaRe-RL은 다양한 이전 지식을 활용한 강화 학습 프레임워크로 안전하고 효율적인 온라인 학습 가능

- 산업 조립 작업에서 SHaRe-RL은 안정적인 성능을 보이며 경제적인 시간 내에 신뢰성 있는 결과 달성 가능

---

*Generated on 2025-09-18 17:16:14*