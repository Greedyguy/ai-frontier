---
keywords:
  - LLM-Filter
  - Large Language Model
  - System-as-Prompt
  - State Estimation
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.20051
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:57:39.627960",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "LLM-Filter",
    "Large Language Model",
    "System-as-Prompt",
    "State Estimation"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "LLM-Filter": 0.8,
    "Large Language Model": 0.85,
    "System-as-Prompt": 0.78,
    "State Estimation": 0.82
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "LLM-Filter",
        "canonical": "LLM-Filter",
        "aliases": [
          "Large Language Model Filter"
        ],
        "category": "unique_technical",
        "rationale": "Represents a novel approach leveraging LLMs for state estimation, offering unique insights into filtering tasks.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Central to the proposed method, connecting to a wide range of applications in AI.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "System-as-Prompt",
        "canonical": "System-as-Prompt",
        "aliases": [
          "SaP"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel prompt design strategy that enhances LLM understanding in estimation tasks.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "state estimation",
        "canonical": "State Estimation",
        "aliases": [
          "hidden state estimation"
        ],
        "category": "specific_connectable",
        "rationale": "A key concept in the paper, linking to various applications in dynamical systems.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.75,
        "link_intent_score": 0.82
      }
    ],
    "ban_list_suggestions": [
      "dynamical systems",
      "optimal filtering",
      "estimation tasks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "LLM-Filter",
      "resolved_canonical": "LLM-Filter",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "System-as-Prompt",
      "resolved_canonical": "System-as-Prompt",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "state estimation",
      "resolved_canonical": "State Estimation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.75,
        "link_intent": 0.82
      }
    }
  ]
}
-->

# One Filters All: A Generalist Filter for State Estimation

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.20051.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.20051](https://arxiv.org/abs/2509.20051)

## 🔗 유사한 논문
- [[2025-09-23/SignalLLM_ A General-Purpose LLM Agent Framework for Automated Signal Processing_20250923|SignalLLM: A General-Purpose LLM Agent Framework for Automated Signal Processing]] (85.1% similar)
- [[2025-09-24/Prior-based Noisy Text Data Filtering_ Fast and Strong Alternative For Perplexity_20250924|Prior-based Noisy Text Data Filtering: Fast and Strong Alternative For Perplexity]] (82.8% similar)
- [[2025-09-23/A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue_20250923|A State-Update Prompting Strategy for Efficient and Robust Multi-turn Dialogue]] (82.6% similar)
- [[2025-09-19/Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (82.5% similar)
- [[2025-09-22/Not All Parameters Are Created Equal_ Smart Isolation Boosts Fine-Tuning Performance_20250922|Not All Parameters Are Created Equal: Smart Isolation Boosts Fine-Tuning Performance]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/State Estimation|State Estimation]]
**⚡ Unique Technical**: [[keywords/LLM-Filter|LLM-Filter]], [[keywords/System-as-Prompt|System-as-Prompt]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.20051v1 Announce Type: cross 
Abstract: Estimating hidden states in dynamical systems, also known as optimal filtering, is a long-standing problem in various fields of science and engineering. In this paper, we introduce a general filtering framework, \textbf{LLM-Filter}, which leverages large language models (LLMs) for state estimation by embedding noisy observations with text prototypes. In various experiments for classical dynamical systems, we find that first, state estimation can significantly benefit from the reasoning knowledge embedded in pre-trained LLMs. By achieving proper modality alignment with the frozen LLM, LLM-Filter outperforms the state-of-the-art learning-based approaches. Second, we carefully design the prompt structure, System-as-Prompt (SaP), incorporating task instructions that enable the LLM to understand the estimation tasks. Guided by these prompts, LLM-Filter exhibits exceptional generalization, capable of performing filtering tasks accurately in changed or even unseen environments. We further observe a scaling-law behavior in LLM-Filter, where accuracy improves with larger model sizes and longer training times. These findings make LLM-Filter a promising foundation model of filtering.

## 📝 요약

이 논문은 동적 시스템에서 숨겨진 상태를 추정하는 문제를 해결하기 위해 대형 언어 모델(LLM)을 활용한 일반 필터링 프레임워크인 LLM-Filter를 소개합니다. LLM-Filter는 노이즈가 있는 관측치를 텍스트 프로토타입과 결합하여 상태 추정을 수행합니다. 실험 결과, 사전 학습된 LLM의 추론 지식을 활용하면 상태 추정의 성능이 크게 향상됨을 확인했습니다. 또한, System-as-Prompt(SaP)라는 프롬프트 구조를 설계하여 LLM이 추정 작업을 이해하도록 했으며, 이를 통해 변화된 환경에서도 정확한 필터링 작업을 수행할 수 있는 뛰어난 일반화 능력을 보였습니다. 모델 크기와 학습 시간이 증가할수록 정확도가 향상되는 스케일링 법칙도 관찰되었습니다. 이러한 결과는 LLM-Filter가 필터링의 유망한 기초 모델임을 시사합니다.

## 🎯 주요 포인트

- 1. LLM-Filter는 대형 언어 모델(LLM)을 활용하여 상태 추정 문제를 해결하는 일반적인 필터링 프레임워크를 제안합니다.
- 2. 사전 학습된 LLM의 추론 지식을 활용하여 상태 추정의 성능을 크게 향상시킬 수 있습니다.
- 3. System-as-Prompt(SaP) 구조를 통해 LLM이 추정 작업을 이해할 수 있도록 설계하여, 변화된 환경에서도 정확한 필터링 작업을 수행할 수 있습니다.
- 4. LLM-Filter는 모델 크기와 학습 시간이 증가할수록 정확도가 향상되는 스케일링 법칙을 보입니다.
- 5. LLM-Filter는 필터링의 유망한 기초 모델로서의 가능성을 보여줍니다.


---

*Generated on 2025-09-25 15:57:39*