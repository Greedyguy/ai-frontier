---
keywords:
  - Vision-Language Model
  - Discourse-level Scene Graph Parsing
  - Graph Refinement
  - SPICE Metric
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2506.15583
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:06:03.731253",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Discourse-level Scene Graph Parsing",
    "Graph Refinement",
    "SPICE Metric"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Discourse-level Scene Graph Parsing": 0.82,
    "Graph Refinement": 0.78,
    "SPICE Metric": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's focus on discourse-level parsing, linking it to multimodal learning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Discourse-level text Scene Graph parsing",
        "canonical": "Discourse-level Scene Graph Parsing",
        "aliases": [
          "DiscoSG"
        ],
        "category": "unique_technical",
        "rationale": "This new task is the core contribution of the paper, offering a unique perspective on scene graph parsing.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Graph Refinement",
        "canonical": "Graph Refinement",
        "aliases": [
          "Iterative Graph Refinement"
        ],
        "category": "specific_connectable",
        "rationale": "Graph refinement is a key process in improving the robustness of scene graph parsing, linking to iterative improvement techniques.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "SPICE",
        "canonical": "SPICE Metric",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "SPICE is a specific evaluation metric used to measure the performance of the proposed models, crucial for understanding improvements.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "task"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Discourse-level text Scene Graph parsing",
      "resolved_canonical": "Discourse-level Scene Graph Parsing",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Graph Refinement",
      "resolved_canonical": "Graph Refinement",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "SPICE",
      "resolved_canonical": "SPICE Metric",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# DiscoSG: Towards Discourse-Level Text Scene Graph Parsing through Iterative Graph Refinement

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.15583.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2506.15583](https://arxiv.org/abs/2506.15583)

## 🔗 유사한 논문
- [[2025-09-22/Vision-Language Models as Differentiable Semantic and Spatial Rewards for Text-to-3D Generation_20250922|Vision-Language Models as Differentiable Semantic and Spatial Rewards for Text-to-3D Generation]] (84.4% similar)
- [[2025-09-23/SD-VLM_ Spatial Measuring and Understanding with Depth-Encoded Vision-Language Models_20250923|SD-VLM: Spatial Measuring and Understanding with Depth-Encoded Vision-Language Models]] (82.6% similar)
- [[2025-09-23/DISCO_ Disentangled Communication Steering for Large Language Models_20250923|DISCO: Disentangled Communication Steering for Large Language Models]] (82.6% similar)
- [[2025-09-22/ViSpec_ Accelerating Vision-Language Models with Vision-Aware Speculative Decoding_20250922|ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative Decoding]] (82.4% similar)
- [[2025-09-23/SpecVLM_ Fast Speculative Decoding in Vision-Language Models_20250923|SpecVLM: Fast Speculative Decoding in Vision-Language Models]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Graph Refinement|Graph Refinement]]
**⚡ Unique Technical**: [[keywords/Discourse-level Scene Graph Parsing|Discourse-level Scene Graph Parsing]], [[keywords/SPICE Metric|SPICE Metric]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.15583v2 Announce Type: replace 
Abstract: Vision-Language Models (VLMs) generate discourse-level, multi-sentence visual descriptions, challenging text scene graph parsers built for single-sentence caption-to-graph mapping. Current approaches typically merge sentence-level parsing outputs for discourse input, often missing phenomena like cross-sentence coreference, resulting in fragmented graphs and degraded downstream VLM task performance. We introduce a new task, Discourse-level text Scene Graph parsing (DiscoSG), and release DiscoSG-DS, a dataset of 400 expert-annotated and 8,430 synthesised multi-sentence caption-graph pairs. Each caption averages 9 sentences, and each graph contains at least 3 times more triples than those in existing datasets.
  Fine-tuning GPT-4o on DiscoSG-DS yields over 40% higher SPICE than the strongest sentence-merging baseline. However, its high inference cost and licensing restrict open-source use, and smaller fine-tuned open-source models (e.g., Flan-T5) perform poorly on dense graph generation. To bridge this gap, we propose DiscoSG-Refiner, which drafts a base graph using a seed parser and iteratively refines it with a second model, improving robustness for complex graph generation. Using two small fine-tuned Flan-T5-Base models, DiscoSG-Refiner improves SPICE by approximately 30% over the baseline while achieving 86 times faster inference than GPT-4o. It also delivers consistent gains on downstream VLM tasks, including discourse-level caption evaluation and hallucination detection, outperforming alternative parsers. Code and data are available at https://github.com/ShaoqLin/DiscoSG .

## 📝 요약

이 논문은 비전-언어 모델(VLM)이 생성하는 다중 문장 시각 설명을 보다 효과적으로 처리하기 위해 새로운 과제인 담화 수준의 텍스트 장면 그래프 파싱(DiscoSG)을 제안합니다. 이를 위해 400개의 전문가 주석과 8,430개의 합성된 다중 문장 캡션-그래프 쌍으로 구성된 데이터셋 DiscoSG-DS를 공개했습니다. DiscoSG-Refiner라는 새로운 방법론을 도입하여, 초기 그래프를 생성한 후 두 번째 모델로 이를 반복적으로 개선하여 복잡한 그래프 생성의 강건성을 높였습니다. 이 방법은 두 개의 소형 Flan-T5-Base 모델을 사용하여 기존의 문장 병합 기법보다 약 30% 높은 SPICE 점수를 기록하며, GPT-4o보다 86배 빠른 추론 속도를 자랑합니다. 또한, 담화 수준의 캡션 평가와 환각 탐지와 같은 VLM 과제에서도 일관된 성능 향상을 보여줍니다. 코드와 데이터는 GitHub에서 제공됩니다.

## 🎯 주요 포인트

- 1. Vision-Language Models (VLMs)는 단일 문장 기반의 텍스트 장면 그래프 파서를 넘어서는 담화 수준의 다중 문장 시각적 설명을 생성합니다.
- 2. 기존 방법은 문장 수준의 파싱 출력을 병합하여 담화 입력을 처리하지만, 문장 간 상호 참조와 같은 현상을 놓쳐 단편적인 그래프를 생성합니다.
- 3. 새로운 과제인 담화 수준 텍스트 장면 그래프 파싱(DiscoSG)을 소개하고, 400개의 전문가 주석 및 8,430개의 합성된 다중 문장 캡션-그래프 쌍으로 구성된 DiscoSG-DS 데이터셋을 공개합니다.
- 4. DiscoSG-Refiner는 시드 파서를 사용하여 기본 그래프를 초안 작성하고 두 번째 모델로 반복적으로 개선하여 복잡한 그래프 생성의 견고성을 향상시킵니다.
- 5. 두 개의 소형 미세 조정된 Flan-T5-Base 모델을 사용하여 DiscoSG-Refiner는 GPT-4o보다 86배 빠른 추론 속도로 SPICE를 약 30% 개선하고, 대체 파서보다 뛰어난 성능을 보입니다.


---

*Generated on 2025-09-24 04:06:03*