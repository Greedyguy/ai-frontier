# DualEdit: Dual Editing for Knowledge Updating in Vision-Language Models

**Korean Title:** 듀얼에딧: 비전-언어 모델에서 지식 업데이트를 위한 이중 편집

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Cross-modal Knowledge Updating

## 🔗 유사한 논문
- [[2025-09-18/EdiVal-Agent_ An Object-Centric Framework for Automated, Scalable, Fine-Grained Evaluation of Multi-Turn Editing_20250918|EdiVal-Agent An Object-Centric Framework for Automated, Scalable, Fine-Grained Evaluation of Multi-Turn Editing]] (82.2% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (81.8% similar)
- [[2025-09-18/DPDEdit_ Detail-Preserved Diffusion Models for Multimodal Fashion Image Editing_20250918|DPDEdit Detail-Preserved Diffusion Models for Multimodal Fashion Image Editing]] (81.7% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (81.5% similar)
- [[2025-09-19/V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (81.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.13638v2 Announce Type: replace-cross 
Abstract: Model editing aims to efficiently update a pre-trained model's knowledge without the need for time-consuming full retraining. While existing pioneering editing methods achieve promising results, they primarily focus on editing single-modal language models (LLMs). However, for vision-language models (VLMs), which involve multiple modalities, the role and impact of each modality on editing performance remain largely unexplored. To address this gap, we explore the impact of textual and visual modalities on model editing and find that: (1) textual and visual representations reach peak sensitivity at different layers, reflecting their varying importance; and (2) editing both modalities can efficiently update knowledge, but this comes at the cost of compromising the model's original capabilities. Based on our findings, we propose DualEdit, an editor that modifies both textual and visual modalities at their respective key layers. Additionally, we introduce a gating module within the more sensitive textual modality, allowing DualEdit to efficiently update new knowledge while preserving the model's original information. We evaluate DualEdit across multiple VLM backbones and benchmark datasets, demonstrating its superiority over state-of-the-art VLM editing baselines as well as adapted LLM editing methods on different evaluation metrics. Codes are available at https://github.com/zhiyiscs/DualEdit

## 🔍 Abstract (한글 번역)

arXiv:2506.13638v2 발표 유형: 교차 교체  
초록: 모델 편집은 시간 소모적인 전체 재훈련 없이 사전 훈련된 모델의 지식을 효율적으로 업데이트하는 것을 목표로 합니다. 기존의 선구적인 편집 방법들은 유망한 결과를 달성하지만, 주로 단일 모달 언어 모델(LLMs)의 편집에 초점을 맞추고 있습니다. 그러나 여러 모달리티를 포함하는 비전-언어 모델(VLMs)의 경우, 각 모달리티가 편집 성능에 미치는 역할과 영향은 거의 탐구되지 않았습니다. 이 격차를 해결하기 위해, 우리는 모델 편집에 대한 텍스트 및 시각적 모달리티의 영향을 탐구하고 다음과 같은 사실을 발견했습니다: (1) 텍스트 및 시각적 표현은 서로 다른 레이어에서 최대 민감도에 도달하며, 이는 그들의 중요성이 다름을 반영합니다; (2) 두 모달리티를 편집하는 것은 지식을 효율적으로 업데이트할 수 있지만, 이는 모델의 원래 기능을 손상시키는 대가를 치릅니다. 우리의 발견에 기반하여, 우리는 각 모달리티의 주요 레이어에서 텍스트 및 시각적 모달리티를 수정하는 편집기인 DualEdit을 제안합니다. 추가로, 더 민감한 텍스트 모달리티 내에 게이팅 모듈을 도입하여 DualEdit이 모델의 원래 정보를 보존하면서 새로운 지식을 효율적으로 업데이트할 수 있도록 합니다. 우리는 여러 VLM 백본과 벤치마크 데이터셋에 걸쳐 DualEdit을 평가하여, 다양한 평가 지표에서 최첨단 VLM 편집 기준선 및 적응된 LLM 편집 방법보다 우수함을 입증했습니다. 코드는 https://github.com/zhiyiscs/DualEdit에서 제공됩니다.

## 📝 요약

이 논문은 사전 학습된 모델의 지식을 효율적으로 업데이트하는 모델 편집 기법을 다룹니다. 특히, 기존 연구들이 주로 단일 모달 언어 모델에 집중한 반면, 이 연구는 텍스트와 시각적 모달리티를 모두 포함하는 비전-언어 모델(VLM)의 편집 성능에 미치는 영향을 조사합니다. 연구 결과, 텍스트와 시각적 표현은 서로 다른 층에서 최대 민감도를 보이며, 두 모달리티를 동시에 편집할 경우 모델의 원래 기능이 손상될 수 있음을 발견했습니다. 이를 바탕으로, DualEdit라는 편집기를 제안하여 각 모달리티의 핵심 층을 수정하고, 텍스트 모달리티에 게이팅 모듈을 도입하여 새로운 지식을 효율적으로 업데이트하면서도 모델의 기존 정보를 보존합니다. DualEdit는 여러 VLM 백본과 벤치마크 데이터셋에서 기존 최첨단 VLM 편집 기법 및 적응된 LLM 편집 방법보다 우수한 성능을 보였습니다. 코드도 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 모델 편집은 사전 훈련된 모델의 지식을 효율적으로 업데이트하는 것을 목표로 하며, 기존 방법들은 주로 단일 모달 언어 모델에 초점을 맞추고 있다.

- 2. 비전-언어 모델(VLMs)에서는 텍스트와 시각적 모달리티가 편집 성능에 미치는 영향이 아직 충분히 탐구되지 않았다.

- 3. 텍스트와 시각적 표현은 서로 다른 계층에서 최고 민감도에 도달하며, 이는 각 모달리티의 중요성을 반영한다.

- 4. DualEdit는 텍스트와 시각적 모달리티를 각각의 주요 계층에서 수정하여 효율적으로 지식을 업데이트하는 편집기를 제안한다.

- 5. DualEdit는 다양한 VLM 백본과 벤치마크 데이터셋에서 기존의 VLM 편집 방법 및 적응된 LLM 편집 방법보다 우수한 성능을 보인다.

---

*Generated on 2025-09-22 14:55:29*