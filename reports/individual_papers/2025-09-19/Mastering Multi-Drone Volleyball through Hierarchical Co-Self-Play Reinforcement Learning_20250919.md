
# Mastering Multi-Drone Volleyball through Hierarchical Co-Self-Play Reinforcement Learning

**Korean Title:** 다단계 자기 대결 강화 학습을 통한 다중 드론 배구 숙달

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multi-Agent Coordination

## 🔗 유사한 논문
- [[Reinforcement_Learning_Agent_for_a_2D_Shooter_Game_20250919|Reinforcement Learning Agent for a 2D Shooter Game]] (79.4% similar)
- [[Dual Actor DDPG for Airborne STAR-RIS Assisted Communications]] (78.7% similar)
- [[OpenHA A Series of Open-Source Hierarchical Agentic Models in Minecraft]] (78.5% similar)
- [[Hybrid_Diffusion_Policies_with_Projective_Geometric_Algebra_for_Efficient_Robot_Manipulation_Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (78.3% similar)
- [[Cooperative Target Detection with AUVs A Dual-Timescale Hierarchical MARDL Approach]] (78.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.04317v4 Announce Type: replace 
Abstract: In this paper, we tackle the problem of learning to play 3v3 multi-drone volleyball, a new embodied competitive task that requires both high-level strategic coordination and low-level agile control. The task is turn-based, multi-agent, and physically grounded, posing significant challenges due to its long-horizon dependencies, tight inter-agent coupling, and the underactuated dynamics of quadrotors. To address this, we propose Hierarchical Co-Self-Play (HCSP), a hierarchical reinforcement learning framework that separates centralized high-level strategic decision-making from decentralized low-level motion control. We design a three-stage population-based training pipeline to enable both strategy and skill to emerge from scratch without expert demonstrations: (I) training diverse low-level skills, (II) learning high-level strategy via self-play with fixed low-level skills, and (III) joint fine-tuning through co-self-play. Experiments show that HCSP achieves superior performance, outperforming non-hierarchical self-play and rule-based hierarchical baselines with an average 82.9% win rate and a 71.5% win rate against the two-stage variant. Moreover, co-self-play leads to emergent team behaviors such as role switching and coordinated formations, demonstrating the effectiveness of our hierarchical design and training scheme. The project page is at https://sites.google.com/view/hi-co-self-play.

## 🔍 Abstract (한글 번역)

arXiv:2505.04317v4 발표 유형: 교체  
초록: 본 논문에서는 고수준의 전략적 협력과 저수준의 민첩한 제어가 모두 필요한 새로운 구현형 경쟁 과제인 3v3 멀티 드론 배구를 학습하는 문제를 다룹니다. 이 과제는 턴 기반, 다중 에이전트, 물리적으로 기반을 두고 있으며, 긴 시간적 의존성, 에이전트 간의 긴밀한 결합, 쿼드로터의 비제어 동역학으로 인해 상당한 도전 과제를 제시합니다. 이를 해결하기 위해, 중앙 집중식 고수준 전략적 의사결정과 분산형 저수준 운동 제어를 분리하는 계층적 강화 학습 프레임워크인 Hierarchical Co-Self-Play (HCSP)를 제안합니다. 우리는 전문가 시연 없이 전략과 기술이 처음부터 나타날 수 있도록 하는 3단계 인구 기반 학습 파이프라인을 설계했습니다: (I) 다양한 저수준 기술 훈련, (II) 고정된 저수준 기술과의 자기 대전을 통한 고수준 전략 학습, (III) 공동 자기 대전을 통한 공동 미세 조정. 실험 결과, HCSP는 비계층적 자기 대전 및 규칙 기반 계층적 기준선을 능가하는 평균 82.9%의 승률과 2단계 변형에 대한 71.5%의 승률로 우수한 성능을 달성했습니다. 더욱이, 공동 자기 대전은 역할 전환 및 협력적 포메이션과 같은 팀 행동의 출현으로 이어져, 우리의 계층적 설계 및 학습 체계의 효과성을 입증합니다. 프로젝트 페이지는 https://sites.google.com/view/hi-co-self-play에 있습니다.

## 📝 요약

이 논문은 3대3 멀티 드론 배구 게임을 학습하는 문제를 다룹니다. 이 게임은 고도의 전략적 협력과 민첩한 제어를 요구하는 새로운 경쟁 과제입니다. 이를 해결하기 위해, 중앙집중식 고수준 전략 결정과 분산된 저수준 동작 제어를 분리한 계층적 강화 학습 프레임워크인 Hierarchical Co-Self-Play (HCSP)를 제안합니다. 세 단계의 인구 기반 훈련 파이프라인을 통해 전문가 시범 없이 전략과 기술을 학습합니다. 실험 결과, HCSP는 비계층적 자가 학습 및 규칙 기반 계층적 기준을 능가하며, 82.9%의 평균 승률을 기록했습니다. 또한, 공동 자가 학습은 역할 전환 및 협력적 포메이션과 같은 팀 행동을 유도하여, 계층적 설계와 훈련 방식의 효과를 입증했습니다.

## 🎯 주요 포인트

- 1. 3v3 멀티 드론 배구 문제를 해결하기 위해 계층적 강화 학습 프레임워크인 HCSP를 제안했습니다.

- 2. HCSP는 중앙집중식 고수준 전략적 의사결정과 분산형 저수준 운동 제어를 분리하여 학습합니다.

- 3. 세 단계의 인구 기반 훈련 파이프라인을 통해 전략과 기술이 전문가 시범 없이도 처음부터 학습됩니다.

- 4. 실험 결과, HCSP는 비계층적 자기 학습 및 규칙 기반 계층적 기준선을 능가하는 성능을 보였습니다.

- 5. 공동 자기 학습을 통해 역할 전환 및 협력적 포메이션과 같은 팀 행동이 나타났습니다.

---

*Generated on 2025-09-19 15:09:05*