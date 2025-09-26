---
keywords:
  - Large Language Model
  - Vision-Language Model
  - ROME Benchmark
  - Multimodal Reasoning
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17177
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:20:26.774785",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Vision-Language Model",
    "ROME Benchmark",
    "Multimodal Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.78,
    "Vision-Language Model": 0.82,
    "ROME Benchmark": 0.7,
    "Multimodal Reasoning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Reasoning Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LRM"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the broader category of models capable of advanced reasoning, linking with existing large language model concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM"
        ],
        "category": "evolved_concepts",
        "rationale": "Represents an evolved concept in AI that integrates vision and language, facilitating cross-modal reasoning.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "ROME",
        "canonical": "ROME Benchmark",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A unique benchmark specifically designed for evaluating reasoning in vision-language models.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Reasoning from Visual Clues",
        "canonical": "Multimodal Reasoning",
        "aliases": [
          "Visual Reasoning"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the ability to reason across different modalities, crucial for linking vision and language processing.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "evaluation",
      "preliminary findings",
      "contamination-free"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Reasoning Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "ROME",
      "resolved_canonical": "ROME Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Reasoning from Visual Clues",
      "resolved_canonical": "Multimodal Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# FlagEval Findings Report: A Preliminary Evaluation of Large Reasoning Models on Automatically Verifiable Textual and Visual Questions

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17177.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17177](https://arxiv.org/abs/2509.17177)

## 🔗 유사한 논문
- [[2025-09-22/DivLogicEval_ A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models_20250922|DivLogicEval: A Framework for Benchmarking Logical Reasoning Evaluation in Large Language Models]] (84.6% similar)
- [[2025-09-19/Understanding the Thinking Process of Reasoning Models_ A Perspective from Schoenfeld's Episode Theory_20250919|Understanding the Thinking Process of Reasoning Models: A Perspective from Schoenfeld's Episode Theory]] (83.9% similar)
- [[2025-09-23/ProReason_ Multi-Modal Proactive Reasoning with Decoupled Eyesight and Wisdom_20250923|ProReason: Multi-Modal Proactive Reasoning with Decoupled Eyesight and Wisdom]] (83.9% similar)
- [[2025-09-22/GRE Suite_ Geo-localization Inference via Fine-Tuned Vision-Language Models and Enhanced Reasoning Chains_20250922|GRE Suite: Geo-localization Inference via Fine-Tuned Vision-Language Models and Enhanced Reasoning Chains]] (83.8% similar)
- [[2025-09-23/Reasoning Core_ A Scalable RL Environment for LLM Symbolic Reasoning_20250923|Reasoning Core: A Scalable RL Environment for LLM Symbolic Reasoning]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multimodal Reasoning|Multimodal Reasoning]]
**⚡ Unique Technical**: [[keywords/ROME Benchmark|ROME Benchmark]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17177v1 Announce Type: cross 
Abstract: We conduct a moderate-scale contamination-free (to some extent) evaluation of current large reasoning models (LRMs) with some preliminary findings. We also release ROME, our evaluation benchmark for vision language models intended to test reasoning from visual clues. We attach links to the benchmark, evaluation data, and other updates on this website: https://flageval-baai.github.io/LRM-Eval/

## 📝 요약

이 논문은 현재 대규모 추론 모델(LRMs)의 오염 없는 평가를 수행하고, 초기 결과를 제시합니다. 또한, 시각적 단서를 통한 추론을 테스트하기 위한 비전 언어 모델 평가 벤치마크인 ROME을 공개합니다. 벤치마크, 평가 데이터 및 기타 업데이트는 제공된 웹사이트에서 확인할 수 있습니다. 주요 기여는 LRMs의 성능을 체계적으로 평가하고, 시각적 추론 능력을 검증할 수 있는 도구를 제공한 것입니다.

## 🎯 주요 포인트

- 1. 현재 대규모 추론 모델(LRMs)의 중간 규모 오염 없는 평가를 수행했습니다.
- 2. 시각적 단서로부터의 추론을 테스트하기 위한 비전 언어 모델 평가 벤치마크인 ROME을 공개했습니다.
- 3. 벤치마크, 평가 데이터 및 기타 업데이트에 대한 링크를 제공했습니다.


---

*Generated on 2025-09-24 02:20:26*