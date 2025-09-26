---
keywords:
  - LLM Ensemble
  - Ensemble Before Inference
  - Ensemble During Inference
  - Ensemble After Inference
category: cs.CL
publish_date: 2025-09-22
arxiv_id: 2502.18036
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T11:41:38.245659",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "LLM Ensemble",
    "Ensemble Before Inference",
    "Ensemble During Inference",
    "Ensemble After Inference"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "LLM Ensemble": 0.8,
    "Ensemble Before Inference": 0.78,
    "Ensemble During Inference": 0.79,
    "Ensemble After Inference": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLM Ensemble",
        "canonical": "LLM Ensemble",
        "aliases": [
          "Large Language Model Ensemble",
          "LLM Aggregation"
        ],
        "category": "unique_technical",
        "rationale": "This concept is central to the paper and represents a novel approach in the use of multiple LLMs.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "ensemble-before-inference",
        "canonical": "Ensemble Before Inference",
        "aliases": [
          "pre-inference ensemble"
        ],
        "category": "specific_connectable",
        "rationale": "This method is part of the taxonomy introduced and can link to related ensemble strategies.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "ensemble-during-inference",
        "canonical": "Ensemble During Inference",
        "aliases": [
          "inference-time ensemble"
        ],
        "category": "specific_connectable",
        "rationale": "This is a distinct phase in the ensemble process, relevant for linking inference techniques.",
        "novelty_score": 0.68,
        "connectivity_score": 0.77,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "ensemble-after-inference",
        "canonical": "Ensemble After Inference",
        "aliases": [
          "post-inference ensemble"
        ],
        "category": "specific_connectable",
        "rationale": "This phase is crucial for understanding post-processing in ensemble methods.",
        "novelty_score": 0.67,
        "connectivity_score": 0.74,
        "specificity_score": 0.83,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "review",
      "paper",
      "study"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLM Ensemble",
      "resolved_canonical": "LLM Ensemble",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "ensemble-before-inference",
      "resolved_canonical": "Ensemble Before Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "ensemble-during-inference",
      "resolved_canonical": "Ensemble During Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.77,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "ensemble-after-inference",
      "resolved_canonical": "Ensemble After Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.67,
        "connectivity": 0.74,
        "specificity": 0.83,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Harnessing Multiple Large Language Models: A Survey on LLM Ensemble

**Korean Title:** 다중 대형 언어 모델 활용: LLM 앙상블에 관한 조사

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2502.18036.pdf)
**Category**: cs.CL
**Published**: 2025-09-22
**ArXiv ID**: [2502.18036](https://arxiv.org/abs/2502.18036)

## 🔗 유사한 논문
- [[2025-09-18/From Automation to Autonomy_ A Survey on Large Language Models in Scientific Discovery_20250918|From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery]] (85.5% similar)
- [[2025-09-19/Modular Machine Learning_ An Indispensable Path towards New-Generation Large Language Models_20250919|Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models]] (85.0% similar)
- [[2025-09-22/Predicting Language Models' Success at Zero-Shot Probabilistic Prediction_20250922|Predicting Language Models' Success at Zero-Shot Probabilistic Prediction]] (84.6% similar)
- [[2025-09-22/Are LLMs Better Formalizers than Solvers on Complex Problems?_20250922|Are LLMs Better Formalizers than Solvers on Complex Problems?]] (84.2% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Ensemble Before Inference|Ensemble Before Inference]], [[keywords/Ensemble During Inference|Ensemble During Inference]], [[keywords/Ensemble After Inference|Ensemble After Inference]]
**⚡ Unique Technical**: [[keywords/LLM Ensemble|LLM Ensemble]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.18036v5 Announce Type: replace 
Abstract: LLM Ensemble -- which involves the comprehensive use of multiple large language models (LLMs), each aimed at handling user queries during downstream inference, to benefit from their individual strengths -- has gained substantial attention recently. The widespread availability of LLMs, coupled with their varying strengths and out-of-the-box usability, has profoundly advanced the field of LLM Ensemble. This paper presents the first systematic review of recent developments in LLM Ensemble. First, we introduce our taxonomy of LLM Ensemble and discuss several related research problems. Then, we provide a more in-depth classification of the methods under the broad categories of "ensemble-before-inference, ensemble-during-inference, ensemble-after-inference'', and review all relevant methods. Finally, we introduce related benchmarks and applications, summarize existing studies, and suggest several future research directions. A curated list of papers on LLM Ensemble is available at https://github.com/junchenzhi/Awesome-LLM-Ensemble.

## 🔍 Abstract (한글 번역)

arXiv:2502.18036v5 발표 유형: 교체  
초록: LLM 앙상블은 사용자 쿼리를 처리하기 위해 각기 다른 강점을 가진 여러 대형 언어 모델(LLM)을 종합적으로 활용하여 다운스트림 추론 시 이들의 개별적인 강점을 활용하는 방법으로, 최근 상당한 주목을 받고 있습니다. LLM의 광범위한 가용성과 다양한 강점, 그리고 즉시 사용 가능한 특성은 LLM 앙상블 분야를 크게 발전시켰습니다. 본 논문은 LLM 앙상블의 최근 발전에 대한 최초의 체계적인 리뷰를 제공합니다. 먼저, LLM 앙상블의 분류 체계를 소개하고 관련 연구 문제들을 논의합니다. 그런 다음, "추론 전 앙상블, 추론 중 앙상블, 추론 후 앙상블"이라는 넓은 범주에 따라 방법들을 보다 심층적으로 분류하고, 관련된 모든 방법을 검토합니다. 마지막으로, 관련 벤치마크와 응용 프로그램을 소개하고, 기존 연구를 요약하며, 향후 연구 방향을 제안합니다. LLM 앙상블에 관한 논문 목록은 https://github.com/junchenzhi/Awesome-LLM-Ensemble에서 확인할 수 있습니다.

## 📝 요약

이 논문은 최근 주목받고 있는 대형 언어 모델(LLM) 앙상블에 대한 체계적인 리뷰를 제공합니다. LLM 앙상블은 여러 LLM을 활용하여 각 모델의 강점을 살려 사용자 쿼리를 처리하는 방법론입니다. 저자들은 LLM 앙상블의 분류 체계를 제시하고, "추론 전 앙상블", "추론 중 앙상블", "추론 후 앙상블"로 방법론을 분류하여 관련 연구를 검토합니다. 또한, 관련 벤치마크와 응용 사례를 소개하고, 향후 연구 방향을 제안합니다.

## 🎯 주요 포인트

- 1. LLM 앙상블은 여러 대형 언어 모델을 종합적으로 활용하여 각 모델의 강점을 살려 사용자 쿼리를 처리하는 방법으로 주목받고 있다.
- 2. 본 논문은 LLM 앙상블의 최근 발전을 체계적으로 검토한 최초의 연구로, LLM 앙상블의 분류 체계를 소개하고 관련 연구 문제를 논의한다.
- 3. "추론 전 앙상블, 추론 중 앙상블, 추론 후 앙상블"이라는 범주로 방법을 분류하고 관련 방법들을 검토한다.
- 4. 관련 벤치마크와 응용 사례를 소개하고 기존 연구를 요약하며, 향후 연구 방향을 제안한다.
- 5. LLM 앙상블에 관한 논문 목록은 https://github.com/junchenzhi/Awesome-LLM-Ensemble에서 확인할 수 있다.


---

*Generated on 2025-09-23 11:41:38*