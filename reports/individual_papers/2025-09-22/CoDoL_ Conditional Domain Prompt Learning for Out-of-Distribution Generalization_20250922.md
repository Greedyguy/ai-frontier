---
keywords:
  - Vision-Language Model
  - Out-of-Distribution Generalization
  - Conditional Domain Prompt Learning
  - Zero-Shot Learning
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15330
---


<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:55:49.396447",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Out-of-Distribution Generalization",
    "Conditional Domain Prompt Learning",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Out-of-Distribution Generalization": 0.8,
    "Conditional Domain Prompt Learning": 0.78,
    "Zero-Shot Learning": 0.77
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
        "rationale": "Vision-Language Models are central to the paper's focus on improving OOD generalization and embedding alignment.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Out-of-Distribution Generalization",
        "canonical": "Out-of-Distribution Generalization",
        "aliases": [
          "OOD Generalization"
        ],
        "category": "unique_technical",
        "rationale": "The paper introduces a method specifically aimed at enhancing OOD generalization, making it a unique technical focus.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Conditional Domain Prompt Learning",
        "canonical": "Conditional Domain Prompt Learning",
        "aliases": [
          "CoDoL"
        ],
        "category": "unique_technical",
        "rationale": "CoDoL is the novel method proposed in the paper, directly addressing the challenges with prompt-based methods.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Zero-Shot Learning",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is a key challenge addressed by the proposed method, relevant for linking with related research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
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
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Out-of-Distribution Generalization",
      "resolved_canonical": "Out-of-Distribution Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Conditional Domain Prompt Learning",
      "resolved_canonical": "Conditional Domain Prompt Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Zero-Shot Learning",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# CoDoL: Conditional Domain Prompt Learning for Out-of-Distribution Generalization

**Korean Title:** CoDoL: 분포 외 일반화를 위한 조건부 도메인 프롬프트 학습

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15330.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15330](https://arxiv.org/abs/2509.15330)

## 🔗 유사한 논문
- [[2025-09-22/Advances in Multimodal Adaptation and Generalization_ From Traditional Approaches to Foundation Models_20250922|Advances in Multimodal Adaptation and Generalization: From Traditional Approaches to Foundation Models]] (83.6% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (82.5% similar)
- [[2025-09-22/Towards Robust Visual Continual Learning with Multi-Prototype Supervision_20250922|Towards Robust Visual Continual Learning with Multi-Prototype Supervision]] (81.6% similar)
- [[2025-09-22/Two Facets of the Same Optimization Coin_ Model Degradation and Representation Collapse in Graph Foundation Models_20250922|Two Facets of the Same Optimization Coin: Model Degradation and Representation Collapse in Graph Foundation Models]] (81.5% similar)
- [[2025-09-19/An Empirical Study of Federated Prompt Learning for Vision Language Model_20250919|An Empirical Study of Federated Prompt Learning for Vision Language Model]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Out-of-Distribution Generalization|Out-of-Distribution Generalization]], [[keywords/Conditional Domain Prompt Learning|Conditional Domain Prompt Learning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15330v1 Announce Type: new 
Abstract: Recent advances in pre-training vision-language models (VLMs), e.g., contrastive language-image pre-training (CLIP) methods, have shown great potential in learning out-of-distribution (OOD) representations. Despite showing competitive performance, the prompt-based CLIP methods still suffer from: i) inaccurate text descriptions, which leads to degraded accuracy and robustness, and poses a challenge for zero-shot CLIP methods. ii) limited vision-language embedding alignment, which significantly affects the generalization performance. To tackle the above issues, this paper proposes a novel Conditional Domain prompt Learning (CoDoL) method, which utilizes readily-available domain information to form prompts and improves the vision-language embedding alignment for improving OOD generalization. To capture both instance-specific and domain-specific information, we further propose a lightweight Domain Meta Network (DMN) to generate input-conditional tokens for images in each domain. Extensive experiments on four OOD benchmarks (PACS, VLCS, OfficeHome and DigitDG) validate the effectiveness of our proposed CoDoL in terms of improving the vision-language embedding alignment as well as the out-of-distribution generalization performance.

## 🔍 Abstract (한글 번역)

arXiv:2509.15330v1 발표 유형: 신규  
초록: 최근의 비전-언어 모델(VLMs) 사전 학습, 예를 들어 대조적 언어-이미지 사전 학습(CLIP) 방법은 분포 외(OOD) 표현 학습에 큰 잠재력을 보여주고 있습니다. 경쟁력 있는 성능을 보임에도 불구하고, 프롬프트 기반 CLIP 방법은 여전히 다음과 같은 문제를 겪고 있습니다: i) 부정확한 텍스트 설명으로 인해 정확성과 강건성이 저하되며, 이는 제로샷 CLIP 방법에 도전 과제를 제시합니다. ii) 제한된 비전-언어 임베딩 정렬로 인해 일반화 성능에 큰 영향을 미칩니다. 이러한 문제를 해결하기 위해, 본 논문은 조건부 도메인 프롬프트 학습(CoDoL)이라는 새로운 방법을 제안합니다. 이 방법은 쉽게 이용 가능한 도메인 정보를 사용하여 프롬프트를 형성하고, 비전-언어 임베딩 정렬을 개선하여 OOD 일반화를 향상시킵니다. 인스턴스별 및 도메인별 정보를 모두 포착하기 위해, 우리는 각 도메인 내 이미지에 대해 입력 조건부 토큰을 생성하는 경량 도메인 메타 네트워크(DMN)를 추가로 제안합니다. 네 가지 OOD 벤치마크(PACS, VLCS, OfficeHome 및 DigitDG)에 대한 광범위한 실험은 비전-언어 임베딩 정렬 개선과 분포 외 일반화 성능 향상 측면에서 제안된 CoDoL의 효과를 검증합니다.

