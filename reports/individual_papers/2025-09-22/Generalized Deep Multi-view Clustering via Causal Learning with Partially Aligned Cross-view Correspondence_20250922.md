---
keywords:
  - Multi-view Clustering
  - Causal Learning
  - Variational Auto-Encoder
  - Contrastive Regularization
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.16022
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:17:56.185277",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multi-view Clustering",
    "Causal Learning",
    "Variational Auto-Encoder",
    "Contrastive Regularization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multi-view Clustering": 0.8,
    "Causal Learning": 0.82,
    "Variational Auto-Encoder": 0.79,
    "Contrastive Regularization": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multi-view Clustering",
        "canonical": "Multi-view Clustering",
        "aliases": [
          "MVC"
        ],
        "category": "specific_connectable",
        "rationale": "Multi-view Clustering is central to the paper's methodology and connects to various clustering techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Causal Learning",
        "canonical": "Causal Learning",
        "aliases": [
          "Causal Inference"
        ],
        "category": "specific_connectable",
        "rationale": "Causal Learning is a key methodological approach in the paper, offering strong connections to causal inference studies.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.77,
        "link_intent_score": 0.82
      },
      {
        "surface": "Variational Auto-Encoder",
        "canonical": "Variational Auto-Encoder",
        "aliases": [
          "VAE"
        ],
        "category": "broad_technical",
        "rationale": "Variational Auto-Encoder is a widely used tool in deep learning, relevant for its role in feature extraction in the paper.",
        "novelty_score": 0.45,
        "connectivity_score": 0.82,
        "specificity_score": 0.65,
        "link_intent_score": 0.79
      },
      {
        "surface": "Contrastive Regularizer",
        "canonical": "Contrastive Regularization",
        "aliases": [
          "Contrastive Loss"
        ],
        "category": "unique_technical",
        "rationale": "Contrastive Regularizer is a unique technique in the paper for capturing sample correlations, enhancing clustering.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multi-view Clustering",
      "resolved_canonical": "Multi-view Clustering",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Causal Learning",
      "resolved_canonical": "Causal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.77,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Variational Auto-Encoder",
      "resolved_canonical": "Variational Auto-Encoder",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.82,
        "specificity": 0.65,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Contrastive Regularizer",
      "resolved_canonical": "Contrastive Regularization",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Generalized Deep Multi-view Clustering via Causal Learning with Partially Aligned Cross-view Correspondence

**Korean Title:** 부분적으로 정렬된 교차 뷰 대응을 통한 인과 학습을 이용한 일반화된 심층 다중 뷰 클러스터링

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16022.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.16022](https://arxiv.org/abs/2509.16022)

## 🔗 유사한 논문
- [[2025-09-17/Beyond Correlation_ Causal Multi-View Unsupervised Feature Selection Learning_20250917|Beyond Correlation: Causal Multi-View Unsupervised Feature Selection Learning]] (82.5% similar)
- [[2025-09-18/One-step Multi-view Clustering With Adaptive Low-rank Anchor-graph Learning_20250918|One-step Multi-view Clustering With Adaptive Low-rank Anchor-graph Learning]] (82.2% similar)
- [[2025-09-22/MoCA_ Multi-modal Cross-masked Autoencoder for Digital Health Measurements_20250922|MoCA: Multi-modal Cross-masked Autoencoder for Digital Health Measurements]] (80.7% similar)
- [[2025-09-19/MemEvo_ Memory-Evolving Incremental Multi-view Clustering_20250919|MemEvo: Memory-Evolving Incremental Multi-view Clustering]] (80.2% similar)
- [[2025-09-19/CausalPre_ Scalable and Effective Data Pre-processing for Causal Fairness_20250919|CausalPre: Scalable and Effective Data Pre-processing for Causal Fairness]] (79.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Variational Auto-Encoder|Variational Auto-Encoder]]
**🔗 Specific Connectable**: [[keywords/Multi-view Clustering|Multi-view Clustering]], [[keywords/Causal Learning|Causal Learning]]
**⚡ Unique Technical**: [[keywords/Contrastive Regularization|Contrastive Regularization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16022v1 Announce Type: new 
Abstract: Multi-view clustering (MVC) aims to explore the common clustering structure across multiple views. Many existing MVC methods heavily rely on the assumption of view consistency, where alignments for corresponding samples across different views are ordered in advance. However, real-world scenarios often present a challenge as only partial data is consistently aligned across different views, restricting the overall clustering performance. In this work, we consider the model performance decreasing phenomenon caused by data order shift (i.e., from fully to partially aligned) as a generalized multi-view clustering problem. To tackle this problem, we design a causal multi-view clustering network, termed CauMVC. We adopt a causal modeling approach to understand multi-view clustering procedure. To be specific, we formulate the partially aligned data as an intervention and multi-view clustering with partially aligned data as an post-intervention inference. However, obtaining invariant features directly can be challenging. Thus, we design a Variational Auto-Encoder for causal learning by incorporating an encoder from existing information to estimate the invariant features. Moreover, a decoder is designed to perform the post-intervention inference. Lastly, we design a contrastive regularizer to capture sample correlations. To the best of our knowledge, this paper is the first work to deal generalized multi-view clustering via causal learning. Empirical experiments on both fully and partially aligned data illustrate the strong generalization and effectiveness of CauMVC.

## 🔍 Abstract (한글 번역)

arXiv:2509.16022v1 발표 유형: 신규  
초록: 다중 시각 클러스터링(MVC)은 여러 시각에 걸쳐 공통의 클러스터링 구조를 탐색하는 것을 목표로 합니다. 기존의 많은 MVC 방법들은 시각 일관성 가정에 크게 의존하며, 이는 서로 다른 시각에서 대응되는 샘플의 정렬이 사전에 이루어지는 것을 의미합니다. 그러나 실제 시나리오에서는 서로 다른 시각에 걸쳐 일관되게 정렬된 데이터가 부분적으로만 존재하는 경우가 많아 전체적인 클러스터링 성능을 제한하는 도전 과제를 제시합니다. 본 연구에서는 데이터 순서 이동(즉, 완전히 정렬된 상태에서 부분적으로 정렬된 상태로의 이동)으로 인해 발생하는 모델 성능 저하 현상을 일반화된 다중 시각 클러스터링 문제로 고려합니다. 이 문제를 해결하기 위해 CauMVC라 불리는 인과 다중 시각 클러스터링 네트워크를 설계하였습니다. 우리는 다중 시각 클러스터링 절차를 이해하기 위해 인과 모델링 접근 방식을 채택하였습니다. 구체적으로, 부분적으로 정렬된 데이터를 개입으로, 부분적으로 정렬된 데이터와 함께하는 다중 시각 클러스터링을 개입 후 추론으로 공식화하였습니다. 그러나 불변 특징을 직접적으로 얻는 것은 도전적일 수 있습니다. 따라서 기존 정보로부터 인코더를 통합하여 불변 특징을 추정하는 인과 학습을 위한 변분 오토인코더를 설계하였습니다. 또한, 개입 후 추론을 수행하기 위한 디코더를 설계하였습니다. 마지막으로, 샘플 간 상관관계를 포착하기 위해 대조 정규화를 설계하였습니다. 우리가 아는 한, 이 논문은 인과 학습을 통해 일반화된 다중 시각 클러스터링을 다루는 첫 번째 연구입니다. 완전히 정렬된 데이터와 부분적으로 정렬된 데이터 모두에 대한 실험적 결과는 CauMVC의 강력한 일반화와 효과성을 보여줍니다.

## 📝 요약

이 논문은 다중 뷰 클러스터링(MVC)에서 데이터 정렬이 완전히 이루어지지 않은 경우에도 성능을 유지할 수 있는 인과적 다중 뷰 클러스터링 네트워크(CauMVC)를 제안합니다. 기존 MVC 방법은 뷰 간의 일관된 정렬에 의존하지만, 실제 환경에서는 부분적으로만 정렬된 데이터가 많아 성능이 저하됩니다. CauMVC는 부분 정렬 데이터를 개입으로 보고, 이를 기반으로 클러스터링을 수행합니다. 변이형 오토인코더를 활용하여 불변 특징을 추정하고, 대조 정규화를 통해 샘플 간 상관관계를 포착합니다. 실험 결과, CauMVC는 완전 및 부분 정렬 데이터 모두에서 뛰어난 일반화 성능을 보였습니다.

## 🎯 주요 포인트

- 1. 다중 뷰 클러스터링(MVC)은 여러 뷰에 걸쳐 공통의 클러스터링 구조를 탐색하는 것을 목표로 한다.
- 2. 기존 MVC 방법들은 주로 뷰 일관성 가정에 의존하지만, 실제 시나리오에서는 부분적으로만 정렬된 데이터가 존재하여 클러스터링 성능이 제한된다.
- 3. CauMVC는 부분적으로 정렬된 데이터를 개입으로 보고, 이를 통한 다중 뷰 클러스터링을 사후 개입 추론으로 모델링한다.
- 4. 변이형 오토인코더를 설계하여 불변 특징을 추정하고, 대조 정규화를 통해 샘플 간의 상관관계를 포착한다.
- 5. CauMVC는 인과 학습을 통해 일반화된 다중 뷰 클러스터링 문제를 해결한 최초의 연구로, 실험 결과 강력한 일반화와 효과성을 입증했다.


---

*Generated on 2025-09-23 12:17:56*