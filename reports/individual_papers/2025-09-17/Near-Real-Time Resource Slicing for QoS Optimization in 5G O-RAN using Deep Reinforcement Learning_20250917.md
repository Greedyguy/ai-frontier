---
keywords:
  - Graph Neural Networks
  - Reinforcement Learning
  - Optimization
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:49:40.664945",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Networks",
    "Reinforcement Learning",
    "Optimization"
  ],
  "rejected_keywords": [
    "Near-Real-Time RAN Intelligent Controller"
  ],
  "similarity_scores": {
    "Graph Neural Networks": 0.78,
    "Reinforcement Learning": 0.8,
    "Optimization": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Near-Real-Time Resource Slicing for QoS Optimization in 5G O-RAN using Deep Reinforcement Learning

**Korean Title:** 5G O-RAN에서 심층 강화 학습을 이용한 QoS 최적화를 위한 거의 실시간 자원 슬라이싱

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]       [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Optimization|Quality-of-Service Optimization]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Networks|Graph Convolutional Network]], [[keywords/Reinforcement Learning|Deep Reinforcement Learning]]

## 🔗 유사한 논문
- [[An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing_20250919|An Explainable AI Framework for Dynamic Resource Management in Vehicular Network Slicing]] (85.2% similar)
- [[Odin_ Effective End-to-End SLA Decomposition for 5G6G Network Slicing via Online Learning_20250918|Odin Effective End-to-End SLA Decomposition for 5G6G Network Slicing via Online Learning]] (82.0% similar)
- [[Anomaly Detection in Offshore Open Radio Access Network Using Long Short-Term Memory Models on a Novel Artificial Intelligence-Driven Cloud-Native Data Platform_20250918|Anomaly Detection in Offshore Open Radio Access Network Using Long Short-Term Memory Models on a Novel Artificial Intelligence-Driven Cloud-Native Data Platform]] (78.7% similar)
- [[Self-Explaining Reinforcement Learning for Mobile Network Resource Allocation_20250918|Self-Explaining Reinforcement Learning for Mobile Network Resource Allocation]] (77.1% similar)
- [[Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution_20250919|Scalable Multi-Objective Robot Reinforcement Learning through Gradient Conflict Resolution]] (76.7% similar)

## 📋 저자 정보

**Authors:** Peihao Yan, Jie Lu, Huacheng Zeng, Y. Thomas Hou

## 📄 Abstract (원문)

Open-Radio Access Network (O-RAN) has become an important paradigm for 5G and
beyond radio access networks. This paper presents an xApp called xSlice for the
Near-Real-Time (Near-RT) RAN Intelligent Controller (RIC) of 5G O-RANs. xSlice
is an online learning algorithm that adaptively adjusts MAC-layer resource
allocation in response to dynamic network states, including time-varying
wireless channel conditions, user mobility, traffic fluctuations, and changes
in user demand. To address these network dynamics, we first formulate the
Quality-of-Service (QoS) optimization problem as a regret minimization problem
by quantifying the QoS demands of all traffic sessions through weighting their
throughput, latency, and reliability. We then develop a deep reinforcement
learning (DRL) framework that utilizes an actor-critic model to combine the
advantages of both value-based and policy-based updating methods. A graph
convolutional network (GCN) is incorporated as a component of the DRL framework
for graph embedding of RAN data, enabling xSlice to handle a dynamic number of
traffic sessions. We have implemented xSlice on an O-RAN testbed with 10
smartphones and conducted extensive experiments to evaluate its performance in
realistic scenarios. Experimental results show that xSlice can reduce
performance regret by 67% compared to the state-of-the-art solutions. Source
code is available on GitHub [1].

## 🔍 Abstract (한글 번역)

오픈 라디오 액세스 네트워크(O-RAN)은 5G 및 그 이상의 라디오 액세스 네트워크에서 중요한 패러다임이 되었습니다. 이 논문은 5G O-RAN의 근실시간(근RT) RAN 지능형 컨트롤러(RIC)를 위한 xSlice라는 xApp을 소개합니다. xSlice는 시간에 따라 변하는 무선 채널 상태, 사용자 이동성, 트래픽 변동, 사용자 요구의 변화 등 동적인 네트워크 상태에 대응하여 MAC 계층 자원 할당을 적응적으로 조정하는 온라인 학습 알고리즘입니다. 이러한 네트워크 동적성을 해결하기 위해, 우리는 먼저 모든 트래픽 세션의 QoS 요구를 처리량, 지연 시간 및 신뢰성을 가중하여 정량화함으로써 QoS 최적화 문제를 후회 최소화 문제로 공식화합니다. 그런 다음 가치 기반 및 정책 기반 업데이트 방법의 장점을 결합하기 위해 액터-크리틱 모델을 활용하는 심층 강화 학습(DRL) 프레임워크를 개발합니다. 그래프 임베딩을 위해 RAN 데이터를 그래프 형태로 처리할 수 있도록 DRL 프레임워크의 구성 요소로 그래프 컨볼루션 네트워크(GCN)가 통합됩니다. 이를 통해 xSlice는 동적인 수의 트래픽 세션을 처리할 수 있습니다. 우리는 10개의 스마트폰을 사용한 O-RAN 테스트베드에서 xSlice를 구현하고, 현실적인 시나리오에서 그 성능을 평가하기 위한 광범위한 실험을 수행했습니다. 실험 결과에 따르면, xSlice는 최첨단 솔루션에 비해 성능 후회를 67% 감소시킬 수 있음을 보여줍니다. 소스 코드는 GitHub에서 이용할 수 있습니다 [1].

## 📝 요약

이 논문은 5G O-RAN의 Near-Real-Time RAN Intelligent Controller를 위한 xApp인 xSlice를 소개합니다. xSlice는 온라인 학습 알고리즘으로, 네트워크 상태 변화에 따라 MAC 계층의 자원 할당을 적응적으로 조정합니다. 이를 위해 QoS 최적화 문제를 후회 최소화 문제로 공식화하고, 딥 강화 학습(DRL) 프레임워크를 개발하여 가치 기반 및 정책 기반 갱신 방법의 장점을 결합합니다. 또한, 그래프 컨볼루션 네트워크(GCN)를 활용하여 RAN 데이터의 그래프 임베딩을 수행합니다. 실험 결과, xSlice는 최신 솔루션 대비 성능 후회를 67% 감소시켰습니다. 소스 코드는 GitHub에 공개되어 있습니다.

## 🎯 주요 포인트

- 1. O-RAN은 5G 및 그 이상의 무선 접속 네트워크에서 중요한 패러다임으로 자리 잡고 있습니다.

- 2. xSlice는 5G O-RAN의 Near-RT RIC를 위한 xApp으로, 동적 네트워크 상태에 적응하여 MAC 계층의 자원 할당을 조정하는 온라인 학습 알고리즘입니다.

- 3. QoS 최적화 문제를 후회 최소화 문제로 수식화하고, 이를 해결하기 위해 가치 기반 및 정책 기반 업데이트 방법을 결합한 심층 강화 학습(DRL) 프레임워크를 개발했습니다.

- 4. DRL 프레임워크에 그래프 컨볼루션 네트워크(GCN)를 통합하여 RAN 데이터의 그래프 임베딩을 수행하고, 동적인 트래픽 세션 수를 처리할 수 있도록 했습니다.

- 5. 실험 결과, xSlice는 최신 솔루션과 비교하여 성능 후회를 67% 감소시킬 수 있음을 보여주었습니다.

---

*Generated on 2025-09-20 07:38:07*