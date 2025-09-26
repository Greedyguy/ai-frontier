---
keywords:
  - Vision-Language Model
  - Remote Sensing
  - Quality Assessment
  - Reinforcement Learning
  - Best-of-N Scaling
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2503.00743
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:31:28.940266",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Remote Sensing",
    "Quality Assessment",
    "Reinforcement Learning",
    "Best-of-N Scaling"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.85,
    "Remote Sensing": 0.78,
    "Quality Assessment": 0.7,
    "Reinforcement Learning": 0.8,
    "Best-of-N Scaling": 0.72
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLM",
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models are central to the paper's focus and connect well with multimodal learning trends.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Remote Sensing",
        "canonical": "Remote Sensing",
        "aliases": [
          "RS"
        ],
        "category": "unique_technical",
        "rationale": "Remote Sensing is a specific domain focus of the paper, providing a unique application context.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Quality Assessment",
        "canonical": "Quality Assessment",
        "aliases": [
          "QA"
        ],
        "category": "unique_technical",
        "rationale": "Quality Assessment is a novel aspect of the paper's methodology, focusing on data curation.",
        "novelty_score": 0.68,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.7
      },
      {
        "surface": "Reinforcement Learning",
        "canonical": "Reinforcement Learning",
        "aliases": [
          "RL"
        ],
        "category": "broad_technical",
        "rationale": "Reinforcement Learning is used in the paper for training models, linking to broader machine learning techniques.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      },
      {
        "surface": "Best-of-N Scaling",
        "canonical": "Best-of-N Scaling",
        "aliases": [
          "BoN"
        ],
        "category": "unique_technical",
        "rationale": "Best-of-N Scaling is a specific technique highlighted in the paper for improving model performance.",
        "novelty_score": 0.7,
        "connectivity_score": 0.55,
        "specificity_score": 0.78,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "data synthesis",
      "semantic relationships"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Remote Sensing",
      "resolved_canonical": "Remote Sensing",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Quality Assessment",
      "resolved_canonical": "Quality Assessment",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Reinforcement Learning",
      "resolved_canonical": "Reinforcement Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Best-of-N Scaling",
      "resolved_canonical": "Best-of-N Scaling",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.55,
        "specificity": 0.78,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models

**Korean Title:** 원격 감지 비전-언어 데이터의 품질 중심 큐레이션을 위한 학습된 스코어링 모델 활용

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2503.00743.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2503.00743](https://arxiv.org/abs/2503.00743)

## 🔗 유사한 논문
- [[2025-09-22/Vision-Language Models as Differentiable Semantic and Spatial Rewards for Text-to-3D Generation_20250922|Vision-Language Models as Differentiable Semantic and Spatial Rewards for Text-to-3D Generation]] (85.8% similar)
- [[2025-09-19/QuizRank_ Picking Images by Quizzing VLMs_20250919|QuizRank: Picking Images by Quizzing VLMs]] (84.5% similar)
- [[2025-09-22/Robust Vision-Language Models via Tensor Decomposition_ A Defense Against Adversarial Attacks_20250922|Robust Vision-Language Models via Tensor Decomposition: A Defense Against Adversarial Attacks]] (84.4% similar)
- [[2025-09-22/SAR-TEXT_ A Large-Scale SAR Image-Text Dataset Built with SAR-Narrator and Progressive Transfer Learning_20250922|SAR-TEXT: A Large-Scale SAR Image-Text Dataset Built with SAR-Narrator and Progressive Transfer Learning]] (84.2% similar)
- [[2025-09-19/UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets]] (84.0% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Reinforcement Learning|Reinforcement Learning]]
**⚡ Unique Technical**: [[keywords/Remote Sensing|Remote Sensing]], [[keywords/Quality Assessment|Quality Assessment]], [[keywords/Best-of-N Scaling|Best-of-N Scaling]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.00743v2 Announce Type: replace 
Abstract: Vision-Language Models (VLMs) have demonstrated great potential in interpreting remote sensing (RS) images through language-guided semantic. However, the effectiveness of these VLMs critically depends on high-quality image-text training data that captures rich semantic relationships between visual content and language descriptions. Unlike natural images, RS lacks large-scale interleaved image-text pairs from web data, making data collection challenging. While current approaches rely primarily on rule-based methods or flagship VLMs for data synthesis, a systematic framework for automated quality assessment of such synthetically generated RS vision-language data is notably absent. To fill this gap, we propose a novel score model trained on large-scale RS vision-language preference data for automated quality assessment. Our empirical results demonstrate that fine-tuning CLIP or advanced VLMs (e.g., Qwen2-VL) with the top 30% of data ranked by our score model achieves superior accuracy compared to both full-data fine-tuning and CLIP-score-based ranking approaches. Furthermore, we demonstrate applications of our scoring model for reinforcement learning (RL) training and best-of-N (BoN) test-time scaling, enabling significant improvements in VLM performance for RS tasks. Our code, model, and dataset are publicly available

## 🔍 Abstract (한글 번역)

arXiv:2503.00743v2 발표 유형: 교체  
초록: 비전-언어 모델(VLMs)은 언어로 유도된 의미론을 통해 원격 감지(RS) 이미지를 해석하는 데 있어 큰 잠재력을 보여주었습니다. 그러나 이러한 VLMs의 효과는 시각적 콘텐츠와 언어 설명 간의 풍부한 의미 관계를 포착하는 고품질 이미지-텍스트 학습 데이터에 크게 의존합니다. 자연 이미지와 달리, RS는 웹 데이터에서 대규모로 얽힌 이미지-텍스트 쌍이 부족하여 데이터 수집이 어렵습니다. 현재의 접근 방식은 주로 규칙 기반 방법이나 주력 VLMs에 의존하여 데이터를 합성하지만, 이러한 합성된 RS 비전-언어 데이터의 자동 품질 평가를 위한 체계적인 프레임워크는 눈에 띄게 부족합니다. 이러한 격차를 메우기 위해, 우리는 대규모 RS 비전-언어 선호 데이터에 대해 학습된 새로운 점수 모델을 제안하여 자동 품질 평가를 수행합니다. 우리의 실험 결과는 점수 모델에 의해 상위 30%로 순위가 매겨진 데이터로 CLIP 또는 고급 VLMs(예: Qwen2-VL)를 미세 조정하면 전체 데이터 미세 조정 및 CLIP 점수 기반 순위 접근 방식보다 우수한 정확도를 달성함을 보여줍니다. 또한, 우리는 강화 학습(RL) 훈련 및 베스트 오브 N(BoN) 테스트 시간 확장을 위한 점수 모델의 응용을 시연하여 RS 작업에 대한 VLM 성능의 상당한 개선을 가능하게 합니다. 우리의 코드, 모델 및 데이터셋은 공개적으로 이용 가능합니다.

## 📝 요약

이 논문은 원격 탐사(RS) 이미지의 언어 기반 의미 해석을 위한 비전-언어 모델(VLMs)의 효과적인 활용을 위해 고품질 이미지-텍스트 데이터의 필요성을 강조합니다. RS 분야에서는 대규모 이미지-텍스트 쌍이 부족하여 데이터 수집이 어렵습니다. 이를 해결하기 위해, 저자들은 대규모 RS 비전-언어 선호 데이터로 훈련된 새로운 스코어 모델을 제안하여 자동 품질 평가를 수행합니다. 실험 결과, 이 스코어 모델로 상위 30% 데이터를 선별하여 CLIP 또는 고급 VLMs를 미세 조정하면 전체 데이터를 사용하는 경우보다 더 높은 정확도를 달성했습니다. 또한, 이 스코어 모델은 강화 학습(RL) 훈련과 테스트 시 확장에 활용되어 RS 작업에서 VLM 성능을 크게 향상시켰습니다. 코드, 모델, 데이터셋은 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 원격 감지(RS) 이미지 해석을 위한 비전-언어 모델(VLM)의 효과는 고품질 이미지-텍스트 훈련 데이터에 크게 의존합니다.
- 2. RS는 웹 데이터에서 대규모 이미지-텍스트 쌍이 부족하여 데이터 수집이 어렵습니다.
- 3. 본 연구에서는 자동 품질 평가를 위한 새로운 점수 모델을 제안하여, 상위 30% 데이터로 미세 조정 시 높은 정확도를 달성했습니다.
- 4. 제안된 점수 모델은 강화 학습(RL) 훈련 및 테스트 시 성능 향상을 위한 다양한 응용이 가능합니다.
- 5. 연구의 코드, 모델, 데이터셋은 공개되어 있습니다.


---

*Generated on 2025-09-23 12:31:28*