---
keywords:
  - Large Language Model
  - Multi-image Interleaved Reasoning
  - Curriculum Learning
  - Vision-Language Model
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17040
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:41:53.446839",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multi-image Interleaved Reasoning",
    "Curriculum Learning",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.78,
    "Multi-image Interleaved Reasoning": 0.82,
    "Curriculum Learning": 0.8,
    "Vision-Language Model": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-modal Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "MLLMs"
        ],
        "category": "broad_technical",
        "rationale": "This term is central to the paper's focus on enhancing reasoning capabilities across multiple images and text, linking it to the broader field of language models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Multi-image Interleaved Reasoning",
        "canonical": "Multi-image Interleaved Reasoning",
        "aliases": [
          "MIR"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel concept introduced by the paper, essential for understanding its contribution and potential connections to other multi-modal reasoning research.",
        "novelty_score": 0.92,
        "connectivity_score": 0.7,
        "specificity_score": 0.88,
        "link_intent_score": 0.82
      },
      {
        "surface": "Curriculum Learning",
        "canonical": "Curriculum Learning",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "The paper's use of a stage-wise curriculum learning strategy is crucial for understanding the progressive approach to training models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "This concept is key to the paper's focus on reasoning across visual and textual data, linking to recent trends in multimodal AI.",
        "novelty_score": 0.6,
        "connectivity_score": 0.83,
        "specificity_score": 0.77,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "method",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-modal Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Multi-image Interleaved Reasoning",
      "resolved_canonical": "Multi-image Interleaved Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.7,
        "specificity": 0.88,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Curriculum Learning",
      "resolved_canonical": "Curriculum Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.83,
        "specificity": 0.77,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# From Easy to Hard: The MIR Benchmark for Progressive Interleaved Multi-Image Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17040.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17040](https://arxiv.org/abs/2509.17040)

## 🔗 유사한 논문
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (87.0% similar)
- [[2025-09-22/Beyond Spurious Signals_ Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing_20250922|Beyond Spurious Signals: Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing]] (84.0% similar)
- [[2025-09-19/MARIC_ Multi-Agent Reasoning for Image Classification_20250919|MARIC: Multi-Agent Reasoning for Image Classification]] (83.9% similar)
- [[2025-09-22/Multi-Physics_ A Comprehensive Benchmark for Multimodal LLMs Reasoning on Chinese Multi-Subject Physics Problems_20250922|Multi-Physics: A Comprehensive Benchmark for Multimodal LLMs Reasoning on Chinese Multi-Subject Physics Problems]] (83.8% similar)
- [[2025-09-23/NUMINA_ A Natural Understanding Benchmark for Multi-dimensional Intelligence and Numerical Reasoning Abilities_20250923|NUMINA: A Natural Understanding Benchmark for Multi-dimensional Intelligence and Numerical Reasoning Abilities]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Curriculum Learning|Curriculum Learning]]
**⚡ Unique Technical**: [[keywords/Multi-image Interleaved Reasoning|Multi-image Interleaved Reasoning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17040v1 Announce Type: cross 
Abstract: Multi-image Interleaved Reasoning aims to improve Multi-modal Large Language Models (MLLMs) ability to jointly comprehend and reason across multiple images and their associated textual contexts, introducing unique challenges beyond single-image or non-interleaved multi-image tasks. While current multi-image benchmarks overlook interleaved textual contexts and neglect distinct relationships between individual images and their associated texts, enabling models to reason over multi-image interleaved data may significantly enhance their comprehension of complex scenes and better capture cross-modal correlations. To bridge this gap, we introduce a novel benchmark MIR, requiring joint reasoning over multiple images accompanied by interleaved textual contexts to accurately associate image regions with corresponding texts and logically connect information across images. To enhance MLLMs ability to comprehend multi-image interleaved data, we introduce reasoning steps for each instance within the benchmark and propose a stage-wise curriculum learning strategy. This strategy follows an "easy to hard" approach, progressively guiding models from simple to complex scenarios, thereby enhancing their ability to handle challenging tasks. Extensive experiments benchmarking multiple MLLMs demonstrate that our method significantly enhances models reasoning performance on MIR and other established benchmarks. We believe that MIR will encourage further research into multi-image interleaved reasoning, facilitating advancements in MLLMs capability to handle complex inter-modal tasks.Our code and dataset are available at https://github.com/Shelly-coder239/MIRBench.

## 📝 요약

이 논문은 다중 이미지 교차 추론을 통해 다중 모달 대형 언어 모델(MLLMs)의 복잡한 장면 이해 능력을 향상시키는 방법을 제안합니다. 기존의 다중 이미지 벤치마크는 이미지 간의 상호 연관된 텍스트 문맥을 간과하고, 개별 이미지와 텍스트 간의 관계를 충분히 고려하지 못했습니다. 이를 해결하기 위해, 우리는 새로운 벤치마크인 MIR을 도입하여 다중 이미지와 교차된 텍스트 문맥을 함께 추론하도록 요구합니다. 또한, 모델의 추론 능력을 향상시키기 위해 단계적 커리큘럼 학습 전략을 제안하며, 이는 쉬운 것에서 어려운 것으로 점진적으로 모델을 안내합니다. 실험 결과, 이 방법이 MIR 및 다른 벤치마크에서 모델의 추론 성능을 크게 향상시킴을 보여줍니다. 이 연구는 MLLMs의 복잡한 교차 모달 작업 처리 능력을 발전시키는 데 기여할 것으로 기대됩니다.

## 🎯 주요 포인트

- 1. 다중 이미지 교차 추론은 MLLMs의 다중 이미지 및 관련 텍스트 문맥을 이해하고 추론하는 능력을 향상시키고자 한다.
- 2. 기존의 다중 이미지 벤치마크는 교차된 텍스트 문맥을 간과하고 이미지와 텍스트 간의 고유한 관계를 무시한다.
- 3. 새로운 벤치마크 MIR은 다중 이미지와 교차된 텍스트 문맥을 통해 이미지 영역과 텍스트를 정확히 연결하고 논리적으로 정보를 연결하는 것을 요구한다.
- 4. 단계별 커리큘럼 학습 전략을 통해 모델이 단순한 시나리오에서 복잡한 시나리오로 점진적으로 학습하도록 유도한다.
- 5. 제안된 방법은 MIR 및 다른 벤치마크에서 모델의 추론 성능을 크게 향상시킨다.


---

*Generated on 2025-09-23 23:41:53*