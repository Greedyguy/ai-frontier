---
keywords:
  - Vision-Language Model
  - Test-Time Adaptation
  - Contrastive Loss
  - Outlier Contrastive Exposure
  - Zero-Shot Learning
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2507.14312
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:38:45.761013",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Test-Time Adaptation",
    "Contrastive Loss",
    "Outlier Contrastive Exposure",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Test-Time Adaptation": 0.78,
    "Contrastive Loss": 0.8,
    "Outlier Contrastive Exposure": 0.77,
    "Zero-Shot Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-language models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-language models are central to the paper's theme and connect well with multimodal and zero-shot learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Test-time adaptation",
        "canonical": "Test-Time Adaptation",
        "aliases": [
          "TTA"
        ],
        "category": "unique_technical",
        "rationale": "Test-time adaptation is a unique concept introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Contrastive loss",
        "canonical": "Contrastive Loss",
        "aliases": [
          "soft contrastive loss"
        ],
        "category": "specific_connectable",
        "rationale": "Contrastive loss is a key component of the proposed method, linking to broader contrastive learning techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Outlier Contrastive Exposure",
        "canonical": "Outlier Contrastive Exposure",
        "aliases": [
          "OCE loss"
        ],
        "category": "unique_technical",
        "rationale": "Outlier Contrastive Exposure is a novel loss function introduced for improving OOD detection, specific to this work.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Zero-shot capabilities",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "zero-shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot capabilities are crucial for understanding the performance of vision-language models under distribution shifts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.68,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "entropy minimization",
      "pseudo-label drift",
      "class collapse"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-language models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Test-time adaptation",
      "resolved_canonical": "Test-Time Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Contrastive loss",
      "resolved_canonical": "Contrastive Loss",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Outlier Contrastive Exposure",
      "resolved_canonical": "Outlier Contrastive Exposure",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Zero-shot capabilities",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.68,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# CLIPTTA: Robust Contrastive Vision-Language Test-Time Adaptation

