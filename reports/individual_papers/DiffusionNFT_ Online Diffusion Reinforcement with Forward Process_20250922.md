# DiffusionNFT: Online Diffusion Reinforcement with Forward Process

**Korean Title:** DiffusionNFT: 순방향 프로세스를 통한 온라인 확산 강화 학습

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Online Diffusion Reinforcement

## 🔗 유사한 논문
- [[2025-09-22/RLinf_ Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation_20250922|RLinf Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation]] (84.1% similar)
- [[2025-09-18/Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning_20250918|Fast and Fluent Diffusion Language Models via Convolutional Decoding and Rejective Fine-tuning]] (83.9% similar)
- [[2025-09-18/FlightDiffusion_ Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video_20250918|FlightDiffusion Revolutionising Autonomous Drone Training with Diffusion Models Generating FPV Video]] (83.9% similar)
- [[2025-09-19/FlowRL_ Matching Reward Distributions for LLM Reasoning_20250919|FlowRL Matching Reward Distributions for LLM Reasoning]] (83.8% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (82.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16117v1 Announce Type: cross 
Abstract: Online reinforcement learning (RL) has been central to post-training language models, but its extension to diffusion models remains challenging due to intractable likelihoods. Recent works discretize the reverse sampling process to enable GRPO-style training, yet they inherit fundamental drawbacks, including solver restrictions, forward-reverse inconsistency, and complicated integration with classifier-free guidance (CFG). We introduce Diffusion Negative-aware FineTuning (DiffusionNFT), a new online RL paradigm that optimizes diffusion models directly on the forward process via flow matching. DiffusionNFT contrasts positive and negative generations to define an implicit policy improvement direction, naturally incorporating reinforcement signals into the supervised learning objective. This formulation enables training with arbitrary black-box solvers, eliminates the need for likelihood estimation, and requires only clean images rather than sampling trajectories for policy optimization. DiffusionNFT is up to $25\times$ more efficient than FlowGRPO in head-to-head comparisons, while being CFG-free. For instance, DiffusionNFT improves the GenEval score from 0.24 to 0.98 within 1k steps, while FlowGRPO achieves 0.95 with over 5k steps and additional CFG employment. By leveraging multiple reward models, DiffusionNFT significantly boosts the performance of SD3.5-Medium in every benchmark tested.

## 🔍 Abstract (한글 번역)

arXiv:2509.16117v1 발표 유형: 교차  
초록: 온라인 강화 학습(RL)은 사후 훈련 언어 모델에 중심적이었지만, 난해한 가능성 때문에 확산 모델로의 확장은 여전히 도전적입니다. 최근 연구들은 역 샘플링 과정을 이산화하여 GRPO 스타일의 훈련을 가능하게 하지만, 이들은 기본적인 단점들을 상속받습니다. 여기에는 해법 제한, 순방향-역방향 불일치, 그리고 분류기 없는 안내(CFG)와의 복잡한 통합이 포함됩니다. 우리는 확산 부정 인식 미세 조정(DiffusionNFT)을 소개합니다. 이는 흐름 매칭을 통해 순방향 과정에서 확산 모델을 직접 최적화하는 새로운 온라인 RL 패러다임입니다. DiffusionNFT는 긍정적 및 부정적 생성을 대조하여 암묵적인 정책 개선 방향을 정의하고, 강화 신호를 지도 학습 목표에 자연스럽게 통합합니다. 이 공식은 임의의 블랙박스 해법으로 훈련을 가능하게 하고, 가능성 추정을 필요로 하지 않으며, 정책 최적화를 위해 샘플링 경로 대신 깨끗한 이미지만 필요로 합니다. DiffusionNFT는 FlowGRPO와의 직접 비교에서 최대 25배 더 효율적이며, CFG가 필요하지 않습니다. 예를 들어, DiffusionNFT는 1k 단계 내에 GenEval 점수를 0.24에서 0.98로 향상시키는 반면, FlowGRPO는 5k 이상의 단계와 추가적인 CFG 사용으로 0.95를 달성합니다. 여러 보상 모델을 활용하여, DiffusionNFT는 테스트된 모든 벤치마크에서 SD3.5-Medium의 성능을 크게 향상시킵니다.

## 📝 요약

이 논문은 확산 모델에 온라인 강화 학습(RL)을 적용하는 새로운 패러다임인 Diffusion Negative-aware FineTuning(DiffusionNFT)을 제안합니다. 기존 방법들이 갖는 역추론 과정의 제약과 복잡성을 해결하기 위해, DiffusionNFT는 흐름 매칭을 통해 직접 전방 과정을 최적화합니다. 이 방법은 강화 신호를 지도 학습 목표에 자연스럽게 통합하여, 임의의 블랙박스 솔버와 함께 사용할 수 있으며, 확률 추정이 필요 없고 깨끗한 이미지로만 정책 최적화가 가능합니다. DiffusionNFT는 FlowGRPO보다 최대 25배 더 효율적이며, CFG 없이도 높은 성능을 달성합니다. 예를 들어, GenEval 점수를 1,000 스텝 내에 0.24에서 0.98로 향상시켰으며, 이는 FlowGRPO가 5,000 스텝 이상과 추가 CFG 사용 후에야 0.95를 달성한 것과 비교됩니다. 여러 보상 모델을 활용하여, DiffusionNFT는 SD3.5-Medium의 성능을 모든 테스트된 벤치마크에서 크게 향상시켰습니다.

## 🎯 주요 포인트

- 1. DiffusionNFT는 역추적 과정의 불연속성을 해결하여 강화 학습 신호를 지도 학습 목표에 자연스럽게 통합합니다.

- 2. DiffusionNFT는 임의의 블랙박스 솔버와의 통합을 가능하게 하고, 가능도 추정이 필요 없으며, 정책 최적화를 위해 샘플링 경로 대신 깨끗한 이미지만 필요로 합니다.

- 3. DiffusionNFT는 FlowGRPO보다 최대 25배 더 효율적이며, CFG 없이도 높은 성능을 발휘합니다.

- 4. DiffusionNFT는 GenEval 점수를 1k 단계 내에서 0.24에서 0.98로 개선하며, FlowGRPO는 5k 단계 이상과 추가 CFG 사용으로 0.95를 달성합니다.

- 5. 여러 보상 모델을 활용하여 DiffusionNFT는 모든 테스트된 벤치마크에서 SD3.5-Medium의 성능을 크게 향상시킵니다.

---

*Generated on 2025-09-22 14:25:08*