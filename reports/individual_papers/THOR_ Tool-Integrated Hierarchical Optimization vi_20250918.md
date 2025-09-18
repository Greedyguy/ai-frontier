
# THOR: Tool-Integrated Hierarchical Optimization via RL for Mathematical Reasoning

**Korean Title:** THOR: 수학적 추론을 위한 RL을 통한 도구 통합 계층 최적화

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Multi-agent RAG|Multi-agent RAG]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/RL|RL]] [[keywords/specific/Actor-Critic|Actor-Critic]] [[keywords/unique/THOR|THOR]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Hierarchical Optimization
**🔬 Broad Technical**: Large Language Models, RL
**🔗 Specific Connectable**: Multi-agent Actor-Critic
**⭐ Unique Technical**: THOR

**ArXiv ID**: [2509.13761](https://arxiv.org/abs/2509.13761)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.13761.pdf)


## 🏷️ 추출된 키워드



`Large Language Models` • 

`RL` • 

`Multi-agent Actor-Critic` • 

`THOR` • 

`Tool-Integrated Hierarchical Optimization`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13761v1 Announce Type: new 
Abstract: Large Language Models (LLMs) have made remarkable progress in mathematical reasoning, but still continue to struggle with high-precision tasks like numerical computation and formal symbolic manipulation. Integrating external tools has emerged as a promising approach to bridge this gap. Despite recent advances, existing methods struggle with three key challenges: constructing tool-integrated reasoning data, performing fine-grained optimization, and enhancing inference. To overcome these limitations, we propose THOR (Tool-Integrated Hierarchical Optimization via RL). First, we introduce TIRGen, a multi-agent actor-critic-based pipeline for constructing high-quality datasets of tool-integrated reasoning paths, aligning with the policy and generalizing well across diverse models. Second, to perform fine-grained hierarchical optimization, we introduce an RL strategy that jointly optimizes for both trajectory-level problem solving and step-level code generation. This is motivated by our key insight that the success of an intermediate tool call is a strong predictor of the final answer's correctness. Finally, THOR incorporates a self-correction mechanism that leverages immediate tool feedback to dynamically revise erroneous reasoning paths during inference. Our approach demonstrates strong generalization across diverse models, performing effectively in both reasoning and non-reasoning models. It further achieves state-of-the-art performance for models of a similar scale on multiple mathematical benchmarks, while also delivering consistent improvements on code benchmarks. Our code will be publicly available at https://github.com/JingMog/THOR.

## 🔍 Abstract (한글 번역)

arXiv:2509.13761v1 발표 유형: 새로운
요약: 대규모 언어 모델(LLMs)은 수학적 추론에서 놀라운 진전을 이루었지만, 여전히 숫자 계산 및 형식적인 기호 조작과 같은 고정밀 작업에는 여전히 어려움을 겪고 있습니다. 외부 도구를 통합하는 것이 이 간극을 메우는 유망한 접근법으로 떠오르고 있습니다. 최근의 발전에도 불구하고, 기존 방법은 세 가지 주요 도전에 직면하고 있습니다: 도구 통합 추론 데이터의 구축, 세밀한 최적화 수행, 추론 강화. 이러한 제한을 극복하기 위해 우리는 THOR(Tool-Integrated Hierarchical Optimization via RL)를 제안합니다. 먼저, 우리는 고품질의 도구 통합 추론 경로 데이터셋을 구축하기 위한 다중 에이전트 액터-크리틱 기반 파이프라인인 TIRGen을 소개합니다. 이는 정책과 잘 일반화되는 다양한 모델에 맞추어집니다. 둘째, 세밀한 계층적 최적화를 수행하기 위해, 우리는 문제 해결의 경로 수준과 코드 생성의 단계 수준을 모두 최적화하는 RL 전략을 소개합니다. 이는 중간 도구 호출의 성공이 최종 답의 정확성의 강력한 예측자임을 감안한 것입니다. 마지막으로, THOR는 추론 중에 오류가 있는 추론 경로를 동적으로 수정하기 위해 즉각적인 도구 피드백을 활용하는 자가 교정 메커니즘을 통합합니다. 우리의 접근법은 다양한 모델에 걸쳐 강력한 일반화를 보여주며, 추론 및 비추론 모델 모두에서 효과적으로 수행됩니다. 또한, 수학적 벤치마크에서 유사 규모의 모델에 대해 최첨단의 성능을 달성하며, 코드 벤치마크에서도 일관된 개선을 이루어냅니다. 우리의 코드는 https://github.com/JingMog/THOR에서 공개적으로 이용 가능할 것입니다.

## 📝 요약

한국어 요약:
최근 대형 언어 모델(Large Language Models, LLMs)은 수학적 추론에서 뛰어난 성과를 보이지만, 숫자 계산 및 형식적 기호 조작과 같은 고정밀 작업에서 여전히 어려움을 겪고 있다. 외부 도구 통합은 이 간극을 메우는 유망한 접근법으로 부상하고 있다. 본 연구에서는 THOR(Tool-Integrated Hierarchical Optimization via RL)를 제안하여 이러한 한계를 극복한다. 우리는 TIRGen을 소개하여 고품질의 도구 통합 추론 경로 데이터셋을 구축하고, 강화학습을 통해 계층적 최적화를 수행하며, 추론 중에 오류 수정 메커니즘을 도입하여 다양한 모델에 강력한 일반화 능력을 보여준다. 이를 통해 수학적 벤치마크에서 최첨단 성능을 달성하고 코드 벤치마크에서도 일관된 개선을 이루어낸다.

## 🎯 주요 포인트


- 1. 대형 언어 모델은 수학적 추론에서 놀라운 진전을 이루었지만 숫자 계산 및 형식적 상징 조작과 같은 고정밀 작업에서 여전히 어려움을 겪고 있다.

- 2. THOR은 외부 도구를 통합하여 이 간극을 메우는 유망한 방법으로 제안되었으며, 다양한 모델에 대해 잘 일반화되는 고품질 데이터셋을 구축하기 위한 TIRGen을 소개한다.

- 3. THOR은 중간 도구 호출의 성공이 최종 답의 정확성에 강력한 예측자임을 감안하여 문제 해결 및 코드 생성을 동시에 최적화하는 RL 전략을 도입한다.


---

*Generated on 2025-09-18 16:16:13*