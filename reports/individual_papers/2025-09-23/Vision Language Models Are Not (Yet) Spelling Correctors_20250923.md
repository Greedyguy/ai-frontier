---
keywords:
  - Vision-Language Model
  - Real Visual Correction
  - Multimodal Spelling Correction
  - Joint OCR-Correction Pipeline
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17418
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:25:00.712743",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Real Visual Correction",
    "Multimodal Spelling Correction",
    "Joint OCR-Correction Pipeline"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Real Visual Correction": 0.7,
    "Multimodal Spelling Correction": 0.78,
    "Joint OCR-Correction Pipeline": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's focus and connect well with recent trends in multimodal AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "ReViCo",
        "canonical": "Real Visual Correction",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "ReViCo is a new benchmark introduced in the paper, offering a unique contribution to the field of visual spelling correction.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Multimodal Spelling Correction",
        "canonical": "Multimodal Spelling Correction",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This concept is central to the paper's exploration of correcting spelling errors using multimodal inputs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Joint OCR-Correction pipeline",
        "canonical": "Joint OCR-Correction Pipeline",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The pipeline is a novel approach discussed in the paper, offering insights into integrated OCR and correction processes.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "spelling correction",
      "visual input"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "ReViCo",
      "resolved_canonical": "Real Visual Correction",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Multimodal Spelling Correction",
      "resolved_canonical": "Multimodal Spelling Correction",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Joint OCR-Correction pipeline",
      "resolved_canonical": "Joint OCR-Correction Pipeline",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Vision Language Models Are Not (Yet) Spelling Correctors

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17418.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17418](https://arxiv.org/abs/2509.17418)

## 🔗 유사한 논문
- [[2025-09-22/ViSpec_ Accelerating Vision-Language Models with Vision-Aware Speculative Decoding_20250922|ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding]] (84.6% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (84.5% similar)
- [[2025-09-23/Re-Align_ Aligning Vision Language Models via Retrieval-Augmented Direct Preference Optimization_20250923|Re-Align: Aligning Vision Language Models via Retrieval-Augmented Direct Preference Optimization]] (84.0% similar)
- [[2025-09-19/V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM: Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (83.2% similar)
- [[2025-09-22/Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models_20250922|Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Spelling Correction|Multimodal Spelling Correction]]
**⚡ Unique Technical**: [[keywords/Real Visual Correction|Real Visual Correction]], [[keywords/Joint OCR-Correction Pipeline|Joint OCR-Correction Pipeline]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17418v1 Announce Type: new 
Abstract: Spelling correction from visual input poses unique challenges for vision language models (VLMs), as it requires not only detecting but also correcting textual errors directly within images. We present ReViCo (Real Visual Correction), the first benchmark that systematically evaluates VLMs on real-world visual spelling correction across Chinese and English. ReViCo contains naturally occurring errors collected from real-world image data and supports fine-grained evaluation at both image and token levels. Through comprehensive experiments on representative cascaded (Qwen) and native (InternVL) open-source models, as well as closed-source systems (GPT-4o, Claude), we show that current VLMs fall significantly short of human performance, particularly in correction. To address these limitations, we explore two solution paradigms: a Joint OCR-Correction pipeline and a Background Information enhanced approach, both of which yield consistent performance gains. Our analysis highlights fundamental limitations of existing architectures and provides actionable insights for advancing multimodal spelling correction.

## 📝 요약

이 논문은 시각적 입력에서의 철자 교정을 다루는 비전 언어 모델(VLM)의 도전 과제를 탐구합니다. 이를 위해 중국어와 영어의 실제 시각적 철자 교정을 체계적으로 평가하는 첫 번째 벤치마크인 ReViCo를 제시합니다. ReViCo는 실제 이미지 데이터에서 수집된 자연 발생 오류를 포함하며, 이미지 및 토큰 수준에서 세밀한 평가를 지원합니다. 대표적인 개방형 및 폐쇄형 모델에 대한 실험을 통해 현재 VLM이 인간의 성능에 비해 특히 교정에서 크게 부족함을 보여줍니다. 이를 개선하기 위해 Joint OCR-Correction 파이프라인과 배경 정보 강화 접근법을 탐구하여 일관된 성능 향상을 달성했습니다. 이 연구는 기존 아키텍처의 근본적인 한계를 강조하고 다중 모달 철자 교정을 발전시키기 위한 실행 가능한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. ReViCo는 중국어와 영어에서 실제 시각적 맞춤법 교정을 체계적으로 평가하는 최초의 벤치마크입니다.
- 2. ReViCo는 실제 이미지 데이터에서 수집된 자연 발생 오류를 포함하며, 이미지 및 토큰 수준에서 세밀한 평가를 지원합니다.
- 3. 현재의 비전 언어 모델(VLM)은 특히 교정 작업에서 인간의 성능에 크게 미치지 못합니다.
- 4. Joint OCR-Correction 파이프라인과 배경 정보 강화 접근법을 통해 성능 향상을 달성할 수 있습니다.
- 5. 기존 아키텍처의 근본적인 한계를 분석하고 다중 모달 맞춤법 교정을 발전시키기 위한 실행 가능한 통찰을 제공합니다.


---

*Generated on 2025-09-24 03:25:00*