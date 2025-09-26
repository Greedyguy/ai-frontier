<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:28:38.019309",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "CRISP",
    "OMOP CDM",
    "SNOMED-CT",
    "Clinical Artificial Intelligence"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "CRISP": 0.8,
    "OMOP CDM": 0.78,
    "SNOMED-CT": 0.77,
    "Clinical Artificial Intelligence": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "CRITICAL Records Integrated Standardization Pipeline",
        "canonical": "CRISP",
        "aliases": [
          "CRITICAL Records Integrated Standardization Pipeline"
        ],
        "category": "unique_technical",
        "rationale": "CRISP is a novel pipeline specifically designed for processing large-scale multi-institutional OMOP CDM data, offering a unique contribution to data harmonization efforts.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Observational Medical Outcomes Partnership Common Data Model",
        "canonical": "OMOP CDM",
        "aliases": [
          "Observational Medical Outcomes Partnership Common Data Model"
        ],
        "category": "specific_connectable",
        "rationale": "OMOP CDM is a widely recognized framework for standardizing healthcare data, facilitating connections with other research using similar models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "SNOMED-CT standards",
        "canonical": "SNOMED-CT",
        "aliases": [
          "SNOMED Clinical Terms"
        ],
        "category": "specific_connectable",
        "rationale": "SNOMED-CT is a comprehensive clinical terminology that enhances interoperability and data sharing across healthcare systems.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "clinical AI",
        "canonical": "Clinical Artificial Intelligence",
        "aliases": [
          "clinical AI"
        ],
        "category": "broad_technical",
        "rationale": "Clinical AI is a broad technical domain that connects with various healthcare applications, facilitating advancements in predictive modeling and health equity.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "data harmonization",
      "baseline model benchmarks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "CRITICAL Records Integrated Standardization Pipeline",
      "resolved_canonical": "CRISP",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Observational Medical Outcomes Partnership Common Data Model",
      "resolved_canonical": "OMOP CDM",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "SNOMED-CT standards",
      "resolved_canonical": "SNOMED-CT",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "clinical AI",
      "resolved_canonical": "Clinical Artificial Intelligence",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# The CRITICAL Records Integrated Standardization Pipeline (CRISP): End-to-End Processing of Large-scale Multi-institutional OMOP CDM Data

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.08247.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.08247](https://arxiv.org/abs/2509.08247)

## 🔗 유사한 논문
- [[2025-09-23/Longitudinal and Multimodal Recording System to Capture Real-World Patient-Clinician Conversations for AI and Encounter Research_ Protocol_20250923|Longitudinal and Multimodal Recording System to Capture Real-World Patient-Clinician Conversations for AI and Encounter Research: Protocol]] (82.0% similar)
- [[2025-09-23/MIRA_ Medical Time Series Foundation Model for Real-World Health Data_20250923|MIRA: Medical Time Series Foundation Model for Real-World Health Data]] (80.3% similar)
- [[2025-09-23/Enhancing Clinical Decision-Making_ Integrating Multi-Agent Systems with Ethical AI Governance_20250923|Enhancing Clinical Decision-Making: Integrating Multi-Agent Systems with Ethical AI Governance]] (80.1% similar)
- [[2025-09-24/Citrus-V_ Advancing Medical Foundation Models with Unified Medical Image Grounding for Clinical Reasoning_20250924|Citrus-V: Advancing Medical Foundation Models with Unified Medical Image Grounding for Clinical Reasoning]] (80.1% similar)
- [[2025-09-18/Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT_20250918|Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Clinical Artificial Intelligence|Clinical Artificial Intelligence]]
**🔗 Specific Connectable**: [[keywords/OMOP CDM|OMOP CDM]], [[keywords/SNOMED-CT|SNOMED-CT]]
**⚡ Unique Technical**: [[keywords/CRISP|CRISP]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.08247v2 Announce Type: replace 
Abstract: While existing critical care EHR datasets such as MIMIC and eICU have enabled significant advances in clinical AI research, the CRITICAL dataset opens new frontiers by providing extensive scale and diversity -- containing 1.95 billion records from 371,365 patients across four geographically diverse CTSA institutions. CRITICAL's unique strength lies in capturing full-spectrum patient journeys, including pre-ICU, ICU, and post-ICU encounters across both inpatient and outpatient settings. This multi-institutional, longitudinal perspective creates transformative opportunities for developing generalizable predictive models and advancing health equity research. However, the richness of this multi-site resource introduces substantial complexity in data harmonization, with heterogeneous collection practices and diverse vocabulary usage patterns requiring sophisticated preprocessing approaches.
  We present CRISP to unlock the full potential of this valuable resource. CRISP systematically transforms raw Observational Medical Outcomes Partnership Common Data Model data into ML-ready datasets through: (1) transparent data quality management with comprehensive audit trails, (2) cross-vocabulary mapping of heterogeneous medical terminologies to unified SNOMED-CT standards, with deduplication and unit standardization, (3) modular architecture with parallel optimization enabling complete dataset processing in $<$1 day even on standard computing hardware, and (4) comprehensive baseline model benchmarks spanning multiple clinical prediction tasks to establish reproducible performance standards. By providing processing pipeline, baseline implementations, and detailed transformation documentation, CRISP saves researchers months of preprocessing effort and democratizes access to large-scale multi-institutional critical care data, enabling them to focus on advancing clinical AI.

## 📝 요약

CRITICAL 데이터셋은 371,365명의 환자에 대한 19억 5천만 개의 기록을 포함하며, 다양한 지리적 위치의 CTSA 기관에서 수집된 데이터를 통해 임상 AI 연구에 새로운 가능성을 제공합니다. 이 데이터셋은 ICU 전후의 환자 여정을 포괄적으로 담고 있어 일반화 가능한 예측 모델 개발과 건강 형평성 연구에 기여할 수 있습니다. 그러나 데이터의 복잡성과 다양한 용어 사용으로 인해 데이터 조화가 어려운 문제점이 있습니다. 이를 해결하기 위해 CRISP는 데이터 품질 관리, 용어 통합, 모듈식 아키텍처, 임상 예측 과제를 위한 기준 모델 벤치마크를 통해 데이터를 ML에 적합하게 변환합니다. CRISP는 연구자들이 대규모 다기관 중환자 데이터에 쉽게 접근할 수 있도록 하여 임상 AI 발전에 집중할 수 있게 합니다.

## 🎯 주요 포인트

- 1. CRITICAL 데이터셋은 371,365명의 환자로부터 19억 5천만 개의 기록을 포함하여, 다양한 지리적 배경의 CTSA 기관들에서 수집된 방대한 규모와 다양성을 제공합니다.
- 2. CRITICAL의 강점은 입원 및 외래 환경에서의 ICU 전, 중, 후의 환자 여정을 포괄적으로 포착하여 일반화 가능한 예측 모델 개발과 건강 형평성 연구를 촉진할 수 있다는 점입니다.
- 3. CRISP는 복잡한 데이터 전처리 과정을 단순화하여 연구자들이 대규모 다기관 중환자 치료 데이터를 쉽게 활용할 수 있도록 지원합니다.
- 4. CRISP는 SNOMED-CT 표준으로의 의료 용어 교차 매핑, 데이터 품질 관리, 모듈형 아키텍처 및 다양한 임상 예측 작업에 대한 기준 모델 벤치마크를 제공합니다.
- 5. CRISP는 연구자들이 전처리에 소요되는 시간을 절약하고 임상 AI 발전에 집중할 수 있도록 지원하는 처리 파이프라인과 변환 문서를 제공합니다.


---

*Generated on 2025-09-24 15:28:38*