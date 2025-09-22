# Foundation Models as World Models: A Foundational Study in Text-Based GridWorlds

**Korean Title:** 텍스트 기반 그리드월드에서의 기초 연구: 세계 모델로서의 기초 모델

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Foundation Agents

## 🔗 유사한 논문
- [[2025-09-18/Self-Improving Embodied Foundation Models_20250918|Self-Improving Embodied Foundation Models]] (82.5% similar)
- [[2025-09-19/(P)rior(D)yna(F)low_ A Priori Dynamic Workflow Construction via Multi-Agent Collaboration_20250919|(P)rior(D)yna(F)low A Priori Dynamic Workflow Construction via Multi-Agent Collaboration]] (82.2% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (81.9% similar)
- [[2025-09-19/WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (81.5% similar)
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (81.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15915v1 Announce Type: cross 
Abstract: While reinforcement learning from scratch has shown impressive results in solving sequential decision-making tasks with efficient simulators, real-world applications with expensive interactions require more sample-efficient agents. Foundation models (FMs) are natural candidates to improve sample efficiency as they possess broad knowledge and reasoning capabilities, but it is yet unclear how to effectively integrate them into the reinforcement learning framework. In this paper, we anticipate and, most importantly, evaluate two promising strategies. First, we consider the use of foundation world models (FWMs) that exploit the prior knowledge of FMs to enable training and evaluating agents with simulated interactions. Second, we consider the use of foundation agents (FAs) that exploit the reasoning capabilities of FMs for decision-making. We evaluate both approaches empirically in a family of grid-world environments that are suitable for the current generation of large language models (LLMs). Our results suggest that improvements in LLMs already translate into better FWMs and FAs; that FAs based on current LLMs can already provide excellent policies for sufficiently simple environments; and that the coupling of FWMs and reinforcement learning agents is highly promising for more complex settings with partial observability and stochastic elements.

## 🔍 Abstract (한글 번역)

arXiv:2509.15915v1 발표 유형: 교차  
초록: 강화 학습이 효율적인 시뮬레이터를 사용하여 순차적 의사 결정 작업을 해결하는 데 인상적인 결과를 보여주었지만, 상호작용 비용이 높은 실제 응용에서는 더 샘플 효율적인 에이전트가 필요합니다. 기초 모델(FMs)은 광범위한 지식과 추론 능력을 갖추고 있어 샘플 효율성을 향상시킬 수 있는 자연스러운 후보이지만, 이를 강화 학습 프레임워크에 효과적으로 통합하는 방법은 아직 명확하지 않습니다. 본 논문에서는 두 가지 유망한 전략을 예측하고, 가장 중요하게는 평가합니다. 첫째, FMs의 사전 지식을 활용하여 시뮬레이션된 상호작용을 통해 에이전트를 훈련하고 평가할 수 있는 기초 세계 모델(FWMs)의 사용을 고려합니다. 둘째, FMs의 추론 능력을 활용하여 의사 결정을 내리는 기초 에이전트(FAs)의 사용을 고려합니다. 우리는 현재 대규모 언어 모델(LLMs)에 적합한 그리드 월드 환경의 가족에서 두 접근 방식을 실증적으로 평가합니다. 우리의 결과는 LLMs의 개선이 이미 더 나은 FWMs와 FAs로 이어진다는 것을 시사하며, 현재 LLMs 기반의 FAs가 충분히 단순한 환경에서는 이미 우수한 정책을 제공할 수 있음을 보여줍니다. 또한 FWMs와 강화 학습 에이전트의 결합이 부분 관찰성과 확률적 요소를 가진 더 복잡한 설정에 대해 매우 유망하다는 것을 시사합니다.

## 📝 요약

이 논문은 강화 학습의 샘플 효율성을 높이기 위해 기초 모델(FMs)을 활용하는 두 가지 전략을 평가합니다. 첫째, 기초 세계 모델(FWMs)을 사용하여 FMs의 사전 지식을 활용해 시뮬레이션 상호작용을 통해 에이전트를 훈련 및 평가하는 방법을 제안합니다. 둘째, FMs의 추론 능력을 활용한 기초 에이전트(FAs)를 통한 의사결정 방식을 고려합니다. 그리드 월드 환경에서의 실험 결과, 현재의 대형 언어 모델(LLMs)이 FWMs와 FAs의 성능을 향상시킬 수 있으며, 간단한 환경에서는 FAs가 우수한 정책을 제공할 수 있음을 보여줍니다. 또한, FWMs와 강화 학습 에이전트의 결합이 부분 관찰 및 확률적 요소가 있는 복잡한 환경에서 유망하다는 것을 시사합니다.

## 🎯 주요 포인트

- 1. 강화 학습은 효율적인 시뮬레이터를 통해 순차적 의사 결정 작업을 해결하는 데 뛰어난 결과를 보여주었지만, 실제 응용에서는 더 많은 샘플 효율성을 요구합니다.

- 2. 파운데이션 모델(FM)은 광범위한 지식과 추론 능력을 가지고 있어 샘플 효율성을 개선할 수 있는 자연스러운 후보입니다.

- 3. 본 연구에서는 파운데이션 월드 모델(FWM)과 파운데이션 에이전트(FA)의 두 가지 전략을 평가하였습니다.

- 4. 그리드 월드 환경에서의 실험 결과, 현재의 대형 언어 모델(LLM)을 기반으로 한 FA는 간단한 환경에서 우수한 정책을 제공할 수 있음을 보여줍니다.

- 5. FWM과 강화 학습 에이전트의 결합은 부분 관찰성과 확률적 요소가 있는 복잡한 환경에서 매우 유망합니다.

---

*Generated on 2025-09-22 14:17:00*