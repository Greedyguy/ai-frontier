---
keywords:
  - Large Language Model
  - MediGen
  - Fine-Tuning
  - Electronic Health Records
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2409.09324
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T16:16:42.965614",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "MediGen",
    "Fine-Tuning",
    "Electronic Health Records"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "MediGen": 0.7,
    "Fine-Tuning": 0.78,
    "Electronic Health Records": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the study and connect well with existing research on language models and AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "MediGen",
        "canonical": "MediGen",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "MediGen represents a specific application of LLMs in medical documentation, offering unique insights into this niche.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Fine-Tuning",
        "canonical": "Fine-Tuning",
        "aliases": [
          "Model Fine-Tuning"
        ],
        "category": "specific_connectable",
        "rationale": "Fine-tuning is a critical process in adapting large models to specific tasks, enhancing connectivity with model training techniques.",
        "novelty_score": 0.5,
        "connectivity_score": 0.82,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Electronic Health Records",
        "canonical": "Electronic Health Records",
        "aliases": [
          "EHRs"
        ],
        "category": "specific_connectable",
        "rationale": "EHRs are a significant part of the administrative burden in healthcare, linking to studies on healthcare technology.",
        "novelty_score": 0.4,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "administrative tasks",
      "healthcare delivery"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
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
      "candidate_surface": "MediGen",
      "resolved_canonical": "MediGen",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Fine-Tuning",
      "resolved_canonical": "Fine-Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.82,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Electronic Health Records",
      "resolved_canonical": "Electronic Health Records",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Efficient Fine-Tuning of Large Language Models for Automated Medical Documentation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2409.09324.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2409.09324](https://arxiv.org/abs/2409.09324)

## 🔗 유사한 논문
- [[2025-09-23/SparseDoctor_ Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models_20250923|SparseDoctor: Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models]] (87.7% similar)
- [[2025-09-19/MedVAL_ Toward Expert-Level Medical Text Validation with Language Models_20250919|MedVAL: Toward Expert-Level Medical Text Validation with Language Models]] (86.6% similar)
- [[2025-09-24/Advances in Large Language Models for Medicine_20250924|Advances in Large Language Models for Medicine]] (86.1% similar)
- [[2025-09-22/EHR-MCP_ Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol_20250922|EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large Language Models via Model Context Protocol]] (86.0% similar)
- [[2025-09-18/Integrating Text and Time-Series into (Large) Language Models to Predict Medical Outcomes_20250918|Integrating Text and Time-Series into (Large) Language Models to Predict Medical Outcomes]] (85.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Fine-Tuning|Fine-Tuning]], [[keywords/Electronic Health Records|Electronic Health Records]]
**⚡ Unique Technical**: [[keywords/MediGen|MediGen]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2409.09324v3 Announce Type: replace-cross 
Abstract: Scientific research indicates that for every hour spent in direct patient care, physicians spend nearly two additional hours on administrative tasks, particularly on electronic health records (EHRs) and desk work. This excessive administrative burden not only reduces the time available for patient care but also contributes to physician burnout and inefficiencies in healthcare delivery. To address these challenges, this study introduces MediGen, a fine-tuned large language model (LLM) designed to automate the generation of medical reports from medical dialogues. By leveraging state-of-the-art methodologies for fine-tuning open-source pretrained models, including LLaMA3-8B, MediGen achieves high accuracy in transcribing and summarizing clinical interactions. The fine-tuned LLaMA3-8B model demonstrated promising results, achieving a ROUGE score of 58% and a BERTScore-F1 of 72%, indicating its effectiveness in generating accurate and clinically relevant medical reports. These findings suggest that MediGen has the potential to significantly reduce the administrative workload on physicians, improving both healthcare efficiency and physician well-being.

## 📝 요약

이 연구는 의사들이 환자 진료 외에 전자의무기록(EHR) 및 사무 작업에 많은 시간을 소모하는 문제를 해결하기 위해 MediGen이라는 대형 언어 모델(LLM)을 소개합니다. MediGen은 의료 대화를 자동으로 보고서로 생성하며, LLaMA3-8B 등 최신 기법을 활용해 높은 정확도를 달성했습니다. 이 모델은 ROUGE 점수 58%, BERTScore-F1 72%를 기록하며, 정확하고 임상적으로 유의미한 보고서를 생성하는 데 효과적임을 보여줍니다. 이를 통해 의사들의 행정 업무 부담을 줄이고, 의료 효율성과 의사들의 복지를 향상시킬 잠재력이 있음을 시사합니다.

## 🎯 주요 포인트

- 1. 의사들은 환자 진료에 직접적으로 한 시간을 보낼 때마다 추가로 두 시간을 행정 업무에 소비한다.
- 2. 과도한 행정 업무는 환자 진료 시간을 줄이고, 의사 번아웃과 의료 서비스 비효율성을 초래한다.
- 3. MediGen은 의료 대화로부터 의료 보고서를 자동 생성하는 대형 언어 모델로, 행정 업무를 줄이는 데 기여할 수 있다.
- 4. MediGen은 LLaMA3-8B 모델을 미세 조정하여 높은 정확도로 임상 상호작용을 전사 및 요약한다.
- 5. MediGen은 ROUGE 점수 58%와 BERTScore-F1 72%를 기록하며, 정확하고 임상적으로 관련 있는 보고서를 생성하는 데 효과적이다.


---

*Generated on 2025-09-25 16:16:42*