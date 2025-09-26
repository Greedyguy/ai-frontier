<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:34:02.758378",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Latent Representation",
    "Multi-scale Modeling",
    "Deep Learning",
    "Shock-Induced Energy Localization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Latent Representation": 0.78,
    "Multi-scale Modeling": 0.82,
    "Deep Learning": 0.75,
    "Shock-Induced Energy Localization": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "latent representation",
        "canonical": "Latent Representation",
        "aliases": [
          "latent space",
          "latent variable"
        ],
        "category": "specific_connectable",
        "rationale": "Latent representations are crucial for connecting various scales in multi-scale modeling, enhancing the understanding of underlying dynamics.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "multi-scale modeling",
        "canonical": "Multi-scale Modeling",
        "aliases": [
          "multi-scale framework",
          "scale-bridging"
        ],
        "category": "unique_technical",
        "rationale": "Multi-scale modeling is a unique approach in physics and engineering for linking different scales, crucial for understanding complex systems.",
        "novelty_score": 0.72,
        "connectivity_score": 0.79,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "deep learning models",
        "canonical": "Deep Learning",
        "aliases": [
          "DL models"
        ],
        "category": "broad_technical",
        "rationale": "Deep learning is a foundational technology that supports the development of surrogate models in multi-scale frameworks.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "shock-induced energy localization",
        "canonical": "Shock-Induced Energy Localization",
        "aliases": [
          "energy localization",
          "shock dynamics"
        ],
        "category": "unique_technical",
        "rationale": "This specific phenomenon is central to the study, providing insights into the behavior of energetic materials under shock.",
        "novelty_score": 0.78,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "meso-scale",
      "micro-scale",
      "closure models"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "latent representation",
      "resolved_canonical": "Latent Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "multi-scale modeling",
      "resolved_canonical": "Multi-scale Modeling",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.79,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "deep learning models",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "shock-induced energy localization",
      "resolved_canonical": "Shock-Induced Energy Localization",
      "decision": "linked",
      "scores": {
        "novelty": 0.78,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Latent Representation Learning of Multi-scale Thermophysics: Application to Dynamics in Shocked Porous Energetic Material

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.12996.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2506.12996](https://arxiv.org/abs/2506.12996)

## 🔗 유사한 논문
- [[2025-09-22/StFT_ Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction_20250922|StFT: Spatio-temporal Fourier Transformer for Long-term Dynamics Prediction]] (84.6% similar)
- [[2025-09-22/Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media_20250922|Spatio-temporal, multi-field deep learning of shock propagation in meso-structured media]] (84.0% similar)
- [[2025-09-18/Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution_20250918|Physics-Informed GCN-LSTM Framework for Long-Term Forecasting of 2D and 3D Microstructure Evolution]] (82.0% similar)
- [[2025-09-18/Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model_20250918|Learning Mechanistic Subtypes of Neurodegeneration with a Physics-Informed Variational Autoencoder Mixture Model]] (81.4% similar)
- [[2025-09-24/Unveiling the Role of Learning Rate Schedules via Functional Scaling Laws_20250924|Unveiling the Role of Learning Rate Schedules via Functional Scaling Laws]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Latent Representation|Latent Representation]]
**⚡ Unique Technical**: [[keywords/Multi-scale Modeling|Multi-scale Modeling]], [[keywords/Shock-Induced Energy Localization|Shock-Induced Energy Localization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.12996v2 Announce Type: replace-cross 
Abstract: Coupling of physics across length and time scales plays an important role in the response of microstructured materials to external loads. In a multi-scale framework, unresolved (subgrid) meso-scale dynamics is upscaled to the homogenized (macro-scale) representation of the heterogeneous material through closure models. Deep learning models trained using meso-scale simulation data are now a popular route to assimilate such closure laws. However, meso-scale simulations are computationally taxing, posing practical challenges in training deep learning-based surrogate models from scratch. In this work, we investigate an alternative meta-learning approach motivated by the idea of tokenization in natural language processing. We show that one can learn a reduced representation of the micro-scale physics to accelerate the meso-scale learning process by tokenizing the meso-scale evolution of the physical fields involved in an archetypal, albeit complex, reactive dynamics problem, \textit{viz.}, shock-induced energy localization in a porous energetic material. A probabilistic latent representation of \textit{micro}-scale dynamics is learned as building blocks for \textit{meso}-scale dynamics. The \textit{meso-}scale latent dynamics model learns the correlation between neighboring building blocks by training over a small dataset of meso-scale simulations. We compare the performance of our model with a physics-aware recurrent convolutional neural network (PARC) trained only on the full meso-scale dataset. We demonstrate that our model can outperform PARC with scarce meso-scale data. The proposed approach accelerates the development of closure models by leveraging inexpensive micro-scale simulations and fast training over a small meso-scale dataset, and can be applied to a range of multi-scale modeling problems.

## 📝 요약

이 논문은 미세구조 재료의 외부 하중 반응을 다루는 다중 스케일 모델링에서, 메조 스케일의 동역학을 거시 스케일로 업스케일링하는 새로운 메타 학습 접근법을 제안합니다. 자연어 처리의 토큰화 개념을 활용하여, 복잡한 반응 동역학 문제에서 메조 스케일 물리장의 진화를 토큰화하여 미세 스케일 물리의 축소된 표현을 학습합니다. 이를 통해 메조 스케일 학습을 가속화하고, 적은 메조 스케일 데이터로도 기존의 물리 기반 신경망 모델(PARC)을 능가하는 성능을 보입니다. 이 방법은 저렴한 미세 스케일 시뮬레이션과 소규모 메조 스케일 데이터셋을 활용하여 폐쇄 모델 개발을 가속화할 수 있으며, 다양한 다중 스케일 모델링 문제에 적용 가능합니다.

## 🎯 주요 포인트

- 1. 물리학의 길이 및 시간 척도 간의 결합은 미세 구조 재료의 외부 하중 반응에 중요한 역할을 한다.
- 2. 심층 학습 모델은 중간 규모 시뮬레이션 데이터를 사용하여 클로저 법칙을 동화하는 인기 있는 방법이다.
- 3. 본 연구는 자연어 처리의 토큰화 아이디어에서 영감을 얻어 대안적인 메타 학습 접근법을 조사한다.
- 4. 미세 규모 물리학의 축소 표현을 학습하여 중간 규모 학습 과정을 가속화할 수 있음을 보여준다.
- 5. 제안된 접근법은 저렴한 미세 규모 시뮬레이션과 소규모 중간 규모 데이터셋을 활용하여 클로저 모델 개발을 가속화한다.


---

*Generated on 2025-09-24 15:34:02*