---
keywords:
  - Multimodal Learning
  - Functionally Equivalent Sampling
  - Uncertainty Quantification
  - Vision-Language Model
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16648
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T22:51:00.284967",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Functionally Equivalent Sampling",
    "Uncertainty Quantification",
    "Vision-Language Model"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.85,
    "Functionally Equivalent Sampling": 0.78,
    "Uncertainty Quantification": 0.8,
    "Vision-Language Model": 0.82
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
        "rationale": "Links to the trending concept of integrating multiple modalities in learning systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.85
      },
      {
        "surface": "Functionally Equivalent Sampling",
        "canonical": "Functionally Equivalent Sampling",
        "aliases": [
          "FESTA"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel technique for trust assessment in multimodal models.",
        "novelty_score": 0.92,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Uncertainty Quantification",
        "canonical": "Uncertainty Quantification",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Essential for assessing model predictions and linking to other trust assessment methods.",
        "novelty_score": 0.58,
        "connectivity_score": 0.83,
        "specificity_score": 0.72,
        "link_intent_score": 0.8
      },
      {
        "surface": "Vision-LLMs",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language Models"
        ],
        "category": "evolved_concepts",
        "rationale": "Represents an evolved concept in integrating vision and language processing.",
        "novelty_score": 0.6,
        "connectivity_score": 0.87,
        "specificity_score": 0.79,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "Trust Assessment",
      "Selective Prediction"
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
        "specificity": 0.78,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Functionally Equivalent Sampling",
      "resolved_canonical": "Functionally Equivalent Sampling",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Uncertainty Quantification",
      "resolved_canonical": "Uncertainty Quantification",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.83,
        "specificity": 0.72,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Vision-LLMs",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.87,
        "specificity": 0.79,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# FESTA: Functionally Equivalent Sampling for Trust Assessment of Multimodal LLMs

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16648.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16648](https://arxiv.org/abs/2509.16648)

## 🔗 유사한 논문
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (82.9% similar)
- [[2025-09-19/A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation_20250919|A Multi-To-One Interview Paradigm for Efficient MLLM Evaluation]] (82.5% similar)
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (82.3% similar)
- [[2025-09-19/Estimating Semantic Alphabet Size for LLM Uncertainty Quantification_20250919|Estimating Semantic Alphabet Size for LLM Uncertainty Quantification]] (81.3% similar)
- [[2025-09-22/Evaluating Multimodal Large Language Models on Spoken Sarcasm Understanding_20250922|Evaluating Multimodal Large Language Models on Spoken Sarcasm Understanding]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]], [[keywords/Uncertainty Quantification|Uncertainty Quantification]]
**⚡ Unique Technical**: [[keywords/Functionally Equivalent Sampling|Functionally Equivalent Sampling]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16648v1 Announce Type: new 
Abstract: The accurate trust assessment of multimodal large language models (MLLMs) generated predictions, which can enable selective prediction and improve user confidence, is challenging due to the diverse multi-modal input paradigms. We propose Functionally Equivalent Sampling for Trust Assessment (FESTA), a multimodal input sampling technique for MLLMs, that generates an uncertainty measure based on the equivalent and complementary input samplings. The proposed task-preserving sampling approach for uncertainty quantification expands the input space to probe the consistency (through equivalent samples) and sensitivity (through complementary samples) of the model. FESTA uses only input-output access of the model (black-box), and does not require ground truth (unsupervised). The experiments are conducted with various off-the-shelf multi-modal LLMs, on both visual and audio reasoning tasks. The proposed FESTA uncertainty estimate achieves significant improvement (33.3% relative improvement for vision-LLMs and 29.6% relative improvement for audio-LLMs) in selective prediction performance, based on area-under-receiver-operating-characteristic curve (AUROC) metric in detecting mispredictions. The code implementation is open-sourced.

## 📝 요약

이 논문은 다중 모달 대형 언어 모델(MLLMs)의 예측에 대한 신뢰 평가를 개선하기 위해 FESTA라는 새로운 방법을 제안합니다. FESTA는 모델의 입력 공간을 확장하여 일관성과 민감도를 평가하는 입력 샘플링 기법으로, 모델의 입력-출력만을 사용하여 불확실성을 측정합니다. 실험 결과, FESTA는 시각 및 오디오 추론 작업에서 AUROC 기준으로 각각 33.3%와 29.6%의 상대적 성능 향상을 보였습니다. 이 방법은 감독 없이도 신뢰도를 높일 수 있으며, 코드가 공개되어 있습니다.

## 🎯 주요 포인트

- 1. FESTA는 멀티모달 대형 언어 모델의 신뢰 평가를 위한 입력 샘플링 기법으로, 등가 및 보완적 입력 샘플링을 통해 불확실성을 측정합니다.
- 2. 제안된 샘플링 기법은 모델의 일관성과 민감성을 탐색하기 위해 입력 공간을 확장하며, 모델의 입력-출력 접근만을 사용하고 지도 학습이 필요 없습니다.
- 3. FESTA는 시각 및 오디오 추론 작업에서 다양한 멀티모달 LLM을 대상으로 실험을 진행하였으며, 선택적 예측 성능에서 AUROC 기준으로 시각-LLM에서 33.3%, 오디오-LLM에서 29.6%의 상대적 개선을 달성했습니다.
- 4. 코드 구현은 오픈 소스로 제공됩니다.


---

*Generated on 2025-09-23 22:51:00*