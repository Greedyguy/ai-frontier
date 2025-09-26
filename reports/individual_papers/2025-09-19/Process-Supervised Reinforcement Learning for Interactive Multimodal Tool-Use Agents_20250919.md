---
keywords:
  - Reinforcement Learning
  - Large Language Models
  - Turn-level Adjudicated Reinforcement Learning
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14480
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:28:39.277673",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Reinforcement Learning",
    "Large Language Models",
    "Turn-level Adjudicated Reinforcement Learning"
  ],
  "rejected_keywords": [
    "Multi-Modal Learning",
    "Tool Integrated Reasoning"
  ],
  "similarity_scores": {
    "Reinforcement Learning": 0.85,
    "Large Language Models": 0.8,
    "Turn-level Adjudicated Reinforcement Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents

**Korean Title:** 프로세스 감독 강화 학습을 통한 상호작용 멀티모달 도구 사용 에이전트

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning|Reinforcement Learning]], [[keywords/Large Language Models|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Turn-level Adjudicated Reinforcement Learning|Turn-level Adjudicated Reinforcement Learning]]

## 🔗 유사한 논문
- [[THOR Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning]] (85.3% similar)
- [[LLM-I LLMs are Naturally Interleaved Multimodal Creators]] (83.9% similar)
- [[Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (83.5% similar)
- [[AppAgent v2 Advanced Agent for Flexible Mobile Interactions]] (82.9% similar)
- [[AI Agents with Human-Like Collaborative Tools Adaptive Strategies for Enhanced Problem-Solving]] (82.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14480v1 Announce Type: cross 
Abstract: Effective interactive tool use requires agents to master Tool Integrated Reasoning (TIR): a complex process involving multi-turn planning and long-context dialogue management. To train agents for this dynamic process, particularly in multi-modal contexts, we introduce a sandbox environment for reinforcement learning (RL) that supports interleaved speech-text rollouts. Our core strategy, Turn-level Adjudicated Reinforcement Learning (TARL), addresses the challenge of credit assignment in long-horizon tasks by employing a Large Language Model (LLM) as a judge to provide turn-level evaluation. To enhance exploration, we integrate a mixed-task training curriculum with mathematical reasoning problems. This unified approach boosts the task pass rate on the text-based $\tau$-bench by over 6% compared to strong RL baselines. Crucially, we demonstrate our framework's suitability for fine-tuning a multi-modal foundation model for agentic tasks. By training a base multi-modal LLM on interleaved speech-text rollouts, we equip it with tool-use abilities, paving the way for more natural, voice-driven interactive agents.

## 🔍 Abstract (한글 번역)

arXiv:2509.14480v1 발표 유형: 교차  
초록: 효과적인 상호작용 도구 사용은 에이전트가 도구 통합 추론(TIR)을 숙달하는 것을 요구합니다. 이는 다중 턴 계획 및 긴 맥락 대화 관리가 포함된 복잡한 과정입니다. 특히 다중 모달 컨텍스트에서 이 동적인 과정을 위해 에이전트를 훈련시키기 위해, 우리는 강화 학습(RL)을 위한 샌드박스 환경을 도입하여 음성-텍스트 롤아웃을 교차하여 지원합니다. 우리의 핵심 전략인 턴 수준 판결 강화 학습(TARL)은 대규모 언어 모델(LLM)을 판사로 활용하여 턴 수준 평가를 제공함으로써 긴 수평선 작업에서의 크레딧 할당 문제를 해결합니다. 탐색을 강화하기 위해, 우리는 수학적 추론 문제와 함께 혼합 작업 훈련 커리큘럼을 통합합니다. 이 통합 접근 방식은 강력한 RL 기준선과 비교하여 텍스트 기반 $\tau$-벤치에서 작업 통과율을 6% 이상 향상시킵니다. 중요한 것은, 우리는 에이전트 작업을 위한 다중 모달 기초 모델을 미세 조정하는 데 우리의 프레임워크가 적합하다는 것을 입증합니다. 기본 다중 모달 LLM을 음성-텍스트 롤아웃에 대해 훈련함으로써, 우리는 그것에 도구 사용 능력을 부여하여 더 자연스럽고 음성 구동 상호작용 에이전트를 위한 길을 열었습니다.

## 📝 요약

이 논문은 도구 통합 추론(TIR)을 위한 에이전트 훈련을 위해 강화 학습(RL) 샌드박스 환경을 제안합니다. 이 환경은 음성-텍스트 롤아웃을 지원하여 복잡한 계획 및 대화 관리가 가능하도록 합니다. 주요 기여는 Turn-level Adjudicated Reinforcement Learning (TARL) 방법론으로, 대규모 언어 모델(LLM)을 심판으로 활용해 긴 과제에서의 신용 할당 문제를 해결합니다. 또한, 수학적 문제를 포함한 혼합 과제 훈련을 통해 탐색을 강화하여 텍스트 기반 $\tau$-벤치에서 과제 통과율을 6% 이상 향상시켰습니다. 이 프레임워크는 다중 모달 기초 모델을 에이전트 작업에 맞게 미세 조정하는 데 적합하며, 음성-텍스트 롤아웃을 통해 도구 사용 능력을 갖춘 자연스러운 상호작용 에이전트를 개발할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. Tool Integrated Reasoning (TIR)은 다중 턴 계획 및 긴 맥락의 대화 관리를 포함하는 복잡한 과정으로, 효과적인 상호작용 도구 사용을 위해 필수적입니다.

- 2. 강화 학습을 위한 샌드박스 환경을 도입하여 다중 모달 맥락에서의 도구 사용 능력을 훈련합니다.

- 3. Turn-level Adjudicated Reinforcement Learning (TARL)은 긴 수평선 과제에서의 신용 할당 문제를 해결하기 위해 대형 언어 모델(LLM)을 심판으로 활용합니다.

- 4. 혼합 과제 훈련 커리큘럼과 수학적 추론 문제를 통합하여 탐색을 강화하고, 텍스트 기반 $\tau$-벤치에서 과제 통과율을 6% 이상 향상시킵니다.

- 5. 음성-텍스트 롤아웃을 통해 다중 모달 LLM을 훈련하여 자연스럽고 음성 기반의 상호작용 에이전트를 위한 도구 사용 능력을 갖추게 합니다.

---

*Generated on 2025-09-19 14:55:45*