---
keywords:
  - Large Language Model
  - Frame Semantics
  - FrameNet
  - Prompt-based Inference
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2509.19540
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:42:45.526278",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Frame Semantics",
    "FrameNet",
    "Prompt-based Inference"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Frame Semantics": 0.78,
    "FrameNet": 0.72,
    "Prompt-based Inference": 0.8
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
        "rationale": "This term is central to the study, focusing on the capabilities of large language models in frame semantics.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Frame Semantics",
        "canonical": "Frame Semantics",
        "aliases": [
          "Frame Semantic Parsing"
        ],
        "category": "unique_technical",
        "rationale": "A core concept of the paper, crucial for understanding the semantic analysis performed.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "FrameNet",
        "canonical": "FrameNet",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "FrameNet is a specific lexical resource used for evaluating the models, essential for contextual understanding.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Prompt-based Inference",
        "canonical": "Prompt-based Inference",
        "aliases": [
          "Prompting"
        ],
        "category": "specific_connectable",
        "rationale": "This technique is a key method used in the study to evaluate model performance.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "latent knowledge",
      "task-specific training"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Frame Semantics",
      "resolved_canonical": "Frame Semantics",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "FrameNet",
      "resolved_canonical": "FrameNet",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Prompt-based Inference",
      "resolved_canonical": "Prompt-based Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Do LLMs Encode Frame Semantics? Evidence from Frame Identification

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19540.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2509.19540](https://arxiv.org/abs/2509.19540)

## 🔗 유사한 논문
- [[2025-09-25/Language Models Fail to Introspect About Their Knowledge of Language_20250925|Language Models Fail to Introspect About Their Knowledge of Language]] (84.7% similar)
- [[2025-09-17/Do Large Language Models Understand Word Senses?_20250917|Do Large Language Models Understand Word Senses?]] (84.1% similar)
- [[2025-09-19/Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models_20250919|Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code Large Language Models]] (84.1% similar)
- [[2025-09-23/Robust Native Language Identification through Agentic Decomposition_20250923|Robust Native Language Identification through Agentic Decomposition]] (83.6% similar)
- [[2025-09-19/Large Multi-modal Models Can Interpret Features in Large Multi-modal Models_20250919|Large Multi-modal Models Can Interpret Features in Large Multi-modal Models]] (83.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Prompt-based Inference|Prompt-based Inference]]
**⚡ Unique Technical**: [[keywords/Frame Semantics|Frame Semantics]], [[keywords/FrameNet|FrameNet]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19540v1 Announce Type: new 
Abstract: We investigate whether large language models encode latent knowledge of frame semantics, focusing on frame identification, a core challenge in frame semantic parsing that involves selecting the appropriate semantic frame for a target word in context. Using the FrameNet lexical resource, we evaluate models under prompt-based inference and observe that they can perform frame identification effectively even without explicit supervision. To assess the impact of task-specific training, we fine-tune the model on FrameNet data, which substantially improves in-domain accuracy while generalizing well to out-of-domain benchmarks. Further analysis shows that the models can generate semantically coherent frame definitions, highlighting the model's internalized understanding of frame semantics.

## 📝 요약

이 논문은 대형 언어 모델이 프레임 의미론의 잠재적 지식을 내포하고 있는지를 조사합니다. 특히, 문맥에서 목표 단어에 적합한 의미 프레임을 선택하는 프레임 식별에 중점을 둡니다. FrameNet을 활용하여 프롬프트 기반 추론을 통해 모델을 평가한 결과, 명시적인 감독 없이도 효과적으로 프레임 식별을 수행할 수 있음을 발견했습니다. 또한, FrameNet 데이터로 모델을 미세 조정하면 도메인 내 정확도가 크게 향상되며, 도메인 외 벤치마크에서도 잘 일반화됩니다. 추가 분석에서는 모델이 의미적으로 일관된 프레임 정의를 생성할 수 있음을 보여주어 프레임 의미론에 대한 모델의 내재된 이해를 강조합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델이 프레임 의미론의 잠재적 지식을 내재하고 있는지를 조사하였다.
- 2. 프레임넷 자원을 활용하여 프레임 식별을 위한 프롬프트 기반 추론에서 모델의 성능을 평가하였다.
- 3. 프레임넷 데이터로 모델을 미세 조정하면 도메인 내 정확도가 크게 향상되며, 도메인 외 벤치마크에도 잘 일반화된다.
- 4. 모델이 의미적으로 일관된 프레임 정의를 생성할 수 있음을 보여주어 프레임 의미론에 대한 모델의 내재된 이해를 강조하였다.


---

*Generated on 2025-09-26 08:42:45*