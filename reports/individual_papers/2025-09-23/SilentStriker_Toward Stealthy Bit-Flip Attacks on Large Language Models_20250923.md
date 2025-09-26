---
keywords:
  - Large Language Model
  - Bit-Flip Attack
  - SilentStriker
  - Output Naturalness
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2509.17371
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T02:22:43.514077",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Bit-Flip Attack",
    "SilentStriker",
    "Output Naturalness"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Bit-Flip Attack": 0.78,
    "SilentStriker": 0.8,
    "Output Naturalness": 0.72
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
        "rationale": "Central to the paper's focus on security vulnerabilities in LLMs.",
        "novelty_score": 0.2,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Bit-Flip Attacks",
        "canonical": "Bit-Flip Attack",
        "aliases": [
          "BFA"
        ],
        "category": "unique_technical",
        "rationale": "A unique attack method discussed extensively in the paper.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "SilentStriker",
        "canonical": "SilentStriker",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The primary novel contribution of the paper, representing a new attack method.",
        "novelty_score": 0.85,
        "connectivity_score": 0.5,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "output naturalness",
        "canonical": "Output Naturalness",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A key metric for evaluating the stealthiness of attacks on LLMs.",
        "novelty_score": 0.4,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.72
      }
    ],
    "ban_list_suggestions": [
      "performance degradation",
      "task performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.2,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Bit-Flip Attacks",
      "resolved_canonical": "Bit-Flip Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "SilentStriker",
      "resolved_canonical": "SilentStriker",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.5,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "output naturalness",
      "resolved_canonical": "Output Naturalness",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.72
      }
    }
  ]
}
-->

# SilentStriker:Toward Stealthy Bit-Flip Attacks on Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.17371.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2509.17371](https://arxiv.org/abs/2509.17371)

## 🔗 유사한 논문
- [[2025-09-23/MIST_ Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning_20250923|MIST: Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning]] (83.4% similar)
- [[2025-09-22/Inverting Trojans in LLMs_20250922|Inverting Trojans in LLMs]] (83.0% similar)
- [[2025-09-22/AdaSteer_ Your Aligned LLM is Inherently an Adaptive Jailbreak Defender_20250922|AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender]] (82.5% similar)
- [[2025-09-22/SABER_ Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection_20250922|SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection]] (82.1% similar)
- [[2025-09-23/Targeting Alignment_ Extracting Safety Classifiers of Aligned LLMs_20250923|Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs]] (81.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Output Naturalness|Output Naturalness]]
**⚡ Unique Technical**: [[keywords/Bit-Flip Attack|Bit-Flip Attack]], [[keywords/SilentStriker|SilentStriker]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.17371v1 Announce Type: cross 
Abstract: The rapid adoption of large language models (LLMs) in critical domains has spurred extensive research into their security issues. While input manipulation attacks (e.g., prompt injection) have been well studied, Bit-Flip Attacks (BFAs) -- which exploit hardware vulnerabilities to corrupt model parameters and cause severe performance degradation -- have received far less attention. Existing BFA methods suffer from key limitations: they fail to balance performance degradation and output naturalness, making them prone to discovery. In this paper, we introduce SilentStriker, the first stealthy bit-flip attack against LLMs that effectively degrades task performance while maintaining output naturalness. Our core contribution lies in addressing the challenge of designing effective loss functions for LLMs with variable output length and the vast output space. Unlike prior approaches that rely on output perplexity for attack loss formulation, which inevitably degrade output naturalness, we reformulate the attack objective by leveraging key output tokens as targets for suppression, enabling effective joint optimization of attack effectiveness and stealthiness. Additionally, we employ an iterative, progressive search strategy to maximize attack efficacy. Experiments show that SilentStriker significantly outperforms existing baselines, achieving successful attacks without compromising the naturalness of generated text.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 보안 취약점을 악용하는 비트 플립 공격(BFA)에 대해 다룹니다. 기존의 BFA는 성능 저하와 출력 자연스러움 간의 균형을 맞추지 못해 쉽게 발견되는 한계가 있었습니다. 본 연구는 이러한 문제를 해결하기 위해 SilentStriker라는 새로운 비트 플립 공격 기법을 제안합니다. SilentStriker는 출력 자연스러움을 유지하면서도 모델의 작업 성능을 효과적으로 저하시킵니다. 이를 위해 다양한 출력 길이와 방대한 출력 공간을 고려한 손실 함수 설계 문제를 해결하고, 주요 출력 토큰을 억제 대상으로 삼아 공격의 효과성과 은밀성을 동시에 최적화합니다. 실험 결과, SilentStriker는 기존 방법들보다 우수한 성능을 보이며, 자연스러운 텍스트 생성을 유지하면서도 성공적인 공격을 수행할 수 있음을 입증했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 보안 문제 중 하드웨어 취약점을 이용한 Bit-Flip 공격(BFA)에 대한 연구가 부족하다.
- 2. 기존 BFA 방법은 성능 저하와 출력 자연스러움의 균형을 맞추지 못해 쉽게 발견될 수 있다.
- 3. SilentStriker는 LLM에 대한 최초의 은밀한 BFA로, 성능 저하와 출력 자연스러움을 동시에 유지한다.
- 4. SilentStriker는 출력 혼란도를 이용한 기존 공격 손실 공식화를 개선하여, 주요 출력 토큰을 억제하는 방식으로 공격 목표를 재구성한다.
- 5. 실험 결과, SilentStriker는 기존의 방법들보다 뛰어난 성능을 보이며, 생성된 텍스트의 자연스러움을 손상시키지 않고 성공적인 공격을 달성한다.


---

*Generated on 2025-09-24 02:22:43*