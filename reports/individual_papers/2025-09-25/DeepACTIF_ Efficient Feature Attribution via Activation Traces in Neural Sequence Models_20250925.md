---
keywords:
  - DeepACTIF
  - Feature Attribution
  - LSTM
  - Biometric Data
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19362
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:29:58.370026",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "DeepACTIF",
    "Feature Attribution",
    "LSTM",
    "Biometric Data"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "DeepACTIF": 0.85,
    "Feature Attribution": 0.8,
    "LSTM": 0.82,
    "Biometric Data": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "DeepACTIF",
        "canonical": "DeepACTIF",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "DeepACTIF is a novel feature attribution method specifically designed for neural sequence models, making it a unique technical contribution.",
        "novelty_score": 0.95,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.85
      },
      {
        "surface": "feature attribution",
        "canonical": "Feature Attribution",
        "aliases": [
          "feature importance"
        ],
        "category": "broad_technical",
        "rationale": "Feature attribution is a fundamental concept in interpreting deep learning models, linking to various methods and applications.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "LSTM-based networks",
        "canonical": "LSTM",
        "aliases": [
          "Long Short-Term Memory"
        ],
        "category": "specific_connectable",
        "rationale": "LSTM is a widely used neural network architecture for sequence modeling, providing strong connectivity to time-series applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "biometric gaze datasets",
        "canonical": "Biometric Data",
        "aliases": [
          "gaze tracking"
        ],
        "category": "specific_connectable",
        "rationale": "Biometric data, particularly gaze tracking, is crucial for applications in healthcare and human-AI interaction, offering specific connectivity.",
        "novelty_score": 0.55,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
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
      "candidate_surface": "DeepACTIF",
      "resolved_canonical": "DeepACTIF",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "feature attribution",
      "resolved_canonical": "Feature Attribution",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "LSTM-based networks",
      "resolved_canonical": "LSTM",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "biometric gaze datasets",
      "resolved_canonical": "Biometric Data",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# DeepACTIF: Efficient Feature Attribution via Activation Traces in Neural Sequence Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19362.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19362](https://arxiv.org/abs/2509.19362)

## 🔗 유사한 논문
- [[2025-09-24/HadaSmileNet_ Hadamard fusion of handcrafted and deep-learning features for enhancing facial emotion recognition of genuine smiles_20250924|HadaSmileNet: Hadamard fusion of handcrafted and deep-learning features for enhancing facial emotion recognition of genuine smiles]] (81.8% similar)
- [[2025-09-23/Incorporating the Refractory Period into Spiking Neural Networks through Spike-Triggered Threshold Dynamics_20250923|Incorporating the Refractory Period into Spiking Neural Networks through Spike-Triggered Threshold Dynamics]] (81.5% similar)
- [[2025-09-23/AHA -- Predicting What Matters Next_ Online Highlight Detection Without Looking Ahead_20250923|AHA -- Predicting What Matters Next: Online Highlight Detection Without Looking Ahead]] (81.4% similar)
- [[2025-09-22/Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception_20250922|Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception]] (81.4% similar)
- [[2025-09-23/DynSTG-Mamba_ Dynamic Spatio-Temporal Graph Mamba with Cross-Graph Knowledge Distillation for Gait Disorders Recognition_20250923|DynSTG-Mamba: Dynamic Spatio-Temporal Graph Mamba with Cross-Graph Knowledge Distillation for Gait Disorders Recognition]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Feature Attribution|Feature Attribution]]
**🔗 Specific Connectable**: [[keywords/LSTM|LSTM]], [[keywords/Biometric Data|Biometric Data]]
**⚡ Unique Technical**: [[keywords/DeepACTIF|DeepACTIF]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19362v1 Announce Type: cross 
Abstract: Feature attribution is essential for interpreting deep learning models, particularly in time-series domains such as healthcare, biometrics, and human-AI interaction. However, standard attribution methods, such as Integrated Gradients or SHAP, are computationally intensive and not well-suited for real-time applications. We present DeepACTIF, a lightweight and architecture-aware feature attribution method that leverages internal activations of sequence models to estimate feature importance efficiently. Focusing on LSTM-based networks, we introduce an inverse-weighted aggregation scheme that emphasises stability and magnitude of activations across time steps. Our evaluation across three biometric gaze datasets shows that DeepACTIF not only preserves predictive performance under severe feature reduction (top 10% of features) but also significantly outperforms established methods, including SHAP, IG, and DeepLIFT, in terms of both accuracy and statistical robustness. Using Wilcoxon signed-rank tests and effect size analysis, we demonstrate that DeepACTIF yields more informative feature rankings with significantly lower error across all top-k conditions (10 - 40%). Our experiments demonstrate that DeepACTIF not only reduces computation time and memory usage by orders of magnitude but also preserves model accuracy when using only top-ranked features. That makes DeepACTIF a viable solution for real-time interpretability on edge devices such as mobile XR headsets or embedded health monitors.

## 📝 요약

DeepACTIF는 시퀀스 모델의 내부 활성화를 활용하여 효율적으로 특징 중요도를 추정하는 경량의 아키텍처 인식 특징 귀속 방법입니다. LSTM 기반 네트워크에 초점을 맞추어, 시간 단계에 걸쳐 활성화의 안정성과 크기를 강조하는 역가중 집계 방식을 도입했습니다. 세 가지 생체 인식 시선 데이터셋에서의 평가 결과, DeepACTIF는 예측 성능을 유지하면서도 기존 방법보다 높은 정확성과 통계적 견고성을 보여주었습니다. 또한, 계산 시간과 메모리 사용량을 크게 줄이면서도 상위 특징만을 사용하여 모델 정확성을 유지하여, 모바일 XR 헤드셋이나 임베디드 건강 모니터와 같은 엣지 디바이스에서 실시간 해석 가능성을 제공합니다.

## 🎯 주요 포인트

- 1. DeepACTIF는 경량화된 구조 인식 기능 귀속 방법으로, 시퀀스 모델의 내부 활성화를 활용하여 기능 중요성을 효율적으로 추정합니다.
- 2. LSTM 기반 네트워크에 초점을 맞춰, 시간 단계 전반에 걸쳐 활성화의 안정성과 크기를 강조하는 역가중 집계 방식을 도입했습니다.
- 3. DeepACTIF는 생체 인식 응시 데이터셋에서 예측 성능을 유지하면서도 SHAP, IG, DeepLIFT 등 기존 방법보다 정확성과 통계적 강건성에서 뛰어난 성능을 보였습니다.
- 4. Wilcoxon 부호 순위 검정과 효과 크기 분석을 통해, DeepACTIF가 모든 상위-k 조건에서 더 정보성 있는 기능 순위를 제공하며 오류가 현저히 낮음을 입증했습니다.
- 5. DeepACTIF는 계산 시간과 메모리 사용량을 대폭 줄이면서도 상위 순위 기능만 사용할 때 모델 정확성을 유지하여, 모바일 XR 헤드셋이나 임베디드 건강 모니터와 같은 엣지 디바이스에서 실시간 해석 가능성을 제공합니다.


---

*Generated on 2025-09-25 15:29:58*