**Korean Title:** CLIPTTA: 강건한 대조적 비전-언어 테스트 시간 적응

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2507.14312.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2507.14312](https://arxiv.org/abs/2507.14312)

## 🔗 유사한 논문
- [[2025-09-18/Singular Value Few-shot Adaptation of Vision-Language Models_20250918|Singular Value Few-shot Adaptation of Vision-Language Models]] (84.7% similar)
- [[2025-09-22/Robust Vision-Language Models via Tensor Decomposition_ A Defense Against Adversarial Attacks_20250922|Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks]] (84.0% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (83.9% similar)
- [[2025-09-22/Towards Robust Visual Continual Learning with Multi-Prototype Supervision_20250922|Towards Robust Visual Continual Learning with Multi-Prototype Supervision]] (82.7% similar)
- [[2025-09-22/Global Pre-fixing, Local Adjusting_ A Simple yet Effective Contrastive Strategy for Continual Learning_20250922|Global Pre-fixing, Local Adjusting: A Simple yet Effective Contrastive Strategy for Continual Learning]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Contrastive Loss|Contrastive Loss]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Test-Time Adaptation|Test-Time Adaptation]], [[keywords/Outlier Contrastive Exposure|Outlier Contrastive Exposure]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.14312v2 Announce Type: replace 
Abstract: Vision-language models (VLMs) like CLIP exhibit strong zero-shot capabilities but often fail to generalize under distribution shifts. Test-time adaptation (TTA) allows models to update at inference time without labeled data, typically via entropy minimization. However, this objective is fundamentally misaligned with the contrastive image-text training of VLMs, limiting adaptation performance and introducing failure modes such as pseudo-label drift and class collapse. We propose CLIPTTA, a new gradient-based TTA method for vision-language models that leverages a soft contrastive loss aligned with CLIP's pre-training objective. We provide a theoretical analysis of CLIPTTA's gradients, showing how its batch-aware design mitigates the risk of collapse. We further extend CLIPTTA to the open-set setting, where both in-distribution (ID) and out-of-distribution (OOD) samples are encountered, using an Outlier Contrastive Exposure (OCE) loss to improve OOD detection. Evaluated on 75 datasets spanning diverse distribution shifts, CLIPTTA consistently outperforms entropy-based objectives and is highly competitive with state-of-the-art TTA methods, outperforming them on a large number of datasets and exhibiting more stable performance across diverse shifts.

## 🔍 Abstract (한글 번역)

arXiv:2507.14312v2 발표 유형: 교체  
초록: CLIP과 같은 비전-언어 모델(VLM)은 강력한 제로샷 능력을 보이지만, 분포 변화에 따라 일반화하는 데 실패하는 경우가 많습니다. 테스트 시점 적응(TTA)은 레이블이 없는 데이터로 모델이 추론 시 업데이트할 수 있도록 하며, 일반적으로 엔트로피 최소화를 통해 수행됩니다. 그러나 이 목표는 VLM의 대조 이미지-텍스트 훈련과 근본적으로 맞지 않아 적응 성능을 제한하고, 의사 레이블 드리프트 및 클래스 붕괴와 같은 실패 모드를 초래합니다. 우리는 CLIP의 사전 훈련 목표와 정렬된 부드러운 대조 손실을 활용하는 비전-언어 모델을 위한 새로운 그래디언트 기반 TTA 방법인 CLIPTTA를 제안합니다. CLIPTTA의 그래디언트에 대한 이론적 분석을 제공하며, 배치 인식 설계가 붕괴 위험을 어떻게 완화하는지 보여줍니다. 우리는 또한 CLIPTTA를 개방형 세트 설정으로 확장하여, 분포 내(ID) 및 분포 외(OOD) 샘플이 모두 발생하는 상황에서 OOD 탐지를 개선하기 위해 이상치 대조 노출(OCE) 손실을 사용합니다. 다양한 분포 변화를 아우르는 75개의 데이터셋에서 평가한 결과, CLIPTTA는 일관되게 엔트로피 기반 목표를 능가하며, 최첨단 TTA 방법과 매우 경쟁력이 있으며, 많은 데이터셋에서 그들을 능가하고 다양한 변화에 걸쳐 더 안정적인 성능을 보입니다.

## 📝 요약

이 논문은 CLIP과 같은 비전-언어 모델(VLM)의 테스트 시 적응(TTA) 성능을 개선하기 위한 새로운 방법인 CLIPTTA를 제안합니다. 기존의 엔트로피 최소화 기반 TTA는 VLM의 대조적 이미지-텍스트 훈련과 잘 맞지 않아 적응 성능이 제한되고, 가짜 레이블 이동 및 클래스 붕괴와 같은 문제를 초래합니다. CLIPTTA는 CLIP의 사전 훈련 목표와 정렬된 소프트 대조 손실을 활용하여 이러한 문제를 해결하며, 배치 인식 설계를 통해 붕괴 위험을 완화합니다. 또한, CLIPTTA는 개방형 세트 설정으로 확장되어, ID 및 OOD 샘플을 모두 처리하며, OOD 탐지를 개선하기 위해 Outlier Contrastive Exposure(OCE) 손실을 사용합니다. 75개의 다양한 데이터셋에서 평가한 결과, CLIPTTA는 엔트로피 기반 목표를 일관되게 능가하며, 최신 TTA 방법들과 비교하여 많은 데이터셋에서 더 나은 성능을 보이고 다양한 분포 변화에 대해 더 안정적인 성능을 나타냅니다.

## 🎯 주요 포인트

- 1. Vision-language 모델(VLMs)인 CLIP은 강력한 제로샷 능력을 보이지만, 분포 변화에 대한 일반화에는 실패하는 경우가 많습니다.
- 2. 테스트 시점 적응(TTA)은 레이블이 없는 데이터로 모델을 업데이트할 수 있게 하지만, 기존의 엔트로피 최소화 방식은 VLMs의 대조적 이미지-텍스트 훈련과 근본적으로 맞지 않아 적응 성능을 제한합니다.
- 3. CLIPTTA는 CLIP의 사전 훈련 목표와 정렬된 소프트 대조 손실을 활용하여 VLMs에 대한 새로운 그래디언트 기반 TTA 방법을 제안합니다.
- 4. CLIPTTA는 배치 인식 설계를 통해 클래스 붕괴 위험을 완화하며, ID와 OOD 샘플을 모두 처리할 수 있는 개방형 설정으로 확장됩니다.
- 5. 75개의 다양한 데이터셋에서 평가한 결과, CLIPTTA는 엔트로피 기반 목표보다 일관되게 우수한 성능을 보였으며, 다양한 분포 변화에서도 안정적인 성능을 나타냈습니다.


---

*Generated on 2025-09-23 12:38:45*