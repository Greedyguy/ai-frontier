---
keywords:
  - Self-supervised Learning
  - Brain-Computer Interface
  - Euclidean Alignment
  - Steady-State Visual Evoked Potentials
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19403
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:34:38.198795",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Self-supervised Learning",
    "Brain-Computer Interface",
    "Euclidean Alignment",
    "Steady-State Visual Evoked Potentials"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Self-supervised Learning": 0.85,
    "Brain-Computer Interface": 0.8,
    "Euclidean Alignment": 0.75,
    "Steady-State Visual Evoked Potentials": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Self-supervision",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "Self-supervised",
          "Self-supervision"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised learning is a key technique in the proposed algorithm, facilitating adaptation without labeled data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Brain-Computer Interface",
        "canonical": "Brain-Computer Interface",
        "aliases": [
          "BCI",
          "Brain-Machine Interface"
        ],
        "category": "unique_technical",
        "rationale": "The study focuses on enhancing the adaptability of brain-computer interfaces, making it a central concept.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Euclidean alignment",
        "canonical": "Euclidean Alignment",
        "aliases": [
          "Euclidean space alignment"
        ],
        "category": "unique_technical",
        "rationale": "Euclidean alignment is a novel approach used in the dual-stage alignment process of the algorithm.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Steady-State Visual Evoked Potentials",
        "canonical": "Steady-State Visual Evoked Potentials",
        "aliases": [
          "SSVEP"
        ],
        "category": "unique_technical",
        "rationale": "SSVEP is a specific BCI paradigm where the proposed algorithm shows significant accuracy gains.",
        "novelty_score": 0.6,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "online adaptation",
      "decoder",
      "batch normalization"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Self-supervision",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Brain-Computer Interface",
      "resolved_canonical": "Brain-Computer Interface",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Euclidean alignment",
      "resolved_canonical": "Euclidean Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Steady-State Visual Evoked Potentials",
      "resolved_canonical": "Steady-State Visual Evoked Potentials",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Online Adaptation via Dual-Stage Alignment and Self-Supervision for Fast-Calibration Brain-Computer Interfaces

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19403.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19403](https://arxiv.org/abs/2509.19403)

## 🔗 유사한 논문
- [[2025-09-22/Dual-Mode Visual System for Brain-Computer Interfaces_ Integrating SSVEP and P300 Responses_20250922|Dual-Mode Visual System for Brain-Computer Interfaces: Integrating SSVEP and P300 Responses]] (84.0% similar)
- [[2025-09-24/An Efficient Self-Supervised Framework for Long-Sequence EEG Modeling_20250924|An Efficient Self-Supervised Framework for Long-Sequence EEG Modeling]] (83.5% similar)
- [[2025-09-17/Personalization on a Budget_ Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection_20250917|Personalization on a Budget: Minimally-Labeled Continual Learning for Resource-Efficient Seizure Detection]] (82.6% similar)
- [[2025-09-19/UMind_ A Unified Multitask Network for Zero-Shot M/EEG Visual Decoding_20250919|UMind: A Unified Multitask Network for Zero-Shot M/EEG Visual Decoding]] (81.8% similar)
- [[2025-09-23/DBConformer_ Dual-Branch Convolutional Transformer for EEG Decoding_20250923|DBConformer: Dual-Branch Convolutional Transformer for EEG Decoding]] (81.6% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Brain-Computer Interface|Brain-Computer Interface]], [[keywords/Euclidean Alignment|Euclidean Alignment]], [[keywords/Steady-State Visual Evoked Potentials|Steady-State Visual Evoked Potentials]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19403v1 Announce Type: cross 
Abstract: Individual differences in brain activity hinder the online application of electroencephalogram (EEG)-based brain computer interface (BCI) systems. To overcome this limitation, this study proposes an online adaptation algorithm for unseen subjects via dual-stage alignment and self-supervision. The alignment process begins by applying Euclidean alignment in the EEG data space and then updates batch normalization statistics in the representation space. Moreover, a self-supervised loss is designed to update the decoder. The loss is computed by soft pseudo-labels derived from the decoder as a proxy for the unknown ground truth, and is calibrated by Shannon entropy to facilitate self-supervised training. Experiments across five public datasets and seven decoders show the proposed algorithm can be integrated seamlessly regardless of BCI paradigm and decoder architecture. In each iteration, the decoder is updated with a single online trial, which yields average accuracy gains of 4.9% on steady-state visual evoked potentials (SSVEP) and 3.6% on motor imagery. These results support fast-calibration operation and show that the proposed algorithm has great potential for BCI applications.

## 📝 요약

이 연구는 뇌파(EEG) 기반 뇌-컴퓨터 인터페이스(BCI) 시스템의 개인차 문제를 해결하기 위해 새로운 온라인 적응 알고리즘을 제안합니다. 제안된 방법론은 이중 단계 정렬과 자기 지도 학습을 활용하여 미지의 피험자에 대한 적응을 수행합니다. 정렬 과정은 EEG 데이터 공간에서 유클리드 정렬을 적용하고, 표현 공간에서 배치 정규화 통계를 업데이트합니다. 또한, 자기 지도 학습을 위해 디코더에서 파생된 소프트 의사 레이블을 사용하여 손실을 계산하고, 이를 샤논 엔트로피로 보정합니다. 다섯 개의 공개 데이터셋과 일곱 개의 디코더를 대상으로 한 실험 결과, 제안된 알고리즘은 BCI 패러다임과 디코더 구조에 관계없이 원활하게 통합될 수 있으며, 평균적으로 SSVEP에서 4.9%, 운동 이미지에서 3.6%의 정확도 향상을 보여줍니다. 이는 빠른 보정 작업을 지원하며 BCI 응용에 큰 잠재력을 지니고 있음을 시사합니다.

## 🎯 주요 포인트

- 1. 뇌 활동의 개인차가 EEG 기반 뇌-컴퓨터 인터페이스(BCI) 시스템의 온라인 적용을 방해하는 문제를 해결하기 위해, 미지의 피험자에 대한 온라인 적응 알고리즘을 제안합니다.
- 2. 제안된 알고리즘은 EEG 데이터 공간에서의 유클리드 정렬과 표현 공간에서의 배치 정규화 통계 업데이트를 포함한 이중 단계 정렬을 수행합니다.
- 3. 셀프 슈퍼비전 손실은 디코더에서 파생된 소프트 의사 레이블을 사용하여 계산되며, 셰넌 엔트로피로 보정되어 셀프 슈퍼비전 학습을 촉진합니다.
- 4. 다섯 개의 공개 데이터셋과 일곱 개의 디코더를 통한 실험 결과, 제안된 알고리즘은 BCI 패러다임과 디코더 아키텍처에 관계없이 원활하게 통합될 수 있음을 보여줍니다.
- 5. 제안된 알고리즘은 빠른 보정 작업을 지원하며, SSVEP에서 평균 4.9%, 모터 이미저리에서 3.6%의 정확도 향상을 달성하여 BCI 응용 프로그램에 큰 잠재력을 가지고 있음을 입증합니다.


---

*Generated on 2025-09-25 15:34:38*