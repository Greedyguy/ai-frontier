---
keywords:
  - Reinforcement Learning
  - Dynamic Sampling with Curriculum Learning
  - Large Language Models
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14718
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:21:04.792135",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Dynamic Sampling with Curriculum Learning",
    "Large Language Models"
  ],
  "rejected_keywords": [
    "Multi-Task Learning"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.8,
    "Dynamic Sampling with Curriculum Learning": 0.78,
    "Large Language Models": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# ToolSample: Dual Dynamic Sampling Methods with Curriculum Learning for RL-based Tool Learning

**Korean Title:** 도구 샘플: RL 기반 도구 학습을 위한 커리큘럼 학습을 활용한 이중 동적 샘플링 방법

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Dynamic Sampling with Curriculum Learning|Dynamic Sampling with Curriculum Learning]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Large Language Models]]

## 🔗 유사한 논문
- [[Process-Supervised_Reinforcement_Learning_for_Interactive_Multimodal_Tool-Use_Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (82.8% similar)
- [[Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (81.3% similar)
- [[FlowRL Matching Reward Distributions for LLM Reasoning]] (80.6% similar)
- [[(P)rior(D)yna(F)low A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (79.9% similar)
- [[Constructive_Conflict-Driven_Multi-Agent_Reinforcement_Learning_for_Strategic_Diversity_20250919|Constructive Conflict-Driven Multi-Agent Reinforcement Learning for Strategic Diversity]] (79.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14718v1 Announce Type: new 
Abstract: While reinforcement learning (RL) is increasingly used for LLM-based tool learning, its efficiency is often hampered by an overabundance of simple samples that provide diminishing learning value as training progresses. Existing dynamic sampling techniques are ill-suited for the multi-task structure and fine-grained reward mechanisms inherent to tool learning. This paper introduces Dynamic Sampling with Curriculum Learning (DSCL), a framework specifically designed to address this challenge by targeting the unique characteristics of tool learning: its multiple interdependent sub-tasks and multi-valued reward functions. DSCL features two core components: Reward-Based Dynamic Sampling, which uses multi-dimensional reward statistics (mean and variance) to prioritize valuable data, and Task-Based Dynamic Curriculum Learning, which adaptively focuses training on less-mastered sub-tasks. Through extensive experiments, we demonstrate that DSCL significantly improves training efficiency and model performance over strong baselines, achieving a 3.29\% improvement on the BFCLv3 benchmark. Our method provides a tailored solution that effectively leverages the complex reward signals and sub-task dynamics within tool learning to achieve superior results.

## 🔍 Abstract (한글 번역)

arXiv:2509.14718v1 발표 유형: 신규  
초록: 강화 학습(RL)은 점점 더 LLM 기반 도구 학습에 사용되고 있지만, 훈련이 진행됨에 따라 학습 가치가 감소하는 단순한 샘플의 과다로 인해 효율성이 종종 저해됩니다. 기존의 동적 샘플링 기법은 도구 학습에 내재된 다중 작업 구조와 세분화된 보상 메커니즘에 적합하지 않습니다. 본 논문에서는 이러한 문제를 해결하기 위해 도구 학습의 고유한 특성, 즉 여러 상호 의존적인 하위 작업과 다중 값 보상 함수를 목표로 설계된 프레임워크인 커리큘럼 학습을 통한 동적 샘플링(DSCL)을 소개합니다. DSCL은 두 가지 핵심 구성 요소를 특징으로 합니다: 다차원 보상 통계(평균 및 분산)를 사용하여 가치 있는 데이터를 우선시하는 보상 기반 동적 샘플링과 덜 숙달된 하위 작업에 적응적으로 훈련을 집중시키는 작업 기반 동적 커리큘럼 학습입니다. 광범위한 실험을 통해 DSCL이 강력한 기준선 대비 훈련 효율성과 모델 성능을 크게 향상시켜 BFCLv3 벤치마크에서 3.29%의 개선을 달성함을 입증합니다. 우리의 방법은 도구 학습 내의 복잡한 보상 신호와 하위 작업 역학을 효과적으로 활용하여 우수한 결과를 달성하는 맞춤형 솔루션을 제공합니다.

## 📝 요약

이 논문은 도구 학습의 다중 과제 구조와 세분화된 보상 메커니즘에 적합하지 않은 기존의 동적 샘플링 기법 문제를 해결하기 위해, DSCL(커리큘럼 학습을 통한 동적 샘플링) 프레임워크를 제안합니다. DSCL은 보상 기반 동적 샘플링과 과제 기반 동적 커리큘럼 학습을 통해 학습 효율성과 모델 성능을 향상시킵니다. 실험 결과, DSCL은 BFCLv3 벤치마크에서 3.29%의 성능 향상을 보여주며, 도구 학습의 복잡한 보상 신호와 하위 과제 동태를 효과적으로 활용하여 우수한 결과를 달성합니다.

## 🎯 주요 포인트

- 1. 강화 학습은 LLM 기반 도구 학습에 점점 더 많이 사용되지만, 단순 샘플의 과잉으로 인해 학습 효율성이 저하될 수 있습니다.

- 2. 기존의 동적 샘플링 기법은 도구 학습의 다중 과제 구조와 세밀한 보상 메커니즘에 적합하지 않습니다.

- 3. DSCL(커리큘럼 학습을 통한 동적 샘플링)은 도구 학습의 독특한 특성을 겨냥하여 설계된 프레임워크로, 보상 기반 동적 샘플링과 과제 기반 동적 커리큘럼 학습을 포함합니다.

- 4. DSCL은 BFCLv3 벤치마크에서 3.29%의 성능 향상을 이루며, 강력한 기준선 대비 훈련 효율성과 모델 성능을 크게 개선합니다.

- 5. 이 방법은 복잡한 보상 신호와 하위 과제의 역학을 효과적으로 활용하여 도구 학습에서 우수한 결과를 달성합니다.

---

*Generated on 2025-09-19 15:26:25*