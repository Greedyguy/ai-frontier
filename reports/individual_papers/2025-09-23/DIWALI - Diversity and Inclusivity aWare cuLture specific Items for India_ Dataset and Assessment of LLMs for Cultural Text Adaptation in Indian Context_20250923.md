---
keywords:
  - Large Language Model
  - Cultural Text Adaptation
  - Cultural Competence
  - Culturally Grounded Dataset
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17399
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:24:42.472133",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Cultural Text Adaptation",
    "Cultural Competence",
    "Culturally Grounded Dataset"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Cultural Text Adaptation": 0.8,
    "Cultural Competence": 0.78,
    "Culturally Grounded Dataset": 0.77
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
        "rationale": "Central to the paper's focus on cultural adaptation and evaluation.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cultural Text Adaptation",
        "canonical": "Cultural Text Adaptation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A unique task evaluated in the paper, linking cultural datasets with LLMs.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Cultural Competence",
        "canonical": "Cultural Competence",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Key concept for evaluating LLMs in the context of cultural understanding.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Culturally Grounded Datasets",
        "canonical": "Culturally Grounded Dataset",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Essential for the evaluation of cultural alignment in LLMs.",
        "novelty_score": 0.72,
        "connectivity_score": 0.68,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Evaluation Metrics",
      "Human Evaluations",
      "Quantitative Analysis"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cultural Text Adaptation",
      "resolved_canonical": "Cultural Text Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Cultural Competence",
      "resolved_canonical": "Cultural Competence",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Culturally Grounded Datasets",
      "resolved_canonical": "Culturally Grounded Dataset",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.68,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# DIWALI - Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17399.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17399](https://arxiv.org/abs/2509.17399)

## 🔗 유사한 논문
- [[2025-09-23/Fluent but Foreign_ Even Regional LLMs Lack Cultural Alignment_20250923|Fluent but Foreign: Even Regional LLMs Lack Cultural Alignment]] (88.7% similar)
- [[2025-09-22/CultureScope_ A Dimensional Lens for Probing Cultural Understanding in LLMs_20250922|CultureScope: A Dimensional Lens for Probing Cultural Understanding in LLMs]] (87.5% similar)
- [[2025-09-23/Seeing Culture_ A Benchmark for Visual Reasoning and Grounding_20250923|Seeing Culture: A Benchmark for Visual Reasoning and Grounding]] (82.7% similar)
- [[2025-09-19/Adding LLMs to the psycholinguistic norming toolbox_ A practical guide to getting the most out of human ratings_20250919|Adding LLMs to the psycholinguistic norming toolbox: A practical guide to getting the most out of human ratings]] (81.9% similar)
- [[2025-09-23/AIPsychoBench_ Understanding the Psychometric Differences between LLMs and Humans_20250923|AIPsychoBench: Understanding the Psychometric Differences between LLMs and Humans]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Cultural Text Adaptation|Cultural Text Adaptation]], [[keywords/Cultural Competence|Cultural Competence]], [[keywords/Culturally Grounded Dataset|Culturally Grounded Dataset]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17399v1 Announce Type: new 
Abstract: Large language models (LLMs) are widely used in various tasks and applications. However, despite their wide capabilities, they are shown to lack cultural alignment \citep{ryan-etal-2024-unintended, alkhamissi-etal-2024-investigating} and produce biased generations \cite{naous-etal-2024-beer} due to a lack of cultural knowledge and competence. Evaluation of LLMs for cultural awareness and alignment is particularly challenging due to the lack of proper evaluation metrics and unavailability of culturally grounded datasets representing the vast complexity of cultures at the regional and sub-regional levels. Existing datasets for culture specific items (CSIs) focus primarily on concepts at the regional level and may contain false positives. To address this issue, we introduce a novel CSI dataset for Indian culture, belonging to 17 cultural facets. The dataset comprises $\sim$8k cultural concepts from 36 sub-regions. To measure the cultural competence of LLMs on a cultural text adaptation task, we evaluate the adaptations using the CSIs created, LLM as Judge, and human evaluations from diverse socio-demographic region. Furthermore, we perform quantitative analysis demonstrating selective sub-regional coverage and surface-level adaptations across all considered LLMs. Our dataset is available here: \href{https://huggingface.co/datasets/nlip/DIWALI}{https://huggingface.co/datasets/nlip/DIWALI}, project webpage\footnote{\href{https://nlip-lab.github.io/nlip/publications/diwali/}{https://nlip-lab.github.io/nlip/publications/diwali/}}, and our codebase with model outputs can be found here: \href{https://github.com/pramitsahoo/culture-evaluation}{https://github.com/pramitsahoo/culture-evaluation}.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 문화적 적합성과 편향 문제를 해결하기 위해 인도 문화를 대상으로 한 새로운 문화 특정 항목(CSI) 데이터셋을 소개합니다. 이 데이터셋은 36개 하위 지역에서 17개의 문화적 측면에 걸쳐 약 8,000개의 문화 개념을 포함하고 있습니다. 연구진은 LLM의 문화적 텍스트 적응 작업에서의 문화적 역량을 평가하기 위해 CSI, LLM 평가, 다양한 사회적 배경의 인간 평가를 사용했습니다. 또한, 하위 지역별 선택적 적용과 표면적 적응을 정량적으로 분석했습니다. 데이터셋과 관련 자료는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)은 문화적 지식과 역량 부족으로 인해 문화적 정렬이 부족하고 편향된 결과를 생성하는 것으로 나타났습니다.
- 2. LLM의 문화적 인식 및 정렬 평가가 어려운 이유는 적절한 평가 기준과 지역 및 하위 지역 수준의 문화적 복잡성을 대표하는 데이터셋의 부재 때문입니다.
- 3. 인도 문화를 위한 새로운 CSI 데이터셋이 소개되었으며, 이는 17개의 문화적 측면에 속하는 약 8천 개의 문화 개념을 36개의 하위 지역에서 포함하고 있습니다.
- 4. LLM의 문화적 텍스트 적응 작업에 대한 문화적 역량을 측정하기 위해, CSI를 사용한 적응 평가, LLM 평가, 다양한 사회-인구학적 지역의 인간 평가를 수행했습니다.
- 5. 모든 고려된 LLM에서 선택적 하위 지역 커버리지와 표면 수준의 적응을 보여주는 정량적 분석을 수행했습니다.


---

*Generated on 2025-09-24 03:24:42*