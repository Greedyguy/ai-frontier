---
keywords:
  - Graph Neural Networks
  - Functional Magnetic Resonance Imaging
  - Hyperbolic Graph Neural Networks
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14965
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:54:27.427182",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Networks",
    "Functional Magnetic Resonance Imaging",
    "Hyperbolic Graph Neural Networks"
  ],
  "rejected_keywords": [
    "Geometric Deep Learning"
  ],
  "similarity_scores": {
    "Graph Neural Networks": 0.88,
    "Functional Magnetic Resonance Imaging": 0.85,
    "Hyperbolic Graph Neural Networks": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Brain-HGCN: A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis

**Korean Title:** 브레인-HGCN: 뇌 기능 네트워크 분석을 위한 쌍곡 그래프 합성곱 신경망

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Networks|Graph Neural Networks]], [[keywords/Functional Magnetic Resonance Imaging|Functional Magnetic Resonance Imaging]]
**⚡ Unique Technical**: [[keywords/Hyperbolic Graph Neural Networks|Hyperbolic Graph Convolutional Network]]

## 🔗 유사한 논문
- [[GraphTorque Torque-Driven Rewiring Graph Neural Network]] (81.3% similar)
- [[Federated Hypergraph Learning with Local Differential Privacy Toward Privacy-Aware Hypergraph Structure Completion]] (80.6% similar)
- [[Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (79.3% similar)
- [[Multimodal Hate Detection Using Dual-Stream Graph Neural Networks]] (79.2% similar)
- [[A Geometric Graph-Based Deep Learning Model for Drug-Target Affinity Prediction]] (79.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14965v1 Announce Type: new 
Abstract: Functional magnetic resonance imaging (fMRI) provides a powerful non-invasive window into the brain's functional organization by generating complex functional networks, typically modeled as graphs. These brain networks exhibit a hierarchical topology that is crucial for cognitive processing. However, due to inherent spatial constraints, standard Euclidean GNNs struggle to represent these hierarchical structures without high distortion, limiting their clinical performance. To address this limitation, we propose Brain-HGCN, a geometric deep learning framework based on hyperbolic geometry, which leverages the intrinsic property of negatively curved space to model the brain's network hierarchy with high fidelity. Grounded in the Lorentz model, our model employs a novel hyperbolic graph attention layer with a signed aggregation mechanism to distinctly process excitatory and inhibitory connections, ultimately learning robust graph-level representations via a geometrically sound Fr\'echet mean for graph readout. Experiments on two large-scale fMRI datasets for psychiatric disorder classification demonstrate that our approach significantly outperforms a wide range of state-of-the-art Euclidean baselines. This work pioneers a new geometric deep learning paradigm for fMRI analysis, highlighting the immense potential of hyperbolic GNNs in the field of computational psychiatry.

## 🔍 Abstract (한글 번역)

arXiv:2509.14965v1 발표 유형: 신규  
초록: 기능적 자기공명영상(fMRI)은 복잡한 기능적 네트워크를 생성하여 뇌의 기능적 조직을 비침습적으로 관찰할 수 있는 강력한 도구로, 일반적으로 그래프로 모델링됩니다. 이러한 뇌 네트워크는 인지 처리에 중요한 계층적 토폴로지를 나타냅니다. 그러나 고유한 공간적 제약으로 인해 표준 유클리드 GNN은 높은 왜곡 없이 이러한 계층 구조를 표현하는 데 어려움을 겪어 임상적 성능이 제한됩니다. 이러한 한계를 극복하기 위해 우리는 뇌의 네트워크 계층 구조를 높은 충실도로 모델링하기 위해 음의 곡률 공간의 고유한 특성을 활용하는 쌍곡 기하학에 기반한 기하학적 딥러닝 프레임워크인 Brain-HGCN을 제안합니다. 로렌츠 모델에 기반한 우리의 모델은 흥분성 및 억제성 연결을 명확하게 처리하기 위해 서명된 집계 메커니즘을 갖춘 새로운 쌍곡 그래프 주의 레이어를 사용하여, 그래프 읽기를 위한 기하학적으로 타당한 프레셰 평균을 통해 견고한 그래프 수준 표현을 학습합니다. 정신 질환 분류를 위한 두 개의 대규모 fMRI 데이터셋에 대한 실험은 우리의 접근 방식이 다양한 최신 유클리드 기준선을 크게 능가한다는 것을 보여줍니다. 이 연구는 fMRI 분석을 위한 새로운 기하학적 딥러닝 패러다임을 개척하며, 계산 정신의학 분야에서 쌍곡 GNN의 엄청난 잠재력을 강조합니다.

## 📝 요약

이 논문은 fMRI를 활용한 뇌 기능 네트워크 분석에서 기존 유클리드 GNN의 한계를 극복하기 위해 Brain-HGCN이라는 새로운 기하학적 딥러닝 프레임워크를 제안합니다. 이 프레임워크는 음의 곡률을 가진 쌍곡 기하학을 활용하여 뇌의 계층적 구조를 정확히 모델링합니다. Lorentz 모델을 기반으로 한 새로운 쌍곡 그래프 주의 메커니즘을 통해 흥분성 및 억제성 연결을 구분 처리하며, 프레셰 평균을 사용한 그래프 수준 표현 학습을 수행합니다. 두 개의 대규모 fMRI 데이터셋에서의 실험 결과, 이 접근법은 기존 유클리드 기반 모델들을 능가하는 성능을 보였습니다. 이는 계산 정신의학 분야에서 쌍곡 GNN의 잠재력을 강조합니다.

## 🎯 주요 포인트

- 1. fMRI는 복잡한 기능적 네트워크를 생성하여 뇌의 기능적 조직을 비침습적으로 관찰할 수 있는 강력한 도구이다.

- 2. 표준 유클리드 GNN은 뇌 네트워크의 계층적 구조를 왜곡 없이 표현하는 데 한계가 있다.

- 3. Brain-HGCN은 음의 곡률 공간을 활용하여 뇌 네트워크의 계층 구조를 고충실도로 모델링하는 기하학적 딥러닝 프레임워크이다.

- 4. 새로운 쌍곡 그래프 주의 레이어와 서명 집계 메커니즘을 통해 흥분성 및 억제성 연결을 명확히 처리한다.

- 5. 두 개의 대규모 fMRI 데이터셋 실험에서 Brain-HGCN은 최신 유클리드 기반 모델들을 능가하는 성능을 보였다.

---

*Generated on 2025-09-19 16:08:00*