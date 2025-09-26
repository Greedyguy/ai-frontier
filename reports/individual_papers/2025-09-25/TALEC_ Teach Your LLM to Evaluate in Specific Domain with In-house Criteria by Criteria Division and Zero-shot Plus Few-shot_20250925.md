---
keywords:
  - Large Language Model
  - Few-Shot Learning
  - In-context Learning
  - Evaluation Criteria
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2407.10999
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:15:28.272940",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Few-Shot Learning",
    "In-context Learning",
    "Evaluation Criteria"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Few-Shot Learning": 0.8,
    "In-context Learning": 0.82,
    "Evaluation Criteria": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Model"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on evaluation methods for language models.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Zero-shot and Few-shot",
        "canonical": "Few-Shot Learning",
        "aliases": [
          "Zero-shot Learning",
          "Few-shot"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights the combination of learning paradigms used in the evaluation approach.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      },
      {
        "surface": "In-context Learning",
        "canonical": "In-context Learning",
        "aliases": [
          "ICL"
        ],
        "category": "unique_technical",
        "rationale": "Key technique used for teaching models in the proposed evaluation method.",
        "novelty_score": 0.65,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Evaluation Criteria",
        "canonical": "Evaluation Criteria",
        "aliases": [
          "In-house Criteria",
          "Criteria Division"
        ],
        "category": "unique_technical",
        "rationale": "Specific focus on tailoring evaluation metrics to domain-specific needs.",
        "novelty_score": 0.7,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "model-based evaluation",
      "prompt paradigm",
      "engineering approach"
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
      "candidate_surface": "Zero-shot and Few-shot",
      "resolved_canonical": "Few-Shot Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "In-context Learning",
      "resolved_canonical": "In-context Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Evaluation Criteria",
      "resolved_canonical": "Evaluation Criteria",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# TALEC: Teach Your LLM to Evaluate in Specific Domain with In-house Criteria by Criteria Division and Zero-shot Plus Few-shot

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2407.10999.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2407.10999](https://arxiv.org/abs/2407.10999)

## 🔗 유사한 논문
- [[2025-09-25/Integrated Framework for LLM Evaluation with Answer Generation_20250925|Integrated Framework for LLM Evaluation with Answer Generation]] (85.6% similar)
- [[2025-09-25/Do Before You Judge_ Self-Reference as a Pathway to Better LLM Evaluation_20250925|Do Before You Judge: Self-Reference as a Pathway to Better LLM Evaluation]] (85.4% similar)
- [[2025-09-25/Unveiling the Merits and Defects of LLMs in Automatic Review Generation for Scientific Papers_20250925|Unveiling the Merits and Defects of LLMs in Automatic Review Generation for Scientific Papers]] (85.2% similar)
- [[2025-09-22/Beyond Pointwise Scores_ Decomposed Criteria-Based Evaluation of LLM Responses_20250922|Beyond Pointwise Scores: Decomposed Criteria-Based Evaluation of LLM Responses]] (85.2% similar)
- [[2025-09-23/Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues_20250923|Evaluating LLM-Generated Versus Human-Authored Responses in Role-Play Dialogues]] (84.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Few-Shot Learning|Few-Shot Learning]]
**⚡ Unique Technical**: [[keywords/In-context Learning|In-context Learning]], [[keywords/Evaluation Criteria|Evaluation Criteria]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2407.10999v2 Announce Type: replace-cross 
Abstract: With the rapid development of large language models (LLM), the evaluation of LLM becomes increasingly important. Measuring text generation tasks such as summarization and article creation is very difficult. Especially in specific application domains (e.g., to-business or to-customer service), in-house evaluation criteria have to meet not only general standards (correctness, helpfulness and creativity, etc.) but also specific needs of customers and business security requirements at the same time, making the evaluation more difficult. So far, the evaluation of LLM in business scenarios has mainly relied on manual, which is expensive and time-consuming. In this paper, we propose a model-based evaluation method: TALEC, which allows users to flexibly set their own evaluation criteria, and uses in-context learning (ICL) to teach judge model these in-house criteria. In addition, we try combining zero-shot and few-shot to make the judge model focus on more information. We also propose a prompt paradigm and an engineering approach to adjust and iterate the shots ,helping judge model to better understand the complex criteria. We then compare fine-tuning with ICL, finding that fine-tuning can be replaced by ICL. TALEC demonstrates a strong capability to accurately reflect human preferences and achieves a correlation of over 80% with human judgments, outperforming even the inter-human correlation in some tasks. The code is released in https://github.com/zlkqz/auto_eval

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 평가 방법을 제안합니다. 특히, 비즈니스 시나리오에서의 LLM 평가가 수작업에 의존하여 비용이 많이 들고 시간이 소요되는 문제를 해결하기 위해, 사용자 맞춤형 평가 기준을 설정할 수 있는 모델 기반 평가 방법인 TALEC를 소개합니다. TALEC는 in-context learning(ICL)을 활용하여 평가 모델이 내부 기준을 학습하도록 하며, 제로샷과 퓨샷을 결합하여 더 많은 정보를 반영하도록 합니다. 또한, 프롬프트 패러다임과 엔지니어링 접근법을 통해 평가 모델이 복잡한 기준을 더 잘 이해할 수 있도록 돕습니다. 연구 결과, TALEC는 인간의 선호도를 정확히 반영하며, 인간 평가와 80% 이상의 상관관계를 보여줍니다. 이는 일부 작업에서 인간 간 상관관계보다 우수한 성과입니다. 코드도 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 평가 중요성이 증가하고 있으며, 특히 특정 응용 분야에서 평가 기준이 더욱 복잡해지고 있다.
- 2. 기존의 비즈니스 시나리오에서의 LLM 평가는 주로 수동으로 이루어져 비용이 많이 들고 시간이 소요된다.
- 3. TALEC라는 모델 기반 평가 방법을 제안하여 사용자들이 유연하게 평가 기준을 설정하고, in-context learning(ICL)을 통해 모델이 내부 기준을 학습하도록 한다.
- 4. 제안된 방법은 zero-shot과 few-shot을 결합하여 모델이 더 많은 정보를 집중하도록 하며, 프롬프트 패러다임과 엔지니어링 접근법을 통해 모델의 이해도를 높인다.
- 5. TALEC는 인간의 선호를 정확히 반영하며, 인간 평가와의 상관관계가 80% 이상으로, 일부 작업에서는 인간 간 상관관계보다 뛰어난 성능을 보인다.


---

*Generated on 2025-09-25 16:15:28*