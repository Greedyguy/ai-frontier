---
keywords:
  - Anomalous Sound Detection
  - Domain-Adaptive Pre-trained Model
  - Hierarchical Clustering
  - Supervised Fine-Tuning
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.12845
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T10:14:02.080047",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Anomalous Sound Detection",
    "Domain-Adaptive Pre-trained Model",
    "Hierarchical Clustering",
    "Supervised Fine-Tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Anomalous Sound Detection": 0.8,
    "Domain-Adaptive Pre-trained Model": 0.75,
    "Hierarchical Clustering": 0.7,
    "Supervised Fine-Tuning": 0.65
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Anomalous Sound Detection",
        "canonical": "Anomalous Sound Detection",
        "aliases": [
          "ASD"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific task within sound analysis that benefits from linking to related anomaly detection research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "domain-adaptive pre-trained model",
        "canonical": "Domain-Adaptive Pre-trained Model",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper's methodology and connects to domain adaptation and pre-training techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "hierarchical clustering",
        "canonical": "Hierarchical Clustering",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Hierarchical clustering is a well-known method in machine learning, useful for linking to clustering and unsupervised learning topics.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      },
      {
        "surface": "supervised fine-tuning",
        "canonical": "Supervised Fine-Tuning",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "This process is a common technique in adapting models, linking to broader machine learning practices.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.65
      }
    ],
    "ban_list_suggestions": [
      "machine attribute classification",
      "performance gains"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Anomalous Sound Detection",
      "resolved_canonical": "Anomalous Sound Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "domain-adaptive pre-trained model",
      "resolved_canonical": "Domain-Adaptive Pre-trained Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "hierarchical clustering",
      "resolved_canonical": "Hierarchical Clustering",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "supervised fine-tuning",
      "resolved_canonical": "Supervised Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.65
      }
    }
  ]
}
-->

# Improving Anomalous Sound Detection with Attribute-aware Representation from Domain-adaptive Pre-training

