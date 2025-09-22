# Structure Matters: Brain Graph Augmentation via Learnable Edge Masking for Data-efficient Psychiatric Diagnosis

**Korean Title:** 구조의 중요성: 데이터 효율적인 정신과 진단을 위한 학습 가능한 엣지 마스킹을 통한 뇌 그래프 증강

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Structure-aware Augmentation

## 🔗 유사한 논문
- [[2025-09-19/Brain-HGCN_ A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis_20250919|Brain-HGCN A Hyperbolic Graph Convolutional Network for Brain Functional Network Analysis]] (82.1% similar)
- [[2025-09-22/EvoBrain_ Dynamic Multi-channel EEG Graph Modeling for Time-evolving Brain Network_20250922|EvoBrain Dynamic Multi-channel EEG Graph Modeling for Time-evolving Brain Network]] (80.7% similar)
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (79.9% similar)
- [[2025-09-17/Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation_20250917|Consistent View Alignment Improves Foundation Models for 3D Medical Image Segmentation]] (79.7% similar)
- [[2025-09-19/UMind_ A Unified Multitask Network for Zero-Shot MEEG Visual Decoding_20250919|UMind A Unified Multitask Network for Zero-Shot MEEG Visual Decoding]] (79.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.09744v2 Announce Type: replace-cross 
Abstract: The limited availability of labeled brain network data makes it challenging to achieve accurate and interpretable psychiatric diagnoses. While self-supervised learning (SSL) offers a promising solution, existing methods often rely on augmentation strategies that can disrupt crucial structural semantics in brain graphs. To address this, we propose SAM-BG, a two-stage framework for learning brain graph representations with structural semantic preservation. In the pre-training stage, an edge masker is trained on a small labeled subset to capture key structural semantics. In the SSL stage, the extracted structural priors guide a structure-aware augmentation process, enabling the model to learn more semantically meaningful and robust representations. Experiments on two real-world psychiatric datasets demonstrate that SAM-BG outperforms state-of-the-art methods, particularly in small-labeled data settings, and uncovers clinically relevant connectivity patterns that enhance interpretability. Our code is available at https://github.com/mjliu99/SAM-BG.

## 🔍 Abstract (한글 번역)

arXiv:2509.09744v2 발표 유형: 교차 교체  
초록: 라벨이 지정된 뇌 네트워크 데이터의 제한된 가용성은 정확하고 해석 가능한 정신과 진단을 달성하는 데 어려움을 줍니다. 자가 지도 학습(SSL)은 유망한 해결책을 제공하지만, 기존 방법들은 종종 뇌 그래프의 중요한 구조적 의미를 방해할 수 있는 증강 전략에 의존합니다. 이를 해결하기 위해, 우리는 구조적 의미 보존을 통해 뇌 그래프 표현을 학습하는 두 단계의 프레임워크인 SAM-BG를 제안합니다. 사전 학습 단계에서는 소량의 라벨이 지정된 하위 집합에서 엣지 마스커를 훈련하여 주요 구조적 의미를 포착합니다. SSL 단계에서는 추출된 구조적 사전 지식이 구조 인식 증강 과정을 안내하여 모델이 더 의미 있고 강력한 표현을 학습할 수 있게 합니다. 두 개의 실제 정신과 데이터셋에 대한 실험 결과, SAM-BG는 특히 소량의 라벨이 지정된 데이터 환경에서 최첨단 방법들을 능가하며, 해석 가능성을 향상시키는 임상적으로 관련된 연결 패턴을 발견합니다. 우리의 코드는 https://github.com/mjliu99/SAM-BG에서 이용할 수 있습니다.

## 📝 요약

SAM-BG는 구조적 의미 보존을 통해 뇌 그래프 표현을 학습하는 두 단계 프레임워크로, 제한된 라벨 뇌 네트워크 데이터의 문제를 해결하고자 합니다. 첫 번째 단계에서는 소량의 라벨 데이터로 엣지 마스커를 훈련하여 주요 구조적 의미를 포착합니다. 두 번째 단계에서는 추출된 구조적 사전 지식을 활용해 구조 인식 증강 과정을 진행하여 의미 있고 강력한 표현을 학습합니다. 두 개의 실제 정신과 데이터셋 실험에서 SAM-BG는 특히 소량의 라벨 데이터 환경에서 기존 방법보다 우수한 성능을 보였으며, 임상적으로 중요한 연결 패턴을 발견하여 해석 가능성을 높였습니다.

## 🎯 주요 포인트

- 1. SAM-BG는 구조적 의미 보존을 통해 뇌 그래프 표현을 학습하는 두 단계 프레임워크를 제안합니다.

- 2. 소량의 라벨링된 데이터로 훈련된 엣지 마스커가 핵심 구조적 의미를 포착합니다.

- 3. 구조적 사전 지식은 구조 인식 증강 과정을 안내하여 의미 있고 강력한 표현 학습을 가능하게 합니다.

- 4. SAM-BG는 소량의 라벨링된 데이터 환경에서 기존 방법보다 우수한 성능을 보이며, 임상적으로 관련 있는 연결 패턴을 발견하여 해석 가능성을 높입니다.

- 5. 제안된 방법의 코드는 https://github.com/mjliu99/SAM-BG에서 제공됩니다.

---

*Generated on 2025-09-22 15:03:07*