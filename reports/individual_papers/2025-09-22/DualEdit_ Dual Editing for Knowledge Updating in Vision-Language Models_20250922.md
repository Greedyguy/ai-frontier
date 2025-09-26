---
keywords:
  - Vision-Language Model
  - Model Editing
  - DualEdit
  - Multimodal Learning
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2506.13638
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:03:52.421218",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Model Editing",
    "DualEdit",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Model Editing": 0.78,
    "DualEdit": 0.82,
    "Multimodal Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper and represent an evolved concept crucial for linking multimodal learning discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Model Editing",
        "canonical": "Model Editing",
        "aliases": [
          "Knowledge Updating",
          "Model Update"
        ],
        "category": "unique_technical",
        "rationale": "Model Editing is a unique technical concept introduced in the paper, focusing on updating models without full retraining.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.81,
        "link_intent_score": 0.78
      },
      {
        "surface": "DualEdit",
        "canonical": "DualEdit",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "DualEdit is a novel method proposed in the paper, specifically designed for editing both textual and visual modalities in VLMs.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multimodal Learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is a key area related to the integration of textual and visual modalities, enhancing the connectivity of the paper's concepts.",
        "novelty_score": 0.48,
        "connectivity_score": 0.83,
        "specificity_score": 0.77,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "full retraining",
      "evaluation metrics"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Model Editing",
      "resolved_canonical": "Model Editing",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.81,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "DualEdit",
      "resolved_canonical": "DualEdit",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multimodal Learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.48,
        "connectivity": 0.83,
        "specificity": 0.77,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# DualEdit: Dual Editing for Knowledge Updating in Vision-Language Models

**Korean Title:** 이중 편집: 비전-언어 모델에서 지식 업데이트를 위한 이중 편집

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.13638.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2506.13638](https://arxiv.org/abs/2506.13638)

## 🔗 유사한 논문
- [[2025-09-18/EdiVal-Agent_ An Object-Centric Framework for Automated, Scalable, Fine-Grained Evaluation of Multi-Turn Editing_20250918|EdiVal-Agent: An Object-Centric Framework for Automated, Scalable, Fine-Grained Evaluation of Multi-Turn Editing]] (82.2% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (81.8% similar)
- [[2025-09-18/DPDEdit_ Detail-Preserved Diffusion Models for Multimodal Fashion Image Editing_20250918|DPDEdit: Detail-Preserved Diffusion Models for Multimodal Fashion Image Editing]] (81.7% similar)
- [[2025-09-22/ViSpec_ Accelerating Vision-Language Models with Vision-Aware Speculative Decoding_20250922|ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding]] (81.5% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (81.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Model Editing|Model Editing]], [[keywords/DualEdit|DualEdit]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.13638v2 Announce Type: replace-cross 
Abstract: Model editing aims to efficiently update a pre-trained model's knowledge without the need for time-consuming full retraining. While existing pioneering editing methods achieve promising results, they primarily focus on editing single-modal language models (LLMs). However, for vision-language models (VLMs), which involve multiple modalities, the role and impact of each modality on editing performance remain largely unexplored. To address this gap, we explore the impact of textual and visual modalities on model editing and find that: (1) textual and visual representations reach peak sensitivity at different layers, reflecting their varying importance; and (2) editing both modalities can efficiently update knowledge, but this comes at the cost of compromising the model's original capabilities. Based on our findings, we propose DualEdit, an editor that modifies both textual and visual modalities at their respective key layers. Additionally, we introduce a gating module within the more sensitive textual modality, allowing DualEdit to efficiently update new knowledge while preserving the model's original information. We evaluate DualEdit across multiple VLM backbones and benchmark datasets, demonstrating its superiority over state-of-the-art VLM editing baselines as well as adapted LLM editing methods on different evaluation metrics. Codes are available at https://github.com/zhiyiscs/DualEdit

## 🔍 Abstract (한글 번역)

arXiv:2506.13638v2 발표 유형: 교차 교체  
초록: 모델 편집은 시간이 많이 소요되는 전체 재학습 없이 사전 학습된 모델의 지식을 효율적으로 업데이트하는 것을 목표로 합니다. 기존의 선구적인 편집 방법들은 유망한 결과를 달성하지만, 주로 단일 모달 언어 모델(LLMs)의 편집에 중점을 두고 있습니다. 그러나 여러 모달리티가 포함된 비전-언어 모델(VLMs)의 경우, 각 모달리티가 편집 성능에 미치는 역할과 영향은 거의 탐구되지 않았습니다. 이 격차를 해소하기 위해, 우리는 모델 편집에서 텍스트와 시각적 모달리티의 영향을 탐구하고 다음과 같은 결과를 발견했습니다: (1) 텍스트와 시각적 표현은 서로 다른 레이어에서 최대 민감도에 도달하며, 이는 그들의 중요성이 다름을 반영합니다; (2) 두 모달리티를 편집하면 지식을 효율적으로 업데이트할 수 있지만, 이는 모델의 원래 기능을 손상시키는 대가를 치르게 됩니다. 우리의 발견을 바탕으로, 우리는 각각의 주요 레이어에서 텍스트와 시각적 모달리티를 수정하는 편집기인 DualEdit을 제안합니다. 또한, 더 민감한 텍스트 모달리티 내에 게이팅 모듈을 도입하여 DualEdit이 모델의 원래 정보를 보존하면서 새로운 지식을 효율적으로 업데이트할 수 있도록 합니다. 우리는 여러 VLM 백본과 벤치마크 데이터셋을 통해 DualEdit을 평가하여, 다양한 평가 지표에서 최첨단 VLM 편집 기준선뿐만 아니라 적응된 LLM 편집 방법보다 우수함을 입증합니다. 코드는 https://github.com/zhiyiscs/DualEdit에서 제공됩니다.

## 📝 요약

이 논문은 사전 학습된 모델의 지식을 효율적으로 업데이트하는 모델 편집 기법을 제안합니다. 기존 방법들은 주로 단일 모달 언어 모델에 집중했으나, 이 연구는 비전-언어 모델(VLM)에서 텍스트와 시각 모달리티의 편집 성능에 대한 영향을 탐구합니다. 연구 결과, 텍스트와 시각 표현은 서로 다른 층에서 최고 민감도를 나타내며, 두 모달리티를 편집하면 지식 업데이트가 가능하지만 모델의 원래 성능이 저하될 수 있음을 발견했습니다. 이를 바탕으로, DualEdit라는 편집기를 제안하여 텍스트와 시각 모달리티를 각각의 주요 층에서 수정하고, 텍스트 모달리티에 게이팅 모듈을 도입하여 모델의 원래 정보를 유지하면서 새로운 지식을 효율적으로 업데이트합니다. DualEdit는 다양한 VLM 백본과 벤치마크 데이터셋에서 우수한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 모델 편집은 사전 훈련된 모델의 지식을 효율적으로 업데이트하는 것을 목표로 하며, 전체 재훈련의 필요성을 줄인다.
- 2. 기존 편집 방법은 주로 단일 모달 언어 모델에 초점을 맞추고 있으며, 다중 모달을 포함하는 비전-언어 모델의 편집 성능에 대한 각 모달의 역할과 영향은 거의 탐구되지 않았다.
- 3. 텍스트와 시각적 표현은 서로 다른 레이어에서 최고 민감도에 도달하며, 이는 그들의 중요성이 다름을 반영한다.
- 4. DualEdit는 텍스트와 시각적 모달리티를 각각의 주요 레이어에서 수정하여 새로운 지식을 효율적으로 업데이트하면서도 모델의 원래 정보를 보존한다.
- 5. DualEdit는 여러 VLM 백본과 벤치마크 데이터셋에서 평가되어, 최첨단 VLM 편집 기준 및 적응된 LLM 편집 방법보다 우수한 성능을 입증했다.


---

*Generated on 2025-09-23 10:03:52*