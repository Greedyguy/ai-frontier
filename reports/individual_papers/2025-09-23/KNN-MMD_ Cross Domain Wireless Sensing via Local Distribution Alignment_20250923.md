---
keywords:
  - KNN-MMD
  - Domain Alignment
  - Channel State Information
  - Few-Shot Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2412.04783
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:41:58.805725",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "KNN-MMD",
    "Domain Alignment",
    "Channel State Information",
    "Few-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "KNN-MMD": 0.78,
    "Domain Alignment": 0.75,
    "Channel State Information": 0.72,
    "Few-Shot Learning": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "K-Nearest Neighbors Maximum Mean Discrepancy",
        "canonical": "KNN-MMD",
        "aliases": [
          "KNN-MMD",
          "K-Nearest Neighbors MMD"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel method introduced in the paper, offering a unique approach to cross-domain wireless sensing.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Domain Alignment",
        "canonical": "Domain Alignment",
        "aliases": [
          "DAL"
        ],
        "category": "specific_connectable",
        "rationale": "Domain Alignment is a key concept in cross-domain classification, relevant for linking with other domain adaptation techniques.",
        "novelty_score": 0.45,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Channel State Information",
        "canonical": "Channel State Information",
        "aliases": [
          "CSI"
        ],
        "category": "unique_technical",
        "rationale": "CSI is crucial for wireless sensing applications, providing a specific technical focus for linking with related sensing technologies.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Few-Shot Method",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-Shot",
          "Few-Shot Method"
        ],
        "category": "specific_connectable",
        "rationale": "Few-Shot Learning is a trending concept that enhances the paper's method by addressing data scarcity in cross-domain tasks.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method",
      "environment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "K-Nearest Neighbors Maximum Mean Discrepancy",
      "resolved_canonical": "KNN-MMD",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Domain Alignment",
      "resolved_canonical": "Domain Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Channel State Information",
      "resolved_canonical": "Channel State Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Few-Shot Method",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# KNN-MMD: Cross Domain Wireless Sensing via Local Distribution Alignment

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2412.04783.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2412.04783](https://arxiv.org/abs/2412.04783)

## 🔗 유사한 논문
- [[2025-09-23/Training-Free Label Space Alignment for Universal Domain Adaptation_20250923|Training-Free Label Space Alignment for Universal Domain Adaptation]] (82.5% similar)
- [[2025-09-22/Domain-invariant feature learning in brain MR imaging for content-based image retrieval_20250922|Domain-invariant feature learning in brain MR imaging for content-based image retrieval]] (81.2% similar)
- [[2025-09-19/Domain Adaptation for Ulcerative Colitis Severity Estimation Using Patient-Level Diagnoses_20250919|Domain Adaptation for Ulcerative Colitis Severity Estimation Using Patient-Level Diagnoses]] (81.1% similar)
- [[2025-09-22/Cross-Resolution SAR Target Detection Using Structural Hierarchy Adaptation and Reliable Adjacency Alignment_20250922|Cross-Resolution SAR Target Detection Using Structural Hierarchy Adaptation and Reliable Adjacency Alignment]] (81.0% similar)
- [[2025-09-22/Advances in Multimodal Adaptation and Generalization_ From Traditional Approaches to Foundation Models_20250922|Advances in Multimodal Adaptation and Generalization: From Traditional Approaches to Foundation Models]] (80.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Domain Alignment|Domain Alignment]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/KNN-MMD|KNN-MMD]], [[keywords/Channel State Information|Channel State Information]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.04783v4 Announce Type: replace-cross 
Abstract: Wireless sensing has recently found widespread applications in diverse environments, including homes, offices, and public spaces. By analyzing patterns in channel state information (CSI), it is possible to infer human actions for tasks such as person identification, gesture recognition, and fall detection. However, CSI is highly sensitive to environmental changes, where even minor alterations can significantly distort the CSI patterns. This sensitivity often leads to performance degradation or outright failure when applying wireless sensing models trained in one environment to another. To address this challenge, Domain Alignment (DAL) has been widely adopted for cross-domain classification tasks, as it focuses on aligning the global distributions of the source and target domains in feature space. Despite its popularity, DAL often neglects inter-category relationships, which can lead to misalignment between categories across domains, even when global alignment is achieved. To overcome these limitations, we propose K-Nearest Neighbors Maximum Mean Discrepancy (KNN-MMD), a novel few-shot method for cross-domain wireless sensing. Our approach begins by constructing a help set using KNN from the target domain, enabling local alignment between the source and target domains within each category using MMD. Additionally, we address a key instability issue commonly observed in cross-domain methods, where model performance fluctuates sharply between epochs. Further, most existing methods struggle to determine an optimal stopping point during training due to the absence of labeled data from the target domain. Our method resolves this by excluding the support set from the target domain during training and employing it as a validation set to determine the stopping criterion.The dataset and code are publicly available at https://github.com/RS2002/KNN-MMD .

## 📝 요약

이 논문은 무선 센싱의 환경 변화에 따른 성능 저하 문제를 해결하기 위해 K-Nearest Neighbors Maximum Mean Discrepancy (KNN-MMD)라는 새로운 방법을 제안합니다. 기존의 도메인 정렬(DAL) 방법은 전역적 분포 정렬에 중점을 두지만, 카테고리 간 관계를 간과하여 도메인 간 오분류가 발생할 수 있습니다. KNN-MMD는 대상 도메인에서 KNN을 사용해 도움 집합을 구성하고, 각 카테고리 내에서 소스와 대상 도메인의 지역적 정렬을 수행합니다. 또한, 모델 성능의 불안정성과 최적의 학습 종료 시점 결정 문제를 해결하기 위해 대상 도메인의 지원 집합을 검증 세트로 활용합니다. 데이터셋과 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 무선 센싱은 다양한 환경에서 인간 행동을 추론하는 데 사용되지만, 환경 변화에 민감하여 성능 저하가 발생할 수 있습니다.
- 2. 도메인 정렬(DAL)은 소스와 타겟 도메인의 전역 분포를 맞추는 데 중점을 두지만, 카테고리 간 관계를 간과할 수 있습니다.
- 3. K-최근접 이웃 최대 평균 차이(KNN-MMD)는 소수 샷 방법으로, 각 카테고리 내에서 소스와 타겟 도메인의 지역 정렬을 가능하게 합니다.
- 4. 제안된 방법은 타겟 도메인의 지원 세트를 검증 세트로 사용하여 최적의 학습 중단 시점을 결정합니다.
- 5. 데이터셋과 코드는 https://github.com/RS2002/KNN-MMD 에서 공개적으로 이용할 수 있습니다.


---

*Generated on 2025-09-24 00:41:58*