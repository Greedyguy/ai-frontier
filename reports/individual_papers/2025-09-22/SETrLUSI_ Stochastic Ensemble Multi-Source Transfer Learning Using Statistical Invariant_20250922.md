---
keywords:
  - Transfer Learning
  - Multi-Source Transfer Learning
  - Ensemble Learning
  - Statistical Invariant
category: cs.LG
publish_date: 2025-09-22
arxiv_id: 2509.15593
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:50:17.772117",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transfer Learning",
    "Multi-Source Transfer Learning",
    "Ensemble Learning",
    "Statistical Invariant"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transfer Learning": 0.78,
    "Multi-Source Transfer Learning": 0.82,
    "Ensemble Learning": 0.77,
    "Statistical Invariant": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "transfer learning",
        "canonical": "Transfer Learning",
        "aliases": [
          "domain adaptation",
          "knowledge transfer"
        ],
        "category": "broad_technical",
        "rationale": "Transfer Learning is a foundational concept that connects various domains and methods in machine learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "multi-source transfer learning",
        "canonical": "Multi-Source Transfer Learning",
        "aliases": [
          "multi-domain transfer",
          "multi-source adaptation"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a specific approach within transfer learning.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "ensemble learning framework",
        "canonical": "Ensemble Learning",
        "aliases": [
          "ensemble methods",
          "ensemble approach"
        ],
        "category": "specific_connectable",
        "rationale": "Ensemble Learning is a key technique that enhances model performance by combining multiple models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      },
      {
        "surface": "statistical invariant",
        "canonical": "Statistical Invariant",
        "aliases": [
          "SI",
          "statistical consistency"
        ],
        "category": "unique_technical",
        "rationale": "The concept of Statistical Invariant is novel and crucial for the proposed method in the paper.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance",
      "process",
      "framework"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "transfer learning",
      "resolved_canonical": "Transfer Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "multi-source transfer learning",
      "resolved_canonical": "Multi-Source Transfer Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "ensemble learning framework",
      "resolved_canonical": "Ensemble Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "statistical invariant",
      "resolved_canonical": "Statistical Invariant",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# SETrLUSI: Stochastic Ensemble Multi-Source Transfer Learning Using Statistical Invariant

**Korean Title:** SETrLUSI: 통계적 불변성을 활용한 확률적 앙상블 다중 소스 전이 학습

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15593.pdf)
**Category**: cs.LG
**Published**: 2025-09-22
**ArXiv ID**: [2509.15593](https://arxiv.org/abs/2509.15593)

## 🔗 유사한 논문
- [[2025-09-19/Select to Know_ An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering_20250919|Select to Know: An Internal-External Knowledge Self-Selection Framework for Domain-Specific Question Answering]] (80.6% similar)
- [[2025-09-22/TISDiSS_ A Training-Time and Inference-Time Scalable Framework for Discriminative Source Separation_20250922|TISDiSS: A Training-Time and Inference-Time Scalable Framework for Discriminative Source Separation]] (80.5% similar)
- [[2025-09-22/Boosting Active Learning with Knowledge Transfer_20250922|Boosting Active Learning with Knowledge Transfer]] (80.4% similar)
- [[2025-09-22/Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data_20250922|Efficient Long-Tail Learning in Latent Space by sampling Synthetic Data]] (79.7% similar)
- [[2025-09-19/CodeLSI_ Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning_20250919|CodeLSI: Leveraging Foundation Models for Automated Code Generation with Low-Rank Optimization and Domain-Specific Instruction Tuning]] (79.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transfer Learning|Transfer Learning]]
**🔗 Specific Connectable**: [[keywords/Ensemble Learning|Ensemble Learning]]
**⚡ Unique Technical**: [[keywords/Multi-Source Transfer Learning|Multi-Source Transfer Learning]], [[keywords/Statistical Invariant|Statistical Invariant]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15593v1 Announce Type: cross 
Abstract: In transfer learning, a source domain often carries diverse knowledge, and different domains usually emphasize different types of knowledge. Different from handling only a single type of knowledge from all domains in traditional transfer learning methods, we introduce an ensemble learning framework with a weak mode of convergence in the form of Statistical Invariant (SI) for multi-source transfer learning, formulated as Stochastic Ensemble Multi-Source Transfer Learning Using Statistical Invariant (SETrLUSI). The proposed SI extracts and integrates various types of knowledge from both source and target domains, which not only effectively utilizes diverse knowledge but also accelerates the convergence process. Further, SETrLUSI incorporates stochastic SI selection, proportional source domain sampling, and target domain bootstrapping, which improves training efficiency while enhancing model stability. Experiments show that SETrLUSI has good convergence and outperforms related methods with a lower time cost.

## 🔍 Abstract (한글 번역)

arXiv:2509.15593v1 발표 유형: 교차  
초록: 전이 학습에서 소스 도메인은 종종 다양한 지식을 포함하고 있으며, 서로 다른 도메인은 보통 서로 다른 유형의 지식을 강조합니다. 전통적인 전이 학습 방법에서 모든 도메인으로부터 단일 유형의 지식만을 처리하는 것과 달리, 우리는 다중 소스 전이 학습을 위한 통계 불변량(Statistical Invariant, SI)의 형태로 약한 수렴 모드를 갖춘 앙상블 학습 프레임워크를 도입합니다. 이는 통계 불변량을 사용한 확률적 앙상블 다중 소스 전이 학습(Stochastic Ensemble Multi-Source Transfer Learning Using Statistical Invariant, SETrLUSI)으로 공식화됩니다. 제안된 SI는 소스 및 타겟 도메인 모두에서 다양한 유형의 지식을 추출하고 통합하여 다양한 지식을 효과적으로 활용할 뿐만 아니라 수렴 과정을 가속화합니다. 또한, SETrLUSI는 확률적 SI 선택, 비례 소스 도메인 샘플링, 타겟 도메인 부트스트래핑을 포함하여 훈련 효율성을 개선하면서 모델 안정성을 향상시킵니다. 실험 결과, SETrLUSI는 우수한 수렴성을 보이며, 낮은 시간 비용으로 관련 방법들보다 뛰어난 성능을 발휘합니다.

## 📝 요약

이 논문은 전이 학습에서 다양한 지식을 효과적으로 활용하기 위해 다중 소스 전이 학습을 위한 통계적 불변량(SI)을 활용한 앙상블 학습 프레임워크(SETrLUSI)를 제안합니다. SI는 소스와 타겟 도메인에서 다양한 지식을 추출하고 통합하여 수렴 과정을 가속화합니다. 또한, 확률적 SI 선택, 비례적 소스 도메인 샘플링, 타겟 도메인 부트스트래핑을 통해 훈련 효율성과 모델 안정성을 향상시킵니다. 실험 결과, SETrLUSI는 우수한 수렴성을 보이며 관련 방법들보다 낮은 시간 비용으로 뛰어난 성능을 나타냅니다.

## 🎯 주요 포인트

- 1. SETrLUSI는 다중 소스 전이 학습을 위해 통계적 불변성을 활용한 앙상블 학습 프레임워크를 제안합니다.
- 2. 제안된 통계적 불변성은 소스와 타겟 도메인에서 다양한 지식을 추출하고 통합하여, 지식 활용을 극대화하고 수렴 과정을 가속화합니다.
- 3. SETrLUSI는 확률적 통계적 불변성 선택, 비례 소스 도메인 샘플링, 타겟 도메인 부트스트래핑을 포함하여 훈련 효율성을 개선하고 모델의 안정성을 향상시킵니다.
- 4. 실험 결과, SETrLUSI는 우수한 수렴성을 보이며 관련 방법들보다 낮은 시간 비용으로 뛰어난 성능을 발휘합니다.


---

*Generated on 2025-09-23 10:50:17*