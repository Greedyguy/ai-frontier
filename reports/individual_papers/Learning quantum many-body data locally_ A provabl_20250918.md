
# Learning quantum many-body data locally: A provably scalable framework

**Korean Title:** 지역적으로 양자 다체 데이터 학습: 증명 가능한 확장 가능한 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Translationally Symmetric Data|Translationally Symmetric Data]] [[keywords/broad/Machine Learning|Machine Learning]] [[keywords/broad/Quantum Computing|Quantum Computing]] [[keywords/specific/Quantum Expectation Values|Quantum Expectation Values]] [[keywords/unique/Geometrically Local Quantum Kernel (GLQK|Geometrically Local Quantum Kernel (GLQK]] [[categories/cs.LG|cs.LG]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Translationally Symmetric Data
**🔬 Broad Technical**: Machine Learning, Quantum Computing
**🔗 Specific Connectable**: Quantum Expectation Values
**⭐ Unique Technical**: Geometrically Local Quantum Kernel (GLQK

**ArXiv ID**: [2509.13705](https://arxiv.org/abs/2509.13705)
**Published**: 2025-09-18
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2509.13705.pdf)


## 🏷️ 추출된 키워드



`Machine Learning` • 

`Quantum Computing` • 

`Quantum Kernel` • 

`GLQK` • 

`Quantum Many-Body Data`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13705v1 Announce Type: cross 
Abstract: Machine learning (ML) holds great promise for extracting insights from complex quantum many-body data obtained in quantum experiments. This approach can efficiently solve certain quantum problems that are classically intractable, suggesting potential advantages of harnessing quantum data. However, addressing large-scale problems still requires significant amounts of data beyond the limited computational resources of near-term quantum devices. We propose a scalable ML framework called Geometrically Local Quantum Kernel (GLQK), designed to efficiently learn quantum many-body experimental data by leveraging the exponential decay of correlations, a phenomenon prevalent in noncritical systems. In the task of learning an unknown polynomial of quantum expectation values, we rigorously prove that GLQK substantially improves polynomial sample complexity in the number of qubits $n$, compared to the existing shadow kernel, by constructing a feature space from local quantum information at the correlation length scale. This improvement is particularly notable when each term of the target polynomial involves few local subsystems. Remarkably, for translationally symmetric data, GLQK achieves constant sample complexity, independent of $n$. We numerically demonstrate its high scalability in two learning tasks on quantum many-body phenomena. These results establish new avenues for utilizing experimental data to advance the understanding of quantum many-body physics.

## 🔍 Abstract (한글 번역)

arXiv:2509.13705v1 발표 유형: 교차
요약: 기계 학습(ML)은 양자 실험에서 얻은 복잡한 양자 다체 데이터로부터 통찰을 추출하는 데 큰 잠재력을 가지고 있습니다. 이 접근 방식은 고전적으로 해결하기 어려운 특정 양자 문제를 효율적으로 해결할 수 있으며, 양자 데이터를 활용하는 잠재적 이점을 제안합니다. 그러나 대규모 문제를 다루기 위해서는 여전히 근시일 양자 장치의 제한된 계산 자원을 넘어서는 상당한 양의 데이터가 필요합니다. 우리는 상관의 지수적 감소를 활용하여 양자 다체 실험 데이터를 효율적으로 학습하기 위해 설계된 확장 가능한 ML 프레임워크인 기하적으로 지역적 양자 커널(GLQK)을 제안합니다. 비비극적 시스템에서 흔히 나타나는 현상입니다. 양자 기대값의 알려지지 않은 다항식을 학습하는 작업에서, 우리는 GLQK가 기존의 그림자 커널과 비교하여 큐비트 수 $n$에 대한 다항식 샘플 복잡성을 상당히 개선한다는 것을 엄밀히 증명합니다. 상관 길이 스케일에서 지역 양자 정보로부터 특징 공간을 구성함으로써. 이 개선은 특히 대상 다항식의 각 항이 몇 개의 지역 하부 시스템을 포함할 때 주목할 만합니다. 놀랍게도, 변환 대칭 데이터의 경우 GLQK는 $n$에 독립적인 상수 샘플 복잡성을 달성합니다. 우리는 양자 다체 현상에 대한 두 가지 학습 작업에서 그의 높은 확장성을 수치적으로 증명합니다. 이러한 결과는 실험 데이터를 활용하여 양자 다체 물리학의 이해를 발전시키는 새로운 길을 열어줍니다.

## 📝 요약

본 연구는 양자 실험에서 얻은 복잡한 양자 다체 데이터로부터 통찰을 추출하는 데 머신 러닝(ML)이 큰 잠재력을 가지고 있다는 것을 보여줍니다. GLQK는 양자 다체 실험 데이터를 효율적으로 학습하기 위해 설계된 확장 가능한 ML 프레임워크로, 상관 관계의 지수적 감소를 활용합니다. GLQK는 기존의 그림자 커널과 비교하여 다항식 샘플 복잡성을 크게 개선하며, 특히 대칭 데이터의 경우 n과 독립적인 상수 샘플 복잡성을 달성합니다. 이러한 결과는 실험 데이터를 활용하여 양자 다체 물리학의 이해를 발전시키는 새로운 길을 열어줍니다.

## 🎯 주요 포인트


- 1. 기하학적으로 지역화된 양자 커널(GLQK)은 양자 많체 실험 데이터를 효율적으로 학습하는 확장 가능한 기계 학습 프레임워크이다.

- 2. GLQK는 상관 관계의 지수적 감소를 활용하여 양자 기대값의 알려지지 않은 다항식을 효율적으로 학습함으로써 다항식 샘플 복잡성을 크게 개선한다.

- 3. GLQK는 특히 각 항이 몇 개의 지역 하위 시스템을 포함하는 경우에 더욱 높은 확장성을 보여준다.


---

*Generated on 2025-09-18 16:43:33*