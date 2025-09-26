---
keywords:
  - Few-Shot Learning
  - Vision-Language Model
  - Blind Image Quality Assessment
  - Meta-Prompt Learning
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2409.05381
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:15:20.349090",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Few-Shot Learning",
    "Vision-Language Model",
    "Blind Image Quality Assessment",
    "Meta-Prompt Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Few-Shot Learning": 0.82,
    "Vision-Language Model": 0.85,
    "Blind Image Quality Assessment": 0.78,
    "Meta-Prompt Learning": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Few-Shot Image Quality Assessment",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Few-Shot IQA"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the concept of learning with limited data, which is central to the paper's approach.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Highlights the integration of visual and language data, crucial for the proposed method.",
        "novelty_score": 0.7,
        "connectivity_score": 0.88,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Blind IQA",
        "canonical": "Blind Image Quality Assessment",
        "aliases": [
          "BIQA"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specific challenge in the field addressed by the paper.",
        "novelty_score": 0.68,
        "connectivity_score": 0.75,
        "specificity_score": 0.82,
        "link_intent_score": 0.78
      },
      {
        "surface": "Meta-Prompt IQA Framework",
        "canonical": "Meta-Prompt Learning",
        "aliases": [
          "GRMP-IQA"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel framework that adapts prompts for IQA tasks.",
        "novelty_score": 0.72,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Image Quality Assessment",
      "Quality-Aware Gradient Regularization"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Few-Shot Image Quality Assessment",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.88,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Blind IQA",
      "resolved_canonical": "Blind Image Quality Assessment",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.75,
        "specificity": 0.82,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Meta-Prompt IQA Framework",
      "resolved_canonical": "Meta-Prompt Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Few-Shot Image Quality Assessment via Adaptation of Vision-Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2409.05381.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2409.05381](https://arxiv.org/abs/2409.05381)

## 🔗 유사한 논문
- [[2025-09-23/Revisiting Vision Language Foundations for No-Reference Image Quality Assessment_20250923|Revisiting Vision Language Foundations for No-Reference Image Quality Assessment]] (85.5% similar)
- [[2025-09-23/DocIQ_ A Benchmark Dataset and Feature Fusion Network for Document Image Quality Assessment_20250923|DocIQ: A Benchmark Dataset and Feature Fusion Network for Document Image Quality Assessment]] (83.2% similar)
- [[2025-09-22/MMAPG_ A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs_20250922|MMAPG: A Training-Free Framework for Multimodal Multi-hop Question Answering via Adaptive Planning Graphs]] (82.2% similar)
- [[2025-09-23/GeoPQA_ Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning_20250923|GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning]] (82.0% similar)
- [[2025-09-23/Catching the Details_ Self-Distilled RoI Predictors for Fine-Grained MLLM Perception_20250923|Catching the Details: Self-Distilled RoI Predictors for Fine-Grained MLLM Perception]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Blind Image Quality Assessment|Blind Image Quality Assessment]], [[keywords/Meta-Prompt Learning|Meta-Prompt Learning]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.05381v2 Announce Type: replace 
Abstract: Image Quality Assessment (IQA) remains an unresolved challenge in computer vision due to complex distortions, diverse image content, and limited data availability. Existing Blind IQA (BIQA) methods largely rely on extensive human annotations, which are labor-intensive and costly due to the demanding nature of creating IQA datasets. To reduce this dependency, we propose the Gradient-Regulated Meta-Prompt IQA Framework (GRMP-IQA), designed to efficiently adapt the visual-language pre-trained model, CLIP, to IQA tasks, achieving high accuracy even with limited data. GRMP-IQA consists of two core modules: (i) Meta-Prompt Pre-training Module and (ii) Quality-Aware Gradient Regularization. The Meta Prompt Pre-training Module leverages a meta-learning paradigm to pre-train soft prompts with shared meta-knowledge across different distortions, enabling rapid adaptation to various IQA tasks. On the other hand, the Quality-Aware Gradient Regularization is designed to adjust the update gradients during fine-tuning, focusing the model's attention on quality-relevant features and preventing overfitting to semantic information. Extensive experiments on standard BIQA datasets demonstrate the superior performance to the state-of-the-art BIQA methods under limited data setting. Notably, utilizing just 20% of the training data, GRMP-IQA is competitive with most existing fully supervised BIQA approaches.

## 📝 요약

이 논문은 이미지 품질 평가(IQA)의 어려움을 해결하기 위해 GRMP-IQA라는 새로운 프레임워크를 제안합니다. 기존의 BIQA 방법들은 많은 양의 인적 주석에 의존하지만, GRMP-IQA는 CLIP 모델을 IQA 작업에 효율적으로 적응시켜 적은 데이터로도 높은 정확도를 달성합니다. 이 프레임워크는 메타-프롬프트 사전 학습 모듈과 품질 인식 그래디언트 정규화를 포함합니다. 메타-프롬프트 사전 학습 모듈은 다양한 왜곡에 빠르게 적응할 수 있도록 메타-러닝 패러다임을 활용하며, 품질 인식 그래디언트 정규화는 모델이 품질 관련 특징에 집중하도록 도와줍니다. 실험 결과, GRMP-IQA는 제한된 데이터 환경에서도 기존의 BIQA 방법들보다 우수한 성능을 보였으며, 훈련 데이터의 20%만 사용해도 대부분의 기존 방법들과 경쟁할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 이미지 품질 평가(IQA)는 복잡한 왜곡, 다양한 이미지 콘텐츠, 제한된 데이터 가용성으로 인해 여전히 해결되지 않은 과제입니다.
- 2. 기존의 Blind IQA(BIQA) 방법은 많은 인적 주석에 의존하며, 이는 노동 집약적이고 비용이 많이 듭니다.
- 3. GRMP-IQA는 시각-언어 사전 학습 모델인 CLIP을 IQA 작업에 효율적으로 적응시켜, 제한된 데이터로도 높은 정확도를 달성합니다.
- 4. GRMP-IQA는 메타 프롬프트 사전 학습 모듈과 품질 인식 그래디언트 정규화라는 두 가지 핵심 모듈로 구성됩니다.
- 5. GRMP-IQA는 훈련 데이터의 20%만 사용하여도 대부분의 기존 완전 감독 BIQA 접근법과 경쟁할 수 있는 성능을 보입니다.


---

*Generated on 2025-09-24 05:15:20*