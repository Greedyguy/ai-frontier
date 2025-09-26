---
keywords:
  - Semantic Orientation
  - 6-DoF Spatial Reasoning
  - Zero-Shot Learning
  - Vision-Language Model
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2502.13143
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:19:18.375273",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Semantic Orientation",
    "6-DoF Spatial Reasoning",
    "Zero-Shot Learning",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Semantic Orientation": 0.78,
    "6-DoF Spatial Reasoning": 0.72,
    "Zero-Shot Learning": 0.8,
    "Vision-Language Model": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "semantic orientation",
        "canonical": "Semantic Orientation",
        "aliases": [
          "natural language orientation",
          "reference-frame-free orientation"
        ],
        "category": "unique_technical",
        "rationale": "Semantic orientation introduces a novel approach to defining object orientations using natural language, which is crucial for linking spatial reasoning and object manipulation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "6-DoF spatial reasoning",
        "canonical": "6-DoF Spatial Reasoning",
        "aliases": [
          "six degrees of freedom reasoning"
        ],
        "category": "unique_technical",
        "rationale": "6-DoF spatial reasoning is essential for understanding complex object manipulation tasks, providing a strong link to robotics and spatial analysis.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.85,
        "link_intent_score": 0.72
      },
      {
        "surface": "zero-shot semantic orientation prediction",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "zero-shot prediction",
          "zero-shot orientation"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot learning is a trending concept that enhances the model's ability to predict semantic orientations without prior examples, linking to broader machine learning strategies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "vision-language agent"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are crucial for integrating semantic orientation into agents, bridging visual and linguistic data for enhanced reasoning.",
        "novelty_score": 0.6,
        "connectivity_score": 0.9,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "object localization",
      "traditional pose representations"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "semantic orientation",
      "resolved_canonical": "Semantic Orientation",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "6-DoF spatial reasoning",
      "resolved_canonical": "6-DoF Spatial Reasoning",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.85,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "zero-shot semantic orientation prediction",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.9,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# SoFar: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2502.13143.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2502.13143](https://arxiv.org/abs/2502.13143)

## 🔗 유사한 논문
- [[2025-09-23/FoREST_ Frame of Reference Evaluation in Spatial Reasoning Tasks_20250923|FoREST: Frame of Reference Evaluation in Spatial Reasoning Tasks]] (82.9% similar)
- [[2025-09-23/SD-VLM_ Spatial Measuring and Understanding with Depth-Encoded Vision-Language Models_20250923|SD-VLM: Spatial Measuring and Understanding with Depth-Encoded Vision-Language Models]] (82.7% similar)
- [[2025-09-22/Spatial Understanding from Videos_ Structured Prompts Meet Simulation Data_20250922|Spatial Understanding from Videos: Structured Prompts Meet Simulation Data]] (82.5% similar)
- [[2025-09-24/Do It Yourself_ Learning Semantic Correspondence from Pseudo-Labels_20250924|Do It Yourself: Learning Semantic Correspondence from Pseudo-Labels]] (81.8% similar)
- [[2025-09-24/How Far are VLMs from Visual Spatial Intelligence? A Benchmark-Driven Perspective_20250924|How Far are VLMs from Visual Spatial Intelligence? A Benchmark-Driven Perspective]] (81.8% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Semantic Orientation|Semantic Orientation]], [[keywords/6-DoF Spatial Reasoning|6-DoF Spatial Reasoning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.13143v2 Announce Type: replace-cross 
Abstract: While spatial reasoning has made progress in object localization relationships, it often overlooks object orientation-a key factor in 6-DoF fine-grained manipulation. Traditional pose representations rely on pre-defined frames or templates, limiting generalization and semantic grounding. In this paper, we introduce the concept of semantic orientation, which defines object orientations using natural language in a reference-frame-free manner (e.g., the "plug-in" direction of a USB or the "handle" direction of a cup). To support this, we construct OrienText300K, a large-scale dataset of 3D objects annotated with semantic orientations, and develop PointSO, a general model for zero-shot semantic orientation prediction. By integrating semantic orientation into VLM agents, our SoFar framework enables 6-DoF spatial reasoning and generates robotic actions. Extensive experiments demonstrated the effectiveness and generalization of our SoFar, e.g., zero-shot 48.7% successful rate on Open6DOR and zero-shot 74.9% successful rate on SIMPLER-Env.

## 📝 요약

이 논문은 객체의 방향성을 자연어로 정의하는 '의미론적 방향성' 개념을 제안하여 6자유도(6-DoF) 세밀한 조작에서의 공간 추론을 개선합니다. 이를 위해 3D 객체에 의미론적 방향성을 주석한 대규모 데이터셋 OrienText300K를 구축하고, 제로샷 의미론적 방향성 예측을 위한 모델 PointSO를 개발했습니다. 제안된 SoFar 프레임워크는 VLM 에이전트에 의미론적 방향성을 통합하여 6-DoF 공간 추론과 로봇 행동 생성을 가능하게 합니다. 실험 결과, SoFar는 Open6DOR에서 48.7%, SIMPLER-Env에서 74.9%의 제로샷 성공률을 보여 효과성과 일반화를 입증했습니다.

## 🎯 주요 포인트

- 1. 기존의 공간 추론은 객체의 방향성을 간과하여 6-DoF 세밀한 조작에 한계가 있다.
- 2. 본 논문에서는 자연어를 사용하여 참조 프레임 없이 객체의 방향을 정의하는 '의미론적 방향' 개념을 도입하였다.
- 3. 3D 객체에 의미론적 방향을 주석으로 달아놓은 대규모 데이터셋 OrienText300K를 구축하였다.
- 4. 제로샷 의미론적 방향 예측을 위한 일반 모델 PointSO를 개발하였다.
- 5. SoFar 프레임워크는 의미론적 방향을 VLM 에이전트에 통합하여 6-DoF 공간 추론 및 로봇 행동 생성을 가능하게 한다.


---

*Generated on 2025-09-25 16:19:18*