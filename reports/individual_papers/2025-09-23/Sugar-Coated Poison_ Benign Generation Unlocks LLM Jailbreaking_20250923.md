---
keywords:
  - Large Language Model
  - Defense Threshold Decay
  - Sugar-Coated Poison
  - Part-of-Speech Defense
  - Prompt Engineering
category: cs.CL
publish_date: 2025-09-23
arxiv_id: 2504.05652
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T04:15:59.418069",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Defense Threshold Decay",
    "Sugar-Coated Poison",
    "Part-of-Speech Defense",
    "Prompt Engineering"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Defense Threshold Decay": 0.78,
    "Sugar-Coated Poison": 0.82,
    "Part-of-Speech Defense": 0.8,
    "Prompt Engineering": 0.7
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
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's discussion on safety mechanisms and jailbreak attacks.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.85
      },
      {
        "surface": "Defense Threshold Decay",
        "canonical": "Defense Threshold Decay",
        "aliases": [
          "DTD"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel concept affecting LLM safety, pivotal for understanding the proposed attack.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sugar-Coated Poison",
        "canonical": "Sugar-Coated Poison",
        "aliases": [
          "SCP"
        ],
        "category": "unique_technical",
        "rationale": "Represents a new attack paradigm that is central to the paper's contribution.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.82
      },
      {
        "surface": "Part-of-Speech Defense",
        "canonical": "Part-of-Speech Defense",
        "aliases": [
          "POSD"
        ],
        "category": "unique_technical",
        "rationale": "Proposed defense mechanism leveraging syntactic analysis, crucial for enhancing LLM safety.",
        "novelty_score": 0.7,
        "connectivity_score": 0.68,
        "specificity_score": 0.78,
        "link_intent_score": 0.8
      },
      {
        "surface": "Prompt Engineering",
        "canonical": "Prompt Engineering",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "A key technique in jailbreak attacks, relevant for linking discussions on LLM vulnerabilities.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "jailbreak attacks",
      "safety mechanisms"
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
        "specificity": 0.7,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Defense Threshold Decay",
      "resolved_canonical": "Defense Threshold Decay",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sugar-Coated Poison",
      "resolved_canonical": "Sugar-Coated Poison",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Part-of-Speech Defense",
      "resolved_canonical": "Part-of-Speech Defense",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.68,
        "specificity": 0.78,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Prompt Engineering",
      "resolved_canonical": "Prompt Engineering",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2504.05652.pdf)
**Category**: cs.CL
**Published**: 2025-09-23
**ArXiv ID**: [2504.05652](https://arxiv.org/abs/2504.05652)

## 🔗 유사한 논문
- [[2025-09-23/Targeting Alignment_ Extracting Safety Classifiers of Aligned LLMs_20250923|Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs]] (88.9% similar)
- [[2025-09-23/Adaptive Distraction_ Probing LLM Contextual Robustness with Automated Tree Search_20250923|Adaptive Distraction: Probing LLM Contextual Robustness with Automated Tree Search]] (88.8% similar)
- [[2025-09-23/Revisiting Backdoor Attacks on LLMs_ A Stealthy and Practical Poisoning Framework via Harmless Inputs_20250923|Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs]] (88.5% similar)
- [[2025-09-23/MIST_ Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning_20250923|MIST: Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning]] (88.3% similar)
- [[2025-09-22/SABER_ Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection_20250922|SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection]] (88.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Prompt Engineering|Prompt Engineering]]
**⚡ Unique Technical**: [[keywords/Defense Threshold Decay|Defense Threshold Decay]], [[keywords/Sugar-Coated Poison|Sugar-Coated Poison]], [[keywords/Part-of-Speech Defense|Part-of-Speech Defense]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.05652v3 Announce Type: replace-cross 
Abstract: With the increasingly deep integration of large language models (LLMs) across diverse domains, the effectiveness of their safety mechanisms is encountering severe challenges. Currently, jailbreak attacks based on prompt engineering have become a major safety threat. However, existing methods primarily rely on black-box manipulation of prompt templates, resulting in poor interpretability and limited generalization. To break through the bottleneck, this study first introduces the concept of Defense Threshold Decay (DTD), revealing the potential safety impact caused by LLMs' benign generation: as benign content generation in LLMs increases, the model's focus on input instructions progressively diminishes. Building on this insight, we propose the Sugar-Coated Poison (SCP) attack paradigm, which uses a "semantic reversal" strategy to craft benign inputs that are opposite in meaning to malicious intent. This strategy induces the models to generate extensive benign content, thereby enabling adversarial reasoning to bypass safety mechanisms. Experiments show that SCP outperforms existing baselines. Remarkably, it achieves an average attack success rate of 87.23% across six LLMs. For defense, we propose Part-of-Speech Defense (POSD), leveraging verb-noun dependencies for syntactic analysis to enhance safety of LLMs while preserving their generalization ability.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 안전 메커니즘이 직면한 문제를 다룹니다. 기존의 프롬프트 엔지니어링 기반 탈옥 공격은 해석 가능성과 일반화가 제한적입니다. 이를 해결하기 위해, 연구는 '방어 임계값 감쇠(DTD)' 개념을 도입하여 LLM의 안전성에 영향을 미치는 요인을 분석합니다. 이를 바탕으로 '설탕 코팅 독(SCP)' 공격 패러다임을 제안하며, 이는 의미 반전 전략을 사용해 악의적 의도를 가진 입력을 무해한 것으로 위장하여 모델의 안전 메커니즘을 우회합니다. 실험 결과 SCP는 기존 방법들보다 뛰어난 성과를 보이며, 평균 87.23%의 공격 성공률을 기록했습니다. 방어 측면에서는 동사-명사 의존성을 활용한 '품사 방어(POSD)'를 제안하여 LLM의 안전성을 강화합니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)의 안전 메커니즘이 점점 더 심각한 도전에 직면하고 있으며, 프롬프트 엔지니어링을 기반으로 한 탈옥 공격이 주요 위협으로 부상하고 있다.
- 2. 기존 방법은 프롬프트 템플릿의 블랙박스 조작에 의존하여 해석 가능성과 일반화가 제한적이다.
- 3. 연구에서는 방어 임계값 감쇠(DTD) 개념을 도입하여 LLM의 무해한 생성이 안전에 미치는 잠재적 영향을 밝혀냈다.
- 4. "의미 반전" 전략을 사용하는 Sugar-Coated Poison(SCP) 공격 패러다임을 제안하여, 모델이 안전 메커니즘을 우회하도록 유도한다.
- 5. SCP는 기존 기준을 능가하며, 여섯 개의 LLM에서 평균 87.23%의 공격 성공률을 달성했다. 방어를 위해 동사-명사 의존성을 활용한 품사 방어(POSD)를 제안한다.


---

*Generated on 2025-09-24 04:15:59*