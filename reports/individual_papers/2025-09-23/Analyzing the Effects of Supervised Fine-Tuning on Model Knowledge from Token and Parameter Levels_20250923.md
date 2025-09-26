---
keywords:
  - Large Language Model
  - Supervised Fine-Tuning
  - Closed-Book Question Answering
  - Parameter Updates
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2509.16596
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T23:27:28.135538",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Supervised Fine-Tuning",
    "Closed-Book Question Answering",
    "Parameter Updates"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Supervised Fine-Tuning": 0.82,
    "Closed-Book Question Answering": 0.79,
    "Parameter Updates": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large language models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "large-scale language models"
        ],
        "category": "broad_technical",
        "rationale": "This term is essential for linking discussions about advanced NLP systems and their capabilities.",
        "novelty_score": 0.45,
        "connectivity_score": 0.92,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "supervised fine-tuning",
        "canonical": "Supervised Fine-Tuning",
        "aliases": [
          "SFT",
          "fine-tuning"
        ],
        "category": "specific_connectable",
        "rationale": "Critical for understanding the post-training modifications applied to models, impacting their performance.",
        "novelty_score": 0.58,
        "connectivity_score": 0.88,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "closed-book question answering",
        "canonical": "Closed-Book Question Answering",
        "aliases": [
          "CBQA"
        ],
        "category": "unique_technical",
        "rationale": "Represents a specific task used to evaluate model knowledge without external information.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.81,
        "link_intent_score": 0.79
      },
      {
        "surface": "parameter updates",
        "canonical": "Parameter Updates",
        "aliases": [
          "model updates",
          "weight adjustments"
        ],
        "category": "unique_technical",
        "rationale": "Understanding parameter updates is crucial for analyzing how fine-tuning impacts model knowledge.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "performance",
      "model behavior",
      "knowledge enhancement"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large language models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.92,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "supervised fine-tuning",
      "resolved_canonical": "Supervised Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.88,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "closed-book question answering",
      "resolved_canonical": "Closed-Book Question Answering",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.81,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "parameter updates",
      "resolved_canonical": "Parameter Updates",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Analyzing the Effects of Supervised Fine-Tuning on Model Knowledge from Token and Parameter Levels

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16596.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2509.16596](https://arxiv.org/abs/2509.16596)

## 🔗 유사한 논문
- [[2025-09-22/Not All Parameters Are Created Equal_ Smart Isolation Boosts Fine-Tuning Performance_20250922|Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance]] (87.0% similar)
- [[2025-09-22/Mind the Gap_ Data Rewriting for Stable Off-Policy Supervised Fine-Tuning_20250922|Mind the Gap: Data Rewriting for Stable Off-Policy Supervised Fine-Tuning]] (84.9% similar)
- [[2025-09-22/A method for improving multilingual quality and diversity of instruction fine-tuning datasets_20250922|A method for improving multilingual quality and diversity of instruction fine-tuning datasets]] (84.1% similar)
- [[2025-09-22/Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data_20250922|Exploring Fine-Tuning of Large Audio Language Models for Spoken Language Understanding under Limited Speech data]] (83.9% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (83.7% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Supervised Fine-Tuning|Supervised Fine-Tuning]]
**⚡ Unique Technical**: [[keywords/Closed-Book Question Answering|Closed-Book Question Answering]], [[keywords/Parameter Updates|Parameter Updates]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16596v1 Announce Type: cross 
Abstract: Large language models (LLMs) acquire substantial world knowledge during pre-training, which is further shaped by post-training techniques such as supervised fine-tuning (SFT). However, the impact of SFT on a model's knowledge remains underexplored, limiting our ability to control knowledge change behavior in fine-tuned models. To address this gap, we evaluate closed-book question answering (CBQA) performance across five LLMs from the LLaMA-2 and LLaMA-3 families. Surprisingly, models fine-tuned on 1,920 samples perform up to 14% worse than those fine-tuned on only 240 samples. Furthermore, varying the level of knowledge mastery in the fine-tuning data leads to performance fluctuations of over 12%. To investigate these effects, we analyze model behavior at both the token and parameter levels. Our analysis reveals that up to 90% of parameter updates during SFT do not contribute to knowledge enhancement. Restoring these updates can improve performance on the CBQA task, depending on the characteristics of the fine-tuning data. These insights offer practical guidance for developing fine-tuning strategies that more effectively strengthen model knowledge.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 사전 훈련 후 감독된 미세 조정(SFT)이 모델의 지식에 미치는 영향을 분석합니다. LLaMA-2 및 LLaMA-3 계열의 모델을 대상으로 폐쇄형 질문 응답(CBQA) 성능을 평가한 결과, 1,920개의 샘플로 미세 조정된 모델이 240개의 샘플로 조정된 모델보다 최대 14% 성능이 저하되었습니다. 또한, 미세 조정 데이터의 지식 수준에 따라 성능이 12% 이상 변동하는 것으로 나타났습니다. 분석 결과, SFT 중 최대 90%의 매개변수 업데이트가 지식 향상에 기여하지 않으며, 이를 복원하면 CBQA 성능이 개선될 수 있습니다. 이러한 발견은 모델 지식을 효과적으로 강화하는 미세 조정 전략 개발에 실질적인 지침을 제공합니다.

## 🎯 주요 포인트

- 1. 대규모 언어 모델(LLM)은 사전 훈련 동안 상당한 세계 지식을 습득하며, 이는 감독된 미세 조정(SFT)과 같은 후속 훈련 기법에 의해 추가로 형성된다.
- 2. 1,920개의 샘플로 미세 조정된 모델이 240개의 샘플로 미세 조정된 모델보다 최대 14% 성능이 저하되는 현상이 관찰되었다.
- 3. 미세 조정 데이터의 지식 숙달 수준에 따라 성능 변동이 12% 이상 발생한다.
- 4. SFT 동안의 매개변수 업데이트 중 최대 90%가 지식 향상에 기여하지 않으며, 이러한 업데이트를 복원하면 CBQA 작업 성능이 개선될 수 있다.
- 5. 연구 결과는 모델 지식을 더 효과적으로 강화하는 미세 조정 전략 개발에 실질적인 지침을 제공한다.


---

*Generated on 2025-09-23 23:27:28*