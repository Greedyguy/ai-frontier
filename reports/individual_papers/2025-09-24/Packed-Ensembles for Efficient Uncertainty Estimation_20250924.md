<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:20:28.419276",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Ensembles",
    "Packed-Ensembles",
    "Uncertainty Estimation",
    "Out-of-Distribution Detection"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Ensembles": 0.85,
    "Packed-Ensembles": 0.9,
    "Uncertainty Estimation": 0.8,
    "Out-of-Distribution Detection": 0.85
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep Ensembles",
        "canonical": "Deep Ensembles",
        "aliases": [
          "DE"
        ],
        "category": "unique_technical",
        "rationale": "Deep Ensembles are a key technique in uncertainty estimation and are central to the paper's contributions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Packed-Ensembles",
        "canonical": "Packed-Ensembles",
        "aliases": [
          "PE"
        ],
        "category": "unique_technical",
        "rationale": "Packed-Ensembles represent the novel contribution of the paper, offering a new approach to ensemble learning.",
        "novelty_score": 0.9,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.9
      },
      {
        "surface": "Uncertainty Estimation",
        "canonical": "Uncertainty Estimation",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Uncertainty estimation is a fundamental aspect of the paper's focus and connects to broader machine learning discussions.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Out-of-Distribution Detection",
        "canonical": "Out-of-Distribution Detection",
        "aliases": [
          "OOD Detection"
        ],
        "category": "specific_connectable",
        "rationale": "This is a specific application area of the proposed method, relevant for linking to related research.",
        "novelty_score": 0.6,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "method",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep Ensembles",
      "resolved_canonical": "Deep Ensembles",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Packed-Ensembles",
      "resolved_canonical": "Packed-Ensembles",
      "decision": "linked",
      "scores": {
        "novelty": 0.9,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Uncertainty Estimation",
      "resolved_canonical": "Uncertainty Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Out-of-Distribution Detection",
      "resolved_canonical": "Out-of-Distribution Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    }
  ]
}
-->

# Packed-Ensembles for Efficient Uncertainty Estimation

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2210.09184.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2210.09184](https://arxiv.org/abs/2210.09184)

## 🔗 유사한 논문
- [[2025-09-18/Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning_20250918|Post-Hoc Split-Point Self-Consistency Verification for Efficient, Unified Quantification of Aleatoric and Epistemic Uncertainty in Deep Learning]] (78.0% similar)
- [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE: Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (77.9% similar)
- [[2025-09-19/Sample Efficient Experience Replay in Non-stationary Environments_20250919|Sample Efficient Experience Replay in Non-stationary Environments]] (77.8% similar)
- [[2025-09-23/MoEs Are Stronger than You Think_ Hyper-Parallel Inference Scaling with RoE_20250923|MoEs Are Stronger than You Think: Hyper-Parallel Inference Scaling with RoE]] (77.6% similar)
- [[2025-09-19/Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning_20250919|Communication-Efficient and Privacy-Adaptable Mechanism for Federated Learning]] (77.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Uncertainty Estimation|Uncertainty Estimation]]
**🔗 Specific Connectable**: [[keywords/Out-of-Distribution Detection|Out-of-Distribution Detection]]
**⚡ Unique Technical**: [[keywords/Deep Ensembles|Deep Ensembles]], [[keywords/Packed-Ensembles|Packed-Ensembles]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2210.09184v4 Announce Type: replace 
Abstract: Deep Ensembles (DE) are a prominent approach for achieving excellent performance on key metrics such as accuracy, calibration, uncertainty estimation, and out-of-distribution detection. However, hardware limitations of real-world systems constrain to smaller ensembles and lower-capacity networks, significantly deteriorating their performance and properties. We introduce Packed-Ensembles (PE), a strategy to design and train lightweight structured ensembles by carefully modulating the dimension of their encoding space. We leverage grouped convolutions to parallelize the ensemble into a single shared backbone and forward pass to improve training and inference speeds. PE is designed to operate within the memory limits of a standard neural network. Our extensive research indicates that PE accurately preserves the properties of DE, such as diversity, and performs equally well in terms of accuracy, calibration, out-of-distribution detection, and robustness to distribution shift. We make our code available at https://github.com/ENSTA-U2IS/torch-uncertainty.

## 📝 요약

이 논문은 Deep Ensembles(DE)의 성능을 유지하면서도 하드웨어 제약을 극복하기 위한 Packed-Ensembles(PE)를 제안합니다. PE는 인코딩 공간의 차원을 조절하여 경량화된 구조적 앙상블을 설계하고 훈련하며, 그룹화된 컨볼루션을 활용해 단일 백본과 포워드 패스를 공유함으로써 훈련 및 추론 속도를 향상시킵니다. 연구 결과, PE는 DE의 다양성과 성능을 정확히 유지하면서도 정확도, 보정, 분포 외 탐지 및 분포 변화에 대한 강건성에서 동등한 성과를 보였습니다.

## 🎯 주요 포인트

- 1. Packed-Ensembles(PE)는 인코딩 공간의 차원을 조절하여 경량화된 구조적 앙상블을 설계하고 훈련하는 전략을 제시합니다.
- 2. 그룹화된 컨볼루션을 활용하여 앙상블을 단일 공유 백본과 전방 패스로 병렬화하여 훈련 및 추론 속도를 향상시킵니다.
- 3. PE는 표준 신경망의 메모리 한계 내에서 작동하도록 설계되었습니다.
- 4. 연구 결과, PE는 Deep Ensembles(DE)의 다양성과 같은 특성을 정확히 보존하며, 정확도, 보정, 분포 외 탐지 및 분포 변화에 대한 강건성 측면에서 동등한 성능을 보입니다.
- 5. 연구 코드는 https://github.com/ENSTA-U2IS/torch-uncertainty에서 제공됩니다.


---

*Generated on 2025-09-24 15:20:28*