---
keywords:
  - Mutual Information
  - Bayesian Update
  - Multimodal Learning
  - Information-Theoretic Operationalization
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.17047
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:21:18.224843",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Mutual Information",
    "Bayesian Update",
    "Multimodal Learning",
    "Information-Theoretic Operationalization"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Mutual Information": 0.82,
    "Bayesian Update": 0.8,
    "Multimodal Learning": 0.78,
    "Information-Theoretic Operationalization": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "mutual information",
        "canonical": "Mutual Information",
        "aliases": [
          "MI"
        ],
        "category": "unique_technical",
        "rationale": "Mutual Information is central to the paper's model of information quality in language processing.",
        "novelty_score": 0.65,
        "connectivity_score": 0.72,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Bayesian update",
        "canonical": "Bayesian Update",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Bayesian Update is a key method used in the mathematical model of reading described in the paper.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      },
      {
        "surface": "multimodal language models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "multimodal models"
        ],
        "category": "specific_connectable",
        "rationale": "The use of multimodal language models is crucial for estimating mutual information in the study.",
        "novelty_score": 0.55,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "information-theoretic operationalization",
        "canonical": "Information-Theoretic Operationalization",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This concept is a novel approach to defining information quality in the context of the study.",
        "novelty_score": 0.68,
        "connectivity_score": 0.65,
        "specificity_score": 0.77,
        "link_intent_score": 0.79
      }
    ],
    "ban_list_suggestions": [
      "reading times",
      "visual forms"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "mutual information",
      "resolved_canonical": "Mutual Information",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.72,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Bayesian update",
      "resolved_canonical": "Bayesian Update",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "multimodal language models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "information-theoretic operationalization",
      "resolved_canonical": "Information-Theoretic Operationalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.65,
        "specificity": 0.77,
        "link_intent": 0.79
      }
    }
  ]
}
-->

# Modeling Bottom-up Information Quality during Language Processing

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17047.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.17047](https://arxiv.org/abs/2509.17047)

## 🔗 유사한 논문
- [[2025-09-22/The Curious Case of Visual Grounding_ Different Effects for Speech- and Text-based Language Encoders_20250922|The Curious Case of Visual Grounding: Different Effects for Speech- and Text-based Language Encoders]] (82.4% similar)
- [[2025-09-22/Modeling the Human Visual System_ Comparative Insights from Response-Optimized and Task-Optimized Vision Models, Language Models, and different Readout Mechanisms_20250922|Modeling the Human Visual System: Comparative Insights from Response-Optimized and Task-Optimized Vision Models, Language Models, and different Readout Mechanisms]] (80.5% similar)
- [[2025-09-19/Large Language Model probabilities cannot distinguish between possible and impossible language_20250919|Large Language Model probabilities cannot distinguish between possible and impossible language]] (80.1% similar)
- [[2025-09-22/Once Upon a Time_ Interactive Learning for Storytelling with Small Language Models_20250922|Once Upon a Time: Interactive Learning for Storytelling with Small Language Models]] (80.1% similar)
- [[2025-09-22/Quantifying Self-Awareness of Knowledge in Large Language Models_20250922|Quantifying Self-Awareness of Knowledge in Large Language Models]] (80.0% similar)

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Mutual Information|Mutual Information]], [[keywords/Bayesian Update|Bayesian Update]], [[keywords/Information-Theoretic Operationalization|Information-Theoretic Operationalization]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17047v1 Announce Type: new 
Abstract: Contemporary theories model language processing as integrating both top-down expectations and bottom-up inputs. One major prediction of such models is that the quality of the bottom-up inputs modulates ease of processing -- noisy inputs should lead to difficult and effortful comprehension. We test this prediction in the domain of reading. First, we propose an information-theoretic operationalization for the "quality" of bottom-up information as the mutual information (MI) between visual information and word identity. We formalize this prediction in a mathematical model of reading as a Bayesian update. Second, we test our operationalization by comparing participants' reading times in conditions where words' information quality has been reduced, either by occluding their top or bottom half, with full words. We collect data in English and Chinese. We then use multimodal language models to estimate the mutual information between visual inputs and words. We use these data to estimate the specific effect of reduced information quality on reading times. Finally, we compare how information is distributed across visual forms. In English and Chinese, the upper half contains more information about word identity than the lower half. However, the asymmetry is more pronounced in English, a pattern which is reflected in the reading times.

## 📝 요약

이 논문은 언어 처리 모델에서 상향식 입력과 하향식 기대의 통합을 다루며, 입력의 질이 처리 용이성에 영향을 미친다는 예측을 검증합니다. 연구에서는 시각 정보와 단어 정체성 간의 상호 정보를 통해 입력의 질을 정의하고, 이를 읽기 과정의 수학적 모델로 공식화합니다. 실험에서는 단어의 상반부 또는 하반부를 가린 상태와 전체 단어 상태에서 참가자의 읽기 시간을 비교하여 입력 질의 영향을 분석합니다. 영어와 중국어 데이터를 수집하고, 다중 모달 언어 모델을 사용해 시각 입력과 단어 간 상호 정보를 추정합니다. 결과적으로, 영어와 중국어 모두에서 단어 정체성에 대한 정보가 상반부에 더 많이 포함되어 있으며, 이 비대칭성은 영어에서 더 두드러지게 나타나 읽기 시간에 반영됩니다.

## 🎯 주요 포인트

- 1. 언어 처리 모델은 상향식 입력과 하향식 기대를 통합하여 처리의 용이성을 설명하며, 입력의 질이 낮을수록 이해가 어려워진다고 예측합니다.
- 2. 입력 정보의 "질"을 시각 정보와 단어 정체성 간의 상호 정보(MI)로 정의하고, 이를 바탕으로 읽기 과정을 베이지안 업데이트 수학 모델로 공식화했습니다.
- 3. 단어의 정보 질이 감소된 조건(단어의 상반부 또는 하반부 가려짐)에서 참가자들의 읽기 시간을 비교하여 이론을 검증했습니다.
- 4. 영어와 중국어에서 시각 입력과 단어 간 상호 정보를 추정하기 위해 다중 모달 언어 모델을 사용했습니다.
- 5. 영어와 중국어 모두 단어 정체성에 대한 정보가 상반부에 더 많이 포함되어 있으며, 이 비대칭성은 영어에서 더 두드러지게 나타났습니다.


---

*Generated on 2025-09-24 03:21:18*