# THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning

**Korean Title:** THOR: 수학적 추론을 위한 강화 학습 기반 도구 통합 계층적 최적화

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Qikai Chang|Qikai Chang]] [[authors/Zhenrong Zhang|Zhenrong Zhang]] [[authors/Pengfei Hu|Pengfei Hu]] [[authors/Jiefeng Ma|Jiefeng Ma]] [[authors/Yicheng Pan|Yicheng Pan]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Hierarchical Optimization

## 🔗 유사한 논문
- [[Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (85.5% similar)
- [[Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents_20250919|Process-Supervised Reinforcement Learning for Interactive Multimodal Tool-Use Agents]] (84.9% similar)
- [[WebCoT_ Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback_20250919|WebCoT Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (83.5% similar)
- [[Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models Multi-Agent Consensus Alignment]] (82.9% similar)
- [[Understanding the Thinking Process of Reasoning Models_ A Perspective from Schoenfeld's Episode Theory_20250919|Understanding the Thinking Process of Reasoning Models A Perspective from Schoenfeld's Episode Theory]] (82.7% similar)

## 📋 저자 정보

**Authors:** Qikai Chang, Zhenrong Zhang, Pengfei Hu, Jiefeng Ma, Yicheng Pan, Jianshu Zhang, Jun Du, Quan Liu, Jianqing Gao

## 📄 Abstract (원문)

Large Language Models (LLMs) have made remarkable progress in mathematical
reasoning, but still continue to struggle with high-precision tasks like
numerical computation and formal symbolic manipulation. Integrating external
tools has emerged as a promising approach to bridge this gap. Despite recent
advances, existing methods struggle with three key challenges: constructing
tool-integrated reasoning data, performing fine-grained optimization, and
enhancing inference. To overcome these limitations, we propose THOR
(Tool-Integrated Hierarchical Optimization via RL). First, we introduce TIRGen,
a multi-agent actor-critic-based pipeline for constructing high-quality
datasets of tool-integrated reasoning paths, aligning with the policy and
generalizing well across diverse models. Second, to perform fine-grained
hierarchical optimization, we introduce an RL strategy that jointly optimizes
for both trajectory-level problem solving and step-level code generation. This
is motivated by our key insight that the success of an intermediate tool call
is a strong predictor of the final answer's correctness. Finally, THOR
incorporates a self-correction mechanism that leverages immediate tool feedback
to dynamically revise erroneous reasoning paths during inference. Our approach
demonstrates strong generalization across diverse models, performing
effectively in both reasoning and non-reasoning models. It further achieves
state-of-the-art performance for models of a similar scale on multiple
mathematical benchmarks, while also delivering consistent improvements on code
benchmarks. Our code will be publicly available at
https://github.com/JingMog/THOR.

## 🔍 Abstract (한글 번역)

대형 언어 모델(LLMs)은 수학적 추론에서 놀라운 진전을 이루었지만, 여전히 수치 계산 및 형식적 기호 조작과 같은 고정밀 작업에서는 어려움을 겪고 있습니다. 외부 도구를 통합하는 것은 이러한 격차를 해소하기 위한 유망한 접근 방식으로 부상하고 있습니다. 최근의 발전에도 불구하고 기존 방법들은 도구 통합 추론 데이터를 구축하고, 세밀한 최적화를 수행하며, 추론을 향상시키는 세 가지 주요 과제에 직면하고 있습니다. 이러한 한계를 극복하기 위해 우리는 THOR(Tool-Integrated Hierarchical Optimization via RL)을 제안합니다. 먼저, 우리는 정책과 정렬되고 다양한 모델에 걸쳐 잘 일반화되는 도구 통합 추론 경로의 고품질 데이터셋을 구축하기 위한 다중 에이전트 액터-크리틱 기반 파이프라인인 TIRGen을 소개합니다. 둘째, 세밀한 계층적 최적화를 수행하기 위해, 우리는 궤적 수준의 문제 해결과 단계 수준의 코드 생성 모두를 공동으로 최적화하는 강화 학습(RL) 전략을 도입합니다. 이는 중간 도구 호출의 성공이 최종 답의 정확성을 강력하게 예측한다는 우리의 핵심 통찰에 의해 동기 부여되었습니다. 마지막으로, THOR는 추론 중에 잘못된 추론 경로를 동적으로 수정하기 위해 즉각적인 도구 피드백을 활용하는 자기 수정 메커니즘을 통합합니다. 우리의 접근 방식은 다양한 모델에 걸쳐 강력한 일반화를 보여주며, 추론 및 비추론 모델 모두에서 효과적으로 작동합니다. 또한 여러 수학적 벤치마크에서 유사한 규모의 모델에 대해 최첨단 성능을 달성하며, 코드 벤치마크에서도 일관된 개선을 제공합니다. 우리의 코드는 https://github.com/JingMog/THOR에서 공개적으로 제공될 예정입니다.

## 📝 요약

대형 언어 모델(LLM)은 수학적 추론에서 상당한 발전을 이루었지만, 여전히 수치 계산 및 형식적 기호 조작과 같은 고정밀 작업에서는 어려움을 겪고 있습니다. 이를 해결하기 위해 외부 도구 통합이 유망한 접근법으로 부상하고 있습니다. 그러나 기존 방법들은 도구 통합 추론 데이터 구성, 세밀한 최적화 수행, 추론 향상에서 어려움을 겪고 있습니다. 이를 극복하기 위해, 우리는 THOR(Tool-Integrated Hierarchical Optimization via RL)을 제안합니다. 먼저, TIRGen이라는 멀티 에이전트 액터-크리틱 기반 파이프라인을 통해 다양한 모델에서 일반화가 잘 되는 도구 통합 추론 경로의 고품질 데이터셋을 구축합니다. 둘째, 세밀한 계층적 최적화를 위해 문제 해결과 코드 생성의 궤적 수준을 공동으로 최적화하는 강화 학습 전략을 도입합니다. 마지막으로, THOR는 즉각적인 도구 피드백을 활용해 추론 중 오류를 동적으로 수정하는 자기 수정 메커니즘을 포함합니다. 우리의 접근법은 다양한 모델에서 강력한 일반화 성능을 보이며, 여러 수학적 벤치마크에서 최첨단 성능을 달성하고 코드 벤치마크에서도 일관된 개선을 제공합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 수학적 추론에서 상당한 진전을 이루었지만, 여전히 수치 계산 및 형식적 기호 조작과 같은 고정밀 작업에서는 어려움을 겪고 있습니다.

- 2. 외부 도구 통합은 이러한 격차를 해소하기 위한 유망한 접근 방식으로 부상하고 있습니다.

- 3. THOR는 RL을 통한 도구 통합 계층 최적화를 제안하여, 도구 통합 추론 경로의 고품질 데이터셋을 구축하고, 세밀한 계층 최적화를 수행하며, 추론 중 오류를 동적으로 수정하는 메커니즘을 포함합니다.

- 4. THOR는 다양한 모델에서 강력한 일반화 성능을 보여주며, 수학적 벤치마크와 코드 벤치마크에서 최첨단 성능을 달성합니다.

- 5. THOR의 코드는 https://github.com/JingMog/THOR에서 공개될 예정입니다.

---

*Generated on 2025-09-20 09:35:26*