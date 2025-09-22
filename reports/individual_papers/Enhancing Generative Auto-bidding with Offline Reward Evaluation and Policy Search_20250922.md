# Enhancing Generative Auto-bidding with Offline Reward Evaluation and Policy Search

**Korean Title:** 생성적 자동 입찰의 향상을 위한 오프라인 보상 평가 및 정책 탐색

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Generative Planning with Policy Optimization

## 🔗 유사한 논문
- [[2025-09-19/JU-NLP at Touch'e_ Covert Advertisement in Conversational AI-Generation and Detection Strategies_20250919|JU-NLP at Touch'e Covert Advertisement in Conversational AI-Generation and Detection Strategies]] (83.2% similar)
- [[2025-09-19/Optimal Type-Dependent Liquid Welfare Guarantees for Autobidding Agents with Budgets_20250919|Optimal Type-Dependent Liquid Welfare Guarantees for Autobidding Agents with Budgets]] (82.3% similar)
- [[2025-09-18/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250918|TGPO Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (81.5% similar)
- [[2025-09-17/TGPO_ Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning_20250917|TGPO Tree-Guided Preference Optimization for Robust Web Agent Reinforcement Learning]] (81.4% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (80.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15927v1 Announce Type: cross 
Abstract: Auto-bidding is an essential tool for advertisers to enhance their advertising performance. Recent progress has shown that AI-Generated Bidding (AIGB), which formulates the auto-bidding as a trajectory generation task and trains a conditional diffusion-based planner on offline data, achieves superior and stable performance compared to typical offline reinforcement learning (RL)-based auto-bidding methods. However, existing AIGB methods still encounter a performance bottleneck due to their neglect of fine-grained generation quality evaluation and inability to explore beyond static datasets. To address this, we propose AIGB-Pearl (\emph{Planning with EvAluator via RL}), a novel method that integrates generative planning and policy optimization. The key to AIGB-Pearl is to construct a non-bootstrapped \emph{trajectory evaluator} to assign rewards and guide policy search, enabling the planner to optimize its generation quality iteratively through interaction. Furthermore, to enhance trajectory evaluator accuracy in offline settings, we incorporate three key techniques: (i) a Large Language Model (LLM)-based architecture for better representational capacity, (ii) hybrid point-wise and pair-wise losses for better score learning, and (iii) adaptive integration of expert feedback for better generalization ability. Extensive experiments on both simulated and real-world advertising systems demonstrate the state-of-the-art performance of our approach.

## 🔍 Abstract (한글 번역)

arXiv:2509.15927v1 발표 유형: 교차  
초록: 자동 입찰은 광고주가 광고 성과를 향상시키기 위한 필수 도구입니다. 최근의 발전은 AI 생성 입찰(AIGB)이 자동 입찰을 궤적 생성 작업으로 공식화하고 오프라인 데이터에서 조건부 확산 기반 계획자를 훈련하여 전형적인 오프라인 강화 학습(RL) 기반 자동 입찰 방법에 비해 우수하고 안정적인 성능을 달성한다는 것을 보여주었습니다. 그러나 기존의 AIGB 방법은 세밀한 생성 품질 평가를 무시하고 정적 데이터셋을 넘어 탐색할 수 없기 때문에 여전히 성능 병목 현상을 겪고 있습니다. 이를 해결하기 위해 우리는 생성 계획과 정책 최적화를 통합한 새로운 방법인 AIGB-Pearl(\emph{Planning with EvAluator via RL})을 제안합니다. AIGB-Pearl의 핵심은 비부트스트랩 \emph{궤적 평가자}를 구성하여 보상을 할당하고 정책 탐색을 안내함으로써 계획자가 상호작용을 통해 생성 품질을 반복적으로 최적화할 수 있도록 하는 것입니다. 더욱이, 오프라인 환경에서 궤적 평가자의 정확성을 높이기 위해 우리는 세 가지 주요 기술을 통합합니다: (i) 더 나은 표현 능력을 위한 대형 언어 모델(LLM) 기반 아키텍처, (ii) 더 나은 점수 학습을 위한 하이브리드 점 단위 및 쌍 단위 손실, (iii) 더 나은 일반화 능력을 위한 전문가 피드백의 적응적 통합. 시뮬레이션 및 실제 광고 시스템 모두에서의 광범위한 실험은 우리 접근 방식의 최첨단 성능을 입증합니다.

## 📝 요약

이 논문은 광고 성능을 향상시키기 위한 자동 입찰 도구인 AI-생성 입찰(AIGB)의 성능 한계를 극복하기 위해 AIGB-Pearl을 제안합니다. 기존 AIGB는 주로 오프라인 강화 학습 기반으로 작동하지만, 세밀한 생성 품질 평가와 정적 데이터셋을 넘어선 탐색에 한계가 있었습니다. AIGB-Pearl은 생성 계획과 정책 최적화를 통합하여 이러한 문제를 해결합니다. 특히, 비부트스트랩 방식의 경로 평가자를 도입하여 보상을 할당하고 정책 탐색을 안내함으로써 생성 품질을 반복적으로 최적화합니다. 또한, 오프라인 환경에서의 정확성을 높이기 위해 대형 언어 모델(LLM) 기반 아키텍처, 혼합 손실 함수, 전문가 피드백의 적응적 통합을 활용합니다. 실험 결과, 제안된 방법이 최첨단 성능을 보임을 확인했습니다.

## 🎯 주요 포인트

- 1. AIGB-Pearl은 생성적 계획과 정책 최적화를 통합하여 광고 성능을 향상시키는 새로운 방법입니다.

- 2. 비부트스트랩 방식의 경로 평가자를 구축하여 보상을 할당하고 정책 탐색을 안내합니다.

- 3. 오프라인 환경에서 경로 평가자의 정확성을 높이기 위해 LLM 기반 아키텍처, 혼합 손실, 전문가 피드백의 적응적 통합을 사용합니다.

- 4. 시뮬레이션 및 실제 광고 시스템 실험에서 AIGB-Pearl의 최첨단 성능이 입증되었습니다.

---

*Generated on 2025-09-22 14:17:23*