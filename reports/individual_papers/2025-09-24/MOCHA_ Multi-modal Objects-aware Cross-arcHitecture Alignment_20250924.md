<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:43:03.949686",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "MOCHA",
    "Vision-Language Model",
    "Object Detection",
    "Few-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "MOCHA": 0.78,
    "Vision-Language Model": 0.8,
    "Object Detection": 0.78,
    "Few-Shot Learning": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "MOCHA",
        "canonical": "MOCHA",
        "aliases": [
          "Multi-modal Objects-aware Cross-arcHitecture Alignment"
        ],
        "category": "unique_technical",
        "rationale": "MOCHA represents a novel approach in the paper, focusing on cross-architecture alignment, making it a unique technical concept.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language Teacher",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language Teacher"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's methodology, providing a basis for the knowledge distillation process.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Object Detector Student",
        "canonical": "Object Detection",
        "aliases": [
          "Object Detector Student"
        ],
        "category": "specific_connectable",
        "rationale": "Object Detection is a key component in the paper, linking it to broader computer vision tasks.",
        "novelty_score": 0.45,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "Few-Shot Regimes",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-Shot Regimes"
        ],
        "category": "specific_connectable",
        "rationale": "Few-Shot Learning is crucial for the paper's evaluation, highlighting its relevance in personalized detection benchmarks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "knowledge distillation",
      "translation module",
      "dual-objective loss"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "MOCHA",
      "resolved_canonical": "MOCHA",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language Teacher",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Object Detector Student",
      "resolved_canonical": "Object Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Few-Shot Regimes",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# MOCHA: Multi-modal Objects-aware Cross-arcHitecture Alignment

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.14001.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.14001](https://arxiv.org/abs/2509.14001)

## 🔗 유사한 논문
- [[2025-09-17/MOCHA_ Multi-modal Objects-aware Cross-arcHitecture Alignment_20250917|MOCHA: Multi-modal Objects-aware Cross-arcHitecture Alignment]] (98.8% similar)
- [[2025-09-23/MO R-CNN_ Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image_20250923|MO R-CNN: Multispectral Oriented R-CNN for Object Detection in Remote Sensing Image]] (84.8% similar)
- [[2025-09-19/Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities_20250919|Multimodal Knowledge Distillation for Egocentric Action Recognition Robust to Missing Modalities]] (84.7% similar)
- [[2025-09-24/LCMF_ Lightweight Cross-Modality Mambaformer for Embodied Robotics VQA_20250924|LCMF: Lightweight Cross-Modality Mambaformer for Embodied Robotics VQA]] (84.0% similar)
- [[2025-09-23/MCP_ A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models_20250923|MCP: A Control-Theoretic Orchestration Framework for Synergistic Efficiency and Interpretability in Multimodal Large Language Models]] (83.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Object Detection|Object Detection]], [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/MOCHA|MOCHA]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14001v2 Announce Type: replace-cross 
Abstract: We introduce MOCHA (Multi-modal Objects-aware Cross-arcHitecture Alignment), a knowledge distillation approach that transfers region-level multimodal semantics from a large vision-language teacher (e.g., LLaVa) into a lightweight vision-only object detector student (e.g., YOLO). A translation module maps student features into a joint space, where the training of the student and translator is guided by a dual-objective loss that enforces both local alignment and global relational consistency. Unlike prior approaches focused on dense or global alignment, MOCHA operates at the object level, enabling efficient transfer of semantics without modifying the teacher or requiring textual input at inference. We validate our method across four personalized detection benchmarks under few-shot regimes. Results show consistent gains over baselines, with a +10.1 average score improvement. Despite its compact architecture, MOCHA reaches performance on par with larger multimodal models, proving its suitability for real-world deployment.

## 📝 요약

MOCHA는 대규모 비전-언어 모델에서 경량 비전 전용 객체 탐지기로 지역 수준의 다중 모달 의미를 전이하는 지식 증류 방법입니다. 학생 모델의 특징을 공동 공간으로 변환하여 지역 정렬과 전역 관계 일관성을 동시에 유지하는 이중 목표 손실로 학습을 진행합니다. MOCHA는 객체 수준에서 의미를 효율적으로 전이하며, 교사 모델 수정이나 추론 시 텍스트 입력이 필요하지 않습니다. 네 가지 개인화된 탐지 벤치마크에서 MOCHA는 기존 방법보다 평균 10.1점 향상된 성능을 보였으며, 경량 구조임에도 대형 다중 모달 모델과 유사한 성능을 발휘하여 실제 적용에 적합함을 입증했습니다.

## 🎯 주요 포인트

- 1. MOCHA는 대형 비전-언어 교사 모델의 지역 수준 다중 모달 의미를 경량 비전 전용 객체 탐지 학생 모델로 전이하는 지식 증류 접근법입니다.
- 2. 학생 특징을 공동 공간으로 매핑하는 번역 모듈을 사용하여, 이중 목표 손실을 통해 지역 정렬과 전역 관계 일관성을 동시에 강화합니다.
- 3. MOCHA는 객체 수준에서 작동하여 교사 모델을 수정하거나 추론 시 텍스트 입력을 요구하지 않고도 효율적인 의미 전이를 가능하게 합니다.
- 4. 네 가지 개인화된 탐지 벤치마크에서 MOCHA의 성능을 검증한 결과, 기준 모델 대비 평균 10.1점의 일관된 성능 향상을 보였습니다.
- 5. MOCHA는 컴팩트한 아키텍처에도 불구하고 대형 다중 모달 모델과 동등한 성능을 발휘하여 실제 환경에서의 적합성을 입증합니다.


---

*Generated on 2025-09-24 14:43:03*