# EvoBrain: Dynamic Multi-channel EEG Graph Modeling for Time-evolving Brain Network

**Korean Title:** EvoBrain: 시간에 따라 변화하는 뇌 네트워크를 위한 동적 다채널 EEG 그래프 모델링

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Time-evolving Brain Network

## 🔗 유사한 논문
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (83.7% similar)
- [[2025-09-17/Personalization on a Budget_ Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection_20250917|Personalization on a Budget Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (82.8% similar)
- [[2025-09-22/IEFS-GMB_ Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders_20250922|IEFS-GMB Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders]] (82.7% similar)
- [[2025-09-18/Explaining deep learning for ECG using time-localized clusters_20250918|Explaining deep learning for ECG using time-localized clusters]] (82.3% similar)
- [[2025-09-19/UMind_ A Unified Multitask Network for Zero-Shot MEEG Visual Decoding_20250919|UMind A Unified Multitask Network for Zero-Shot MEEG Visual Decoding]] (81.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15857v1 Announce Type: cross 
Abstract: Dynamic GNNs, which integrate temporal and spatial features in Electroencephalography (EEG) data, have shown great potential in automating seizure detection. However, fully capturing the underlying dynamics necessary to represent brain states, such as seizure and non-seizure, remains a non-trivial task and presents two fundamental challenges. First, most existing dynamic GNN methods are built on temporally fixed static graphs, which fail to reflect the evolving nature of brain connectivity during seizure progression. Second, current efforts to jointly model temporal signals and graph structures and, more importantly, their interactions remain nascent, often resulting in inconsistent performance. To address these challenges, we present the first theoretical analysis of these two problems, demonstrating the effectiveness and necessity of explicit dynamic modeling and time-then-graph dynamic GNN method. Building on these insights, we propose EvoBrain, a novel seizure detection model that integrates a two-stream Mamba architecture with a GCN enhanced by Laplacian Positional Encoding, following neurological insights. Moreover, EvoBrain incorporates explicitly dynamic graph structures, allowing both nodes and edges to evolve over time. Our contributions include (a) a theoretical analysis proving the expressivity advantage of explicit dynamic modeling and time-then-graph over other approaches, (b) a novel and efficient model that significantly improves AUROC by 23% and F1 score by 30%, compared with the dynamic GNN baseline, and (c) broad evaluations of our method on the challenging early seizure prediction tasks.

## 🔍 Abstract (한글 번역)

arXiv:2509.15857v1 발표 유형: 교차  
초록: 동적 그래프 신경망(Dynamic GNNs)은 뇌전도(EEG) 데이터에서 시간적 및 공간적 특징을 통합하여 발작 탐지를 자동화하는 데 큰 잠재력을 보여주고 있습니다. 그러나 발작 및 비발작과 같은 뇌 상태를 나타내는 데 필요한 기본 동적 특성을 완전히 포착하는 것은 여전히 어려운 과제이며 두 가지 근본적인 도전 과제를 제시합니다. 첫째, 대부분의 기존 동적 GNN 방법은 시간적으로 고정된 정적 그래프를 기반으로 구축되어 발작 진행 중 뇌 연결성의 진화하는 특성을 반영하지 못합니다. 둘째, 시간 신호와 그래프 구조를 공동으로 모델링하고, 더 나아가 이들의 상호작용을 모델링하려는 현재의 노력은 초기 단계에 머물러 있어 일관되지 않은 성능을 초래하는 경우가 많습니다. 이러한 문제를 해결하기 위해 우리는 이 두 가지 문제에 대한 최초의 이론적 분석을 제시하여 명시적 동적 모델링과 시간-그래프 동적 GNN 방법의 효과와 필요성을 입증합니다. 이러한 통찰을 바탕으로, 우리는 신경학적 통찰을 따르는 라플라시안 위치 인코딩으로 강화된 GCN과 함께 이중 스트림 맘바 아키텍처를 통합한 새로운 발작 탐지 모델인 EvoBrain을 제안합니다. 더욱이, EvoBrain은 명시적으로 동적 그래프 구조를 통합하여 노드와 엣지가 시간이 지남에 따라 진화할 수 있도록 합니다. 우리의 기여는 (a) 명시적 동적 모델링과 시간-그래프 접근 방식이 다른 접근 방식보다 표현력에서 우위를 가진다는 이론적 분석, (b) 동적 GNN 기준선과 비교하여 AUROC를 23% 및 F1 점수를 30% 향상시키는 새로운 효율적인 모델, (c) 도전적인 초기 발작 예측 과제에 대한 우리의 방법의 광범위한 평가를 포함합니다.

## 📝 요약

이 논문은 EEG 데이터를 활용한 발작 탐지 자동화에서 동적 GNN의 잠재력을 탐구하며, 두 가지 주요 문제를 해결하고자 합니다. 첫째, 기존 동적 GNN은 고정된 그래프를 사용해 발작 진행 중의 뇌 연결 변화를 제대로 반영하지 못합니다. 둘째, 시계열 신호와 그래프 구조의 상호작용을 효과적으로 모델링하지 못해 성능이 일관되지 않습니다. 이를 해결하기 위해, 저자들은 명시적인 동적 모델링과 시간-그래프 순서의 동적 GNN 방법론의 필요성을 이론적으로 분석하고, EvoBrain이라는 새로운 발작 탐지 모델을 제안합니다. EvoBrain은 Mamba 아키텍처와 라플라시안 위치 인코딩을 결합하여 노드와 엣지가 시간에 따라 진화하는 동적 그래프 구조를 통합합니다. 이 모델은 AUROC와 F1 점수를 각각 23%와 30% 향상시키며, 초기 발작 예측 과제에서도 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. EEG 데이터의 시간적 및 공간적 특징을 통합하는 동적 GNN이 발작 탐지 자동화에 큰 잠재력을 보이고 있음.

- 2. 기존 동적 GNN 방법은 고정된 정적 그래프에 기반하여 발작 진행 중 뇌 연결성의 변화를 반영하지 못함.

- 3. 시간 신호와 그래프 구조의 상호작용을 공동으로 모델링하는 시도가 초기 단계에 머물러 있어 일관된 성능을 보이지 않음.

- 4. EvoBrain 모델은 명시적 동적 모델링과 시간-그래프 순서의 동적 GNN 방법의 표현력 우위를 이론적으로 분석하고 이를 기반으로 개발됨.

- 5. EvoBrain은 AUROC를 23%, F1 점수를 30% 향상시키며, 초기 발작 예측 작업에서 광범위한 평가를 통해 그 효율성을 입증함.

---

*Generated on 2025-09-22 14:13:57*