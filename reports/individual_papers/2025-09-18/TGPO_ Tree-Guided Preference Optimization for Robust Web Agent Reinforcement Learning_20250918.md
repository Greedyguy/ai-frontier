---
keywords:
  - Reinforcement Learning
  - Large Language Models
  - Vision-Language Models
category: cs.AI
publish_date: 2025-09-18
arxiv_id: 2509.14172
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:07:35.990802",
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

**Korean Title:** TGPO: 강건한 웹 에이전트 강화학습을 위한 트리 가이드 선호 최적화

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]], [[keywords/Vision-Language Models|Vision-Language Models]]

## 🔗 유사한 논문
- [[AgentCTG Harnessing Multi-Agent Collaboration for Fine-Grained Precise Control in Text Generation]] (80.5% similar)
- [[Controllable Pareto Trade-off between Fairness and Accuracy]] (80.3% similar)
- [[Video-Language Critic Transferable Reward Functions for Language-Conditioned Robotics]] (80.1% similar)
- [[DRDT3 Diffusion-Refined Decision Test-Time Training Model]] (79.8% similar)
- [[THOR Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning]] (79.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14172v1 Announce Type: cross 
Abstract: With the rapid advancement of large language models and vision-language models, employing large models as Web Agents has become essential for automated web interaction. However, training Web Agents with reinforcement learning faces critical challenges including credit assignment misallocation, prohibitively high annotation costs, and reward sparsity. To address these issues, we propose Tree-Guided Preference Optimization (TGPO), an offline reinforcement learning framework that proposes a tree-structured trajectory representation merging semantically identical states across trajectories to eliminate label conflicts. Our framework incorporates a Process Reward Model that automatically generates fine-grained rewards through subgoal progress, redundancy detection, and action verification. Additionally, a dynamic weighting mechanism prioritizes high-impact decision points during training. Experiments on Online-Mind2Web and our self-constructed C-WebShop datasets demonstrate that TGPO significantly outperforms existing methods, achieving higher success rates with fewer redundant steps.

## 🔍 Abstract (한글 번역)

arXiv:2509.14172v1 발표 유형: cross 
초록: 대규모 언어 모델과 비전-언어 모델의 급속한 발전으로, 자동화된 웹 상호작용을 위해 대규모 모델을 웹 에이전트로 활용하는 것이 필수적이 되었다. 그러나 강화학습으로 웹 에이전트를 훈련하는 것은 신용 할당 오분배, 극도로 높은 주석 비용, 그리고 보상 희소성과 같은 중요한 문제들에 직면하고 있다. 이러한 문제들을 해결하기 위해, 우리는 Tree-Guided Preference Optimization (TGPO)을 제안한다. 이는 의미적으로 동일한 상태들을 궤적들 간에 병합하여 레이블 충돌을 제거하는 트리 구조 궤적 표현을 제안하는 오프라인 강화학습 프레임워크이다. 우리의 프레임워크는 하위 목표 진행도, 중복성 탐지, 그리고 행동 검증을 통해 자동으로 세밀한 보상을 생성하는 Process Reward Model을 포함한다. 또한, 동적 가중치 메커니즘이 훈련 중 높은 영향력을 가진 결정 지점들에 우선순위를 부여한다. Online-Mind2Web과 우리가 자체 구축한 C-WebShop 데이터셋에서의 실험은 TGPO가 기존 방법들을 상당히 능가하며, 더 적은 중복 단계로 더 높은 성공률을 달성함을 보여준다.

## 📝 요약

이 논문은 대형 언어 모델과 비전-언어 모델의 발전에 따라 웹 에이전트로서의 자동화된 웹 상호작용의 필요성을 강조합니다. 그러나 강화 학습을 통한 웹 에이전트 훈련은 여러 문제점이 있습니다. 이를 해결하기 위해, 저자들은 Tree-Guided Preference Optimization (TGPO)라는 오프라인 강화 학습 프레임워크를 제안합니다. TGPO는 트리 구조의 궤적 표현을 사용하여 레이블 충돌을 제거하고, 프로세스 보상 모델을 통해 세부적인 보상을 자동 생성합니다. 또한, 동적 가중치 메커니즘을 통해 훈련 시 중요한 결정 지점에 우선순위를 둡니다. 실험 결과, TGPO는 기존 방법들보다 높은 성공률과 적은 중복 단계를 달성했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델과 비전-언어 모델의 발전으로 웹 에이전트의 자동화된 웹 상호작용이 중요해졌습니다.

- 2. 웹 에이전트의 강화 학습에는 보상 할당 오류, 높은 주석 비용, 보상 희소성 등의 문제가 있습니다.

- 3. Tree-Guided Preference Optimization (TGPO)는 오프라인 강화 학습 프레임워크로, 트리 구조의 경로 표현을 통해 레이블 충돌을 제거합니다.

- 4. TGPO는 세부 보상을 자동 생성하는 프로세스 보상 모델을 포함하여 학습 중 중요한 결정 지점을 우선시하는 동적 가중치 메커니즘을 제공합니다.

- 5. 실험 결과 TGPO는 기존 방법보다 높은 성공률과 적은 중복 단계로 우수한 성능을 보였습니다.

---

*Generated on 2025-09-19 10:50:17*