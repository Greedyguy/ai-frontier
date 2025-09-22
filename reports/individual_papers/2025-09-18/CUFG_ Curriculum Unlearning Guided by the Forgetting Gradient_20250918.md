# CUFG: Curriculum Unlearning Guided by the Forgetting Gradient

**Korean Title:** CUFG: 망각 기울기에 의해 안내되는 커리큘럼 비학습

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Jiaxing Miao|Jiaxing Miao]] [[authors/Liang Hu|Liang Hu]] [[authors/Qi Zhang|Qi Zhang]] [[authors/Lai Zhong Yuan|Lai Zhong Yuan]] [[authors/Usman Naseem|Usman Naseem]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Curriculum Unlearning

## 🔗 유사한 논문
- [[Towards a Real-World Aligned Benchmark for Unlearning in Recommender Systems_20250919|Towards a Real-World Aligned Benchmark for Unlearning in Recommender Systems]] (82.5% similar)
- [[HAM_ Hierarchical Adapter Merging for Scalable Continual Learning_20250918|HAM Hierarchical Adapter Merging for Scalable Continual Learning]] (80.7% similar)
- [[Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (79.4% similar)
- [[Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning_20250918|Hybrid Diffusion Policies with Projective Geometric Algebra for Efficient Robot Manipulation Learning]] (79.0% similar)
- [[LNE-Blocking_ An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models_20250918|LNE-Blocking An Efficient Framework for Contamination Mitigation Evaluation on Large Language Models]] (78.5% similar)

## 📋 저자 정보

**Authors:** Jiaxing Miao, Liang Hu, Qi Zhang, Lai Zhong Yuan, Usman Naseem

## 📄 Abstract (원문)

As privacy and security take center stage in AI, machine unlearning, the
ability to erase specific knowledge from models, has garnered increasing
attention. However, existing methods overly prioritize efficiency and
aggressive forgetting, which introduces notable limitations. In particular,
radical interventions like gradient ascent, influence functions, and random
label noise can destabilize model weights, leading to collapse and reduced
reliability. To address this, we propose CUFG (Curriculum Unlearning via
Forgetting Gradients), a novel framework that enhances the stability of
approximate unlearning through innovations in both forgetting mechanisms and
data scheduling strategies. Specifically, CUFG integrates a new gradient
corrector guided by forgetting gradients for fine-tuning-based unlearning and a
curriculum unlearning paradigm that progressively forgets from easy to hard.
These innovations narrow the gap with the gold-standard Retrain method by
enabling more stable and progressive unlearning, thereby improving both
effectiveness and reliability. Furthermore, we believe that the concept of
curriculum unlearning has substantial research potential and offers
forward-looking insights for the development of the MU field. Extensive
experiments across various forgetting scenarios validate the rationale and
effectiveness of our approach and CUFG. Codes are available at
https://anonymous.4open.science/r/CUFG-6375.

## 🔍 Abstract (한글 번역)

AI 분야에서 프라이버시와 보안이 중심 무대에 오르면서, 모델에서 특정 지식을 삭제할 수 있는 기계 학습의 '잊기' 기능이 점점 더 많은 주목을 받고 있습니다. 그러나 기존 방법들은 효율성과 공격적인 잊기를 지나치게 우선시하여 상당한 한계를 초래합니다. 특히, 기울기 상승, 영향 함수, 무작위 레이블 노이즈와 같은 급진적인 개입은 모델 가중치를 불안정하게 만들어 붕괴와 신뢰성 저하를 초래할 수 있습니다. 이를 해결하기 위해 우리는 CUFG(Curriculum Unlearning via Forgetting Gradients)라는 새로운 프레임워크를 제안합니다. 이는 잊기 메커니즘과 데이터 스케줄링 전략 모두에서 혁신을 통해 근사적 잊기의 안정성을 향상시킵니다. 구체적으로, CUFG는 잊기 기울기에 의해 안내되는 새로운 기울기 보정기를 통합하여 미세 조정 기반의 잊기를 수행하며, 쉬운 것부터 어려운 것까지 점진적으로 잊는 커리큘럼 잊기 패러다임을 도입합니다. 이러한 혁신은 보다 안정적이고 점진적인 잊기를 가능하게 하여, 효과성과 신뢰성을 모두 개선함으로써 금표준인 재훈련 방법과의 격차를 좁힙니다. 또한, 커리큘럼 잊기 개념은 상당한 연구 잠재력을 지니고 있으며, MU 분야의 발전을 위한 미래 지향적인 통찰력을 제공합니다. 다양한 잊기 시나리오에 걸친 광범위한 실험은 우리의 접근 방식과 CUFG의 합리성과 효과성을 검증합니다. 코드는 https://anonymous.4open.science/r/CUFG-6375에서 확인할 수 있습니다.

## 📝 요약

AI에서 프라이버시와 보안이 중요해지면서 특정 지식을 모델에서 제거하는 '기계 학습 삭제'가 주목받고 있습니다. 기존 방법들은 효율성과 공격적인 삭제에 중점을 두어 모델의 안정성을 해치는 문제를 가지고 있습니다. 이를 해결하기 위해, 우리는 CUFG(Curriculum Unlearning via Forgetting Gradients)라는 새로운 프레임워크를 제안합니다. CUFG는 잊기 기울기를 활용한 새로운 기울기 보정기와 쉬운 것부터 어려운 것 순으로 점진적으로 잊는 커리큘럼 학습 패러다임을 통합하여 안정성과 효과성을 높입니다. 이 접근법은 재학습 방법과의 격차를 줄이며, 다양한 실험을 통해 그 효과와 타당성을 입증했습니다. CUFG는 기계 학습 삭제 분야의 발전에 중요한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 기계 학습 모델에서 특정 지식을 지우는 '기계적 망각'의 중요성이 증가하고 있습니다.

- 2. 기존 방법들은 효율성과 공격적인 망각을 지나치게 중시하여 모델의 안정성을 해칠 수 있습니다.

- 3. CUFG는 망각 기울기를 활용한 새로운 기울기 교정기와 점진적 망각을 위한 커리큘럼 망각 패러다임을 통합하여 안정성을 향상시킵니다.

- 4. CUFG는 점진적이고 안정적인 망각을 통해 기존의 재훈련 방법과의 격차를 좁히며, 효과성과 신뢰성을 개선합니다.

- 5. 다양한 망각 시나리오에서의 실험을 통해 CUFG의 접근 방식의 타당성과 효과가 입증되었습니다.

---

*Generated on 2025-09-20 05:47:52*