# A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning

**Korean Title:** 로봇의 실제 환경 강화 학습을 위한 비전-언어-행동-비평가 모델

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Vision-Language-Action Models

## 🔗 유사한 논문
- [[2025-09-19/CollabVLA_ Self-Reflective Vision-Language-Action Model Dreaming Together with Human_20250919|CollabVLA Self-Reflective Vision-Language-Action Model Dreaming Together with Human]] (88.2% similar)
- [[2025-09-19/ThinkAct_ Vision-Language-Action Reasoning via Reinforced Visual Latent Planning_20250919|ThinkAct Vision-Language-Action Reasoning via Reinforced Visual Latent Planning]] (86.5% similar)
- [[2025-09-18/CLAW_ A Vision-Language-Action Framework for Weight-Aware Robotic Grasping_20250918|CLAW A Vision-Language-Action Framework for Weight-Aware Robotic Grasping]] (85.9% similar)
- [[2025-09-18/Robot Control Stack_ A Lean Ecosystem for Robot Learning at Scale_20250918|Robot Control Stack A Lean Ecosystem for Robot Learning at Scale]] (85.8% similar)
- [[2025-09-19/ForceVLA_ Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation_20250919|ForceVLA Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]] (85.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15937v1 Announce Type: cross 
Abstract: Robotic real-world reinforcement learning (RL) with vision-language-action (VLA) models is bottlenecked by sparse, handcrafted rewards and inefficient exploration. We introduce VLAC, a general process reward model built upon InternVL and trained on large scale heterogeneous datasets. Given pairwise observations and a language goal, it outputs dense progress delta and done signal, eliminating task-specific reward engineering, and supports one-shot in-context transfer to unseen tasks and environments. VLAC is trained on vision-language datasets to strengthen perception, dialogic and reasoning capabilities, together with robot and human trajectories data that ground action generation and progress estimation, and additionally strengthened to reject irrelevant prompts as well as detect regression or stagnation by constructing large numbers of negative and semantically mismatched samples. With prompt control, a single VLAC model alternately generating reward and action tokens, unifying critic and policy. Deployed inside an asynchronous real-world RL loop, we layer a graded human-in-the-loop protocol (offline demonstration replay, return and explore, human guided explore) that accelerates exploration and stabilizes early learning. Across four distinct real-world manipulation tasks, VLAC lifts success rates from about 30\% to about 90\% within 200 real-world interaction episodes; incorporating human-in-the-loop interventions yields a further 50% improvement in sample efficiency and achieves up to 100% final success.

## 🔍 Abstract (한글 번역)

arXiv:2509.15937v1 발표 유형: 교차  
초록: 비전-언어-행동(VLA) 모델을 사용하는 로봇의 실제 강화 학습(RL)은 드문 수작업 보상과 비효율적인 탐색으로 인해 병목 현상을 겪고 있습니다. 우리는 InternVL에 기반하여 대규모 이질적 데이터셋으로 훈련된 일반적인 프로세스 보상 모델인 VLAC를 소개합니다. 쌍으로 된 관찰과 언어 목표가 주어졌을 때, 이는 조밀한 진행 델타와 완료 신호를 출력하여 과제별 보상 설계를 제거하고, 보지 못한 과제와 환경에 대한 한 번의 맥락 내 전이를 지원합니다. VLAC는 시각-언어 데이터셋으로 훈련되어 인식, 대화 및 추론 능력을 강화하며, 로봇 및 인간 궤적 데이터를 통해 행동 생성 및 진행 추정을 기반으로 하고, 관련 없는 프롬프트를 거부하고 회귀 또는 정체를 감지하기 위해 대량의 부정적 및 의미적으로 불일치하는 샘플을 구성하여 추가로 강화됩니다. 프롬프트 제어를 통해, 단일 VLAC 모델은 보상 및 행동 토큰을 번갈아 생성하여 비평가와 정책을 통합합니다. 비동기적인 실제 RL 루프 내에 배치되어, 탐색을 가속화하고 초기 학습을 안정화하는 등급화된 인간 참여 프로토콜(오프라인 시연 재생, 반환 및 탐색, 인간이 안내하는 탐색)을 계층화합니다. 네 가지 서로 다른 실제 조작 작업에서, VLAC는 약 30%의 성공률을 약 90%로 끌어올리며, 200회의 실제 상호작용 에피소드 내에서 인간 참여 개입을 포함하면 샘플 효율성이 추가로 50% 향상되고 최대 100%의 최종 성공을 달성합니다.

## 📝 요약

이 논문은 로봇의 실제 강화 학습에서 시각-언어-행동(VLA) 모델의 보상과 탐색의 비효율성을 해결하기 위해 VLAC라는 일반적인 프로세스 보상 모델을 제안합니다. VLAC는 InternVL을 기반으로 하여 대규모 이질적 데이터셋에서 훈련되며, 언어 목표와 관찰 쌍을 입력받아 밀도 있는 진행 상황과 완료 신호를 출력합니다. 이를 통해 과제별 보상 설계가 필요 없으며, 새로운 과제와 환경에 대한 일회성 전이 학습을 지원합니다. VLAC는 시각-언어 데이터셋과 로봇 및 인간의 궤적 데이터를 사용하여 인식, 대화 및 추론 능력을 강화하고, 부적절한 프롬프트를 거부하고 퇴보나 정체를 감지할 수 있도록 훈련되었습니다. VLAC는 비동기 실제 RL 루프에 배치되어 인간의 개입을 통한 탐색 가속화와 초기 학습 안정화를 돕습니다. 네 가지 실제 조작 과제에서 성공률을 약 30%에서 90%로 향상시켰으며, 인간의 개입을 통해 샘플 효율성을 50% 더 개선하여 최대 100%의 최종 성공률을 달성했습니다.

## 🎯 주요 포인트

- 1. VLAC는 InternVL을 기반으로 구축된 일반 프로세스 보상 모델로, 대규모 이질적 데이터셋에서 훈련되어 작업별 보상 설계를 제거하고 새로운 작업과 환경에 대한 원샷 전이를 지원합니다.

- 2. VLAC는 시각-언어 데이터셋과 로봇 및 인간의 궤적 데이터를 통해 인식, 대화 및 추론 능력을 강화하고, 무관한 프롬프트를 거부하고 퇴행 또는 정체를 감지하도록 강화되었습니다.

- 3. VLAC 모델은 비동기 실세계 강화 학습 루프 내에 배치되어 탐색을 가속화하고 초기 학습을 안정화하는 인간 참여 프로토콜을 계층화합니다.

- 4. 네 가지 실세계 조작 작업에서 VLAC는 약 30%에서 약 90%로 성공률을 향상시키며, 인간 참여 개입을 통합하면 샘플 효율성이 50% 더 개선되어 최대 100%의 최종 성공을 달성합니다.

---

*Generated on 2025-09-22 14:18:08*