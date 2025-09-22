# Instance Generation for Meta-Black-Box Optimization through Latent Space Reverse Engineering

**Korean Title:** 잠재 공간 역공학을 통한 메타 블랙박스 최적화를 위한 인스턴스 생성

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Meta Black Box Optimization

## 🔗 유사한 논문
- [[2025-09-19/Constructive Conflict-Driven Multi-Agent Reinforcement Learning for Strategic Diversity_20250919|Constructive Conflict-Driven Multi-Agent Reinforcement Learning for Strategic Diversity]] (79.9% similar)
- [[2025-09-19/Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization_20250919|Multi-Fidelity Hybrid Reinforcement Learning via Information Gain Maximization]] (79.6% similar)
- [[2025-09-19/Opening the Black Box_ Interpretable LLMs via Semantic Resonance Architecture_20250919|Opening the Black Box Interpretable LLMs via Semantic Resonance Architecture]] (79.2% similar)
- [[2025-09-19/From Correction to Mastery_ Reinforced Distillation of Large Language Model Agents_20250919|From Correction to Mastery Reinforced Distillation of Large Language Model Agents]] (78.9% similar)
- [[2025-09-19/Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision_20250919|Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision]] (78.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15810v1 Announce Type: cross 
Abstract: To relieve intensive human-expertise required to design optimization algorithms, recent Meta-Black-Box Optimization (MetaBBO) researches leverage generalization strength of meta-learning to train neural network-based algorithm design policies over a predefined training problem set, which automates the adaptability of the low-level optimizers on unseen problem instances. Currently, a common training problem set choice in existing MetaBBOs is well-known benchmark suites CoCo-BBOB. Although such choice facilitates the MetaBBO's development, problem instances in CoCo-BBOB are more or less limited in diversity, raising the risk of overfitting of MetaBBOs, which might further results in poor generalization. In this paper, we propose an instance generation approach, termed as \textbf{LSRE}, which could generate diverse training problem instances for MetaBBOs to learn more generalizable policies. LSRE first trains an autoencoder which maps high-dimensional problem features into a 2-dimensional latent space. Uniform-grid sampling in this latent space leads to hidden representations of problem instances with sufficient diversity. By leveraging a genetic-programming approach to search function formulas with minimal L2-distance to these hidden representations, LSRE reverse engineers a diversified problem set, termed as \textbf{Diverse-BBO}. We validate the effectiveness of LSRE by training various MetaBBOs on Diverse-BBO and observe their generalization performances on either synthetic or realistic scenarios. Extensive experimental results underscore the superiority of Diverse-BBO to existing training set choices in MetaBBOs. Further ablation studies not only demonstrate the effectiveness of design choices in LSRE, but also reveal interesting insights on instance diversity and MetaBBO's generalization.

## 🔍 Abstract (한글 번역)

arXiv:2509.15810v1 발표 유형: 교차  
초록: 최적화 알고리즘 설계에 요구되는 집중적인 인간 전문성을 완화하기 위해, 최근의 메타 블랙박스 최적화(MetaBBO) 연구는 메타 학습의 일반화 능력을 활용하여 사전 정의된 훈련 문제 집합에서 신경망 기반 알고리즘 설계 정책을 훈련함으로써, 보이지 않는 문제 인스턴스에 대한 저수준 최적화기의 적응성을 자동화합니다. 현재 기존 MetaBBO에서 일반적인 훈련 문제 집합 선택은 잘 알려진 벤치마크 스위트 CoCo-BBOB입니다. 이러한 선택은 MetaBBO의 개발을 촉진하지만, CoCo-BBOB의 문제 인스턴스는 다양성이 다소 제한되어 있어 MetaBBO의 과적합 위험을 초래할 수 있으며, 이는 더 나아가 일반화 성능 저하로 이어질 수 있습니다. 본 논문에서는 MetaBBO가 보다 일반화 가능한 정책을 학습할 수 있도록 다양한 훈련 문제 인스턴스를 생성할 수 있는 인스턴스 생성 접근법인 \textbf{LSRE}를 제안합니다. LSRE는 먼저 고차원 문제 특징을 2차원 잠재 공간으로 매핑하는 오토인코더를 훈련합니다. 이 잠재 공간에서의 균일 그리드 샘플링은 충분한 다양성을 가진 문제 인스턴스의 숨겨진 표현을 이끌어냅니다. 이러한 숨겨진 표현과의 최소 L2 거리로 함수 공식을 탐색하기 위해 유전 프로그래밍 접근법을 활용함으로써, LSRE는 \textbf{Diverse-BBO}라고 명명된 다양한 문제 집합을 역설계합니다. Diverse-BBO에서 다양한 MetaBBO를 훈련하고, 이를 통해 합성 또는 현실적인 시나리오에서의 일반화 성능을 관찰함으로써 LSRE의 효과를 검증합니다. 광범위한 실험 결과는 MetaBBO의 기존 훈련 세트 선택에 대한 Diverse-BBO의 우수성을 강조합니다. 추가적인 소거 연구는 LSRE의 설계 선택의 효과를 입증할 뿐만 아니라 인스턴스 다양성과 MetaBBO의 일반화에 대한 흥미로운 통찰을 제공합니다.

## 📝 요약

이 논문은 최적화 알고리즘 설계에 필요한 인간 전문가의 노력을 줄이기 위해 메타 학습을 활용한 Meta-Black-Box Optimization (MetaBBO) 연구를 다룹니다. 기존의 MetaBBO는 CoCo-BBOB와 같은 제한된 다양성의 벤치마크를 사용하여 과적합 위험이 있었습니다. 이를 해결하기 위해, 저자들은 LSRE라는 인스턴스 생성 방법을 제안합니다. LSRE는 고차원 문제 특징을 2차원 잠재 공간으로 매핑하는 오토인코더를 사용하여 다양한 문제 인스턴스를 생성합니다. 이 방법은 다양한 문제 세트인 Diverse-BBO를 역설계하여 MetaBBO의 일반화 성능을 향상시킵니다. 실험 결과, Diverse-BBO가 기존의 훈련 세트보다 우수하며, LSRE의 설계 선택이 효과적임을 보여줍니다.

## 🎯 주요 포인트

- 1. MetaBBO는 메타러닝의 일반화 능력을 활용하여 미리 정의된 문제 세트에서 신경망 기반 알고리즘 설계 정책을 훈련함으로써 새로운 문제에 대한 적응성을 자동화합니다.

- 2. 기존 MetaBBO 연구에서 사용되는 CoCo-BBOB 벤치마크는 다양성이 제한되어 있어 과적합의 위험이 있으며, 이는 일반화 성능 저하로 이어질 수 있습니다.

- 3. LSRE는 고차원 문제 특징을 2차원 잠재 공간으로 매핑하는 오토인코더를 훈련하여 다양한 문제 인스턴스를 생성하고, 이를 통해 MetaBBO의 일반화 가능한 정책 학습을 지원합니다.

- 4. LSRE는 유전 프로그래밍을 활용하여 다양한 문제 세트를 역설계하고, 이를 Diverse-BBO라고 명명하여 MetaBBO의 일반화 성능을 향상시킵니다.

- 5. 다양한 실험 결과는 Diverse-BBO가 기존의 MetaBBO 훈련 세트 선택보다 우수하다는 것을 강조하며, LSRE의 설계 선택의 효과성과 인스턴스 다양성 및 MetaBBO의 일반화에 대한 흥미로운 통찰을 제공합니다.

---

*Generated on 2025-09-22 14:12:56*