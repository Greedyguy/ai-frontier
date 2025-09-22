# Latent learning: episodic memory complements parametric learning by enabling flexible reuse of experiences

**Korean Title:** 잠재 학습: 일화 기억은 경험의 유연한 재사용을 가능하게 함으로써 매개변수 학습을 보완합니다.

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Latent Learning

## 🔗 유사한 논문
- [[2025-09-22/Search and Refine During Think_ Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning_20250922|Search and Refine During Think Facilitating Knowledge Refinement for Improved Retrieval-Augmented Reasoning]] (81.0% similar)
- [[2025-09-22/Dynamic Neural Curiosity Enhances Learning Flexibility for Autonomous Goal Discovery_20250922|Dynamic Neural Curiosity Enhances Learning Flexibility for Autonomous Goal Discovery]] (80.3% similar)
- [[2025-09-19/Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring_20250919|Learning Discrete Abstractions for Visual Rearrangement Tasks Using Vision-Guided Graph Coloring]] (80.1% similar)
- [[2025-09-18/Data coarse graining can improve model performance_20250918|Data coarse graining can improve model performance]] (79.9% similar)
- [[2025-09-18/CUFG_ Curriculum Unlearning Guided by the Forgetting Gradient_20250918|CUFG Curriculum Unlearning Guided by the Forgetting Gradient]] (79.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16189v1 Announce Type: new 
Abstract: When do machine learning systems fail to generalize, and what mechanisms could improve their generalization? Here, we draw inspiration from cognitive science to argue that one weakness of machine learning systems is their failure to exhibit latent learning -- learning information that is not relevant to the task at hand, but that might be useful in a future task. We show how this perspective links failures ranging from the reversal curse in language modeling to new findings on agent-based navigation. We then highlight how cognitive science points to episodic memory as a potential part of the solution to these issues. Correspondingly, we show that a system with an oracle retrieval mechanism can use learning experiences more flexibly to generalize better across many of these challenges. We also identify some of the essential components for effectively using retrieval, including the importance of within-example in-context learning for acquiring the ability to use information across retrieved examples. In summary, our results illustrate one possible contributor to the relative data inefficiency of current machine learning systems compared to natural intelligence, and help to understand how retrieval methods can complement parametric learning to improve generalization.

## 🔍 Abstract (한글 번역)

arXiv:2509.16189v1 발표 유형: 신규  
초록: 기계 학습 시스템이 일반화에 실패하는 경우는 언제이며, 어떤 메커니즘이 그들의 일반화를 향상시킬 수 있을까요? 여기에서 우리는 인지 과학에서 영감을 받아 기계 학습 시스템의 한 가지 약점이 잠재 학습을 보여주지 못하는 것이라고 주장합니다. 잠재 학습이란 현재의 과제와는 관련이 없지만 미래의 과제에서 유용할 수 있는 정보를 학습하는 것입니다. 우리는 이러한 관점이 언어 모델링에서의 역전 저주부터 에이전트 기반 내비게이션에 대한 새로운 발견에 이르기까지의 실패를 어떻게 연결하는지를 보여줍니다. 그런 다음 인지 과학이 이러한 문제에 대한 해결책의 일부로서 일화 기억을 지적하는 방법을 강조합니다. 이에 따라 우리는 오라클 검색 메커니즘을 갖춘 시스템이 학습 경험을 보다 유연하게 사용하여 이러한 많은 도전 과제에서 더 나은 일반화를 달성할 수 있음을 보여줍니다. 또한 검색을 효과적으로 사용하기 위한 필수 구성 요소 중 일부를 식별하며, 검색된 예제 전반에 걸쳐 정보를 사용할 수 있는 능력을 습득하기 위해 예제 내 맥락 학습의 중요성을 포함합니다. 요약하자면, 우리의 결과는 자연 지능에 비해 현재 기계 학습 시스템의 상대적 데이터 비효율성에 기여할 수 있는 한 가지 요소를 설명하고, 검색 방법이 매개변수 학습을 보완하여 일반화를 향상시키는 방법을 이해하는 데 도움을 줍니다.

## 📝 요약

이 논문은 기계 학습 시스템의 일반화 실패 원인과 이를 개선할 수 있는 메커니즘을 탐구합니다. 인지과학에서 영감을 받아, 기계 학습 시스템이 잠재 학습을 잘 수행하지 못하는 것이 약점임을 지적합니다. 잠재 학습은 현재 과제와 직접 관련이 없지만 미래에 유용할 수 있는 정보를 학습하는 것을 의미합니다. 논문은 언어 모델링의 역전 저주부터 에이전트 기반 탐색까지 다양한 실패 사례를 이 관점에서 설명합니다. 또한, 인지과학이 제시하는 해결책으로서 에피소드 기억의 중요성을 강조하며, 오라클 검색 메커니즘을 가진 시스템이 학습 경험을 더 유연하게 활용하여 일반화를 개선할 수 있음을 보여줍니다. 효과적인 검색 활용을 위해서는 예제 내 맥락 학습의 중요성을 강조합니다. 이러한 연구는 현재 기계 학습 시스템이 자연 지능에 비해 데이터 효율성이 낮은 이유를 설명하고, 검색 방법이 매개변수 학습을 보완하여 일반화를 향상시킬 수 있음을 이해하는 데 기여합니다.

## 🎯 주요 포인트

- 1. 기계 학습 시스템은 잠재 학습을 제대로 수행하지 못해 일반화에 실패할 수 있다.

- 2. 인지 과학의 관점에서 에피소드 기억이 일반화 문제 해결의 잠재적 해결책이 될 수 있다.

- 3. 오라클 검색 메커니즘을 갖춘 시스템은 학습 경험을 더 유연하게 활용하여 일반화를 개선할 수 있다.

- 4. 검색을 효과적으로 사용하기 위해서는 예제 내 맥락 학습이 중요하다.

- 5. 검색 방법이 매개변수 학습을 보완하여 일반화를 개선할 수 있는 방법을 이해하는 데 도움이 된다.

---

*Generated on 2025-09-22 15:34:39*