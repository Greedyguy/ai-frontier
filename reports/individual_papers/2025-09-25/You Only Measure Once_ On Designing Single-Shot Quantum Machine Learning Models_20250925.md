---
keywords:
  - Quantum Machine Learning
  - Single-Shot Inference
  - Probability Aggregation
  - Depolarizing Channels
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.20090
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:44:43.406083",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Quantum Machine Learning",
    "Single-Shot Inference",
    "Probability Aggregation",
    "Depolarizing Channels"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Quantum Machine Learning": 0.78,
    "Single-Shot Inference": 0.8,
    "Probability Aggregation": 0.77,
    "Depolarizing Channels": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Quantum Machine Learning",
        "canonical": "Quantum Machine Learning",
        "aliases": [
          "QML"
        ],
        "category": "broad_technical",
        "rationale": "Quantum Machine Learning is a core topic of the paper and connects to broader discussions in machine learning and quantum computing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Single-Shot Inference",
        "canonical": "Single-Shot Inference",
        "aliases": [
          "Single Measurement Inference"
        ],
        "category": "unique_technical",
        "rationale": "Single-Shot Inference is a novel concept introduced in the paper, emphasizing reduced measurement requirements in QML.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Probability Aggregation Mechanism",
        "canonical": "Probability Aggregation",
        "aliases": [
          "Aggregation Mechanism"
        ],
        "category": "unique_technical",
        "rationale": "This mechanism is a unique contribution of the paper, offering a new approach to inference in QML.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      },
      {
        "surface": "Depolarizing Channels",
        "canonical": "Depolarizing Channels",
        "aliases": [
          "Quantum Noise Channels"
        ],
        "category": "specific_connectable",
        "rationale": "Depolarizing Channels are relevant to quantum computing and are crucial for understanding the paper's experimental setup.",
        "novelty_score": 0.52,
        "connectivity_score": 0.79,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
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
      "candidate_surface": "Quantum Machine Learning",
      "resolved_canonical": "Quantum Machine Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Single-Shot Inference",
      "resolved_canonical": "Single-Shot Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Probability Aggregation Mechanism",
      "resolved_canonical": "Probability Aggregation",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Depolarizing Channels",
      "resolved_canonical": "Depolarizing Channels",
      "decision": "linked",
      "scores": {
        "novelty": 0.52,
        "connectivity": 0.79,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# You Only Measure Once: On Designing Single-Shot Quantum Machine Learning Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20090.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.20090](https://arxiv.org/abs/2509.20090)

## 🔗 유사한 논문
- [[2025-09-17/Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment_20250917|Hybrid Quantum-Classical Neural Networks for Few-Shot Credit Risk Assessment]] (85.4% similar)
- [[2025-09-25/Quantum-Classical Hybrid Quantized Neural Network_20250925|Quantum-Classical Hybrid Quantized Neural Network]] (83.4% similar)
- [[2025-09-22/Double descent in quantum kernel methods_20250922|Double descent in quantum kernel methods]] (83.1% similar)
- [[2025-09-24/Re-uploading quantum data_ A universal function approximator for quantum inputs_20250924|Re-uploading quantum data: A universal function approximator for quantum inputs]] (83.0% similar)
- [[2025-09-17/Learning quantum many-body data locally_ A provably scalable framework_20250917|Learning quantum many-body data locally: A provably scalable framework]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Quantum Machine Learning|Quantum Machine Learning]]
**🔗 Specific Connectable**: [[keywords/Depolarizing Channels|Depolarizing Channels]]
**⚡ Unique Technical**: [[keywords/Single-Shot Inference|Single-Shot Inference]], [[keywords/Probability Aggregation|Probability Aggregation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20090v1 Announce Type: new 
Abstract: Quantum machine learning (QML) models conventionally rely on repeated measurements (shots) of observables to obtain reliable predictions. This dependence on large shot budgets leads to high inference cost and time overhead, which is particularly problematic as quantum hardware access is typically priced proportionally to the number of shots. In this work we propose You Only Measure Once (Yomo), a simple yet effective design that achieves accurate inference with dramatically fewer measurements, down to the single-shot regime. Yomo replaces Pauli expectation-value outputs with a probability aggregation mechanism and introduces loss functions that encourage sharp predictions. Our theoretical analysis shows that Yomo avoids the shot-scaling limitations inherent to expectation-based models, and our experiments on MNIST and CIFAR-10 confirm that Yomo consistently outperforms baselines across different shot budgets and under simulations with depolarizing channels. By enabling accurate single-shot inference, Yomo substantially reduces the financial and computational costs of deploying QML, thereby lowering the barrier to practical adoption of QML.

## 📝 요약

이 논문에서는 양자 기계 학습(QML) 모델의 예측 비용을 줄이기 위해 'You Only Measure Once (Yomo)'라는 새로운 방법을 제안합니다. 기존 QML 모델은 많은 측정 횟수(shot)에 의존해 높은 비용과 시간이 소요되는데, Yomo는 단일 측정만으로도 정확한 예측을 가능하게 합니다. 이는 파울리 기대값 대신 확률 집계 메커니즘을 사용하고, 예리한 예측을 유도하는 손실 함수를 도입함으로써 실현됩니다. 이론적 분석과 MNIST 및 CIFAR-10 데이터셋 실험을 통해 Yomo가 다양한 측정 예산과 디폴라라이징 채널 시뮬레이션에서 기존 모델보다 우수한 성능을 보임을 확인했습니다. Yomo는 단일 측정 예측을 가능하게 하여 QML의 재정적, 계산적 비용을 크게 줄이고, QML의 실용적 채택을 촉진합니다.

## 🎯 주요 포인트

- 1. 기존 양자 기계 학습 모델은 신뢰할 수 있는 예측을 위해 반복 측정에 의존하며, 이는 높은 추론 비용과 시간 소모를 초래합니다.
- 2. Yomo는 단일 측정으로도 정확한 추론을 가능하게 하여, 측정 횟수에 따른 비용 문제를 해결합니다.
- 3. Yomo는 파울리 기대값 출력을 확률 집계 메커니즘으로 대체하고, 예리한 예측을 유도하는 손실 함수를 도입합니다.
- 4. 이론적 분석에 따르면 Yomo는 기대 기반 모델의 측정 확장 한계를 피하며, 실험 결과 MNIST와 CIFAR-10 데이터셋에서 일관되게 우수한 성능을 보였습니다.
- 5. Yomo는 정확한 단일 측정 추론을 가능하게 하여, 양자 기계 학습의 실용적 채택을 위한 재정적 및 계산적 장벽을 낮춥니다.


---

*Generated on 2025-09-25 16:44:43*