---
keywords:
  - Transformer
  - Self-supervised Learning
  - Mental Rotation
  - Vision-Language Model
category: cs.AI
publish_date: 2025-09-22
arxiv_id: 2509.15271
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T08:52:15.243666",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transformer",
    "Self-supervised Learning",
    "Mental Rotation",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Transformer": 0.85,
    "Self-supervised Learning": 0.8,
    "Mental Rotation": 0.78,
    "Vision-Language Model": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision Transformer",
        "canonical": "Transformer",
        "aliases": [
          "ViT"
        ],
        "category": "broad_technical",
        "rationale": "Transformers are central to the study and application of large vision models, providing a direct link to the broader field of deep learning.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Self-supervised ViTs",
        "canonical": "Self-supervised Learning",
        "aliases": [
          "self-supervised vision transformers"
        ],
        "category": "specific_connectable",
        "rationale": "Self-supervised learning is a key technique in enhancing model performance, particularly in capturing geometric structures.",
        "novelty_score": 0.55,
        "connectivity_score": 0.79,
        "specificity_score": 0.82,
        "link_intent_score": 0.8
      },
      {
        "surface": "Mental Rotation",
        "canonical": "Mental Rotation",
        "aliases": [
          "spatial reasoning"
        ],
        "category": "unique_technical",
        "rationale": "Mental rotation is a unique cognitive task that is central to the paper's evaluation of model capabilities.",
        "novelty_score": 0.75,
        "connectivity_score": 0.67,
        "specificity_score": 0.9,
        "link_intent_score": 0.78
      },
      {
        "surface": "Vision-Language Model",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-language models represent an evolved concept that bridges visual and textual data, relevant to the paper's exploration of model capabilities.",
        "novelty_score": 0.68,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "model representations",
      "layer by layer",
      "task difficulty"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Vision Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Self-supervised ViTs",
      "resolved_canonical": "Self-supervised Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.79,
        "specificity": 0.82,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Mental Rotation",
      "resolved_canonical": "Mental Rotation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.67,
        "specificity": 0.9,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Vision-Language Model",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Large Vision Models Can Solve Mental Rotation Problems

**Korean Title:** 대형 비전 모델은 정신 회전 문제를 해결할 수 있다.

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15271.pdf)
**Category**: cs.AI
**Published**: 2025-09-22
**ArXiv ID**: [2509.15271](https://arxiv.org/abs/2509.15271)

## 🔗 유사한 논문
- [[2025-09-22/Simulated Cortical Magnification Supports Self-Supervised Object Learning_20250922|Simulated Cortical Magnification Supports Self-Supervised Object Learning]] (83.7% similar)
- [[2025-09-22/Modeling the Human Visual System_ Comparative Insights from Response-Optimized and Task-Optimized Vision Models, Language Models, and different Readout Mechanisms_20250922|Modeling the Human Visual System: Comparative Insights from Response-Optimized and Task-Optimized Vision Models, Language Models, and different Readout Mechanisms]] (82.8% similar)
- [[2025-09-22/Which Direction to Choose? An Analysis on the Representation Power of Self-Supervised ViTs in Downstream Tasks_20250922|Which Direction to Choose? An Analysis on the Representation Power of Self-Supervised ViTs in Downstream Tasks]] (82.2% similar)
- [[2025-09-19/Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models_20250919|Leveraging Geometric Visual Illusions as Perceptual Inductive Biases for Vision Models]] (82.2% similar)
- [[2025-09-22/Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception_20250922|Emulating Human-like Adaptive Vision for Efficient and Flexible Machine Visual Perception]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Self-supervised Learning|Self-supervised Learning]]
**⚡ Unique Technical**: [[keywords/Mental Rotation|Mental Rotation]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15271v1 Announce Type: cross 
Abstract: Mental rotation is a key test of spatial reasoning in humans and has been central to understanding how perception supports cognition. Despite the success of modern vision transformers, it is still unclear how well these models develop similar abilities. In this work, we present a systematic evaluation of ViT, CLIP, DINOv2, and DINOv3 across a range of mental-rotation tasks, from simple block structures similar to those used by Shepard and Metzler to study human cognition, to more complex block figures, three types of text, and photo-realistic objects. By probing model representations layer by layer, we examine where and how these networks succeed. We find that i) self-supervised ViTs capture geometric structure better than supervised ViTs; ii) intermediate layers perform better than final layers; iii) task difficulty increases with rotation complexity and occlusion, mirroring human reaction times and suggesting similar constraints in embedding space representations.

## 🔍 Abstract (한글 번역)

arXiv:2509.15271v1 발표 유형: 교차  
초록: 정신적 회전은 인간의 공간 추론의 핵심 시험이며, 지각이 인지를 어떻게 지원하는지를 이해하는 데 중심적인 역할을 해왔습니다. 현대의 비전 트랜스포머의 성공에도 불구하고, 이러한 모델들이 유사한 능력을 얼마나 잘 개발하는지는 여전히 불분명합니다. 본 연구에서는 Shepard와 Metzler가 인간 인지를 연구하기 위해 사용한 단순한 블록 구조부터 복잡한 블록 도형, 세 가지 유형의 텍스트, 사진과 같은 현실적인 객체에 이르기까지 다양한 정신적 회전 과제를 통해 ViT, CLIP, DINOv2, DINOv3에 대한 체계적인 평가를 제시합니다. 모델 표현을 층별로 조사하여 이러한 네트워크가 어디에서 어떻게 성공하는지를 검토합니다. 우리는 i) 자가 지도 ViT가 지도 학습된 ViT보다 기하학적 구조를 더 잘 포착한다는 것, ii) 중간 층이 최종 층보다 더 잘 수행한다는 것, iii) 회전 복잡성과 폐색에 따라 과제 난이도가 증가하여 인간의 반응 시간과 유사한 제약을 임베딩 공간 표현에서 제안한다는 것을 발견했습니다.

## 📝 요약

이 연구는 인간의 공간 추론 능력을 평가하는 정신 회전 과제를 통해 최신 비전 트랜스포머(ViT, CLIP, DINOv2, DINOv3)의 성능을 체계적으로 평가합니다. 연구 결과, 자기 지도 학습된 ViT가 지도 학습된 모델보다 기하학적 구조를 더 잘 포착하며, 중간 계층이 최종 계층보다 성능이 우수하다는 것을 발견했습니다. 또한, 회전 복잡성과 가림 현상이 증가할수록 과제 난이도가 높아지며, 이는 인간의 반응 시간과 유사한 제약을 모델의 임베딩 공간에서도 나타냅니다.

## 🎯 주요 포인트

- 1. 자기 지도 학습된 비전 트랜스포머(ViT)는 지도 학습된 ViT보다 기하학적 구조를 더 잘 포착한다.
- 2. 중간 계층이 최종 계층보다 정신 회전 과제 수행에 더 우수한 성능을 보인다.
- 3. 회전 복잡성과 가림 현상이 증가함에 따라 과제 난이도가 증가하며, 이는 인간의 반응 시간과 유사한 제약을 시사한다.
- 4. 다양한 정신 회전 과제에서 ViT, CLIP, DINOv2, DINOv3 모델의 성능을 체계적으로 평가하였다.
- 5. 모델 표현을 계층별로 분석하여 네트워크가 성공하는 지점을 조사하였다.


---

*Generated on 2025-09-23 08:52:15*