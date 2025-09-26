---
keywords:
  - Histopathology Automated Report Evaluation
  - Named Entity Recognition
  - Relation Extraction
  - GatorTronS
  - The Cancer Genome Atlas
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16326
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:10:45.227156",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Histopathology Automated Report Evaluation",
    "Named Entity Recognition",
    "Relation Extraction",
    "GatorTronS",
    "The Cancer Genome Atlas"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Histopathology Automated Report Evaluation": 0.78,
    "Named Entity Recognition": 0.82,
    "Relation Extraction": 0.79,
    "GatorTronS": 0.77,
    "The Cancer Genome Atlas": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "HARE",
        "canonical": "Histopathology Automated Report Evaluation",
        "aliases": [
          "HARE framework"
        ],
        "category": "unique_technical",
        "rationale": "HARE is a novel framework specifically designed for evaluating histopathology reports, making it a unique technical contribution.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "named entity recognition",
        "canonical": "Named Entity Recognition",
        "aliases": [
          "NER"
        ],
        "category": "broad_technical",
        "rationale": "Named Entity Recognition is a fundamental technique in Natural Language Processing, linking it to broader NLP concepts.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "relation extraction",
        "canonical": "Relation Extraction",
        "aliases": [
          "RE"
        ],
        "category": "specific_connectable",
        "rationale": "Relation Extraction is closely related to Named Entity Recognition and is crucial for understanding entity relationships in NLP.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.79
      },
      {
        "surface": "GatorTronS",
        "canonical": "GatorTronS",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "GatorTronS is a domain-adapted language model specifically fine-tuned for this framework, representing a unique technical element.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "The Cancer Genome Atlas",
        "canonical": "The Cancer Genome Atlas",
        "aliases": [
          "TCGA"
        ],
        "category": "specific_connectable",
        "rationale": "The Cancer Genome Atlas is a significant source of histopathology reports, linking it to cancer research and genomic studies.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.78,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "benchmark dataset",
      "traditional metrics",
      "domain-specific metrics"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "HARE",
      "resolved_canonical": "Histopathology Automated Report Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "named entity recognition",
      "resolved_canonical": "Named Entity Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "relation extraction",
      "resolved_canonical": "Relation Extraction",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "GatorTronS",
      "resolved_canonical": "GatorTronS",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "The Cancer Genome Atlas",
      "resolved_canonical": "The Cancer Genome Atlas",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.78,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# HARE: an entity and relation centric evaluation framework for histopathology reports

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16326.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16326](https://arxiv.org/abs/2509.16326)

## 🔗 유사한 논문
- [[2025-09-23/Medical AI Consensus_ A Multi-Agent Framework for Radiology Report Generation and Evaluation_20250923|Medical AI Consensus: A Multi-Agent Framework for Radiology Report Generation and Evaluation]] (81.9% similar)
- [[2025-09-23/IPGPhormer_ Interpretable Pathology Graph-Transformer for Survival Analysis_20250923|IPGPhormer: Interpretable Pathology Graph-Transformer for Survival Analysis]] (81.7% similar)
- [[2025-09-22/CLEAR_ A Clinically-Grounded Tabular Framework for Radiology Report Evaluation_20250922|CLEAR: A Clinically-Grounded Tabular Framework for Radiology Report Evaluation]] (81.5% similar)
- [[2025-09-23/From Scores to Steps_ Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations_20250923|From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations]] (81.5% similar)
- [[2025-09-23/HARPT_ A Corpus for Analyzing Consumers' Trust and Privacy Concerns in Electronic Health Apps_20250923|HARPT: A Corpus for Analyzing Consumers' Trust and Privacy Concerns in Electronic Health Apps]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Named Entity Recognition|Named Entity Recognition]]
**🔗 Specific Connectable**: [[keywords/Relation Extraction|Relation Extraction]], [[keywords/The Cancer Genome Atlas|The Cancer Genome Atlas]]
**⚡ Unique Technical**: [[keywords/Histopathology Automated Report Evaluation|Histopathology Automated Report Evaluation]], [[keywords/GatorTronS|GatorTronS]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16326v1 Announce Type: new 
Abstract: Medical domain automated text generation is an active area of research and development; however, evaluating the clinical quality of generated reports remains a challenge, especially in instances where domain-specific metrics are lacking, e.g. histopathology. We propose HARE (Histopathology Automated Report Evaluation), a novel entity and relation centric framework, composed of a benchmark dataset, a named entity recognition (NER) model, a relation extraction (RE) model, and a novel metric, which prioritizes clinically relevant content by aligning critical histopathology entities and relations between reference and generated reports. To develop the HARE benchmark, we annotated 813 de-identified clinical diagnostic histopathology reports and 652 histopathology reports from The Cancer Genome Atlas (TCGA) with domain-specific entities and relations. We fine-tuned GatorTronS, a domain-adapted language model to develop HARE-NER and HARE-RE which achieved the highest overall F1-score (0.915) among the tested models. The proposed HARE metric outperformed traditional metrics including ROUGE and Meteor, as well as radiology metrics such as RadGraph-XL, with the highest correlation and the best regression to expert evaluations (higher than the second best method, GREEN, a large language model based radiology report evaluator, by Pearson $r = 0.168$, Spearman $\rho = 0.161$, Kendall $\tau = 0.123$, $R^2 = 0.176$, $RMSE = 0.018$). We release HARE, datasets, and the models at https://github.com/knowlab/HARE to foster advancements in histopathology report generation, providing a robust framework for improving the quality of reports.

## 📝 요약

이 연구는 병리학 보고서 생성의 임상적 품질 평가를 위한 새로운 프레임워크인 HARE(Histopathology Automated Report Evaluation)를 제안합니다. HARE는 벤치마크 데이터셋, 개체명 인식(NER) 모델, 관계 추출(RE) 모델, 새로운 평가 지표로 구성되어 있으며, 임상적으로 중요한 병리학 개체와 관계를 강조합니다. 연구진은 813개의 임상 진단 병리 보고서와 652개의 TCGA 병리 보고서를 도메인 특화 개체와 관계로 주석 처리하여 HARE 벤치마크를 개발했습니다. GatorTronS 언어 모델을 활용하여 개발된 HARE-NER과 HARE-RE는 테스트된 모델 중 가장 높은 F1 점수(0.915)를 기록했습니다. HARE 지표는 전통적인 ROUGE 및 Meteor 지표뿐만 아니라 방사선학 지표인 RadGraph-XL보다도 높은 상관성과 전문가 평가에 대한 회귀 성능을 보였습니다. 연구 결과는 병리학 보고서 생성의 품질 향상을 위한 강력한 프레임워크를 제공하며, 관련 데이터셋과 모델은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. HARE는 임상적으로 중요한 내용을 우선시하여 참조 보고서와 생성된 보고서 간의 핵심 병리학 엔티티와 관계를 정렬하는 새로운 평가 프레임워크입니다.
- 2. HARE 벤치마크 개발을 위해 813개의 비식별화된 임상 진단 병리 보고서와 652개의 TCGA 병리 보고서를 도메인 특화 엔티티와 관계로 주석 처리했습니다.
- 3. GatorTronS를 미세 조정하여 HARE-NER 및 HARE-RE 모델을 개발했으며, 이 모델은 테스트된 모델 중 가장 높은 F1-score(0.915)를 기록했습니다.
- 4. 제안된 HARE 메트릭은 ROUGE, Meteor 등 전통적인 메트릭 및 RadGraph-XL과 같은 방사선학 메트릭을 능가하며 전문가 평가와의 상관관계 및 회귀에서 최고 성능을 보였습니다.
- 5. HARE, 데이터셋 및 모델은 히스토패톨로지 보고서 생성의 발전을 촉진하기 위해 공개되었으며, 보고서 품질 향상을 위한 견고한 프레임워크를 제공합니다.


---

*Generated on 2025-09-24 03:10:45*