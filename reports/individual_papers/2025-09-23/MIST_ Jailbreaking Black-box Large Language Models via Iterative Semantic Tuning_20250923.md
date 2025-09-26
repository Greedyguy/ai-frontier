---
keywords:
  - Large Language Model
  - Iterative Semantic Tuning
  - Jailbreak Attacks
  - Sequential Synonym Search
category: cs.AI
publish_date: 2025-09-23
arxiv_id: 2506.16792
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T01:08:01.303780",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Iterative Semantic Tuning",
    "Jailbreak Attacks",
    "Sequential Synonym Search"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Iterative Semantic Tuning": 0.9,
    "Jailbreak Attacks": 0.88,
    "Sequential Synonym Search": 0.8
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
        "rationale": "Connects to a broad range of discussions around language model capabilities and vulnerabilities.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.5,
        "link_intent_score": 0.85
      },
      {
        "surface": "Iterative Semantic Tuning",
        "canonical": "Iterative Semantic Tuning",
        "aliases": [
          "MIST"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel method specific to the paper's contribution, enhancing discussions on model manipulation techniques.",
        "novelty_score": 0.85,
        "connectivity_score": 0.6,
        "specificity_score": 0.8,
        "link_intent_score": 0.9
      },
      {
        "surface": "Jailbreak Attacks",
        "canonical": "Jailbreak Attacks",
        "aliases": [
          "jailbreaking"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights a critical area of research in model security and ethical AI, relevant to ongoing discussions.",
        "novelty_score": 0.7,
        "connectivity_score": 0.75,
        "specificity_score": 0.85,
        "link_intent_score": 0.88
      },
      {
        "surface": "Sequential Synonym Search",
        "canonical": "Sequential Synonym Search",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Represents a specific technique within the proposed method, useful for detailed technical discussions.",
        "novelty_score": 0.65,
        "connectivity_score": 0.55,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
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
        "specificity": 0.5,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Iterative Semantic Tuning",
      "resolved_canonical": "Iterative Semantic Tuning",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.6,
        "specificity": 0.8,
        "link_intent": 0.9
      }
    },
    {
      "candidate_surface": "Jailbreak Attacks",
      "resolved_canonical": "Jailbreak Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.75,
        "specificity": 0.85,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "Sequential Synonym Search",
      "resolved_canonical": "Sequential Synonym Search",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.55,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# MIST: Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2506.16792.pdf)
**Category**: cs.AI
**Published**: 2025-09-23
**ArXiv ID**: [2506.16792](https://arxiv.org/abs/2506.16792)

## 🔗 유사한 논문
- [[2025-09-23/FC-Attack_ Jailbreaking Multimodal Large Language Models via Auto-Generated Flowcharts_20250923|FC-Attack: Jailbreaking Multimodal Large Language Models via Auto-Generated Flowcharts]] (86.1% similar)
- [[2025-09-18/MUSE_ MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models_20250918|MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models]] (85.8% similar)
- [[2025-09-18/LLM Jailbreak Detection for (Almost) Free!_20250918|LLM Jailbreak Detection for (Almost) Free!]] (85.3% similar)
- [[2025-09-22/SABER_ Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection_20250922|SABER: Uncovering Vulnerabilities in Safety Alignment via Cross-Layer Residual Connection]] (85.1% similar)
- [[2025-09-23/Targeting Alignment_ Extracting Safety Classifiers of Aligned LLMs_20250923|Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs]] (85.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Jailbreak Attacks|Jailbreak Attacks]]
**⚡ Unique Technical**: [[keywords/Iterative Semantic Tuning|Iterative Semantic Tuning]], [[keywords/Sequential Synonym Search|Sequential Synonym Search]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.16792v3 Announce Type: replace-cross 
Abstract: Despite efforts to align large language models (LLMs) with societal and moral values, these models remain susceptible to jailbreak attacks -- methods designed to elicit harmful responses. Jailbreaking black-box LLMs is considered challenging due to the discrete nature of token inputs, restricted access to the target LLM, and limited query budget. To address the issues above, we propose an effective method for jailbreaking black-box large language Models via Iterative Semantic Tuning, named MIST. MIST enables attackers to iteratively refine prompts that preserve the original semantic intent while inducing harmful content. Specifically, to balance semantic similarity with computational efficiency, MIST incorporates two key strategies: sequential synonym search, and its advanced version -- order-determining optimization. We conduct extensive experiments on two datasets using two open-source and four closed-source models. Results show that MIST achieves competitive attack success rate, relatively low query count, and fair transferability, outperforming or matching state-of-the-art jailbreak methods. Additionally, we conduct analysis on computational efficiency to validate the practical viability of MIST.

## 📝 요약

이 논문은 대형 언어 모델(LLM)의 사회적, 도덕적 가치 정렬에도 불구하고 여전히 유해한 응답을 유도하는 탈옥 공격에 취약하다는 문제를 다룹니다. 특히, 블랙박스 LLM의 탈옥은 토큰 입력의 이산적 특성과 제한된 접근성, 쿼리 예산의 한계로 인해 어려운 과제로 여겨집니다. 이를 해결하기 위해, 저자들은 MIST라는 반복적 의미 조정을 통한 효과적인 탈옥 방법을 제안합니다. MIST는 원래의 의미를 유지하면서 유해한 콘텐츠를 유도하는 프롬프트를 반복적으로 개선할 수 있게 합니다. 이 방법은 순차적 동의어 검색과 순서 결정 최적화라는 두 가지 전략을 포함하여 의미 유사성과 계산 효율성을 균형 있게 유지합니다. 두 개의 데이터셋과 여섯 개의 모델을 사용한 실험 결과, MIST는 경쟁력 있는 공격 성공률과 낮은 쿼리 수, 그리고 양호한 전이성을 보여주며, 기존의 탈옥 방법을 능가하거나 대등한 성능을 보였습니다. 또한, 계산 효율성 분석을 통해 MIST의 실용성을 검증했습니다.

## 🎯 주요 포인트

- 1. 대형 언어 모델(LLM)은 사회적 및 도덕적 가치에 맞추려는 노력에도 불구하고 여전히 유해한 응답을 유도하는 탈옥 공격에 취약하다.
- 2. MIST는 반복적 의미 조정을 통해 블랙박스 대형 언어 모델을 탈옥하는 효과적인 방법으로, 원래의 의미적 의도를 유지하면서 유해한 콘텐츠를 유도하는 프롬프트를 정교하게 조정한다.
- 3. MIST는 의미적 유사성과 계산 효율성을 균형 있게 유지하기 위해 순차적 동의어 검색과 순서 결정 최적화라는 두 가지 핵심 전략을 포함한다.
- 4. 두 개의 데이터셋과 여섯 개의 모델을 사용한 실험 결과, MIST는 경쟁력 있는 공격 성공률과 낮은 쿼리 수, 그리고 공정한 전이성을 보여주며 최신 탈옥 방법을 능가하거나 동등한 성능을 보인다.
- 5. MIST의 실용적 가능성을 검증하기 위해 계산 효율성에 대한 추가 분석을 수행했다.


---

*Generated on 2025-09-24 01:08:01*