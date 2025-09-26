<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:52:57.142061",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Cycle-Consistency in Question Answering",
    "Large Language Model",
    "Flan-T5 Model",
    "Reasoning Benchmarks"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Cycle-Consistency in Question Answering": 0.8,
    "Large Language Model": 0.85,
    "Flan-T5 Model": 0.75,
    "Reasoning Benchmarks": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Cycle-Consistency in Question Answering",
        "canonical": "Cycle-Consistency in Question Answering",
        "aliases": [
          "CCQA"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel reasoning method specifically proposed in the paper, making it a unique concept for linking.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are a central topic in the paper and connect to a broad range of related research.",
        "novelty_score": 0.2,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Flan-T5 model",
        "canonical": "Flan-T5 Model",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The Flan-T5 model is specifically mentioned as a tool used in the research, providing a unique connection point.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Mathematical and Commonsense Reasoning Benchmarks",
        "canonical": "Reasoning Benchmarks",
        "aliases": [
          "Mathematical Reasoning",
          "Commonsense Reasoning"
        ],
        "category": "specific_connectable",
        "rationale": "These benchmarks are critical for evaluating the proposed method and connect to broader research on reasoning.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "inference-time reasoning",
      "state-of-the-art methods",
      "solution"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Cycle-Consistency in Question Answering",
      "resolved_canonical": "Cycle-Consistency in Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Flan-T5 model",
      "resolved_canonical": "Flan-T5 Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Mathematical and Commonsense Reasoning Benchmarks",
      "resolved_canonical": "Reasoning Benchmarks",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# CCQA: Generating Question from Solution Can Improve Inference-Time Reasoning in SLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18536.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18536](https://arxiv.org/abs/2509.18536)

## 🔗 유사한 논문
- [[2025-09-22/FLARE_ Faithful Logic-Aided Reasoning and Exploration_20250922|FLARE: Faithful Logic-Aided Reasoning and Exploration]] (85.6% similar)
- [[2025-09-23/Step Guided Reasoning_ Improving Mathematical Reasoning using Guidance Generation and Step Reasoning_20250923|Step Guided Reasoning: Improving Mathematical Reasoning using Guidance Generation and Step Reasoning]] (85.6% similar)
- [[2025-09-23/Large Language Models Meet Knowledge Graphs for Question Answering_ Synthesis and Opportunities_20250923|Large Language Models Meet Knowledge Graphs for Question Answering: Synthesis and Opportunities]] (84.4% similar)
- [[2025-09-23/Question Answering with LLMs and Learning from Answer Sets_20250923|Question Answering with LLMs and Learning from Answer Sets]] (83.8% similar)
- [[2025-09-22/Quantifying Self-Awareness of Knowledge in Large Language Models_20250922|Quantifying Self-Awareness of Knowledge in Large Language Models]] (83.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Reasoning Benchmarks|Reasoning Benchmarks]]
**⚡ Unique Technical**: [[keywords/Cycle-Consistency in Question Answering|Cycle-Consistency in Question Answering]], [[keywords/Flan-T5 Model|Flan-T5 Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18536v1 Announce Type: cross 
Abstract: Recently, inference-time reasoning strategies have further improved the accuracy of large language models (LLMs), but their effectiveness on smaller models remains unclear. Based on the observation that conventional approaches often fail to improve performance in this context, we propose \textbf{C}ycle-\textbf{C}onsistency in \textbf{Q}uestion \textbf{A}nswering (CCQA), a novel reasoning method that can be effectively applied to SLMs. Inspired by cycle consistency, CCQA generates a question from each reasoning path and answer, evaluates each by its similarity to the original question, and then selects the candidate solution with the highest similarity score as the final response. Since conventional SLMs struggle to generate accurate questions from their own reasoning paths and answers, we employ a lightweight Flan-T5 model specialized for question generation to support this process efficiently. From the experimental results, it is verified that CCQA consistently outperforms existing state-of-the-art (SOTA) methods across eight models on mathematical and commonsense reasoning benchmarks. Furthermore, our method establishes a new practical baseline for efficient reasoning in SLMs. Source code can be found at https://github.com/scai-research/ccqa_official.

## 📝 요약

이 논문은 소형 언어 모델(SLM)에서 추론 정확도를 높이기 위한 새로운 방법론인 CCQA(Cycle-Consistency in Question Answering)를 제안합니다. CCQA는 각 추론 경로와 답변에서 질문을 생성하고, 이를 원래 질문과의 유사성을 평가하여 가장 높은 유사도 점수를 가진 후보를 최종 답변으로 선택하는 방식입니다. 기존 SLM의 한계를 극복하기 위해, 질문 생성에 특화된 경량 Flan-T5 모델을 사용합니다. 실험 결과, CCQA는 수학 및 상식 추론 벤치마크에서 기존 최첨단(SOTA) 방법들을 능가하며, SLM의 효율적인 추론을 위한 새로운 실용적 기준을 제시합니다.

## 🎯 주요 포인트

- 1. CCQA는 소형 언어 모델(SLM)에 효과적으로 적용할 수 있는 새로운 추론 방법입니다.
- 2. CCQA는 각 추론 경로와 답변에서 질문을 생성하고, 이를 원래 질문과의 유사성으로 평가하여 최종 답변을 선택합니다.
- 3. 경량화된 Flan-T5 모델을 사용하여 SLM의 질문 생성 과정을 지원합니다.
- 4. CCQA는 수학 및 상식 추론 벤치마크에서 기존 최첨단(SOTA) 방법을 능가하는 성능을 보였습니다.
- 5. 이 방법은 SLM의 효율적인 추론을 위한 새로운 실용적 기준을 제시합니다.


---

*Generated on 2025-09-24 13:52:57*