---
keywords:
  - Graph Neural Networks
  - Precision Neural Networks
  - Covariance Matrix
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:15:16.189162",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Networks",
    "Precision Neural Networks",
    "Covariance Matrix"
  ],
  "rejected_keywords": [
    "Optimization"
  ],
  "similarity_scores": {
    "Graph Neural Networks": 0.82,
    "Precision Neural Networks": 0.78,
    "Covariance Matrix": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Precision Neural Networks: Joint Graph And Relational Learning

**Korean Title:** 정밀 신경망: 그래프 및 관계 학습의 결합

## 📋 메타데이터

**Links**:      [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Covariance Matrix|Covariance Matrix]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Networks|Graph Neural Networks]]
**⚡ Unique Technical**: [[keywords/Precision Neural Networks|Precision Neural Networks]]

## 🔗 유사한 논문
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (76.8% similar)
- [[GraphTorque_ Torque-Driven Rewiring Graph Neural Network_20250918|GraphTorque Torque-Driven Rewiring Graph Neural Network]] (76.6% similar)
- [[Balancing Sparse RNNs with Hyperparameterization Benefiting Meta-Learning_20250918|Balancing Sparse RNNs with Hyperparameterization Benefiting Meta-Learning]] (76.4% similar)
- [[MaRVIn_ A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration_20250919|MaRVIn A Cross-Layer Mixed-Precision RISC-V Framework for DNN Inference, from ISA Extension to Hardware Acceleration]] (76.2% similar)
- [[Probabilistic and nonlinear compressive sensing_20250918|Probabilistic and nonlinear compressive sensing]] (75.9% similar)

## 📋 저자 정보

**Authors:** Andrea Cavallo, Samuel Rey, Antonio G. Marques, Elvin Isufi

## 📄 Abstract (원문)

CoVariance Neural Networks (VNNs) perform convolutions on the graph
determined by the covariance matrix of the data, which enables expressive and
stable covariance-based learning. However, covariance matrices are typically
dense, fail to encode conditional independence, and are often precomputed in a
task-agnostic way, which may hinder performance. To overcome these limitations,
we study Precision Neural Networks (PNNs), i.e., VNNs on the precision matrix
-- the inverse covariance. The precision matrix naturally encodes statistical
independence, often exhibits sparsity, and preserves the covariance spectral
structure. To make precision estimation task-aware, we formulate an
optimization problem that jointly learns the network parameters and the
precision matrix, and solve it via alternating optimization, by sequentially
updating the network weights and the precision estimate. We theoretically bound
the distance between the estimated and true precision matrices at each
iteration, and demonstrate the effectiveness of joint estimation compared to
two-step approaches on synthetic and real-world data.

## 🔍 Abstract (한글 번역)

공분산 신경망(VNNs)은 데이터의 공분산 행렬에 의해 결정된 그래프에서 컨볼루션을 수행하여 표현력 있고 안정적인 공분산 기반 학습을 가능하게 합니다. 그러나 공분산 행렬은 일반적으로 밀집되어 있으며 조건부 독립성을 인코딩하지 못하고, 종종 과제와 무관하게 사전 계산되기 때문에 성능을 저해할 수 있습니다. 이러한 제한을 극복하기 위해, 우리는 정밀 신경망(PNNs), 즉 정밀 행렬(공분산의 역행렬)에서의 VNNs를 연구합니다. 정밀 행렬은 자연스럽게 통계적 독립성을 인코딩하며, 종종 희소성을 나타내고 공분산의 스펙트럼 구조를 보존합니다. 정밀 추정을 과제에 맞게 만들기 위해, 우리는 네트워크 매개변수와 정밀 행렬을 공동으로 학습하는 최적화 문제를 수립하고, 네트워크 가중치와 정밀 추정을 순차적으로 업데이트하여 교대 최적화를 통해 이를 해결합니다. 우리는 각 반복에서 추정된 정밀 행렬과 실제 정밀 행렬 간의 거리를 이론적으로 제한하고, 합성 및 실제 데이터에서의 두 단계 접근법과 비교하여 공동 추정의 효과를 입증합니다.

## 📝 요약

이 논문에서는 데이터의 공분산 행렬을 기반으로 하는 CoVariance Neural Networks(VNNs)의 한계를 극복하기 위해 Precision Neural Networks(PNNs)를 제안합니다. PNNs는 공분산의 역행렬인 정밀도 행렬을 사용하여 통계적 독립성을 자연스럽게 인코딩하고 희소성을 보입니다. 저자들은 네트워크 파라미터와 정밀도 행렬을 공동으로 학습하는 최적화 문제를 설정하고, 교대 최적화를 통해 이를 해결합니다. 이 방법은 추정된 정밀도 행렬과 실제 행렬 간의 거리를 이론적으로 제한하며, 합성 및 실제 데이터에서 기존의 2단계 접근법보다 효과적임을 입증합니다.

## 🎯 주요 포인트

- 1. CoVariance Neural Networks (VNNs)는 데이터의 공분산 행렬에 의해 결정된 그래프에서 컨볼루션을 수행하여 표현력 있고 안정적인 학습을 가능하게 합니다.

- 2. 공분산 행렬은 일반적으로 밀집되어 있으며 조건부 독립성을 인코딩하지 못하고, 작업과 무관하게 사전 계산되어 성능을 저해할 수 있습니다.

- 3. Precision Neural Networks (PNNs)는 공분산의 역행렬인 정밀도 행렬을 사용하여 이러한 한계를 극복하고자 합니다.

- 4. 정밀도 행렬은 통계적 독립성을 자연스럽게 인코딩하며, 희소성을 나타내고 공분산의 스펙트럼 구조를 보존합니다.

- 5. 네트워크 매개변수와 정밀도 행렬을 공동으로 학습하는 최적화 문제를 제시하고, 이론적으로 각 반복에서 추정된 정밀도 행렬과 실제 정밀도 행렬 간의 거리를 제한합니다.

---

*Generated on 2025-09-20 02:49:58*