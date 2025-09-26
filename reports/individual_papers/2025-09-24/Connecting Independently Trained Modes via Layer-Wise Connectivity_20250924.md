<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:24:01.890107",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mode Connectivity",
    "Neural Network",
    "Compact Convolutional Transformers",
    "Deep Layer Aggregation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mode Connectivity": 0.7,
    "Neural Network": 0.85,
    "Compact Convolutional Transformers": 0.78,
    "Deep Layer Aggregation": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "mode connectivity",
        "canonical": "Mode Connectivity",
        "aliases": [
          "low-loss paths",
          "continuous paths"
        ],
        "category": "unique_technical",
        "rationale": "Mode Connectivity is a novel concept that describes the phenomenon of connecting different neural network solutions, which is central to the paper's contributions.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "neural network models",
        "canonical": "Neural Network",
        "aliases": [
          "neural networks",
          "NN models"
        ],
        "category": "broad_technical",
        "rationale": "Neural Networks are the foundational technology discussed in the paper, providing context for the proposed connectivity methods.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Compact Convolutional Transformers",
        "canonical": "Compact Convolutional Transformers",
        "aliases": [
          "CCT"
        ],
        "category": "specific_connectable",
        "rationale": "Compact Convolutional Transformers represent a modern architecture that the paper's method applies to, highlighting its broader applicability.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Deep Layer Aggregation",
        "canonical": "Deep Layer Aggregation",
        "aliases": [
          "DLA"
        ],
        "category": "specific_connectable",
        "rationale": "Deep Layer Aggregation is a specific architecture that benefits from the proposed connectivity method, emphasizing its versatility.",
        "novelty_score": 0.68,
        "connectivity_score": 0.72,
        "specificity_score": 0.82,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "mode connectivity",
      "resolved_canonical": "Mode Connectivity",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "neural network models",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Compact Convolutional Transformers",
      "resolved_canonical": "Compact Convolutional Transformers",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Deep Layer Aggregation",
      "resolved_canonical": "Deep Layer Aggregation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.72,
        "specificity": 0.82,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Connecting Independently Trained Modes via Layer-Wise Connectivity

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2505.02604.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2505.02604](https://arxiv.org/abs/2505.02604)

## 🔗 유사한 논문
- [[2025-09-22/Incorporating Visual Cortical Lateral Connection Properties into CNN_ Recurrent Activation and Excitatory-Inhibitory Separation_20250922|Incorporating Visual Cortical Lateral Connection Properties into CNN: Recurrent Activation and Excitatory-Inhibitory Separation]] (81.1% similar)
- [[2025-09-23/Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs_20250923|Neuro-inspired Ensemble-to-Ensemble Communication Primitives for Sparse and Efficient ANNs]] (80.4% similar)
- [[2025-09-23/Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks_20250923|Dynamical Low-Rank Compression of Neural Networks with Robustness under Adversarial Attacks]] (80.3% similar)
- [[2025-09-19/Superpose Task-specific Features for Model Merging_20250919|Superpose Task-specific Features for Model Merging]] (80.1% similar)
- [[2025-09-23/Can multimodal representation learning by alignment preserve modality-specific information?_20250923|Can multimodal representation learning by alignment preserve modality-specific information?]] (80.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Compact Convolutional Transformers|Compact Convolutional Transformers]], [[keywords/Deep Layer Aggregation|Deep Layer Aggregation]]
**⚡ Unique Technical**: [[keywords/Mode Connectivity|Mode Connectivity]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.02604v4 Announce Type: replace 
Abstract: Empirical and theoretical studies have shown that continuous low-loss paths can be constructed between independently trained neural network models. This phenomenon, known as mode connectivity, refers to the existence of such paths between distinct modes-i.e., well-trained solutions in parameter space. However, existing empirical methods are primarily effective for older and relatively simple architectures such as basic CNNs, VGG, and ResNet, raising concerns about their applicability to modern and structurally diverse models. In this work, we propose a new empirical algorithm for connecting independently trained modes that generalizes beyond traditional architectures and supports a broader range of networks, including MobileNet, ShuffleNet, EfficientNet, RegNet, Deep Layer Aggregation (DLA), and Compact Convolutional Transformers (CCT). In addition to broader applicability, the proposed method yields more consistent connectivity paths across independently trained mode pairs and supports connecting modes obtained with different training hyperparameters.

## 📝 요약

이 논문은 독립적으로 학습된 신경망 모델 간의 연속적인 저손실 경로를 구축할 수 있는 현상을 다루며, 이를 모드 연결성이라고 합니다. 기존 방법들은 주로 단순한 구조의 모델에만 적용 가능했으나, 본 연구에서는 MobileNet, ShuffleNet, EfficientNet 등 다양한 현대적 모델에도 적용 가능한 새로운 알고리즘을 제안합니다. 이 방법은 다양한 네트워크 구조와 서로 다른 학습 하이퍼파라미터로 얻어진 모드 간의 일관된 연결 경로를 제공합니다.

## 🎯 주요 포인트

- 1. 독립적으로 훈련된 신경망 모델 간의 연속적인 저손실 경로를 구축할 수 있는 모드 연결성 현상이 존재한다.
- 2. 기존의 경험적 방법은 주로 기본 CNN, VGG, ResNet과 같은 오래되고 비교적 단순한 아키텍처에 효과적이다.
- 3. 본 연구에서는 MobileNet, ShuffleNet, EfficientNet, RegNet, DLA, CCT 등 다양한 현대적 네트워크에 적용 가능한 새로운 경험적 알고리즘을 제안한다.
- 4. 제안된 방법은 서로 다른 훈련 하이퍼파라미터로 얻어진 모드를 연결할 수 있으며, 일관된 연결 경로를 제공한다.


---

*Generated on 2025-09-24 15:24:01*