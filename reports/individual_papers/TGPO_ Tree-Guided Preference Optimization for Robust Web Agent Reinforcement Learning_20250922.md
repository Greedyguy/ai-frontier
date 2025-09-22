# TGPO: Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning

**Korean Title:** TGPO: 견고한 웹 에이전트 강화 학습을 위한 트리 기반 선호 최적화

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dynamic Weighting Mechanism

## 🔗 유사한 논문
- [[2025-09-17/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250917|TGPO Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (99.2% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (82.5% similar)
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (82.3% similar)
- [[2025-09-19/Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (81.9% similar)
- [[2025-09-22/PVPO_ Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning_20250922|PVPO Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning]] (81.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14172v2 Announce Type: replace-cross 
Abstract: With the rapid advancement of large language models and vision-language models, employing large models as Web Agents has become essential for automated web interaction. However, training Web Agents with reinforcement learning faces critical challenges including credit assignment misallocation, prohibitively high annotation costs, and reward sparsity. To address these issues, we propose Tree-Guided Preference Optimization (TGPO), an offline reinforcement learning framework that proposes a tree-structured trajectory representation merging semantically identical states across trajectories to eliminate label conflicts. Our framework incorporates a Process Reward Model that automatically generates fine-grained rewards through subgoal progress, redundancy detection, and action verification. Additionally, a dynamic weighting mechanism prioritizes high-impact decision points during training. Experiments on Online-Mind2Web and our self-constructed C-WebShop datasets demonstrate that TGPO significantly outperforms existing methods, achieving higher success rates with fewer redundant steps.

## 🔍 Abstract (한글 번역)

arXiv:2509.14172v2 발표 유형: 교차 교체  
초록: 대형 언어 모델과 비전-언어 모델의 급속한 발전으로 인해 대형 모델을 웹 에이전트로 활용하는 것이 자동화된 웹 상호작용에 필수적이 되었습니다. 그러나 강화 학습을 통해 웹 에이전트를 훈련하는 데에는 신용 할당의 잘못된 배분, 지나치게 높은 주석 비용, 보상의 희소성 등 중요한 문제들이 존재합니다. 이러한 문제를 해결하기 위해, 우리는 Tree-Guided Preference Optimization (TGPO)을 제안합니다. 이는 의미적으로 동일한 상태를 통합하여 경로 간의 레이블 충돌을 제거하는 트리 구조의 경로 표현을 제안하는 오프라인 강화 학습 프레임워크입니다. 우리의 프레임워크는 하위 목표 진행, 중복 감지, 행동 검증을 통해 세분화된 보상을 자동으로 생성하는 프로세스 보상 모델을 포함합니다. 또한, 훈련 중에 높은 영향력을 미치는 결정 지점을 우선시하는 동적 가중 메커니즘을 포함하고 있습니다. Online-Mind2Web 및 우리가 자체적으로 구축한 C-WebShop 데이터셋에 대한 실험은 TGPO가 기존 방법보다 훨씬 뛰어난 성과를 보이며, 더 적은 중복 단계로 더 높은 성공률을 달성함을 보여줍니다.

## 📝 요약

이 논문은 대형 언어 모델과 비전-언어 모델의 발전에 따라 웹 에이전트를 자동화하는 데 필요한 강화 학습의 문제점을 해결하기 위해 Tree-Guided Preference Optimization (TGPO)라는 오프라인 강화 학습 프레임워크를 제안합니다. TGPO는 의미적으로 동일한 상태를 병합하여 레이블 충돌을 제거하는 트리 구조의 경로 표현을 사용합니다. 또한, 세부적인 보상을 자동으로 생성하는 프로세스 보상 모델과 높은 영향력을 가진 결정 지점을 우선시하는 동적 가중치 메커니즘을 포함합니다. 실험 결과, TGPO는 기존 방법보다 더 높은 성공률과 적은 중복 단계로 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델과 비전-언어 모델의 발전으로 웹 에이전트의 자동화된 웹 상호작용이 중요해지고 있다.

- 2. 웹 에이전트의 강화 학습에는 신용 할당 오류, 높은 주석 비용, 보상 희소성 등의 문제가 있다.

- 3. Tree-Guided Preference Optimization (TGPO)는 트리 구조의 궤적 표현을 통해 레이블 충돌을 제거하는 오프라인 강화 학습 프레임워크이다.

- 4. TGPO는 세부적인 보상을 자동 생성하는 프로세스 보상 모델을 포함하며, 중복 탐지와 행동 검증을 통해 보상을 제공한다.

- 5. 실험 결과 TGPO는 기존 방법보다 높은 성공률과 적은 중복 단계를 통해 성능을 입증하였다.

---

*Generated on 2025-09-22 15:05:42*