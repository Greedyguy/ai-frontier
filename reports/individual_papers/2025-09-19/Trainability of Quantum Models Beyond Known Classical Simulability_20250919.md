
# Trainability of Quantum Models Beyond Known Classical Simulability

**Korean Title:** 양자 모델의 훈련 가능성: 알려진 고전적 시뮬레이션 가능성을 넘어

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Quantum Advantage

## 🔗 유사한 논문
- [[Learning quantum many-body data locally A provably scalable framework]] (81.7% similar)
- [[Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit_20250918|Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit]] (81.5% similar)
- [[Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (78.9% similar)
- [[Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (78.7% similar)
- [[Hybrid Quantum-Classical Model for Image Classification]] (77.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.06344v2 Announce Type: replace-cross 
Abstract: Variational Quantum Algorithms (VQAs) are promising candidates for near-term quantum computing, yet they face scalability challenges due to barren plateaus, where gradients vanish exponentially in the system size. Recent conjectures suggest that avoiding barren plateaus might inherently lead to classical simulability, thus limiting the opportunities for quantum advantage. In this work, we advance the theoretical understanding of the relationship between the trainability and computational complexity of VQAs, thus directly addressing the conjecture. We introduce the Linear Clifford Encoder (LCE), a novel technique that ensures constant-scaling gradient statistics on optimization landscape regions that are close to Clifford circuits. Additionally, we leverage classical Taylor surrogates to reveal computational complexity phase transitions from polynomial to super-polynomial as the initialization region size increases. Combining these results, we reveal a deeper link between trainability and computational complexity, and analytically prove that barren plateaus can be avoided in regions for which no classical surrogate is known to exist. Furthermore, numerical experiments on LCE transformed landscapes confirm in practice the existence of a super-polynomially complex ``transition zone'' where gradients decay polynomially. These findings indicate a plausible path to practically relevant, barren plateau-free variational models with potential for quantum advantage.

## 🔍 Abstract (한글 번역)

arXiv:2507.06344v2 발표 유형: 교체-교차  
초록: 변분 양자 알고리즘(VQAs)은 근시일 내에 양자 컴퓨팅의 유망한 후보로 여겨지지만, 시스템 크기에 따라 기울기가 지수적으로 사라지는 불모지 문제로 인해 확장성에 어려움을 겪고 있습니다. 최근의 추측은 불모지를 피하는 것이 본질적으로 고전적 모의 가능성으로 이어질 수 있으며, 이는 양자 우위의 기회를 제한할 수 있다고 제안합니다. 본 연구에서는 VQAs의 훈련 가능성과 계산 복잡성 간의 관계에 대한 이론적 이해를 발전시켜 이 추측을 직접적으로 다룹니다. 우리는 클리포드 회로에 가까운 최적화 경관 영역에서 일정한 스케일링 기울기 통계를 보장하는 새로운 기술인 선형 클리포드 인코더(LCE)를 소개합니다. 또한, 고전적 테일러 대리모델을 활용하여 초기화 영역 크기가 증가함에 따라 계산 복잡성이 다항식에서 초다항식으로 전환되는 단계를 드러냅니다. 이러한 결과를 결합하여 훈련 가능성과 계산 복잡성 간의 더 깊은 연결을 밝히고, 고전적 대리모델이 존재하지 않는 영역에서 불모지를 피할 수 있음을 분석적으로 증명합니다. 더 나아가, LCE 변환 경관에 대한 수치 실험은 기울기가 다항식적으로 감소하는 초다항식적 복잡성의 "전환 영역"이 실제로 존재함을 확인합니다. 이러한 발견은 양자 우위의 잠재력을 가진 실질적으로 관련 있는 불모지 없는 변분 모델로 가는 가능성 있는 경로를 제시합니다.

## 📝 요약

이 논문은 변분 양자 알고리즘(VQAs)의 훈련 가능성과 계산 복잡성 간의 관계를 이론적으로 발전시킵니다. VQAs는 불모지 문제로 인해 확장성에 한계가 있지만, 이를 회피하면 고전적 시뮬레이션 가능성이 증가하여 양자 우위가 제한될 수 있다는 가설이 있습니다. 저자들은 Linear Clifford Encoder(LCE)를 도입하여 Clifford 회로에 가까운 최적화 경관에서 일정한 기울기 통계를 보장합니다. 또한, 고전적 테일러 대리모델을 사용하여 초기화 영역 크기에 따라 계산 복잡성이 다항식에서 초다항식으로 전환되는 과정을 밝힙니다. 이러한 결과를 통해 훈련 가능성과 계산 복잡성 간의 깊은 연결을 드러내고, 고전적 대리모델이 존재하지 않는 영역에서 불모지 문제를 회피할 수 있음을 이론적으로 증명합니다. 수치 실험을 통해 초다항식 복잡성을 가진 "전이 영역"의 존재를 확인하였으며, 이는 실질적으로 유의미한 불모지 문제 없는 변분 모델 개발 가능성을 시사합니다.

## 🎯 주요 포인트

- 1. 변분 양자 알고리즘(VQAs)은 근시일 내 양자 컴퓨팅의 유망한 후보지만, 시스템 크기에 따라 기울기가 지수적으로 사라지는 barren plateaus 문제로 확장성에 어려움을 겪고 있습니다.

- 2. barren plateaus를 피하는 것이 본질적으로 고전적 시뮬레이션 가능성을 초래할 수 있으며, 이는 양자 우위의 기회를 제한할 수 있다는 최근의 추측이 있습니다.

- 3. 본 연구에서는 VQAs의 훈련 가능성과 계산 복잡성 간의 관계를 이론적으로 이해하고, Linear Clifford Encoder(LCE)라는 새로운 기법을 도입하여 Clifford 회로에 가까운 최적화 지형에서 일정한 기울기 통계를 보장합니다.

- 4. 고전적 테일러 대리모델을 활용하여 초기화 영역 크기가 증가함에 따라 계산 복잡성이 다항식에서 초다항식으로 전환되는 과도기를 밝혀냈습니다.

- 5. LCE 변환 지형에 대한 수치 실험은 기울기가 다항식으로 감소하는 초다항식 복잡성의 "전환 구역"의 존재를 실증적으로 확인하였으며, 이는 실질적으로 유의미한 barren plateau-free 변분 모델로의 가능성을 시사합니다.

---

*Generated on 2025-09-19 15:46:46*