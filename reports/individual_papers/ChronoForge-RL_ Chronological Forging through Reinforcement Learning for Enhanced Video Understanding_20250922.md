# ChronoForge-RL: Chronological Forging through Reinforcement Learning for Enhanced Video Understanding

**Korean Title:** ChronoForge-RL: 강화 학습을 통한 연대기적 단조로 비디오 이해력 향상

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Temporal Apex Distillation

## 🔗 유사한 논문
- [[2025-09-19/WorldForge_ Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance_20250919|WorldForge Unlocking Emergent 3D4D Generation in Video Diffusion Model via Training-Free Guidance]] (84.6% similar)
- [[2025-09-17/Dense Video Understanding with Gated Residual Tokenization_20250917|Dense Video Understanding with Gated Residual Tokenization]] (83.3% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (82.3% similar)
- [[2025-09-19/Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning_20250919|Continuous-Time Value Iteration for Multi-Agent Reinforcement Learning]] (81.1% similar)
- [[2025-09-19/ToolSample_ Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning_20250919|ToolSample Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning]] (80.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15800v1 Announce Type: cross 
Abstract: Current state-of-the-art video understanding methods typically struggle with two critical challenges: (1) the computational infeasibility of processing every frame in dense video content and (2) the difficulty in identifying semantically significant frames through naive uniform sampling strategies. In this paper, we propose a novel video understanding framework, called ChronoForge-RL, which combines Temporal Apex Distillation (TAD) and KeyFrame-aware Group Relative Policy Optimization (KF-GRPO) to tackle these issues. Concretely, we introduce a differentiable keyframe selection mechanism that systematically identifies semantic inflection points through a three-stage process to enhance computational efficiency while preserving temporal information. Then, two particular modules are proposed to enable effective temporal reasoning: Firstly, TAD leverages variation scoring, inflection detection, and prioritized distillation to select the most informative frames. Secondly, we introduce KF-GRPO which implements a contrastive learning paradigm with a saliency-enhanced reward mechanism that explicitly incentivizes models to leverage both frame content and temporal relationships. Finally, our proposed ChronoForge-RL achieves 69.1% on VideoMME and 52.7% on LVBench compared to baseline methods, clearly surpassing previous approaches while enabling our 7B parameter model to achieve performance comparable to 72B parameter alternatives.

## 🔍 Abstract (한글 번역)

arXiv:2509.15800v1 발표 유형: 교차  
초록: 현재 최첨단 비디오 이해 방법은 일반적으로 두 가지 중요한 도전에 직면하고 있습니다: (1) 밀집된 비디오 콘텐츠의 모든 프레임을 처리하는 계산적 비현실성과 (2) 단순한 균일 샘플링 전략을 통해 의미론적으로 중요한 프레임을 식별하는 어려움입니다. 본 논문에서는 이러한 문제를 해결하기 위해 Temporal Apex Distillation (TAD)과 KeyFrame-aware Group Relative Policy Optimization (KF-GRPO)을 결합한 새로운 비디오 이해 프레임워크인 ChronoForge-RL을 제안합니다. 구체적으로, 우리는 계산 효율성을 향상시키면서 시간 정보를 보존하기 위해 세 단계의 과정을 통해 의미론적 변곡점을 체계적으로 식별하는 미분 가능한 키프레임 선택 메커니즘을 도입합니다. 그런 다음, 효과적인 시간적 추론을 가능하게 하는 두 가지 모듈을 제안합니다: 첫째, TAD는 변동 점수화, 변곡점 탐지 및 우선 순위 증류를 활용하여 가장 정보가 많은 프레임을 선택합니다. 둘째, 우리는 KF-GRPO를 도입하여 프레임 콘텐츠와 시간적 관계를 모두 활용하도록 명시적으로 모델에 인센티브를 제공하는 주목성 강화 보상 메커니즘을 갖춘 대조 학습 패러다임을 구현합니다. 마지막으로, 제안된 ChronoForge-RL은 VideoMME에서 69.1%, LVBench에서 52.7%를 기록하며, 기존 방법을 명확히 능가하면서 7B 파라미터 모델이 72B 파라미터 대안과 유사한 성능을 달성할 수 있도록 합니다.

## 📝 요약

이 논문에서는 비디오 이해의 두 가지 주요 문제를 해결하기 위해 ChronoForge-RL이라는 새로운 프레임워크를 제안합니다. 첫째, Temporal Apex Distillation(TAD)과 KeyFrame-aware Group Relative Policy Optimization(KF-GRPO)를 결합하여 계산 효율성을 높이면서 의미 있는 프레임을 선택합니다. TAD는 변동 점수와 우선순위 증류를 통해 정보가 풍부한 프레임을 선택하고, KF-GRPO는 대조 학습과 중요도 기반 보상 메커니즘을 사용하여 프레임 내용과 시간적 관계를 활용합니다. 이 방법론은 VideoMME와 LVBench에서 각각 69.1%와 52.7%의 성능을 기록하며, 기존 방법을 능가하는 성과를 보였습니다.

## 🎯 주요 포인트

- 1. 현재 최첨단 비디오 이해 방법은 모든 프레임을 처리하는 계산적 비효율성과 균일 샘플링 전략으로 의미 있는 프레임을 식별하는 어려움에 직면해 있다.

- 2. ChronoForge-RL은 Temporal Apex Distillation(TAD)와 KeyFrame-aware Group Relative Policy Optimization(KF-GRPO)을 결합하여 이러한 문제를 해결하는 새로운 비디오 이해 프레임워크이다.

- 3. 차별화된 키프레임 선택 메커니즘을 통해 의미 있는 변곡점을 체계적으로 식별하여 계산 효율성을 높이고 시간 정보를 보존한다.

- 4. TAD는 변동 점수, 변곡점 탐지 및 우선 순위 증류를 활용하여 가장 정보가 많은 프레임을 선택한다.

- 5. KF-GRPO는 명확한 보상 메커니즘을 통해 프레임 콘텐츠와 시간적 관계를 활용하도록 모델을 유도하며, ChronoForge-RL은 기존 방법을 능가하는 성능을 보여준다.

---

*Generated on 2025-09-22 14:12:11*