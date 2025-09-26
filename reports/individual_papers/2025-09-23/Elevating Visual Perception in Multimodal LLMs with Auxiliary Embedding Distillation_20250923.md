---
keywords:
  - Multimodal Learning
  - Computer Vision
  - Embedding Distillation
  - Vision-Language Model
category: cs.CV
publish_date: 2025-09-23
arxiv_id: 2412.09585
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T05:16:37.829966",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Computer Vision",
    "Embedding Distillation",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.78,
    "Computer Vision": 0.72,
    "Embedding Distillation": 0.77,
    "Vision-Language Model": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal LLMs",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal Large Language Models"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to recent trends in integrating multiple data modalities within language models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Visual Perception",
        "canonical": "Computer Vision",
        "aliases": [
          "Visual Understanding"
        ],
        "category": "broad_technical",
        "rationale": "Links to the domain of computer vision which is integral to the paper's focus on visual data.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      },
      {
        "surface": "Embedding Distillation",
        "canonical": "Embedding Distillation",
        "aliases": [
          "Knowledge Distillation for Embeddings"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel technique specific to the paper's methodology.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.77
      },
      {
        "surface": "Vision Encoder",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision Encoder Models"
        ],
        "category": "evolved_concepts",
        "rationale": "Represents the integration of vision and language processing, a key concept in the study.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.68,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "natural language supervision",
      "spatial reasoning",
      "embodied AI"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal LLMs",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Visual Perception",
      "resolved_canonical": "Computer Vision",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "Embedding Distillation",
      "resolved_canonical": "Embedding Distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Vision Encoder",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.68,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Elevating Visual Perception in Multimodal LLMs with Auxiliary Embedding Distillation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2412.09585.pdf)
**Category**: cs.CV
**Published**: 2025-09-23
**ArXiv ID**: [2412.09585](https://arxiv.org/abs/2412.09585)

## 🔗 유사한 논문
- [[2025-09-22/Perception-R1_ Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward_20250922|Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward]] (87.9% similar)
- [[2025-09-22/LLMs Can Compensate for Deficiencies in Visual Representations_20250922|LLMs Can Compensate for Deficiencies in Visual Representations]] (86.4% similar)
- [[2025-09-23/Catching the Details_ Self-Distilled RoI Predictors for Fine-Grained MLLM Perception_20250923|Catching the Details: Self-Distilled RoI Predictors for Fine-Grained MLLM Perception]] (86.1% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (84.6% similar)
- [[2025-09-23/GeoPQA_ Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning_20250923|GeoPQA: Bridging the Visual Perception Gap in MLLMs for Geometric Reasoning]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Computer Vision|Computer Vision]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Embedding Distillation|Embedding Distillation]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.09585v2 Announce Type: replace 
Abstract: In recent times, the standard practice for developing MLLMs is to feed features from vision encoder(s) into the LLM and train with natural language supervision. This approach often causes models to lean towards language comprehension and undermine the rich visual perception signals present in the data, which are critical for tasks involving spatial reasoning in the domain of embodied AI and robotics. Is it possible to optimize both at the same time? In this work, we propose VisPer-LM, the first approach that infuses visual perception knowledge from expert vision encoders into the LLM's (of an MLLM) hidden representations. We start by investigating MLLMs trained solely with natural language supervision and identify a positive correlation between the quality of visual representations within these models and their downstream performance. Given this insight, we formulate the objective during the pretraining stage in MLLMs as a coupled optimization of predictive visual embedding and next (text) token prediction. Moreover, through extensive probing, we observe improved visual representation quality due to embedding optimization, underscoring the effectiveness of our probing setup. We demonstrate that our VisPer-LM outperforms the single and multi-encoder baselines, proving our approach's superiority over explicitly feeding the corresponding features to the LLM. In particular, VisPer-LM boosts performance by an average margin of up to 2.5% on various benchmarks, with a notable improvement of 8.7% on the Depth task in CV-Bench.

## 📝 요약

최근 MLLM 개발에서는 비전 인코더의 특징을 LLM에 입력하고 자연어 감독으로 학습하는 것이 일반적입니다. 그러나 이는 언어 이해에 치우쳐 공간적 추론이 중요한 영역에서 시각적 인식 신호를 간과할 수 있습니다. 본 연구에서는 VisPer-LM을 제안하여 전문가 비전 인코더의 시각적 인식 지식을 MLLM의 숨겨진 표현에 주입합니다. 자연어 감독으로만 학습된 MLLM을 분석한 결과, 시각적 표현의 질과 다운스트림 성능 간의 긍정적 상관관계를 확인했습니다. 이를 바탕으로 예측 시각 임베딩과 다음 텍스트 토큰 예측의 결합 최적화를 목표로 설정했습니다. VisPer-LM은 단일 및 다중 인코더 기반을 능가하며, 특히 CV-Bench의 Depth 작업에서 8.7%의 성능 향상을 보였습니다.

## 🎯 주요 포인트

- 1. VisPer-LM은 전문 비전 인코더의 시각적 지식을 MLLM의 숨겨진 표현에 주입하는 최초의 접근법을 제안합니다.
- 2. 자연어 감독만으로 훈련된 MLLM에서 시각적 표현의 품질과 다운스트림 성능 간의 긍정적인 상관관계를 확인했습니다.
- 3. 사전 훈련 단계에서 예측 시각 임베딩과 다음 텍스트 토큰 예측의 결합 최적화를 목표로 설정했습니다.
- 4. VisPer-LM은 단일 및 다중 인코더 기준 모델을 능가하며, CV-Bench의 Depth 과제에서 8.7%의 성능 향상을 포함하여 다양한 벤치마크에서 평균 2.5%의 성능 향상을 보였습니다.
- 5. 임베딩 최적화를 통해 시각적 표현의 품질이 향상되었음을 광범위한 프로빙을 통해 관찰했습니다.


---

*Generated on 2025-09-24 05:16:37*