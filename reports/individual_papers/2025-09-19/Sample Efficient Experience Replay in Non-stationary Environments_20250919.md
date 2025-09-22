
# Sample Efficient Experience Replay in Non-stationary Environments

**Korean Title:** 비정상 환경에서의 샘플 효율적 경험 재생

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Adaptive Experience Replay

## 🔗 유사한 논문
- [[Efficient Last-Iterate Convergence in Regret Minimization via Adaptive Reward Transformation]] (78.8% similar)
- [[Self-Guided_Function_Calling_in_Large_Language_Models_via_Stepwise_Experience_Recall_20250918|Self-Guided Function Calling in Large Language Models via Stepwise Experience Recall]] (78.4% similar)
- [[MIMIC-D Multi-modal Imitation for MultI-agent Coordination with Decentralized Diffusion Policies]] (78.3% similar)
- [[DECAMP Towards Scene-Consistent Multi-Agent Motion Prediction with Disentangled Context-Aware Pre-Training]] (77.9% similar)
- [[Video-Language Critic Transferable Reward Functions for Language-Conditioned Robotics]] (77.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15032v1 Announce Type: cross 
Abstract: Reinforcement learning (RL) in non-stationary environments is challenging, as changing dynamics and rewards quickly make past experiences outdated. Traditional experience replay (ER) methods, especially those using TD-error prioritization, struggle to distinguish between changes caused by the agent's policy and those from the environment, resulting in inefficient learning under dynamic conditions. To address this challenge, we propose the Discrepancy of Environment Dynamics (DoE), a metric that isolates the effects of environment shifts on value functions. Building on this, we introduce Discrepancy of Environment Prioritized Experience Replay (DEER), an adaptive ER framework that prioritizes transitions based on both policy updates and environmental changes. DEER uses a binary classifier to detect environment changes and applies distinct prioritization strategies before and after each shift, enabling more sample-efficient learning. Experiments on four non-stationary benchmarks demonstrate that DEER further improves the performance of off-policy algorithms by 11.54 percent compared to the best-performing state-of-the-art ER methods.

## 🔍 Abstract (한글 번역)

arXiv:2509.15032v1 발표 유형: 교차  
초록: 비정상 환경에서의 강화 학습(RL)은 도전적입니다. 변화하는 동태와 보상은 과거의 경험을 빠르게 구시화하기 때문입니다. 전통적인 경험 재생(ER) 방법, 특히 TD-오류 우선순위를 사용하는 방법은 에이전트의 정책에 의해 발생한 변화와 환경으로부터의 변화를 구별하는 데 어려움을 겪으며, 이는 동적 조건 하에서 비효율적인 학습을 초래합니다. 이 문제를 해결하기 위해 우리는 가치 함수에 대한 환경 변화의 영향을 분리하는 척도인 환경 동태 불일치(DoE)를 제안합니다. 이를 바탕으로, 우리는 정책 업데이트와 환경 변화를 모두 기반으로 전이를 우선시하는 적응형 ER 프레임워크인 환경 우선순위 경험 재생(DEER)을 소개합니다. DEER은 환경 변화를 감지하기 위해 이진 분류기를 사용하고, 각 변화 전후에 구별된 우선순위 전략을 적용하여 더 샘플 효율적인 학습을 가능하게 합니다. 네 가지 비정상 벤치마크에 대한 실험은 DEER이 최신 ER 방법 중 가장 성능이 좋은 방법에 비해 오프 폴리시 알고리즘의 성능을 11.54% 향상시킴을 보여줍니다.

## 📝 요약

비정상적인 환경에서의 강화 학습은 변화하는 동적 및 보상 체계로 인해 과거 경험이 빠르게 무용지물이 되어 도전적입니다. 기존의 경험 재생(ER) 방법, 특히 TD-오류 우선순위화 기법은 에이전트의 정책 변화와 환경 변화의 구분이 어려워 비효율적인 학습을 초래합니다. 이를 해결하기 위해, 우리는 환경 동적 불일치(DoE)라는 메트릭을 제안하여 환경 변화가 가치 함수에 미치는 영향을 분리합니다. 이를 바탕으로, 정책 업데이트와 환경 변화를 모두 고려한 우선순위 경험 재생 프레임워크인 DEER를 소개합니다. DEER는 이진 분류기를 사용해 환경 변화를 감지하고, 변화 전후에 다른 우선순위 전략을 적용하여 샘플 효율성을 높입니다. 네 가지 비정상적 벤치마크 실험에서 DEER는 최신 ER 방법 대비 성능을 11.54% 향상시켰습니다.

## 🎯 주요 포인트

- 1. 비정상 환경에서의 강화 학습은 변화하는 동적 및 보상으로 인해 과거 경험이 빠르게 무용지물이 되어 도전적입니다.

- 2. 전통적인 경험 재생 방법은 에이전트의 정책 변화와 환경 변화의 구분이 어려워 비효율적인 학습을 초래합니다.

- 3. 우리는 환경 변화가 가치 함수에 미치는 영향을 분리하는 환경 동적 불일치(DoE) 메트릭을 제안합니다.

- 4. DEER은 정책 업데이트와 환경 변화를 기반으로 전환을 우선시하는 적응형 경험 재생 프레임워크입니다.

- 5. DEER은 비정상적인 벤치마크에서 오프 폴리시 알고리즘의 성능을 최첨단 경험 재생 방법에 비해 11.54% 향상시킵니다.

---

*Generated on 2025-09-19 15:04:13*