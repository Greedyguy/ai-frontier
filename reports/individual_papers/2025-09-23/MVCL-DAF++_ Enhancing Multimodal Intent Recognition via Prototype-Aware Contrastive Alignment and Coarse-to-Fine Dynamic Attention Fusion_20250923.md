---
keywords:
  - Multimodal Learning
  - Prototype-guided Learning
  - Attention Mechanism
  - Few-Shot Learning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.17446
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:56:15.499302",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Prototype-guided Learning",
    "Attention Mechanism",
    "Few-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Prototype-guided Learning": 0.8,
    "Attention Mechanism": 0.82,
    "Few-Shot Learning": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal intent recognition",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MMIR"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is a key area in AI that connects various modalities, enhancing understanding across different data types.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Prototype-aware contrastive alignment",
        "canonical": "Prototype-guided Learning",
        "aliases": [
          "Prototype-aware alignment"
        ],
        "category": "unique_technical",
        "rationale": "This technique enhances semantic consistency, a novel approach in aligning instances to class-level prototypes.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Coarse-to-fine attention fusion",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Hierarchical attention fusion"
        ],
        "category": "specific_connectable",
        "rationale": "This method refines attention mechanisms by integrating global and token-level features, crucial for cross-modal interaction.",
        "novelty_score": 0.6,
        "connectivity_score": 0.83,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      },
      {
        "surface": "Rare-class recognition",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Rare class detection"
        ],
        "category": "specific_connectable",
        "rationale": "Few-Shot Learning techniques are essential for improving recognition in rare-class scenarios, enhancing model robustness.",
        "novelty_score": 0.5,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "state-of-the-art",
      "source code"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal intent recognition",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Prototype-aware contrastive alignment",
      "resolved_canonical": "Prototype-guided Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Coarse-to-fine attention fusion",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.83,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Rare-class recognition",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# MVCL-DAF++: Enhancing Multimodal Intent Recognition via Prototype-Aware Contrastive Alignment and Coarse-to-Fine Dynamic Attention Fusion

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17446.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.17446](https://arxiv.org/abs/2509.17446)

## 🔗 유사한 논문
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (84.3% similar)
- [[2025-09-22/Towards Robust Visual Continual Learning with Multi-Prototype Supervision_20250922|Towards Robust Visual Continual Learning with Multi-Prototype Supervision]] (83.7% similar)
- [[2025-09-23/AIMMerging_ Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning_20250923|AIMMerging: Adaptive Iterative Model Merging Using Training Trajectories for Language Model Continual Learning]] (83.1% similar)
- [[2025-09-17/MOCHA_ Multi-modal Objects-aware Cross-arcHitecture Alignment_20250917|MOCHA: Multi-modal Objects-aware Cross-arcHitecture Alignment]] (82.5% similar)
- [[2025-09-23/From Easy to Hard_ The MIR Benchmark for Progressive Interleaved Multi-Image Reasoning_20250923|From Easy to Hard: The MIR Benchmark for Progressive Interleaved Multi-Image Reasoning]] (82.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Attention Mechanism|Attention Mechanism]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Prototype-guided Learning|Prototype-guided Learning]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17446v1 Announce Type: cross 
Abstract: Multimodal intent recognition (MMIR) suffers from weak semantic grounding and poor robustness under noisy or rare-class conditions. We propose MVCL-DAF++, which extends MVCL-DAF with two key modules: (1) Prototype-aware contrastive alignment, aligning instances to class-level prototypes to enhance semantic consistency; and (2) Coarse-to-fine attention fusion, integrating global modality summaries with token-level features for hierarchical cross-modal interaction. On MIntRec and MIntRec2.0, MVCL-DAF++ achieves new state-of-the-art results, improving rare-class recognition by +1.05\% and +4.18\% WF1, respectively. These results demonstrate the effectiveness of prototype-guided learning and coarse-to-fine fusion for robust multimodal understanding. The source code is available at https://github.com/chr1s623/MVCL-DAF-PlusPlus.

## 📝 요약

다중 모달 의도 인식(MMIR)의 문제점인 약한 의미적 기반과 노이즈 또는 희귀 클래스 조건에서의 낮은 강건성을 개선하기 위해 MVCL-DAF++를 제안합니다. 이 모델은 두 가지 주요 모듈을 포함합니다: (1) 프로토타입 기반 대조 정렬로, 인스턴스를 클래스 수준의 프로토타입에 맞춰 의미적 일관성을 강화하고, (2) 거칠게부터 세밀하게 주의 융합하여 전역 모달 요약과 토큰 수준의 특징을 통합해 계층적 교차 모달 상호작용을 촉진합니다. MIntRec 및 MIntRec2.0 데이터셋에서 MVCL-DAF++는 희귀 클래스 인식을 각각 +1.05% 및 +4.18% WF1 향상시키며 새로운 최첨단 결과를 달성했습니다. 이는 프로토타입 기반 학습과 거칠게부터 세밀하게 융합하는 접근법이 강건한 다중 모달 이해에 효과적임을 보여줍니다. 소스 코드는 https://github.com/chr1s623/MVCL-DAF-PlusPlus에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. MVCL-DAF++는 프로토타입 인식 대비 정렬과 세분화된 주의 융합을 통해 멀티모달 의도 인식의 의미적 일관성을 강화합니다.
- 2. 제안된 방법은 MIntRec와 MIntRec2.0 데이터셋에서 희귀 클래스 인식 성능을 각각 +1.05%와 +4.18% WF1로 향상시켜 새로운 최첨단 결과를 달성했습니다.
- 3. 프로토타입 기반 학습과 세분화된 융합은 강력한 멀티모달 이해를 위한 효과적인 접근법임을 입증했습니다.
- 4. 제안된 방법의 소스 코드는 https://github.com/chr1s623/MVCL-DAF-PlusPlus에서 제공됩니다.


---

*Generated on 2025-09-23 23:56:15*