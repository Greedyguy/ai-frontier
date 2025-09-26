---
keywords:
  - Quantum Many-Body Data
  - Machine Learning
  - Geometrically Local Quantum Kernel
category: cs.AI
publish_date: 2025-09-17
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:52:12.185229",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Quantum Many-Body Data",
    "Machine Learning",
    "Geometrically Local Quantum Kernel"
  ],
  "rejected_keywords": [
    "Exponential Decay of Correlations"
  ],
  "similarity_scores": {
    "Quantum Many-Body Data": 0.8,
    "Machine Learning": 0.85,
    "Geometrically Local Quantum Kernel": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Learning quantum many-body data locally: A provably scalable framework

**Korean Title:** 양자 다체 데이터를 지역적으로 학습하기: 입증 가능한 확장 가능한 프레임워크

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250917|2025-09-17]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Machine Learning|Machine learning]]
**⚡ Unique Technical**: [[keywords/Quantum Many-Body Data|quantum many-body data]], [[keywords/Geometrically Local Quantum Kernel|Geometrically Local Quantum Kernel]]

## 🔗 유사한 논문
- [[Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment_20250917|Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (83.7% similar)
- [[Trainability of Quantum Models Beyond Known Classical Simulability_20250919|Trainability of Quantum Models Beyond Known Classical Simulability]] (82.4% similar)
- [[Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks_20250917|Quantum Variational Activation Functions Empower Kolmogorov-Arnold Networks]] (82.0% similar)
- [[Efficiently learning depth-3 circuits via quantum agnostic boosting_20250917|Efficiently learning depth-3 circuits via quantum agnostic boosting]] (81.4% similar)
- [[Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit_20250918|Learning AC Power Flow Solutions using a Data-Dependent Variational Quantum Circuit]] (81.0% similar)

## 📋 저자 정보

**Authors:** Koki Chinzei, Quoc Hoan Tran, Norifumi Matsumoto, Yasuhiro Endo, Hirotaka Oshima

## 📄 Abstract (원문)

Machine learning (ML) holds great promise for extracting insights from
complex quantum many-body data obtained in quantum experiments. This approach
can efficiently solve certain quantum problems that are classically
intractable, suggesting potential advantages of harnessing quantum data.
However, addressing large-scale problems still requires significant amounts of
data beyond the limited computational resources of near-term quantum devices.
We propose a scalable ML framework called Geometrically Local Quantum Kernel
(GLQK), designed to efficiently learn quantum many-body experimental data by
leveraging the exponential decay of correlations, a phenomenon prevalent in
noncritical systems. In the task of learning an unknown polynomial of quantum
expectation values, we rigorously prove that GLQK substantially improves
polynomial sample complexity in the number of qubits $n$, compared to the
existing shadow kernel, by constructing a feature space from local quantum
information at the correlation length scale. This improvement is particularly
notable when each term of the target polynomial involves few local subsystems.
Remarkably, for translationally symmetric data, GLQK achieves constant sample
complexity, independent of $n$. We numerically demonstrate its high scalability
in two learning tasks on quantum many-body phenomena. These results establish
new avenues for utilizing experimental data to advance the understanding of
quantum many-body physics.

## 🔍 Abstract (한글 번역)

기계 학습(ML)은 양자 실험에서 얻은 복잡한 양자 다체 데이터로부터 통찰을 추출하는 데 큰 가능성을 가지고 있습니다. 이 접근 방식은 고전적으로 다루기 어려운 특정 양자 문제를 효율적으로 해결할 수 있으며, 이는 양자 데이터를 활용하는 잠재적 이점을 시사합니다. 그러나 대규모 문제를 해결하기 위해서는 여전히 근시일 내의 양자 장치의 제한된 계산 자원을 넘어서는 상당한 양의 데이터가 필요합니다. 우리는 비임계 시스템에서 흔히 볼 수 있는 상관관계의 지수적 감소를 활용하여 양자 다체 실험 데이터를 효율적으로 학습하도록 설계된 확장 가능한 ML 프레임워크인 Geometrically Local Quantum Kernel(GLQK)을 제안합니다. 양자 기대값의 미지의 다항식을 학습하는 과제에서, 우리는 GLQK가 기존의 섀도우 커널과 비교하여 상관 길이 스케일에서 지역 양자 정보를 통해 특징 공간을 구성함으로써 큐비트 수 $n$에 대한 다항식 샘플 복잡성을 상당히 개선한다는 것을 엄밀히 증명합니다. 이러한 개선은 목표 다항식의 각 항이 몇 개의 지역 하위 시스템을 포함할 때 특히 두드러집니다. 놀랍게도, 변환 대칭 데이터를 위해 GLQK는 $n$과 독립적인 상수 샘플 복잡성을 달성합니다. 우리는 양자 다체 현상에 대한 두 가지 학습 과제에서 그 높은 확장성을 수치적으로 입증합니다. 이러한 결과는 양자 다체 물리학의 이해를 발전시키기 위해 실험 데이터를 활용하는 새로운 길을 열어줍니다.

## 📝 요약

이 논문은 양자 실험에서 얻은 복잡한 양자 다체 데이터를 효율적으로 학습하기 위한 기하학적으로 지역적인 양자 커널(GLQK)이라는 확장 가능한 기계 학습 프레임워크를 제안합니다. GLQK는 비임계 시스템에서 흔히 나타나는 상관관계의 지수적 감소를 활용하여, 기존의 섀도우 커널보다 큐비트 수 $n$에 대한 다항식 샘플 복잡성을 크게 개선합니다. 특히, 목표 다항식의 각 항이 적은 지역적 하위 시스템을 포함할 때 이점이 두드러지며, 변환 대칭 데이터를 다룰 때는 샘플 복잡성이 $n$과 무관하게 일정합니다. 두 가지 양자 다체 현상 학습 과제에서 GLQK의 높은 확장성을 수치적으로 입증하였으며, 이는 양자 다체 물리학 이해를 발전시키기 위한 실험 데이터 활용의 새로운 가능성을 제시합니다.

## 🎯 주요 포인트

- 1. 기하학적으로 지역적인 양자 커널(GLQK)은 상관관계의 지수적 감소를 활용하여 양자 다체 실험 데이터를 효율적으로 학습하도록 설계된 확장 가능한 머신러닝 프레임워크입니다.

- 2. GLQK는 기존의 섀도우 커널과 비교하여 양자 기대값의 다항식을 학습할 때 큐비트 수 $n$에 대한 다항 샘플 복잡성을 상당히 개선합니다.

- 3. 변환 대칭 데이터를 다룰 때, GLQK는 $n$에 독립적인 상수 샘플 복잡성을 달성합니다.

- 4. 두 가지 양자 다체 현상 학습 과제에서 GLQK의 높은 확장성을 수치적으로 입증하였습니다.

- 5. 이 연구 결과는 양자 다체 물리학 이해를 발전시키기 위해 실험 데이터를 활용하는 새로운 길을 열었습니다.

---

*Generated on 2025-09-20 09:39:12*