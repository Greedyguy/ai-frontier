---
keywords:
  - Reinforcement Learning
  - Large Language Models
  - Vision-Language Models
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:44:39.255190",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Large Language Models",
    "Vision-Language Models"
  ],
  "rejected_keywords": [
    "Tree-Guided Preference Optimization"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.85,
    "Large Language Models": 0.8,
    "Vision-Language Models": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning

**Korean Title:** TGPO: 강건한 웹 에이전트 강화 학습을 위한 트리 안내형 선호 최적화

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]], [[keywords/Vision-Language Models|Vision-Language Models]]

## 🔗 유사한 논문
- [[TGPO Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (99.2% similar)
- [[Controllable Pareto Trade-off between Fairness and Accuracy]] (80.4% similar)
- [[DRDT3 Diffusion-Refined Decision Test-Time Training Model]] (79.9% similar)
- [[Video-Language Critic Transferable Reward Functions for Language-Conditioned Robotics]] (79.8% similar)
- [[AgentCTG Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation]] (79.5% similar)

## 📋 저자 정보

**Authors:** Ziyuan Chen, Zhenghui Zhao, Zhangye Han, Miancan Liu, Xianhang Ye, Yiqing Li, Hongbo Min, Jinkui Ren, Xiantao Zhang, Guitao Cao

## 📄 Abstract (원문)

With the rapid advancement of large language models and vision-language
models, employing large models as Web Agents has become essential for automated
web interaction. However, training Web Agents with reinforcement learning faces
critical challenges including credit assignment misallocation, prohibitively
high annotation costs, and reward sparsity. To address these issues, we propose
Tree-Guided Preference Optimization (TGPO), an offline reinforcement learning
framework that proposes a tree-structured trajectory representation merging
semantically identical states across trajectories to eliminate label conflicts.
Our framework incorporates a Process Reward Model that automatically generates
fine-grained rewards through subgoal progress, redundancy detection, and action
verification. Additionally, a dynamic weighting mechanism prioritizes
high-impact decision points during training. Experiments on Online-Mind2Web and
our self-constructed C-WebShop datasets demonstrate that TGPO significantly
outperforms existing methods, achieving higher success rates with fewer
redundant steps.

## 🔍 Abstract (한글 번역)

대규모 언어 모델 및 시각-언어 모델의 급속한 발전으로 대규모 모델을 웹 에이전트로 사용하는 것이 자동화된 웹 상호작용에 필수적이 되었습니다. 그러나 강화 학습을 사용하여 웹 에이전트를 훈련하는 것은 신용 할당 오류, 지나치게 높은 주석 비용 및 보상 희소성과 같은 중요한 도전에 직면하고 있습니다. 이러한 문제를 해결하기 위해 우리는 Tree-Guided Preference Optimization (TGPO)을 제안합니다. 이는 레이블 충돌을 제거하기 위해 궤적 표현을 합치는 트리 구조로 구성된 오프라인 강화 학습 프레임워크입니다. 우리의 프레임워크는 하위 목표 진행, 중복 감지 및 작업 확인을 통해 세부적인 보상을 자동으로 생성하는 Process Reward Model을 포함하고 있습니다. 또한, 훈련 중에 고영향 결정 지점을 우선적으로 다루는 동적 가중치 메커니즘을 포함하고 있습니다. Online-Mind2Web 및 우리가 직접 구축한 C-WebShop 데이터셋에서의 실험 결과는 TGPO가 기존 방법보다 훨씬 우수한 성과를 보여주며, 더 적은 중복 단계로 더 높은 성공률을 달성한다는 것을 보여줍니다.

## 📝 요약

최근 대형 언어 모델 및 시각-언어 모델의 급속한 발전으로 대규모 모델을 웹 에이전트로 활용하는 것이 자동화된 웹 상호작용에 필수적이 되었다. 그러나 강화 학습을 사용하여 웹 에이전트를 훈련하는 것은 신용 할당 오류, 과도한 주석 비용 및 보상 희소성과 같은 중요한 도전에 직면하고 있다. 이러한 문제를 해결하기 위해 우리는 Tree-Guided Preference Optimization (TGPO)이라는 오프라인 강화 학습 프레임워크를 제안한다. TGPO는 레이블 충돌을 제거하기 위해 의미적으로 동일한 상태를 병합하는 트리 구조의 경로 표현을 제안한다. 또한 세부 목표 진행, 중복 감지 및 작업 확인을 통해 세분화된 보상을 자동으로 생성하는 Process Reward Model을 포함하고 있다. 실험 결과는 TGPO가 기존 방법보다 우수한 성능을 보이며 더 적은 중복 단계로 더 높은 성공률을 달성한다는 것을 보여준다.

## 🎯 주요 포인트

- 대규모 언어 모델 및 시각-언어 모델의 급속한 발전으로 대규모 모델을 웹 에이전트로 활용하는 것이 자동화된 웹 상호작용에 필수적이 되었다.

- TGPO는 오프라인 강화 학습 프레임워크로, 라벨 충돌을 제거하기 위해 의미적으로 동일한 상태를 병합하는 트리 구조의 경로 표현을 제안한다.

- 프로세스 보상 모델을 통해 하위 목표 진행, 중복 감지 및 작업 확인을 통해 세부적인 보상을 자동으로 생성한다.

- TGPO는 기존 방법보다 높은 성공률을 달성하면서 중복 단계를 줄이는 것을 실험을 통해 입증했다.

---

*Generated on 2025-09-18 17:04:30*