**Korean Title:** 도메인 적응 사전 훈련에서 속성 인식 표현을 활용한 이상 음향 탐지 개선

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.12845.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.12845](https://arxiv.org/abs/2509.12845)

## 🔗 유사한 논문
- [[2025-09-22/Contrastive Learning with Spectrum Information Augmentation in Abnormal Sound Detection_20250922|Contrastive Learning with Spectrum Information Augmentation in Abnormal Sound Detection]] (83.6% similar)
- [[2025-09-22/Domain-invariant feature learning in brain MR imaging for content-based image retrieval_20250922|Domain-invariant feature learning in brain MR imaging for content-based image retrieval]] (80.9% similar)
- [[2025-09-19/Multi-label Scene Classification for Autonomous Vehicles_ Acquiring and Accumulating Knowledge from Diverse Datasets_20250919|Multi-label Scene Classification for Autonomous Vehicles: Acquiring and Accumulating Knowledge from Diverse Datasets]] (80.3% similar)
- [[2025-09-22/Hybrid Temporal Differential Consistency Autoencoder for Efficient and Sustainable Anomaly Detection in Cyber-Physical Systems_20250922|Hybrid Temporal Differential Consistency Autoencoder for Efficient and Sustainable Anomaly Detection in Cyber-Physical Systems]] (80.2% similar)
- [[2025-09-22/DC-Mamba_ Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection_20250922|DC-Mamba: Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection]] (79.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Supervised Fine-Tuning|Supervised Fine-Tuning]]
**🔗 Specific Connectable**: [[keywords/Hierarchical Clustering|Hierarchical Clustering]]
**⚡ Unique Technical**: [[keywords/Anomalous Sound Detection|Anomalous Sound Detection]], [[keywords/Domain-Adaptive Pre-trained Model|Domain-Adaptive Pre-trained Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.12845v2 Announce Type: replace-cross 
Abstract: Anomalous Sound Detection (ASD) is often formulated as a machine attribute classification task, a strategy necessitated by the common scenario where only normal data is available for training. However, the exhaustive collection of machine attribute labels is laborious and impractical. To address the challenge of missing attribute labels, this paper proposes an agglomerative hierarchical clustering method for the assignment of pseudo-attribute labels using representations derived from a domain-adaptive pre-trained model, which are expected to capture machine attribute characteristics. We then apply model adaptation to this pre-trained model through supervised fine-tuning for machine attribute classification, resulting in a new state-of-the-art performance. Evaluation on the Detection and Classification of Acoustic Scenes and Events (DCASE) 2025 Challenge dataset demonstrates that our proposed approach yields significant performance gains, ultimately outperforming our previous top-ranking system in the challenge.

## 🔍 Abstract (한글 번역)

arXiv:2509.12845v2 발표 유형: 교차 교체  
초록: 비정상 소리 감지(Anomalous Sound Detection, ASD)는 종종 기계 속성 분류 작업으로 공식화되며, 이는 일반적으로 정상 데이터만 훈련에 사용할 수 있는 상황에서 필요로 하는 전략입니다. 그러나 기계 속성 레이블을 완전하게 수집하는 것은 번거롭고 비현실적입니다. 이러한 속성 레이블의 부재 문제를 해결하기 위해, 본 논문에서는 도메인 적응 사전 학습 모델에서 파생된 표현을 사용하여 의사 속성 레이블을 할당하는 응집적 계층적 군집화 방법을 제안합니다. 이러한 표현은 기계 속성 특성을 포착할 것으로 기대됩니다. 이후, 우리는 기계 속성 분류를 위한 지도 학습 미세 조정을 통해 이 사전 학습 모델에 모델 적응을 적용하여 새로운 최첨단 성능을 달성합니다. 2025년 음향 장면 및 이벤트 감지 및 분류(DCASE) 챌린지 데이터셋에 대한 평가 결과, 제안된 접근 방식이 상당한 성능 향상을 가져오며, 궁극적으로 챌린지에서 이전의 최고 순위 시스템을 능가하는 성과를 보였습니다.

## 📝 요약

이 논문은 비정상 소리 탐지(ASD)를 위한 새로운 접근법을 제안합니다. 일반적으로 ASD는 정상 데이터만을 사용하여 기계 속성 분류 작업으로 정의되지만, 속성 레이블 수집이 어렵습니다. 이를 해결하기 위해, 저자들은 도메인 적응 사전 학습 모델에서 파생된 표현을 활용하여 의사 속성 레이블을 할당하는 응집적 계층적 클러스터링 방법을 제안합니다. 이후, 이 모델을 기계 속성 분류를 위한 지도 학습으로 미세 조정하여 최첨단 성능을 달성했습니다. DCASE 2025 챌린지 데이터셋 평가 결과, 제안된 방법이 이전 시스템보다 성능이 크게 향상되었습니다.

## 🎯 주요 포인트

- 1. 비정상 음향 탐지는 일반적으로 기계 속성 분류 작업으로 공식화되며, 이는 정상 데이터만으로 훈련하는 일반적인 시나리오 때문이다.
- 2. 기계 속성 레이블의 포괄적인 수집은 번거롭고 비현실적이다.
- 3. 본 논문은 도메인 적응 사전 훈련 모델에서 파생된 표현을 사용하여 의사 속성 레이블을 할당하는 응집적 계층적 클러스터링 방법을 제안한다.
- 4. 제안된 방법은 DCASE 2025 챌린지 데이터셋 평가에서 성능 향상을 보여주며, 이전의 상위 시스템을 능가하는 결과를 얻었다.
- 5. 사전 훈련된 모델에 대한 감독된 미세 조정을 통해 기계 속성 분류를 위한 모델 적응을 수행하여 새로운 최첨단 성능을 달성했다.


---

*Generated on 2025-09-23 10:14:02*