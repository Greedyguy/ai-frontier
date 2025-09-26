---
keywords:
  - Large Language Model
  - Misinformation Evolution
  - Persona-Conditioned Generation
  - Semantic Drift
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16564
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:14:07.030095",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Misinformation Evolution",
    "Persona-Conditioned Generation",
    "Semantic Drift"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Misinformation Evolution": 0.78,
    "Persona-Conditioned Generation": 0.77,
    "Semantic Drift": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's methodology and connect to broader discussions in NLP.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Misinformation Evolution",
        "canonical": "Misinformation Evolution",
        "aliases": [
          "Misinformation Dynamics"
        ],
        "category": "unique_technical",
        "rationale": "This concept is key to the paper's focus on how misinformation changes over time.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Persona-Conditioned Generation",
        "canonical": "Persona-Conditioned Generation",
        "aliases": [
          "Persona-Based Generation"
        ],
        "category": "unique_technical",
        "rationale": "This novel approach is central to the study's methodology, offering a new perspective on content generation.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Semantic Drift",
        "canonical": "Semantic Drift",
        "aliases": [
          "Semantic Change"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding semantic drift is crucial for analyzing how misinformation evolves.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Misinformation Evolution",
      "resolved_canonical": "Misinformation Evolution",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Persona-Conditioned Generation",
      "resolved_canonical": "Persona-Conditioned Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Semantic Drift",
      "resolved_canonical": "Semantic Drift",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# MPCG: Multi-Round Persona-Conditioned Generation for Modeling the Evolution of Misinformation with LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16564.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16564](https://arxiv.org/abs/2509.16564)

## 🔗 유사한 논문
- [[2025-09-22/The Psychology of Falsehood_ A Human-Centric Survey of Misinformation Detection_20250922|The Psychology of Falsehood: A Human-Centric Survey of Misinformation Detection]] (82.6% similar)
- [[2025-09-23/Privacy-Aware In-Context Learning for Large Language Models_20250923|Privacy-Aware In-Context Learning for Large Language Models]] (81.5% similar)
- [[2025-09-19/Internalizing Self-Consistency in Language Models_ Multi-Agent Consensus Alignment_20250919|Internalizing Self-Consistency in Language Models: Multi-Agent Consensus Alignment]] (81.5% similar)
- [[2025-09-23/Privacy in Action_ Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents_20250923|Privacy in Action: Towards Realistic Privacy Mitigation and Evaluation for LLM-Powered Agents]] (81.3% similar)
- [[2025-09-23/Steering Towards Fairness_ Mitigating Political Bias in LLMs_20250923|Steering Towards Fairness: Mitigating Political Bias in LLMs]] (81.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Semantic Drift|Semantic Drift]]
**⚡ Unique Technical**: [[keywords/Misinformation Evolution|Misinformation Evolution]], [[keywords/Persona-Conditioned Generation|Persona-Conditioned Generation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16564v1 Announce Type: new 
Abstract: Misinformation evolves as it spreads, shifting in language, framing, and moral emphasis to adapt to new audiences. However, current misinformation detection approaches implicitly assume that misinformation is static. We introduce MPCG, a multi-round, persona-conditioned framework that simulates how claims are iteratively reinterpreted by agents with distinct ideological perspectives. Our approach uses an uncensored large language model (LLM) to generate persona-specific claims across multiple rounds, conditioning each generation on outputs from the previous round, enabling the study of misinformation evolution. We evaluate the generated claims through human and LLM-based annotations, cognitive effort metrics (readability, perplexity), emotion evocation metrics (sentiment analysis, morality), clustering, feasibility, and downstream classification. Results show strong agreement between human and GPT-4o-mini annotations, with higher divergence in fluency judgments. Generated claims require greater cognitive effort than the original claims and consistently reflect persona-aligned emotional and moral framing. Clustering and cosine similarity analyses confirm semantic drift across rounds while preserving topical coherence. Feasibility results show a 77% feasibility rate, confirming suitability for downstream tasks. Classification results reveal that commonly used misinformation detectors experience macro-F1 performance drops of up to 49.7%. The code is available at https://github.com/bcjr1997/MPCG

## 📝 요약

이 논문은 허위 정보가 전파되면서 언어, 프레임, 도덕적 강조점이 변화하는 과정을 연구합니다. 기존의 허위 정보 탐지 방법은 정보를 고정된 것으로 가정하지만, 저자들은 이를 극복하기 위해 MPCG라는 다중 라운드, 페르소나 조건화 프레임워크를 제안합니다. 이 방법은 대형 언어 모델을 사용해 다양한 이념적 관점을 가진 에이전트가 주장을 재해석하는 과정을 시뮬레이션합니다. 연구 결과, 생성된 주장은 원본보다 높은 인지적 노력을 요구하며, 페르소나에 맞춘 감정적, 도덕적 프레이밍을 보여줍니다. 또한, 기존의 허위 정보 탐지기가 성능 저하를 겪는 것으로 나타났습니다. 이 연구는 허위 정보의 진화 과정을 이해하는 데 기여하며, 관련 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 허위 정보는 전파되면서 언어, 프레이밍, 도덕적 강조점이 변화하여 새로운 청중에 맞춰 적응한다.
- 2. MPCG는 다양한 이데올로기적 관점을 가진 에이전트들이 주장을 반복적으로 재해석하는 과정을 시뮬레이션하는 프레임워크이다.
- 3. 생성된 주장은 원래 주장보다 더 많은 인지적 노력을 요구하며, 페르소나에 맞춘 감정적 및 도덕적 프레이밍을 일관되게 반영한다.
- 4. 클러스터링 및 코사인 유사도 분석은 주제의 일관성을 유지하면서도 라운드 간 의미적 변화를 확인한다.
- 5. 일반적인 허위 정보 탐지기는 최대 49.7%의 성능 저하를 경험하며, 이는 MPCG의 유효성을 입증한다.


---

*Generated on 2025-09-24 03:14:07*