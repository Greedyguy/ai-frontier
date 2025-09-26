---
keywords:
  - Stochastic Hybrid Systems
  - Augmented Control Barrier Certificates
  - Safety Controller Synthesis
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2409.10018
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:51:55.505831",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Stochastic Hybrid Systems",
    "Augmented Control Barrier Certificates",
    "Safety Controller Synthesis"
  ],
  "rejected_keywords": [
    "Sum-of-Squares Optimization"
  ],
  "similarity_scores": {
    "Stochastic Hybrid Systems": 0.78,
    "Augmented Control Barrier Certificates": 0.7,
    "Safety Controller Synthesis": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Compositional Design of Safety Controllers for Large-scale Stochastic Hybrid Systems

**Korean Title:** 대규모 확률적 하이브리드 시스템을 위한 안전 제어기의 구성적 설계

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Stochastic Hybrid Systems|stochastic hybrid systems]], [[keywords/Augmented Control Barrier Certificates|augmented control barrier certificates]], [[keywords/Safety Controller Synthesis|safety controller synthesis]]

## 🔗 유사한 논문
- [[Digital Twin-based Cooperative Autonomous Driving in Smart Intersections A Multi-Agent Reinforcement Learning Approach]] (81.1% similar)
- [[The Sum Leaks More Than Its Parts Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (78.5% similar)
- [[TopoSizing An LLM-aided Framework of Topology-based Understanding and Sizing for AMS Circuits]] (78.3% similar)
- [[AdapJ An Adaptive Extended Jacobian Controller for Soft Manipulators]] (78.0% similar)
- [[Privacy-Preserving Uncertainty Disclosure for Facilitating Enhanced Energy Storage Dispatch]] (77.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.10018v2 Announce Type: replace 
Abstract: In this work, we propose a compositional scheme based on small-gain reasoning for the safety controller synthesis of interconnected stochastic hybrid systems with both continuous evolutions and instantaneous jumps. In our proposed setting, we first offer an augmented scheme to represent each stochastic hybrid subsystem with continuous and discrete evolutions in a unified framework, ensuring that the state trajectories match those of the original hybrid systems. We then introduce the concept of augmented control sub-barrier certificates (A-CSBC) for each subsystem, which allows the construction of augmented control barrier certificates (A-CBC) for interconnected systems and their safety controllers under small-gain compositional conditions. We eventually leverage the constructed A-CBC and quantify a guaranteed probabilistic bound across the safety of the interconnected system. While the computational complexity of designing a barrier certificate and its safety controller grows polynomially with network dimension using sum-of-squares (SOS) optimization program, our compositional approach significantly reduces it to a linear scale with respect to the number of subsystems. We verify the efficacy of our proposed approach over an interconnected stochastic hybrid system composed of 1000 nonlinear subsystems with two distinct interconnection topologies.

## 🔍 Abstract (한글 번역)

arXiv:2409.10018v2 발표 유형: 교체  
초록: 본 연구에서는 연속적인 진화와 순간적인 점프를 모두 포함하는 상호 연결된 확률적 하이브리드 시스템의 안전 제어기 합성을 위해 소득 이득 추론에 기반한 구성적 방식을 제안합니다. 제안된 설정에서는 먼저 연속적 및 이산적 진화를 통합된 프레임워크로 표현하여 각 확률적 하이브리드 하위 시스템을 나타내는 증강된 방식을 제공하며, 이를 통해 상태 궤적이 원래 하이브리드 시스템의 궤적과 일치하도록 보장합니다. 그런 다음, 각 하위 시스템에 대해 증강된 제어 하위 장벽 증명서(A-CSBC)의 개념을 도입하여, 소득 이득 구성 조건 하에서 상호 연결된 시스템과 그 안전 제어기를 위한 증강된 제어 장벽 증명서(A-CBC)를 구축할 수 있게 합니다. 최종적으로, 구축된 A-CBC를 활용하여 상호 연결된 시스템의 안전성에 대한 보장된 확률적 경계를 정량화합니다. 장벽 증명서와 그 안전 제어기를 설계하는 데 있어 합의 제곱(SOS) 최적화 프로그램을 사용하면 네트워크 차원에 따라 계산 복잡도가 다항적으로 증가하지만, 우리의 구성적 접근 방식은 하위 시스템의 수에 비례하여 선형적으로 이를 크게 줄입니다. 우리는 두 가지 상호 연결 토폴로지를 가진 1000개의 비선형 하위 시스템으로 구성된 상호 연결된 확률적 하이브리드 시스템을 통해 제안된 접근 방식의 효능을 검증합니다.

## 📝 요약

이 연구는 연속적 진화와 순간적 점프를 포함하는 상호 연결된 확률적 하이브리드 시스템의 안전 제어기 합성을 위한 소규모 이득 추론 기반의 합성 방식을 제안합니다. 각 확률적 하이브리드 하위 시스템을 통합된 프레임워크로 표현하여 원래 시스템의 상태 궤적과 일치하도록 하며, 이를 통해 상호 연결된 시스템과 안전 제어기를 위한 보강된 제어 장벽 증명서를 구성합니다. 이로써 상호 연결된 시스템의 안전성을 보장하는 확률적 경계를 정량화합니다. 제안된 방법은 네트워크 차원에 따라 장벽 증명서와 안전 제어기를 설계하는 계산 복잡도를 선형적으로 줄이며, 1000개의 비선형 하위 시스템으로 구성된 시스템에서 그 효율성을 검증했습니다.

## 🎯 주요 포인트

- 1. 본 연구는 연속적 진화와 순간적 점프를 포함하는 상호 연결된 확률적 하이브리드 시스템의 안전 제어기 합성을 위한 소규모 이득 추론 기반의 구성적 방법을 제안합니다.

- 2. 각 확률적 하이브리드 하위 시스템을 통합된 프레임워크로 표현하기 위한 확장된 스킴을 제공하여 원래 하이브리드 시스템의 상태 궤적과 일치하도록 합니다.

- 3. 각 하위 시스템에 대해 확장된 제어 서브 배리어 인증서(A-CSBC)의 개념을 도입하여 상호 연결된 시스템과 그 안전 제어기의 확장된 제어 배리어 인증서(A-CBC)를 구성합니다.

- 4. 제안된 방법은 상호 연결된 시스템의 안전성을 보장하는 확률적 경계를 정량화하며, 네트워크 차원에 따라 배리어 인증서 설계의 계산 복잡성을 선형적으로 감소시킵니다.

- 5. 제안된 접근 방식의 효능은 두 가지 상호 연결 토폴로지를 가진 1000개의 비선형 하위 시스템으로 구성된 상호 연결된 확률적 하이브리드 시스템에서 검증되었습니다.

---

*Generated on 2025-09-19 16:46:22*