---
keywords:
  - Automatic Speech Recognition
  - Dysarthric-Idiosyncratic Model
  - Normative Models
  - Idiosyncratic Models
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16718
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:39:31.560094",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Automatic Speech Recognition",
    "Dysarthric-Idiosyncratic Model",
    "Normative Models",
    "Idiosyncratic Models"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Automatic Speech Recognition": 0.78,
    "Dysarthric-Idiosyncratic Model": 0.79,
    "Normative Models": 0.74,
    "Idiosyncratic Models": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "automatic speech recognition",
        "canonical": "Automatic Speech Recognition",
        "aliases": [
          "ASR"
        ],
        "category": "broad_technical",
        "rationale": "ASR is a foundational technology in speech processing, linking to broader research in machine learning and natural language processing.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.78
      },
      {
        "surface": "dysarthric-idiosyncratic model",
        "canonical": "Dysarthric-Idiosyncratic Model",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "This model uniquely combines normative and idiosyncratic strategies, offering insights into personalized ASR for atypical speech.",
        "novelty_score": 0.75,
        "connectivity_score": 0.68,
        "specificity_score": 0.82,
        "link_intent_score": 0.79
      },
      {
        "surface": "normative models",
        "canonical": "Normative Models",
        "aliases": [
          "generalized models"
        ],
        "category": "specific_connectable",
        "rationale": "Normative models are crucial for understanding the generalization capabilities in ASR systems.",
        "novelty_score": 0.55,
        "connectivity_score": 0.77,
        "specificity_score": 0.7,
        "link_intent_score": 0.74
      },
      {
        "surface": "idiosyncratic models",
        "canonical": "Idiosyncratic Models",
        "aliases": [
          "personalized models"
        ],
        "category": "specific_connectable",
        "rationale": "Idiosyncratic models highlight the importance of personalization in ASR for atypical speech.",
        "novelty_score": 0.58,
        "connectivity_score": 0.79,
        "specificity_score": 0.72,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "atypical speech",
      "speech encoder",
      "word error rate"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "automatic speech recognition",
      "resolved_canonical": "Automatic Speech Recognition",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "dysarthric-idiosyncratic model",
      "resolved_canonical": "Dysarthric-Idiosyncratic Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.68,
        "specificity": 0.82,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "normative models",
      "resolved_canonical": "Normative Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.77,
        "specificity": 0.7,
        "link_intent": 0.74
      }
    },
    {
      "candidate_surface": "idiosyncratic models",
      "resolved_canonical": "Idiosyncratic Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.79,
        "specificity": 0.72,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Idiosyncratic Versus Normative Modeling of Atypical Speech Recognition: Dysarthric Case Studies

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16718.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16718](https://arxiv.org/abs/2509.16718)

## 🔗 유사한 논문
- [[2025-09-22/AS-ASR_ A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition_20250922|AS-ASR: A Lightweight Framework for Aphasia-Specific Automatic Speech Recognition]] (85.6% similar)
- [[2025-09-22/Fine-Tuning Large Multimodal Models for Automatic Pronunciation Assessment_20250922|Fine-Tuning Large Multimodal Models for Automatic Pronunciation Assessment]] (83.0% similar)
- [[2025-09-17/Deploying UDM Series in Real-Life Stuttered Speech Applications_ A Clinical Evaluation Framework_20250917|Deploying UDM Series in Real-Life Stuttered Speech Applications: A Clinical Evaluation Framework]] (82.8% similar)
- [[2025-09-23/Leveraging Multilingual Training for Authorship Representation_ Enhancing Generalization across Languages and Domains_20250923|Leveraging Multilingual Training for Authorship Representation: Enhancing Generalization across Languages and Domains]] (82.5% similar)
- [[2025-09-19/Listening, Imagining \& Refining_ A Heuristic Optimized ASR Correction Framework with LLMs_20250919|Listening, Imagining \& Refining: A Heuristic Optimized ASR Correction Framework with LLMs]] (82.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Automatic Speech Recognition|Automatic Speech Recognition]]
**🔗 Specific Connectable**: [[keywords/Normative Models|Normative Models]], [[keywords/Idiosyncratic Models|Idiosyncratic Models]]
**⚡ Unique Technical**: [[keywords/Dysarthric-Idiosyncratic Model|Dysarthric-Idiosyncratic Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16718v1 Announce Type: cross 
Abstract: State-of-the-art automatic speech recognition (ASR) models like Whisper, perform poorly on atypical speech, such as that produced by individuals with dysarthria. Past works for atypical speech have mostly investigated fully personalized (or idiosyncratic) models, but modeling strategies that can both generalize and handle idiosyncracy could be more effective for capturing atypical speech. To investigate this, we compare four strategies: (a) $\textit{normative}$ models trained on typical speech (no personalization), (b) $\textit{idiosyncratic}$ models completely personalized to individuals, (c) $\textit{dysarthric-normative}$ models trained on other dysarthric speakers, and (d) $\textit{dysarthric-idiosyncratic}$ models which combine strategies by first modeling normative patterns before adapting to individual speech. In this case study, we find the dysarthric-idiosyncratic model performs better than idiosyncratic approach while requiring less than half as much personalized data (36.43 WER with 128 train size vs 36.99 with 256). Further, we found that tuning the speech encoder alone (as opposed to the LM decoder) yielded the best results reducing word error rate from 71% to 32% on average. Our findings highlight the value of leveraging both normative (cross-speaker) and idiosyncratic (speaker-specific) patterns to improve ASR for underrepresented speech populations.

## 📝 요약

이 논문은 비정형 발화, 특히 운동장애로 인한 발화를 인식하는 자동 음성 인식(ASR) 모델의 성능 개선을 다룹니다. 기존 연구는 주로 개인화된 모델에 집중했으나, 일반화와 개인화를 동시에 고려하는 전략이 더 효과적일 수 있음을 제안합니다. 네 가지 모델 전략을 비교한 결과, 비정형-개인화 모델이 개인화 모델보다 적은 데이터로도 더 나은 성능을 보였습니다. 특히, 음성 인코더만 조정했을 때 단어 오류율이 평균 71%에서 32%로 감소했습니다. 이는 일반적 패턴과 개인적 패턴을 모두 활용하는 것이 비정형 발화 인식 개선에 유용함을 시사합니다.

## 🎯 주요 포인트

- 1. Whisper와 같은 최신 자동 음성 인식(ASR) 모델은 이형성 언어, 특히 운동장애를 가진 개인이 생성한 음성에 대해 성능이 저조하다.
- 2. 이형성 언어를 위한 모델링 전략은 일반화와 개별화 모두를 처리할 수 있는 접근이 더 효과적일 수 있다.
- 3. 연구에서는 네 가지 전략을 비교했으며, 이 중 dysarthric-idiosyncratic 모델이 idiosyncratic 모델보다 적은 개인화 데이터를 사용하면서도 더 나은 성능을 보였다.
- 4. 음성 인코더만을 조정하는 것이 언어 모델 디코더를 조정하는 것보다 더 나은 결과를 가져왔으며, 평균 단어 오류율을 71%에서 32%로 줄였다.
- 5. 연구 결과는 일반적인 패턴과 개별적인 패턴을 모두 활용하는 것이 대표성이 부족한 음성 인구에 대한 ASR 개선에 중요함을 강조한다.


---

*Generated on 2025-09-24 03:39:31*