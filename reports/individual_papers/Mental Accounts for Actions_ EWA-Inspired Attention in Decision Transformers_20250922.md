# Mental Accounts for Actions: EWA-Inspired Attention in Decision Transformers

**Korean Title:** 행동에 대한 정신적 계좌: 결정 변환기에서 EWA 영감을 받은 주의력

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Entropy-Regularized Training

## 🔗 유사한 논문
- [[2025-09-17/Large Language Model-Empowered Decision Transformer for UAV-Enabled Data Collection_20250917|Large Language Model-Empowered Decision Transformer for UAV-Enabled Data Collection]] (80.7% similar)
- [[2025-09-22/Attention Schema-based Attention Control (ASAC)_ A Cognitive-Inspired Approach for Attention Management in Transformers_20250922|Attention Schema-based Attention Control (ASAC) A Cognitive-Inspired Approach for Attention Management in Transformers]] (80.3% similar)
- [[2025-09-22/AttentionDrop_ A Novel Regularization Method for Transformer Models_20250922|AttentionDrop A Novel Regularization Method for Transformer Models]] (80.1% similar)
- [[2025-09-17/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250917|TGPO Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (80.0% similar)
- [[2025-09-18/TDRM_ Smooth Reward Models with Temporal Difference for LLM RL and Inference_20250918|TDRM Smooth Reward Models with Temporal Difference for LLM RL and Inference]] (79.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15498v1 Announce Type: new 
Abstract: Transformers have emerged as a compelling architecture for sequential decision-making by modeling trajectories via self-attention. In reinforcement learning (RL), they enable return-conditioned control without relying on value function approximation. Decision Transformers (DTs) exploit this by casting RL as supervised sequence modeling, but they are restricted to offline data and lack exploration. Online Decision Transformers (ODTs) address this limitation through entropy-regularized training on on-policy rollouts, offering a stable alternative to traditional RL methods like Soft Actor-Critic, which depend on bootstrapped targets and reward shaping. Despite these advantages, ODTs use standard attention, which lacks explicit memory of action-specific outcomes. This leads to inefficiencies in learning long-term action effectiveness. Inspired by cognitive models such as Experience-Weighted Attraction (EWA), we propose Experience-Weighted Attraction with Vector Quantization for Online Decision Transformers (EWA-VQ-ODT), a lightweight module that maintains per-action mental accounts summarizing recent successes and failures. Continuous actions are routed via direct grid lookup to a compact vector-quantized codebook, where each code stores a scalar attraction updated online through decay and reward-based reinforcement. These attractions modulate attention by biasing the columns associated with action tokens, requiring no change to the backbone or training objective. On standard continuous-control benchmarks, EWA-VQ-ODT improves sample efficiency and average return over ODT, particularly in early training. The module is computationally efficient, interpretable via per-code traces, and supported by theoretical guarantees that bound the attraction dynamics and its impact on attention drift.

## 🔍 Abstract (한글 번역)

arXiv:2509.15498v1 발표 유형: 신규  
초록: 트랜스포머는 자기 주의를 통해 궤적을 모델링하여 순차적 의사 결정에 매력적인 아키텍처로 부상했습니다. 강화 학습(RL)에서는 가치 함수 근사에 의존하지 않고 반환 조건부 제어를 가능하게 합니다. Decision Transformers(DTs)는 이를 활용하여 RL을 감독된 시퀀스 모델링으로 변환하지만, 오프라인 데이터에 제한되며 탐색이 부족합니다. Online Decision Transformers(ODTs)는 정책 롤아웃에 대한 엔트로피 정규화 훈련을 통해 이 제한을 해결하며, 부트스트랩 타겟과 보상 형성에 의존하는 Soft Actor-Critic과 같은 전통적인 RL 방법에 대한 안정적인 대안을 제공합니다. 이러한 장점에도 불구하고, ODTs는 행동별 결과에 대한 명시적 기억이 없는 표준 주의를 사용합니다. 이는 장기적인 행동 효과 학습에 비효율성을 초래합니다. Experience-Weighted Attraction(EWA)와 같은 인지 모델에서 영감을 받아, 우리는 Online Decision Transformers를 위한 벡터 양자화된 경험 가중 매력을 제안합니다(EWA-VQ-ODT). 이 경량 모듈은 최근 성공과 실패를 요약하는 행동별 정신 계정을 유지합니다. 연속적인 행동은 직접적인 그리드 조회를 통해 압축된 벡터 양자화 코드북으로 라우팅되며, 각 코드는 감쇠와 보상 기반 강화로 온라인 업데이트되는 스칼라 매력을 저장합니다. 이러한 매력은 행동 토큰과 관련된 열에 편향을 주어 주의를 조절하며, 백본이나 훈련 목표의 변경이 필요하지 않습니다. 표준 연속 제어 벤치마크에서 EWA-VQ-ODT는 특히 초기 훈련에서 ODT에 비해 샘플 효율성과 평균 반환을 향상시킵니다. 이 모듈은 계산적으로 효율적이며, 코드별 추적을 통해 해석 가능하고, 매력 역학과 주의 드리프트에 대한 영향을 제한하는 이론적 보증에 의해 지원됩니다.

## 📝 요약

트랜스포머는 자기 주의를 통해 경로를 모델링하여 순차적 의사결정에 효과적인 구조로 부상했습니다. 강화 학습(RL)에서, 이는 가치 함수 근사 없이 반환 조건부 제어를 가능하게 합니다. Decision Transformers(DTs)는 이를 활용하여 RL을 지도 학습 시퀀스 모델링으로 전환하지만, 오프라인 데이터에만 국한되고 탐색이 부족합니다. Online Decision Transformers(ODTs)는 정책 롤아웃에 대한 엔트로피 정규화 훈련을 통해 이 제한을 해결하며, Soft Actor-Critic과 같은 전통적인 RL 방법에 비해 안정적인 대안을 제공합니다. 그러나 ODTs는 표준 주의를 사용하여 행동별 결과에 대한 명시적 기억이 부족합니다. 이를 해결하기 위해 Experience-Weighted Attraction(EWA)에서 영감을 받아, 우리는 Online Decision Transformers를 위한 Experience-Weighted Attraction with Vector Quantization(EWA-VQ-ODT)를 제안합니다. 이 모듈은 최근 성공과 실패를 요약하는 행동별 정신 계정을 유지하며, 연속적인 행동을 벡터 양자화된 코드북으로 라우팅하여 주의를 조정합니다. EWA-VQ-ODT는 초기 훈련에서 샘플 효율성과 평균 수익을 개선하며, 계산 효율적이고 해석 가능하며, 이론적 보장을 통해 주의 드리프트에 대한 영향을 제한합니다.

## 🎯 주요 포인트

- 1. Decision Transformers는 강화 학습을 감독 학습 시퀀스 모델링으로 변환하지만, 탐색 기능이 부족하고 오프라인 데이터에만 의존합니다.

- 2. Online Decision Transformers는 엔트로피 정규화된 훈련을 통해 이 제한을 극복하며, 전통적인 강화 학습 방법보다 안정적인 대안을 제공합니다.

- 3. Experience-Weighted Attraction with Vector Quantization for Online Decision Transformers (EWA-VQ-ODT)는 각 행동의 최근 성공과 실패를 요약하는 경량 모듈로, 학습 효율성을 개선합니다.

- 4. EWA-VQ-ODT는 연속적인 행동을 벡터 양자화된 코드북으로 라우팅하여 주의력을 조정하며, 기본 구조나 훈련 목표를 변경하지 않습니다.

- 5. EWA-VQ-ODT는 표준 연속 제어 벤치마크에서 샘플 효율성과 평균 수익을 개선하며, 특히 초기 훈련에서 두드러집니다.

---

*Generated on 2025-09-22 15:16:45*