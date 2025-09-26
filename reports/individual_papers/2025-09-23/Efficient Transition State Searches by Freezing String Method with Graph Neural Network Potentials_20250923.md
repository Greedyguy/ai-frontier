---
keywords:
  - Graph Neural Network
  - Freezing String Method
  - Transition State Search
  - Potential Energy Surface
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2501.06159
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:59:57.464999",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Freezing String Method",
    "Transition State Search",
    "Potential Energy Surface"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.85,
    "Freezing String Method": 0.72,
    "Transition State Search": 0.78,
    "Potential Energy Surface": 0.68
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Graph Neural Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are central to the paper's methodology and connect well with existing research in neural network applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "Freezing String Method",
        "canonical": "Freezing String Method",
        "aliases": [
          "FSM"
        ],
        "category": "unique_technical",
        "rationale": "The Freezing String Method is a unique approach used in the paper, providing a specific technique for linking to transition state search methods.",
        "novelty_score": 0.67,
        "connectivity_score": 0.65,
        "specificity_score": 0.79,
        "link_intent_score": 0.72
      },
      {
        "surface": "Transition State Search",
        "canonical": "Transition State Search",
        "aliases": [
          "TS Search"
        ],
        "category": "unique_technical",
        "rationale": "Transition State Search is a key focus of the paper, essential for linking to studies on chemical reactivity and computational chemistry.",
        "novelty_score": 0.61,
        "connectivity_score": 0.77,
        "specificity_score": 0.81,
        "link_intent_score": 0.78
      },
      {
        "surface": "Potential Energy Surface",
        "canonical": "Potential Energy Surface",
        "aliases": [
          "PES"
        ],
        "category": "broad_technical",
        "rationale": "Potential Energy Surface is a fundamental concept in chemistry that connects to a wide range of studies on molecular interactions.",
        "novelty_score": 0.4,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.68
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Freezing String Method",
      "resolved_canonical": "Freezing String Method",
      "decision": "linked",
      "scores": {
        "novelty": 0.67,
        "connectivity": 0.65,
        "specificity": 0.79,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Transition State Search",
      "resolved_canonical": "Transition State Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.61,
        "connectivity": 0.77,
        "specificity": 0.81,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Potential Energy Surface",
      "resolved_canonical": "Potential Energy Surface",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.68
      }
    }
  ]
}
-->

# Efficient Transition State Searches by Freezing String Method with Graph Neural Network Potentials

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2501.06159.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2501.06159](https://arxiv.org/abs/2501.06159)

## 🔗 유사한 논문
- [[2025-09-23/Active Learning for Machine Learning Driven Molecular Dynamics_20250923|Active Learning for Machine Learning Driven Molecular Dynamics]] (80.1% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (79.4% similar)
- [[2025-09-22/An Equivariant Graph Network for Interpretable Nanoporous Materials Design_20250922|An Equivariant Graph Network for Interpretable Nanoporous Materials Design]] (79.3% similar)
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (79.2% similar)
- [[2025-09-17/An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction_20250917|An End-to-End Differentiable, Graph Neural Network-Embedded Pore Network Model for Permeability Prediction]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Potential Energy Surface|Potential Energy Surface]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Freezing String Method|Freezing String Method]], [[keywords/Transition State Search|Transition State Search]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2501.06159v2 Announce Type: replace-cross 
Abstract: Transition state (TS) searches are a critical bottleneck in computational studies of chemical reactivity, as accurately capturing complex phenomena like bond breaking and formation events requires repeated evaluations of expensive ab-initio potential energy surfaces (PESs). While numerous algorithms have been developed to locate TSs efficiently, the computational cost of PES evaluations remains a key limitation. In this work, we develop and fine-tune a graph neural network (GNN) PES to accelerate TS searches for organic reactions. Our GNN of choice, SchNet, is first pre-trained on the ANI-1 dataset and subsequently fine-tuned on a small dataset of reactant, product, and TS structures. We integrate this GNN PES into the Freezing String Method (FSM), enabling rapid generation of TS guess geometries. Across a benchmark suite of chemically diverse reactions, our fine-tuned model (GNN-FT) achieves a 100% success rate, locating the reference TSs in all cases while reducing the number of ab-initio calculations by 72% on average compared to conventional DFT-based FSM searches. Fine-tuning reduces GNN-FT errors by orders of magnitude for out-of-distribution cases such as non-covalent interactions, and improves TS-region predictions with comparatively little data. Analysis of transition state geometries and energy errors shows that GNN-FT captures PES along the reaction coordinate with sufficient accuracy to serve as a reliable DFT surrogate. These results demonstrate that modern GNN potentials, when properly trained, can significantly reduce the cost of TS searches and broaden the scope and size of systems considered in chemical reactivity studies.

## 📝 요약

이 논문은 유기 반응의 전이 상태(TS) 검색을 가속화하기 위해 그래프 신경망(GNN)을 활용한 잠재 에너지 표면(PES) 모델을 개발하고 조정한 연구입니다. SchNet GNN을 ANI-1 데이터셋으로 사전 학습한 후, 반응물, 생성물, TS 구조의 소규모 데이터셋으로 미세 조정했습니다. 이를 Freezing String Method(FSM)에 통합하여 TS 추정 기하학을 빠르게 생성했습니다. 결과적으로, 다양한 화학 반응에서 GNN-FT 모델은 100% 성공률을 보였으며, 전통적인 DFT 기반 FSM 검색에 비해 평균 72%의 계산 비용을 절감했습니다. 특히 비공유 결합 상호작용 같은 분포 외 사례에서도 높은 정확성을 보였습니다. 이 연구는 GNN 잠재력이 TS 검색 비용을 크게 줄이고, 화학 반응성 연구의 범위와 규모를 확장할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 전이 상태(Transition State, TS) 검색은 화학 반응성 연구에서 중요한 병목 현상으로, 복잡한 현상을 정확히 포착하기 위해 반복적인 고비용의 ab-initio 포텐셜 에너지 표면(PES) 평가가 필요합니다.
- 2. 본 연구에서는 유기 반응의 TS 검색을 가속화하기 위해 그래프 신경망(GNN) PES를 개발하고 조정하였으며, SchNet을 선택하여 ANI-1 데이터셋으로 사전 학습한 후 소규모 데이터셋으로 미세 조정하였습니다.
- 3. GNN PES를 Freezing String Method(FSM)에 통합하여 TS 추정 기하학을 빠르게 생성할 수 있게 하였으며, GNN-FT 모델은 다양한 화학 반응에서 100% 성공률을 기록하였습니다.
- 4. GNN-FT는 전통적인 DFT 기반 FSM 검색에 비해 평균적으로 ab-initio 계산 횟수를 72% 줄였으며, 비공유 상호작용과 같은 분포 외 사례에서도 오류를 크게 줄였습니다.
- 5. 연구 결과는 현대 GNN 포텐셜이 적절히 학습되면 TS 검색 비용을 크게 줄이고 화학 반응성 연구에서 고려할 수 있는 시스템의 범위와 크기를 확장할 수 있음을 보여줍니다.


---

*Generated on 2025-09-24 02:59:57*