---
keywords:
  - Large Language Model
  - Visual Program Reasoning
  - Vision-Language Model
  - Fast-Slow Reasoning Framework
  - Parameter Search
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2509.17743
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:01:28.877566",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Visual Program Reasoning",
    "Vision-Language Model",
    "Fast-Slow Reasoning Framework",
    "Parameter Search"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Visual Program Reasoning": 0.78,
    "Vision-Language Model": 0.8,
    "Fast-Slow Reasoning Framework": 0.82,
    "Parameter Search": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are central to the paper's approach and connect to existing research in language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Visual Program Reasoning",
        "canonical": "Visual Program Reasoning",
        "aliases": [
          "Visual Reasoning"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel approach introduced in the paper, providing a unique perspective on videoQA.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VideoLLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are crucial for the integration of visual and textual data in the paper.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "Fast-Slow Reasoning Framework",
        "canonical": "Fast-Slow Reasoning Framework",
        "aliases": [
          "FS-VisPR"
        ],
        "category": "unique_technical",
        "rationale": "This framework is a key contribution of the paper, offering a new method for handling complex queries.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Parameter Search",
        "canonical": "Parameter Search",
        "aliases": [
          "Parameter Tuning"
        ],
        "category": "specific_connectable",
        "rationale": "Parameter search is a critical component for optimizing visual programs, linking to broader optimization techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "program workflows",
      "subtitle retrieval"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Visual Program Reasoning",
      "resolved_canonical": "Visual Program Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Fast-Slow Reasoning Framework",
      "resolved_canonical": "Fast-Slow Reasoning Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Parameter Search",
      "resolved_canonical": "Parameter Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Adaptive Fast-and-Slow Visual Program Reasoning for Long-Form VideoQA

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17743.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2509.17743](https://arxiv.org/abs/2509.17743)

## 🔗 유사한 논문
- [[2025-09-23/ProReason_ Multi-Modal Proactive Reasoning with Decoupled Eyesight and Wisdom_20250923|ProReason: Multi-Modal Proactive Reasoning with Decoupled Eyesight and Wisdom]] (85.8% similar)
- [[2025-09-23/Open Vision Reasoner_ Transferring Linguistic Cognitive Behavior for Visual Reasoning_20250923|Open Vision Reasoner: Transferring Linguistic Cognitive Behavior for Visual Reasoning]] (84.7% similar)
- [[2025-09-23/Eye Gaze Tells You Where to Compute_ Gaze-Driven Efficient VLMs_20250923|Eye Gaze Tells You Where to Compute: Gaze-Driven Efficient VLMs]] (83.6% similar)
- [[2025-09-22/Think, Verbalize, then Speak_ Bridging Complex Thoughts and Comprehensible Speech_20250922|Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech]] (83.0% similar)
- [[2025-09-23/ProtoVQA_ An Adaptable Prototypical Framework for Explainable Fine-Grained Visual Question Answering_20250923|ProtoVQA: An Adaptable Prototypical Framework for Explainable Fine-Grained Visual Question Answering]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Parameter Search|Parameter Search]]
**⚡ Unique Technical**: [[keywords/Visual Program Reasoning|Visual Program Reasoning]], [[keywords/Fast-Slow Reasoning Framework|Fast-Slow Reasoning Framework]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17743v1 Announce Type: new 
Abstract: Large language models (LLMs) have shown promise in generating program workflows for visual tasks. However, previous approaches often rely on closed-source models, lack systematic reasoning, and struggle with long-form video question answering (videoQA). To address these challenges, we introduce the FS-VisPR framework, an adaptive visual program reasoning approach that balances fast reasoning for simple queries with slow reasoning for difficult ones. First, we design efficient visual modules (e.g., key clip retrieval and subtitle retrieval) to support long-form video tasks. Then, we construct a diverse and high-quality fast-slow reasoning dataset with a strong LLM to align open-source language models' ability to generate visual program workflows as FS-LLM. Next, we design a fast-slow reasoning framework with FS-LLM: Simple queries are directly solved by VideoLLMs, while difficult ones invoke visual program reasoning, motivated by human-like reasoning processes. During this process, low-confidence fast-thinking answers will trigger a second-stage slow-reasoning process, and a fallback mechanism to fast reasoning is activated if the program execution fails. Moreover, we improve visual programs through parameter search during both training and inference. By adjusting the parameters of the visual modules within the program, multiple variants are generated: during training, programs that yield correct answers are selected, while during inference, the program with the highest confidence result is applied. Experiments show that FS-VisPR improves both efficiency and reliability in visual program workflows. It achieves 50.4% accuracy on LVBench, surpassing GPT-4o, matching the performance of Qwen2.5VL-72B on VideoMME.

## 📝 요약

FS-VisPR 프레임워크는 시각적 프로그램 추론을 통해 장문의 비디오 질문 응답(videoQA) 문제를 해결하는 접근법입니다. 이 프레임워크는 간단한 쿼리에는 빠른 추론을, 복잡한 쿼리에는 느린 추론을 적용하여 효율성을 높입니다. 이를 위해 키 클립 및 자막 검색과 같은 효율적인 시각 모듈을 설계하고, 다양한 빠른-느린 추론 데이터셋을 구축하여 오픈소스 언어 모델의 시각 프로그램 워크플로우 생성 능력을 강화했습니다. FS-LLM을 활용한 이 프레임워크는 인간의 사고 과정을 모방하여, 낮은 신뢰도의 빠른 추론 결과는 느린 추론 단계로 전환하며, 프로그램 실행 실패 시 빠른 추론으로 복귀합니다. 또한, 시각 모듈의 매개변수 조정을 통해 다양한 프로그램 변형을 생성하고, 훈련 및 추론 과정에서 최적의 프로그램을 선택합니다. 실험 결과, FS-VisPR은 LVBench에서 50.4%의 정확도를 기록하며, GPT-4o를 능가하고 Qwen2.5VL-72B와 유사한 성능을 보였습니다.

## 🎯 주요 포인트

- 1. FS-VisPR 프레임워크는 간단한 쿼리에는 빠른 추론을, 어려운 쿼리에는 느린 추론을 적용하여 비주얼 프로그램 워크플로우를 생성합니다.
- 2. 효율적인 비주얼 모듈(예: 키 클립 검색 및 자막 검색)을 설계하여 장기 비디오 작업을 지원합니다.
- 3. FS-LLM을 통해 오픈 소스 언어 모델의 비주얼 프로그램 워크플로우 생성 능력을 강화하고, 다양한 고품질의 빠른-느린 추론 데이터셋을 구축합니다.
- 4. 낮은 신뢰도의 빠른 추론 답변은 두 번째 단계의 느린 추론 과정을 유발하며, 프로그램 실행 실패 시 빠른 추론으로 되돌아가는 메커니즘이 작동합니다.
- 5. FS-VisPR은 LVBench에서 50.4%의 정확도를 달성하며, GPT-4o를 능가하고 Qwen2.5VL-72B와 성능을 맞춥니다.


---

*Generated on 2025-09-24 05:01:28*