---
keywords:
  - Cognitive Behavioral Therapy
  - Large Language Model
  - Cognitive Therapy Rating Scale
  - Fine-tuning
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2412.00251
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T00:24:28.301773",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Cognitive Behavioral Therapy",
    "Large Language Model",
    "Cognitive Therapy Rating Scale",
    "Fine-tuning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Cognitive Behavioral Therapy": 0.8,
    "Large Language Model": 0.85,
    "Cognitive Therapy Rating Scale": 0.75,
    "Fine-tuning": 0.9
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Cognitive Behavioral Therapy",
        "canonical": "Cognitive Behavioral Therapy",
        "aliases": [
          "CBT"
        ],
        "category": "unique_technical",
        "rationale": "CBT is central to the study, focusing on its delivery through fine-tuned language models.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "The study involves fine-tuning LLMs, a key aspect of modern NLP research.",
        "novelty_score": 0.5,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Cognitive Therapy Rating Scale",
        "canonical": "Cognitive Therapy Rating Scale",
        "aliases": [
          "CTRS"
        ],
        "category": "unique_technical",
        "rationale": "CTRS is used to evaluate the fidelity of CBT delivery, crucial for assessing model performance.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.75
      },
      {
        "surface": "Fine-tuning",
        "canonical": "Fine-tuning",
        "aliases": [
          "Model Fine-tuning"
        ],
        "category": "specific_connectable",
        "rationale": "Fine-tuning is a critical process in adapting LLMs for specific tasks like CBT delivery.",
        "novelty_score": 0.6,
        "connectivity_score": 0.8,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      }
    ],
    "ban_list_suggestions": [
      "feasibility study",
      "simulated patient transcripts"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Cognitive Behavioral Therapy",
      "resolved_canonical": "Cognitive Behavioral Therapy",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Cognitive Therapy Rating Scale",
      "resolved_canonical": "Cognitive Therapy Rating Scale",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Fine-tuning",
      "resolved_canonical": "Fine-tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.8,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    }
  ]
}
-->

# Fine-Tuning Open-Weight Language Models to Deliver Cognitive Behavioral Therapy for Depression: A Feasibility Study

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2412.00251.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2412.00251](https://arxiv.org/abs/2412.00251)

## 🔗 유사한 논문
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (83.8% similar)
- [[2025-09-23/Multi-View Attention Multiple-Instance Learning Enhanced by LLM Reasoning for Cognitive Distortion Detection_20250923|Multi-View Attention Multiple-Instance Learning Enhanced by LLM Reasoning for Cognitive Distortion Detection]] (83.6% similar)
- [[2025-09-22/Do Retrieval Augmented Language Models Know When They Don't Know?_20250922|Do Retrieval Augmented Language Models Know When They Don't Know?]] (83.0% similar)
- [[2025-09-22/Calibrating LLM Confidence by Probing Perturbed Representation Stability_20250922|Calibrating LLM Confidence by Probing Perturbed Representation Stability]] (83.0% similar)
- [[2025-09-23/The Sound of Syntax_ Finetuning and Comprehensive Evaluation of Language Models for Speech Pathology_20250923|The Sound of Syntax: Finetuning and Comprehensive Evaluation of Language Models for Speech Pathology]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Fine-tuning|Fine-tuning]]
**⚡ Unique Technical**: [[keywords/Cognitive Behavioral Therapy|Cognitive Behavioral Therapy]], [[keywords/Cognitive Therapy Rating Scale|Cognitive Therapy Rating Scale]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2412.00251v2 Announce Type: replace 
Abstract: Cognitive Behavioral Therapy (CBT) is a well-established, evidence-based treatment for Major Depressive Disorder. Unfortunately, there exist significant barriers to individuals accessing CBT, including cost, scarcity of therapists and stigma. This study explores the feasibility of fine-tuning small open weight large language models (LLMs) to deliver CBT for depression. Using synthetic CBT transcripts generated by the Nous Research fine-tune of Llama 3.1 405b, we fine-tuned three models: Mistral 7b v0.3, Qwen 2.5 7b, and Llama 3.1 8b. CBT fidelity was evaluated through a modified Cognitive Therapy Rating Scale (CTRS). All fine-tuned models were compared against each other, as well as their instruct-tuned variants. Simulated patient transcripts were generated for the purpose of evaluating model performance, with the instruct and CBT-tuned models acting as the therapist and DeepSeek-V2.5 acting as the patient. These simulated transcripts were evaluated on a modified CTRS by Gemini 1.5 Pro-002. Our findings demonstrated that the CBT-tuned models significantly outperformed their instruct-tuned counterparts, with an average improvement of 11.33 points (p < 0.001) on total CTRS score. Llama 3.1 8b had the strongest performance (mean CTRS score 67.86 +/- 7.24), followed by Qwen 2.5 7b (64.28 +/- 9.55) and Mistral 7b v0.3 (64.17 +/- 9.79), with these differences between models being statistically significant. The CBT-tuned models were competent in implementing core CBT techniques and providing empathetic responses, however, there were limitations observed in agenda adherence, exploration depth and long-context coherence. This study establishes that CBT specific fine-tuning can effectively encode therapeutic competencies in small LLMs, though significant technical and ethical considerations must be resolved prior to clinical deployment.

## 📝 요약

이 연구는 주요 우울 장애 치료에 효과적인 인지 행동 치료(CBT)를 제공하기 위해 소형 대형 언어 모델(LLM)을 미세 조정하는 가능성을 탐구합니다. Nous Research의 Llama 3.1 405b를 기반으로 생성된 합성 CBT 대본을 사용하여 Mistral 7b v0.3, Qwen 2.5 7b, Llama 3.1 8b 모델을 미세 조정했습니다. 수정된 인지 치료 평가 척도(CTRS)를 통해 CBT 충실도를 평가한 결과, CBT 조정 모델이 지시 조정 모델보다 평균 11.33점 더 높은 CTRS 점수를 기록하며 우수한 성능을 보였습니다. Llama 3.1 8b가 가장 높은 성과를 보였으며, CBT 기법 구현과 공감적 응답에서 유능했으나, 일정 준수, 탐색 깊이, 긴 문맥 일관성에서 한계가 있었습니다. 이 연구는 CBT 특화 미세 조정이 소형 LLM에 치료적 역량을 효과적으로 부여할 수 있음을 보여주지만, 임상 적용 전 기술적, 윤리적 고려가 필요합니다.

## 🎯 주요 포인트

- 1. 인지행동치료(CBT)는 주요우울장애 치료에 효과적이지만, 비용, 치료사 부족, 낙인 등 접근 장벽이 존재한다.
- 2. 본 연구는 작은 대형 언어 모델(LLM)을 미세 조정하여 우울증 치료를 위한 CBT 제공 가능성을 탐구하였다.
- 3. CBT 미세 조정 모델이 지시 조정 모델보다 평균 11.33점 더 높은 CTRS 점수를 기록하며 우수한 성능을 보였다.
- 4. Llama 3.1 8b 모델이 가장 높은 성능을 보였으며, 모델 간의 성능 차이는 통계적으로 유의미했다.
- 5. CBT 미세 조정 모델은 핵심 CBT 기술 구현과 공감적 반응 제공에 능숙했으나, 일정 준수, 탐색 깊이, 장기 맥락 일관성에서 한계가 있었다.


---

*Generated on 2025-09-24 00:24:28*