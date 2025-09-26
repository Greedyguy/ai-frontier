---
keywords:
  - Graph Neural Network
  - Electroencephalography
  - Seizure Detection
  - Laplacian Positional Encoding
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15857
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T09:17:08.120010",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Graph Neural Network",
    "Electroencephalography",
    "Seizure Detection",
    "Laplacian Positional Encoding"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Graph Neural Network": 0.8,
    "Electroencephalography": 0.75,
    "Seizure Detection": 0.78,
    "Laplacian Positional Encoding": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Dynamic GNNs",
        "canonical": "Graph Neural Network",
        "aliases": [
          "Dynamic Graph Neural Networks"
        ],
        "category": "specific_connectable",
        "rationale": "Dynamic GNNs are a key focus of the paper and connect well with existing Graph Neural Network literature.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "EEG data",
        "canonical": "Electroencephalography",
        "aliases": [
          "EEG"
        ],
        "category": "unique_technical",
        "rationale": "EEG data is central to the study's context, linking neuroscience with machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Seizure detection",
        "canonical": "Seizure Detection",
        "aliases": [
          "Epileptic Seizure Detection"
        ],
        "category": "unique_technical",
        "rationale": "Seizure detection is a specific application area that enhances the paper's focus on medical applications.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Laplacian Positional Encoding",
        "canonical": "Laplacian Positional Encoding",
        "aliases": [
          "Laplacian Encoding"
        ],
        "category": "unique_technical",
        "rationale": "This technique is novel in the context of the paper, offering a unique approach to graph modeling.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Dynamic GNNs",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "EEG data",
      "resolved_canonical": "Electroencephalography",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Seizure detection",
      "resolved_canonical": "Seizure Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Laplacian Positional Encoding",
      "resolved_canonical": "Laplacian Positional Encoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# EvoBrain: Dynamic Multi-channel EEG Graph Modeling for Time-evolving Brain Network

