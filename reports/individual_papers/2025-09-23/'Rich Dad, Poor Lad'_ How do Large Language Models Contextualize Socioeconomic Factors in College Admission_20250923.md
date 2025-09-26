---
keywords:
  - Large Language Model
  - Socioeconomic Status
  - Dual-Process Framework
  - College Admissions
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2509.16400
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:11:46.203522",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Socioeconomic Status",
    "Dual-Process Framework",
    "College Admissions"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Socioeconomic Status": 0.82,
    "Dual-Process Framework": 0.79,
    "College Admissions": 0.77
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
        "rationale": "Central to the paper's theme, linking to broader discussions on AI capabilities.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "socioeconomic status",
        "canonical": "Socioeconomic Status",
        "aliases": [
          "SES"
        ],
        "category": "unique_technical",
        "rationale": "Key factor in the study, relevant for linking to social science and ethics discussions.",
        "novelty_score": 0.72,
        "connectivity_score": 0.67,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "dual-process framework",
        "canonical": "Dual-Process Framework",
        "aliases": [
          "DPAF"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel methodological approach, crucial for understanding LLM reasoning.",
        "novelty_score": 0.85,
        "connectivity_score": 0.59,
        "specificity_score": 0.81,
        "link_intent_score": 0.79
      },
      {
        "surface": "college admissions decisions",
        "canonical": "College Admissions",
        "aliases": [
          "admissions decisions"
        ],
        "category": "specific_connectable",
        "rationale": "Specific application context for LLMs, linking to education and policy discussions.",
        "novelty_score": 0.58,
        "connectivity_score": 0.73,
        "specificity_score": 0.69,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "decision-only setup",
      "explanation-based setup"
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
      "candidate_surface": "socioeconomic status",
      "resolved_canonical": "Socioeconomic Status",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.67,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "dual-process framework",
      "resolved_canonical": "Dual-Process Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.59,
        "specificity": 0.81,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "college admissions decisions",
      "resolved_canonical": "College Admissions",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.73,
        "specificity": 0.69,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# 'Rich Dad, Poor Lad': How do Large Language Models Contextualize Socioeconomic Factors in College Admission ?

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.16400.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2509.16400](https://arxiv.org/abs/2509.16400)

## 🔗 유사한 논문
- [[2025-09-22/It Depends_ Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge_20250922|It Depends: Resolving Referential Ambiguity in Minimal Contexts with Commonsense Knowledge]] (85.7% similar)
- [[2025-09-23/Intrinsic Meets Extrinsic Fairness_ Assessing the Downstream Impact of Bias Mitigation in Large Language Models_20250923|Intrinsic Meets Extrinsic Fairness: Assessing the Downstream Impact of Bias Mitigation in Large Language Models]] (85.0% similar)
- [[2025-09-23/Steering Towards Fairness_ Mitigating Political Bias in LLMs_20250923|Steering Towards Fairness: Mitigating Political Bias in LLMs]] (84.9% similar)
- [[2025-09-23/Justice in Judgment_ Unveiling (Hidden) Bias in LLM-assisted Peer Reviews_20250923|Justice in Judgment: Unveiling (Hidden) Bias in LLM-assisted Peer Reviews]] (84.5% similar)
- [[2025-09-22/Bias Beware_ The Impact of Cognitive Biases on LLM-Driven Product Recommendations_20250922|Bias Beware: The Impact of Cognitive Biases on LLM-Driven Product Recommendations]] (84.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/College Admissions|College Admissions]]
**⚡ Unique Technical**: [[keywords/Socioeconomic Status|Socioeconomic Status]], [[keywords/Dual-Process Framework|Dual-Process Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.16400v1 Announce Type: new 
Abstract: Large Language Models (LLMs) are increasingly involved in high-stakes domains, yet how they reason about socially sensitive decisions remains underexplored. We present a large-scale audit of LLMs' treatment of socioeconomic status (SES) in college admissions decisions using a novel dual-process framework inspired by cognitive science. Leveraging a synthetic dataset of 30,000 applicant profiles grounded in real-world correlations, we prompt 4 open-source LLMs (Qwen 2, Mistral v0.3, Gemma 2, Llama 3.1) under 2 modes: a fast, decision-only setup (System 1) and a slower, explanation-based setup (System 2). Results from 5 million prompts reveal that LLMs consistently favor low-SES applicants -- even when controlling for academic performance -- and that System 2 amplifies this tendency by explicitly invoking SES as compensatory justification, highlighting both their potential and volatility as decision-makers. We then propose DPAF, a dual-process audit framework to probe LLMs' reasoning behaviors in sensitive applications.

## 📝 요약

이 논문은 대형 언어 모델(LLM)이 사회경제적 지위(SES)를 고려한 대학 입학 결정에서 어떻게 작용하는지를 대규모로 분석합니다. 연구는 인지과학에서 영감을 받은 이중 프로세스 프레임워크를 사용하여 30,000개의 합성 지원자 프로필을 기반으로 4개의 오픈소스 LLM(Qwen 2, Mistral v0.3, Gemma 2, Llama 3.1)을 평가했습니다. 두 가지 모드, 즉 빠른 결정 모드(System 1)와 설명 기반 모드(System 2)에서의 실험 결과, LLM은 일관되게 낮은 SES 지원자를 선호하며, System 2에서는 SES를 보상적 정당화로 명시적으로 언급하여 이 경향이 더욱 강화됨을 발견했습니다. 이러한 결과는 LLM의 잠재력과 변동성을 동시에 보여주며, 민감한 응용 분야에서 LLM의 추론 행동을 조사하기 위한 DPAF라는 이중 프로세스 감사 프레임워크를 제안합니다.

## 🎯 주요 포인트

- 1. 대규모 감사 연구를 통해 LLMs가 대학 입학 결정에서 사회경제적 지위(SES)를 어떻게 다루는지 조사했습니다.
- 2. 30,000개의 합성 지원자 프로필을 사용하여 4개의 오픈소스 LLMs를 두 가지 모드로 테스트했습니다: 빠른 결정 전용 모드(System 1)와 설명 기반 모드(System 2).
- 3. 연구 결과, LLMs는 학업 성과를 통제하더라도 일관되게 저소득층 지원자를 선호하는 경향을 보였습니다.
- 4. System 2 모드는 SES를 보상적 정당화로 명시적으로 언급하여 이러한 경향을 더욱 증폭시켰습니다.
- 5. 민감한 응용 분야에서 LLMs의 추론 행동을 조사하기 위해 DPAF라는 이중 프로세스 감사 프레임워크를 제안했습니다.


---

*Generated on 2025-09-24 03:11:46*