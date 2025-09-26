---
keywords:
  - Vision-Language Model
  - Zero-Shot Learning
  - TrustVLM
  - Multimodal Learning
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2505.23745
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:26:05.783183",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Vision-Language Model",
    "Zero-Shot Learning",
    "TrustVLM",
    "Multimodal Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Vision-Language Model": 0.9,
    "Zero-Shot Learning": 0.85,
    "TrustVLM": 0.8,
    "Multimodal Learning": 0.78
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
        "rationale": "Vision-Language Models represent a key concept in the paper and are central to understanding the multimodal capabilities discussed.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.82,
        "link_intent_score": 0.9
      },
      {
        "surface": "Zero-Shot Learning",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "ZSL"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-Shot Learning is a critical capability of Vision-Language Models that enhances their applicability across various tasks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "TrustVLM",
        "canonical": "TrustVLM",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "TrustVLM is a novel framework introduced in the paper, specifically designed to improve the trustworthiness of VLM predictions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multimodal Understanding",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Understanding is a core aspect of Vision-Language Models, crucial for their ability to process and integrate visual and textual data.",
        "novelty_score": 0.55,
        "connectivity_score": 0.82,
        "specificity_score": 0.76,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "misclassification",
      "safety-critical domains"
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
        "specificity": 0.82,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Zero-Shot Learning",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "TrustVLM",
      "resolved_canonical": "TrustVLM",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multimodal Understanding",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.82,
        "specificity": 0.76,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# To Trust Or Not To Trust Your Vision-Language Model's Prediction

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2505.23745.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2505.23745](https://arxiv.org/abs/2505.23745)

## 🔗 유사한 논문
- [[2025-09-24/Bi-VLM_ Pushing Ultra-Low Precision Post-Training Quantization Boundaries in Vision-Language Models_20250924|Bi-VLM: Pushing Ultra-Low Precision Post-Training Quantization Boundaries in Vision-Language Models]] (85.6% similar)
- [[2025-09-22/Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models_20250922|Quality-Driven Curation of Remote Sensing Vision-Language Data via Learned Scoring Models]] (85.5% similar)
- [[2025-09-22/ViLU_ Learning Vision-Language Uncertainties for Failure Prediction_20250922|ViLU: Learning Vision-Language Uncertainties for Failure Prediction]] (85.5% similar)
- [[2025-09-24/No Labels Needed_ Zero-Shot Image Classification with Collaborative Self-Learning_20250924|No Labels Needed: Zero-Shot Image Classification with Collaborative Self-Learning]] (84.8% similar)
- [[2025-09-22/Are Vision-Language Models Safe in the Wild? A Meme-Based Benchmark Study_20250922|Are Vision-Language Models Safe in the Wild? A Meme-Based Benchmark Study]] (84.5% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]], [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/TrustVLM|TrustVLM]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.23745v2 Announce Type: replace-cross 
Abstract: Vision-Language Models (VLMs) have demonstrated strong capabilities in aligning visual and textual modalities, enabling a wide range of applications in multimodal understanding and generation. While they excel in zero-shot and transfer learning scenarios, VLMs remain susceptible to misclassification, often yielding confident yet incorrect predictions. This limitation poses a significant risk in safety-critical domains, where erroneous predictions can lead to severe consequences. In this work, we introduce TrustVLM, a training-free framework designed to address the critical challenge of estimating when VLM's predictions can be trusted. Motivated by the observed modality gap in VLMs and the insight that certain concepts are more distinctly represented in the image embedding space, we propose a novel confidence-scoring function that leverages this space to improve misclassification detection. We rigorously evaluate our approach across 17 diverse datasets, employing 4 architectures and 2 VLMs, and demonstrate state-of-the-art performance, with improvements of up to 51.87% in AURC, 9.14% in AUROC, and 32.42% in FPR95 compared to existing baselines. By improving the reliability of the model without requiring retraining, TrustVLM paves the way for safer deployment of VLMs in real-world applications. The code is available at https://github.com/EPFL-IMOS/TrustVLM.

## 📝 요약

Vision-Language Models(VLMs)는 시각 및 텍스트 모달리티를 효과적으로 결합하여 다양한 멀티모달 이해 및 생성 작업을 수행할 수 있습니다. 그러나 이 모델들은 오분류 문제로 인해 안전이 중요한 분야에서 위험을 초래할 수 있습니다. 본 연구에서는 VLM의 예측 신뢰성을 평가하는 훈련이 필요 없는 프레임워크인 TrustVLM을 제안합니다. 이미지 임베딩 공간에서의 특정 개념의 명확한 표현을 활용한 새로운 신뢰도 점수 함수를 통해 오분류를 감지합니다. 17개의 다양한 데이터셋과 4개의 아키텍처, 2개의 VLM을 사용한 평가에서 기존 기준보다 최대 51.87%의 AURC, 9.14%의 AUROC, 32.42%의 FPR95 향상을 달성했습니다. TrustVLM은 재훈련 없이 모델의 신뢰성을 높여 실제 응용에서의 안전한 VLM 사용을 가능하게 합니다.

## 🎯 주요 포인트

- 1. Vision-Language Models(VLMs)는 시각 및 텍스트 모달리티를 정렬하는 데 뛰어난 능력을 보이며, 다양한 멀티모달 이해 및 생성 응용에 활용된다.
- 2. VLMs는 제로샷 및 전이 학습 시나리오에서 우수한 성능을 보이지만, 잘못된 예측을 자신 있게 내놓는 경우가 있어 안전이 중요한 분야에서는 큰 위험을 초래할 수 있다.
- 3. TrustVLM은 VLM의 예측 신뢰성을 평가하는 문제를 해결하기 위해 제안된 훈련이 필요 없는 프레임워크로, 이미지 임베딩 공간을 활용한 새로운 신뢰 점수 기능을 제안한다.
- 4. TrustVLM은 17개의 다양한 데이터셋과 4개의 아키텍처, 2개의 VLM을 통해 평가되었으며, 기존 기준 대비 AURC 51.87%, AUROC 9.14%, FPR95 32.42%의 성능 향상을 보였다.
- 5. TrustVLM은 재훈련 없이 모델의 신뢰성을 향상시켜 VLM의 실제 응용에서의 안전한 배포를 가능하게 한다.


---

*Generated on 2025-09-25 16:26:05*