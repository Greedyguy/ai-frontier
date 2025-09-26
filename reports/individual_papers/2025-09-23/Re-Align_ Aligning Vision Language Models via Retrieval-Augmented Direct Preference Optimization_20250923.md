---
keywords:
  - Vision-Language Model
  - Direct Preference Optimization
  - Reinforcement Learning from Human Feedback
  - Visual Question-Answering
  - Image Retrieval
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2502.13146
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:01:32.711917",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Direct Preference Optimization",
    "Reinforcement Learning from Human Feedback",
    "Visual Question-Answering",
    "Image Retrieval"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.92,
    "Direct Preference Optimization": 0.8,
    "Reinforcement Learning from Human Feedback": 0.85,
    "Visual Question-Answering": 0.78,
    "Image Retrieval": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "Vision-Language Models"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's focus on cross-modal applications and are a trending concept.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.85,
        "link_intent_score": 0.92
      },
      {
        "surface": "Direct Preference Optimization",
        "canonical": "Direct Preference Optimization",
        "aliases": [
          "DPO"
        ],
        "category": "unique_technical",
        "rationale": "Direct Preference Optimization is a unique technique introduced in the paper for aligning models, offering new insights.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Reinforcement Learning from Human Feedback",
        "canonical": "Reinforcement Learning from Human Feedback",
        "aliases": [
          "RLHF"
        ],
        "category": "specific_connectable",
        "rationale": "RLHF is a well-known technique that connects with existing literature on model alignment strategies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Visual Question-Answering",
        "canonical": "Visual Question-Answering",
        "aliases": [
          "VQA"
        ],
        "category": "specific_connectable",
        "rationale": "Visual Question-Answering is a specific application area that benefits from the discussed alignment techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Image Retrieval",
        "canonical": "Image Retrieval",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Image Retrieval is a fundamental component of the proposed alignment framework, linking visual data with textual data.",
        "novelty_score": 0.3,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "hallucinations",
      "performance gains",
      "real-world scenarios"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.85,
        "link_intent": 0.92
      }
    },
    {
      "candidate_surface": "Direct Preference Optimization",
      "resolved_canonical": "Direct Preference Optimization",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Reinforcement Learning from Human Feedback",
      "resolved_canonical": "Reinforcement Learning from Human Feedback",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Visual Question-Answering",
      "resolved_canonical": "Visual Question-Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Image Retrieval",
      "resolved_canonical": "Image Retrieval",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Re-Align: Aligning Vision Language Models via Retrieval-Augmented Direct Preference Optimization

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2502.13146.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2502.13146](https://arxiv.org/abs/2502.13146)

## 🔗 유사한 논문
- [[2025-09-23/Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization_20250923|Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization]] (87.2% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (86.5% similar)
- [[2025-09-23/LifeAlign_ Lifelong Alignment for Large Language Models with Memory-Augmented Focalized Preference Optimization_20250923|LifeAlign: Lifelong Alignment for Large Language Models with Memory-Augmented Focalized Preference Optimization]] (86.1% similar)
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (85.9% similar)
- [[2025-09-23/When Big Models Train Small Ones_ Label-Free Model Parity Alignment for Efficient Visual Question Answering using Small VLMs_20250923|When Big Models Train Small Ones: Label-Free Model Parity Alignment for Efficient Visual Question Answering using Small VLMs]] (85.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Image Retrieval|Image Retrieval]]
**🔗 Specific Connectable**: [[keywords/Reinforcement Learning from Human Feedback|Reinforcement Learning from Human Feedback]], [[keywords/Visual Question-Answering|Visual Question-Answering]]
**⚡ Unique Technical**: [[keywords/Direct Preference Optimization|Direct Preference Optimization]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.13146v3 Announce Type: replace-cross 
Abstract: The emergence of large Vision Language Models (VLMs) has broadened the scope and capabilities of single-modal Large Language Models (LLMs) by integrating visual modalities, thereby unlocking transformative cross-modal applications in a variety of real-world scenarios. Despite their impressive performance, VLMs are prone to significant hallucinations, particularly in the form of cross-modal inconsistencies. Building on the success of Reinforcement Learning from Human Feedback (RLHF) in aligning LLMs, recent advancements have focused on applying direct preference optimization (DPO) on carefully curated datasets to mitigate these issues. Yet, such approaches typically introduce preference signals in a brute-force manner, neglecting the crucial role of visual information in the alignment process. In this paper, we introduce Re-Align, a novel alignment framework that leverages image retrieval to construct a dual-preference dataset, effectively incorporating both textual and visual preference signals. We further introduce rDPO, an extension of the standard direct preference optimization that incorporates an additional visual preference objective during fine-tuning. Our experimental results demonstrate that Re-Align not only mitigates hallucinations more effectively than previous methods but also yields significant performance gains in general visual question-answering (VQA) tasks. Moreover, we show that Re-Align maintains robustness and scalability across a wide range of VLM sizes and architectures. This work represents a significant step forward in aligning multimodal LLMs, paving the way for more reliable and effective cross-modal applications. We release all the code in https://github.com/taco-group/Re-Align.

## 📝 요약

이 논문은 대규모 비전 언어 모델(VLM)의 환각 문제, 특히 교차 모달 불일치를 해결하기 위해 새로운 정렬 프레임워크인 Re-Align을 제안합니다. Re-Align은 이미지 검색을 활용하여 텍스트와 시각적 선호 신호를 모두 포함하는 이중 선호 데이터셋을 구축합니다. 또한, 시각적 선호 목표를 추가한 rDPO를 도입하여 기존 방법보다 환각을 효과적으로 줄이고, 일반적인 시각적 질문 응답(VQA) 작업에서 성능을 향상시킵니다. Re-Align은 다양한 VLM 크기와 아키텍처에서 견고성과 확장성을 유지하며, 멀티모달 LLM 정렬에 중요한 진전을 이룹니다.

## 🎯 주요 포인트

- 1. 대형 비전 언어 모델(VLM)은 시각적 모달리티를 통합하여 단일 모달 대형 언어 모델(LLM)의 범위와 기능을 확장합니다.
- 2. VLM은 특히 교차 모달 불일치 형태의 환각에 취약하며, 이를 해결하기 위해 인간 피드백을 통한 강화 학습(RLHF)과 직접 선호 최적화(DPO)가 사용됩니다.
- 3. Re-Align은 이미지 검색을 활용하여 텍스트와 시각적 선호 신호를 모두 포함하는 이중 선호 데이터셋을 구축하는 새로운 정렬 프레임워크입니다.
- 4. rDPO는 표준 직접 선호 최적화의 확장으로, 시각적 선호 목표를 추가하여 미세 조정 중에 적용됩니다.
- 5. Re-Align은 환각을 효과적으로 줄이고 일반적인 시각적 질문 응답(VQA) 작업에서 성능 향상을 보여주며, 다양한 VLM 크기와 아키텍처에 걸쳐 견고성과 확장성을 유지합니다.


---

*Generated on 2025-09-24 03:01:32*