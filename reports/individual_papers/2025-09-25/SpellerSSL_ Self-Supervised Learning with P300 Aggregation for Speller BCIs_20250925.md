---
keywords:
  - Self-supervised Learning
  - P300 Speller
  - Electroencephalogram
  - 1D U-Net
category: cs.LG
publish_date: 2025-09-25
arxiv_id: 2509.19401
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:53:09.778519",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "P300 Speller",
    "Electroencephalogram",
    "1D U-Net"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "P300 Speller": 0.78,
    "Electroencephalogram": 0.8,
    "1D U-Net": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervised Learning",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "SSL"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised Learning is a key technique in the paper, connecting it to broader machine learning advancements.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "P300 Speller",
        "canonical": "P300 Speller",
        "aliases": [
          "P300 BCI"
        ],
        "category": "unique_technical",
        "rationale": "P300 Speller is a unique application of BCIs, crucial for linking research in EEG-based communication.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Electroencephalogram",
        "canonical": "Electroencephalogram",
        "aliases": [
          "EEG"
        ],
        "category": "broad_technical",
        "rationale": "EEG is fundamental to the study, linking it to a wide range of neurotechnology research.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "1D U-Net",
        "canonical": "1D U-Net",
        "aliases": [
          "1D U-Net Backbone"
        ],
        "category": "unique_technical",
        "rationale": "1D U-Net is a specialized neural network architecture used in the paper, linking it to deep learning innovations.",
        "novelty_score": 0.68,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "calibration",
      "character recognition rate"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-supervised Learning",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "P300 Speller",
      "resolved_canonical": "P300 Speller",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Electroencephalogram",
      "resolved_canonical": "Electroencephalogram",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "1D U-Net",
      "resolved_canonical": "1D U-Net",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# SpellerSSL: Self-Supervised Learning with P300 Aggregation for Speller BCIs

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19401.pdf)
**Category**: cs.LG
**Published**: 2025-09-25
**ArXiv ID**: [2509.19401](https://arxiv.org/abs/2509.19401)

## 🔗 유사한 논문
- [[2025-09-22/Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization_20250922|Chunk Based Speech Pre-training with High Resolution Finite Scalar Quantization]] (82.1% similar)
- [[2025-09-22/Dual-Mode Visual System for Brain-Computer Interfaces_ Integrating SSVEP and P300 Responses_20250922|Dual-Mode Visual System for Brain-Computer Interfaces: Integrating SSVEP and P300 Responses]] (81.4% similar)
- [[2025-09-25/Online Adaptation via Dual-Stage Alignment and Self-Supervision for Fast-Calibration Brain-Computer Interfaces_20250925|Online Adaptation via Dual-Stage Alignment and Self-Supervision for Fast-Calibration Brain-Computer Interfaces]] (81.3% similar)
- [[2025-09-23/Leveraging Audio-Visual Data to Reduce the Multilingual Gap in Self-Supervised Speech Models_20250923|Leveraging Audio-Visual Data to Reduce the Multilingual Gap in Self-Supervised Speech Models]] (81.3% similar)
- [[2025-09-24/An Efficient Self-Supervised Framework for Long-Sequence EEG Modeling_20250924|An Efficient Self-Supervised Framework for Long-Sequence EEG Modeling]] (80.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Electroencephalogram|Electroencephalogram]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/P300 Speller|P300 Speller]], [[keywords/1D U-Net|1D U-Net]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19401v1 Announce Type: cross 
Abstract: Electroencephalogram (EEG)-based P300 speller brain-computer interfaces (BCIs) face three main challenges: low signal-to-noise ratio (SNR), poor generalization, and time-consuming calibration. We propose SpellerSSL, a framework that combines self-supervised learning (SSL) with P300 aggregation to address these issues. First, we introduce an aggregation strategy to enhance SNR. Second, to achieve generalization in training, we employ a customized 1D U-Net backbone and pretrain the model on both cross-domain and in-domain EEG data. The pretrained model is subsequently fine-tuned with a lightweight ERP-Head classifier for P300 detection, which adapts the learned representations to subject-specific data. Our evaluations on calibration time demonstrate that combining the aggregation strategy with SSL significantly reduces the calibration burden per subject and improves robustness across subjects. Experimental results show that SSL learns effective EEG representations in both in-domain and cross-domain, with in-domain achieving a state-of-the-art character recognition rate of 94% with only 7 repetitions and the highest information transfer rate (ITR) of 21.86 bits/min on the public II-B dataset. Moreover, in-domain SSL with P300 aggregation reduces the required calibration size by 60% while maintaining a comparable character recognition rate. To the best of our knowledge, this is the first study to apply SSL to P300 spellers, highlighting its potential to improve both efficiency and generalization in speller BCIs and paving the way toward an EEG foundation model for P300 speller BCIs.

## 📝 요약

SpellerSSL은 EEG 기반 P300 스펠러 BCI의 낮은 신호 대 잡음비(SNR), 일반화 부족, 긴 보정 시간 문제를 해결하기 위해 제안된 프레임워크입니다. 이 연구는 P300 집계를 통한 SNR 향상과 1D U-Net 백본을 활용한 자가 지도 학습(SSL)을 통해 일반화를 달성합니다. 사전 학습된 모델은 ERP-Head 분류기로 미세 조정되어 주제별 데이터에 적응합니다. 실험 결과, SSL은 도메인 내 및 도메인 간에서 효과적인 EEG 표현을 학습하며, 도메인 내에서는 94%의 문자 인식률과 21.86 bits/min의 정보 전송률을 기록했습니다. 또한, P300 집계와 SSL의 결합은 보정 크기를 60% 줄이면서 유사한 문자 인식률을 유지합니다. 이는 P300 스펠러에 SSL을 적용한 최초의 연구로, 스펠러 BCI의 효율성과 일반화를 개선할 잠재력을 보여줍니다.

## 🎯 주요 포인트

- 1. SpellerSSL은 자기 지도 학습(SSL)과 P300 집계를 결합하여 EEG 기반 P300 스펠러 BCI의 낮은 신호 대 잡음비(SNR), 일반화 부족, 시간 소모적인 보정 문제를 해결합니다.
- 2. 맞춤형 1D U-Net 백본을 사용하여 교차 도메인 및 도메인 내 EEG 데이터에 대해 모델을 사전 훈련하고, 경량 ERP-Head 분류기로 미세 조정하여 주제별 데이터에 적응시킵니다.
- 3. 실험 결과, 도메인 내 SSL은 7회 반복만으로 94%의 문자 인식률과 21.86 비트/분의 정보 전송률(ITR)을 달성했습니다.
- 4. P300 집계와 결합된 도메인 내 SSL은 보정 크기를 60% 줄이면서도 유사한 문자 인식률을 유지합니다.
- 5. 이 연구는 P300 스펠러에 SSL을 적용한 최초의 연구로, 스펠러 BCI의 효율성과 일반화를 개선할 잠재력을 강조합니다.


---

*Generated on 2025-09-25 16:53:09*