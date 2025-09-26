---
keywords:
  - Large Language Model
  - Gaslighting Attacks
  - Multimodal Learning
  - Adversarial Input
category: cs.CL
publish_date: 2025-09-25
arxiv_id: 2509.19858
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-26T08:45:46.614900",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Gaslighting Attacks",
    "Multimodal Learning",
    "Adversarial Input"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.78,
    "Gaslighting Attacks": 0.82,
    "Multimodal Learning": 0.79,
    "Adversarial Input": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Speech Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "Speech LLMs"
        ],
        "category": "broad_technical",
        "rationale": "Links to the broader concept of LLMs, crucial for understanding the context of speech-based AI.",
        "novelty_score": 0.45,
        "connectivity_score": 0.85,
        "specificity_score": 0.6,
        "link_intent_score": 0.78
      },
      {
        "surface": "Gaslighting Attacks",
        "canonical": "Gaslighting Attacks",
        "aliases": [
          "Manipulative Prompts"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel attack vector specific to speech models, enhancing understanding of adversarial strategies.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.82
      },
      {
        "surface": "Multimodal Robustness",
        "canonical": "Multimodal Learning",
        "aliases": [
          "Multimodal Resilience"
        ],
        "category": "specific_connectable",
        "rationale": "Connects to the trending concept of multimodal systems, relevant for evaluating model robustness.",
        "novelty_score": 0.55,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.79
      },
      {
        "surface": "Adversarial Input",
        "canonical": "Adversarial Input",
        "aliases": [
          "Adversarial Prompts"
        ],
        "category": "unique_technical",
        "rationale": "Highlights the challenge of adversarial manipulation in AI, linking to security considerations.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.75,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "performance degradation",
      "behavioral responses"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Speech Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.85,
        "specificity": 0.6,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Gaslighting Attacks",
      "resolved_canonical": "Gaslighting Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Multimodal Robustness",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "Adversarial Input",
      "resolved_canonical": "Adversarial Input",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.75,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Benchmarking Gaslighting Attacks Against Speech Large Language Models

## 📋 메타데이터

**Links**: [[daily_digest_20250925|20250925]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19858.pdf)
**Category**: cs.CL
**Published**: 2025-09-25
**ArXiv ID**: [2509.19858](https://arxiv.org/abs/2509.19858)

## 🔗 유사한 논문
- [[2025-09-23/Strategic Dishonesty Can Undermine AI Safety Evaluations of Frontier LLM_20250923|Strategic Dishonesty Can Undermine AI Safety Evaluations of Frontier LLM]] (86.0% similar)
- [[2025-09-25/Semantic Representation Attack against Aligned Large Language Models_20250925|Semantic Representation Attack against Aligned Large Language Models]] (85.8% similar)
- [[2025-09-23/Breaking the Reviewer_ Assessing the Vulnerability of Large Language Models in Automated Peer Review Under Textual Adversarial Attacks_20250923|Breaking the Reviewer: Assessing the Vulnerability of Large Language Models in Automated Peer Review Under Textual Adversarial Attacks]] (85.6% similar)
- [[2025-09-23/Sugar-Coated Poison_ Benign Generation Unlocks LLM Jailbreaking_20250923|Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking]] (85.5% similar)
- [[2025-09-23/Challenging the Evaluator_ LLM Sycophancy Under User Rebuttal_20250923|Challenging the Evaluator: LLM Sycophancy Under User Rebuttal]] (85.1% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Gaslighting Attacks|Gaslighting Attacks]], [[keywords/Adversarial Input|Adversarial Input]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19858v1 Announce Type: new 
Abstract: As Speech Large Language Models (Speech LLMs) become increasingly integrated into voice-based applications, ensuring their robustness against manipulative or adversarial input becomes critical. Although prior work has studied adversarial attacks in text-based LLMs and vision-language models, the unique cognitive and perceptual challenges of speech-based interaction remain underexplored. In contrast, speech presents inherent ambiguity, continuity, and perceptual diversity, which make adversarial attacks more difficult to detect. In this paper, we introduce gaslighting attacks, strategically crafted prompts designed to mislead, override, or distort model reasoning as a means to evaluate the vulnerability of Speech LLMs. Specifically, we construct five manipulation strategies: Anger, Cognitive Disruption, Sarcasm, Implicit, and Professional Negation, designed to test model robustness across varied tasks. It is worth noting that our framework captures both performance degradation and behavioral responses, including unsolicited apologies and refusals, to diagnose different dimensions of susceptibility. Moreover, acoustic perturbation experiments are conducted to assess multi-modal robustness. To quantify model vulnerability, comprehensive evaluation across 5 Speech and multi-modal LLMs on over 10,000 test samples from 5 diverse datasets reveals an average accuracy drop of 24.3% under the five gaslighting attacks, indicating significant behavioral vulnerability. These findings highlight the need for more resilient and trustworthy speech-based AI systems.

## 📝 요약

이 논문은 음성 기반 애플리케이션에서 사용되는 대형 언어 모델(Speech LLMs)의 취약성을 평가하기 위해 고안된 '가스라이팅 공격'을 소개합니다. 이러한 공격은 모델의 추론을 오도하거나 왜곡하는 전략적 프롬프트로 구성되며, 분노, 인지적 혼란, 풍자, 암시, 전문적 부정 등 다섯 가지 조작 전략을 통해 모델의 강건성을 테스트합니다. 연구는 5개의 다양한 데이터셋에서 10,000개 이상의 테스트 샘플을 사용하여 5개의 음성 및 멀티모달 LLM에 대한 종합 평가를 수행했으며, 평균 정확도가 24.3% 감소하는 것으로 나타났습니다. 이는 음성 기반 AI 시스템의 신뢰성과 강건성을 높일 필요성을 강조합니다.

## 🎯 주요 포인트

- 1. 음성 기반 애플리케이션에서 Speech LLMs의 조작 및 적대적 입력에 대한 강인성을 확보하는 것이 중요합니다.
- 2. 음성은 고유의 모호성과 연속성, 지각적 다양성을 지니고 있어 적대적 공격을 탐지하기 어렵습니다.
- 3. 본 논문에서는 Speech LLMs의 취약성을 평가하기 위해 모델의 추론을 오도하는 '가스라이팅 공격'을 소개합니다.
- 4. 다섯 가지 조작 전략(분노, 인지적 혼란, 풍자, 암시, 전문적 부정)을 통해 모델의 강인성을 다양한 작업에서 테스트합니다.
- 5. 5개의 Speech 및 멀티모달 LLMs에 대한 평가 결과, 가스라이팅 공격 시 평균 정확도가 24.3% 감소하여 모델의 행동적 취약성을 드러냅니다.


---

*Generated on 2025-09-26 08:45:46*