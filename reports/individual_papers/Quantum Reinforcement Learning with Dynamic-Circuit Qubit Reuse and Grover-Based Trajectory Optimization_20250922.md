# Quantum Reinforcement Learning with Dynamic-Circuit Qubit Reuse and Grover-Based Trajectory Optimization

**Korean Title:** 양자 강화 학습: 동적 회로 큐비트 재사용 및 그로버 기반 궤적 최적화

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/specific/Dynamic Circuit Qubit Reuse|Dynamic Circuit Qubit Reuse]] [[keywords/specific/Grovers Algorithm|Grovers Algorithm]] [[keywords/broad/Quantum Reinforcement Learning|Quantum Reinforcement Learning]] [[keywords/unique/Quantum Markov Decision Process|Quantum Markov Decision Process]] [[categories/cs.LG|cs.LG]] [[2025-09-17/Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures_20250917|Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures]] (83.6% similar) [[2025-09-17/Learning quantum many-body data locally_ A provably scalable framework_20250917|Learning quantum many-body data locally: A provably scalable framework]] (82.4% similar) [[2025-09-17/Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment_20250917|Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Quantum Markov Decision Process
**🔗 Specific Connectable**: Grovers Algorithm
**🔬 Broad Technical**: Quantum Reinforcement Learning
**⭐ Unique Technical**: Dynamic Circuit Qubit Reuse
## 🔗 유사한 논문
- [[2025-09-17/Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures_20250917|Quantum Reinforcement Learning-Guided Diffusion Model for Image Synthesis via Hybrid Quantum-Classical Generative Model Architectures]] (83.6% similar)
- [[2025-09-17/Learning quantum many-body data locally_ A provably scalable framework_20250917|Learning quantum many-body data locally A provably scalable framework]] (82.4% similar)
- [[2025-09-17/Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment_20250917|Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (82.2% similar)
- [[2025-09-17/Efficiently learning depth-3 circuits via quantum agnostic boosting_20250917|Efficiently learning depth-3 circuits via quantum agnostic boosting]] (81.7% similar)
- [[2025-09-17/Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks_20250917|Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks]] (81.7% similar)


**ArXiv ID**: [2509.16002](https://arxiv.org/abs/2509.16002)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.16002.pdf)


**ArXiv ID**: [2509.16002](https://arxiv.org/abs/2509.16002)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.16002.pdf)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: Grovers Algorithm, Quantum Markov Decision Process
**⭐ Unique Technical**: Dynamic Circuit Qubit Reuse
**🔬 Broad Technical**: Quantum Reinforcement Learning

## 🏷️ 추출된 키워드



`Quantum Computing` • 

`Reinforcement Learning` • 

`Grovers Algorithm` • 

`Quantum Markov Decision Process` • 

`Dynamic Circuit Qubit Reuse`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16002v1 Announce Type: cross 
Abstract: A fully quantum reinforcement learning framework is developed that integrates a quantum Markov decision process, dynamic circuit-based qubit reuse, and Grover's algorithm for trajectory optimization. The framework encodes states, actions, rewards, and transitions entirely within the quantum domain, enabling parallel exploration of state-action sequences through superposition and eliminating classical subroutines. Dynamic circuit operations, including mid-circuit measurement and reset, allow reuse of the same physical qubits across multiple agent-environment interactions, reducing qubit requirements from 7*T to 7 for T time steps while preserving logical continuity. Quantum arithmetic computes trajectory returns, and Grover's search is applied to the superposition of these evaluated trajectories to amplify the probability of measuring those with the highest return, thereby accelerating the identification of the optimal policy. Simulations demonstrate that the dynamic-circuit-based implementation preserves trajectory fidelity while reducing qubit usage by 66 percent relative to the static design. Experimental deployment on IBM Heron-class quantum hardware confirms that the framework operates within the constraints of current quantum processors and validates the feasibility of fully quantum multi-step reinforcement learning under noisy intermediate-scale quantum conditions. This framework advances the scalability and practical application of quantum reinforcement learning for large-scale sequential decision-making tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.16002v1 발표 유형: 교차  
초록: 완전한 양자 강화 학습 프레임워크가 개발되었으며, 이는 양자 마르코프 결정 과정, 동적 회로 기반 큐비트 재사용, 그리고 궤적 최적화를 위한 그로버 알고리즘을 통합합니다. 이 프레임워크는 상태, 행동, 보상 및 전이를 완전히 양자 영역 내에 인코딩하여 중첩을 통한 상태-행동 시퀀스의 병렬 탐색을 가능하게 하고 고전적 서브루틴을 제거합니다. 중간 회로 측정 및 리셋을 포함한 동적 회로 연산은 여러 에이전트-환경 상호작용에서 동일한 물리적 큐비트를 재사용할 수 있게 하여, T 시간 단계에서 큐비트 요구 사항을 7*T에서 7로 줄이면서 논리적 연속성을 유지합니다. 양자 산술은 궤적 반환을 계산하며, 그로버 검색은 평가된 궤적의 중첩에 적용되어 가장 높은 반환을 가진 궤적을 측정할 확률을 증폭시켜 최적 정책의 식별을 가속화합니다. 시뮬레이션은 동적 회로 기반 구현이 궤적 충실도를 유지하면서 정적 설계에 비해 큐비트 사용을 66% 줄임을 보여줍니다. IBM Heron급 양자 하드웨어에서의 실험적 배포는 프레임워크가 현재 양자 프로세서의 제약 내에서 작동함을 확인하고, 노이즈가 있는 중간 규모 양자 조건에서 완전한 양자 다단계 강화 학습의 실현 가능성을 검증합니다. 이 프레임워크는 대규모 순차적 의사결정 작업을 위한 양자 강화 학습의 확장성과 실용적 적용을 진전시킵니다.

## 📝 요약

이 논문은 완전한 양자 강화 학습 프레임워크를 제안합니다. 이 프레임워크는 양자 마르코프 결정 과정, 동적 회로 기반 큐비트 재사용, 그리고 Grover 알고리즘을 통합하여 경로 최적화를 수행합니다. 상태, 행동, 보상, 전이를 양자 영역 내에서 인코딩하여 상태-행동 시퀀스를 병렬로 탐색하고, 고전적 서브루틴을 제거합니다. 동적 회로 연산을 통해 동일한 물리적 큐비트를 여러 상호작용에 재사용하여 큐비트 요구량을 크게 줄입니다. Grover 알고리즘을 사용하여 최적의 정책을 빠르게 식별합니다. 시뮬레이션 결과, 이 구현은 큐비트 사용을 66% 줄이면서 경로의 정확성을 유지합니다. IBM Heron-class 양자 하드웨어에서의 실험은 이 프레임워크가 현재 양자 프로세서의 제약 내에서 작동함을 확인하고, 대규모 순차적 의사결정 작업에 양자 강화 학습의 확장 가능성과 실용성을 입증합니다.

## 🎯 주요 포인트


- 1. 완전한 양자 강화 학습 프레임워크는 양자 마르코프 결정 과정, 동적 회로 기반 큐비트 재사용, 그리고 그로버 알고리즘을 통합하여 경로 최적화를 수행합니다.

- 2. 동적 회로 연산을 통해 동일한 물리적 큐비트를 여러 에이전트-환경 상호작용에 재사용함으로써 큐비트 요구량을 크게 줄입니다.

- 3. 그로버의 검색 알고리즘을 사용하여 최적의 정책을 가속적으로 식별하며, 이는 경로 반환이 높은 상태-행동 시퀀스의 측정 확률을 증폭시킵니다.

- 4. 시뮬레이션 결과, 동적 회로 기반 구현은 경로 충실도를 유지하면서 큐비트 사용을 66% 감소시킵니다.

- 5. IBM Heron-class 양자 하드웨어에서의 실험적 배포는 현재 양자 프로세서의 제약 내에서 프레임워크가 작동함을 확인하고, 소음이 있는 중간 규모 양자 조건에서의 다단계 강화 학습의 실현 가능성을 검증합니다.


---

*Generated on 2025-09-22 15:46:25*