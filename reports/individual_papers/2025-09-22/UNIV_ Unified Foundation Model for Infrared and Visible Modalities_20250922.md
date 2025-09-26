---
keywords:
  - Cross-modality Contrastive Learning
  - Transformer
  - Knowledge Preservation
  - Multimodal Learning
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15642
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:04:06.791192",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Cross-modality Contrastive Learning",
    "Transformer",
    "Knowledge Preservation",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Cross-modality Contrastive Learning": 0.78,
    "Transformer": 0.8,
    "Knowledge Preservation": 0.72,
    "Multimodal Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Patch-wise Cross-modality Contrastive Learning",
        "canonical": "Cross-modality Contrastive Learning",
        "aliases": [
          "PCCL"
        ],
        "category": "unique_technical",
        "rationale": "This technique is a novel approach for aligning features across modalities, enhancing multimodal learning capabilities.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Transformer-based architecture",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are a foundational architecture in deep learning, relevant to the proposed model's compatibility.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.8
      },
      {
        "surface": "dual-knowledge preservation mechanism",
        "canonical": "Knowledge Preservation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This mechanism is crucial for maintaining performance across modalities, reflecting advanced model design.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "Multimodal Learning",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "The paper's focus on integrating infrared and visible data highlights the importance of multimodal approaches.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "autonomous vehicles",
      "weather conditions",
      "baseline performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Patch-wise Cross-modality Contrastive Learning",
      "resolved_canonical": "Cross-modality Contrastive Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Transformer-based architecture",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "dual-knowledge preservation mechanism",
      "resolved_canonical": "Knowledge Preservation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Multimodal Learning",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# UNIV: Unified Foundation Model for Infrared and Visible Modalities

**Korean Title:** UNIV: 적외선 및 가시광선 모달리티를 위한 통합 기초 모델

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15642.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15642](https://arxiv.org/abs/2509.15642)

## 🔗 유사한 논문
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets]] (84.2% similar)
- [[2025-09-22/UniMRSeg_ Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation_20250922|UniMRSeg: Unified Modality-Relax Segmentation via Hierarchical Self-Supervised Compensation]] (83.2% similar)
- [[2025-09-18/UniPLV_ Towards Label-Efficient Open-World 3D Scene Understanding by Regional Visual Language Supervision_20250918|UniPLV: Towards Label-Efficient Open-World 3D Scene Understanding by Regional Visual Language Supervision]] (82.5% similar)
- [[2025-09-22/Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception_20250922|Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception]] (81.5% similar)
- [[2025-09-19/UMind_ A Unified Multitask Network for Zero-Shot M/EEG Visual Decoding_20250919|UMind: A Unified Multitask Network for Zero-Shot M/EEG Visual Decoding]] (81.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Cross-modality Contrastive Learning|Cross-modality Contrastive Learning]], [[keywords/Knowledge Preservation|Knowledge Preservation]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15642v1 Announce Type: new 
Abstract: The demand for joint RGB-visible and infrared perception is growing rapidly, particularly to achieve robust performance under diverse weather conditions. Although pre-trained models for RGB-visible and infrared data excel in their respective domains, they often underperform in multimodal scenarios, such as autonomous vehicles equipped with both sensors. To address this challenge, we propose a biologically inspired UNified foundation model for Infrared and Visible modalities (UNIV), featuring two key innovations. First, we introduce Patch-wise Cross-modality Contrastive Learning (PCCL), an attention-guided distillation framework that mimics retinal horizontal cells' lateral inhibition, which enables effective cross-modal feature alignment while remaining compatible with any transformer-based architecture. Second, our dual-knowledge preservation mechanism emulates the retina's bipolar cell signal routing - combining LoRA adapters (2% added parameters) with synchronous distillation to prevent catastrophic forgetting, thereby replicating the retina's photopic (cone-driven) and scotopic (rod-driven) functionality. To support cross-modal learning, we introduce the MVIP dataset, the most comprehensive visible-infrared benchmark to date. It contains 98,992 precisely aligned image pairs spanning diverse scenarios. Extensive experiments demonstrate UNIV's superior performance on infrared tasks (+1.7 mIoU in semantic segmentation and +0.7 mAP in object detection) while maintaining 99%+ of the baseline performance on visible RGB tasks. Our code is available at https://github.com/fangyuanmao/UNIV.

## 🔍 Abstract (한글 번역)

arXiv:2509.15642v1 발표 유형: 신규  
초록: RGB-가시광선과 적외선의 결합 인식에 대한 수요가 급격히 증가하고 있으며, 특히 다양한 기상 조건에서 강력한 성능을 달성하기 위해 중요합니다. RGB-가시광선과 적외선 데이터를 위한 사전 학습된 모델은 각자의 영역에서 뛰어난 성능을 보이지만, 두 센서를 장착한 자율 주행 차량과 같은 다중 모달 시나리오에서는 종종 성능이 저하됩니다. 이 문제를 해결하기 위해, 우리는 적외선 및 가시광선 모달리티를 위한 생물학적으로 영감을 받은 통합 기초 모델(UNIV)을 제안하며, 두 가지 주요 혁신을 특징으로 합니다. 첫째, 우리는 패치 기반 교차 모달 대조 학습(PCCL)을 도입합니다. 이는 망막의 수평 세포의 측면 억제를 모방한 주의 기반 증류 프레임워크로, 모든 트랜스포머 기반 아키텍처와 호환되면서 효과적인 교차 모달 특징 정렬을 가능하게 합니다. 둘째, 우리의 이중 지식 보존 메커니즘은 망막의 양극 세포 신호 경로를 모방하여 LoRA 어댑터(2% 추가 매개변수)와 동기화 증류를 결합하여 파국적 망각을 방지하며, 망막의 명시적(원추세포 주도) 및 암시적(막대세포 주도) 기능을 재현합니다. 교차 모달 학습을 지원하기 위해, 우리는 현재까지 가장 포괄적인 가시광선-적외선 벤치마크인 MVIP 데이터셋을 소개합니다. 이 데이터셋은 다양한 시나리오에 걸쳐 정확히 정렬된 98,992개의 이미지 쌍을 포함하고 있습니다. 광범위한 실험을 통해 UNIV가 적외선 작업에서 우수한 성능을 보임을 입증했습니다(의미론적 분할에서 +1.7 mIoU, 객체 탐지에서 +0.7 mAP)하며, 가시 RGB 작업에서 기준 성능의 99% 이상을 유지합니다. 우리의 코드는 https://github.com/fangyuanmao/UNIV에서 이용할 수 있습니다.

## 📝 요약

이 논문은 다양한 기상 조건에서 강력한 성능을 발휘하기 위해 RGB-가시광선과 적외선 데이터를 결합한 인식의 필요성이 증가하는 상황에서, 두 가지 모달리티를 효과적으로 통합하는 UNIV 모델을 제안합니다. 주요 기여로는 두 가지 혁신적인 방법론이 있습니다. 첫째, Patch-wise Cross-modality Contrastive Learning(PCCL)은 망막의 수평 세포 억제 메커니즘을 모방하여 교차 모달 피처 정렬을 가능하게 합니다. 둘째, 듀얼 지식 보존 메커니즘은 망막의 신호 경로를 모방하여 LoRA 어댑터와 동기 증류를 결합, 망각을 방지합니다. 또한, 다양한 시나리오를 포함한 98,992개의 이미지 쌍을 제공하는 MVIP 데이터셋을 소개합니다. 실험 결과, UNIV는 적외선 작업에서 우수한 성능을 보이며, RGB 작업에서도 99% 이상의 성능을 유지합니다.

## 🎯 주요 포인트

- 1. RGB-가시광선과 적외선 데이터를 결합한 인식 수요가 증가하고 있으며, 특히 다양한 날씨 조건에서의 견고한 성능을 목표로 하고 있습니다.
- 2. UNIV 모델은 Patch-wise Cross-modality Contrastive Learning (PCCL)을 도입하여 효과적인 교차 모달 특성 정렬을 가능하게 합니다.
- 3. 이 모델은 LoRA 어댑터와 동기 증류를 결합한 이중 지식 보존 메커니즘을 통해 망각을 방지하고, 망막의 기능을 모방합니다.
- 4. MVIP 데이터셋은 가장 포괄적인 가시광선-적외선 벤치마크로, 다양한 시나리오를 아우르는 98,992개의 정밀하게 정렬된 이미지 쌍을 포함하고 있습니다.
- 5. UNIV 모델은 적외선 작업에서 뛰어난 성능을 보이며, 가시광선 RGB 작업에서도 99% 이상의 기준 성능을 유지합니다.


---

*Generated on 2025-09-23 12:04:06*