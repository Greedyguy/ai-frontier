
# UMind: A Unified Multitask Network for Zero-Shot M/EEG Visual Decoding

**Korean Title:** UMind: 제로샷 M/EEG 시각 디코딩을 위한 통합 멀티태스크 네트워크

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Multitask Visual Decoding

## 🔗 유사한 논문
- [[Reconstruction Alignment Improves Unified Multimodal Models_20250919|Reconstruction Alignment Improves Unified Multimodal Models]] (82.8% similar)
- [[UnifiedVisual A Framework for Constructing Unified Vision-Language Datasets]] (82.1% similar)
- [[Intelligent Healthcare Imaging Platform An VLM-Based Framework for Automated Medical Image Analysis and Clinical Report Generation]] (81.9% similar)
- [[Personalization on a Budget Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (81.1% similar)
- [[VocSegMRI Multimodal Learning for Precise Vocal Tract Segmentation in Real-time MRI]] (80.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14772v1 Announce Type: new 
Abstract: Decoding visual information from time-resolved brain recordings, such as EEG and MEG, plays a pivotal role in real-time brain-computer interfaces. However, existing approaches primarily focus on direct brain-image feature alignment and are limited to single-task frameworks or task-specific models. In this paper, we propose a Unified MultItask Network for zero-shot M/EEG visual Decoding (referred to UMind), including visual stimulus retrieval, classification, and reconstruction, where multiple tasks mutually enhance each other. Our method learns robust neural-visual and semantic representations through multimodal alignment with both image and text modalities. The integration of both coarse and fine-grained texts enhances the extraction of these neural representations, enabling more detailed semantic and visual decoding. These representations then serve as dual conditional inputs to a pre-trained diffusion model, guiding visual reconstruction from both visual and semantic perspectives. Extensive evaluations on MEG and EEG datasets demonstrate the effectiveness, robustness, and biological plausibility of our approach in capturing spatiotemporal neural dynamics. Our approach sets a multitask pipeline for brain visual decoding, highlighting the synergy of semantic information in visual feature extraction.

## 🔍 Abstract (한글 번역)

arXiv:2509.14772v1 발표 유형: 신규  
초록: EEG 및 MEG와 같은 시간 분해된 뇌 기록으로부터 시각 정보를 해독하는 것은 실시간 뇌-컴퓨터 인터페이스에서 중요한 역할을 합니다. 그러나 기존 접근 방식은 주로 직접적인 뇌-이미지 특징 정렬에 초점을 맞추고 있으며, 단일 작업 프레임워크나 작업별 모델에 국한되어 있습니다. 본 논문에서는 시각 자극 검색, 분류 및 재구성을 포함하여 여러 작업이 서로를 상호 보완하는 제로샷 M/EEG 시각 해독을 위한 통합 다중 작업 네트워크(UMind)를 제안합니다. 우리의 방법은 이미지 및 텍스트 모달리티와의 다중 모달 정렬을 통해 강력한 신경-시각 및 의미 표현을 학습합니다. 거친 텍스트와 세밀한 텍스트의 통합은 이러한 신경 표현의 추출을 강화하여 보다 세부적인 의미 및 시각 해독을 가능하게 합니다. 이러한 표현은 사전 훈련된 확산 모델에 대한 이중 조건 입력으로 작용하여 시각 및 의미적 관점에서 시각 재구성을 안내합니다. MEG 및 EEG 데이터셋에 대한 광범위한 평가를 통해 우리의 접근 방식이 시공간 신경 역학을 포착하는 데 있어 효과적이고, 견고하며, 생물학적으로 타당함을 입증합니다. 우리의 접근 방식은 뇌 시각 해독을 위한 다중 작업 파이프라인을 설정하여 시각 특징 추출에서 의미 정보의 시너지를 강조합니다.

## 📝 요약

이 논문에서는 실시간 뇌-컴퓨터 인터페이스에서 중요한 역할을 하는 EEG와 MEG와 같은 시간 분해 뇌 기록에서 시각 정보를 해독하기 위한 새로운 방법론을 제안합니다. 기존 방법들이 단일 작업에 국한된 반면, 본 연구는 시각 자극 검색, 분류, 재구성을 포함하는 다중 작업 네트워크인 UMind를 제안하여 각 작업이 상호 보완적으로 작용하도록 합니다. 이미지와 텍스트 모달리티를 활용한 다중 모달 정렬을 통해 강력한 신경-시각 및 의미 표현을 학습하며, 이를 통해 더 상세한 의미 및 시각 해독이 가능합니다. 이러한 표현은 사전 학습된 확산 모델의 조건부 입력으로 사용되어 시각 및 의미적 관점에서 시각 재구성을 유도합니다. MEG와 EEG 데이터셋에 대한 광범위한 평가를 통해 본 접근법의 효과성, 강건성 및 생물학적 타당성을 입증하였으며, 시각 특징 추출에서 의미 정보의 시너지를 강조합니다.

## 🎯 주요 포인트

- 1. UMind는 시각적 자극 검색, 분류 및 재구성을 포함하는 다중 작업 네트워크로, 여러 작업이 상호 보완적으로 작용합니다.

- 2. 이 방법은 이미지와 텍스트 모달리티를 통한 다중 모달 정렬을 통해 강력한 신경-시각 및 의미 표현을 학습합니다.

- 3. 세밀한 텍스트 통합은 신경 표현의 추출을 강화하여 더 상세한 의미 및 시각적 디코딩을 가능하게 합니다.

- 4. 사전 훈련된 확산 모델에 이중 조건 입력으로 사용되어 시각 및 의미 관점에서 시각적 재구성을 안내합니다.

- 5. MEG 및 EEG 데이터셋에 대한 광범위한 평가를 통해 우리의 접근 방식이 시공간 신경 역학을 포착하는 데 효과적이고 강력하며 생물학적으로 타당함을 입증했습니다.

---

*Generated on 2025-09-19 16:47:54*