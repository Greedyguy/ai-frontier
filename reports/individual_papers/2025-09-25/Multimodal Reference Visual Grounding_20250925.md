---
keywords:
  - Multimodal Reference Visual Grounding
  - Vision-Language Model
  - Few-Shot Learning
  - Large Language Model
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2504.02876
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:38:13.302995",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Reference Visual Grounding",
    "Vision-Language Model",
    "Few-Shot Learning",
    "Large Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Reference Visual Grounding": 0.88,
    "Vision-Language Model": 0.8,
    "Few-Shot Learning": 0.82,
    "Large Language Model": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Reference Visual Grounding",
        "canonical": "Multimodal Reference Visual Grounding",
        "aliases": [
          "MRVG"
        ],
        "category": "unique_technical",
        "rationale": "This is a newly introduced task that combines multimodal learning and visual grounding, making it a unique technical concept.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.88
      },
      {
        "surface": "Large Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "LVLM",
          "Vision-Language Models"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's methodology and are a trending concept in AI research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Few-Shot Object Detection",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-Shot Detection"
        ],
        "category": "specific_connectable",
        "rationale": "Few-Shot Learning is crucial for the proposed method and connects to broader machine learning strategies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are used for object matching, linking to a broad technical category.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "dataset",
      "method",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Reference Visual Grounding",
      "resolved_canonical": "Multimodal Reference Visual Grounding",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Large Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Few-Shot Object Detection",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Multimodal Reference Visual Grounding

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2504.02876.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2504.02876](https://arxiv.org/abs/2504.02876)

## 🔗 유사한 논문
- [[2025-09-22/Zero-Shot Visual Grounding in 3D Gaussians via View Retrieval_20250922|Zero-Shot Visual Grounding in 3D Gaussians via View Retrieval]] (85.3% similar)
- [[2025-09-18/Improving Generalized Visual Grounding with Instance-aware Joint Learning_20250918|Improving Generalized Visual Grounding with Instance-aware Joint Learning]] (84.8% similar)
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets]] (84.6% similar)
- [[2025-09-25/Towards Visual Text Grounding of Multimodal Large Language Model_20250925|Towards Visual Text Grounding of Multimodal Large Language Model]] (84.3% similar)
- [[2025-09-24/RSVG-ZeroOV_ Exploring a Training-Free Framework for Zero-Shot Open-Vocabulary Visual Grounding in Remote Sensing Images_20250924|RSVG-ZeroOV: Exploring a Training-Free Framework for Zero-Shot Open-Vocabulary Visual Grounding in Remote Sensing Images]] (83.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Multimodal Reference Visual Grounding|Multimodal Reference Visual Grounding]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.02876v2 Announce Type: replace-cross 
Abstract: Visual grounding focuses on detecting objects from images based on language expressions. Recent Large Vision-Language Models (LVLMs) have significantly advanced visual grounding performance by training large models with large-scale datasets. However, the problem remains challenging, especially when similar objects appear in the input image. For example, an LVLM may not be able to differentiate Diet Coke and regular Coke in an image. In this case, if additional reference images of Diet Coke and regular Coke are available, it can help the visual grounding of similar objects.
  In this work, we introduce a new task named Multimodal Reference Visual Grounding (MRVG). In this task, a model has access to a set of reference images of objects in a database. Based on these reference images and a language expression, the model is required to detect a target object from a query image. We first introduce a new dataset to study the MRVG problem. Then we introduce a novel method, named MRVG-Net, to solve this visual grounding problem. We show that by efficiently using reference images with few-shot object detection and using Large Language Models (LLMs) for object matching, our method achieves superior visual grounding performance compared to the state-of-the-art LVLMs such as Qwen2.5-VL-72B. Our approach bridges the gap between few-shot detection and visual grounding, unlocking new capabilities for visual understanding, which has wide applications in robotics. Project page with our video, code, and dataset: https://irvlutd.github.io/MultiGrounding

## 📝 요약

이 논문은 유사한 객체가 포함된 이미지에서 언어 표현을 기반으로 객체를 식별하는 '멀티모달 참조 시각적 그라운딩(MRVG)'이라는 새로운 과제를 소개합니다. MRVG는 데이터베이스의 참조 이미지를 활용하여 목표 객체를 식별하는 작업입니다. 이를 위해 새로운 데이터셋과 MRVG-Net이라는 방법론을 제안하였으며, 참조 이미지를 활용한 소수 샷 객체 탐지와 대형 언어 모델(LLM)을 통한 객체 매칭을 통해 기존의 대형 비전-언어 모델(LVLM)보다 우수한 성능을 보였습니다. 이 접근법은 로봇공학 등 다양한 분야에 응용될 수 있는 시각적 이해의 새로운 가능성을 열었습니다.

## 🎯 주요 포인트

- 1. 본 연구는 유사한 객체가 등장하는 이미지에서 시각적 그라운딩 문제를 해결하기 위해 새로운 작업인 다중 모달 참조 시각적 그라운딩(MRVG)을 소개합니다.
- 2. MRVG 작업에서는 데이터베이스에 있는 객체의 참조 이미지를 활용하여 쿼리 이미지에서 목표 객체를 탐지해야 합니다.
- 3. MRVG-Net이라는 새로운 방법을 제안하여, 소수 샷 객체 탐지와 대형 언어 모델(LLM)을 활용한 객체 매칭을 통해 시각적 그라운딩 성능을 향상시켰습니다.
- 4. 제안된 방법은 최첨단 대형 비전-언어 모델(LVLM)보다 우수한 성능을 보이며, 로봇 공학 등 다양한 분야에서의 시각적 이해 능력을 확장합니다.
- 5. 연구 결과와 관련된 비디오, 코드, 데이터셋은 프로젝트 페이지(https://irvlutd.github.io/MultiGrounding)에서 확인할 수 있습니다.


---

*Generated on 2025-09-26 08:38:13*