---
keywords:
  - Diffusion Transformer
  - Vision-Language Model
  - In-Context Editing
  - Instruction-based Image Editing
  - Early Filter Inference-Time Scaling
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2504.20690
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:21:28.996087",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Diffusion Transformer",
    "Vision-Language Model",
    "In-Context Editing",
    "Instruction-based Image Editing",
    "Early Filter Inference-Time Scaling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Diffusion Transformer": 0.78,
    "Vision-Language Model": 0.81,
    "In-Context Editing": 0.77,
    "Instruction-based Image Editing": 0.75,
    "Early Filter Inference-Time Scaling": 0.74
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Diffusion Transformers",
        "canonical": "Diffusion Transformer",
        "aliases": [
          "DiTs"
        ],
        "category": "unique_technical",
        "rationale": "Diffusion Transformers represent a novel approach within the Transformer architecture, enabling new capabilities in image editing.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are crucial for understanding and generating image content based on textual instructions, linking visual and language modalities.",
        "novelty_score": 0.58,
        "connectivity_score": 0.85,
        "specificity_score": 0.79,
        "link_intent_score": 0.81
      },
      {
        "surface": "In-Context Editing",
        "canonical": "In-Context Editing",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "In-Context Editing is a specific technique that enhances the precision of image modifications without altering the underlying architecture.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Instruction-based Image Editing",
        "canonical": "Instruction-based Image Editing",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's approach, focusing on modifying images through natural language instructions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      },
      {
        "surface": "Early Filter Inference-Time Scaling",
        "canonical": "Early Filter Inference-Time Scaling",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This technique optimizes the efficiency of the editing process by selecting high-quality noise samples, enhancing performance.",
        "novelty_score": 0.72,
        "connectivity_score": 0.6,
        "specificity_score": 0.83,
        "link_intent_score": 0.74
      }
    ],
    "ban_list_suggestions": [
      "fine-tuning",
      "training data"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Diffusion Transformers",
      "resolved_canonical": "Diffusion Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.85,
        "specificity": 0.79,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "In-Context Editing",
      "resolved_canonical": "In-Context Editing",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Instruction-based Image Editing",
      "resolved_canonical": "Instruction-based Image Editing",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Early Filter Inference-Time Scaling",
      "resolved_canonical": "Early Filter Inference-Time Scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.6,
        "specificity": 0.83,
        "link_intent": 0.74
      }
    }
  ]
}
-->

# In-Context Edit: Enabling Instructional Image Editing with In-Context Generation in Large Scale Diffusion Transformer

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2504.20690.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2504.20690](https://arxiv.org/abs/2504.20690)

## 🔗 유사한 논문
- [[2025-09-23/ContextFlow_ Training-Free Video Object Editing via Adaptive Context Enrichment_20250923|ContextFlow: Training-Free Video Object Editing via Adaptive Context Enrichment]] (84.9% similar)
- [[2025-09-18/EdiVal-Agent_ An Object-Centric Framework for Automated, Scalable, Fine-Grained Evaluation of Multi-Turn Editing_20250918|EdiVal-Agent: An Object-Centric Framework for Automated, Scalable, Fine-Grained Evaluation of Multi-Turn Editing]] (84.5% similar)
- [[2025-09-19/TIDE_ Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement_20250919|TIDE: Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement]] (82.6% similar)
- [[2025-09-22/RespoDiff_ Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation_20250922|RespoDiff: Dual-Module Bottleneck Transformation for Responsible & Faithful T2I Generation]] (82.0% similar)
- [[2025-09-23/Optimizing Inference in Transformer-Based Models_ A Multi-Method Benchmark_20250923|Optimizing Inference in Transformer-Based Models: A Multi-Method Benchmark]] (81.7% similar)

## 🏷️ 카테고리화된 키워드
**⚡ Unique Technical**: [[keywords/Diffusion Transformer|Diffusion Transformer]], [[keywords/In-Context Editing|In-Context Editing]], [[keywords/Instruction-based Image Editing|Instruction-based Image Editing]], [[keywords/Early Filter Inference-Time Scaling|Early Filter Inference-Time Scaling]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.20690v2 Announce Type: replace 
Abstract: Instruction-based image editing enables precise modifications via natural language prompts, but existing methods face a precision-efficiency tradeoff: fine-tuning demands massive datasets (>10M) and computational resources, while training-free approaches suffer from weak instruction comprehension. We address this by proposing ICEdit, which leverages the inherent comprehension and generation abilities of large-scale Diffusion Transformers (DiTs) through three key innovations: (1) An in-context editing paradigm without architectural modifications; (2) Minimal parameter-efficient fine-tuning for quality improvement; (3) Early Filter Inference-Time Scaling, which uses VLMs to select high-quality noise samples for efficiency. Experiments show that ICEdit achieves state-of-the-art editing performance with only 0.1\% of the training data and 1\% trainable parameters compared to previous methods. Our approach establishes a new paradigm for balancing precision and efficiency in instructional image editing. Codes and demos can be found in https://river-zhang.github.io/ICEdit-gh-pages/.

## 📝 요약

ICEdit는 자연어 지시를 통해 이미지를 정밀하게 수정하는 방법으로, 기존 방법들이 직면한 정밀도와 효율성 간의 균형 문제를 해결합니다. ICEdit는 대규모 Diffusion Transformers의 이해 및 생성 능력을 활용하여, (1) 아키텍처 수정 없이 맥락 내 편집, (2) 최소한의 파라미터 효율적 미세 조정, (3) VLM을 통한 고품질 노이즈 샘플 선택으로 효율성을 높이는 Early Filter Inference-Time Scaling을 제안합니다. 실험 결과, ICEdit는 기존 방법 대비 0.1%의 훈련 데이터와 1%의 학습 가능한 파라미터만으로 최첨단 편집 성능을 달성했습니다. 이 접근법은 지시 기반 이미지 편집에서 정밀도와 효율성의 균형을 새로운 방식으로 제시합니다.

## 🎯 주요 포인트

- 1. ICEdit는 대규모 Diffusion Transformers(DiTs)의 이해 및 생성 능력을 활용하여 이미지 편집의 정밀도와 효율성 간의 균형을 맞추는 새로운 패러다임을 제시합니다.
- 2. ICEdit는 아키텍처 수정 없이 컨텍스트 내 편집 패러다임을 도입하고, 최소한의 파라미터 효율적 미세 조정을 통해 품질을 개선합니다.
- 3. VLMs를 활용한 Early Filter Inference-Time Scaling을 통해 고품질의 노이즈 샘플을 선택하여 효율성을 높입니다.
- 4. ICEdit는 기존 방법에 비해 0.1%의 훈련 데이터와 1%의 학습 가능한 파라미터만으로 최첨단 편집 성능을 달성합니다.
- 5. ICEdit의 코드와 데모는 https://river-zhang.github.io/ICEdit-gh-pages/에서 확인할 수 있습니다.


---

*Generated on 2025-09-24 05:21:28*