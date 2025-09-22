
# How Bad Is Forming Your Own Multidimensional Opinion?

**Korean Title:** 자신만의 다차원적 의견을 형성하는 것은 얼마나 나쁜가?

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Price of Anarchy in Multidimensional Models

## 🔗 유사한 논문
- [[Emergent Alignment via Competition_20250919|Emergent Alignment via Competition]] (80.4% similar)
- [[Emergent Social Dynamics of LLM Agents in the El Farol Bar Problem_20250918|Emergent Social Dynamics of LLM Agents in the El Farol Bar Problem]] (79.0% similar)
- [[Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game_20250918|Distributionally Robust Equilibria over the Wasserstein Distance for Generalized Nash Game]] (78.2% similar)
- [[The Sum Leaks More Than Its Parts Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration]] (77.9% similar)
- [[Geometry-Aware Decentralized Sinkhorn for Wasserstein Barycenters_20250919|Geometry-Aware Decentralized Sinkhorn for Wasserstein Barycenters]] (77.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14411v1 Announce Type: new 
Abstract: Understanding the formation of opinions on interconnected topics within social networks is of significant importance. It offers insights into collective behavior and decision-making, with applications in Graph Neural Networks. Existing models propose that individuals form opinions based on a weighted average of their peers' opinions and their own beliefs. This averaging process, viewed as a best-response game, can be seen as an individual minimizing disagreements with peers, defined by a quadratic penalty, leading to an equilibrium. Bindel, Kleinberg, and Oren (FOCS 2011) provided tight bounds on the "price of anarchy" defined as the maximum overall disagreement at equilibrium relative to a social optimum. Bhawalkar, Gollapudi, and Munagala (STOC 2013) generalized the penalty function to non-quadratic penalties and provided tight bounds on the price of anarchy.
  When considering multiple topics, an individual's opinions can be represented as a vector. Parsegov, Proskurnikov, Tempo, and Friedkin (2016) proposed a multidimensional model using the weighted averaging process, but with constant interdependencies between topics. However, the question of the price of anarchy for this model remained open. We address this by providing tight bounds on the multidimensional model, while also generalizing it to more complex interdependencies. Following the work of Bhawalkar, Gollapudi, and Munagala, we provide tight bounds on the price of anarchy under non-quadratic penalties. Surprisingly, these bounds match the scalar model. We further demonstrate that the bounds remain unchanged even when adding another layer of complexity, involving groups of individuals minimizing their overall internal and external disagreement penalty, a common occurrence in real-life scenarios.

## 🔍 Abstract (한글 번역)

arXiv:2509.14411v1 발표 유형: 신규  
초록: 사회 네트워크 내에서 상호 연결된 주제에 대한 의견 형성을 이해하는 것은 매우 중요합니다. 이는 집단 행동과 의사 결정에 대한 통찰력을 제공하며, 그래프 신경망(Graph Neural Networks)에서 응용됩니다. 기존 모델들은 개인이 동료들의 의견과 자신의 신념을 가중 평균하여 의견을 형성한다고 제안합니다. 이러한 평균화 과정은 최적 반응 게임으로 간주될 수 있으며, 이는 개인이 동료들과의 불일치를 최소화하는 것으로, 이는 이차 페널티로 정의되어 균형에 도달합니다. Bindel, Kleinberg, Oren (FOCS 2011)은 사회적 최적에 비해 균형 상태에서의 최대 전체 불일치로 정의되는 "무질서의 대가(price of anarchy)"에 대한 엄밀한 경계를 제공했습니다. Bhawalkar, Gollapudi, Munagala (STOC 2013)는 페널티 함수를 비이차 페널티로 일반화하고 무질서의 대가에 대한 엄밀한 경계를 제공했습니다.  
여러 주제를 고려할 때, 개인의 의견은 벡터로 표현될 수 있습니다. Parsegov, Proskurnikov, Tempo, Friedkin (2016)은 주제 간의 상호 의존성이 일정한 상태에서 가중 평균 과정을 사용하는 다차원 모델을 제안했습니다. 그러나 이 모델에 대한 무질서의 대가에 대한 질문은 열려 있었습니다. 우리는 이 문제를 해결하기 위해 다차원 모델에 대한 엄밀한 경계를 제공하고, 더 복잡한 상호 의존성으로 일반화합니다. Bhawalkar, Gollapudi, Munagala의 연구를 따라, 비이차 페널티 하에서 무질서의 대가에 대한 엄밀한 경계를 제공합니다. 놀랍게도, 이러한 경계는 스칼라 모델과 일치합니다. 우리는 또한 개인 그룹이 내부 및 외부 불일치 페널티를 최소화하는 또 다른 복잡성 계층을 추가하더라도 경계가 변하지 않는다는 것을 보여줍니다. 이는 실제 시나리오에서 흔히 발생하는 일입니다.

## 📝 요약

이 논문은 사회 네트워크 내에서 상호 연결된 주제에 대한 의견 형성을 이해하는 데 중점을 둡니다. 기존 모델은 개인이 자신의 의견과 주변 사람들의 의견을 가중 평균하여 형성한다고 제안합니다. 이 과정은 최적 반응 게임으로 볼 수 있으며, 개인이 이견을 최소화하여 균형을 이루는 것으로 설명됩니다. 본 연구는 다차원 모델에서 주제 간 상호 의존성을 고려하여 의견 형성의 "혼란 비용"에 대한 명확한 경계를 제시합니다. 특히, 비이차적 패널티 하에서도 이러한 경계가 기존 스칼라 모델과 일치함을 발견했습니다. 또한, 그룹 내외부의 의견 불일치를 최소화하는 복잡한 상황에서도 이러한 경계가 변하지 않음을 보여줍니다.

## 🎯 주요 포인트

- 1. 사회 네트워크 내에서 상호 연결된 주제에 대한 의견 형성은 집단 행동과 의사결정에 대한 통찰을 제공하며, 그래프 신경망에 응용될 수 있다.

- 2. 기존 모델은 개인이 동료의 의견과 자신의 신념의 가중 평균을 통해 의견을 형성한다고 제안하며, 이는 최적 반응 게임으로 볼 수 있다.

- 3. Bindel, Kleinberg, Oren은 균형 상태에서의 최대 불일치와 사회 최적 상태의 비율인 '혼잡의 대가'에 대한 엄밀한 경계를 제시했다.

- 4. 다차원 모델에서 주제 간 상호 의존성을 고려한 '혼잡의 대가'에 대한 문제를 해결하고, 비이차적 패널티 하에서의 경계를 제시했다.

- 5. 복잡성을 더해도 '혼잡의 대가' 경계는 변하지 않으며, 이는 현실에서 그룹의 내부 및 외부 불일치 최소화와 관련이 있다.

---

*Generated on 2025-09-19 16:49:40*