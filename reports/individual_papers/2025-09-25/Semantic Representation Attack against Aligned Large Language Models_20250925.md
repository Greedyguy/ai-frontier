---
keywords:
  - Large Language Model
  - Semantic Representation Attack
  - Semantic Representation Heuristic Search
category: cs.AI
publish_date: 2025-09-25
arxiv_id: 2509.19360
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-25T15:29:43.231312",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Semantic Representation Attack",
    "Semantic Representation Heuristic Search"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Semantic Representation Attack": 0.8,
    "Semantic Representation Heuristic Search": 0.78
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
        "rationale": "Central to the paper's focus on adversarial attacks, linking to existing work on LLMs.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Semantic Representation Attack",
        "canonical": "Semantic Representation Attack",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Introduces a novel attack method specific to the paper, enhancing understanding of new adversarial techniques.",
        "novelty_score": 0.95,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Semantic Representation Heuristic Search",
        "canonical": "Semantic Representation Heuristic Search",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "A specific algorithm proposed in the paper, crucial for understanding the implementation of the attack.",
        "novelty_score": 0.92,
        "connectivity_score": 0.55,
        "specificity_score": 0.88,
        "link_intent_score": 0.78
      }
    ],
    "ban_list_suggestions": [
      "attack success rates",
      "harmful outputs",
      "prompt naturalness"
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
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Semantic Representation Attack",
      "resolved_canonical": "Semantic Representation Attack",
      "decision": "linked",
      "scores": {
        "novelty": 0.95,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Semantic Representation Heuristic Search",
      "resolved_canonical": "Semantic Representation Heuristic Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.92,
        "connectivity": 0.55,
        "specificity": 0.88,
        "link_intent": 0.78
      }
    }
  ]
}
-->

# Semantic Representation Attack against Aligned Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19360.pdf)
**Category**: cs.AI
**Published**: 2025-09-25
**ArXiv ID**: [2509.19360](https://arxiv.org/abs/2509.19360)

## 🔗 유사한 논문
- [[2025-09-23/Sugar-Coated Poison_ Benign Generation Unlocks LLM Jailbreaking_20250923|Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking]] (90.0% similar)
- [[2025-09-23/Targeting Alignment_ Extracting Safety Classifiers of Aligned LLMs_20250923|Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs]] (87.7% similar)
- [[2025-09-23/MIST_ Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning_20250923|MIST: Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning]] (86.9% similar)
- [[2025-09-23/Revisiting Backdoor Attacks on LLMs_ A Stealthy and Practical Poisoning Framework via Harmless Inputs_20250923|Revisiting Backdoor Attacks on LLMs: A Stealthy and Practical Poisoning Framework via Harmless Inputs]] (86.7% similar)
- [[2025-09-22/SABER_ Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection_20250922|SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection]] (86.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Semantic Representation Attack|Semantic Representation Attack]], [[keywords/Semantic Representation Heuristic Search|Semantic Representation Heuristic Search]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19360v1 Announce Type: cross 
Abstract: Large Language Models (LLMs) increasingly employ alignment techniques to prevent harmful outputs. Despite these safeguards, attackers can circumvent them by crafting prompts that induce LLMs to generate harmful content.
  Current methods typically target exact affirmative responses, such as ``Sure, here is...'', suffering from limited convergence, unnatural prompts, and high computational costs.
  We introduce Semantic Representation Attack, a novel paradigm that fundamentally reconceptualizes adversarial objectives against aligned LLMs.
  Rather than targeting exact textual patterns, our approach exploits the semantic representation space comprising diverse responses with equivalent harmful meanings.
  This innovation resolves the inherent trade-off between attack efficacy and prompt naturalness that plagues existing methods.
  The Semantic Representation Heuristic Search algorithm is proposed to efficiently generate semantically coherent and concise adversarial prompts by maintaining interpretability during incremental expansion.
  We establish rigorous theoretical guarantees for semantic convergence and demonstrate that our method achieves unprecedented attack success rates (89.41\% averaged across 18 LLMs, including 100\% on 11 models) while maintaining stealthiness and efficiency.
  Comprehensive experimental results confirm the overall superiority of our Semantic Representation Attack.
  The code will be publicly available.

## 📝 요약

이 논문은 대형 언어 모델(LLMs)의 정렬 기법을 우회하여 유해한 출력을 생성하는 새로운 공격 방법인 '의미 표현 공격'을 제안합니다. 기존 방법은 특정 문구를 목표로 하여 제한된 수렴성과 높은 계산 비용 문제를 겪었습니다. 반면, 제안된 방법은 다양한 유해 의미를 가진 응답의 의미 표현 공간을 활용하여 공격 효과와 자연스러운 프롬프트 간의 균형을 해결합니다. '의미 표현 휴리스틱 검색 알고리즘'을 통해 해석 가능성을 유지하면서 효율적인 공격 프롬프트를 생성합니다. 이 방법은 18개의 LLM에서 평균 89.41%의 높은 공격 성공률을 기록하며, 11개 모델에서는 100%의 성공률을 달성했습니다. 실험 결과는 제안된 방법의 우수성을 입증하며, 코드는 공개될 예정입니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLMs)의 정렬 기술을 우회하는 새로운 공격 패러다임인 'Semantic Representation Attack'을 소개합니다.
- 2. 기존의 정확한 텍스트 패턴을 목표로 하는 방법 대신, 다양한 반응의 의미적 표현 공간을 활용하여 공격 목표를 재구성합니다.
- 3. 제안된 'Semantic Representation Heuristic Search' 알고리즘은 해석 가능성을 유지하면서 의미적으로 일관된 공격 프롬프트를 효율적으로 생성합니다.
- 4. 이 방법은 18개의 LLM에서 평균 89.41%, 11개의 모델에서 100%의 공격 성공률을 달성하며, 스텔스성과 효율성을 유지합니다.
- 5. 실험 결과는 'Semantic Representation Attack'의 전반적인 우수성을 확인하며, 코드도 공개될 예정입니다.


---

*Generated on 2025-09-25 15:29:43*