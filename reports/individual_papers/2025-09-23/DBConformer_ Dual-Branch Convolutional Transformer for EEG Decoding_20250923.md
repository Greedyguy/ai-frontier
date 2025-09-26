---
keywords:
  - DBConformer
  - EEG Decoding
  - Neural Network
  - Attention Mechanism
  - Transformer
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.21140
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:09:43.946846",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "DBConformer",
    "EEG Decoding",
    "Neural Network",
    "Attention Mechanism",
    "Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "DBConformer": 0.8,
    "EEG Decoding": 0.75,
    "Neural Network": 0.7,
    "Attention Mechanism": 0.78,
    "Transformer": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "DBConformer",
        "canonical": "DBConformer",
        "aliases": [
          "Dual-Branch Convolutional Transformer"
        ],
        "category": "unique_technical",
        "rationale": "DBConformer is a novel architecture specific to EEG decoding, providing a unique technical focus for linking.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "EEG Decoding",
        "canonical": "EEG Decoding",
        "aliases": [
          "Electroencephalography Decoding"
        ],
        "category": "specific_connectable",
        "rationale": "EEG Decoding is a specific application area that connects to broader neuroscience and BCI research.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.82,
        "link_intent_score": 0.75
      },
      {
        "surface": "Convolutional Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "CNNs"
        ],
        "category": "broad_technical",
        "rationale": "CNNs are a foundational technology in EEG decoding, linking to a wide range of neural network research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.7
      },
      {
        "surface": "Channel Attention Module",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Channel-wise Attention"
        ],
        "category": "specific_connectable",
        "rationale": "The channel attention module is a specific implementation of attention mechanisms, crucial for EEG signal processing.",
        "novelty_score": 0.65,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.78
      },
      {
        "surface": "Temporal Conformer",
        "canonical": "Transformer",
        "aliases": [
          "Temporal Transformer"
        ],
        "category": "specific_connectable",
        "rationale": "Temporal Conformer is a specialized Transformer variant, enhancing temporal dependency modeling in EEG.",
        "novelty_score": 0.6,
        "connectivity_score": 0.82,
        "specificity_score": 0.78,
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
      "candidate_surface": "DBConformer",
      "resolved_canonical": "DBConformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "EEG Decoding",
      "resolved_canonical": "EEG Decoding",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.82,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Convolutional Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Channel Attention Module",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Temporal Conformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.82,
        "specificity": 0.78,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# DBConformer: Dual-Branch Convolutional Transformer for EEG Decoding

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.21140.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.21140](https://arxiv.org/abs/2506.21140)

## 🔗 유사한 논문
- [[2025-09-22/Channel-Imposed Fusion_ A Simple yet Effective Method for Medical Time Series Classification_20250922|Channel-Imposed Fusion: A Simple yet Effective Method for Medical Time Series Classification]] (82.6% similar)
- [[2025-09-22/EvoBrain_ Dynamic Multi-channel EEG Graph Modeling for Time-evolving Brain Network_20250922|EvoBrain: Dynamic Multi-channel EEG Graph Modeling for Time-evolving Brain Network]] (81.6% similar)
- [[2025-09-23/A Simple Review of EEG Foundation Models_ Datasets, Advancements and Future Perspectives_20250923|A Simple Review of EEG Foundation Models: Datasets, Advancements and Future Perspectives]] (81.1% similar)
- [[2025-09-22/IEFS-GMB_ Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders_20250922|IEFS-GMB: Gradient Memory Bank-Guided Feature Selection Based on Information Entropy for EEG Classification of Neurological Disorders]] (80.8% similar)
- [[2025-09-17/Exploring the Relationship between Brain Hemisphere States and Frequency Bands through Deep Learning Optimization Techniques_20250917|Exploring the Relationship between Brain Hemisphere States and Frequency Bands through Deep Learning Optimization Techniques]] (80.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/EEG Decoding|EEG Decoding]], [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Transformer|Transformer]]
**⚡ Unique Technical**: [[keywords/DBConformer|DBConformer]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.21140v2 Announce Type: replace-cross 
Abstract: Electroencephalography (EEG)-based brain-computer interfaces (BCIs) transform spontaneous/evoked neural activity into control commands for external communication. While convolutional neural networks (CNNs) remain the mainstream backbone for EEG decoding, their inherently short receptive field makes it difficult to capture long-range temporal dependencies and global inter-channel relationships. Recent CNN-Transformer (Conformer) hybrids partially address this issue, but most adopt a serial design, resulting in suboptimal integration of local and global features, and often overlook explicit channel-wise modeling. To address these limitations, we propose DBConformer, a dual-branch convolutional Transformer network tailored for EEG decoding. It integrates a temporal Conformer to model long-range temporal dependencies and a spatial Conformer to extract inter-channel interactions, capturing both temporal dynamics and spatial patterns in EEG signals. A lightweight channel attention module further refines spatial representations by assigning data-driven importance to EEG channels. Extensive experiments under four evaluation settings on three paradigms, including motor imagery, seizure detection, and steady-state visual evoked potential, demonstrated that DBConformer consistently outperformed 13 competitive baseline models, with over an eight-fold reduction in parameters than current high-capacity EEG Conformer architecture. Furthermore, the visualization results confirmed that the features extracted by DBConformer are physiologically interpretable and aligned with prior knowledge. The superior performance and interpretability of DBConformer make it reliable for accurate, robust, and explainable EEG decoding. Code is publicized at https://github.com/wzwvv/DBConformer.

## 📝 요약

DBConformer는 EEG 기반 뇌-컴퓨터 인터페이스(BCI)에서 장기적인 시간적 의존성과 채널 간 상호작용을 효과적으로 포착하기 위해 설계된 이중 브랜치 컨볼루셔널 트랜스포머 네트워크입니다. 이 모델은 시간적 및 공간적 컨포머를 통합하여 EEG 신호의 시간적 역학과 공간적 패턴을 모두 포착하며, 경량의 채널 주의 모듈을 통해 채널별 중요도를 조정하여 공간 표현을 개선합니다. 모터 이미지, 발작 감지, 안정 상태 시각 유발 전위 등 세 가지 패러다임에서의 실험 결과, DBConformer는 기존 모델들보다 우수한 성능을 보였으며, 파라미터 수는 기존 고용량 모델에 비해 8배 이상 감소했습니다. 또한, DBConformer가 추출한 특징은 생리학적으로 해석 가능하며, 기존 지식과 일치함을 확인했습니다. 이러한 성능과 해석 가능성 덕분에 DBConformer는 정확하고 견고하며 설명 가능한 EEG 디코딩에 신뢰할 수 있는 도구로 자리잡을 수 있습니다. 코드: https://github.com/wzwvv/DBConformer.

## 🎯 주요 포인트

- 1. EEG 기반 BCI의 디코딩을 위해 제안된 DBConformer는 장거리 시간 의존성과 채널 간 상호작용을 효과적으로 모델링합니다.
- 2. DBConformer는 시간적 Conformer와 공간적 Conformer를 통합하여 EEG 신호의 시간적 역학과 공간적 패턴을 포착합니다.
- 3. 경량 채널 주의 모듈을 통해 EEG 채널에 데이터 기반 중요도를 부여하여 공간 표현을 정제합니다.
- 4. DBConformer는 13개의 경쟁 모델을 능가하며, 기존의 고용량 EEG Conformer 아키텍처보다 매개변수가 8배 이상 감소했습니다.
- 5. DBConformer의 특징은 생리학적으로 해석 가능하며, 이전 지식과 일치하여 신뢰할 수 있는 EEG 디코딩을 제공합니다.


---

*Generated on 2025-09-24 01:09:43*