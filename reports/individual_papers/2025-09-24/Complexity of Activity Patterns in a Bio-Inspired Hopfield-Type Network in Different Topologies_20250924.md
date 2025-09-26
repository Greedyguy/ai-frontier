<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:01:50.725367",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Scale-Free Network",
    "Temporal Complexity",
    "Random Network"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.8,
    "Scale-Free Network": 0.78,
    "Temporal Complexity": 0.7,
    "Random Network": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Hopfield network",
        "canonical": "Neural Network",
        "aliases": [
          "Hopfield-type network",
          "Hopfield model"
        ],
        "category": "broad_technical",
        "rationale": "Hopfield networks are a foundational concept in neural network models, providing a strong link to existing neural network discussions.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "scale-free network",
        "canonical": "Scale-Free Network",
        "aliases": [
          "scale-free topology",
          "hub-dominated network"
        ],
        "category": "specific_connectable",
        "rationale": "Scale-free networks are crucial for understanding complex network dynamics, linking to studies on network topology.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "temporal complexity",
        "canonical": "Temporal Complexity",
        "aliases": [
          "TC theory",
          "temporal dynamics"
        ],
        "category": "unique_technical",
        "rationale": "Temporal complexity is a unique concept in the study of neural dynamics, offering novel insights into network behavior.",
        "novelty_score": 0.65,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "random network topology",
        "canonical": "Random Network",
        "aliases": [
          "random topology",
          "random graph"
        ],
        "category": "specific_connectable",
        "rationale": "Random network topology provides a contrasting perspective to scale-free networks, enhancing discussions on network structures.",
        "novelty_score": 0.55,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "complex network theory",
      "global activation patterns"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Hopfield network",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "scale-free network",
      "resolved_canonical": "Scale-Free Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "temporal complexity",
      "resolved_canonical": "Temporal Complexity",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "random network topology",
      "resolved_canonical": "Random Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Complexity of Activity Patterns in a Bio-Inspired Hopfield-Type Network in Different Topologies

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18758.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18758](https://arxiv.org/abs/2509.18758)

## 🔗 유사한 논문
- [[2025-09-17/A Neural Network for the Identical Kuramoto Equation_ Architectural Considerations and Performance Evaluation_20250917|A Neural Network for the Identical Kuramoto Equation: Architectural Considerations and Performance Evaluation]] (79.6% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (79.5% similar)
- [[2025-09-23/Towards Quantifying the Hessian Structure of Neural Networks_20250923|Towards Quantifying the Hessian Structure of Neural Networks]] (79.4% similar)
- [[2025-09-23/Information-Theoretic Bounds and Task-Centric Learning Complexity for Real-World Dynamic Nonlinear Systems_20250923|Information-Theoretic Bounds and Task-Centric Learning Complexity for Real-World Dynamic Nonlinear Systems]] (78.6% similar)
- [[2025-09-17/Exploring Major Transitions in the Evolution of Biological Cognition With Artificial Neural Networks_20250917|Exploring Major Transitions in the Evolution of Biological Cognition With Artificial Neural Networks]] (78.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Scale-Free Network|Scale-Free Network]], [[keywords/Random Network|Random Network]]
**⚡ Unique Technical**: [[keywords/Temporal Complexity|Temporal Complexity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18758v1 Announce Type: cross 
Abstract: Neural network models capable of storing memory have been extensively studied in computer science and computational neuroscience. The Hopfield network is a prototypical example of a model designed for associative, or content-addressable, memory and has been analyzed in many forms. Further, ideas and methods from complex network theory have been incorporated into artificial neural networks and learning, emphasizing their structural properties. Nevertheless, the temporal dynamics also play a vital role in biological neural networks, whose temporal structure is a crucial feature to examine. Biological neural networks display complex intermittency and, thus, can be studied through the lens of the temporal complexity (TC) theory. The TC approach look at the metastability of self-organized states, characterized by a power-law decay in the inter-event time distribution and in the total activity distribution or a scaling behavior in the corresponding event-driven diffusion processes. In this study, we present a temporal complexity (TC) analysis of a biologically-inspired Hopfield-type neural network model. We conducted a comparative assessment between scale-free and random network topologies, with particular emphasis on their global activation patterns. Our parametric analysis revealed comparable dynamical behaviors across both neural network architectures. Furthermore, our investigation into temporal complexity characteristics uncovered that seemingly distinct dynamical patterns exhibit similar temporal complexity behaviors. In particular, similar power-law decay in the activity distribution and similar complexity levels are observed in both topologies, but with a much reduced noise in the scale-free topology. Notably, most of the complex dynamical profiles were consistently observed in scale-free network configurations, thus confirming the crucial role of hubs in neural network dynamics.

## 📝 요약

이 논문은 생물학적으로 영감을 받은 Hopfield 유형의 신경망 모델에 대한 시간 복잡성(TC) 분석을 수행했습니다. 연구는 스케일-프리 네트워크와 임의 네트워크의 전역 활성화 패턴을 비교 평가했으며, 두 네트워크 구조 모두 유사한 동적 행동을 보였습니다. 특히, 두 구조에서 활동 분포의 멱법칙 감소와 유사한 복잡성 수준이 관찰되었지만, 스케일-프리 구조에서는 잡음이 현저히 줄어들었습니다. 이 연구는 신경망 동역학에서 허브의 중요한 역할을 확인하며, 복잡한 동적 프로파일이 주로 스케일-프리 네트워크에서 일관되게 나타남을 보여줍니다.

## 🎯 주요 포인트

- 1. Hopfield 네트워크는 연상 기억을 위한 모델로, 다양한 형태로 분석되어 왔습니다.
- 2. 생물학적 신경망의 시간적 구조는 중요한 특징으로, 시간 복잡성(TC) 이론을 통해 연구될 수 있습니다.
- 3. 본 연구에서는 생물학적 영감을 받은 Hopfield 유형의 신경망 모델에 대한 시간 복잡성 분석을 수행했습니다.
- 4. 스케일-프리 및 랜덤 네트워크 토폴로지 간의 비교 평가를 통해 두 구조 모두 유사한 동적 행동을 보였습니다.
- 5. 스케일-프리 네트워크 구성에서 복잡한 동적 프로파일이 일관되게 관찰되었으며, 허브의 역할이 중요함을 확인했습니다.


---

*Generated on 2025-09-24 14:01:50*