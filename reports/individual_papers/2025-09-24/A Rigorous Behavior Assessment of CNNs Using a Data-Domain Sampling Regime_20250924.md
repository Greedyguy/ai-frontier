<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:26:02.683067",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Data-Domain Sampling",
    "Visual Perception in Neural Networks",
    "Domain Shift"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Data-Domain Sampling": 0.7,
    "Visual Perception in Neural Networks": 0.77,
    "Domain Shift": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "CNNs",
        "canonical": "Neural Network",
        "aliases": [
          "Convolutional Neural Networks",
          "CNN"
        ],
        "category": "broad_technical",
        "rationale": "CNNs are a fundamental type of neural network used extensively in computer vision tasks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "data-domain sampling regime",
        "canonical": "Data-Domain Sampling",
        "aliases": [
          "sampling regime"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific technique introduced in the paper for assessing CNN behavior.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "graphic perception behaviors",
        "canonical": "Visual Perception in Neural Networks",
        "aliases": [
          "graphic perception",
          "visual perception"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding how neural networks perceive graphics is crucial for linking to computer vision research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "training-test distribution discrepancies",
        "canonical": "Domain Shift",
        "aliases": [
          "distribution discrepancies",
          "training-test shift"
        ],
        "category": "specific_connectable",
        "rationale": "Domain shift is a key concept in understanding model generalization and robustness.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "trials",
      "participants",
      "registration",
      "code"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "CNNs",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "data-domain sampling regime",
      "resolved_canonical": "Data-Domain Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "graphic perception behaviors",
      "resolved_canonical": "Visual Perception in Neural Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "training-test distribution discrepancies",
      "resolved_canonical": "Domain Shift",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# A Rigorous Behavior Assessment of CNNs Using a Data-Domain Sampling Regime

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2507.03866.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2507.03866](https://arxiv.org/abs/2507.03866)

## 🔗 유사한 논문
- [[2025-09-23/R-Net_ A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration_20250923|R-Net: A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration]] (82.5% similar)
- [[2025-09-23/A study on Deep Convolutional Neural Networks, transfer learning, and Mnet model for Cervical Cancer Detection_20250923|A study on Deep Convolutional Neural Networks, transfer learning, and Mnet model for Cervical Cancer Detection]] (81.8% similar)
- [[2025-09-22/Training A Neural Network For Partially Occluded Road Sign Identification In The Context Of Autonomous Vehicles_20250922|Training A Neural Network For Partially Occluded Road Sign Identification In The Context Of Autonomous Vehicles]] (81.4% similar)
- [[2025-09-23/Deep Learning Inductive Biases for fMRI Time Series Classification during Resting-state and Movie-watching_20250923|Deep Learning Inductive Biases for fMRI Time Series Classification during Resting-state and Movie-watching]] (81.2% similar)
- [[2025-09-22/Incorporating Visual Cortical Lateral Connection Properties into CNN_ Recurrent Activation and Excitatory-Inhibitory Separation_20250922|Incorporating Visual Cortical Lateral Connection Properties into CNN: Recurrent Activation and Excitatory-Inhibitory Separation]] (80.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Visual Perception in Neural Networks|Visual Perception in Neural Networks]], [[keywords/Domain Shift|Domain Shift]]
**⚡ Unique Technical**: [[keywords/Data-Domain Sampling|Data-Domain Sampling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2507.03866v2 Announce Type: replace 
Abstract: We present a data-domain sampling regime for quantifying CNNs' graphic perception behaviors. This regime lets us evaluate CNNs' ratio estimation ability in bar charts from three perspectives: sensitivity to training-test distribution discrepancies, stability to limited samples, and relative expertise to human observers. After analyzing 16 million trials from 800 CNNs models and 6,825 trials from 113 human participants, we arrived at a simple and actionable conclusion: CNNs can outperform humans and their biases simply depend on the training-test distance. We show evidence of this simple, elegant behavior of the machines when they interpret visualization images. osf.io/gfqc3 provides registration, the code for our sampling regime, and experimental results.

## 📝 요약

이 논문은 CNN의 그래픽 인식 행동을 평가하기 위한 데이터 도메인 샘플링 체계를 제시합니다. 이 체계는 바 차트에서 CNN의 비율 추정 능력을 세 가지 관점에서 평가합니다: 훈련-테스트 분포 차이에 대한 민감도, 제한된 샘플에 대한 안정성, 인간 관찰자에 대한 상대적 전문성. 800개의 CNN 모델과 113명의 인간 참가자에 대한 실험을 통해, CNN이 인간을 능가할 수 있으며, 그 편향은 훈련-테스트 거리의 영향을 받는다는 결론을 도출했습니다. 이 연구는 CNN이 시각화 이미지를 해석할 때의 단순하고 우아한 행동을 보여줍니다.

## 🎯 주요 포인트

- 1. CNN의 그래픽 인식 행동을 정량화하기 위한 데이터 도메인 샘플링 체계를 제시했습니다.
- 2. 바 차트에서 CNN의 비율 추정 능력을 세 가지 관점에서 평가했습니다: 훈련-테스트 분포 불일치에 대한 민감성, 제한된 샘플에 대한 안정성, 인간 관찰자에 대한 상대적 전문성.
- 3. 800개의 CNN 모델과 113명의 인간 참가자로부터 수집한 데이터를 분석한 결과, CNN이 인간을 능가할 수 있으며 그 편향은 훈련-테스트 거리의 영향을 받는다는 결론을 도출했습니다.
- 4. CNN이 시각화 이미지를 해석할 때 단순하고 우아한 행동을 보인다는 증거를 제시했습니다.
- 5. 연구 등록, 샘플링 체계 코드 및 실험 결과는 osf.io/gfqc3에서 확인할 수 있습니다.


---

*Generated on 2025-09-24 15:26:02*