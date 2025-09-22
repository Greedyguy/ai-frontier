# Concept Unlearning in Large Language Models via Self-Constructed Knowledge Triplets

**Korean Title:** 대형 언어 모델에서 자기 구성 지식 삼중항을 통한 개념 학습 제거

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Machine Unlearning

## 🔗 유사한 논문
- [[2025-09-18/Reveal and Release_ Iterative LLM Unlearning with Self-generated Data_20250918|Reveal and Release Iterative LLM Unlearning with Self-generated Data]] (86.5% similar)
- [[2025-09-18/CUFG_ Curriculum Unlearning Guided by the Forgetting Gradient_20250918|CUFG Curriculum Unlearning Guided by the Forgetting Gradient]] (85.1% similar)
- [[2025-09-17/Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning_20250917|Scrub It Out! Erasing Sensitive Memorization in Code Language Models via Machine Unlearning]] (82.8% similar)
- [[2025-09-22/Pre-Forgettable Models_ Prompt Learning as a Native Mechanism for Unlearning_20250922|Pre-Forgettable Models Prompt Learning as a Native Mechanism for Unlearning]] (82.0% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning An Indispensable Path towards New-Generation Large Language Models]] (81.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15621v1 Announce Type: cross 
Abstract: Machine Unlearning (MU) has recently attracted considerable attention as a solution to privacy and copyright issues in large language models (LLMs). Existing MU methods aim to remove specific target sentences from an LLM while minimizing damage to unrelated knowledge. However, these approaches require explicit target sentences and do not support removing broader concepts, such as persons or events. To address this limitation, we introduce Concept Unlearning (CU) as a new requirement for LLM unlearning. We leverage knowledge graphs to represent the LLM's internal knowledge and define CU as removing the forgetting target nodes and associated edges. This graph-based formulation enables a more intuitive unlearning and facilitates the design of more effective methods. We propose a novel method that prompts the LLM to generate knowledge triplets and explanatory sentences about the forgetting target and applies the unlearning process to these representations. Our approach enables more precise and comprehensive concept removal by aligning the unlearning process with the LLM's internal knowledge representations. Experiments on real-world and synthetic datasets demonstrate that our method effectively achieves concept-level unlearning while preserving unrelated knowledge.

## 🔍 Abstract (한글 번역)

arXiv:2509.15621v1 발표 유형: 교차  
초록: 기계 학습 제거(Machine Unlearning, MU)는 최근 대형 언어 모델(LLM)에서의 프라이버시 및 저작권 문제에 대한 해결책으로 상당한 주목을 받고 있습니다. 기존의 MU 방법은 특정 대상 문장을 LLM에서 제거하면서 관련 없는 지식에 대한 손상을 최소화하는 것을 목표로 합니다. 그러나 이러한 접근법은 명시적인 대상 문장을 필요로 하며, 사람이나 사건과 같은 더 넓은 개념을 제거하는 것을 지원하지 않습니다. 이러한 한계를 해결하기 위해, 우리는 LLM 제거에 대한 새로운 요구사항으로 개념 제거(Concept Unlearning, CU)를 소개합니다. 우리는 지식 그래프를 활용하여 LLM의 내부 지식을 표현하고, CU를 망각 대상 노드와 관련된 엣지를 제거하는 것으로 정의합니다. 이 그래프 기반의 공식화는 보다 직관적인 제거를 가능하게 하고, 더 효과적인 방법의 설계를 촉진합니다. 우리는 LLM이 망각 대상에 대한 지식 삼중항과 설명 문장을 생성하도록 유도하고, 이러한 표현에 제거 과정을 적용하는 새로운 방법을 제안합니다. 우리의 접근법은 제거 과정을 LLM의 내부 지식 표현과 일치시킴으로써 보다 정밀하고 포괄적인 개념 제거를 가능하게 합니다. 실제 및 합성 데이터셋에 대한 실험은 우리의 방법이 관련 없는 지식을 보존하면서 개념 수준의 제거를 효과적으로 달성함을 보여줍니다.

## 📝 요약

이 논문은 대형 언어 모델(LLM)에서 개인정보 및 저작권 문제를 해결하기 위한 기계 학습 제거(MU)의 한계를 극복하고자 새로운 개념 제거(CU) 방법론을 제안합니다. 기존 MU 방법은 특정 문장을 제거하는 데 중점을 두지만, CU는 사람이나 사건과 같은 더 넓은 개념을 제거할 수 있도록 설계되었습니다. 이를 위해 지식 그래프를 활용하여 LLM의 내부 지식을 표현하고, 제거할 개념을 그래프의 노드와 간선으로 정의합니다. 제안된 방법은 LLM이 생성한 지식 삼중항과 설명 문장을 기반으로 제거 과정을 수행하여, 보다 정밀하고 포괄적인 개념 제거를 가능하게 합니다. 실험 결과, 제안된 방법은 관련 없는 지식을 보존하면서도 효과적으로 개념 수준의 제거를 달성함을 보여줍니다.

## 🎯 주요 포인트

- 1. 기계 학습 모델에서 특정 문장을 제거하는 기존 방법의 한계를 극복하기 위해 개념 학습 제거(CU)를 도입했습니다.

- 2. CU는 지식 그래프를 활용하여 모델의 내부 지식을 표현하고, 제거 대상 노드와 관련된 엣지를 삭제하는 방식으로 정의됩니다.

- 3. 제안된 방법은 모델이 잊어야 할 대상을 설명하는 지식 삼중항과 문장을 생성하게 하여, 이를 기반으로 학습 제거를 수행합니다.

- 4. 실험 결과, 제안된 방법은 개념 수준에서의 학습 제거를 효과적으로 수행하면서도 관련 없는 지식은 보존하는 데 성공했습니다.

---

*Generated on 2025-09-22 15:40:37*