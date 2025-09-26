---
keywords:
  - Vision-Language Model
  - Open-Vocabulary Semantic Segmentation
  - Source-Free Domain Adaptation
  - Zero-Shot Learning
category: cs.CV
publish_date: 2025-09-25
arxiv_id: 2509.15225
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T09:28:47.173593",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Open-Vocabulary Semantic Segmentation",
    "Source-Free Domain Adaptation",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Open-Vocabulary Semantic Segmentation": 0.8,
    "Source-Free Domain Adaptation": 0.78,
    "Zero-Shot Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Links to the trending concept of integrating vision and language tasks, crucial for semantic segmentation.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Open-Vocabulary Semantic Segmentation",
        "canonical": "Open-Vocabulary Semantic Segmentation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a specialized task in computer vision, connecting to domain adaptation and segmentation.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Source-Free Domain Adaptation",
        "canonical": "Source-Free Domain Adaptation",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Highlights a novel approach in domain adaptation without source data, relevant for linking adaptation strategies.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Zero-Shot Segmentation",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-Shot Segmentation"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the concept of learning without prior examples, important for segmentation tasks.",
        "novelty_score": 0.6,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "pseudo-label generation",
      "Top-K class selection"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Open-Vocabulary Semantic Segmentation",
      "resolved_canonical": "Open-Vocabulary Semantic Segmentation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Source-Free Domain Adaptation",
      "resolved_canonical": "Source-Free Domain Adaptation",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Zero-Shot Segmentation",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Lost in Translation? Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15225.pdf)
**Category**: cs.CV
**Published**: 2025-09-25
**ArXiv ID**: [2509.15225](https://arxiv.org/abs/2509.15225)

## 🔗 유사한 논문
- [[2025-09-18/Lost in Translation? Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation_20250918|Lost in Translation? Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation]] (99.4% similar)
- [[2025-09-23/Depth Edge Alignment Loss_ DEALing with Depth in Weakly Supervised Semantic Segmentation_20250923|Depth Edge Alignment Loss: DEALing with Depth in Weakly Supervised Semantic Segmentation]] (83.9% similar)
- [[2025-09-24/MOCHA_ Multi-modal Objects-aware Cross-arcHitecture Alignment_20250924|MOCHA: Multi-modal Objects-aware Cross-arcHitecture Alignment]] (83.5% similar)
- [[2025-09-23/Re-Align_ Aligning Vision Language Models via Retrieval-Augmented Direct Preference Optimization_20250923|Re-Align: Aligning Vision Language Models via Retrieval-Augmented Direct Preference Optimization]] (83.0% similar)
- [[2025-09-24/No Labels Needed_ Zero-Shot Image Classification with Collaborative Self-Learning_20250924|No Labels Needed: Zero-Shot Image Classification with Collaborative Self-Learning]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Open-Vocabulary Semantic Segmentation|Open-Vocabulary Semantic Segmentation]], [[keywords/Source-Free Domain Adaptation|Source-Free Domain Adaptation]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15225v2 Announce Type: replace 
Abstract: We introduce VocAlign, a novel source-free domain adaptation framework specifically designed for VLMs in open-vocabulary semantic segmentation. Our method adopts a student-teacher paradigm enhanced with a vocabulary alignment strategy, which improves pseudo-label generation by incorporating additional class concepts. To ensure efficiency, we use Low-Rank Adaptation (LoRA) to fine-tune the model, preserving its original capabilities while minimizing computational overhead. In addition, we propose a Top-K class selection mechanism for the student model, which significantly reduces memory requirements while further improving adaptation performance. Our approach achieves a notable 6.11 mIoU improvement on the CityScapes dataset and demonstrates superior performance on zero-shot segmentation benchmarks, setting a new standard for source-free adaptation in the open-vocabulary setting.

## 📝 요약

VocAlign은 VLMs의 오픈 보캐뷸러리 의미론적 분할을 위한 새로운 소스 프리 도메인 적응 프레임워크입니다. 학생-교사 패러다임과 어휘 정렬 전략을 통해 추가 클래스 개념을 포함하여 가짜 레이블 생성을 개선합니다. LoRA를 사용하여 모델을 미세 조정함으로써 효율성을 유지하고, Top-K 클래스 선택 메커니즘을 도입하여 메모리 요구 사항을 줄이면서 적응 성능을 향상시킵니다. 이 접근법은 CityScapes 데이터셋에서 6.11 mIoU 개선을 이루었으며, 제로샷 분할 벤치마크에서 우수한 성능을 보여 소스 프리 적응의 새로운 기준을 세웠습니다.

## 🎯 주요 포인트

- 1. VocAlign은 개방형 어휘 의미 분할을 위한 VLM에 특화된 소스 프리 도메인 적응 프레임워크입니다.
- 2. 학생-교사 패러다임과 어휘 정렬 전략을 채택하여 추가 클래스 개념을 포함한 가짜 레이블 생성을 개선합니다.
- 3. LoRA를 사용하여 모델을 미세 조정함으로써 원래의 기능을 유지하면서 계산 오버헤드를 최소화합니다.
- 4. 학생 모델을 위한 Top-K 클래스 선택 메커니즘을 제안하여 메모리 요구 사항을 크게 줄이고 적응 성능을 향상시킵니다.
- 5. CityScapes 데이터셋에서 6.11 mIoU 개선을 달성하고, 제로샷 분할 벤치마크에서 우수한 성능을 보여줍니다.


---

*Generated on 2025-09-26 09:28:47*