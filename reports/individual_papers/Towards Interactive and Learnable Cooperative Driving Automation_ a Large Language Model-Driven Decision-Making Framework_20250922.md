# Towards Interactive and Learnable Cooperative Driving Automation: a Large Language Model-Driven Decision-Making Framework

**Korean Title:** 상호작용 가능하고 학습 가능한 협력적 운전 자동화를 향하여: 대형 언어 모델 기반 의사결정 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Interactive Cooperative Driving

## 🔗 유사한 논문
- [[2025-09-19/Digital Twin-based Cooperative Autonomous Driving in Smart Intersections_ A Multi-Agent Reinforcement Learning Approach_20250919|Digital Twin-based Cooperative Autonomous Driving in Smart Intersections A Multi-Agent Reinforcement Learning Approach]] (83.5% similar)
- [[2025-09-19/CRAFT_ Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks_20250919|CRAFT Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks]] (83.4% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (82.5% similar)
- [[2025-09-19/Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning_20250919|Traffic Co-Simulation Framework Empowered by Infrastructure Camera Sensing and Reinforcement Learning]] (82.3% similar)
- [[2025-09-18/CARGO_ A Framework for Confidence-Aware Routing of Large Language Models_20250918|CARGO A Framework for Confidence-Aware Routing of Large Language Models]] (82.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.12812v3 Announce Type: replace-cross 
Abstract: At present, Connected Autonomous Vehicles (CAVs) have begun to open road testing around the world, but their safety and efficiency performance in complex scenarios is still not satisfactory. Cooperative driving leverages the connectivity ability of CAVs to achieve synergies greater than the sum of their parts, making it a promising approach to improving CAV performance in complex scenarios. However, the lack of interaction and continuous learning ability limits current cooperative driving to single-scenario applications and specific Cooperative Driving Automation (CDA). To address these challenges, this paper proposes CoDrivingLLM, an interactive and learnable LLM-driven cooperative driving framework, to achieve all-scenario and all-CDA. First, since Large Language Models(LLMs) are not adept at handling mathematical calculations, an environment module is introduced to update vehicle positions based on semantic decisions, thus avoiding potential errors from direct LLM control of vehicle positions. Second, based on the four levels of CDA defined by the SAE J3216 standard, we propose a Chain-of-Thought (COT) based reasoning module that includes state perception, intent sharing, negotiation, and decision-making, enhancing the stability of LLMs in multi-step reasoning tasks. Centralized conflict resolution is then managed through a conflict coordinator in the reasoning process. Finally, by introducing a memory module and employing retrieval-augmented generation, CAVs are endowed with the ability to learn from their past experiences. We validate the proposed CoDrivingLLM through ablation experiments on the negotiation module, reasoning with different shots experience, and comparison with other cooperative driving methods.

## 🔍 Abstract (한글 번역)

arXiv:2409.12812v3 발표 유형: 교체-크로스  
초록: 현재, 연결된 자율주행차(CAVs)는 전 세계적으로 도로 시험을 시작했지만, 복잡한 시나리오에서의 안전성과 효율성 성능은 여전히 만족스럽지 않습니다. 협력 주행은 CAV의 연결 능력을 활용하여 개별 성능의 합을 초과하는 시너지를 달성함으로써, 복잡한 시나리오에서 CAV 성능을 향상시키는 유망한 접근법입니다. 그러나 상호작용과 지속적인 학습 능력의 부족은 현재의 협력 주행을 단일 시나리오 응용 및 특정 협력 주행 자동화(CDA)로 제한합니다. 이러한 문제를 해결하기 위해, 본 논문은 모든 시나리오와 모든 CDA를 달성하기 위한 상호작용 가능하고 학습 가능한 LLM 기반 협력 주행 프레임워크인 CoDrivingLLM을 제안합니다. 첫째, 대형 언어 모델(LLM)은 수학적 계산을 처리하는 데 능숙하지 않기 때문에, 의미적 결정을 기반으로 차량 위치를 업데이트하는 환경 모듈을 도입하여 LLM이 차량 위치를 직접 제어하는 것에서 발생할 수 있는 잠재적 오류를 피합니다. 둘째, SAE J3216 표준에 의해 정의된 CDA의 네 가지 수준을 기반으로, 상태 인식, 의도 공유, 협상 및 의사 결정을 포함하는 사고의 연쇄(COT) 기반 추론 모듈을 제안하여 다단계 추론 작업에서 LLM의 안정성을 강화합니다. 중앙 집중식 갈등 해결은 추론 과정에서 갈등 조정자를 통해 관리됩니다. 마지막으로, 메모리 모듈을 도입하고 검색 증강 생성 방식을 사용하여, CAV는 과거 경험에서 학습할 수 있는 능력을 부여받습니다. 우리는 협상 모듈에 대한 소거 실험, 다양한 샷 경험을 통한 추론, 및 다른 협력 주행 방법과의 비교를 통해 제안된 CoDrivingLLM을 검증합니다.

## 📝 요약

이 논문은 복잡한 시나리오에서 자율주행차(CAV)의 성능을 개선하기 위해 CoDrivingLLM이라는 상호작용 가능하고 학습 가능한 협력 주행 프레임워크를 제안합니다. CoDrivingLLM은 대형 언어 모델(LLM)을 활용하여 모든 시나리오와 모든 협력 주행 자동화(CDA)를 목표로 합니다. 수학적 계산에 약한 LLM의 한계를 극복하기 위해 환경 모듈을 도입하여 차량 위치를 갱신하고, CDA의 네 가지 수준에 기반한 Chain-of-Thought(COT) 추론 모듈을 통해 다단계 추론의 안정성을 높입니다. 또한, 중앙 집중식 갈등 해결을 위한 조정자와 과거 경험 학습을 위한 메모리 모듈을 포함합니다. 제안된 프레임워크는 협상 모듈의 절제 실험과 다른 협력 주행 방법과의 비교를 통해 검증되었습니다.

## 🎯 주요 포인트

- 1. 현재 자율주행차(CAV)의 복잡한 시나리오에서의 안전성과 효율성 성능이 만족스럽지 않음.

- 2. CAV의 연결성을 활용한 협력 운전이 복잡한 시나리오에서 성능을 향상시키는 유망한 접근법으로 제시됨.

- 3. CoDrivingLLM은 대화형 및 학습 가능한 LLM 기반 협력 운전 프레임워크로, 모든 시나리오와 모든 CDA를 목표로 함.

- 4. 수학적 계산에 능숙하지 않은 LLM의 한계를 보완하기 위해 환경 모듈을 도입하여 차량 위치를 갱신함.

- 5. 과거 경험으로부터 학습할 수 있도록 메모리 모듈과 검색 증강 생성 방식을 도입하여 CAV의 학습 능력을 강화함.

---

*Generated on 2025-09-22 14:38:33*