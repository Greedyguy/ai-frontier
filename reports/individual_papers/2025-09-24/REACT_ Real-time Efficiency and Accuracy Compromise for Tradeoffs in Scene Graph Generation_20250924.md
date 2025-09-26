<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:25:57.785533",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Scene Graph Generation",
    "REACT",
    "Graph Neural Network",
    "Object Detection",
    "Relation Prediction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Scene Graph Generation": 0.78,
    "REACT": 0.82,
    "Graph Neural Network": 0.75,
    "Object Detection": 0.7,
    "Relation Prediction": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Scene Graph Generation",
        "canonical": "Scene Graph Generation",
        "aliases": [
          "SGG"
        ],
        "category": "unique_technical",
        "rationale": "Scene Graph Generation is central to the paper's contribution and links to graph-based visual tasks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Real-time Efficiency and Accuracy Compromise for Tradeoffs",
        "canonical": "REACT",
        "aliases": [
          "Real-time Efficiency and Accuracy Compromise"
        ],
        "category": "unique_technical",
        "rationale": "REACT is the novel architecture proposed, crucial for understanding the paper's unique contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.82
      },
      {
        "surface": "Graph Neural Network",
        "canonical": "Graph Neural Network",
        "aliases": [
          "GNN"
        ],
        "category": "specific_connectable",
        "rationale": "Graph Neural Networks are relevant to the graph-based structure of Scene Graph Generation.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      },
      {
        "surface": "Object Detection",
        "canonical": "Object Detection",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Object Detection is a key component of the Scene Graph Generation process.",
        "novelty_score": 0.3,
        "connectivity_score": 0.8,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Relation Prediction",
        "canonical": "Relation Prediction",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Relation Prediction is a critical aspect of Scene Graph Generation, directly addressed by the paper.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Scene Graph Generation",
      "resolved_canonical": "Scene Graph Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Real-time Efficiency and Accuracy Compromise for Tradeoffs",
      "resolved_canonical": "REACT",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Graph Neural Network",
      "resolved_canonical": "Graph Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Object Detection",
      "resolved_canonical": "Object Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.8,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Relation Prediction",
      "resolved_canonical": "Relation Prediction",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# REACT: Real-time Efficiency and Accuracy Compromise for Tradeoffs in Scene Graph Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2405.16116.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2405.16116](https://arxiv.org/abs/2405.16116)

## 🔗 유사한 논문
- [[2025-09-22/Schreier-Coset Graph Propagation_20250922|Schreier-Coset Graph Propagation]] (82.0% similar)
- [[2025-09-23/CGTGait_ Collaborative Graph and Transformer for Gait Emotion Recognition_20250923|CGTGait: Collaborative Graph and Transformer for Gait Emotion Recognition]] (80.7% similar)
- [[2025-09-23/Neural-MMGS_ Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction_20250923|Neural-MMGS: Multi-modal Neural Gaussian Splats for Large-Scale Scene Reconstruction]] (80.6% similar)
- [[2025-09-23/DiscoSG_ Towards Discourse-Level Text Scene Graph Parsing through Iterative Graph Refinement_20250923|DiscoSG: Towards Discourse-Level Text Scene Graph Parsing through Iterative Graph Refinement]] (79.9% similar)
- [[2025-09-22/MCGA_ Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention_20250922|MCGA: Mixture of Codebooks Hyperspectral Reconstruction via Grayscale-Aware Attention]] (79.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Object Detection|Object Detection]]
**🔗 Specific Connectable**: [[keywords/Graph Neural Network|Graph Neural Network]]
**⚡ Unique Technical**: [[keywords/Scene Graph Generation|Scene Graph Generation]], [[keywords/REACT|REACT]], [[keywords/Relation Prediction|Relation Prediction]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2405.16116v3 Announce Type: replace 
Abstract: Scene Graph Generation (SGG) is a task that encodes visual relationships between objects in images as graph structures. SGG shows significant promise as a foundational component for downstream tasks, such as reasoning for embodied agents. To enable real-time applications, SGG must address the trade-off between performance and inference speed. However, current methods tend to focus on one of the following: (1) improving relation prediction accuracy, (2) enhancing object detection accuracy, or (3) reducing latency, without aiming to balance all three objectives simultaneously. To address this limitation, we propose the Real-time Efficiency and Accuracy Compromise for Tradeoffs in Scene Graph Generation (REACT) architecture, which achieves the highest inference speed among existing SGG models, improving object detection accuracy without sacrificing relation prediction performance. Compared to state-of-the-art approaches, REACT is 2.7 times faster and improves object detection accuracy by 58\%. Furthermore, our proposal significantly reduces model size, with an average of 5.5x fewer parameters. The code is available at https://github.com/Maelic/SGG-Benchmark

## 📝 요약

이 논문은 이미지 내 객체 간의 시각적 관계를 그래프 구조로 인코딩하는 작업인 장면 그래프 생성(SGG)에 대해 다룹니다. SGG는 실시간 응용 프로그램을 위해 성능과 추론 속도 간의 균형을 맞춰야 하는데, 기존 방법들은 관계 예측 정확도, 객체 탐지 정확도, 지연 시간 중 하나에만 집중하는 경향이 있습니다. 이를 해결하기 위해 제안된 REACT 아키텍처는 기존 SGG 모델 중 가장 빠른 추론 속도를 자랑하며, 객체 탐지 정확도를 향상시키면서도 관계 예측 성능을 유지합니다. REACT는 최신 기법 대비 2.7배 빠르고 객체 탐지 정확도를 58% 향상시켰으며, 모델 크기도 평균 5.5배 줄였습니다. 코드는 https://github.com/Maelic/SGG-Benchmark에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. 장면 그래프 생성(SGG)은 이미지 내 객체 간의 시각적 관계를 그래프 구조로 인코딩하는 작업이다.
- 2. SGG는 성능과 추론 속도 간의 균형을 맞추는 것이 중요하지만, 현재 방법들은 주로 관계 예측 정확성, 객체 탐지 정확성, 지연 시간 감소 중 하나에만 집중한다.
- 3. REACT 아키텍처는 기존 SGG 모델 중 가장 빠른 추론 속도를 달성하며, 객체 탐지 정확성을 향상시키면서 관계 예측 성능을 유지한다.
- 4. REACT는 최신 기술 대비 2.7배 빠르고 객체 탐지 정확성을 58% 향상시킨다.
- 5. 제안된 모델은 평균적으로 5.5배 적은 파라미터를 사용하여 모델 크기를 크게 줄인다.


---

*Generated on 2025-09-24 16:25:57*