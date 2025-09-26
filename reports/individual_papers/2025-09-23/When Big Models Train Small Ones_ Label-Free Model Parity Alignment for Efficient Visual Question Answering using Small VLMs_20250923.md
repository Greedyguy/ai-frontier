---
keywords:
  - Vision-Language Model
  - Model Parity Aligner
  - Knowledge Transfer
  - Visual Question Answering
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16633
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:29:22.292991",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Model Parity Aligner",
    "Knowledge Transfer",
    "Visual Question Answering"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Model Parity Aligner": 0.78,
    "Knowledge Transfer": 0.8,
    "Visual Question Answering": 0.82
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
        "rationale": "This concept is central to the paper and connects to the broader field of multimodal learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Model Parity Aligner",
        "canonical": "Model Parity Aligner",
        "aliases": [
          "MPA"
        ],
        "category": "unique_technical",
        "rationale": "A novel framework introduced in the paper, crucial for understanding the proposed method.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Knowledge Transfer",
        "canonical": "Knowledge Transfer",
        "aliases": [
          "Transfer Learning"
        ],
        "category": "specific_connectable",
        "rationale": "A key process in the paper, linking it to broader machine learning techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.82,
        "specificity_score": 0.68,
        "link_intent_score": 0.8
      },
      {
        "surface": "Visual Question Answering",
        "canonical": "Visual Question Answering",
        "aliases": [
          "VQA"
        ],
        "category": "specific_connectable",
        "rationale": "The primary application domain of the study, providing context for the research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "efficiency",
      "performance gap"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Model Parity Aligner",
      "resolved_canonical": "Model Parity Aligner",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Knowledge Transfer",
      "resolved_canonical": "Knowledge Transfer",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.82,
        "specificity": 0.68,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Visual Question Answering",
      "resolved_canonical": "Visual Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# When Big Models Train Small Ones: Label-Free Model Parity Alignment for Efficient Visual Question Answering using Small VLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16633.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16633](https://arxiv.org/abs/2509.16633)

## 🔗 유사한 논문
- [[2025-09-19/V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM: Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (85.3% similar)
- [[2025-09-22/VLA-Mark_ A cross modal watermark for large vision-language alignment model_20250922|VLA-Mark: A cross modal watermark for large vision-language alignment model]] (85.1% similar)
- [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (85.0% similar)
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (84.6% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (84.4% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Knowledge Transfer|Knowledge Transfer]], [[keywords/Visual Question Answering|Visual Question Answering]]
**⚡ Unique Technical**: [[keywords/Model Parity Aligner|Model Parity Aligner]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16633v1 Announce Type: cross 
Abstract: Large Vision-Language Models (L-VLMs) have demonstrated remarkable performance in various vision and language tasks, including visual question answering (VQA). However, their high computational cost makes them impractical for resource-constrained settings and inference-heavy applications. In contrast, Small Vision-Language Models (S-VLMs) offer efficiency but suffer from a significant performance gap compared to their larger counterparts. In this work, we introduce the Model Parity Aligner (MPA), a novel framework designed to systematically improve S-VLMs by leveraging unlabeled images and effective knowledge transfer from L-VLMs. Instead of traditional knowledge distillation methods that rely on labeled training data, MPA employs a strategic parity-based approach that precisely identifies the knowledge disparities between S-VLMs and L-VLMs, and optimizes training by targeting only these disparities. We conduct extensive experiments on four diverse VQA benchmarks, namely TextVQA, ST-VQA, ChartQA, and OKVQA, each of which requires specialized reasoning capabilities such as text recognition, chart interpretation, and commonsense and factual understanding. Our results demonstrate that MPA consistently enhances the performance of S-VLMs on all benchmarks, reducing the performance gap while maintaining computational efficiency. We make our code publicly available.

## 📝 요약

이 논문은 소형 비전-언어 모델(S-VLM)의 성능을 개선하기 위한 새로운 프레임워크인 모델 패리티 얼라이너(MPA)를 소개합니다. 기존의 지식 증류 방법이 레이블이 있는 데이터를 필요로 하는 반면, MPA는 레이블이 없는 이미지를 활용하여 대형 비전-언어 모델(L-VLM)과의 지식 격차를 식별하고 이를 목표로 최적화합니다. 이를 통해 S-VLM의 성능을 향상시키면서도 계산 효율성을 유지합니다. 연구는 TextVQA, ST-VQA, ChartQA, OKVQA 등 다양한 VQA 벤치마크에서 실험을 진행하였으며, MPA가 모든 벤치마크에서 S-VLM의 성능을 일관되게 향상시킴을 입증했습니다. 코드도 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 대형 비전-언어 모델(L-VLMs)은 뛰어난 성능을 보이지만, 높은 계산 비용으로 인해 자원이 제한된 환경에서는 비효율적입니다.
- 2. 소형 비전-언어 모델(S-VLMs)은 효율적이지만, 성능 면에서 L-VLMs와 큰 차이를 보입니다.
- 3. 본 연구에서는 MPA(Model Parity Aligner)라는 새로운 프레임워크를 제안하여, 라벨이 없는 이미지와 L-VLMs의 효과적인 지식 전이를 활용해 S-VLMs의 성능을 체계적으로 개선합니다.
- 4. MPA는 전통적인 지식 증류 방법 대신, S-VLMs와 L-VLMs 간의 지식 격차를 정확히 식별하고 이를 목표로 최적화하여 성능을 향상시킵니다.
- 5. 다양한 VQA 벤치마크 실험 결과, MPA는 S-VLMs의 성능을 일관되게 향상시키면서도 계산 효율성을 유지합니다.


---

*Generated on 2025-09-23 23:29:22*