<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:11:52.861860",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Adversarial Examples",
    "Domain Generalization",
    "Jailbreaking Large Language Models",
    "Deep Learning"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Adversarial Examples": 0.78,
    "Domain Generalization": 0.79,
    "Jailbreaking Large Language Models": 0.81,
    "Deep Learning": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "adversarial examples",
        "canonical": "Adversarial Examples",
        "aliases": [
          "adversarial attacks"
        ],
        "category": "specific_connectable",
        "rationale": "Adversarial examples are crucial for understanding vulnerabilities in deep learning models, linking to robustness strategies.",
        "novelty_score": 0.65,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "domain generalization",
        "canonical": "Domain Generalization",
        "aliases": [
          "distribution generalization"
        ],
        "category": "specific_connectable",
        "rationale": "Domain generalization is key for training models that perform well on unseen data, enhancing cross-domain learning links.",
        "novelty_score": 0.68,
        "connectivity_score": 0.82,
        "specificity_score": 0.77,
        "link_intent_score": 0.79
      },
      {
        "surface": "jailbreaking large language models",
        "canonical": "Jailbreaking Large Language Models",
        "aliases": [
          "LLM jailbreaking"
        ],
        "category": "unique_technical",
        "rationale": "This concept is emerging as a critical area of study for ensuring the ethical use of language models.",
        "novelty_score": 0.72,
        "connectivity_score": 0.78,
        "specificity_score": 0.85,
        "link_intent_score": 0.81
      },
      {
        "surface": "deep learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep learning is a foundational concept that connects various advanced topics in the paper.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "robustness properties",
      "training paradigms",
      "certification algorithms"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "adversarial examples",
      "resolved_canonical": "Adversarial Examples",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "domain generalization",
      "resolved_canonical": "Domain Generalization",
      "decision": "linked",
      "scores": {
        "novelty": 0.68,
        "connectivity": 0.82,
        "specificity": 0.77,
        "link_intent": 0.79
      }
    },
    {
      "candidate_surface": "jailbreaking large language models",
      "resolved_canonical": "Jailbreaking Large Language Models",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.78,
        "specificity": 0.85,
        "link_intent": 0.81
      }
    },
    {
      "candidate_surface": "deep learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# Algorithms for Adversarially Robust Deep Learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2509.19100.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2509.19100](https://arxiv.org/abs/2509.19100)

## 🔗 유사한 논문
- [[2025-09-23/Sugar-Coated Poison_ Benign Generation Unlocks LLM Jailbreaking_20250923|Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking]] (88.7% similar)
- [[2025-09-23/Large Language Models for Cyber Security_ A Systematic Literature Review_20250923|Large Language Models for Cyber Security: A Systematic Literature Review]] (87.3% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (85.5% similar)
- [[2025-09-23/Reasoning-to-Defend_ Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking_20250923|Reasoning-to-Defend: Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking]] (85.4% similar)
- [[2025-09-22/Activation Space Interventions Can Be Transferred Between Large Language Models_20250922|Activation Space Interventions Can Be Transferred Between Large Language Models]] (85.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Adversarial Examples|Adversarial Examples]], [[keywords/Domain Generalization|Domain Generalization]]
**⚡ Unique Technical**: [[keywords/Jailbreaking Large Language Models|Jailbreaking Large Language Models]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.19100v1 Announce Type: cross 
Abstract: Given the widespread use of deep learning models in safety-critical applications, ensuring that the decisions of such models are robust against adversarial exploitation is of fundamental importance. In this thesis, we discuss recent progress toward designing algorithms that exhibit desirable robustness properties. First, we discuss the problem of adversarial examples in computer vision, for which we introduce new technical results, training paradigms, and certification algorithms. Next, we consider the problem of domain generalization, wherein the task is to train neural networks to generalize from a family of training distributions to unseen test distributions. We present new algorithms that achieve state-of-the-art generalization in medical imaging, molecular identification, and image classification. Finally, we study the setting of jailbreaking large language models (LLMs), wherein an adversarial user attempts to design prompts that elicit objectionable content from an LLM. We propose new attacks and defenses, which represent the frontier of progress toward designing robust language-based agents.

## 📝 요약

이 논문은 안전이 중요한 응용 분야에서 딥러닝 모델의 결정이 적대적 공격에 대해 견고하도록 보장하는 방법을 연구합니다. 먼저, 컴퓨터 비전에서의 적대적 예제 문제를 다루며, 새로운 기술 결과, 훈련 패러다임, 인증 알고리즘을 제시합니다. 또한, 도메인 일반화 문제를 다루어, 의료 영상, 분자 식별, 이미지 분류에서 최첨단 일반화를 달성하는 새로운 알고리즘을 소개합니다. 마지막으로, 대형 언어 모델(LLM)의 탈옥 상황을 연구하여, 적대적 사용자가 LLM에서 부적절한 콘텐츠를 유도하는 프롬프트를 설계하는 문제를 다루고, 이에 대한 새로운 공격 및 방어 방법을 제안합니다.

## 🎯 주요 포인트

- 1. 안전이 중요한 응용 분야에서 딥러닝 모델의 결정이 적대적 공격에 대해 견고하도록 보장하는 것이 중요하다.
- 2. 컴퓨터 비전에서 적대적 예제 문제를 해결하기 위한 새로운 기술 결과, 훈련 패러다임, 인증 알고리즘을 소개한다.
- 3. 도메인 일반화 문제를 다루며, 새로운 알고리즘을 통해 의료 영상, 분자 식별, 이미지 분류에서 최첨단 일반화를 달성한다.
- 4. 대형 언어 모델(LLM)의 탈옥 상황을 연구하며, 적대적 사용자가 LLM에서 반대되는 콘텐츠를 유도하는 프롬프트를 설계하는 문제를 다룬다.
- 5. 견고한 언어 기반 에이전트를 설계하기 위한 새로운 공격 및 방어 방법을 제안한다.


---

*Generated on 2025-09-24 14:11:52*