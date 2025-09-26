---
keywords:
  - Infrared Small Target Detection
  - Deep Learning
  - Cross-dataset Evaluation
  - Systematic Error Analysis
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16888
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:37:35.166604",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Infrared Small Target Detection",
    "Deep Learning",
    "Cross-dataset Evaluation",
    "Systematic Error Analysis"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Infrared Small Target Detection": 0.85,
    "Deep Learning": 0.7,
    "Cross-dataset Evaluation": 0.78,
    "Systematic Error Analysis": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Infrared Small Target Detection",
        "canonical": "Infrared Small Target Detection",
        "aliases": [
          "IRSTD"
        ],
        "category": "unique_technical",
        "rationale": "This is the primary focus of the paper and represents a specific application area in computer vision.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Deep learning is a fundamental technique used in the advancements discussed in the paper.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Cross-dataset Evaluation",
        "canonical": "Cross-dataset Evaluation",
        "aliases": [
          "Dataset Generalization"
        ],
        "category": "unique_technical",
        "rationale": "This concept is crucial for understanding model robustness and is emphasized in the paper.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Error Analysis",
        "canonical": "Systematic Error Analysis",
        "aliases": [
          "Failure Mode Analysis"
        ],
        "category": "specific_connectable",
        "rationale": "Error analysis is vital for improving model performance and is a key contribution of the paper.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "performance scores",
      "evaluation protocols",
      "model capabilities"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Infrared Small Target Detection",
      "resolved_canonical": "Infrared Small Target Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Cross-dataset Evaluation",
      "resolved_canonical": "Cross-dataset Evaluation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Error Analysis",
      "resolved_canonical": "Systematic Error Analysis",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Rethinking Evaluation of Infrared Small Target Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16888.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16888](https://arxiv.org/abs/2509.16888)

## 🔗 유사한 논문
- [[2025-09-19/An Evaluation-Centric Paradigm for Scientific Visualization Agents_20250919|An Evaluation-Centric Paradigm for Scientific Visualization Agents]] (81.8% similar)
- [[2025-09-22/Towards Size-invariant Salient Object Detection_ A Generic Evaluation and Optimization Approach_20250922|Towards Size-invariant Salient Object Detection: A Generic Evaluation and Optimization Approach]] (81.3% similar)
- [[2025-09-23/Intention-aware Hierarchical Diffusion Model for Long-term Trajectory Anomaly Detection_20250923|Intention-aware Hierarchical Diffusion Model for Long-term Trajectory Anomaly Detection]] (81.3% similar)
- [[2025-09-18/Limitations of Public Chest Radiography Datasets for Artificial Intelligence_ Label Quality, Domain Shift, Bias and Evaluation Challenges_20250918|Limitations of Public Chest Radiography Datasets for Artificial Intelligence: Label Quality, Domain Shift, Bias and Evaluation Challenges]] (81.2% similar)
- [[2025-09-23/DisastIR_ A Comprehensive Information Retrieval Benchmark for Disaster Management_20250923|DisastIR: A Comprehensive Information Retrieval Benchmark for Disaster Management]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Systematic Error Analysis|Systematic Error Analysis]]
**⚡ Unique Technical**: [[keywords/Infrared Small Target Detection|Infrared Small Target Detection]], [[keywords/Cross-dataset Evaluation|Cross-dataset Evaluation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16888v1 Announce Type: new 
Abstract: As an essential vision task, infrared small target detection (IRSTD) has seen significant advancements through deep learning. However, critical limitations in current evaluation protocols impede further progress. First, existing methods rely on fragmented pixel- and target-level specific metrics, which fails to provide a comprehensive view of model capabilities. Second, an excessive emphasis on overall performance scores obscures crucial error analysis, which is vital for identifying failure modes and improving real-world system performance. Third, the field predominantly adopts dataset-specific training-testing paradigms, hindering the understanding of model robustness and generalization across diverse infrared scenarios. This paper addresses these issues by introducing a hybrid-level metric incorporating pixel- and target-level performance, proposing a systematic error analysis method, and emphasizing the importance of cross-dataset evaluation. These aim to offer a more thorough and rational hierarchical analysis framework, ultimately fostering the development of more effective and robust IRSTD models. An open-source toolkit has be released to facilitate standardized benchmarking.

## 📝 요약

이 논문은 적외선 소형 목표물 탐지(IRSTD) 분야에서 딥러닝을 활용한 발전을 다루며, 현재 평가 프로토콜의 한계를 지적합니다. 기존 방법은 파편화된 픽셀 및 목표물 수준의 지표에 의존하여 모델의 전반적인 능력을 평가하는 데 한계가 있으며, 전체 성능 점수에 치중하여 오류 분석이 부족합니다. 또한, 데이터셋에 특화된 훈련-테스트 방식은 모델의 견고성과 일반화 능력을 저해합니다. 이를 해결하기 위해, 이 논문은 픽셀 및 목표물 수준 성능을 통합한 하이브리드 지표, 체계적인 오류 분석 방법, 데이터셋 간 평가의 중요성을 강조합니다. 이러한 접근은 IRSTD 모델의 효과적이고 견고한 발전을 촉진하며, 표준화된 벤치마킹을 위한 오픈 소스 도구도 제공됩니다.

## 🎯 주요 포인트

- 1. 현재 평가 프로토콜의 한계로 인해 적외선 소형 목표물 탐지(IRSTD) 분야의 발전이 저해되고 있다.
- 2. 기존 방법들은 분절된 픽셀 및 목표물 수준의 특정 지표에 의존하여 모델의 전반적인 능력을 포괄적으로 평가하지 못한다.
- 3. 전체 성능 점수에 대한 과도한 강조는 오류 분석을 가리며, 이는 실패 모드를 식별하고 실제 시스템 성능을 개선하는 데 필수적이다.
- 4. 데이터셋에 특화된 훈련-테스트 패러다임은 다양한 적외선 시나리오에서 모델의 견고성과 일반화 능력을 이해하는 데 방해가 된다.
- 5. 이 논문은 픽셀 및 목표물 수준의 성능을 통합한 하이브리드 수준의 지표를 도입하고, 체계적인 오류 분석 방법과 교차 데이터셋 평가의 중요성을 강조한다.


---

*Generated on 2025-09-24 04:37:35*