**Korean Title:** EvoBrain: 시간에 따라 변화하는 뇌 네트워크를 위한 동적 다채널 EEG 그래프 모델링

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15857.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15857](https://arxiv.org/abs/2509.15857)

## 🔗 유사한 논문
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN: A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (83.7% similar)
- [[2025-09-17/Personalization on a Budget_ Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection_20250917|Personalization on a Budget: Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (82.8% similar)
- [[2025-09-22/IEFS-GMB_ Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders_20250922|IEFS-GMB: Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders]] (82.7% similar)
- [[2025-09-18/Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (82.3% similar)
- [[2025-09-19/UMind_ A Unified Multitask Network for Zero-Shot M/EEG Visual Decoding_20250919|UMind: A Unified Multitask Network for Zero-Shot M/EEG Visual Decoding]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Electroencephalography|Electroencephalography]], [[keywords/Seizure Detection|Seizure Detection]], [[keywords/Laplacian Positional Encoding|Laplacian Positional Encoding]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15857v1 Announce Type: cross 
Abstract: Dynamic GNNs, which integrate temporal and spatial features in Electroencephalography (EEG) data, have shown great potential in automating seizure detection. However, fully capturing the underlying dynamics necessary to represent brain states, such as seizure and non-seizure, remains a non-trivial task and presents two fundamental challenges. First, most existing dynamic GNN methods are built on temporally fixed static graphs, which fail to reflect the evolving nature of brain connectivity during seizure progression. Second, current efforts to jointly model temporal signals and graph structures and, more importantly, their interactions remain nascent, often resulting in inconsistent performance. To address these challenges, we present the first theoretical analysis of these two problems, demonstrating the effectiveness and necessity of explicit dynamic modeling and time-then-graph dynamic GNN method. Building on these insights, we propose EvoBrain, a novel seizure detection model that integrates a two-stream Mamba architecture with a GCN enhanced by Laplacian Positional Encoding, following neurological insights. Moreover, EvoBrain incorporates explicitly dynamic graph structures, allowing both nodes and edges to evolve over time. Our contributions include (a) a theoretical analysis proving the expressivity advantage of explicit dynamic modeling and time-then-graph over other approaches, (b) a novel and efficient model that significantly improves AUROC by 23% and F1 score by 30%, compared with the dynamic GNN baseline, and (c) broad evaluations of our method on the challenging early seizure prediction tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.15857v1 발표 유형: 교차  
초록: EEG(뇌전도) 데이터에서 시간적 및 공간적 특징을 통합하는 동적 GNN은 발작 탐지를 자동화하는 데 큰 잠재력을 보여주고 있습니다. 그러나 발작 및 비발작과 같은 뇌 상태를 나타내는 데 필요한 근본적인 역학을 완전히 포착하는 것은 여전히 어려운 과제이며 두 가지 근본적인 문제를 제기합니다. 첫째, 대부분의 기존 동적 GNN 방법은 시간적으로 고정된 정적 그래프를 기반으로 구축되어 발작 진행 중 뇌 연결의 변화하는 특성을 반영하지 못합니다. 둘째, 시간 신호와 그래프 구조, 더 나아가 그 상호작용을 공동으로 모델링하려는 현재의 노력은 초기 단계에 있으며, 종종 일관되지 않은 성능을 초래합니다. 이러한 문제를 해결하기 위해 우리는 이 두 가지 문제에 대한 최초의 이론적 분석을 제시하고 명시적 동적 모델링과 시간-그다음-그래프 동적 GNN 방법의 효과와 필요성을 입증합니다. 이러한 통찰력을 바탕으로 우리는 신경학적 통찰을 따르는 라플라시안 위치 인코딩으로 강화된 GCN과 이중 스트림 맘바 아키텍처를 통합한 새로운 발작 탐지 모델인 EvoBrain을 제안합니다. 더욱이, EvoBrain은 명시적으로 동적 그래프 구조를 통합하여 노드와 엣지가 시간에 따라 진화할 수 있도록 합니다. 우리의 기여는 (a) 명시적 동적 모델링과 시간-그다음-그래프 접근 방식의 표현력 우위를 입증하는 이론적 분석, (b) 동적 GNN 기준선과 비교하여 AUROC를 23%, F1 점수를 30% 향상시키는 새로운 효율적인 모델, (c) 도전적인 초기 발작 예측 작업에 대한 우리의 방법의 광범위한 평가를 포함합니다.

## 📝 요약

이 논문은 뇌전증 발작 감지를 자동화하기 위해 EEG 데이터의 시간적 및 공간적 특징을 통합하는 동적 그래프 신경망(Dynamic GNN)의 한계를 극복하고자 합니다. 기존 방법들은 발작 진행 중 뇌 연결성의 변화를 반영하지 못하는 고정된 그래프에 의존하며, 시간 신호와 그래프 구조의 상호작용을 효과적으로 모델링하지 못합니다. 이를 해결하기 위해 저자들은 명시적 동적 모델링과 시간-그래프 순서의 동적 GNN 방법의 필요성을 이론적으로 분석하고, EvoBrain이라는 새로운 발작 감지 모델을 제안합니다. EvoBrain은 두 개의 스트림으로 구성된 Mamba 아키텍처와 라플라시안 위치 인코딩이 강화된 GCN을 통합하며, 시간에 따라 변화하는 그래프 구조를 포함합니다. 이 모델은 AUROC를 23%, F1 점수를 30% 향상시키며, 초기 발작 예측 작업에서 우수한 성능을 보입니다.

## 🎯 주요 포인트

- 1. 동적 GNN은 EEG 데이터에서 발작 감지를 자동화하는 데 큰 잠재력을 보이지만, 뇌 상태를 완전히 표현하는 것은 여전히 어려운 과제입니다.
- 2. 기존 동적 GNN 방법은 시간적으로 고정된 정적 그래프에 기반하여 발작 진행 중 뇌 연결성의 변화를 반영하지 못합니다.
- 3. 시간 신호와 그래프 구조의 상호작용을 공동으로 모델링하는 현재의 노력은 초기 단계에 있으며, 일관되지 않은 성능을 초래합니다.
- 4. EvoBrain은 두 개의 스트림 Mamba 아키텍처와 라플라시안 위치 인코딩으로 강화된 GCN을 통합하여 발작 감지 성능을 크게 향상시킵니다.
- 5. EvoBrain은 명시적으로 동적 그래프 구조를 포함하여 시간에 따라 노드와 엣지가 진화할 수 있도록 설계되었습니다.


---

*Generated on 2025-09-23 09:17:08*