# Subject Matter Expertise vs Professional Management in Collective Sequential Decision Making

**Korean Title:** 집단 순차적 의사 결정에서의 전문 분야 지식 대 전문적 관리

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Professional Manager Model

## 🔗 유사한 논문
- [[2025-09-19/Predicting Multi-Agent Specialization via Task Parallelizability_20250919|Predicting Multi-Agent Specialization via Task Parallelizability]] (78.9% similar)
- [[2025-09-19/Emergent Alignment via Competition_20250919|Emergent Alignment via Competition]] (78.4% similar)
- [[2025-09-22/Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context_20250922|Diagnostics of cognitive failures in multi-agent expert systems using dynamic evaluation protocols and subsequent mutation of the processing context]] (77.5% similar)
- [[2025-09-19/LEED_ A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning_20250919|LEED A Highly Efficient and Scalable LLM-Empowered Expert Demonstrations Framework for Multi-Agent Reinforcement Learning]] (76.6% similar)
- [[2025-09-22/SWE-Effi_ Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints_20250922|SWE-Effi Re-Evaluating Software AI Agent System Effectiveness Under Resource Constraints]] (76.5% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15263v1 Announce Type: cross 
Abstract: Your company's CEO is retiring. You search for a successor. You can promote an employee from the company familiar with the company's operations, or recruit an external professional manager. Who should you prefer? It has not been clear how to address this question, the "subject matter expertise vs. professional manager debate", quantitatively and objectively. We note that a company's success depends on long sequences of interdependent decisions, with often-opposing recommendations of diverse board members. To model this task in a controlled environment, we utilize chess - a complex, sequential game with interdependent decisions which allows for quantitative analysis of performance and expertise (since the states, actions and game outcomes are well-defined). The availability of chess engines differing in style and expertise, allows scalable experimentation. We considered a team of (computer) chess players. At each turn, team members recommend a move and a manager chooses a recommendation. We compared the performance of two manager types. For manager as "subject matter expert", we used another (computer) chess player that assesses the recommendations of the team members based on its own chess expertise. We examined the performance of such managers at different strength levels. To model a "professional manager", we used Reinforcement Learning (RL) to train a network that identifies the board positions in which different team members have relative advantage, without any pretraining in chess. We further examined this network to see if any chess knowledge is acquired implicitly. We found that subject matter expertise beyond a minimal threshold does not significantly contribute to team synergy. Moreover, performance of a RL-trained "professional" manager significantly exceeds that of even the best "expert" managers, while acquiring only limited understanding of chess.

## 🔍 Abstract (한글 번역)

arXiv:2509.15263v1 발표 유형: 교차  
초록: 귀사의 CEO가 은퇴합니다. 후임자를 찾고 있습니다. 회사의 운영에 익숙한 직원을 승진시키거나 외부의 전문 경영인을 채용할 수 있습니다. 누구를 선호해야 할까요? 이 질문, 즉 "주제 전문성 대 전문 경영인 논쟁"을 정량적이고 객관적으로 해결하는 방법은 명확하지 않았습니다. 우리는 회사의 성공이 종종 다양한 이사회의 상반된 권고와 함께 상호 의존적인 긴 의사결정 연속에 달려 있다는 점에 주목합니다. 이 작업을 통제된 환경에서 모델링하기 위해, 우리는 성능과 전문성의 정량적 분석을 가능하게 하는 상호 의존적인 결정이 있는 복잡한 순차 게임인 체스를 활용합니다 (상태, 행동 및 게임 결과가 잘 정의되어 있기 때문입니다). 스타일과 전문성이 다른 체스 엔진의 가용성은 확장 가능한 실험을 가능하게 합니다. 우리는 (컴퓨터) 체스 플레이어 팀을 고려했습니다. 각 턴마다 팀원들은 이동을 추천하고 매니저가 추천을 선택합니다. 우리는 두 가지 유형의 매니저 성과를 비교했습니다. "주제 전문가"로서의 매니저를 위해, 우리는 팀원의 추천을 자신의 체스 전문성에 기반하여 평가하는 또 다른 (컴퓨터) 체스 플레이어를 사용했습니다. 우리는 이러한 매니저의 성과를 다양한 강도 수준에서 조사했습니다. "전문 경영인"을 모델링하기 위해, 우리는 체스에 대한 사전 학습 없이 다른 팀원들이 상대적 이점을 가지는 보드 위치를 식별하는 네트워크를 훈련시키기 위해 강화 학습(RL)을 사용했습니다. 우리는 이 네트워크가 암묵적으로 체스 지식을 습득하는지 여부를 추가로 조사했습니다. 우리는 최소한의 임계값을 초과하는 주제 전문성이 팀 시너지에 크게 기여하지 않는다는 것을 발견했습니다. 더욱이, RL로 훈련된 "전문" 매니저의 성과는 심지어 최고의 "전문가" 매니저의 성과를 크게 초과하며, 체스에 대한 제한된 이해만을 획득했습니다.

## 📝 요약

이 논문은 기업의 CEO 후임 선택 문제를 체스 게임을 통해 모델링하여 분석합니다. 내부 전문가와 외부 전문 경영인 중 누구를 선택할지에 대한 논쟁을 해결하기 위해, 체스의 복잡한 의사결정 과정을 활용했습니다. 연구에서는 체스 엔진을 사용하여 팀의 추천을 평가하는 '전문가' 관리자와 강화 학습을 통해 훈련된 '전문 경영인' 관리자의 성과를 비교했습니다. 결과적으로, 최소한의 전문성을 초과하는 전문가의 기여는 팀 시너지에 큰 영향을 미치지 않았으며, RL로 훈련된 전문 경영인의 성과가 전문가 관리자보다 뛰어났습니다. 이는 체스에 대한 제한된 이해만으로도 가능했습니다.

## 🎯 주요 포인트

- 1. 기업의 성공은 상호 의존적인 결정의 연속에 달려 있으며, 다양한 이사회의 상반된 권고가 영향을 미친다.

- 2. 체스를 활용하여 복잡한 의사결정 과정을 정량적으로 분석하고, 전문성과 성과를 평가할 수 있는 모델을 구축하였다.

- 3. 주제 전문가로서의 관리자는 팀원의 추천을 자신의 체스 전문성에 기반하여 평가하는 컴퓨터 체스 플레이어로 모델링하였다.

- 4. 전문 관리자 모델은 체스에 대한 사전 훈련 없이 팀원의 상대적 이점을 식별하는 강화 학습 네트워크를 사용하였다.

- 5. 최소한의 주제 전문성 이상은 팀 시너지에 크게 기여하지 않으며, 강화 학습을 통해 훈련된 전문 관리자의 성과가 최고 수준의 전문가 관리자보다 우수하였다.

---

*Generated on 2025-09-22 15:36:29*