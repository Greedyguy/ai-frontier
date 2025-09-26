<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:53:01.695464",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Chain-of-Thought Reasoning",
    "Step-by-step Prompting",
    "Translation Decomposition"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Chain-of-Thought Reasoning": 0.78,
    "Step-by-step Prompting": 0.72,
    "Translation Decomposition": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "As a foundational technology in the paper, it connects to a wide range of topics in NLP and AI.",
        "novelty_score": 0.35,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Chain-of-Thought reasoning",
        "canonical": "Chain-of-Thought Reasoning",
        "aliases": [
          "CoT reasoning"
        ],
        "category": "unique_technical",
        "rationale": "This technique is central to the paper's exploration of translation strategies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Step-by-step prompting",
        "canonical": "Step-by-step Prompting",
        "aliases": [
          "multi-step prompting"
        ],
        "category": "unique_technical",
        "rationale": "It represents a specific method of interacting with LLMs, relevant to the paper's findings.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.77,
        "link_intent_score": 0.72
      },
      {
        "surface": "Translation decomposition",
        "canonical": "Translation Decomposition",
        "aliases": [
          "decomposing translation"
        ],
        "category": "unique_technical",
        "rationale": "This concept is key to understanding the paper's critique of current translation methods.",
        "novelty_score": 0.68,
        "connectivity_score": 0.68,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "human-like reasoning",
      "performance gains",
      "empirical evidence"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.35,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Chain-of-Thought reasoning",
      "resolved_canonical": "Chain-of-Thought Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Step-by-step prompting",
      "resolved_canonical": "Step-by-step Prompting",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.77,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Translation decomposition",
      "resolved_canonical": "Translation Decomposition",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.68,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Please Translate Again: Two Simple Experiments on Whether Human-Like Reasoning Helps Translation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2506.04521.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2506.04521](https://arxiv.org/abs/2506.04521)

## 🔗 유사한 논문
- [[2025-09-23/Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates_20250923|Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates]] (86.5% similar)
- [[2025-09-24/LightThinker_ Thinking Step-by-Step Compression_20250924|LightThinker: Thinking Step-by-Step Compression]] (83.8% similar)
- [[2025-09-23/EvoCoT_ Overcoming the Exploration Bottleneck in Reinforcement Learning_20250923|EvoCoT: Overcoming the Exploration Bottleneck in Reinforcement Learning]] (83.7% similar)
- [[2025-09-23/GPO_ Learning from Critical Steps to Improve LLM Reasoning_20250923|GPO: Learning from Critical Steps to Improve LLM Reasoning]] (83.5% similar)
- [[2025-09-22/Language Mixing in Reasoning Language Models_ Patterns, Impact, and Internal Causes_20250922|Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Chain-of-Thought Reasoning|Chain-of-Thought Reasoning]], [[keywords/Step-by-step Prompting|Step-by-step Prompting]], [[keywords/Translation Decomposition|Translation Decomposition]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.04521v2 Announce Type: replace 
Abstract: Large Language Models (LLMs) demonstrate strong reasoning capabilities for many tasks, often by explicitly decomposing the task via Chain-of-Thought (CoT) reasoning. Recent work on LLM-based translation designs hand-crafted prompts to decompose translation, or trains models to incorporate intermediate steps. Translating Step-by-step (Briakou et al., 2024), for instance, introduces a multi-step prompt with decomposition and refinement of translation with LLMs, which achieved state-of-the-art results on WMT24 test data. In this work, we scrutinise this strategy's effectiveness. Empirically, we find no clear evidence that performance gains stem from explicitly decomposing the translation process via CoT, at least for the models on test; and we show prompting LLMs to 'translate again' and self-refine yields even better results than human-like step-by-step prompting. While the decomposition influences translation behaviour, faithfulness to the decomposition has both positive and negative effects on translation. Our analysis therefore suggests a divergence between the optimal translation strategies for humans and LLMs.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 번역 성능을 향상시키기 위한 체인 오브 소트(Chain-of-Thought, CoT) 방식의 효과를 분석합니다. 기존 연구에서는 번역 과정을 단계별로 나누어 수행하는 방법을 제안했으나, 실험 결과 이러한 방법이 성능 향상의 주요 원인이라는 명확한 증거는 발견되지 않았습니다. 대신, LLM에게 번역을 반복하고 스스로 개선하도록 유도하는 방식이 더 나은 결과를 보였습니다. 이는 인간과 LLM의 최적 번역 전략이 다를 수 있음을 시사합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 Chain-of-Thought(COT) 추론을 통해 많은 작업에서 강력한 추론 능력을 보여줍니다.
- 2. 번역 작업에서 LLM 기반의 번역은 중간 단계를 포함하도록 모델을 훈련하거나 수작업으로 프롬프트를 설계하여 번역을 분해합니다.
- 3. 'Step-by-step' 번역 방식은 LLM을 사용하여 번역을 분해하고 정제하는 다단계 프롬프트를 도입하여 WMT24 테스트 데이터에서 최첨단 결과를 달성했습니다.
- 4. 연구 결과, 번역 과정에서 CoT를 통한 명시적 분해가 성능 향상에 기여한다는 명확한 증거는 없었으며, '다시 번역'하고 자체 정제를 유도하는 프롬프트가 더 나은 결과를 가져왔습니다.
- 5. 번역 분해는 번역 행동에 영향을 미치며, 인간과 LLM의 최적 번역 전략 간의 차이가 있음을 시사합니다.


---

*Generated on 2025-09-24 15:53:01*