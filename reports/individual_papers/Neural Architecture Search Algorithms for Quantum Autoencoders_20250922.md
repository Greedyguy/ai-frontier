# Neural Architecture Search Algorithms for Quantum Autoencoders

**Korean Title:** 양자 오토인코더를 위한 신경망 구조 탐색 알고리즘

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Quantum Autoencoders

## 🔗 유사한 논문
- [[2025-09-17/Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks_20250917|Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks]] (81.8% similar)
- [[2025-09-17/Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment_20250917|Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (79.8% similar)
- [[2025-09-18/Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit_20250918|Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit]] (79.5% similar)
- [[2025-09-19/Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (79.3% similar)
- [[2025-09-22/KNARsack_ Teaching Neural Algorithmic Reasoners to Solve Pseudo-Polynomial Problems_20250922|KNARsack Teaching Neural Algorithmic Reasoners to Solve Pseudo-Polynomial Problems]] (78.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15451v1 Announce Type: cross 
Abstract: The design of quantum circuits is currently driven by the specific objectives of the quantum algorithm in question. This approach thus relies on a significant manual effort by the quantum algorithm designer to design an appropriate circuit for the task. However this approach cannot scale to more complex quantum algorithms in the future without exponentially increasing the circuit design effort and introducing unwanted inductive biases. Motivated by this observation, we propose to automate the process of cicuit design by drawing inspiration from Neural Architecture Search (NAS). In this work, we propose two Quantum-NAS algorithms that aim to find efficient circuits given a particular quantum task. We choose quantum data compression as our driver quantum task and demonstrate the performance of our algorithms by finding efficient autoencoder designs that outperform baselines on three different tasks - quantum data denoising, classical data compression and pure quantum data compression. Our results indicate that quantum NAS algorithms can significantly alleviate the manual effort while delivering performant quantum circuits for any given task.

## 🔍 Abstract (한글 번역)

arXiv:2509.15451v1 발표 유형: 교차  
초록: 양자 회로 설계는 현재 문제의 양자 알고리즘의 특정 목표에 의해 주도됩니다. 이 접근 방식은 따라서 양자 알고리즘 설계자가 작업에 적합한 회로를 설계하기 위해 상당한 수작업을 필요로 합니다. 그러나 이 접근 방식은 미래에 더 복잡한 양자 알고리즘으로 확장할 수 없으며, 회로 설계 노력을 기하급수적으로 증가시키고 원치 않는 귀납적 편향을 도입할 수 있습니다. 이러한 관찰에 동기 부여되어, 우리는 신경망 아키텍처 검색(NAS)에서 영감을 받아 회로 설계 과정을 자동화할 것을 제안합니다. 이 연구에서 우리는 특정 양자 작업에 대해 효율적인 회로를 찾기 위한 두 가지 양자-NAS 알고리즘을 제안합니다. 우리는 양자 데이터 압축을 우리의 주 양자 작업으로 선택하고, 세 가지 다른 작업 - 양자 데이터 잡음 제거, 고전적 데이터 압축 및 순수 양자 데이터 압축 - 에서 기준선을 능가하는 효율적인 오토인코더 설계를 찾아 우리의 알고리즘 성능을 입증합니다. 우리의 결과는 양자 NAS 알고리즘이 주어진 작업에 대해 성능이 뛰어난 양자 회로를 제공하면서 수작업을 상당히 줄일 수 있음을 나타냅니다.

## 📝 요약

이 논문은 양자 회로 설계를 자동화하기 위해 신경망 아키텍처 검색(NAS)에서 영감을 받아 두 가지 Quantum-NAS 알고리즘을 제안합니다. 기존에는 양자 알고리즘 설계자가 수작업으로 회로를 설계했으나, 이는 복잡한 알고리즘에 비효율적입니다. 제안된 알고리즘은 양자 데이터 압축을 주요 과제로 삼아, 양자 데이터 노이즈 제거, 고전적 데이터 압축, 순수 양자 데이터 압축에서 기존 방법보다 우수한 성능을 보이는 효율적인 오토인코더 설계를 발견했습니다. 결과적으로, Quantum-NAS 알고리즘은 수작업 노력을 줄이면서도 성능 좋은 양자 회로를 제공할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 현재의 양자 회로 설계는 특정 양자 알고리즘의 목표에 따라 수작업으로 이루어지고 있어, 복잡한 양자 알고리즘에는 확장성이 부족합니다.

- 2. Neural Architecture Search (NAS)에서 영감을 받아 양자 회로 설계 과정을 자동화하는 방법을 제안합니다.

- 3. 제안된 두 가지 Quantum-NAS 알고리즘은 특정 양자 작업에 적합한 효율적인 회로를 찾는 것을 목표로 합니다.

- 4. 양자 데이터 압축을 주요 작업으로 설정하고, 제안된 알고리즘이 양자 데이터 노이즈 제거, 고전 데이터 압축, 순수 양자 데이터 압축에서 기존 기준을 능가하는 성능을 보임을 입증했습니다.

- 5. Quantum-NAS 알고리즘은 수작업의 노력을 크게 줄이면서도 주어진 작업에 대해 성능 좋은 양자 회로를 제공할 수 있음을 시사합니다.

---

*Generated on 2025-09-22 15:38:26*