## 📝 요약

최근 비전-언어 모델(VLM)의 사전 학습, 특히 CLIP 방법은 분포 외(OOD) 표현 학습에서 큰 잠재력을 보였습니다. 그러나 프롬프트 기반 CLIP 방법은 부정확한 텍스트 설명과 제한된 비전-언어 임베딩 정렬로 인해 정확성과 일반화 성능이 저하됩니다. 이를 해결하기 위해 본 논문은 조건부 도메인 프롬프트 학습(CoDoL) 방법을 제안합니다. CoDoL은 도메인 정보를 활용하여 프롬프트를 형성하고 비전-언어 임베딩 정렬을 개선하여 OOD 일반화를 향상시킵니다. 또한, 도메인 메타 네트워크(DMN)를 통해 각 도메인 내 이미지에 대한 입력 조건 토큰을 생성하여 인스턴스 및 도메인별 정보를 포착합니다. 네 가지 OOD 벤치마크(PACS, VLCS, OfficeHome, DigitDG)에서의 실험을 통해 CoDoL의 효과가 입증되었습니다.

## 🎯 주요 포인트

- 1. 최근의 대비 언어-이미지 사전 학습(CLIP) 방법은 분포 밖(OOD) 표현 학습에서 큰 잠재력을 보여주고 있다.
- 2. 기존의 CLIP 방법은 부정확한 텍스트 설명과 제한된 비전-언어 임베딩 정렬 문제로 인해 정확성과 일반화 성능이 저하된다.
- 3. 본 논문에서는 조건부 도메인 프롬프트 학습(CoDoL) 방법을 제안하여 OOD 일반화 성능을 개선하고자 한다.
- 4. CoDoL은 도메인 정보를 활용하여 프롬프트를 형성하고, 비전-언어 임베딩 정렬을 개선한다.
- 5. 제안된 방법은 PACS, VLCS, OfficeHome, DigitDG 등 네 가지 OOD 벤치마크에서 효과성을 입증하였다.


---

*Generated on 2025-09-23 11:55:49*