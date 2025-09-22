# MT-RewardTree: A Comprehensive Framework for Advancing LLM-Based Machine Translation via Reward Modeling

**Korean Title:** MT-RewardTree: 보상 모델링을 통한 대형 언어 모델 기반 기계 번역 발전을 위한 종합 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Token-level Supervision

## 🔗 유사한 논문
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (86.6% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (83.0% similar)
- [[2025-09-19/PMPO_ Probabilistic Metric Prompt Optimization for Small and Large Language Models_20250919|PMPO Probabilistic Metric Prompt Optimization for Small and Large Language Models]] (82.8% similar)
- [[2025-09-22/Reward Hacking Mitigation using Verifiable Composite Rewards_20250922|Reward Hacking Mitigation using Verifiable Composite Rewards]] (82.3% similar)
- [[2025-09-19/Zero-Shot LLMs in Human-in-the-Loop RL_ Replacing Human Feedback for Reward Shaping_20250919|Zero-Shot LLMs in Human-in-the-Loop RL Replacing Human Feedback for Reward Shaping]] (81.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.12123v2 Announce Type: replace-cross 
Abstract: Process reward models (PRMs) have shown success in complex reasoning tasks for large language models (LLMs). However, their application to machine translation (MT) remains underexplored due to the lack of systematic methodologies and evaluation benchmarks. To address this gap, we introduce \textbf{MT-RewardTree}, a comprehensive framework for constructing, evaluating, and deploying process reward models in MT. Unlike traditional vanilla preference pair construction, we propose a novel method for automatically generating token-level preference pairs using approximate Monte Carlo Tree Search (MCTS), which mitigates the prohibitive cost of human annotation for fine-grained steps. Then, we establish the first MT-specific reward model benchmark and provide a systematic comparison of different reward modeling architectures, revealing that token-level supervision effectively captures fine-grained preferences. Experimental results demonstrate that our MT-PRM-Qwen-2.5-3B achieves state-of-the-art performance in both token-level and sequence-level evaluation given the same input prefix. Furthermore, we showcase practical applications where PRMs enable test-time alignment for LLMs without additional alignment training and significantly improve performance in hypothesis ensembling. Our work provides valuable insights into the role of reward models in MT research. Our code and data are released in \href{https://sabijun.github.io/MT_RewardTreePage/}{https://sabijun.github.io/MT\_RewardTreePage}.

## 🔍 Abstract (한글 번역)

arXiv:2503.12123v2 발표 유형: 교차 대체  
초록: 프로세스 보상 모델(PRMs)은 대형 언어 모델(LLMs)의 복잡한 추론 작업에서 성공을 보여주었습니다. 그러나 체계적인 방법론과 평가 기준의 부족으로 인해 기계 번역(MT) 분야에서의 적용은 아직 충분히 탐구되지 않았습니다. 이러한 격차를 해소하기 위해, 우리는 MT에서 프로세스 보상 모델을 구축, 평가 및 배포하기 위한 포괄적인 프레임워크인 \textbf{MT-RewardTree}를 소개합니다. 전통적인 기본 선호 쌍 구성과 달리, 우리는 근사 몬테카를로 트리 탐색(MCTS)을 사용하여 토큰 수준의 선호 쌍을 자동으로 생성하는 새로운 방법을 제안하여 세부 단계에 대한 인간 주석의 과도한 비용을 완화합니다. 그런 다음, 우리는 최초의 MT 전용 보상 모델 벤치마크를 설정하고 다양한 보상 모델링 아키텍처를 체계적으로 비교하여 토큰 수준의 감독이 세부적인 선호를 효과적으로 포착함을 밝혀냅니다. 실험 결과, 우리의 MT-PRM-Qwen-2.5-3B는 동일한 입력 접두어를 주었을 때 토큰 수준 및 시퀀스 수준 평가에서 최첨단 성능을 달성함을 보여줍니다. 또한, PRMs가 추가적인 정렬 훈련 없이 LLMs에 대한 테스트 시간 정렬을 가능하게 하고 가설 앙상블에서 성능을 크게 향상시키는 실용적인 응용 사례를 제시합니다. 우리의 연구는 MT 연구에서 보상 모델의 역할에 대한 귀중한 통찰력을 제공합니다. 우리의 코드와 데이터는 \href{https://sabijun.github.io/MT_RewardTreePage/}{https://sabijun.github.io/MT\_RewardTreePage}에서 공개됩니다.

## 📝 요약

이 논문은 기계 번역(MT)에서 프로세스 보상 모델(PRM)의 활용을 탐구하며, MT-RewardTree라는 프레임워크를 제안합니다. 이 프레임워크는 토큰 수준의 선호 쌍을 자동 생성하는 새로운 방법론을 도입하여 인간 주석의 비용을 줄입니다. 또한, MT에 특화된 보상 모델 벤치마크를 구축하고 다양한 보상 모델 아키텍처를 비교하여 토큰 수준의 감독이 세밀한 선호를 효과적으로 포착함을 보여줍니다. 실험 결과, 제안된 MT-PRM-Qwen-2.5-3B 모델이 최첨단 성능을 달성했으며, PRM이 추가적인 정렬 훈련 없이 테스트 시 정렬을 가능하게 하고 가설 앙상블링 성능을 크게 향상시킴을 입증합니다. 이 연구는 MT 연구에서 보상 모델의 역할에 대한 중요한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. MT-RewardTree는 기계 번역에서 프로세스 보상 모델(PRM)을 구축, 평가 및 배포하기 위한 포괄적인 프레임워크를 제공합니다.

- 2. 새로운 토큰 수준의 선호 쌍 생성 방법을 제안하여 인간 주석의 높은 비용 문제를 해결합니다.

- 3. MT-RewardTree는 최초의 기계 번역 전용 보상 모델 벤치마크를 수립하고 다양한 보상 모델링 아키텍처를 체계적으로 비교합니다.

- 4. 실험 결과, MT-PRM-Qwen-2.5-3B 모델이 토큰 및 시퀀스 수준 평가에서 최첨단 성능을 달성함을 보여줍니다.

- 5. PRM은 추가적인 정렬 훈련 없이 테스트 시 LLM의 정렬을 가능하게 하고 가설 앙상블링에서 성능을 크게 향상시킵니다.

---

*Generated on 2025-09-22 14:44:32*