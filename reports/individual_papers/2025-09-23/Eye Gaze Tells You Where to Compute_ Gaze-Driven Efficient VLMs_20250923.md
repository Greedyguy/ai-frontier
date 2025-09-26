---
keywords:
  - Vision-Language Model
  - GazeVLM
  - Fovea-Periphery Perception
  - Human Eye Gaze
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.16476
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:22:21.235745",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "GazeVLM",
    "Fovea-Periphery Perception",
    "Human Eye Gaze"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "GazeVLM": 0.78,
    "Fovea-Periphery Perception": 0.77,
    "Human Eye Gaze": 0.8
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
        "rationale": "Vision-Language Models are central to the paper's discussion and align with recent trends in multimodal AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.72,
        "link_intent_score": 0.85
      },
      {
        "surface": "GazeVLM",
        "canonical": "GazeVLM",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "GazeVLM is the novel framework introduced in the paper, offering a unique approach to efficient VLM inference.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.89,
        "link_intent_score": 0.78
      },
      {
        "surface": "Fovea-Periphery Perception",
        "canonical": "Fovea-Periphery Perception",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is crucial for understanding the proposed method's efficiency in processing visual tokens.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Human Eye Gaze",
        "canonical": "Human Eye Gaze",
        "aliases": [
          "Eye Gaze"
        ],
        "category": "specific_connectable",
        "rationale": "Human Eye Gaze is a key supervisory signal in the proposed framework, linking human attention to computational efficiency.",
        "novelty_score": 0.6,
        "connectivity_score": 0.78,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "edge consumer devices",
      "real-time use",
      "inference efficiency"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.72,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "GazeVLM",
      "resolved_canonical": "GazeVLM",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.89,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Fovea-Periphery Perception",
      "resolved_canonical": "Fovea-Periphery Perception",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Human Eye Gaze",
      "resolved_canonical": "Human Eye Gaze",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.78,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Eye Gaze Tells You Where to Compute: Gaze-Driven Efficient VLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16476.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.16476](https://arxiv.org/abs/2509.16476)

## 🔗 유사한 논문
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (86.2% similar)
- [[2025-09-23/The Better You Learn, The Smarter You Prune_ Towards Efficient Vision-language-action Models via Differentiable Token Pruning_20250923|The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning]] (85.3% similar)
- [[2025-09-23/When Big Models Train Small Ones_ Label-Free Model Parity Alignment for Efficient Visual Question Answering using Small VLMs_20250923|When Big Models Train Small Ones: Label-Free Model Parity Alignment for Efficient Visual Question Answering using Small VLMs]] (84.8% similar)
- [[2025-09-22/Cache-of-Thought_ Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning_20250922|Cache-of-Thought: Master-Apprentice Framework for Cost-Effective Vision Language Model Reasoning]] (84.6% similar)
- [[2025-09-23/Vision Language Models Are Not (Yet) Spelling Correctors_20250923|Vision Language Models Are Not (Yet) Spelling Correctors]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Human Eye Gaze|Human Eye Gaze]]
**⚡ Unique Technical**: [[keywords/GazeVLM|GazeVLM]], [[keywords/Fovea-Periphery Perception|Fovea-Periphery Perception]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16476v1 Announce Type: new 
Abstract: Vision-Language Models (VLMs) deliver impressive performance in understanding visual content with language instructions. However, redundancy in vision tokens results in the degenerated inference efficiency of VLMs, which hinders real-time use on edge consumer devices such as AR/VR devices. Existing efficiency methods commonly prune visual tokens using learned saliency, sparse attention schedules, or controller policies, but they often require architectural modification or access to intermediate activations. These pipelines add inference-time modules that increase compute and memory and often lead to an accuracy trade-off. Moreover, they also suffer from misalignment between the prompts and the region of interest in the images. Without human guidance, the model may focus on the wrong regions and miss small, high-frequency details when prompts or scenes change. In this paper, we propose GazeVLM, a training-free framework that uses the human eye gaze as a natural supervisory signal to allocate computation where it matters. By extracting gaze-driven regions of interest (ROIs) and optionally combining them with a low-resolution global view, GazeVLM mimics fovea-periphery perception to cut redundant visual tokens while preserving task-relevant details. We evaluate the visual question answering tasks on Qwen2.5-VL-3B/7B on the VOILA-COCO benchmark with human gaze. Quality of the answer is assessed by GPT-4o pairwise judging and a weighted score over coverage, accuracy, details, and fluency. Efficiency is measured by token counts and FLOPs. GazeVLM reduces visual tokens by up to 93.1%, total tokens by up to 59.6%, and FLOPs by 50%, while keeping better answer quality relative to full-resolution baselines. Our results show that aligning model computation with human gaze offers a simple, plug-and-play path toward efficient VLM inference on consumer devices.

## 📝 요약

Vision-Language Models(VLMs)은 시각 콘텐츠를 언어 지시와 함께 이해하는 데 뛰어난 성능을 보이지만, 비전 토큰의 중복성으로 인해 실시간 사용이 어려운 문제가 있습니다. 기존 방법들은 시각 토큰을 효율적으로 줄이기 위해 다양한 기법을 사용하지만, 이는 종종 정확도 저하를 초래합니다. 이에 반해, GazeVLM은 인간의 시선 데이터를 활용하여 중요한 부분에 계산 자원을 집중시키는 새로운 프레임워크를 제안합니다. 이 방법은 시선 기반 관심 영역을 추출하고, 필요시 저해상도 전역 뷰와 결합하여 불필요한 비전 토큰을 줄이면서도 과제 관련 세부사항을 유지합니다. 실험 결과, GazeVLM은 시각 토큰을 최대 93.1% 줄이고, 전체 토큰을 최대 59.6%, FLOPs를 50% 감소시키면서도 높은 품질의 답변을 제공합니다. 이는 소비자 기기에서 효율적인 VLM 추론을 가능하게 하는 간단한 방법을 제시합니다.

## 🎯 주요 포인트

- 1. Vision-Language Models(VLMs)의 비효율성은 시각 토큰의 중복성으로 인해 발생하며, 이는 실시간 사용을 방해합니다.
- 2. 기존의 효율성 개선 방법은 시각 토큰을 제거하지만, 이는 정확도 저하를 초래하고 추가적인 계산 및 메모리 사용을 요구합니다.
- 3. GazeVLM은 인간의 시선 데이터를 활용하여 불필요한 시각 토큰을 줄이고, 중요한 세부사항을 유지하는 훈련이 필요 없는 프레임워크입니다.
- 4. GazeVLM은 시선 기반 관심 영역을 추출하고, 필요 시 저해상도 글로벌 뷰와 결합하여 효율성을 높입니다.
- 5. GazeVLM은 시각 토큰을 최대 93.1% 줄이고, FLOPs를 50% 감소시키면서도 높은 품질의 답변을 유지합니다.


---

*Generated on 2025-09-24 04:22:21*