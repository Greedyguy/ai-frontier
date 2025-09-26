---
keywords:
  - Large Language Model
  - Multilingual Fact-Checked Claim Detection
  - Cross-Lingual Settings
  - Low-Resource Languages
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2503.02737
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:52:36.540616",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Multilingual Fact-Checked Claim Detection",
    "Cross-Lingual Settings",
    "Low-Resource Languages"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Multilingual Fact-Checked Claim Detection": 0.78,
    "Cross-Lingual Settings": 0.77,
    "Low-Resource Languages": 0.8
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
        "rationale": "Large Language Models are central to the paper's evaluation and are a key concept in NLP research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Multilingual Fact-Checked Claim Detection",
        "canonical": "Multilingual Fact-Checked Claim Detection",
        "aliases": [
          "Cross-Lingual Claim Verification"
        ],
        "category": "unique_technical",
        "rationale": "This is a unique application of LLMs that addresses a specific challenge in multilingual information verification.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Cross-Lingual Settings",
        "canonical": "Cross-Lingual Settings",
        "aliases": [
          "Cross-Language Contexts"
        ],
        "category": "specific_connectable",
        "rationale": "Cross-lingual settings are crucial for understanding the performance of LLMs across different languages.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      },
      {
        "surface": "Low-Resource Languages",
        "canonical": "Low-Resource Languages",
        "aliases": [
          "Under-Resourced Languages"
        ],
        "category": "specific_connectable",
        "rationale": "Addressing challenges in low-resource languages is vital for the inclusivity of multilingual NLP applications.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "high-resource languages",
      "translating original texts"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Multilingual Fact-Checked Claim Detection",
      "resolved_canonical": "Multilingual Fact-Checked Claim Detection",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Cross-Lingual Settings",
      "resolved_canonical": "Cross-Lingual Settings",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    },
    {
      "candidate_surface": "Low-Resource Languages",
      "resolved_canonical": "Low-Resource Languages",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Large Language Models for Multilingual Previously Fact-Checked Claim Detection

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2503.02737.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2503.02737](https://arxiv.org/abs/2503.02737)

## 🔗 유사한 논문
- [[2025-09-23/Multilingual vs Crosslingual Retrieval of Fact-Checked Claims_ A Tale of Two Approaches_20250923|Multilingual vs Crosslingual Retrieval of Fact-Checked Claims: A Tale of Two Approaches]] (90.5% similar)
- [[2025-09-23/MAKIEval_ A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs_20250923|MAKIEval: A Multilingual Automatic WiKidata-based Framework for Cultural Awareness Evaluation for LLMs]] (86.4% similar)
- [[2025-09-22/A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages_20250922|A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages]] (86.1% similar)
- [[2025-09-22/PolBiX_ Detecting LLMs' Political Bias in Fact-Checking through X-phemisms_20250922|PolBiX: Detecting LLMs' Political Bias in Fact-Checking through X-phemisms]] (85.8% similar)
- [[2025-09-23/Breaking the Reviewer_ Assessing the Vulnerability of Large Language Models in Automated Peer Review Under Textual Adversarial Attacks_20250923|Breaking the Reviewer: Assessing the Vulnerability of Large Language Models in Automated Peer Review Under Textual Adversarial Attacks]] (85.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Cross-Lingual Settings|Cross-Lingual Settings]], [[keywords/Low-Resource Languages|Low-Resource Languages]]
**⚡ Unique Technical**: [[keywords/Multilingual Fact-Checked Claim Detection|Multilingual Fact-Checked Claim Detection]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.02737v3 Announce Type: replace 
Abstract: In our era of widespread false information, human fact-checkers often face the challenge of duplicating efforts when verifying claims that may have already been addressed in other countries or languages. As false information transcends linguistic boundaries, the ability to automatically detect previously fact-checked claims across languages has become an increasingly important task. This paper presents the first comprehensive evaluation of large language models (LLMs) for multilingual previously fact-checked claim detection. We assess seven LLMs across 20 languages in both monolingual and cross-lingual settings. Our results show that while LLMs perform well for high-resource languages, they struggle with low-resource languages. Moreover, translating original texts into English proved to be beneficial for low-resource languages. These findings highlight the potential of LLMs for multilingual previously fact-checked claim detection and provide a foundation for further research on this promising application of LLMs.

## 📝 요약

이 논문은 다국어 환경에서 이미 사실 확인된 주장들을 자동으로 탐지하는 대규모 언어 모델(LLM)의 성능을 평가한 최초의 연구를 제시합니다. 20개 언어에서 7개의 LLM을 단일 언어 및 교차 언어 설정으로 평가한 결과, LLM은 자원이 풍부한 언어에서는 우수한 성능을 보였으나, 자원이 부족한 언어에서는 성능이 저조했습니다. 특히, 저자원 언어의 경우 원문을 영어로 번역하는 것이 유리하다는 점을 발견했습니다. 이 연구는 LLM을 활용한 다국어 사실 확인 탐지의 가능성을 보여주며, 향후 연구의 기초를 제공합니다.

## 🎯 주요 포인트

- 1. 거짓 정보가 언어적 경계를 넘어 확산됨에 따라 다국어로 이전에 사실 확인된 주장을 자동으로 탐지하는 능력이 중요해지고 있다.
- 2. 이 논문은 대형 언어 모델(LLM)을 활용한 다국어 이전 사실 확인 주장 탐지에 대한 최초의 종합적인 평가를 제시한다.
- 3. 20개 언어에서 7개의 LLM을 평가한 결과, LLM은 자원이 풍부한 언어에서는 성능이 좋지만, 자원이 부족한 언어에서는 어려움을 겪는 것으로 나타났다.
- 4. 자원이 부족한 언어의 경우, 원문을 영어로 번역하는 것이 유익한 것으로 드러났다.
- 5. 이러한 연구 결과는 LLM을 활용한 다국어 이전 사실 확인 주장 탐지의 잠재력을 강조하며, 이 분야의 추가 연구를 위한 기초를 제공한다.


---

*Generated on 2025-09-26 08:52:36*