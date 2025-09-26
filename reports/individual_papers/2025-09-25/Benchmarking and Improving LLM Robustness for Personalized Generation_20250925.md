---
keywords:
  - Large Language Model
  - PERG Framework
  - Personalized Generation
  - Preference Aligner
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19358
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:29:13.264353",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "PERG Framework",
    "Personalized Generation",
    "Preference Aligner"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "PERG Framework": 0.8,
    "Personalized Generation": 0.78,
    "Preference Aligner": 0.82
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
        "rationale": "This is a fundamental concept in the paper, linking to a broad technical category relevant to many discussions.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "PERG",
        "canonical": "PERG Framework",
        "aliases": [
          "PERGData"
        ],
        "category": "unique_technical",
        "rationale": "A unique framework introduced in the paper, essential for understanding the proposed evaluation method.",
        "novelty_score": 0.85,
        "connectivity_score": 0.55,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Personalization",
        "canonical": "Personalized Generation",
        "aliases": [
          "personalized responses"
        ],
        "category": "specific_connectable",
        "rationale": "Central theme of the paper, connecting to the concept of tailoring LLM outputs to user preferences.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Pref-Aligner",
        "canonical": "Preference Aligner",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A novel approach proposed to enhance robustness, crucial for understanding improvements in personalization.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "factuality",
      "evaluation",
      "responses"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "PERG",
      "resolved_canonical": "PERG Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.55,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Personalization",
      "resolved_canonical": "Personalized Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Pref-Aligner",
      "resolved_canonical": "Preference Aligner",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# Benchmarking and Improving LLM Robustness for Personalized Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19358.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19358](https://arxiv.org/abs/2509.19358)

## 🔗 유사한 논문
- [[2025-09-23/A Survey of Personalized Large Language Models_ Progress and Future Directions_20250923|A Survey of Personalized Large Language Models: Progress and Future Directions]] (88.2% similar)
- [[2025-09-23/Latent Inter-User Difference Modeling for LLM Personalization_20250923|Latent Inter-User Difference Modeling for LLM Personalization]] (86.8% similar)
- [[2025-09-23/Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements_20250923|Large Language Models Badly Generalize across Option Length, Problem Types, and Irrelevant Noun Replacements]] (86.8% similar)
- [[2025-09-25/Unveiling the Merits and Defects of LLMs in Automatic Review Generation for Scientific Papers_20250925|Unveiling the Merits and Defects of LLMs in Automatic Review Generation for Scientific Papers]] (86.4% similar)
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (86.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Personalized Generation|Personalized Generation]]
**⚡ Unique Technical**: [[keywords/PERG Framework|PERG Framework]], [[keywords/Preference Aligner|Preference Aligner]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19358v1 Announce Type: cross 
Abstract: Recent years have witnessed a growing interest in personalizing the responses of large language models (LLMs). While existing evaluations primarily focus on whether a response aligns with a user's preferences, we argue that factuality is an equally important yet often overlooked dimension. In the context of personalization, we define a model as robust if its responses are both factually accurate and align with the user preferences. To assess this, we introduce PERG, a scalable framework for evaluating robustness in LLMs, along with a new dataset, PERGData. We evaluate fourteen models from five different model families using different prompting methods. Our findings show that current LLMs struggle with robust personalization: even the strongest models (GPT-4.1, LLaMA3-70B) fail to maintain correctness in 5% of previously successful cases without personalization, while smaller models (e.g., 7B-scale) can fail more than 20% of the time. Further analysis reveals that robustness is significantly affected by the nature of the query and the type of user preference. To mitigate these failures, we propose Pref-Aligner, a two-stage approach that improves robustness by an average of 25% across models. Our work highlights critical gaps in current evaluation practices and introduces tools and metrics to support more reliable, user-aligned LLM deployments.

## 📝 요약

최근 대형 언어 모델(LLM)의 개인화된 응답에 대한 관심이 증가하고 있습니다. 기존 평가가 주로 사용자 선호도와의 일치 여부에 초점을 맞추는 반면, 본 연구는 사실성 또한 중요한 요소라고 주장합니다. 개인화 맥락에서, 모델의 응답이 사실적으로 정확하고 사용자 선호도와 일치할 때 이를 강건하다고 정의합니다. 이를 평가하기 위해 PERG라는 확장 가능한 평가 프레임워크와 새로운 데이터셋 PERGData를 소개합니다. 다섯 가지 모델 군에서 14개의 모델을 다양한 프롬프트 방법으로 평가한 결과, 현재 LLM들은 강건한 개인화에 어려움을 겪고 있음을 발견했습니다. 강력한 모델조차도 개인화 없이 성공했던 사례의 5%에서 정확성을 유지하지 못했으며, 작은 모델은 20% 이상 실패할 수 있습니다. 이러한 실패를 줄이기 위해 Pref-Aligner라는 두 단계 접근법을 제안하여 강건성을 평균 25% 향상시켰습니다. 본 연구는 현재 평가 관행의 중요한 격차를 강조하며, 더 신뢰할 수 있는 사용자 맞춤형 LLM 배포를 지원하는 도구와 지표를 소개합니다.

## 🎯 주요 포인트

- 1. 개인화된 대형 언어 모델(LLM)의 응답에서 사실성(factuality)이 중요하지만 종종 간과되고 있다.
- 2. PERG라는 프레임워크와 PERGData라는 새로운 데이터셋을 통해 LLM의 견고성을 평가하는 방법을 제안한다.
- 3. 현재의 LLM들은 개인화된 상황에서 견고한 응답을 유지하는 데 어려움을 겪고 있으며, 특히 작은 모델은 20% 이상의 실패율을 보인다.
- 4. Pref-Aligner라는 두 단계 접근법을 통해 모델의 견고성을 평균 25% 개선할 수 있다.
- 5. 본 연구는 현재 평가 관행의 중요한 격차를 강조하고, 사용자 맞춤형 LLM 배포를 지원하는 도구와 지표를 도입한다.


---

*Generated on 2025-09-25 15:29:13*