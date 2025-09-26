---
keywords:
  - Deep Learning
  - Traffic-Explainer
  - Network Traffic Classification
  - Mutual Information
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.18007
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:28:48.077240",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Traffic-Explainer",
    "Network Traffic Classification",
    "Mutual Information"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Traffic-Explainer": 0.8,
    "Network Traffic Classification": 0.78,
    "Mutual Information": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational technology in the paper, linking it to a wide range of related works.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Traffic-Explainer",
        "canonical": "Traffic-Explainer",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Traffic-Explainer is a novel framework introduced in this paper, central to its contributions.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Network Traffic Classification",
        "canonical": "Network Traffic Classification",
        "aliases": [
          "Traffic Classification"
        ],
        "category": "specific_connectable",
        "rationale": "This is a key application area of the paper, linking it to network analysis and security domains.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Mutual Information",
        "canonical": "Mutual Information",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Mutual Information is used as a core method for feature analysis, connecting to statistical learning techniques.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "model-agnostic",
      "input-perturbation"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Traffic-Explainer",
      "resolved_canonical": "Traffic-Explainer",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Network Traffic Classification",
      "resolved_canonical": "Network Traffic Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Mutual Information",
      "resolved_canonical": "Mutual Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Building Transparency in Deep Learning-Powered Network Traffic Classification: A Traffic-Explainer Framework

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18007.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.18007](https://arxiv.org/abs/2509.18007)

## 🔗 유사한 논문
- [[2025-09-19/Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (83.1% similar)
- [[2025-09-18/Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (82.8% similar)
- [[2025-09-22/Interpretable Network-assisted Random Forest+_20250922|Interpretable Network-assisted Random Forest+]] (82.7% similar)
- [[2025-09-22/Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction_20250922|Deformable Dynamic Convolution for Accurate yet Efficient Spatio-Temporal Traffic Prediction]] (82.0% similar)
- [[2025-09-23/BiLCNet _ BiLSTM-Conformer Network for Encrypted Traffic Classification with 5G SA Physical Channel Records_20250923|BiLCNet : BiLSTM-Conformer Network for Encrypted Traffic Classification with 5G SA Physical Channel Records]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Network Traffic Classification|Network Traffic Classification]], [[keywords/Mutual Information|Mutual Information]]
**⚡ Unique Technical**: [[keywords/Traffic-Explainer|Traffic-Explainer]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18007v1 Announce Type: cross 
Abstract: Recent advancements in deep learning have significantly enhanced the performance and efficiency of traffic classification in networking systems. However, the lack of transparency in their predictions and decision-making has made network operators reluctant to deploy DL-based solutions in production networks. To tackle this challenge, we propose Traffic-Explainer, a model-agnostic and input-perturbation-based traffic explanation framework. By maximizing the mutual information between predictions on original traffic sequences and their masked counterparts, Traffic-Explainer automatically uncovers the most influential features driving model predictions. Extensive experiments demonstrate that Traffic-Explainer improves upon existing explanation methods by approximately 42%. Practically, we further apply Traffic-Explainer to identify influential features and demonstrate its enhanced transparency across three critical tasks: application classification, traffic localization, and network cartography. For the first two tasks, Traffic-Explainer identifies the most decisive bytes that drive predicted traffic applications and locations, uncovering potential vulnerabilities and privacy concerns. In network cartography, Traffic-Explainer identifies submarine cables that drive the mapping of traceroute to physical path, enabling a traceroute-informed risk analysis.

## 📝 요약

최근 딥러닝의 발전은 네트워크 시스템에서의 트래픽 분류 성능과 효율성을 크게 향상시켰습니다. 그러나 예측의 투명성 부족으로 인해 네트워크 운영자들은 딥러닝 기반 솔루션의 실제 네트워크 적용을 꺼리고 있습니다. 이를 해결하기 위해, 우리는 Traffic-Explainer라는 모델 비종속적이고 입력 변형 기반의 트래픽 설명 프레임워크를 제안합니다. Traffic-Explainer는 원본 트래픽 시퀀스와 마스킹된 시퀀스 간의 상호 정보를 최대화하여 모델 예측에 영향을 미치는 주요 특징을 자동으로 식별합니다. 실험 결과, 기존 설명 방법보다 약 42% 개선된 성능을 보였습니다. Traffic-Explainer는 애플리케이션 분류, 트래픽 위치 파악, 네트워크 지도 작성의 세 가지 주요 작업에서 투명성을 향상시킵니다. 특히, 애플리케이션 분류와 트래픽 위치 파악에서 결정적인 바이트를 식별하여 잠재적 취약점과 개인정보 문제를 드러냅니다. 네트워크 지도 작성에서는 트레이서라우트의 물리적 경로 매핑을 주도하는 해저 케이블을 식별하여 위험 분석을 가능하게 합니다.

## 🎯 주요 포인트

- 1. 최근 딥러닝의 발전은 네트워크 시스템에서 트래픽 분류의 성능과 효율성을 크게 향상시켰습니다.
- 2. Traffic-Explainer는 모델에 구애받지 않는 입력 변형 기반의 트래픽 설명 프레임워크로, 예측의 투명성을 높입니다.
- 3. Traffic-Explainer는 기존 설명 방법보다 약 42% 향상된 성능을 보이며, 중요한 특징을 자동으로 식별합니다.
- 4. 이 프레임워크는 애플리케이션 분류, 트래픽 지역화, 네트워크 지도 작성 등 세 가지 주요 작업에서 투명성을 증대시킵니다.
- 5. 네트워크 지도 작성에서는 트래픽 경로를 물리적 경로로 매핑하는 데 중요한 해저 케이블을 식별하여 위험 분석을 가능하게 합니다.


---

*Generated on 2025-09-24 02:28:48*