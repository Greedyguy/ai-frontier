---
keywords:
  - Reinforcement Learning
  - Self-Improvement
  - Autonomous Skill Acquisition
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:10:35.847492",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Self-Improvement",
    "Autonomous Skill Acquisition"
  ],
  "rejected_keywords": [
    "Foundation Models",
    "Behavioral Cloning"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.85,
    "Self-Improvement": 0.8,
    "Autonomous Skill Acquisition": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Self-Improving Embodied Foundation Models

**Korean Title:** 자기 개선 구현 기반 모델

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Self-Improvement|Self-Improvement]], [[keywords/Autonomous Skill Acquisition|Autonomous Skill Acquisition]]

## 🔗 유사한 논문
- [[(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (82.8% similar)
- [[CRAFT_ Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks_20250919|CRAFT Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks]] (82.4% similar)
- [[From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (81.9% similar)
- [[Embracing Bulky Objects with Humanoid Robots_ Whole-Body Manipulation with Reinforcement Learning_20250918|Embracing Bulky Objects with Humanoid Robots Whole-Body Manipulation with Reinforcement Learning]] (81.7% similar)
- [[TrajBooster_ Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning_20250918|TrajBooster Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning]] (81.6% similar)

## 📋 저자 정보

**Authors:** Seyed Kamyar Seyed Ghasemipour, Ayzaan Wahid, Jonathan Tompson, Pannag Sanketi, Igor Mordatch

## 📄 Abstract (원문)

Foundation models trained on web-scale data have revolutionized robotics, but
their application to low-level control remains largely limited to behavioral
cloning. Drawing inspiration from the success of the reinforcement learning
stage in fine-tuning large language models, we propose a two-stage
post-training approach for robotics. The first stage, Supervised Fine-Tuning
(SFT), fine-tunes pretrained foundation models using both: a) behavioral
cloning, and b) steps-to-go prediction objectives. In the second stage,
Self-Improvement, steps-to-go prediction enables the extraction of a
well-shaped reward function and a robust success detector, enabling a fleet of
robots to autonomously practice downstream tasks with minimal human
supervision. Through extensive experiments on real-world and simulated robot
embodiments, our novel post-training recipe unveils significant results on
Embodied Foundation Models. First, we demonstrate that the combination of SFT
and Self-Improvement is significantly more sample-efficient than scaling
imitation data collection for supervised learning, and that it leads to
policies with significantly higher success rates. Further ablations highlight
that the combination of web-scale pretraining and Self-Improvement is the key
to this sample-efficiency. Next, we demonstrate that our proposed combination
uniquely unlocks a capability that current methods cannot achieve: autonomously
practicing and acquiring novel skills that generalize far beyond the behaviors
observed in the imitation learning datasets used during training. These
findings highlight the transformative potential of combining pretrained
foundation models with online Self-Improvement to enable autonomous skill
acquisition in robotics. Our project website can be found at
https://self-improving-efms.github.io .

## 🔍 Abstract (한글 번역)

웹 규모의 데이터로 학습된 기초 모델은 로봇 공학에 혁신을 가져왔지만, 저수준 제어에의 적용은 주로 행동 복제에 제한되어 있습니다. 대형 언어 모델의 미세 조정에서 강화 학습 단계의 성공에서 영감을 받아, 우리는 로봇 공학을 위한 이단계 사후 학습 접근 방식을 제안합니다. 첫 번째 단계인 지도 미세 조정(SFT)에서는 사전 학습된 기초 모델을 a) 행동 복제와 b) 남은 단계 예측 목표를 사용하여 미세 조정합니다. 두 번째 단계인 자기 개선에서는 남은 단계 예측을 통해 잘 형성된 보상 함수와 강력한 성공 탐지기를 추출하여, 로봇 무리가 최소한의 인간 감독 하에 다운스트림 작업을 자율적으로 연습할 수 있게 합니다. 실제 및 시뮬레이션된 로봇 구현에 대한 광범위한 실험을 통해, 우리의 새로운 사후 학습 방법은 구현된 기초 모델에서 중요한 결과를 보여줍니다. 첫째, 우리는 SFT와 자기 개선의 조합이 감독 학습을 위한 모방 데이터 수집을 확장하는 것보다 샘플 효율성이 훨씬 높으며, 이는 성공률이 훨씬 높은 정책으로 이어진다는 것을 입증합니다. 추가적인 분석은 웹 규모의 사전 학습과 자기 개선의 조합이 이 샘플 효율성의 핵심임을 강조합니다. 다음으로, 우리는 제안된 조합이 현재 방법으로는 달성할 수 없는 능력을 독특하게 열어준다는 것을 입증합니다: 훈련 중 사용된 모방 학습 데이터셋에서 관찰된 행동을 훨씬 넘어 일반화되는 새로운 기술을 자율적으로 연습하고 습득하는 것입니다. 이러한 발견은 로봇 공학에서 자율적인 기술 습득을 가능하게 하기 위해 사전 학습된 기초 모델과 온라인 자기 개선을 결합하는 것의 변혁적 잠재력을 강조합니다. 우리의 프로젝트 웹사이트는 https://self-improving-efms.github.io 에서 확인할 수 있습니다.

## 📝 요약

웹 규모의 데이터를 학습한 파운데이션 모델은 로보틱스 분야에 혁신을 가져왔지만, 저수준 제어에의 적용은 주로 행동 복제에 제한되어 있습니다. 본 연구는 대규모 언어 모델의 강화 학습 성공 사례에서 영감을 받아 로보틱스에 두 단계의 사후 학습 접근법을 제안합니다. 첫 번째 단계는 행동 복제와 목표 예측을 활용한 '지도 세분화(SFT)'로, 사전 학습된 모델을 미세 조정합니다. 두 번째 단계인 '자기 개선'에서는 목표 예측을 통해 보상 함수와 성공 탐지기를 추출하여 최소한의 인간 감독으로 로봇이 자율적으로 작업을 수행할 수 있게 합니다. 실험 결과, SFT와 자기 개선의 조합이 모방 학습 데이터 수집보다 샘플 효율성이 높고, 성공률이 크게 향상된 정책을 도출함을 보였습니다. 또한, 웹 규모 사전 학습과 자기 개선의 결합이 이러한 효율성의 핵심임을 밝혔습니다. 이 조합은 기존 방법으로는 불가능한 자율적인 새로운 기술 습득을 가능하게 하며, 로보틱스에서 자율적인 기술 획득의 잠재력을 강조합니다.

## 🎯 주요 포인트

- 1. 웹 규모 데이터로 훈련된 파운데이션 모델은 로보틱스 분야에서 혁신을 일으켰지만, 저수준 제어에의 적용은 주로 행동 복제에 제한되어 있다.

- 2. 본 연구는 대규모 언어 모델의 미세 조정에서 강화 학습의 성공을 바탕으로 로보틱스에 대한 두 단계의 사후 훈련 접근 방식을 제안한다.

- 3. 첫 번째 단계인 감독된 미세 조정(SFT)은 행동 복제와 목표 예측을 통해 사전 훈련된 모델을 미세 조정한다.

- 4. 두 번째 단계인 자기 개선(Self-Improvement)은 목표 예측을 통해 보상 함수와 성공 탐지기를 추출하여 로봇이 최소한의 인간 감독 하에 자율적으로 작업을 수행할 수 있게 한다.

- 5. 제안된 방법은 자율적으로 새로운 기술을 연습하고 습득할 수 있는 능력을 제공하며, 이는 기존 방법으로는 달성할 수 없는 능력이다.

---

*Generated on 2025-09-20 00:55:59*