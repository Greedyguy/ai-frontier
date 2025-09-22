# Fleming-R1: Toward Expert-Level Medical Reasoning via Reinforcement Learning

**Korean Title:** Fleming-R1: 강화 학습을 통한 전문가 수준의 의학적 추론을 향하여

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Knowledge Graph, Chain of Thought

## 🔗 유사한 논문
- [[2025-09-19/MedFact-R1_ Towards Factual Medical Reasoning via Pseudo-Label Augmentation_20250919|MedFact-R1 Towards Factual Medical Reasoning via Pseudo-Label Augmentation]] (86.8% similar)
- [[2025-09-22/Reward Hacking Mitigation using Verifiable Composite Rewards_20250922|Reward Hacking Mitigation using Verifiable Composite Rewards]] (82.7% similar)
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL Toward Expert-Level Medical Text Validation with Language Models]] (82.4% similar)
- [[2025-09-22/FLARE_ Faithful Logic-Aided Reasoning and Exploration_20250922|FLARE Faithful Logic-Aided Reasoning and Exploration]] (82.3% similar)
- [[2025-09-17/Combining Evidence and Reasoning for Biomedical Fact-Checking_20250917|Combining Evidence and Reasoning for Biomedical Fact-Checking]] (81.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15279v1 Announce Type: new 
Abstract: While large language models show promise in medical applications, achieving expert-level clinical reasoning remains challenging due to the need for both accurate answers and transparent reasoning processes. To address this challenge, we introduce Fleming-R1, a model designed for verifiable medical reasoning through three complementary innovations. First, our Reasoning-Oriented Data Strategy (RODS) combines curated medical QA datasets with knowledge-graph-guided synthesis to improve coverage of underrepresented diseases, drugs, and multi-hop reasoning chains. Second, we employ Chain-of-Thought (CoT) cold start to distill high-quality reasoning trajectories from teacher models, establishing robust inference priors. Third, we implement a two-stage Reinforcement Learning from Verifiable Rewards (RLVR) framework using Group Relative Policy Optimization, which consolidates core reasoning skills while targeting persistent failure modes through adaptive hard-sample mining. Across diverse medical benchmarks, Fleming-R1 delivers substantial parameter-efficient improvements: the 7B variant surpasses much larger baselines, while the 32B model achieves near-parity with GPT-4o and consistently outperforms strong open-source alternatives. These results demonstrate that structured data design, reasoning-oriented initialization, and verifiable reinforcement learning can advance clinical reasoning beyond simple accuracy optimization. We release Fleming-R1 publicly to promote transparent, reproducible, and auditable progress in medical AI, enabling safer deployment in high-stakes clinical environments.

## 🔍 Abstract (한글 번역)

arXiv:2509.15279v1 발표 유형: 신규  
초록: 대형 언어 모델은 의료 응용 분야에서 가능성을 보여주고 있지만, 전문가 수준의 임상 추론을 달성하는 것은 정확한 답변과 투명한 추론 과정을 모두 필요로 하기 때문에 여전히 도전 과제입니다. 이 문제를 해결하기 위해, 우리는 검증 가능한 의료 추론을 위해 설계된 모델인 Fleming-R1을 소개합니다. 이 모델은 세 가지 상호 보완적인 혁신을 통해 개발되었습니다. 첫째, 우리의 Reasoning-Oriented Data Strategy (RODS)는 큐레이션된 의료 QA 데이터셋과 지식 그래프 기반 합성을 결합하여, 대표성이 부족한 질병, 약물 및 다중 단계 추론 체인의 범위를 개선합니다. 둘째, 우리는 Chain-of-Thought (CoT) 콜드 스타트를 사용하여 교사 모델로부터 고품질의 추론 경로를 추출하여 견고한 추론 사전 지식을 확립합니다. 셋째, 우리는 Group Relative Policy Optimization을 사용하는 두 단계의 Reinforcement Learning from Verifiable Rewards (RLVR) 프레임워크를 구현하여, 적응형 하드 샘플 마이닝을 통해 지속적인 실패 모드를 목표로 하면서 핵심 추론 기술을 통합합니다. 다양한 의료 벤치마크에서 Fleming-R1은 상당한 파라미터 효율성 향상을 제공합니다: 7B 변형은 훨씬 더 큰 기준선을 능가하며, 32B 모델은 GPT-4o와 거의 동등한 성능을 달성하고 강력한 오픈 소스 대안들을 지속적으로 능가합니다. 이러한 결과는 구조화된 데이터 설계, 추론 지향 초기화 및 검증 가능한 강화 학습이 단순한 정확도 최적화를 넘어 임상 추론을 발전시킬 수 있음을 보여줍니다. 우리는 Fleming-R1을 공개하여 투명하고 재현 가능하며 감사 가능한 의료 AI의 발전을 촉진하고, 고위험 임상 환경에서의 안전한 배치를 가능하게 합니다.

## 📝 요약

Fleming-R1은 의료 분야에서 전문가 수준의 임상 추론을 목표로 하는 모델로, 정확한 답변과 투명한 추론 과정을 동시에 달성하기 위해 개발되었습니다. 이 모델은 세 가지 혁신을 통해 이를 구현합니다. 첫째, Reasoning-Oriented Data Strategy(RODS)를 통해 의료 QA 데이터셋과 지식 그래프 기반 합성을 결합하여 덜 대표되는 질병, 약물, 다중 추론 체인의 범위를 확장합니다. 둘째, Chain-of-Thought(CoT) 기법을 활용하여 고품질의 추론 경로를 구축하고, 셋째, Verifiable Rewards를 통한 강화 학습(RLVR) 프레임워크를 도입하여 핵심 추론 능력을 강화합니다. Fleming-R1은 다양한 의료 벤치마크에서 뛰어난 성능을 보이며, 특히 7B 모델은 더 큰 모델들을 능가하고, 32B 모델은 GPT-4o와 유사한 성능을 보입니다. 이 연구는 구조화된 데이터 설계와 검증 가능한 강화 학습이 임상 추론을 발전시킬 수 있음을 보여줍니다. Fleming-R1은 의료 AI의 투명하고 안전한 발전을 위해 공개되었습니다.

## 🎯 주요 포인트

- 1. Fleming-R1 모델은 정확한 답변과 투명한 추론 과정을 통해 전문가 수준의 임상 추론을 목표로 한다.

- 2. Reasoning-Oriented Data Strategy(RODS)는 지식 그래프를 활용하여 부족한 질병, 약물, 다중 단계 추론을 보완한다.

- 3. Chain-of-Thought(CoT) 기법을 통해 고품질의 추론 경로를 구축하여 강력한 추론 기반을 마련한다.

- 4. Verifiable Rewards를 통한 강화 학습(RLVR) 프레임워크는 적응형 샘플 채굴을 통해 지속적인 실패 모드를 해결한다.

- 5. Fleming-R1은 다양한 의료 벤치마크에서 뛰어난 성능을 보이며, 특히 7B 모델은 더 큰 모델을 능가하고, 32B 모델은 GPT-4o와 유사한 성능을 보인다.

---

*Generated on 2025-09-22 15:09:25*