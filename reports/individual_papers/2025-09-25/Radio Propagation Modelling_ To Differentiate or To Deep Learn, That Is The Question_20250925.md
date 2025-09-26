---
keywords:
  - Differentiable Ray Tracing
  - Deep Learning
  - Radio Propagation Modelling
  - Mobile Network Operators
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19337
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:26:20.081850",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Differentiable Ray Tracing",
    "Deep Learning",
    "Radio Propagation Modelling",
    "Mobile Network Operators"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Differentiable Ray Tracing": 0.78,
    "Deep Learning": 0.85,
    "Radio Propagation Modelling": 0.77,
    "Mobile Network Operators": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Differentiable Ray Tracing",
        "canonical": "Differentiable Ray Tracing",
        "aliases": [
          "Differentiable Ray-Tracing"
        ],
        "category": "unique_technical",
        "rationale": "This term represents a novel approach in radio propagation modeling, distinct from conventional methods, and is central to the paper's findings.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Deep Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational technology discussed in the paper, providing a comparative baseline for differentiable ray tracing.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Radio Propagation Modelling",
        "canonical": "Radio Propagation Modelling",
        "aliases": [
          "Radio Propagation Modeling"
        ],
        "category": "unique_technical",
        "rationale": "This is a key domain-specific term that encapsulates the primary focus of the research, linking to broader wireless communication studies.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Mobile Network Operators",
        "canonical": "Mobile Network Operators",
        "aliases": [
          "MNOs"
        ],
        "category": "specific_connectable",
        "rationale": "MNOs are the primary stakeholders impacted by the research, providing a practical context for the study's implications.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "real-world data",
      "production-grade networks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Differentiable Ray Tracing",
      "resolved_canonical": "Differentiable Ray Tracing",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Deep Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Radio Propagation Modelling",
      "resolved_canonical": "Radio Propagation Modelling",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Mobile Network Operators",
      "resolved_canonical": "Mobile Network Operators",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Radio Propagation Modelling: To Differentiate or To Deep Learn, That Is The Question

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19337.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19337](https://arxiv.org/abs/2509.19337)

## 🔗 유사한 논문
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (81.3% similar)
- [[2025-09-24/Accurate and Efficient Prediction of Wi-Fi Link Quality Based on Machine Learning_20250924|Accurate and Efficient Prediction of Wi-Fi Link Quality Based on Machine Learning]] (81.2% similar)
- [[2025-09-19/Improving Internet Traffic Matrix Prediction via Time Series Clustering_20250919|Improving Internet Traffic Matrix Prediction via Time Series Clustering]] (81.2% similar)
- [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE: Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (81.1% similar)
- [[2025-09-22/Interpretable Network-assisted Random Forest+_20250922|Interpretable Network-assisted Random Forest+]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Mobile Network Operators|Mobile Network Operators]]
**⚡ Unique Technical**: [[keywords/Differentiable Ray Tracing|Differentiable Ray Tracing]], [[keywords/Radio Propagation Modelling|Radio Propagation Modelling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19337v1 Announce Type: cross 
Abstract: Differentiable ray tracing has recently challenged the status quo in radio propagation modelling and digital twinning. Promising unprecedented speed and the ability to learn from real-world data, it offers a real alternative to conventional deep learning (DL) models. However, no experimental evaluation on production-grade networks has yet validated its assumed scalability or practical benefits. This leaves mobile network operators (MNOs) and the research community without clear guidance on its applicability. In this paper, we fill this gap by employing both differentiable ray tracing and DL models to emulate radio coverage using extensive real-world data collected from the network of a major MNO, covering 13 cities and more than 10,000 antennas. Our results show that, while differentiable ray-tracing simulators have contributed to reducing the efficiency-accuracy gap, they struggle to generalize from real-world data at a large scale, and they remain unsuitable for real-time applications. In contrast, DL models demonstrate higher accuracy and faster adaptation than differentiable ray-tracing simulators across urban, suburban, and rural deployments, achieving accuracy gains of up to 3 dB. Our experimental results aim to provide timely insights into a fundamental open question with direct implications on the wireless ecosystem and future research.

## 📝 요약

이 논문은 차별 가능한 레이 트레이싱과 딥러닝(DL) 모델을 활용하여 대규모 이동통신망의 무선 커버리지를 모사하는 연구를 수행했습니다. 주요 통신사업자의 네트워크에서 수집한 데이터를 바탕으로 13개 도시와 10,000개 이상의 안테나를 분석했습니다. 연구 결과, 차별 가능한 레이 트레이싱은 효율성과 정확성 간의 격차를 줄이는 데 기여했지만, 대규모 실데이터에서 일반화하는 데 어려움을 겪었고 실시간 응용에는 부적합했습니다. 반면, DL 모델은 도시, 교외, 농촌 환경에서 더 높은 정확도와 빠른 적응성을 보여주었으며, 최대 3dB의 정확도 향상을 달성했습니다. 이 연구는 무선 생태계와 미래 연구에 중요한 통찰을 제공합니다.

## 🎯 주요 포인트

- 1. 미분 가능한 레이 트레이싱은 기존의 딥러닝 모델에 대한 대안으로 제시되었으나, 대규모 네트워크에서의 확장성이나 실질적인 이점은 아직 검증되지 않았다.
- 2. 본 연구에서는 주요 이동통신사의 네트워크 데이터를 활용하여 미분 가능한 레이 트레이싱과 딥러닝 모델을 비교 평가하였다.
- 3. 미분 가능한 레이 트레이싱 시뮬레이터는 효율성과 정확성 간의 격차를 줄이는 데 기여했으나, 대규모 데이터 일반화와 실시간 응용에는 부적합하다.
- 4. 딥러닝 모델은 도시, 교외, 농촌 지역에서 미분 가능한 레이 트레이싱 시뮬레이터보다 높은 정확도와 빠른 적응력을 보여주며, 최대 3 dB의 정확도 향상을 달성하였다.
- 5. 본 연구의 실험 결과는 무선 생태계와 미래 연구에 직접적인 영향을 미치는 근본적인 질문에 대한 시의적절한 통찰을 제공한다.


---

*Generated on 2025-09-25 15:26:20*