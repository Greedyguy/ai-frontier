<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:51:37.339352",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multi-label Classification",
    "Distribution Alignment",
    "Zero-Shot Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multi-label Classification": 0.78,
    "Distribution Alignment": 0.77,
    "Zero-Shot Learning": 0.82
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
        "rationale": "Large Language Models are central to the study and connect with a wide range of topics in NLP and AI.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multi-label Classification",
        "canonical": "Multi-label Classification",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The paper focuses on how LLMs handle multi-label classification, a distinct task in machine learning.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Distribution Alignment",
        "canonical": "Distribution Alignment",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Distribution alignment is introduced as a novel task for improving LLM performance in subjective tasks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.77
      },
      {
        "surface": "Zero-shot Methods",
        "canonical": "Zero-Shot Learning",
        "aliases": [
          "Zero-shot"
        ],
        "category": "specific_connectable",
        "rationale": "Zero-shot methods are highlighted as a way to improve alignment and predictive performance.",
        "novelty_score": 0.55,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "task"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multi-label Classification",
      "resolved_canonical": "Multi-label Classification",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Distribution Alignment",
      "resolved_canonical": "Distribution Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Zero-shot Methods",
      "resolved_canonical": "Zero-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Large Language Models Do Multi-Label Classification Differently

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2505.17510.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2505.17510](https://arxiv.org/abs/2505.17510)

## 🔗 유사한 논문
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (88.9% similar)
- [[2025-09-23/Probabilistic Token Alignment for Large Language Model Fusion_20250923|Probabilistic Token Alignment for Large Language Model Fusion]] (87.4% similar)
- [[2025-09-19/Decoupled Proxy Alignment_ Mitigating Language Prior Conflict for Multimodal Alignment in MLLM_20250919|Decoupled Proxy Alignment: Mitigating Language Prior Conflict for Multimodal Alignment in MLLM]] (86.9% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (86.5% similar)
- [[2025-09-23/Measuring Scalar Constructs in Social Science with LLMs_20250923|Measuring Scalar Constructs in Social Science with LLMs]] (86.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Zero-Shot Learning|Zero-Shot Learning]]
**⚡ Unique Technical**: [[keywords/Multi-label Classification|Multi-label Classification]], [[keywords/Distribution Alignment|Distribution Alignment]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2505.17510v2 Announce Type: replace 
Abstract: Multi-label classification is prevalent in real-world settings, but the behavior of Large Language Models (LLMs) in this setting is understudied. We investigate how autoregressive LLMs perform multi-label classification, focusing on subjective tasks, by analyzing the output distributions of the models at each label generation step. We find that the initial probability distribution for the first label often does not reflect the eventual final output, even in terms of relative order and find LLMs tend to suppress all but one label at each generation step. We further observe that as model scale increases, their token distributions exhibit lower entropy and higher single-label confidence, but the internal relative ranking of the labels improves. Finetuning methods such as supervised finetuning and reinforcement learning amplify this phenomenon. We introduce the task of distribution alignment for multi-label settings: aligning LLM-derived label distributions with empirical distributions estimated from annotator responses in subjective tasks. We propose both zero-shot and supervised methods which improve both alignment and predictive performance over existing approaches. We find one method -- taking the max probability over all label generation distributions instead of just using the initial probability distribution -- improves both distribution alignment and overall F1 classification without adding any additional computation.

## 📝 요약

이 논문은 대규모 언어 모델(LLM)이 다중 라벨 분류에서 어떻게 작동하는지를 연구합니다. 특히 주관적인 작업에 초점을 맞춰, 각 라벨 생성 단계에서 모델의 출력 분포를 분석합니다. 연구 결과, 첫 번째 라벨의 초기 확률 분포가 최종 출력과 일치하지 않으며, LLM이 각 단계에서 하나의 라벨만을 강조하는 경향이 있음을 발견했습니다. 모델의 규모가 커질수록 토큰 분포의 엔트로피가 낮아지고 단일 라벨에 대한 확신이 높아지지만, 라벨 간의 상대적 순위는 개선됩니다. 또한, 지도 학습 및 강화 학습을 통한 미세 조정이 이러한 현상을 강화합니다. 저자들은 주관적인 작업에서 LLM이 생성한 라벨 분포를 주석자 응답의 경험적 분포와 정렬하는 '분포 정렬' 과제를 제안하고, 이를 개선하기 위한 제로샷 및 지도 학습 방법을 제시합니다. 특히, 모든 라벨 생성 분포에서 최대 확률을 사용하는 방법이 분포 정렬과 F1 분류 성능을 향상시킴을 발견했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 멀티라벨 분류에서 초기 레이블 확률 분포가 최종 출력과 일치하지 않는 경향이 있습니다.
- 2. 모델의 규모가 커질수록 토큰 분포의 엔트로피가 낮아지고 단일 레이블에 대한 신뢰도가 높아지지만, 레이블의 상대적 순위는 개선됩니다.
- 3. 감독 학습 및 강화 학습과 같은 파인튜닝 방법은 단일 레이블 신뢰도를 더욱 증폭시킵니다.
- 4. 주관적 작업에서 LLM 파생 레이블 분포를 주석자 응답에서 추정된 경험적 분포와 정렬하는 '분포 정렬' 작업을 도입했습니다.
- 5. 초기 확률 분포 대신 모든 레이블 생성 분포에서 최대 확률을 사용하는 방법이 분포 정렬과 F1 분류 성능을 개선합니다.


---

*Generated on 2025-09-24 15:51:37*