---
keywords:
  - Medical Priority Fusion
  - Non-Invasive Prenatal Testing
  - Decision Tree
  - Naive Bayes
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17924
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:00:19.250525",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Medical Priority Fusion",
    "Non-Invasive Prenatal Testing",
    "Decision Tree",
    "Naive Bayes"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Medical Priority Fusion": 0.8,
    "Non-Invasive Prenatal Testing": 0.78,
    "Decision Tree": 0.82,
    "Naive Bayes": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Medical Priority Fusion",
        "canonical": "Medical Priority Fusion",
        "aliases": [
          "MPF"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework that resolves the trade-off between sensitivity and interpretability in medical diagnostics.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Non-Invasive Prenatal Testing",
        "canonical": "Non-Invasive Prenatal Testing",
        "aliases": [
          "NIPT"
        ],
        "category": "specific_connectable",
        "rationale": "Key application area for the proposed framework, relevant for linking to prenatal care topics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Decision Tree",
        "canonical": "Decision Tree",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "A fundamental component of the proposed framework, relevant for linking to rule-based logic systems.",
        "novelty_score": 0.4,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "Naive Bayes",
        "canonical": "Naive Bayes",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Integral to the fusion framework, providing probabilistic reasoning, useful for linking to probabilistic models.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "algorithm",
      "method",
      "performance",
      "framework"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Medical Priority Fusion",
      "resolved_canonical": "Medical Priority Fusion",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Non-Invasive Prenatal Testing",
      "resolved_canonical": "Non-Invasive Prenatal Testing",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Decision Tree",
      "resolved_canonical": "Decision Tree",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Naive Bayes",
      "resolved_canonical": "Naive Bayes",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Medical priority fusion: achieving dual optimization of sensitivity and interpretability in nipt anomaly detection

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17924.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17924](https://arxiv.org/abs/2509.17924)

## 🔗 유사한 논문
- [[2025-09-23/Interpretability-Aware Pruning for Efficient Medical Image Analysis_20250923|Interpretability-Aware Pruning for Efficient Medical Image Analysis]] (83.0% similar)
- [[2025-09-19/Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2_ Atypical Mitosis Classification_20250919|Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2: Atypical Mitosis Classification]] (82.6% similar)
- [[2025-09-22/FedHK-MVFC_ Federated Heat Kernel Multi-View Clustering_20250922|FedHK-MVFC: Federated Heat Kernel Multi-View Clustering]] (82.6% similar)
- [[2025-09-23/MRN_ Harnessing 2D Vision Foundation Models for Diagnosing Parkinson's Disease with Limited 3D MR Data_20250923|MRN: Harnessing 2D Vision Foundation Models for Diagnosing Parkinson's Disease with Limited 3D MR Data]] (82.1% similar)
- [[2025-09-23/Estimating Clinical Lab Test Result Trajectories from PPG using Physiological Foundation Model and Patient-Aware State Space Model -- a UNIPHY+ Approach_20250923|Estimating Clinical Lab Test Result Trajectories from PPG using Physiological Foundation Model and Patient-Aware State Space Model -- a UNIPHY+ Approach]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Decision Tree|Decision Tree]], [[keywords/Naive Bayes|Naive Bayes]]
**🔗 Specific Connectable**: [[keywords/Non-Invasive Prenatal Testing|Non-Invasive Prenatal Testing]]
**⚡ Unique Technical**: [[keywords/Medical Priority Fusion|Medical Priority Fusion]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17924v1 Announce Type: new 
Abstract: Clinical machine learning faces a critical dilemma in high-stakes medical applications: algorithms achieving optimal diagnostic performance typically sacrifice the interpretability essential for physician decision-making, while interpretable methods compromise sensitivity in complex scenarios. This paradox becomes particularly acute in non-invasive prenatal testing (NIPT), where missed chromosomal abnormalities carry profound clinical consequences yet regulatory frameworks mandate explainable AI systems. We introduce Medical Priority Fusion (MPF), a constrained multi-objective optimization framework that resolves this fundamental trade-off by systematically integrating Naive Bayes probabilistic reasoning with Decision Tree rule-based logic through mathematically-principled weighted fusion under explicit medical constraints. Rigorous validation on 1,687 real-world NIPT samples characterized by extreme class imbalance (43.4:1 normal-to-abnormal ratio) employed stratified 5-fold cross-validation with comprehensive ablation studies and statistical hypothesis testing using McNemar's paired comparisons. MPF achieved simultaneous optimization of dual objectives: 89.3% sensitivity (95% CI: 83.9-94.7%) with 80% interpretability score, significantly outperforming individual algorithms (McNemar's test, p < 0.001). The optimal fusion configuration achieved Grade A clinical deployment criteria with large effect size (d = 1.24), establishing the first clinically-deployable solution that maintains both diagnostic accuracy and decision transparency essential for prenatal care. This work demonstrates that medical-constrained algorithm fusion can resolve the interpretability-performance trade-off, providing a mathematical framework for developing high-stakes medical decision support systems that meet both clinical efficacy and explainability requirements.

## 📝 요약

이 논문은 비침습적 산전 검사(NIPT)에서 해석 가능성과 진단 성능 간의 딜레마를 해결하기 위해 Medical Priority Fusion(MPF)이라는 다목적 최적화 프레임워크를 제안합니다. MPF는 나이브 베이즈 확률 추론과 의사결정 나무 규칙 기반 논리를 의료 제약 하에 수학적으로 융합하여 이 문제를 해결합니다. 1,687개의 실제 NIPT 샘플을 사용한 검증 결과, MPF는 89.3%의 민감도와 80%의 해석 가능성을 동시에 달성했으며, 이는 기존 알고리즘보다 우수한 성능을 보였습니다. 이 연구는 임상적 효능과 설명 가능성을 모두 충족하는 고위험 의료 의사결정 지원 시스템 개발을 위한 수학적 기반을 제공합니다.

## 🎯 주요 포인트

- 1. 의료 분야의 기계 학습은 진단 성능과 해석 가능성 간의 딜레마에 직면해 있으며, 이는 비침습적 산전 검사(NIPT)에서 특히 두드러진다.
- 2. Medical Priority Fusion(MPF)은 나이브 베이즈 확률 추론과 의사 결정 트리 규칙 기반 논리를 융합하여 이 딜레마를 해결하는 최적화 프레임워크를 제안한다.
- 3. MPF는 1,687개의 실제 NIPT 샘플을 통해 89.3%의 민감도와 80%의 해석 가능성 점수를 동시에 최적화하여 개별 알고리즘을 능가했다.
- 4. 최적의 융합 구성은 임상 배포 기준을 충족하며, 진단 정확성과 의사 결정 투명성을 유지하는 최초의 임상 배포 가능한 솔루션을 제공한다.
- 5. 본 연구는 해석 가능성과 성능 간의 트레이드오프를 해결할 수 있는 수학적 프레임워크를 제시하여, 고위험 의료 의사 결정 지원 시스템 개발에 기여한다.


---

*Generated on 2025-09-24 02:00:19*