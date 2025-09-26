<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:44:47.273567",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Electronic Fetal Monitoring",
    "Time-Series Analysis",
    "Foundation Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Electronic Fetal Monitoring": 0.8,
    "Time-Series Analysis": 0.77,
    "Foundation Model": 0.79
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
        "rationale": "LLMs are central to the paper's comparison and offer strong connectivity to existing AI discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Electronic Fetal Monitoring",
        "canonical": "Electronic Fetal Monitoring",
        "aliases": [
          "EFM",
          "Cardiotocography",
          "CTG"
        ],
        "category": "unique_technical",
        "rationale": "EFM is a specific application domain of interest, providing unique technical insights into prenatal care.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Time-Series Analysis",
        "canonical": "Time-Series Analysis",
        "aliases": [
          "Long Time-Series Data"
        ],
        "category": "specific_connectable",
        "rationale": "Time-series analysis is crucial for understanding the data structure in CTG, linking to broader data analysis techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Foundation Models",
        "canonical": "Foundation Model",
        "aliases": [
          "FMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Foundation models are a newer concept in AI, offering a broad perspective on model capabilities.",
        "novelty_score": 0.68,
        "connectivity_score": 0.82,
        "specificity_score": 0.65,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "antepartum",
      "clinical interpretation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Electronic Fetal Monitoring",
      "resolved_canonical": "Electronic Fetal Monitoring",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Time-Series Analysis",
      "resolved_canonical": "Time-Series Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Foundation Models",
      "resolved_canonical": "Foundation Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.82,
        "specificity": 0.65,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Large language models surpass domain-specific architectures for antepartum electronic fetal monitoring analysis

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18112.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18112](https://arxiv.org/abs/2509.18112)

## 🔗 유사한 논문
- [[2025-09-19/Artificial Intelligence-derived Cardiotocography Age as a Digital Biomarker for Predicting Future Adverse Pregnancy Outcomes_20250919|Artificial Intelligence-derived Cardiotocography Age as a Digital Biomarker for Predicting Future Adverse Pregnancy Outcomes]] (85.7% similar)
- [[2025-09-22/EHR-MCP_ Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol_20250922|EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol]] (82.4% similar)
- [[2025-09-24/Advances in Large Language Models for Medicine_20250924|Advances in Large Language Models for Medicine]] (82.2% similar)
- [[2025-09-24/Model selection meets clinical semantics_ Optimizing ICD-10-CM prediction via LLM-as-Judge evaluation, redundancy-aware sampling, and section-aware fine-tuning_20250924|Model selection meets clinical semantics: Optimizing ICD-10-CM prediction via LLM-as-Judge evaluation, redundancy-aware sampling, and section-aware fine-tuning]] (81.5% similar)
- [[2025-09-24/Learning neuroimaging models from health system-scale data_20250924|Learning neuroimaging models from health system-scale data]] (81.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Time-Series Analysis|Time-Series Analysis]]
**⚡ Unique Technical**: [[keywords/Electronic Fetal Monitoring|Electronic Fetal Monitoring]]
**🚀 Evolved Concepts**: [[keywords/Foundation Model|Foundation Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18112v1 Announce Type: new 
Abstract: Foundation models (FMs) and large language models (LLMs) demonstrate remarkable capabilities across diverse domains through training on massive datasets. These models have demonstrated exceptional performance in healthcare applications, yet their potential for electronic fetal monitoring (EFM)/cardiotocography (CTG) analysis, a critical technology for evaluating fetal well-being, remains largely underexplored. Antepartum CTG interpretation presents unique challenges due to the complex nature of fetal heart rate (FHR) patterns and uterine activity, requiring sophisticated analysis of long time-series data. The assessment of CTG is heavily based on subjective clinical interpretation, often leading to variability in diagnostic accuracy and deviation from timely pregnancy care. This study presents the first comprehensive comparison of state-of-the-art AI approaches for automated antepartum CTG analysis. We systematically compare time-series FMs and LLMs against established CTG-specific architectures. Our evaluation encompasses over 500 CTG recordings of varying durations reflecting real-world clinical recordings, providing robust performance benchmarks across different modelling paradigms. Our results demonstrate that fine-tuned LLMs achieve superior performance compared to both foundation models and domain-specific approaches, offering a promising alternative pathway for clinical CTG interpretation. These findings provide critical insights into the relative strengths of different AI methodologies for fetal monitoring applications and establish a foundation for future clinical AI development in prenatal care.

## 📝 요약

이 연구는 대규모 데이터셋으로 훈련된 기초 모델(FM)과 대형 언어 모델(LLM)의 전자 태아 모니터링(CTG) 분석에 대한 잠재력을 탐구합니다. CTG 해석은 태아 심박수 패턴과 자궁 활동의 복잡성 때문에 도전적이며, 주관적인 임상 해석에 의존해 진단 정확도에 변동이 있습니다. 본 연구는 자동화된 CTG 분석을 위한 최신 AI 접근법을 비교하며, 500개 이상의 CTG 기록을 평가하여 다양한 모델링 패러다임의 성능을 검증했습니다. 그 결과, 미세 조정된 LLM이 기초 모델과 도메인 특화 접근법보다 우수한 성능을 보였으며, 임상 CTG 해석에 유망한 대안을 제시합니다. 이 발견은 태아 모니터링을 위한 AI 방법론의 상대적 강점을 이해하고, 임신 전 관리에서의 AI 개발을 위한 기초를 마련합니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델(LLMs)은 전통적인 CTG 전용 아키텍처보다 우수한 성능을 보여줍니다.
- 2. CTG 해석은 주관적인 임상 해석에 크게 의존하여 진단 정확도에 변동이 발생할 수 있습니다.
- 3. 본 연구는 자동화된 antepartum CTG 분석을 위한 최신 AI 접근 방식의 첫 번째 종합 비교를 제공합니다.
- 4. 500개 이상의 다양한 CTG 기록을 평가하여 다양한 모델링 패러다임에 대한 성능 벤치마크를 제공합니다.
- 5. 연구 결과는 태아 모니터링 응용 프로그램을 위한 다양한 AI 방법론의 상대적 강점에 대한 중요한 통찰력을 제공합니다.


---

*Generated on 2025-09-24 14:44:47*