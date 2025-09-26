<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:48:17.878771",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "ColorBlindnessEval Benchmark",
    "Ishihara Test",
    "Model Hallucination"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.92,
    "ColorBlindnessEval Benchmark": 0.78,
    "Ishihara Test": 0.8,
    "Model Hallucination": 0.75
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
        "rationale": "Vision-Language Models are central to the paper's focus and are a trending topic, facilitating connections to related multimodal research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.92
      },
      {
        "surface": "ColorBlindnessEval",
        "canonical": "ColorBlindnessEval Benchmark",
        "aliases": [
          "Color Blindness Evaluation"
        ],
        "category": "unique_technical",
        "rationale": "This benchmark is unique to the paper and crucial for evaluating VLMs in specific adversarial scenarios.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Ishihara color blindness test",
        "canonical": "Ishihara Test",
        "aliases": [
          "Ishihara Plates"
        ],
        "category": "specific_connectable",
        "rationale": "The Ishihara Test is a well-known method for detecting color blindness, relevant for linking to medical and vision research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "hallucination issues",
        "canonical": "Model Hallucination",
        "aliases": [
          "hallucination",
          "model errors"
        ],
        "category": "specific_connectable",
        "rationale": "Model hallucination is a critical challenge in AI systems, relevant for discussions on model reliability and robustness.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "benchmark",
      "dataset",
      "participants"
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
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "ColorBlindnessEval",
      "resolved_canonical": "ColorBlindnessEval Benchmark",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Ishihara color blindness test",
      "resolved_canonical": "Ishihara Test",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "hallucination issues",
      "resolved_canonical": "Model Hallucination",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# ColorBlindnessEval: Can Vision-Language Models Pass Color Blindness Tests?

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19070.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2509.19070](https://arxiv.org/abs/2509.19070)

## 🔗 유사한 논문
- [[2025-09-23/Evaluating Fairness in Large Vision-Language Models Across Diverse Demographic Attributes and Prompts_20250923|Evaluating Fairness in Large Vision-Language Models Across Diverse Demographic Attributes and Prompts]] (83.3% similar)
- [[2025-09-23/Benchmarking and Mitigating MCQA Selection Bias of Large Vision-Language Models_20250923|Benchmarking and Mitigating MCQA Selection Bias of Large Vision-Language Models]] (83.2% similar)
- [[2025-09-22/Are Vision-Language Models Safe in the Wild? A Meme-Based Benchmark Study_20250922|Are Vision-Language Models Safe in the Wild? A Meme-Based Benchmark Study]] (82.7% similar)
- [[2025-09-19/QuizRank_ Picking Images by Quizzing VLMs_20250919|QuizRank: Picking Images by Quizzing VLMs]] (82.2% similar)
- [[2025-09-23/Seeing Culture_ A Benchmark for Visual Reasoning and Grounding_20250923|Seeing Culture: A Benchmark for Visual Reasoning and Grounding]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Ishihara Test|Ishihara Test]], [[keywords/Model Hallucination|Model Hallucination]]
**⚡ Unique Technical**: [[keywords/ColorBlindnessEval Benchmark|ColorBlindnessEval Benchmark]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19070v1 Announce Type: cross 
Abstract: This paper presents ColorBlindnessEval, a novel benchmark designed to evaluate the robustness of Vision-Language Models (VLMs) in visually adversarial scenarios inspired by the Ishihara color blindness test. Our dataset comprises 500 Ishihara-like images featuring numbers from 0 to 99 with varying color combinations, challenging VLMs to accurately recognize numerical information embedded in complex visual patterns. We assess 9 VLMs using Yes/No and open-ended prompts and compare their performance with human participants. Our experiments reveal limitations in the models' ability to interpret numbers in adversarial contexts, highlighting prevalent hallucination issues. These findings underscore the need to improve the robustness of VLMs in complex visual environments. ColorBlindnessEval serves as a valuable tool for benchmarking and improving the reliability of VLMs in real-world applications where accuracy is critical.

## 📝 요약

이 논문은 시각-언어 모델(VLM)의 강건성을 평가하기 위해 Ishihara 색맹 테스트에서 영감을 받은 ColorBlindnessEval이라는 새로운 벤치마크를 제시합니다. 이 데이터셋은 0부터 99까지의 숫자를 다양한 색상 조합으로 포함한 500개의 Ishihara 유사 이미지를 포함하며, 복잡한 시각 패턴 속에서 숫자를 정확히 인식하도록 VLM에 도전합니다. 9개의 VLM을 Yes/No 및 개방형 질문으로 평가하고, 인간 참가자와의 성능을 비교한 결과, VLM이 적대적 상황에서 숫자를 해석하는 데 한계가 있음을 발견했습니다. 이러한 결과는 복잡한 시각 환경에서 VLM의 강건성을 향상시킬 필요성을 강조하며, ColorBlindnessEval은 실제 응용에서 VLM의 신뢰성을 개선하는 데 유용한 도구로 작용합니다.

## 🎯 주요 포인트

- 1. ColorBlindnessEval은 VLM의 시각적 적대적 상황에서의 강인함을 평가하기 위한 새로운 벤치마크입니다.
- 2. 데이터셋은 0에서 99까지의 숫자가 다양한 색상 조합으로 포함된 500개의 Ishihara 유사 이미지를 포함합니다.
- 3. 실험 결과, VLM이 적대적 맥락에서 숫자를 해석하는 데 한계가 있음을 발견했습니다.
- 4. 연구는 VLM의 복잡한 시각적 환경에서의 강인함을 개선할 필요성을 강조합니다.
- 5. ColorBlindnessEval은 VLM의 신뢰성을 향상시키기 위한 중요한 도구로 활용될 수 있습니다.


---

*Generated on 2025-09-24 15:48:17*