<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T13:48:53.807282",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Scattering Transformer",
    "Heart Murmur Detection",
    "Wavelet Scattering Networks",
    "Self-supervised Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Scattering Transformer": 0.8,
    "Heart Murmur Detection": 0.82,
    "Wavelet Scattering Networks": 0.78,
    "Self-supervised Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Scattering Transformer",
        "canonical": "Scattering Transformer",
        "aliases": [
          "Training-Free Transformer"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel architecture specifically for heart murmur detection, offering a new connection point in transformer research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Heart Murmur Detection",
        "canonical": "Heart Murmur Detection",
        "aliases": [
          "Cardiac Auscultation Automation"
        ],
        "category": "specific_connectable",
        "rationale": "Focuses on a specific biomedical application, linking medical and technical research areas.",
        "novelty_score": 0.7,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Wavelet Scattering Networks",
        "canonical": "Wavelet Scattering Networks",
        "aliases": [
          "Wavelet Scattering"
        ],
        "category": "specific_connectable",
        "rationale": "Provides a technical foundation for the proposed architecture, bridging signal processing and machine learning.",
        "novelty_score": 0.65,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Self-supervised Audio Foundation Models",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Audio Foundation Models"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the role of self-supervised learning in audio tasks, connecting to broader machine learning trends.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "Training Data",
      "Performance",
      "Dataset"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Scattering Transformer",
      "resolved_canonical": "Scattering Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Heart Murmur Detection",
      "resolved_canonical": "Heart Murmur Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Wavelet Scattering Networks",
      "resolved_canonical": "Wavelet Scattering Networks",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Self-supervised Audio Foundation Models",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Scattering Transformer: A Training-Free Transformer Architecture for Heart Murmur Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18424.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.18424](https://arxiv.org/abs/2509.18424)

## 🔗 유사한 논문
- [[2025-09-22/Channel-Imposed Fusion_ A Simple yet Effective Method for Medical Time Series Classification_20250922|Channel-Imposed Fusion: A Simple yet Effective Method for Medical Time Series Classification]] (81.0% similar)
- [[2025-09-23/TractoTransformer_ Diffusion MRI Streamline Tractography using CNN and Transformer Networks_20250923|TractoTransformer: Diffusion MRI Streamline Tractography using CNN and Transformer Networks]] (81.0% similar)
- [[2025-09-18/Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations_20250918|Non-Intrusive Parametrized-Background Data-Weak Reconstruction of Cardiac Displacement Fields from Sparse MRI-like Observations]] (80.4% similar)
- [[2025-09-23/CSDformer_ A Conversion Method for Fully Spike-Driven Transformer_20250923|CSDformer: A Conversion Method for Fully Spike-Driven Transformer]] (80.2% similar)
- [[2025-09-23/DBConformer_ Dual-Branch Convolutional Transformer for EEG Decoding_20250923|DBConformer: Dual-Branch Convolutional Transformer for EEG Decoding]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Heart Murmur Detection|Heart Murmur Detection]], [[keywords/Wavelet Scattering Networks|Wavelet Scattering Networks]], [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Scattering Transformer|Scattering Transformer]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18424v1 Announce Type: cross 
Abstract: In an attempt to address the need for skilled clinicians in heart sound interpretation, recent research efforts on automating cardiac auscultation have explored deep learning approaches. The majority of these approaches have been based on supervised learning that is always challenged in occasions where training data is limited. More recently, there has been a growing interest in potentials of pre-trained self-supervised audio foundation models for biomedical end tasks. Despite exhibiting promising results, these foundational models are typically computationally intensive. Within the context of automatic cardiac auscultation, this study explores a lightweight alternative to these general-purpose audio foundation models by introducing the Scattering Transformer, a novel, training-free transformer architecture for heart murmur detection. The proposed method leverages standard wavelet scattering networks by introducing contextual dependencies in a transformer-like architecture without any backpropagation. We evaluate our approach on the public CirCor DigiScope dataset, directly comparing it against leading general-purpose foundational models. The Scattering Transformer achieves a Weighted Accuracy(WAR) of 0.786 and an Unweighted Average Recall(UAR) of 0.697, demonstrating performance highly competitive with contemporary state of the art methods. This study establishes the Scattering Transformer as a viable and promising alternative in resource-constrained setups.

## 📝 요약

이 연구는 심장 소리 해석 자동화를 위한 경량화된 대안으로 Scattering Transformer를 제안합니다. 이는 훈련이 필요 없는 새로운 트랜스포머 구조로, 심장 잡음 탐지에 사용됩니다. 기존의 일반적인 오디오 모델보다 계산 자원이 덜 소모되며, 표준 웨이블릿 스캐터링 네트워크를 활용해 문맥적 의존성을 도입합니다. CirCor DigiScope 데이터셋에서 테스트한 결과, Weighted Accuracy(WAR) 0.786과 Unweighted Average Recall(UAR) 0.697을 기록하며, 최신 기술과 비슷한 성능을 보였습니다. 이 연구는 자원이 제한된 환경에서 Scattering Transformer의 가능성을 입증합니다.

## 🎯 주요 포인트

- 1. 심장 소리 해석의 자동화를 위한 연구에서 심잡음 탐지를 위한 Scattering Transformer라는 새로운 경량 트랜스포머 아키텍처를 제안합니다.
- 2. 제안된 방법은 학습이 필요 없는 웨이블릿 산란 네트워크와 트랜스포머 아키텍처의 문맥적 의존성을 결합하여 구현되었습니다.
- 3. Scattering Transformer는 CirCor DigiScope 데이터셋에서 테스트되었으며, 최신 일반 목적 모델과 비교하여 높은 성능을 보였습니다.
- 4. 이 연구는 자원이 제한된 환경에서 Scattering Transformer가 유망한 대안임을 입증합니다.


---

*Generated on 2025-09-24 13:48:53*