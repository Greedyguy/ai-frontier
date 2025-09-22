# Entropy-Regularized Process Reward Model

**Korean Title:** 엔트로피 정규화된 프로세스 보상 모델

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Process Rewards|Process Rewards]] [[keywords/specific/KL-regularized Markov Decision Processes|KL-regularized Markov Decision Processes]] [[keywords/broad/Large Language Models|Large Language Models]] [[keywords/broad/Reinforcement Learning|Reinforcement Learning]] [[keywords/unique/Entropy-Regularized Process Reward Model|Entropy-Regularized Process Reward Model]] [[categories/cs.LG|cs.LG]] [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM: Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (87.9% similar) [[2025-09-22/MT-RewardTree_ A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling_20250922|MT-RewardTree: A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling]] (87.9% similar) [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (87.0% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Process Rewards
**🔗 Specific Connectable**: KL-regularized Markov Decision Processes
**🔬 Broad Technical**: Large Language Models, Reinforcement Learning
**⭐ Unique Technical**: Entropy-Regularized Process Reward Model
## 🔗 유사한 논문
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (87.9% similar)
- [[2025-09-22/MT-RewardTree_ A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling_20250922|MT-RewardTree A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling]] (87.9% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (87.0% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1 Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (86.0% similar)
- [[2025-09-22/Reward Hacking Mitigation using Verifiable Composite Rewards_20250922|Reward Hacking Mitigation using Verifiable Composite Rewards]] (85.8% similar)


**ArXiv ID**: [2412.11006](https://arxiv.org/abs/2412.11006)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2412.11006.pdf)


**ArXiv ID**: [2412.11006](https://arxiv.org/abs/2412.11006)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2412.11006.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Entropy-Regularization
**🔗 Specific Connectable**: Markov Decision Processes
**⭐ Unique Technical**: Entropy-Regularized Process Reward Model
**🔬 Broad Technical**: Reinforcement Learning, Large Language Models

## 🏷️ 추출된 키워드



`Large Language Models` • 

`Reinforcement Learning` • 

`KL-regularized Markov Decision Processes` • 

`Entropy-Regularized Process Reward Model` • 

`Process Rewards`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.11006v2 Announce Type: replace 
Abstract: Large language models (LLMs) have shown promise in performing complex multi-step reasoning, yet they continue to struggle with mathematical reasoning, often making systematic errors. A promising solution is reinforcement learning (RL) guided by reward models, particularly those focusing on process rewards, which score each intermediate step rather than solely evaluating the final outcome. This approach is more effective at guiding policy models towards correct reasoning trajectories. In this work, we propose an entropy-regularized process reward model (ER-PRM) that integrates KL-regularized Markov Decision Processes (MDP) to balance policy optimization with the need to prevent the policy from shifting too far from its initial distribution. We derive a novel reward construction method based on the theoretical results. Our theoretical analysis shows that we could derive the optimal reward model from the initial policy sampling. Our empirical experiments on the MATH and GSM8K benchmarks demonstrate that ER-PRM consistently outperforms existing process reward models, achieving 1% improvement on GSM8K and 2-3% improvement on MATH under best-of-N evaluation, and more than 1% improvement under RLHF. These results highlight the efficacy of entropy-regularization in enhancing LLMs' reasoning capabilities.

## 🔍 Abstract (한글 번역)

arXiv:2412.11006v2 발표 유형: 교체  
초록: 대형 언어 모델(LLM)은 복잡한 다단계 추론을 수행하는 데 있어 가능성을 보여주었지만, 여전히 수학적 추론에서는 체계적인 오류를 자주 범하고 있습니다. 유망한 해결책은 보상 모델에 의해 안내되는 강화 학습(RL)이며, 특히 최종 결과만 평가하는 것이 아니라 각 중간 단계를 점수화하는 과정 보상에 중점을 둔 모델입니다. 이 접근법은 정책 모델이 올바른 추론 경로로 나아가도록 더 효과적으로 안내합니다. 본 연구에서는 KL-정규화 마르코프 결정 과정(MDP)을 통합하여 정책 최적화와 초기 분포에서 정책이 너무 멀리 이동하지 않도록 하는 필요성 간의 균형을 맞추는 엔트로피 정규화 과정 보상 모델(ER-PRM)을 제안합니다. 우리는 이론적 결과를 바탕으로 새로운 보상 구성 방법을 도출합니다. 우리의 이론적 분석은 초기 정책 샘플링에서 최적의 보상 모델을 도출할 수 있음을 보여줍니다. MATH와 GSM8K 벤치마크에 대한 실험 결과, ER-PRM은 기존의 과정 보상 모델을 지속적으로 능가하며, GSM8K에서는 1%, MATH에서는 최선의 N 평가에서 2-3%의 개선을 달성하고, RLHF에서는 1% 이상의 개선을 달성했습니다. 이러한 결과는 LLM의 추론 능력을 향상시키는 데 있어 엔트로피 정규화의 효과를 강조합니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 수학적 추론에서 체계적인 오류를 범하는 문제를 해결하기 위해 강화 학습(RL)과 보상 모델을 활용하는 방법을 제안합니다. 특히, 중간 단계마다 점수를 부여하는 프로세스 보상 모델이 효과적임을 강조합니다. 저자들은 KL-정규화 마르코프 결정 과정(MDP)을 통합한 엔트로피 정규화 프로세스 보상 모델(ER-PRM)을 제안하여 정책 최적화와 초기 분포로부터의 과도한 변화 방지를 균형 있게 조절합니다. 이론적 분석을 통해 최적의 보상 모델을 도출할 수 있음을 보였으며, MATH와 GSM8K 벤치마크 실험에서 ER-PRM이 기존 모델보다 우수한 성능을 보였습니다. 이는 LLM의 추론 능력을 향상시키는 데 엔트로피 정규화가 효과적임을 시사합니다.

## 🎯 주요 포인트


- 1. 대형 언어 모델(LLMs)은 복잡한 다단계 추론에서 잠재력을 보이지만, 여전히 수학적 추론에서 체계적인 오류를 범한다.

- 2. 보상 모델에 의해 안내되는 강화 학습(RL)이 유망한 해결책으로, 특히 중간 단계마다 점수를 매기는 프로세스 보상에 중점을 둔다.

- 3. 본 연구에서는 KL-정규화 마르코프 결정 과정(MDP)을 통합한 엔트로피 정규화 프로세스 보상 모델(ER-PRM)을 제안한다.

- 4. ER-PRM은 MATH와 GSM8K 벤치마크에서 기존의 프로세스 보상 모델보다 우수한 성능을 보이며, GSM8K에서 1%, MATH에서 2-3%의 개선을 달성했다.

- 5. 엔트로피 정규화가 LLM의 추론 능력을 향상시키는 데 효과적임을 실험 결과가 강조한다.


---

*Generated on 2025-09-22 15:53:25*