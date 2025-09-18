
# Mining the Long Tail: A Comparative Study of Data-Centric Criticality Metrics for Robust Offline Reinforcement Learning in Autonomous Motion Planning

**Korean Title:** 장바구니 채굴: 자율 주행 계획을 위한 견고한 오프라인 강화 학습을 위한 데이터 중심 중요성 지표의 비교 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Data Curation|Data Curation]] [[keywords/broad/Offline Reinforcement Learning|Offline Reinforcement Learning]] [[keywords/broad/Autonomous Vehicle Planning|Autonomous Vehicle Planning]] [[keywords/specific/Conservative Q-Learning|Conservative Q-Learning]] [[keywords/unique/Waymax simulator|Waymax simulator]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Data Curation
**🔬 Broad Technical**: Offline Reinforcement Learning, Autonomous Vehicle Planning
**🔗 Specific Connectable**: Conservative Q-Learning
**⭐ Unique Technical**: Waymax simulator

**ArXiv ID**: [2508.18397](https://arxiv.org/abs/2508.18397)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2508.18397.pdf)


## 🏷️ 추출된 키워드



`Offline Reinforcement Learning` • 

`Autonomous Vehicle Planning` • 

`Conservative Q-Learning` • 

`Criticality Weighting Schemes` • 

`Data Curation in Offline RL`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.18397v2 Announce Type: replace-cross 
Abstract: Offline Reinforcement Learning (RL) presents a promising paradigm for training autonomous vehicle (AV) planning policies from large-scale, real-world driving logs. However, the extreme data imbalance in these logs, where mundane scenarios vastly outnumber rare "long-tail" events, leads to brittle and unsafe policies when using standard uniform data sampling. In this work, we address this challenge through a systematic, large-scale comparative study of data curation strategies designed to focus the learning process on information-rich samples. We investigate six distinct criticality weighting schemes which are categorized into three families: heuristic-based, uncertainty-based, and behavior-based. These are evaluated at two temporal scales, the individual timestep and the complete scenario. We train seven goal-conditioned Conservative Q-Learning (CQL) agents with a state-of-the-art, attention-based architecture and evaluate them in the high-fidelity Waymax simulator. Our results demonstrate that all data curation methods significantly outperform the baseline. Notably, data-driven curation using model uncertainty as a signal achieves the most significant safety improvements, reducing the collision rate by nearly three-fold (from 16.0% to 5.5%). Furthermore, we identify a clear trade-off where timestep-level weighting excels at reactive safety while scenario-level weighting improves long-horizon planning. Our work provides a comprehensive framework for data curation in Offline RL and underscores that intelligent, non-uniform sampling is a critical component for building safe and reliable autonomous agents.

## 🔍 Abstract (한글 번역)

arXiv:2508.18397v2 발표 유형: replace-cross
요약: 오프라인 강화 학습(RL)은 대규모 실제 운전 로그에서 자율 주행 차량(AV) 계획 정책을 훈련하는 유망한 패러다임을 제시합니다. 그러나 이러한 로그에서의 극도의 데이터 불균형은 일상적인 시나리오가 드물고 "긴 꼬리" 이벤트보다 훨씬 많은 경우에 표준 균일 데이터 샘플링을 사용할 때 취약하고 안전하지 않은 정책으로 이어집니다. 본 연구에서는 정보가 풍부한 샘플에 학습 과정을 집중시키기 위해 설계된 데이터 정리 전략의 체계적이고 대규모 비교 연구를 통해 이러한 도전에 대처합니다. 우리는 세 가지 가족으로 분류된 여섯 가지 다양한 중요도 가중 체계를 조사합니다: 휴리스틱 기반, 불확실성 기반 및 행동 기반. 이들은 개별 시간 단계와 완전한 시나리오 두 가지 시간 척도에서 평가됩니다. 우리는 최첨단 주의 집중형 아키텍처를 가진 일곱 목표 조건화 보수적 Q-러닝(CQL) 에이전트를 훈련하고 고성능 Waymax 시뮬레이터에서 평가합니다. 우리의 결과는 모든 데이터 정리 방법이 기준선을 크게 능가함을 보여줍니다. 특히, 모델 불확실성을 신호로 사용하는 데이터 기반 정리가 가장 중요한 안전 개선을 달성하며 충돌률을 거의 세 배로 줄입니다(16.0%에서 5.5%로). 또한, 우리는 반응적 안전에서 시간 단계 수준의 가중이 뛰어나며 시나리오 수준의 가중이 장기 계획을 개선한다는 명확한 트레이드 오프를 확인합니다. 우리의 연구는 오프라인 RL에서 데이터 정리를 위한 포괄적인 프레임워크를 제공하며 지능적이고 균일하지 않은 샘플링이 안전하고 신뢰할 수 있는 자율 주행 에이전트를 구축하는 데 중요한 구성 요소임을 강조합니다.

## 📝 요약

본 연구는 오프라인 강화 학습을 통해 자율 주행 차량 계획 정책을 학습하는 데 있어 발생하는 데이터 불균형 문제를 해결하기 위해 데이터 선별 전략을 체계적으로 비교하는 연구이다. 우리는 휴리스틱 기반, 불확실성 기반, 행동 기반으로 분류된 여섯 가지 중요도 가중치 방법을 조사하였고, 이를 두 가지 시간 단계에서 평가하였다. 최신 기술을 적용한 주의 깊은 Q-학습(CQL) 에이전트 일곱 개를 훈련시키고, Waymax 시뮬레이터에서 평가하였다. 결과적으로 모든 데이터 선별 방법이 기준선을 크게 능가함을 보였으며, 모델 불확실성을 신호로 사용하는 데이터 선별이 가장 큰 안전성 향상을 이룩했다. 또한, 시간 단계별 가중치는 반응적 안전성에 뛰어나고 시나리오 수준의 가중치는 장기 계획에 도움이 된다는 것을 확인하였다. 이러한 결과는 오프라인 강화 학습에서 데이터 선별의 중요성을 강조하며 안전하고 신뢰할 수 있는 자율 주행 에이전트를 구축하는 데 필수적인 요소임을 보여준다.

## 🎯 주요 포인트


- 대규모, 실제 운전 기록을 사용한 자율 주행 차량 계획 정책 훈련에 대한 오프라인 강화 학습의 유망한 패러다임

- 데이터 적응 방법을 사용하여 안전성 향상

- 모델 불확실성을 신호로 사용하는 데이터 주도적 적응이 충돌율을 거의 3배로 감소시킴

- 시간 단계별 가중치는 반응적 안전성에서 뛰어나며 시나리오 수준의 가중치는 장기 계획을 향상시킴.


---

*Generated on 2025-09-18 16:34:32*