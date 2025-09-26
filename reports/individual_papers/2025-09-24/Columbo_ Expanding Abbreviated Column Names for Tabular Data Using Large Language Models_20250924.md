<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:54:12.502916",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Columbo",
    "NL2SQL",
    "Table Question Answering"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.8,
    "Columbo": 0.85,
    "NL2SQL": 0.78,
    "Table Question Answering": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Language Models"
        ],
        "category": "broad_technical",
        "rationale": "This is a core technology used in the paper's solution, linking it to a broad technical concept.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Columbo",
        "canonical": "Columbo",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Columbo is a unique solution developed in the paper, providing a specific link to the paper's contributions.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "NL2SQL",
        "canonical": "NL2SQL",
        "aliases": [
          "Natural Language to SQL"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specific application area for the paper's solution, enhancing connectivity to related research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Table QA",
        "canonical": "Table Question Answering",
        "aliases": [
          "Table QA"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specific task that benefits from the paper's solution, linking to a focused research area.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "synthetic public data",
      "accuracy measures"
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
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Columbo",
      "resolved_canonical": "Columbo",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "NL2SQL",
      "resolved_canonical": "NL2SQL",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Table QA",
      "resolved_canonical": "Table Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Columbo: Expanding Abbreviated Column Names for Tabular Data Using Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2508.09403.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2508.09403](https://arxiv.org/abs/2508.09403)

## 🔗 유사한 논문
- [[2025-09-22/DynamicNER_ A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition_20250922|DynamicNER: A Dynamic, Multilingual, and Fine-Grained Dataset for LLM-based Named Entity Recognition]] (80.2% similar)
- [[2025-09-22/Tag&Tab_ Pretraining Data Detection in Large Language Models Using Keyword-Based Membership Inference Attack_20250922|Tag&Tab: Pretraining Data Detection in Large Language Models Using Keyword-Based Membership Inference Attack]] (79.7% similar)
- [[2025-09-23/MSCoRe_ A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents_20250923|MSCoRe: A Benchmark for Multi-Stage Collaborative Reasoning in LLM Agents]] (79.4% similar)
- [[2025-09-23/Quality Assessment of Tabular Data using Large Language Models and Code Generation_20250923|Quality Assessment of Tabular Data using Large Language Models and Code Generation]] (79.2% similar)
- [[2025-09-19/MOLE_ Metadata Extraction and Validation in Scientific Papers Using LLMs_20250919|MOLE: Metadata Extraction and Validation in Scientific Papers Using LLMs]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/NL2SQL|NL2SQL]], [[keywords/Table Question Answering|Table Question Answering]]
**⚡ Unique Technical**: [[keywords/Columbo|Columbo]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.09403v3 Announce Type: replace 
Abstract: Expanding the abbreviated column names of tables, such as "esal" to "employee salary", is critical for many downstream NLP tasks for tabular data, such as NL2SQL, table QA, and keyword search. This problem arises in enterprises, domain sciences, government agencies, and more. In this paper, we make three contributions that significantly advance the state of the art. First, we show that the synthetic public data used by prior work has major limitations, and we introduce four new datasets in enterprise/science domains, with real-world abbreviations. Second, we show that accuracy measures used by prior work seriously undercount correct expansions, and we propose new synonym-aware measures that capture accuracy much more accurately. Finally, we develop Columbo, a powerful LLM-based solution that exploits context, rules, chain-of-thought reasoning, and token-level analysis. Extensive experiments show that Columbo significantly outperforms NameGuess, the current most advanced solution, by 4-29%, over five datasets. Columbo has been used in production on EDI, a major data lake for environmental sciences.

## 📝 요약

이 논문은 테이블의 축약된 열 이름을 확장하는 문제를 다룹니다. 주요 기여로는 첫째, 기존 연구에서 사용된 합성 데이터의 한계를 지적하고, 실제 기업 및 과학 분야의 축약어를 포함한 네 가지 새로운 데이터셋을 소개합니다. 둘째, 기존 연구의 정확도 측정 방식의 문제점을 보완하기 위해 동의어를 고려한 새로운 정확도 측정 방법을 제안합니다. 셋째, 문맥, 규칙, 사고의 연쇄, 토큰 수준 분석을 활용하는 강력한 LLM 기반 솔루션인 Columbo를 개발했습니다. 실험 결과, Columbo는 기존 최첨단 솔루션인 NameGuess보다 4-29% 더 높은 성능을 보였으며, 환경 과학 데이터 레이크인 EDI에서 실제로 사용되고 있습니다.

## 🎯 주요 포인트

- 1. 테이블의 축약된 열 이름을 확장하는 것은 NL2SQL, 테이블 QA, 키워드 검색 등 여러 NLP 작업에 중요하다.
- 2. 기존 연구에서 사용된 합성 공공 데이터의 한계를 지적하고, 실제 축약어를 포함한 네 개의 새로운 데이터셋을 소개하였다.
- 3. 기존 연구의 정확도 측정 방식이 올바른 확장을 제대로 반영하지 못한다는 점을 지적하고, 동의어를 고려한 새로운 정확도 측정 방식을 제안하였다.
- 4. Columbo라는 강력한 LLM 기반 솔루션을 개발하여, 문맥, 규칙, 사고의 연결, 토큰 수준 분석을 활용하여 정확도를 높였다.
- 5. Columbo는 5개의 데이터셋에서 기존 최고 솔루션인 NameGuess보다 4-29% 더 높은 성능을 보였으며, 환경 과학을 위한 주요 데이터 레이크인 EDI에서 실제로 사용되고 있다.


---

*Generated on 2025-09-24 15:54:12*