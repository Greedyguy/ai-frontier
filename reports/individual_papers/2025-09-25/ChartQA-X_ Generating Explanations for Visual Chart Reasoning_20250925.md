---
keywords:
  - ChartQA-X
  - Explanatory Narratives
  - Question-Answering
  - Visual Chart Reasoning
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2504.13275
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:24:45.287449",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "ChartQA-X",
    "Explanatory Narratives",
    "Question-Answering",
    "Visual Chart Reasoning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "ChartQA-X": 0.8,
    "Explanatory Narratives": 0.78,
    "Question-Answering": 0.8,
    "Visual Chart Reasoning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "ChartQA-X",
        "canonical": "ChartQA-X",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "ChartQA-X is a unique dataset central to the paper's contributions, enabling connections to datasets and benchmarks in visual reasoning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "explanations",
        "canonical": "Explanatory Narratives",
        "aliases": [
          "explanations",
          "explanation generation"
        ],
        "category": "evolved_concepts",
        "rationale": "Explanatory narratives are key to understanding complex data, linking to concepts in interpretability and explainable AI.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "question-answering accuracy",
        "canonical": "Question-Answering",
        "aliases": [
          "QA accuracy",
          "question answering"
        ],
        "category": "broad_technical",
        "rationale": "Question-answering is a fundamental task in NLP, connecting to a wide range of language processing applications.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "visual chart reasoning",
        "canonical": "Visual Chart Reasoning",
        "aliases": [
          "chart reasoning",
          "visual reasoning"
        ],
        "category": "specific_connectable",
        "rationale": "Visual chart reasoning is a specific task that connects to multimodal learning and vision-language models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "faithfulness",
      "informativeness",
      "coherence",
      "perplexity"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "ChartQA-X",
      "resolved_canonical": "ChartQA-X",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "explanations",
      "resolved_canonical": "Explanatory Narratives",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "question-answering accuracy",
      "resolved_canonical": "Question-Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "visual chart reasoning",
      "resolved_canonical": "Visual Chart Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# ChartQA-X: Generating Explanations for Visual Chart Reasoning

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2504.13275.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2504.13275](https://arxiv.org/abs/2504.13275)

## 🔗 유사한 논문
- [[2025-09-23/Unmasking Deceptive Visuals_ Benchmarking Multimodal Large Language Models on Misleading Chart Question Answering_20250923|Unmasking Deceptive Visuals: Benchmarking Multimodal Large Language Models on Misleading Chart Question Answering]] (86.2% similar)
- [[2025-09-24/Losing the Plot_ How VLM responses degrade on imperfect charts_20250924|Losing the Plot: How VLM responses degrade on imperfect charts]] (85.6% similar)
- [[2025-09-23/See What I Mean? CUE_ A Cognitive Model of Understanding Explanations_20250923|See What I Mean? CUE: A Cognitive Model of Understanding Explanations]] (83.4% similar)
- [[2025-09-23/ChartHal_ A Fine-grained Framework Evaluating Hallucination of Large Vision Language Models in Chart Understanding_20250923|ChartHal: A Fine-grained Framework Evaluating Hallucination of Large Vision Language Models in Chart Understanding]] (83.0% similar)
- [[2025-09-22/Generating Part-Based Global Explanations Via Correspondence_20250922|Generating Part-Based Global Explanations Via Correspondence]] (82.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Question-Answering|Question-Answering]]
**🔗 Specific Connectable**: [[keywords/Visual Chart Reasoning|Visual Chart Reasoning]]
**⚡ Unique Technical**: [[keywords/ChartQA-X|ChartQA-X]]
**🚀 Evolved Concepts**: [[keywords/Explanatory Narratives|Explanatory Narratives]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.13275v3 Announce Type: replace 
Abstract: The ability to explain complex information from chart images is vital for effective data-driven decision-making. In this work, we address the challenge of generating detailed explanations alongside answering questions about charts. We present ChartQA-X, a comprehensive dataset comprising 30,299 chart samples across four chart types, each paired with contextually relevant questions, answers, and explanations. Explanations are generated and selected based on metrics such as faithfulness, informativeness, coherence, and perplexity. Our human evaluation with 245 participants shows that model-generated explanations in ChartQA-X surpass human-written explanations in accuracy and logic and are comparable in terms of clarity and overall quality. Moreover, models fine-tuned on ChartQA-X show substantial improvements across various metrics, including absolute gains of up to 24.57 points in explanation quality, 18.96 percentage points in question-answering accuracy, and 14.75 percentage points on unseen benchmarks for the same task. By integrating explanatory narratives with answers, our approach enables agents to convey complex visual information more effectively, improving comprehension and greater trust in the generated responses.

## 📝 요약

이 연구는 차트 이미지에서 복잡한 정보를 설명하는 능력을 향상시키기 위한 것으로, ChartQA-X라는 데이터셋을 소개합니다. 이 데이터셋은 30,299개의 차트 샘플과 관련 질문, 답변, 설명을 포함하며, 설명은 신뢰성, 정보성, 일관성, 당혹도를 기준으로 생성 및 선택됩니다. 245명의 참가자를 대상으로 한 인간 평가에서, 모델이 생성한 설명이 인간이 작성한 설명보다 정확성과 논리성에서 우수하며 명확성과 전반적 품질에서도 비슷한 수준임을 보였습니다. ChartQA-X로 미세 조정된 모델은 설명 품질에서 최대 24.57점, 질문-답변 정확도에서 18.96%포인트, 새로운 벤치마크에서 14.75%포인트의 향상을 보였습니다. 이 접근법은 설명 내러티브를 답변과 통합하여 복잡한 시각 정보를 효과적으로 전달하고, 이해도와 신뢰성을 높입니다.

## 🎯 주요 포인트

- 1. ChartQA-X는 30,299개의 차트 샘플과 관련 질문, 답변, 설명을 포함한 포괄적인 데이터셋을 제공합니다.
- 2. 생성된 설명은 신뢰성, 정보성, 일관성, 혼란도 등의 기준에 따라 선택됩니다.
- 3. ChartQA-X로 미세 조정된 모델은 설명 품질에서 최대 24.57점, 질문-답변 정확도에서 18.96% 포인트, 새로운 벤치마크에서 14.75% 포인트의 절대적 향상을 보였습니다.
- 4. 모델 생성 설명은 정확성과 논리성에서 인간이 작성한 설명을 능가하며, 명확성과 전체적인 품질에서도 유사한 수준을 보입니다.
- 5. 설명적 내러티브와 답변을 통합함으로써 복잡한 시각 정보를 효과적으로 전달하고, 이해도와 신뢰도를 높입니다.


---

*Generated on 2025-09-26 09:24:45*