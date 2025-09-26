---
keywords:
  - Mixture-of-Experts Framework
  - Neural Network
  - EMG Artifact Removal
  - Signal Filtration Algorithm
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19385
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:52:38.241656",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mixture-of-Experts Framework",
    "Neural Network",
    "EMG Artifact Removal",
    "Signal Filtration Algorithm"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mixture-of-Experts Framework": 0.78,
    "Neural Network": 0.7,
    "EMG Artifact Removal": 0.82,
    "Signal Filtration Algorithm": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "mixture-of-experts framework",
        "canonical": "Mixture-of-Experts Framework",
        "aliases": [
          "MoE framework"
        ],
        "category": "unique_technical",
        "rationale": "The Mixture-of-Experts framework is central to the paper's methodology and offers a unique approach to EMG artifact removal.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "neural network-based denoising",
        "canonical": "Neural Network",
        "aliases": [
          "NN-based denoising"
        ],
        "category": "broad_technical",
        "rationale": "Neural networks are a fundamental component of the denoising process discussed, linking to broader machine learning concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "EMG artifact removal",
        "canonical": "EMG Artifact Removal",
        "aliases": [
          "electromyogenic artifact removal"
        ],
        "category": "specific_connectable",
        "rationale": "EMG artifact removal is a specific application area that connects to broader EEG processing and neural interface topics.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "signal filtration algorithm",
        "canonical": "Signal Filtration Algorithm",
        "aliases": [
          "signal filtering algorithm"
        ],
        "category": "unique_technical",
        "rationale": "This algorithm is a novel contribution of the paper, providing a new method for improving EEG signal quality.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.78,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "mixture-of-experts framework",
      "resolved_canonical": "Mixture-of-Experts Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "neural network-based denoising",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "EMG artifact removal",
      "resolved_canonical": "EMG Artifact Removal",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "signal filtration algorithm",
      "resolved_canonical": "Signal Filtration Algorithm",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# A Statistical Mixture-of-Experts Framework for EMG Artifact Removal in EEG: Empirical Insights and a Proof-of-Concept Application

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19385.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19385](https://arxiv.org/abs/2509.19385)

## 🔗 유사한 논문
- [[2025-09-24/Symphony-MoE_ Harmonizing Disparate Pre-trained Models into a Coherent Mixture-of-Experts_20250924|Symphony-MoE: Harmonizing Disparate Pre-trained Models into a Coherent Mixture-of-Experts]] (84.5% similar)
- [[2025-09-22/MoE-CE_ Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework_20250922|MoE-CE: Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework]] (84.4% similar)
- [[2025-09-22/DiEP_ Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning_20250922|DiEP: Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning]] (84.0% similar)
- [[2025-09-23/MoEs Are Stronger than You Think_ Hyper-Parallel Inference Scaling with RoE_20250923|MoEs Are Stronger than You Think: Hyper-Parallel Inference Scaling with RoE]] (83.5% similar)
- [[2025-09-24/An Efficient Self-Supervised Framework for Long-Sequence EEG Modeling_20250924|An Efficient Self-Supervised Framework for Long-Sequence EEG Modeling]] (83.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/EMG Artifact Removal|EMG Artifact Removal]]
**⚡ Unique Technical**: [[keywords/Mixture-of-Experts Framework|Mixture-of-Experts Framework]], [[keywords/Signal Filtration Algorithm|Signal Filtration Algorithm]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19385v1 Announce Type: cross 
Abstract: Effective control of neural interfaces is limited by poor signal quality. While neural network-based electroencephalography (EEG) denoising methods for electromyogenic (EMG) artifacts have improved in recent years, current state-of-the-art (SOTA) models perform suboptimally in settings with high noise. To address the shortcomings of current machine learning (ML)-based denoising algorithms, we present a signal filtration algorithm driven by a new mixture-of-experts (MoE) framework. Our algorithm leverages three new statistical insights into the EEG-EMG denoising problem: (1) EMG artifacts can be partitioned into quantifiable subtypes to aid downstream MoE classification, (2) local experts trained on narrower signal-to-noise ratio (SNR) ranges can achieve performance increases through specialization, and (3) correlation-based objective functions, in conjunction with rescaling algorithms, can enable faster convergence in a neural network-based denoising context. We empirically demonstrate these three insights into EMG artifact removal and use our findings to create a new downstream MoE denoising algorithm consisting of convolutional (CNN) and recurrent (RNN) neural networks. We tested all results on a major benchmark dataset (EEGdenoiseNet) collected from 67 subjects. We found that our MoE denoising model achieved competitive overall performance with SOTA ML denoising algorithms and superior lower bound performance in high noise settings. These preliminary results highlight the promise of our MoE framework for enabling advances in EMG artifact removal for EEG processing, especially in high noise settings. Further research and development will be necessary to assess our MoE framework on a wider range of real-world test cases and explore its downstream potential to unlock more effective neural interfaces.

## 📝 요약

이 논문은 신경 인터페이스의 신호 품질 문제를 해결하기 위해 새로운 혼합 전문가(MoE) 프레임워크 기반의 신호 필터링 알고리즘을 제안합니다. 주요 기여는 EMG 잡음을 정량화 가능한 하위 유형으로 분류하고, 좁은 신호 대 잡음비(SNR) 범위에 특화된 전문가를 활용하며, 상관 기반 목표 함수를 통해 신경망 기반 잡음 제거의 수렴 속도를 높이는 것입니다. 이 알고리즘은 CNN과 RNN을 결합하여 EEGdenoiseNet 데이터셋에서 테스트되었으며, 특히 높은 잡음 환경에서 기존 최신 기계 학습 기반 잡음 제거 알고리즘보다 우수한 성능을 보였습니다. 이 연구는 EEG 처리에서 EMG 잡음 제거의 가능성을 보여주며, 향후 다양한 실제 사례에서의 추가 연구가 필요합니다.

## 🎯 주요 포인트

- 1. 현재의 기계 학습 기반 EEG 잡음 제거 알고리즘은 높은 노이즈 환경에서 성능이 부족하다.
- 2. 새로운 mixture-of-experts (MoE) 프레임워크를 기반으로 한 신호 필터링 알고리즘을 제안하였다.
- 3. EMG 아티팩트를 정량화 가능한 하위 유형으로 분할하여 MoE 분류를 지원할 수 있다.
- 4. 좁은 신호 대 잡음비(SNR) 범위에 맞춰 훈련된 로컬 전문가들이 성능 향상을 이룰 수 있다.
- 5. MoE 잡음 제거 모델은 높은 노이즈 환경에서 기존 최첨단 기계 학습 잡음 제거 알고리즘보다 우수한 성능을 보였다.


---

*Generated on 2025-09-25 16:52:38*