---
keywords:
  - Contrastive Masked Text-Image Pretraining
  - Spatial Transcriptomics
  - Zero-Shot Learning
  - Masked Feature Modeling
  - Gene-Text Encoder
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16892
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:37:07.548640",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Contrastive Masked Text-Image Pretraining",
    "Spatial Transcriptomics",
    "Zero-Shot Learning",
    "Masked Feature Modeling",
    "Gene-Text Encoder"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Contrastive Masked Text-Image Pretraining": 0.78,
    "Spatial Transcriptomics": 0.82,
    "Zero-Shot Learning": 0.75,
    "Masked Feature Modeling": 0.72,
    "Gene-Text Encoder": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Contrastive Masked Text-Image Pretraining",
        "canonical": "Contrastive Masked Text-Image Pretraining",
        "aliases": [
          "CoMTIP"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel framework specific to the paper, integrating text and image modalities in spatial transcriptomics.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Spatial Transcriptomics",
        "canonical": "Spatial Transcriptomics",
        "aliases": [
          "Spatial Gene Expression"
        ],
        "category": "specific_connectable",
        "rationale": "Central to the paper's focus, linking gene expression with spatial data in transcriptomics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Zero-Shot Gene Expression Prediction",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot Prediction"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights a key capability of the proposed method, connecting it to broader zero-shot learning concepts.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Masked Feature Modeling",
        "canonical": "Masked Feature Modeling",
        "aliases": [
          "Feature Masking"
        ],
        "category": "unique_technical",
        "rationale": "A specific technique used in the vision branch of the framework, crucial for context-aware learning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      },
      {
        "surface": "Gene-Text Encoder",
        "canonical": "Gene-Text Encoder",
        "aliases": [
          "Gene Encoder"
        ],
        "category": "unique_technical",
        "rationale": "A novel component of the framework that processes gene sentences, enhancing connectivity in gene expression studies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "pre-training",
      "downstream tasks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Contrastive Masked Text-Image Pretraining",
      "resolved_canonical": "Contrastive Masked Text-Image Pretraining",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Spatial Transcriptomics",
      "resolved_canonical": "Spatial Transcriptomics",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Zero-Shot Gene Expression Prediction",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Masked Feature Modeling",
      "resolved_canonical": "Masked Feature Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Gene-Text Encoder",
      "resolved_canonical": "Gene-Text Encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Learning from Gene Names, Expression Values and Images: Contrastive Masked Text-Image Pretraining for Spatial Transcriptomics Representation Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16892.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16892](https://arxiv.org/abs/2509.16892)

## 🔗 유사한 논문
- [[2025-09-22/RegionMed-CLIP_ A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding_20250922|RegionMed-CLIP: A Region-Aware Multimodal Contrastive Learning Pre-trained Model for Medical Image Understanding]] (82.9% similar)
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (82.5% similar)
- [[2025-09-22/Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays_20250922|Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays]] (80.5% similar)
- [[2025-09-22/AcT2I_ Evaluating and Improving Action Depiction in Text-to-Image Models_20250922|AcT2I: Evaluating and Improving Action Depiction in Text-to-Image Models]] (80.0% similar)
- [[2025-09-22/CLIPTTA_ Robust Contrastive Vision-Language Test-Time Adaptation_20250922|CLIPTTA: Robust Contrastive Vision-Language Test-Time Adaptation]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Spatial Transcriptomics|Spatial Transcriptomics]], [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Contrastive Masked Text-Image Pretraining|Contrastive Masked Text-Image Pretraining]], [[keywords/Masked Feature Modeling|Masked Feature Modeling]], [[keywords/Gene-Text Encoder|Gene-Text Encoder]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16892v1 Announce Type: cross 
Abstract: Spatial transcriptomics aims to connect high-resolution histology images with spatially resolved gene expression. To achieve better performance on downstream tasks such as gene expression prediction, large-scale pre-training is required to obtain generalisable representations that can bridge histology and transcriptomics across tissues, protocols, and laboratories. Existing cross-modal pre-training approaches for spatial transcriptomics rely on either gene names or expression values in isolation, which strips the gene branch of essential semantics and breaks the association between each gene and its quantitative magnitude. In addition, by restricting supervision to image-text alignment, these methods ignore intrinsic visual cues that are critical for learning robust image features. We present CoMTIP, the first Contrastive Masked Text-Image Pretraining framework that jointly learns from images, gene names, and expression values while capturing fine-grained visual context for spatial transcriptomics. The vision branch uses Masked Feature Modeling to reconstruct occluded patches and learn context-aware image embeddings. The text branch applies a scalable Gene-Text Encoder that processes all gene sentences in parallel, enriches each gene and its numerical value with dedicated embeddings, and employs Pair-aware Adversarial Training (PAAT) to preserve correct gene-value associations. Image and text representations are aligned in a shared InfoNCE-optimised space. Experiments on public spatial transcriptomics datasets show that CoMTIP not only surpasses previous methods on diverse downstream tasks but also achieves zero-shot gene expression prediction, a capability that existing approaches do not provide.

## 📝 요약

이 논문은 공간 전사체학(spatial transcriptomics)에서 고해상도 조직 이미지를 공간적으로 해상된 유전자 발현과 연결하는 방법을 제안합니다. 기존의 방법들은 유전자 이름이나 발현 값만을 사용하여 유전자와 그 양적 크기 간의 연관성을 약화시켰습니다. 또한 이미지-텍스트 정렬에만 초점을 맞춰 중요한 시각적 단서를 무시했습니다. 이를 해결하기 위해, CoMTIP라는 대조적 마스킹 텍스트-이미지 사전 학습 프레임워크를 제안합니다. 이 방법은 이미지, 유전자 이름, 발현 값을 함께 학습하여 세밀한 시각적 맥락을 포착합니다. 이미지 부분은 마스킹된 특징 모델링을 사용하여 맥락을 인식하는 이미지 임베딩을 학습하고, 텍스트 부분은 확장 가능한 유전자-텍스트 인코더를 사용하여 유전자와 그 수치 값을 강화합니다. 실험 결과, CoMTIP는 다양한 다운스트림 작업에서 기존 방법을 능가하며, 제로샷 유전자 발현 예측도 가능하게 합니다.

## 🎯 주요 포인트

- 1. CoMTIP는 이미지, 유전자 이름, 발현 값을 함께 학습하여 공간 전사체학을 위한 세밀한 시각적 맥락을 포착합니다.
- 2. 비전 브랜치는 마스크드 피처 모델링을 사용하여 가려진 패치를 복원하고 맥락 인식 이미지 임베딩을 학습합니다.
- 3. 텍스트 브랜치는 모든 유전자 문장을 병렬로 처리하고, 각 유전자와 그 수치 값을 전용 임베딩으로 풍부하게 하며, PAAT를 통해 올바른 유전자-값 연관성을 유지합니다.
- 4. 이미지와 텍스트 표현은 공유된 InfoNCE 최적화 공간에서 정렬됩니다.
- 5. CoMTIP는 다양한 다운스트림 작업에서 기존 방법을 능가할 뿐만 아니라 기존 접근 방식이 제공하지 않는 제로샷 유전자 발현 예측도 달성합니다.


---

*Generated on 2025-09-23 23:37:07*